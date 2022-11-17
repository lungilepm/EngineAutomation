from helpers.engine.GeneratedNumberRestController import GeneratedNumberRestController
from utilities.genericUtilities import *

obj_auth = GeneratedNumberRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

