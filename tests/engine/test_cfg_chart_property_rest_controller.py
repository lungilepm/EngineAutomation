from helpers.engine.CfgChartPropertyRestController import CfgChartPropertyRestController
from utilities.genericUtilities import *

obj_auth = CfgChartPropertyRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

