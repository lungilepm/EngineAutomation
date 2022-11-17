from helpers.engine.CfgTriggerRestController import CfgTriggerRestController
from utilities.genericUtilities import *

obj_auth = CfgTriggerRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

