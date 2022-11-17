from helpers.engine.AuthExternalApiController import AuthExternalApiController
from utilities.genericUtilities import *
from helpers.engine.AuthExternalApiController import AuthExternalApiController

from utilities.genericUtilities import *

obj_auth = AuthExternalApiController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

