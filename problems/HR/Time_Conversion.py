"""
Given a time in -hour AM/PM format, convert it to military(24-hour) time.

Note: - 12: 00: 00AM on a 12-hour clock is 00: 00: 00 on a 24-hour clock.
- 12: 00: 00PM on a 12-hour clock is 12: 00: 00 on a 24-hour clock.

Example
S = 12:01:00PM
Return '12:01:00'.

S = 12:01:00AM
Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in hour format
Returns

string: the time in hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input

07: 05: 45PM
Sample Output

19: 05: 45
"""

# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    time = s[:-2].split(':')
    suffix = s[len(s)-2:]

    print(time)

    if suffix == 'AM':
        if time[0] == '12':
            time[0] = '00'
    else:
        if time[0] == '12':
            pass
        else:
            time[0] = str(int(time[0]) + 12)

    return (':'.join(time) + suffix)


timeConversion('07:05:45PM') 
