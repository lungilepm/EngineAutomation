from helpers.engine.CfgQueryResponseRestController import CfgQueryResponseRestController
from utilities.genericUtilities import *

obj_auth = CfgQueryResponseRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

