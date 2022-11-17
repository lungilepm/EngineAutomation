from helpers.engine.CallOutRestController import CallOutRestController
from utilities.genericUtilities import *

obj_auth = CallOutRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

