import logging as logger
import os

from faker import Faker

from configs.hosts_config import INT_HOST


def generate_username():
    email = INT_HOST[os.environ.get('ENV', 'email')]
    logger.debug("Generating random username")
    faker = Faker()
    name = faker.first_name() + "Test"
    surname = faker.last_name() + "Test"
    person_info = {'name': name, 'surname': surname, 'email': email}
    # import pdb
    # pdb.set_trace()
    logger.debug(f"Randomly generated username: {person_info}")
    return person_info
