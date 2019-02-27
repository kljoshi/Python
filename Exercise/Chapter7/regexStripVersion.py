#! python3
# regexStripVersion - regex version of Strip function

import re

def strip_custom(x, text):
    # re.search(pattern, text)
    return re.search('^[{s}]*(.*?)[{s}]*$'.format(s=x), text).group(1)

print(strip_custom(' ',' aaabtestbcaa '))

