from helpers.engine.RabbitMqrestController import RabbitMqrestController
from utilities.genericUtilities import *

obj_auth = RabbitMqrestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

