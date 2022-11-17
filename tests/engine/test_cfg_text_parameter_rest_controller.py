from helpers.engine.CfgTextParameterRestController import CfgTextParameterRestController
from utilities.genericUtilities import *

obj_auth = CfgTextParameterRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

