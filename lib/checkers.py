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
  i = 0 # counter for days
  j = 0 # counter for blocks
  while i < 5:
    while j < 4:
      teachers = get_elements(array, i, j)
      if repeatedValues(teachers) == True:
        return True
      j += 1
    i += 1
  return False  


# get a specific data from a 3d array
def get_elements(array, day, block):
  tmpArr = []
  for items in array:
    if array[items][day][block] != "-":
      tmpArr.append(array[items][day][block].split(":")[1])
  
  return tmpArr

  
# determine if there is repeated values
def repeatedValues(array):
    for item in array:
      i = 0
      c = 0
      while i < len(array):
        if item == array[i]:
          c += 1
          if c == 2:
            return True
        i += 1
      return False
        
      
        