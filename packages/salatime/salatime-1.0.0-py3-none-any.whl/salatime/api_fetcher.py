import requests
# from config import get_logger


class ApiFetcher:
    def __init__(self, url: str) -> None:
        self.url = url

        # self.logger = get_logger(__name__)
        # self.logger.info("ApiFetcher instance created")

    def fetch_data_from_api(self):
        """Fetches data from an api that does not need other that endpoint
        and parameters that should be included in the url"""
        try:
            response = requests.get(self.url)
            response_json = response.json()
            # self.logger.debug(f"response json: {response_json}")
            return response_json

        except requests.exceptions.ConnectionError:
            # todo: advanced error handling
            # self.logger.error("Check your internet connection!")
            raise ConnectionError("check your internet connection")


if __name__ == "__main__":
    api_fetcher = ApiFetcher(
        url="https://muslimsalat.com/marrakech/weekly.json")
    a = api_fetcher.fetch_data_from_api()['items'][0]
    print(a)
