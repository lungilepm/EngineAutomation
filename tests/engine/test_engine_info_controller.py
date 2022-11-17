from helpers.engine.EngineInfoController import EngineInfoController
from utilities.genericUtilities import *

obj_auth = EngineInfoController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

