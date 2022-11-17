from helpers.engine.CfgTextRestController import CfgTextRestController
from utilities.genericUtilities import *

obj_auth = CfgTextRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

