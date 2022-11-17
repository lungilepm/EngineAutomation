from helpers.engine.BasicErrorController import BasicErrorController
from utilities.genericUtilities import *

obj_auth = BasicErrorController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

