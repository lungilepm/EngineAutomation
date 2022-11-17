from helpers.engine.CfgTabColumnRestController import CfgTabColumnRestController
from utilities.genericUtilities import *

obj_auth = CfgTabColumnRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

