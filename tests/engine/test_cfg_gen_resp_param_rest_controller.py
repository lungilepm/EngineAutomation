from helpers.engine.CfgGenRespParamRestController import CfgGenRespParamRestController
from utilities.genericUtilities import *

obj_auth = CfgGenRespParamRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

