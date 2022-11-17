from helpers.engine.NumberServiceRestController import NumberServiceRestController
from utilities.genericUtilities import *

obj_auth = NumberServiceRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

