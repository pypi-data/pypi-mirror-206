from datetime import datetime

# from config import get_logger


class Prayer:
    # todo: delete prayer from the following variables
    # todo: because we got to them by a prayer object
    # todo: so it is already readable
    def __init__(self, name: str, datetime: datetime) -> None:

        self.name = name
        self.datetime = datetime

        # self.logger = get_logger(__name__)
        # self.logger.info(f"Prayer instance created: name: {self.name}, datetime: {self.datetime}")

    def __repr__(self) -> str:
        return f"Prayer(name={self.name}, datetime={self.datetime})"


if __name__ == "__main__":
    p = Prayer('asr', datetime.now())
    print(p)
