from helpers.engine.CfgActivityReactiveController import CfgActivityReactiveController
from utilities.genericUtilities import *

obj_auth = CfgActivityReactiveController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

