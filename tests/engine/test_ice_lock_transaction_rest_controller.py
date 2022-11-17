from helpers.engine.IceLockTransactionRestController import IceLockTransactionRestController
from utilities.genericUtilities import *

obj_auth = IceLockTransactionRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

