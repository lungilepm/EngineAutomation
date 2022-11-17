from helpers.engine.CfgSynonymRestController import CfgSynonymRestController
from utilities.genericUtilities import *

obj_auth = CfgSynonymRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

