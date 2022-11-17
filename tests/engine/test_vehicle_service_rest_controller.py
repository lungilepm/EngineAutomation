from helpers.engine.VehicleServiceRestController import VehicleServiceRestController
from utilities.genericUtilities import *

obj_auth = VehicleServiceRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

