from helpers.engine.IceTransactionRecordController import IceTransactionRecordController
from utilities.genericUtilities import *

obj_auth = IceTransactionRecordController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

