from helpers.engine.CfgNumberCompositionRestController import CfgNumberCompositionRestController
from utilities.genericUtilities import *

obj_auth = CfgNumberCompositionRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

