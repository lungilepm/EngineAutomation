from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility


class CfgActivityEditRestController(object):

	def __init__(self):
		self.requests_utility = RequestsUtility()
		self.token_controller = TokenController()
		self.userName = []