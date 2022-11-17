from helpers.engine.CfgFeEntityDependRestController import CfgFeEntityDependRestController
from utilities.genericUtilities import *

obj_auth = CfgFeEntityDependRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

