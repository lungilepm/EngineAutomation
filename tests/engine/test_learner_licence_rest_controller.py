from helpers.engine.LearnerLicenceRestController import LearnerLicenceRestController
from utilities.genericUtilities import *

obj_auth = LearnerLicenceRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

