from helpers.engine.DataSourcePropertiesRestController import DataSourcePropertiesRestController
from utilities.genericUtilities import *

obj_auth = DataSourcePropertiesRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

