from helpers.engine.DefaultHealthController import DefaultHealthController
from utilities.genericUtilities import *

obj_auth = DefaultHealthController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

