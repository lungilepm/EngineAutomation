from helpers.engine.CfgNumberTypeRestController import CfgNumberTypeRestController
from utilities.genericUtilities import *

obj_auth = CfgNumberTypeRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

