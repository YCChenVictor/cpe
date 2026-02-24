import sys

# 2011 rules:
# 1/10, 2/21, 4/4, 5/9, 6/6, 7/11, 8/8, 9/5, 10/10, 11/7, 12/12 are all Mondays

rules = {
  '1': '10',
  '2': '21',
  '3': '14',
  '4': '4',
  '5': '9',
  '6': '6',
  '7': '11',
  '8': '8',
  '9': '5',
  '10': '10',
  '11': '7',
  '12': '12'
}

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

lines = sys.stdin.read().splitlines()

num_of_cases = lines[0]
for i in range(1, len(lines)):
    [month, day] = lines[i].split()
    base = int(rules[month])
    month = int(month)
    day = int(day)
    difference = (day - base) % 7
    print(weekday[difference])
