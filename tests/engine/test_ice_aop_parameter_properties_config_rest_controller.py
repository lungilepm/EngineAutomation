from helpers.engine.IceAopParameterPropertiesConfigRestController import IceAopParameterPropertiesConfigRestController
from utilities.genericUtilities import *

obj_auth = IceAopParameterPropertiesConfigRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

