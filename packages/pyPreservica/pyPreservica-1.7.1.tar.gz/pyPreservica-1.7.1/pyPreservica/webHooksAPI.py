
from pyPreservica.common import *

logger = logging.getLogger(__name__)

BASE_ENDPOINT = '/api/webhook'


class TriggerType(Enum):
    """
    Enumeration of the Web hooks Trigger Types
    """
    MOVED = "MOVED"
    INDEXED = "FULL_TEXT_INDEXED"


class WebHooksAPI(AuthenticatedAPI):

    def subscriptions(self):
        """
        Return all the current active web hook subscriptions

        :return: list of web hooks
        """
        self._check_if_user_has_manager_role()
        headers = {HEADER_TOKEN: self.token}
        response = self.session.get(f'{self.protocol}://{self.server}{BASE_ENDPOINT}/subscriptions', headers=headers)
        if response.status_code == requests.codes.ok:
            json_response = str(response.content.decode('utf-8'))
            print(json_response)

    def un_subscribe(self, subscription_id: str):
        """

        :param subscription_id:
        :return:
        """
        self._check_if_user_has_manager_role()
        headers = {HEADER_TOKEN: self.token}
        response = self.session.delete(
            f'{self.protocol}://{self.server}{BASE_ENDPOINT}/subscriptions/{subscription_id}',
            headers=headers)
        print(response.status_code)

    def subscribe(self, url: str, triggerType: TriggerType, secret: str):
        """
        Subscribe to a new web hook

        :param url:
        :param triggerType:
        :param secret:
        :return:
        """
        self._check_if_user_has_manager_role()
        headers = {HEADER_TOKEN: self.token, 'Accept': 'application/json', 'Content-Type': 'application/json'}

        json_payload = '{"serialVersionUID": 0,   "url": "' + url + '", "triggerType": "' + triggerType.value + '", "secret": "' + secret + '",  "filters" : [],  "includeIdentifiers": "true"}'

        print(json.dumps(json.loads(json_payload)))

        response = self.session.post(f'{self.protocol}://{self.server}{BASE_ENDPOINT}/subscriptions', headers=headers,
                                     data=json.dumps(json.loads(json_payload)))

        print(response.status_code)
        print(response.text)
