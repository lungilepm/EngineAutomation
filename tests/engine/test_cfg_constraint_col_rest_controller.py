from helpers.engine.CfgConstraintColRestController import CfgConstraintColRestController
from utilities.genericUtilities import *

obj_auth = CfgConstraintColRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

