from helpers.engine.CfgConstraintRestController import CfgConstraintRestController
from utilities.genericUtilities import *

obj_auth = CfgConstraintRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

