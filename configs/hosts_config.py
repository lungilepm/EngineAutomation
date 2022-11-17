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
    option = read_doc("resources\envs", "json")
    if option[0]["doc"] == "int_zw":
        tun = read_doc("resources\int\int_zw", "json")
    # import pdb
    #
    # pdb.set_trace()
    return tun


INT_HOST = {
    "unallocated": "false",
    "includeChildren": "true",
    "force": "true",
    "addRoles": "true",
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
    "preferredLanguage": "en",
    "agencies": ["0"],
    "surname": 'Motsweni',
    "userMetaData": {},
    "baseRoles": ['SysAdmin', 'CFGTEMPLATE', 'System', 'AudAdmin', 'LookupAdmin', 'CFGADMIN', 'AuthAdmin', 'AppAdmin',
                  'CfgImporter', 'AuthUser'],
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
