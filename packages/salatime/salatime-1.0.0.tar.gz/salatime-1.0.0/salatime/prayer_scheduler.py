from .prayer import Prayer
from .prayers_day import PrayersDay
from .prayer_times_parser import PrayerTimesParser
from schedulerx import TimerManager
from schedulerx import ServiceManager

from typing import List


class PrayerScheduler:
    def __init__(self) -> None:

        self.prayer_times_parser = PrayerTimesParser()
        self.prayer_days: List[PrayersDay] = self.prayer_times_parser.parse()

        self.service_manger = ServiceManager(
            filename="salat.service",
            description="shut down at salat time",
            command="systemctl suspend -i",
        )
        # timer_manager = TimerManager()

    def schedule(self):
        self.service_manger.create_service_file()
        for day in self.prayer_days:
            for prayer in day.prayers:
                self.timer_manager = TimerManager(
                    filename=self._prayer_timer_filename(day, prayer),
                    on_calendar=prayer.datetime.strftime(r"%Y-%m-%d %H:%M"),
                    service_manager=self.service_manger,
                    description=f"shut down at {prayer.datetime}",
                )
                self.timer_manager.create_timer()
                self.timer_manager.start_timer()
                # self.timer_manager.enable_timer()

    def _prayer_timer_filename(self, day: PrayersDay, prayer: Prayer):
        return f"salat_day{day.day_number}_{prayer.name}.timer"


if __name__ == "__main__":
    o = PrayerScheduler()
    o.schedule()
