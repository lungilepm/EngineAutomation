from helpers.engine.PropertiesConfigRestController import PropertiesConfigRestController
from utilities.genericUtilities import *

obj_auth = PropertiesConfigRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

