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
                                               split=False) + "_" + "helper"

    names = [test_end, call_type, name_test_function, name_helper]

    return names


fpath = "resources\\"
file1 = open(fpath + "lister.txt", "r")  # read the testfile
name_class = "CFGActivityRestController"
name_function = "test_activity_rest_controller"

file_content = file1.readlines()

for line in file_content:
    print(line)
    temp = return_reg(line, line, oldsub="-", newsub="_", substitute=True, lowerCase=True, split=False).title()
    name_class = return_reg(temp, temp, oldsub="_", newsub="", substitute=True, lowerCase=False, split=False)
    name_function = "test_" + return_reg(line, line, oldsub="-", newsub="_", substitute=True, lowerCase=True,
                                         split=False)
    # import pdb
    #
    # pdb.set_trace()
    final = f"import os\n" \
            f"from configs.hosts_config import INT_HOST\n" \
            f"import logging as logger\n" \
            f"from helpers.auth.TokenController import TokenController\n" \
            f"from utilities.genericUtilities import generate_username, write_to_text\n" \
            f"from utilities.requestsUtility import RequestsUtility\n\n\n" \
            f"class {name_class}(object):\n\n" \
            f"\tdef __init__(self):\n" \
            f"\t\tself.requests_utility = RequestsUtility()\n" \
            f"\t\tself.token_controller = TokenController()\n" \
            f"\t\tself.userName = []\n"
    file1.close()

    write_to_text(file_path="\\helpers\\auth\\" + name_class, to_write=final, file_type='py', mode='w')

    testing = f"import pytest\n" \
              f"from configs.hosts_config import INT_HOST\n" \
              f"from helpers.engine.{name_class} import {name_class}\n" \
              f"from utilities.genericUtilities import *\n" \
              f"from utilities.genericUtilities import generate_username, write_to_text\n" \
              f"from utilities.requestsUtility import RequestsUtility\n\n\n" \
              f"obj_auth = {name_class}()\n" \
              f"agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] \n\n"

    file1.close()
    write_to_text(file_path="\\tests\\auth\\" + name_function, to_write=testing, file_type='py', mode='w')
