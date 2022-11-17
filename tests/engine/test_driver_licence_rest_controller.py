from helpers.engine.DriverLicenceRestController import DriverLicenceRestController
from utilities.genericUtilities import *

obj_auth = DriverLicenceRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

