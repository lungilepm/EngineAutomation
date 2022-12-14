import configparser
import json
import logging as logger
import os
import random
from datetime import datetime
from os.path import exists

import oracledb
import pandas as pd
from faker import Faker

from configs.hosts_config import INT_HOST, read_doc

date = datetime.now().strftime("%d/%b/%y")
change = '75003'
TAXPAYEPIN = 'LU' + change + '000M'
IDNUMBER = change + '00'
SERIALNUMBER = IDNUMBER
CHASSIS_NUMBER = 'LUN' + change + 'NBI'
ENTRYNUMBER = '2022NRB' + change + '00'
PLATENUMBER = 'LUN' + change
fspath = 'C:\PycharmProjects\EngineAutomation'


def generate_username():
    email = INT_HOST[os.environ.get('ENV', 'mail')]
    logger.debug("Generating random username")
    faker = Faker()
    number_int = random.randint(1000, 9999)

    name = faker.first_name() + str(number_int)
    surname = faker.last_name() + "Test"
    person_info = {'name': name, 'surname': surname, 'email': email}

    logger.debug(f"Randomly generated username: {person_info}")
    return person_info


def write_to_text(file_path, to_write, file_type, mode):
    full_file = fspath + "\\" + file_path + "." + file_type
    if mode == "w":
        with open(full_file, mode="w") as file:
            file.write(to_write)


def write_to_json(file_path, to_write, mode):
    values = read_doc(file_path, "json")
    if len(values) < 1 or len(to_write) < 1:
        write_to_json_help(file_path, to_write, mode)
    else:
        for i, elem in enumerate(values):
            for j, term in enumerate(to_write):
                one = to_write[j]['username']
                two = values[i]['username']
                if one != two:
                    write_to_json_help(file_path, to_write, mode)


def write_to_json_help(file_path, to_write, mode):
    full_file = fspath + "\\" + file_path + ".json"
    dict_returned = to_write
    if mode == "a":
        we = json.dumps(dict_returned)
        with open(full_file, mode="w") as file:
            file.write(we)
        # import pdb
        #
        # pdb.set_trace()
    if mode == "w":
        if not exists(full_file):
            with open(full_file, mode="w") as file:
                file.write("[]")
        we = json.dumps(dict_returned)
        with open(full_file, mode="w") as file:
            file.write(we)


def find_index(mr_dict, content, element):
    indices = []
    for i, elem in enumerate(mr_dict):
        if elem[element] == content:
            indices.append(i)
    indices = list(dict.fromkeys(indices))
    # import pdb
    #
    # pdb.set_trace()
    return indices


def find_role(mr_dict):
    indices = []
    for i, elem in enumerate(mr_dict):
        indices.append(i)
    indices = list(dict.fromkeys(indices))
    return indices


def connect_to_database(environment):
    config = configparser.RawConfigParser()
    config.read('config.properties')
    user = INT_HOST[os.environ.get('ENV', 'usernamedb')]
    password = INT_HOST[os.environ.get('ENV', 'passworddb')]
    dsn = INT_HOST[os.environ.get('ENV', 'dsn')] + environment
    try:
        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        print(connection)
        return connection
    except oracledb.Error as Error:
        print(Error)
        return connection


def print_to_excel(sheet, connection, environment):
    sql_query = pd.read_sql_query(
        "select MOTHER_NAMES, ID_NUMBER, SERIAL_NUMBER, ENTRYNUMBER, CHASSIS_NUMBER, PIN from NTSABOMO" + environment
        + ".kra_simba inner join NTSABOMO" + environment
        + ".kra_pin_individual on NTSABOMO" + environment
        + ".kra_simba.PIN =NTSABOMO" + environment
        + ".kra_pin_individual.TAXPAYERPIN inner join NTSABOMO" + environment
        + ".NRB_ID on NTSABOMO" + environment
        + ".KRA_PIN_INDIVIDUAL.IDNUMBER=NTSABOMO" + environment
        + ".NRB_ID.ID_NUMBER where chassis_Number like '%LUN%' and REGISTRATION_STATUS_CD = 0",
        connection)
    df = pd.DataFrame(sql_query)
    print(df.info)
    filepath = 'TestData.xlsx'
    if not os.path.exists(filepath):
        df.to_excel(filepath, sheet_name=sheet, index=False)

    # Otherwise, add a sheet. Overwrite if there exists one with the same name.
    else:
        with pd.ExcelWriter(filepath, engine='openpyxl', if_sheet_exists='replace', mode='a') as writer:
            df.to_excel(writer, sheet_name=sheet, index=False)


