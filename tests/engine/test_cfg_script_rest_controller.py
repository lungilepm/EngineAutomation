from helpers.engine.CfgScriptRestController import CfgScriptRestController
from utilities.genericUtilities import *

obj_auth = CfgScriptRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

