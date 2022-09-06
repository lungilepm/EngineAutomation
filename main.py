import regex

file1 = open("resources\oauth_token.txt", "r")  # read the testfile

name_function = ""
parameters = ""
parameters_payload = ""
if_not = ""
test_end = ""
file_content = file1.readlines()
headers = dict()
for line in file_content:
    if regex.search("curl", line):
        test_end = regex.search("(?<=\.za/).*.(?=')", line).group()
        name_function = "test_" + regex.sub("/", "_", test_end)
        name_helper = regex.sub("/", "_", test_end) + "_helper"

    if regex.search("header", line) and not regex.search("Bearer", line):
        temp = regex.search("(?<=\s').*.(?=')", line).group()
        array = regex.split(":", temp)
        headers[array[0]] = array[1].strip()

    else:
        print("coming")
        # headers[array[0]] = "\"Bearer\" "+"auth"


import pdb

pdb.set_trace()
parameters = ""
parameters_payload = ""
if_not = ""

# file1.write(f"\n\n\n    {name_function}({parameters}):\n" +
#
#             "payload = {\n" + parameters_payload +
#
#             "}\n" +
#             if_not + "\n" +
#             +"logger.info(f\"" + test_end + " payload :{payload}\")" +
#             "response = self.requests_utility.post(\'" + test_end + "\', payload=payload)" +
#             "return response)")
# file1.close()

# file1 = open("myfile.txt", "r")
# print("Output of Readlines after appending")
# print(file1.readlines())
# print()
# file1.close()
#
# # Write-Overwrites
# file1 = open("myfile.txt", "w")  # write mode
# file1.write("Tomorrow \n")
# file1.close()
#
# file1 = open("myfile.txt", "r")
# print("Output of Readlines after writing")
# print(file1.readlines())
# print()
# file1.close()
