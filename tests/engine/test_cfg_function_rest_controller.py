from helpers.engine.CfgFunctionRestController import CfgFunctionRestController
from utilities.genericUtilities import *

obj_auth = CfgFunctionRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

