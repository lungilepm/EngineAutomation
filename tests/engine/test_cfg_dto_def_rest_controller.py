from helpers.engine.CfgDtoDefRestController import CfgDtoDefRestController
from utilities.genericUtilities import *

obj_auth = CfgDtoDefRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

