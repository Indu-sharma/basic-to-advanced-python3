import isodate
import datetime
import dateparser


class DateUtils:
    def __init__(self, datestring, time_format="unix"):
        self.datestring = datestring
        self.time_format = time_format

    def get_binning_index(self):
        if self.time_format.lower () == "unix":
            return datetime.datetime.utcfromtimestamp (float (self.datestring)).strftime ('%Y.%m.%d')
        if self.time_format.lower () == "iso":
            return isodate.parse_date (self.datestring).strftime ('%Y.%m.%d')
        if self.time_format.lower () == "human":
            return dateparser.parse (self.datestring).strftime ('%Y.%m.%d')
