from helpers.engine.CfgEntityAttributeRestController import CfgEntityAttributeRestController
from utilities.genericUtilities import *

obj_auth = CfgEntityAttributeRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

