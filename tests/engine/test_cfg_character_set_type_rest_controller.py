from helpers.engine.CfgCharacterSetTypeRestController import CfgCharacterSetTypeRestController
from utilities.genericUtilities import *

obj_auth = CfgCharacterSetTypeRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

