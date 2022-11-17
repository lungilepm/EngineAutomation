from helpers.engine.CfgDtoDefParameterRestController import CfgDtoDefParameterRestController
from utilities.genericUtilities import *

obj_auth = CfgDtoDefParameterRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

