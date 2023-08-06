import json
import requests

from django.conf import settings


class PodleError(Exception):
    pass


class PodleUnprocessableEntityError(Exception):
    pass


class PodleGatewayTimeoutError(PodleError):
    pass


class PodleHttpClient:
    @staticmethod
    def make_request(url, method, data=None):
        # Build header
        access_token = settings.PODLE_AUTH_TOKEN
        headers = {
            "content-type": "application/json",
            "Authorization": "Bearer {}".format(access_token),
        }

        # Make HTTP request
        try:
            response = requests.request(method, url, json=data, headers=headers)
            result = response.text

            # Catch HTTP errors
            if response.status_code == 504:
                raise PodleGatewayTimeoutError(result)
            elif response.status_code == 422:
                raise PodleUnprocessableEntityError(result)

        except Exception as e:
            raise e

        # Parse and return JSON Result
        try:
            return json.loads(result)
        except json.JSONDecodeError:
            return None


class PodleHelper:
    """
    Podle helper to interact with the API.
    https://api.podle.io/documentation
    """

    client = PodleHttpClient()
    base_url = "https://api.podle.io/v1"
    endpoints = {
        "newsletters": f"{base_url}/newsletters",
        "dictionaries": f"{base_url}/dictionaries/default/words",
        "rss": f"{base_url}/rss",
        "rss_batch": f"{base_url}/rss/batch",
    }

    def create_newsletter(self, data):
        url = self.endpoints["newsletters"]
        return self.client.make_request(url, "POST", data)

    def retrieve_newsletter(self, newsletter_id):
        url = f"{self.endpoints['newsletters']}/{newsletter_id}"
        return self.client.make_request(url, "GET")

    def create_or_update_word(self, data):
        url = self.endpoints["dictionaries"]
        return self.client.make_request(url, "POST", data)

    def delete_word(self, word):
        url = f"{self.endpoints['dictionaries']}/{word}"
        return self.client.make_request(url, "DELETE")

    def lookup_word(self, word):
        url = f"{self.endpoints['dictionaries']}/{word}"
        return self.client.make_request(url, "GET")

    def lookup_all_words(self):
        url = self.endpoints["dictionaries"]
        return self.client.make_request(url, "GET")

    def get_private_rss(self, subscriber_id, newsletter_name):
        url = f"{self.endpoints['rss']}?subscriberId={subscriber_id}&newsletterName={newsletter_name}"
        return self.client.make_request(url, "GET")

    def create_private_rss(self, data):
        url = self.endpoints["rss"]
        return self.client.make_request(url, "POST", data)

    def delete_private_rss(self, subscriber_id, newsletter_name):
        url = f"{self.endpoints['rss']}?subscriberId={subscriber_id}&newsletterName={newsletter_name}"
        return self.client.make_request(url, "DELETE")

    def create_batch_private_rss(self, data):
        url = self.endpoints["rss_batch"]
        return self.client.make_request(url, "POST", data)

    def delete_batch_private_rss(self, data):
        url = self.endpoints["rss_batch"]
        return self.client.make_request(url, "DELETE", data)
