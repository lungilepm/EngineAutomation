from helpers.engine.CfgScheduleRestController import CfgScheduleRestController
from utilities.genericUtilities import *

obj_auth = CfgScheduleRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

