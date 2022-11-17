from helpers.engine.ForwardEngineeringController import ForwardEngineeringController
from utilities.genericUtilities import *

obj_auth = ForwardEngineeringController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

