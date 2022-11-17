from helpers.engine.CfgFeSqlRestController import CfgFeSqlRestController
from utilities.genericUtilities import *

obj_auth = CfgFeSqlRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

