from helpers.engine.CfgScheduleCrudController import CfgScheduleCrudController
from utilities.genericUtilities import *

obj_auth = CfgScheduleCrudController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

