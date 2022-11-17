from helpers.engine.CfgConfigTestGroupController import CfgConfigTestGroupController
from utilities.genericUtilities import *

obj_auth = CfgConfigTestGroupController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

