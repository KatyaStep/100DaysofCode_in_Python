import unittest
from Week1.Day3.Pomodoro import pomodoro_timer
from datetime import datetime, timedelta


class MyTestCase(unittest.TestCase):
    def test_pomodoro_deltatime(self):
        # GIVEN:
        timestamp = datetime.now()
        timer = timedelta(milliseconds=2)
        # WHEN:
        new_timestamp = pomodoro_timer(timestamp, timer)
        test_timestamp = timestamp + timer
        # THEN
        self.assertEqual(new_timestamp, test_timestamp)


if __name__ == '__main__':
    unittest.main()
