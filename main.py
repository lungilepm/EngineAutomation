import regex

from utilities.genericUtilities import write_to_text


def stripper(part):
    tem = regex.sub(",", " ", part).strip()
    part = regex.sub(" ", ",", tem)
    return part


def if_noter(ray, name):
    noting = f"if not {ray}:\n \t\t{name}[\'{ray}\'] = INT_HOST[os.environ.get('ENV', \'{ray}\')]\n\t\n\t"
    return noting


def payload_maker(ray, flag_gem=False, ray2=None):
    if not flag_gem or ray == 'Authorization':
        pay = f"\'{ray}\':{ray},\t\n\t"
    else:
        pay = f"\'{ray}\':\'{ray2}\',\t\n\t"
    return pay


def return_reg(reg, the_line, oldsub=':', newsub='-', substitute=True, lowerCase=True, split=False):
    regline = (regex.search(reg, the_line).group().strip())
    regline = regex.sub("\"", "", regline)
    regline = regex.sub(" ", "", regline)
    regline = regex.sub(",", "", regline)
    if split:
        oldsub = oldsub.lower()
        regArray = regex.split(oldsub, regline)
        return regArray

    if substitute:
        regline = regex.sub(oldsub, newsub, regline)

    # Lower the case of the returned string
    if lowerCase:
        regline = regline.lower()

    return regline


def function_namer(reg, the_line):
    test_end = return_reg(reg, the_line, "&", substitute=False, lowerCase=False,
                          split=False)
    call_type = return_reg("(?<=request).*.(?=\s')", the_line, substitute=False, lowerCase=True,
                           split=False)
    # call_type
    name_test_function = "test_" + call_type + "_" + return_reg(reg, the_line, oldsub="/", newsub="_", substitute=True,
                                                                lowerCase=True,
                                                                split=False)
    name_helper = call_type + "_" + return_reg(reg, the_line, oldsub="/", newsub="_", substitute=True,
                                                                lowerCase=True,
                                                                split=False)+"_"+"helper"

    names = [test_end, call_type, name_test_function,  name_helper]
    # import pdb
    #
    # pdb.set_trace()
    return names


fpath = "resources\oauth_token"
file1 = open(fpath + ".txt", "r")  # read the testfile

name_function = ""
function_parameters = ""
parameters_payload = ""
if_not = ""
test_end = ""
file_content = file1.readlines()
headers = ""
params = ""
array2 = []
for line in file_content:
    # Creating parameters payload
    if regex.search("\?", line):
        tempar = return_reg("(?<=\?).*.(?=')", line, "&", substitute=False, lowerCase=True,
                            split=True)  # parameters such as token?grant_type=password&client_id=
        for x in tempar:
            para = regex.split("=", x)
            params = payload_maker(para[0], False) + params
            function_parameters = f"{para[0]}=None," + function_parameters  # create function parameters
            if_not = if_noter(para[0], 'parameters') + if_not

    # Creating endpoints and function names
    if regex.search("curl", line) and regex.search("\?", line):
        namer = function_namer("(?<=\.za/).*.(?=\?)", line)
        test_end = namer[0]
        call_type = namer[1]
        name_test_function = namer[2]
        name_helper = namer[3]

    elif regex.search("curl", line):
        namer = function_namer("(?<=\.za/).*.(?=')", line)
        test_end = namer[0]
        call_type = namer[1]
        name_test_function = namer[2]
        name_helper = namer[3]

    # Creating headers payload
    if regex.search("header", line):
        # headers['compress_token'] = 'true'
        temp = regex.search("(?<=\s').*.(?=')", line).group()  # find the headers of the call
        array = regex.split(": ", temp)  # split the name of header and the header
        headers = payload_maker(array[0], True, array[1]) + headers

    # creating headers body parameters and function parameters
    if regex.search("\"", line):
        array1 = return_reg("(?<=\").*.", line, substitute=True, lowerCase=True, split=True)
        function_parameters = f"{array1[0]}=None," + function_parameters
        parameters_payload = payload_maker(array1[0], False) + parameters_payload

        if_not = if_noter(array1[0], 'payload') + if_not

function_parameters = stripper(function_parameters)
parameters_payload = stripper(parameters_payload)
params = stripper(params)
headers = stripper(headers)

final = f"import os\n" \
        f"from configs.hosts_config import INT_INFO\n" \
        f"import logging as logger\n" \
        f"from tests.auth.test_token_controller import obj_auth\n\n\n" \
        f"def {name_helper}(self, {function_parameters}):\n" \
        f"\tAuthorization = f\"Bearer {{self.post_iceauth_oauth_token_helper()['access_token']}}\"\n" \
        f"\n\t# The headers of the request \n" \
        f"\theaders = " \
        f"{{\n\t{headers}}}\n\n" \
        f"\n\t# The parameters of {name_helper}\n" \
        f"\tparameters = " \
        f"{{\n\t{params}}}\n\n" \
        f"\n\t# The request payload of {name_helper}\n" \
        f"\tpayload = " \
        f"{{\n\t{parameters_payload}}}\n\n" \
        f"\t# Default values to be used\n" \
        f"\t{if_not}\n" \
        f"\tlogger.info(f\"Helper function for iceauth/api/v2/users/json Authentication: {{Authorization}}\\npayload :{{payload}}\\nparams :{{parameters}}\\nheaders :{{headers}}\")\n" \
        f"\tresponse = self.requests_utility.{call_type}(\'{test_end}\', payload=payload, headers=headers, params=parameters)\n" \
        f"\treturn response\n\n" \
        f"def {name_test_function}():\n" \
        f"\texpected_assert = 'Listed results'\n" \
        f"\tlogger.info(\"TEST: test {call_type}  call: {test_end}\")\n" \
        f"\tapi_info = obj_auth.{name_helper}()\n" \
        f"\tlogger.debug(f\"TEST: test {call_type} call {test_end} return payload: {{api_info}}\")\n" \
        f"\tactual_result = api_info['message']\n" \
        f"\tassert expected_assert == actual_result, f\"test failed to assert positive\"\n" \
        f"\tf\"Expected assert: {{expected_assert}} but actual: {{actual_result}}\"\n" \
        f"\tf\"TEST:test get call {test_end} return payload:{{api_info}}\") \n\tassert expected_assert in api_info[0], f\"test failed to assert positive\"\n\tf\"Expected assert:{{expected_assert}} but actual does not exist\""
file1.close()
write_to_text(file_path=fpath, to_write=final, file_type='py', mode='w')
