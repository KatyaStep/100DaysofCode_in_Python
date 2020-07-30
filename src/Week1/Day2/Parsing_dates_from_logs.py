import os
import re
import urllib.request

from datetime import datetime

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
# tmp = os.getenv("TMP", "/tmp")
# logfile = os.path.join(tmp, 'log')
# urllib.request.urlretrieve(
#     'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
#     logfile
# )
#
# with open(logfile) as f:
#     loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    if not line:
        return None
    match = re.search(r'\d{4}-\d{2}-\d{2}\w\d{2}:\d{2}:\d{2}', line)
    return datetime.strptime(match.group(), '%Y-%m-%dT%H:%M:%S')


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_list = []
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            match = re.search(r'\d{4}-\d{2}-\d{2}\w\d{2}:\d{2}:\d{2}', line)
            date = datetime.strptime(match.group(), '%Y-%m-%dT%H:%M:%S')
            shutdown_list.append(date)

    return shutdown_list[-1] - shutdown_list[0]
    pass

# loglines = ['INFO 2014-07-03T23:27:51 supybot Shutdown initiated.', 'INFO 2014-07-03T23:31:22 supybot Shutdown initiated.']
# time_between_shutdowns(loglines)
