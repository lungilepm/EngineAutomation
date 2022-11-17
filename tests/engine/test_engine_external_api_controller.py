from helpers.engine.EngineExternalApiController import EngineExternalApiController
from utilities.genericUtilities import *

obj_auth = EngineExternalApiController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

