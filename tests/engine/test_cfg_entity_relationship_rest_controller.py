from helpers.engine.CfgEntityRelationshipRestController import CfgEntityRelationshipRestController
from utilities.genericUtilities import *

obj_auth = CfgEntityRelationshipRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

