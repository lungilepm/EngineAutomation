from helpers.engine.CfgSequenceRestController import CfgSequenceRestController
from utilities.genericUtilities import *

obj_auth = CfgSequenceRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

