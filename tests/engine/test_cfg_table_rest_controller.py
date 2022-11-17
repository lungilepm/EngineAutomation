from helpers.engine.CfgTableRestController import CfgTableRestController
from utilities.genericUtilities import *

obj_auth = CfgTableRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

