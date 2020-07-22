import unittest
import datetime
from Parsing_dates_from_logs import convert_to_datetime
from Parsing_dates_from_logs import time_between_shutdowns

class MyTestCase(unittest.TestCase):
    def test_info_log_str(self):
        # GIVEN: a log string
        log_str = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'

        # WHEN: run the log converter
        date = convert_to_datetime(log_str)

        # THEN date is Equal to datetime of 2015-10-03T10:12:51
        test_date = datetime.datetime(2015, 10, 3, 10, 12, 51)
        self.assertEqual(date, test_date)

    def test_empty_str(self):
        # GIVEN: a empty string
        log_str = ''

        # WHEN: run the log converter
        date = convert_to_datetime(log_str)

        # THEN date is Equal to None
        self.assertEqual(date, None)

    def test_error_log_str(self):
        # GIVEN: a log string
        log_str = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'

        # WHEN: run the log converter
        date = convert_to_datetime(log_str)

        # THEN date is Equal to datetime of 2014-07-03T23:24:31
        test_date = datetime.datetime(2014, 7, 3, 23, 24, 31)
        self.assertEqual(date, test_date)

    def test_time_between_shutdowns(self):
        # GIVEN: a log string
        loglines = ['INFO 2014-07-03T23:27:51 supybot Shutdown initiated.', 'INFO 2014-07-03T23:31:22 supybot Shutdown initiated.']

        # WHEN: run the log converter
        time_difference = str(time_between_shutdowns(loglines))

        # THEN date is Equal to datetime of 2014-07-03T23:24:31
        test_time = '0:03:31'
        self.assertEqual(time_difference, test_time)

if __name__ == '__main__':
    unittest.main()