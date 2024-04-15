import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("7046503240:AAHT4pZtq4kAsNZN53VJJSqSYyQHRs4YMZ0", "")

    APP_ID = int(os.environ.get("APP_ID", 22766977))

    API_HASH = os.environ.get("API_HASH", "d7f5fc8cf7632325a6ebac8ff5cf103a")
