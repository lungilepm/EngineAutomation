from helpers.engine.CfgIndexRestController import CfgIndexRestController
from utilities.genericUtilities import *

obj_auth = CfgIndexRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