def insert_nrb_id(environment):
    table = "NRB_ID"
    sqlText = "Insert into NTSABOMO" + environment + "." + table + " (ID_NUMBER,SERIAL_NUMBER,DATE_OF_ISSUE,FULL_NAMES,GENDER,DATE_OF_BIRTH,DISTRICT_OF_BIRTH,FATHER_NAMES,MOTHER_NAMES,ADDRESS)  values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)"

    connection = connect_to_database(environment)
    cursorObj = connection.cursor()
    try:
        cursorObj.execute(sqlText, (
            IDNUMBER, SERIALNUMBER, date, 'LUNGILE PEARL MOTSWENI', 'F', 19900109, 'NAKURU', 'LONDI', 'NOMSA',
            'PO BOX 12, NAIROBI'))
        connection.commit()
    except oracledb.Error as Error:
        print(Error)


def insert_kra_individual_pin(environment):
    table = 'KRA_PIN_INDIVIDUAL'
    sqlText = "Insert into NTSABOMO" + environment + "." + table + "(FIRSTNAME,TAXPAYERPIN,RTELNO,MPOBOX,STARTUPDATE,IDTYPE,IDNUMBER,POCODE,MIDDLENAME,MTOWN,LASTNAME) values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)"
    connection = connect_to_database(environment)
    cursorObj = connection.cursor()
    try:
        cursorObj.execute(sqlText, (
            'LUNGILE', TAXPAYEPIN, '072202004', 'PO BOX 12, NAIROBI', 20220806, 'ID', IDNUMBER, 1520, 'PEARL',
            'NAIROBI', 'MOTSWENI'))
        connection.commit()
    except oracledb.Error as Error:
        print(Error)


def insert_kra_simba(environment):
    sqlText = "Insert into NTSABOMO" + environment + ".KRA_SIMBA (ANDCL,CHASSIS_NUMBER,BURDCL,NUMDCL,IDMAKE,IDBODYTYPE,STATUS,PREVREGNUMBER,ENGNUMBER,IDNUMBER,IDMODEL,GAZNOTNUMBER,GAZNOTDATE,LOTNUMBER,AMNTAUCPAID,DRISIDE,AUCTYPE,TARWEIGHT,IDCOUNORIGIN,ENGINE_CAPACITY,YEAR_MANUFACTURE,RELEASEDATE,AMOUNT,PIN,IDVEHICLESOURCE,CPC,COUNTRYOFDESTINATION,BORDERPOINT,PLACEOFDISCHARGE,CODE602,CODE740,CODE601,CODE640,CODE722,CODE744,ENTRYNUMBER,REGISTRATION_STATUS_CD) values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19, :20, :21,:22, :23, :24, :25, :26, :27, :28, :29, :30, :31, :32, :33, :34, :35, :36 ,:37)"
    connection = connect_to_database(environment)
    cursorObj = connection.cursor()
    try:
        cursorObj.execute(sqlText, (
            '2022', CHASSIS_NUMBER, 'NBI', 875844, '18', 2, '0', None, '131742', PLATENUMBER, '0', 0, None,
            None, 0,
            '0', 0, 364, 'JP', 2500, 2010, date, None, TAXPAYEPIN, 9, 'C410', None, None, 'NAIROBI EXPORTS',
            2000, 5100, 0, 0, 0, 0, ENTRYNUMBER, '0'))
        connection.commit()
    except oracledb.Error as Error:
        print(Error)




# class TestDataManager:
#     env = ["DEV", "INT", "MAS", "TST"]
#     for x in env:
#         insert_nrb_id(x)
#         insert_kra_individual_pin(x)
#         insert_kra_simba(x)
#         connection = connect_to_database(x)
#         print_to_excel(x, connection, x)
