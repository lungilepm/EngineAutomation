from helpers.engine.TransactionLogController import TransactionLogController
from utilities.genericUtilities import *

obj_auth = TransactionLogController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

