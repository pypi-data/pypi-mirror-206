from .prayer import Prayer
from typing import List

# from config import get_logger


class PrayersDay:
    def __init__(self, day_number: int, prayers: List[Prayer] = []):
        self.day_number = day_number
        self.prayers = prayers

        # self.logger = get_logger(__name__)
        # self.logger.info(
        # f"PrayersDay instance created:\t day: {self.day_number}, prayers: {self.prayers}"
        # )

    def __repr__(self) -> str:
        return f"Day(index={self.day_number}, prayers={self.prayers[:]}])"


if __name__ == "__main__":
    from datetime import datetime
    asr = Prayer("asr", datetime.now())
    isha = Prayer("isha", datetime.now())

    d = PrayersDay(day_number=0, prayers=[asr, isha])
    print(d)
