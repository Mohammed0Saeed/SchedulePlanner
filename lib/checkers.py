# check if the blocks in the plan are given equally
def checkPlan(array):
    empty = 0
    for i in range(len(array)):
      if array[i][3] == "-":
        empty += 1
    
    if empty >= 3:
      return True
    return False

# TODO > add a condition to check if the teacher is in this place in previous courses using [i:]
def isOnlyOne(array):
   # 3D array
    ...


"""
[
  [
    [000, 001, 002],
    [010, 011, 012],
  ]
  [
    [000, 001, 002],
    [010, 011, 012],
  ]
]
[
  [
    [a, b, c],
    [a, b, c],
  ]
  [
    [a, b, c],
    [a, b, c],
  ]
]
"""
def get_elements(array, index):
   tmpArr = []
   for items in array:
      tmpArr.append(items[index])
  