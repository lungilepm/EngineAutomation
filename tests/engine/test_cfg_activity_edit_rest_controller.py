from helpers.engine.CfgActivityEditRestController import CfgActivityEditRestController
from utilities.genericUtilities import *

obj_auth = CfgActivityEditRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

