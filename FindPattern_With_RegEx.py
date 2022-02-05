"""
To create a Regex object that matches the phone number pattern,
enter the following into the interactive shell. (Remember that
\d means “a digit character” and \d\d\d-\d\d\d-\d\d\d\d is the
regular expression for the cor￾rect phone number pattern.)
"""
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())