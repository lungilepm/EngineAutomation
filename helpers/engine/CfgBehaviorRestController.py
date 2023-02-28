import os
import logging as logger
from configs.hosts_config import INT_HOST
from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility


class CfgBehaviorRestController(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    def post_engine_rest_behavior_helper(self, seq=None, parameter9=None, parameter8=None, parameter7=None,
                                         parameter6=None, parameter5=None, parameter4=None, parameter3=None,
                                         parameter2=None, parameter10=None, parameter1=None, messageCd=None,
                                         lastChangedD=None, lastChangedBy=None, frontEndInd=None, expireD=None,
                                         effectiveD=None, createdD=None, createdBy=None, conditionResult=None,
                                         cfgConditionId=None, cfgConditionEntity=None, cfgBehaviorId=None,
                                         behaviorCd=None, backEndInd=None, agencyId=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json'}

        # The parameters of post_engine_rest_behavior_helper
        parameters = {
        }

        # The request payload of post_engine_rest_behavior_helper
        payload = {
            'seq': seq,
            'parameter9': parameter9,
            'parameter8': parameter8,
            'parameter7': parameter7,
            'parameter6': parameter6,
            'parameter5': parameter5,
            'parameter4': parameter4,
            'parameter3': parameter3,
            'parameter2': parameter2,
            'parameter10': parameter10,
            'parameter1': parameter1,
            'messageCd': messageCd,
            'lastChangedD': lastChangedD,
            'lastChangedBy': lastChangedBy,
            'frontEndInd': frontEndInd,
            'expireD': expireD,
            'effectiveD': effectiveD,
            'createdD': createdD,
            'createdBy': createdBy,
            'conditionResult': conditionResult,
            'cfgConditionId': cfgConditionId,
            'cfgConditionEntity': cfgConditionEntity,
            'cfgBehaviorId': cfgBehaviorId,
            'behaviorCd': behaviorCd,
            'backEndInd': backEndInd,
            'agencyId': agencyId}

        # Default values to be used
        if not seq:
            payload['seq'] = INT_HOST[os.environ.get('ENV', 'seq')]

        if not parameter9:
            payload['parameter9'] = INT_HOST[os.environ.get('ENV', 'parameter9')]

        if not parameter8:
            payload['parameter8'] = INT_HOST[os.environ.get('ENV', 'parameter8')]

        if not parameter7:
            payload['parameter7'] = INT_HOST[os.environ.get('ENV', 'parameter7')]

        if not parameter6:
            payload['parameter6'] = INT_HOST[os.environ.get('ENV', 'parameter6')]

        if not parameter5:
            payload['parameter5'] = INT_HOST[os.environ.get('ENV', 'parameter5')]

        if not parameter4:
            payload['parameter4'] = INT_HOST[os.environ.get('ENV', 'parameter4')]

        if not parameter3:
            payload['parameter3'] = INT_HOST[os.environ.get('ENV', 'parameter3')]

        if not parameter2:
            payload['parameter2'] = INT_HOST[os.environ.get('ENV', 'parameter2')]

        if not parameter10:
            payload['parameter10'] = INT_HOST[os.environ.get('ENV', 'parameter10')]

        if not parameter1:
            payload['parameter1'] = INT_HOST[os.environ.get('ENV', 'parameter1')]

        if not messageCd:
            payload['messageCd'] = INT_HOST[os.environ.get('ENV', 'messageCd')]

        if not lastChangedD:
            payload['lastChangedD'] = INT_HOST[os.environ.get('ENV', 'lastChangedD')]

        if not lastChangedBy:
            payload['lastChangedBy'] = INT_HOST[os.environ.get('ENV', 'lastChangedBy')]

        if not frontEndInd:
            payload['frontEndInd'] = INT_HOST[os.environ.get('ENV', 'frontEndInd')]

        if not expireD:
            payload['expireD'] = INT_HOST[os.environ.get('ENV', 'expireD')]

        if not effectiveD:
            payload['effectiveD'] = INT_HOST[os.environ.get('ENV', 'effectiveD')]

        if not createdD:
            payload['createdD'] = INT_HOST[os.environ.get('ENV', 'createdD')]

        if not createdBy:
            payload['createdBy'] = INT_HOST[os.environ.get('ENV', 'createdBy')]

        if not conditionResult:
            payload['conditionResult'] = INT_HOST[os.environ.get('ENV', 'conditionResult')]

        if not cfgConditionId:
            payload['cfgConditionId'] = INT_HOST[os.environ.get('ENV', 'cfgConditionId')]

        if not cfgConditionEntity:
            payload['cfgConditionEntity'] = INT_HOST[os.environ.get('ENV', 'cfgConditionEntity')]

        if not cfgBehaviorId:
            payload['cfgBehaviorId'] = INT_HOST[os.environ.get('ENV', 'cfgBehaviorId')]

        if not behaviorCd:
            payload['behaviorCd'] = INT_HOST[os.environ.get('ENV', 'behaviorCd')]

        if not backEndInd:
            payload['backEndInd'] = INT_HOST[os.environ.get('ENV', 'backEndInd')]

        if not agencyId:
            payload['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('ENGINE/rest/behavior', payload=payload, headers=headers,
                                              params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response
