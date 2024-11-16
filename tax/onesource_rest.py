import requests
import uuid


class OnesourceRestClient:
    BASE_URL = "https://api-uat.onesourcetax.com"  # default is the uat url
    TOKEN_URL = f"{BASE_URL}/oauth2/v1/token"
    TAX_URL = f"{BASE_URL}/indirect-tax-determination/taxes/v1/calculate"
    DEFAULT_CONFIG = {
        "base_url": "https://api-uat.onesourcetax.com",
        "company_role": "S",
        "calling_source": "DM",
        "charge_response": "CombineWithLine",
        "response_summary": "FullDetails",
        "external_company_id": "GLINTECO",
        "document_amount_type": "GrossPlusTaxAmount",
        "calling_system_number": "DM",
        "charge_included_in_amounts": "false",
    }
    SCOPE = "urn:tr:onesource:auth:api:IndirectTaxDetermination"  # fixed scope for tax determination

    def __init__(self, transaction_data, consumer_key, consumer_secret):
        self.transaction_data = transaction_data
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.config = self.DEFAULT_CONFIG

    def make_request(
        self, method, url, headers=None, params=None, payload=None
    ):
        headers = headers or {
            "Content-Type": "application/json",
        }
        response = requests.request(
            method=method, url=url, headers=headers, json=payload
        )
        return response

    def make_post_request(self, url, headers=None, payload=None):
        return self.make_request("post", url, headers=headers, payload=payload)

    def fetch_access_token(self) -> str:
        headers = {
            "ClientAssertion": f"Bearer {self.consumer_key}",
            "Content-Type": "application/json",
            "Correlation-Id": str(uuid.uuid4()),
        }
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.consumer_key,
            "client_secret": self.consumer_secret,
            "scopes": self.SCOPE,
        }
        print(
            f"Fetching access token from ONESOURCE Rest. Payload: {payload}, Headers: {headers}"
        )
        response = self.make_post_request(
            self.TOKEN_URL, headers=headers, payload=payload
        )
        self.access_token = response.json().get("access_token")
        print(f"New access token fetched: {self.access_token}")
        return self.access_token

    def fetch_tax(self) -> None:
        print("Fetching tax from ONESOURCE Rest")

        self.fetch_access_token()
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/vnd.tri.onesource.idt+json",
            "Correlation-Id": str(uuid.uuid4()),
        }
        response = self.make_post_request(
            self.TAX_URL, headers=headers, payload=self.transaction_data
        )
        self.response_data = response.json()
        print(f"Tax fetched: {self.response_data}")
        return self.response_data
