# Custom logging handler for python for sending log messages via Pushover.
# https://pushover.net/
#
# Extends HTTPHandler
# https://docs.python.org/3.6/library/logging.handlers.html#httphandler

import logging.handlers


class PushoverHTTPHandler(logging.handlers.HTTPHandler):
    _APP_TOKEN = None
    _USER_KEY = None

    # https://pushover.net/api#priority
    PRIORITY_LOWEST = -2
    PRIORITY_LOW = -1
    PRIORITY_NORMAL = 0
    PRIORITY_HIGH = 1
    PRIORITY_EMERGENCY = 2

    # https://docs.python.org/3.6/library/logging.html#logging-levels
    _priority_mapping = {
        logging.NOTSET: PRIORITY_NORMAL,
        logging.DEBUG: PRIORITY_LOWEST,
        logging.INFO: PRIORITY_LOW,
        logging.WARNING: PRIORITY_NORMAL,
        logging.ERROR: PRIORITY_HIGH,
        logging.CRITICAL: PRIORITY_EMERGENCY,
    }

    def __init__(
        self,
        user,
        token,
        priority_mapping=None,
        emergency_retry=30,
        emergency_expire=300,
    ):
        self._APP_TOKEN = token
        self._USER_KEY = user
        if priority_mapping is not None:
            self._priority_mapping = priority_mapping

        # min/max documented at https://pushover.net/api#priority
        self._priority_emergency_retry_every_seconds = (
            emergency_retry if emergency_retry >= 30 else 30
        )
        self._priority_emergency_expire_after_seconds = (
            emergency_expire if emergency_expire <= 10800 else 10800
        )

        super().__init__(
            host="api.pushover.net",
            url="/1/messages.json",
            method="POST",
            secure=True,
            credentials=None,
            context=None,
        )

    def mapLogRecord(self, record):
        mapped_record = dict()
        mapped_record["user"] = self._USER_KEY
        mapped_record["token"] = self._APP_TOKEN
        mapped_record["title"] = record.name
        mapped_record["message"] = record.msg % record.args
        mapped_record["priority"] = self._priority_mapping[record.levelno]

        # If priority is emergency we have to set how often Pushover
        # retries and for how long
        if mapped_record["priority"] == 2:
            mapped_record[
                "retry"
            ] = self._priority_emergency_retry_every_seconds
            mapped_record[
                "expire"
            ] = self._priority_emergency_expire_after_seconds

        return mapped_record

    @property
    def priority_mapping(self):
        return self._priority_mapping

    @priority_mapping.setter
    def priority_mapping(self, mapping):
        self._priority_mapping = mapping
