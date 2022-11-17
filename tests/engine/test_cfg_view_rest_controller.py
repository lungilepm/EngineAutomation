from helpers.engine.CfgViewRestController import CfgViewRestController
from utilities.genericUtilities import *

obj_auth = CfgViewRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

