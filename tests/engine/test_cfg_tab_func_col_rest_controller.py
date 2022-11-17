from helpers.engine.CfgTabFuncColRestController import CfgTabFuncColRestController
from utilities.genericUtilities import *

obj_auth = CfgTabFuncColRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

