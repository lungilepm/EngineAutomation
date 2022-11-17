from helpers.engine.CfgGenRespRestController import CfgGenRespRestController
from utilities.genericUtilities import *

obj_auth = CfgGenRespRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

