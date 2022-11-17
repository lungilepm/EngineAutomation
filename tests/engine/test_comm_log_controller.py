from helpers.engine.CommLogController import CommLogController
from utilities.genericUtilities import *

obj_auth = CommLogController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

