from helpers.engine.CfgQueryParameterRestController import CfgQueryParameterRestController
from utilities.genericUtilities import *

obj_auth = CfgQueryParameterRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

