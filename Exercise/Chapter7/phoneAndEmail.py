#! python3
# phoneAndEmail.py- Finds phone numbers and email addresses on the clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''',re.VERBOSE)

# TODO: Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
    )''',re.VERBOSE)

# TODO: Find Mataches in clipboard text.
text = str(pyperclip.paste())               # get info from things we copied 
matches = []                                # stores the info found from copied value

for groups in phoneRegex.findall(text):     # loops through elements found from phoneRegex
##    print(groups)
    phoneList = [groups[1], groups[3], groups[5]]   # stores the elements in a list
    phoneNum = '-'.join(phoneList)                  # calls the list and joins '-' 
    if groups[8] != '':                             # if extenstion exists 
        phoneNum += ' x' + groups[8]                # adds ' x' extension number
    matches.append(phoneNum)                        # appends phoneNum in matches list
##print(matches)
    
for groups in emailRegex.findall(text):     # loops through elements found from emailRegex
    matches.append(groups[0])               # appends email in matches list

# TODO: Copy results to the clipboard.
if len(matches) > 0:                        # if there exist any thing on matches list 
    pyperclip.copy('\n'.join(matches))      # copy that is clipboard and print on screen
    print('Copied to clipboard:')           
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.') # else if nothing exits on matches list print message
    
