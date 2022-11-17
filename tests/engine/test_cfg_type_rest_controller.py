from helpers.engine.CfgTypeRestController import CfgTypeRestController
from utilities.genericUtilities import *

obj_auth = CfgTypeRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

