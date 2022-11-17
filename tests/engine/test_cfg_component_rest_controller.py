from helpers.engine.CfgComponentRestController import CfgComponentRestController
from utilities.genericUtilities import *

obj_auth = CfgComponentRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

