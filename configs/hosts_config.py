import json

fspath = 'C:\PycharmProjects\EngineAutomation'


def read_doc(file_path, file_type):
    full_file = fspath + "\\" + file_path + "." + file_type
    dict_returned = dict
    if file_type == 'json':
        with open(full_file) as file:
            dict_returned = json.load(file)
    # import pdb
    #
    # pdb.set_trace()
    return dict_returned


def get_host():
    tun = dict
    enviro = ["dev", "int", "mas", "tst"]
    option = read_doc("resources\envs", "json")
    # This is the dev environment
    if option[0]["doc"] == "dev_zw":
        tun = read_doc("resources\\" + enviro[0] + "\\" + enviro[0] + "_zw", "json")

    if option[0]["doc"] == "dev_ke":
        tun = read_doc("resources\\" + enviro[0] + "\\" + enviro[0] + "_ke", "json")

    if option[0]["doc"] == "dev_ca_ke":
        tun = read_doc("resources\\" + enviro[0] + "\\" + enviro[0] + "_ca_ke", "json")
    if option[0]["doc"] == "dev_ca_zw":
        tun = read_doc("resources\\" + enviro[0] + "\\" + enviro[0] + "_ca_zw", "json")

    # This is the int environment
    if option[0]["doc"] == "int_zw":
        tun = read_doc("resources\\" + enviro[1] + "\\" + enviro[1] + "_zw", "json")

    if option[0]["doc"] == "int_ke":
        tun = read_doc("resources\\" + enviro[1] + "\\" + enviro[1] + "_ke", "json")

    if option[0]["doc"] == "int_ca_ke":
        tun = read_doc("resources\\" + enviro[1] + "\\" + enviro[1] + "_ca_ke", "json")
    if option[0]["doc"] == "int_ca_zw":
        tun = read_doc("resources\\" + enviro[1] + "\\" + enviro[1] + "_ca_zw", "json")

    # This is the mas environment
    if option[0]["doc"] == "mas_zw":
        tun = read_doc("resources\\" + enviro[2] + "\\" + enviro[2] + "_zw", "json")

    if option[0]["doc"] == "mas_ke":
        tun = read_doc("resources\\" + enviro[2] + "\\" + enviro[2] + "_ke", "json")

    if option[0]["doc"] == "mas_ca_ke":
        tun = read_doc("resources\\" + enviro[2] + "\\" + enviro[2] + "_ca_ke", "json")
    if option[0]["doc"] == "mas_ca_zw":
        tun = read_doc("resources\\" + enviro[2] + "\\" + enviro[2] + "_ca_zw", "json")

    # This is the tst environment
    if option[0]["doc"] == "tst_zw":
        tun = read_doc("resources\\" + enviro[3] + "\\" + enviro[3] + "_zw", "json")

    if option[0]["doc"] == "tst_ke":
        tun = read_doc("resources\\" + enviro[3] + "\\" + enviro[3] + "_ke", "json")

    if option[0]["doc"] == "tst_ca_ke":
        tun = read_doc("resources\\" + enviro[3] + "\\" + enviro[3] + "_ca_ke", "json")
    if option[0]["doc"] == "tst_ca_zw":
        tun = read_doc("resources\\" + enviro[3] + "\\" + enviro[3] + "_ca_zw", "json")
    # import pdb
    #
    # pdb.set_trace()
    return tun


INT_HOST = {
    "exportPOE": [True, False],
    "exportAuth": [True, False],
    "excludeAgencyParents": [True, False],
    "includeAgencyChildren": [True, False],
    "exportMLCS": [True, False],
    "exportENGINE": [True, False],
    "unallocated": False,
    "includeChildren": False,
    "force": False,
    "addRoles": True,
    "realm": get_host()['env']['realm'],
    "intzw": get_host()['env']['url'],
    "mail": "lungilem@icetech.io",
    "username": get_host()['user']['username'],
    "password": get_host()['user']['password'],
    "roles_path": "resources\\logRoles",
    "auth_token": None,
    "cellN": '0749953376',
    "name": 'Lungile',
    "initials": "LP",
    "organizationalUnit": "0",
    "language": "en",
    "agencies": get_host()['agencies'],
    "surname": 'Motsweni',
    "userMetaData": {},
    "baseRoles": ['SysAdmin', 'CFGTEMPLATE', 'System', 'AudAdmin', 'LookupAdmin', 'CFGADMIN', 'AuthAdmin', 'AppAdmin',
                  'CfgImporter', 'AuthUser', 'MaintainAccReg'],
    "grant_type": 'password',
    "client_id": 'client',
    "client_secret": 'password',
    "refresh_token": None,
    "new_username": None,
    "usernamedb": "LUNGILEMOTSWENI",
    "passworddb": "3230Ayanda#1",
    "dsn": "zayvdb08.spsi.co.za:1521/"
}

CONFLUENCE_HOST = {
    "username": "lungilem@icetech.io",
    "key": "Qa0xa95oNCFi9THaYdom7781",
    "confluenceUrl": "https://icetechprod03.atlassian.net/"
}
