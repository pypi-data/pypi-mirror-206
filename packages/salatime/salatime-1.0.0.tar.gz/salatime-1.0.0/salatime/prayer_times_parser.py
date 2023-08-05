from .prayer import Prayer
from .prayers_day import PrayersDay
from .api_fetcher import ApiFetcher

from pprint import pprint
from datetime import datetime, timedelta


class PrayerTimesParser:
    """Create list of PrayersDay object from fetching data"""

    # todo: add exception handling to city, you can also inherit from
    # ApiFetcher and overwrite
    # todo: the fetch method to be fetch(city) and inside add exception
    # handling to city.
    def __init__(self):

        self.city: str = "marrakech"
        self.api_fetcher: ApiFetcher = ApiFetcher(
            url=rf"https://muslimsalat.com/{self.city}/weekly.json"
        )
        self.prayer_days: dict = self.api_fetcher.fetch_data_from_api()[
            'items']

    def view_api_json_response(self):
        pprint(self.prayer_days)

    def parse(self):
        prayer_days = []
        for day_num in range(1, 8):
            prayer_day = self._parse_day(day_num)
            prayer_days.append(prayer_day)
        return prayer_days

    def _parse_day(self, day_num):
        prayer_day = PrayersDay(day_number=day_num)
        prayer_day.prayers = []
        day = self.prayer_days[day_num - 1]
        prayer_date = self._remove_unnecessary_fields(day)
        for prayer_name, prayer_time in day.items():
            prayer_datetime = self._create_datetime_object(
                prayer_date, prayer_time)
            prayer_datetime = self._add_one_hour(prayer_datetime)
            prayer = Prayer(name=prayer_name, datetime=prayer_datetime)
            prayer_day.prayers.append(prayer)
        return prayer_day

    def _remove_unnecessary_fields(self, day):
        prayer_date = day["date_for"]
        del day["date_for"]
        del day["shurooq"]
        del day["fajr"]
        return prayer_date

    def _create_datetime_object(self, prayer_date: str, prayer_time: str):
        datetime_string = prayer_date + " " + prayer_time
        # time format yyyy-mm-dd hh:mm pm/am
        prayer_datetime_object = datetime.strptime(
            datetime_string, r"%Y-%m-%d %I:%M %p"
        )
        return prayer_datetime_object

    def _add_one_hour(self, prayer_datetime):
        prayer_datetime += timedelta(hours=1)
        return prayer_datetime


if __name__ == "__main__":
    o = PrayerTimesParser()
    o.view_api_json_response()
