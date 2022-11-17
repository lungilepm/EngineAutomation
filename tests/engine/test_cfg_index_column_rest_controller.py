from helpers.engine.CfgIndexColumnRestController import CfgIndexColumnRestController
from utilities.genericUtilities import *

obj_auth = CfgIndexColumnRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

