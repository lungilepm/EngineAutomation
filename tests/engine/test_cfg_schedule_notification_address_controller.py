from helpers.engine.CfgScheduleNotificationAddressController import CfgScheduleNotificationAddressController
from utilities.genericUtilities import *

obj_auth = CfgScheduleNotificationAddressController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

