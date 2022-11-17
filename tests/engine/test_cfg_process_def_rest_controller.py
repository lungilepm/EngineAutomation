from helpers.engine.CfgProcessDefRestController import CfgProcessDefRestController
from utilities.genericUtilities import *

obj_auth = CfgProcessDefRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

