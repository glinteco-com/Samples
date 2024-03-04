import requests


class QuickbookClient:
    REALM_ID = "paste your realm id here"
    ACCESS_TOKEN = "paste your access token here"
    SANDBOX_URL = "https://sandbox-quickbooks.api.intuit.com"

    def get_company_info(self):
        url = f"{self.SANDBOX_URL}/v3/company/{self.REALM_ID}/companyinfo/{self.REALM_ID}"
        headers = {
            "Authorization": f"Bearer {self.REALM_ID}",
            "Accept": "application/json",
        }

        response = requests.get(url, headers=headers)
        print(response.json())
