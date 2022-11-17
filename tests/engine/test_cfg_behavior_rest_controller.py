from helpers.engine.CfgBehaviorRestController import CfgBehaviorRestController
from utilities.genericUtilities import *

obj_auth = CfgBehaviorRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

