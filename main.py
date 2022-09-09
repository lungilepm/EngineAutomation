import json
import regex

fpath = "resources\oauth_token"
file1 = open(fpath + ".txt", "r")  # read the testfile

name_function = ""
function_parameters = ""
parameters_payload = ""
if_not = ""
test_end = ""
file_content = file1.readlines()
headers = dict()
params = ""
array2 = []
for line in file_content:
    # Creating parameters payload
    if regex.search("\?", line):
        temp = regex.search("(?<=\?).*.(?=')",
                            line).group().lower()  # parameters such as token?grant_type=password&client_id=
        tempar = regex.split("&", temp)  # split all the values of the parameters
        for x in tempar:
            para = regex.split("=", x)
            params = f"\'{para[0]}\':{para[0]},\t\n\t" + params
            function_parameters = f"{para[0]}=None, " + function_parameters  # create function parameters
            if_not = f"if not {para[0]}:\n \t\tpayload[\'{para[0]}\'] = INT_HOST[os.environ.get('ENV', \'{para[0]}\')]\n\t\n\t" + if_not
    # Creating endpoints and function names
    if regex.search("curl", line) and regex.search("\?", line):
        test_end = regex.search("(?<=\.za/).*.(?=\?)", line).group().lower()  # endpoint such as /ICEAUTH/oauth/token
        call_type = regex.search("(?<=request).*.(?=\s')",
                                 line).group().strip().lower()  # api call weather post/get/put
        temp = (call_type + "_" + regex.sub("/", "_", test_end)).lower()  # replace / with _ on the endpoint
        name_test_function = "test_" + temp  # create name of test function
        name_helper = "" + temp + "_helper"  # create name of helper function
    elif regex.search("curl", line):
        test_end = regex.search("(?<=\.za/).*.(?=')", line).group().lower()  # endpoint such as /ICEAUTH/oauth/token
        call_type = regex.search("(?<=request).*.(?=\s')",
                                 line).group().strip().lower()  # api call weather post/get/put
        temp = (call_type + "_" + regex.sub("/", "_", test_end)).lower()  # replace / with _ on the endpoint
        name_test_function = "test_" + temp  # create name of test function
        name_helper = "" + temp + "_helper"  # create name of helper function
    # Creating headers payload
    if regex.search("header", line) and not regex.search("Bearer", line):
        headers['compress_token'] = 'true'
        temp = regex.search("(?<=\s').*.(?=')", line).group().lower()  # find the headers of the call
        array = regex.split(":", temp)  # split the name of header and the header
        headers[array[0]] = array[1].strip()  # remove spaces

    elif regex.search("header", line) and regex.search("Bearer", line):
        print("coming")
        temp = regex.search("(?<=\s').*.(?=')", line).group().lower()  # find the headers of the call
        array = regex.split(":", temp)  # split the name of header and the header
        headers[array[0]] = 'bearer_auth'

    #creating body parameters and function parameters
    if regex.search("\"", line):
        temp = regex.search("(?<=\").*.", line).group()  # find the parameters
        temp = regex.sub(",", "", temp)  # remove the (, )
        temp = regex.sub("\"", "", temp)  # remove the (" )
        array1 = regex.split(":", temp)  # split the name of the parameters
        array2.append(array1[0])
        function_parameters = f"{array1[0]}=None, " + function_parameters
        parameters_payload = f"\'{array1[0]}\':{array1[0]},\t\n\t" + parameters_payload
        if_not = f"if not {array1[0]}:\n \t\tpayload[\'{array1[0]}\'] = INT_HOST[os.environ.get('ENV', \'{array1[0]}\')]\n\t\n\t" + if_not

function_parameters = regex.sub(", ", " ", function_parameters).strip()
function_parameters = regex.sub(" ", ",", function_parameters)

parameters_payload = regex.sub(",", " ", parameters_payload).strip()
parameters_payload = regex.sub(" ", ",", parameters_payload)

final = f"import os\n" \
        f"from configs.hosts_config import USER_INFO\n" \
        f"import logging as logger\n" \
        f"from tests.auth.test_token_controller import obj_auth\n\n\n" \
        f"def {name_helper}(self, {function_parameters}):\n" \
        f"\tauth = self.post_iceauth_oauth_token_helper()['access_token']\n" \
        f"\tbearer_auth = f'Bearer {{auth}}'\n" \
        f"\n\t# The headers of the request \n" \
        f"\theaders ={headers}\n" \
        f"\n\t# The parameters of {name_helper}\n" \
        f"\tparameters = " \
        f"{{\n\t{params}}}\n\n" \
        f"\n\t# The request payload of {name_helper}\n" \
        f"\tpayload = " \
        f"{{\n\t{parameters_payload}}}\n\n" \
        f"\t# Default values to be used\n" \
        f"\t{if_not}\n" \
        f"\tlogger.info(f\"Helper function for {test_end} payload :{{payload}}\")\n" \
        f"\tresponse = self.requests_utility.{call_type}(\'{test_end}\', payload=payload, headers=headers, params=parameters, auth=auth)\n" \
        f"\treturn response\n\n" \
        f"def {name_test_function}():\n" \
        f"\texpected_assert = 'Listed results'\n" \
        f"\tlogger.info(\"TEST: test {call_type}  call: {test_end}\")\n" \
        f"\tapi_info = obj_auth.{name_helper}()\n" \
        f"\tlogger.debug(f\"TEST: test {call_type} call {test_end} return payload: {{api_info}}\")\n" \
        f"\tactual_result = api_info['message']\n" \
        f"\tassert expected_assert == actual_result, f\"test failed to assert positive\"\n" \
        f"\tf\"Expected assert: {{expected_assert}} but actual: {{actual_result}}\"\n" \

file1.close()
f = open(fpath + "_made.py", "w")
f.write(final)
f.close()

import pdb

pdb.set_trace()
