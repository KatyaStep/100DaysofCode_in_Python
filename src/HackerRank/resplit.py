regex_pattern = r"\,|\."  # Do not delete 'r'.

strin= '100,000,000.000'
import re
print("\n".join(re.split(regex_pattern, strin)))
#print("\n".join(re.split(regex_pattern, input())))