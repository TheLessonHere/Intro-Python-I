"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

def main():


  # Not Specified
  if len(sys.argv) == 1:
      cmonth = datetime.now().month
      cyear = datetime.now().year
      print(calendar.month(cyear, cmonth))

  # One Argument
  elif len(sys.argv) == 2:
    cmonth = int(sys.argv[1])
    if cmonth < 1 or cmonth > 12:
      print("Please enter a valid month")
      return

    cyear = datetime.now().year
    print(calendar.month(cyear, cmonth))

  # Two Arguments
  elif len(sys.argv) == 3:
    cmonth = int(sys.argv[1])
    if cmonth < 1 or cmonth > 12:
      print("Please enter a valid month")
      return
    year = sys.argv[2]
    cyear = int(year[year.find('[')+1:year.find(']')])
    print(calendar.month(cyear, cmonth))

  # Three + Arguments
  else:
    print("Please enter two or less arguments")

if __name__ == "__main__":
    main()