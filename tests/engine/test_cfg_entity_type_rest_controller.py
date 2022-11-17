from helpers.engine.CfgEntityTypeRestController import CfgEntityTypeRestController
from utilities.genericUtilities import *

obj_auth = CfgEntityTypeRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

