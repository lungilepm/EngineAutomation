from helpers.engine.CfgScheduleNotificationController import CfgScheduleNotificationController
from utilities.genericUtilities import *

obj_auth = CfgScheduleNotificationController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

