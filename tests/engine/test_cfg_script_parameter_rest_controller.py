from helpers.engine.CfgScriptParameterRestController import CfgScriptParameterRestController
from utilities.genericUtilities import *

obj_auth = CfgScriptParameterRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

