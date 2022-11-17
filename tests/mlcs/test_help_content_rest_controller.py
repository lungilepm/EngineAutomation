from helpers.engine.HelpContentRestController import HelpContentRestController
from utilities.genericUtilities import *

obj_auth = HelpContentRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

