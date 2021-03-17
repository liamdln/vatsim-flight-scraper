import json
import requests

class Scraper:

    def __init__(self, grabItems):
        self.grabItems = grabItems

    def grabJson(self, urlBase):
        constructedUrl = self.buildUrl(urlBase)
        res = requests.get(constructedUrl)

        if res:
            if res.status_code == 200:
                data = json.loads(res.content)
                return data
            elif res.status_code == 404:
                raise Exception(f"No content found at {constructedUrl}")
            # more response codes here
        else:
            raise Exception(f"No response from {constructedUrl}.")



    def buildUrl(self, base):
        return base + "/vatsim-data.json"
