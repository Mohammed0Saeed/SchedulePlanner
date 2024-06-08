def main():
  arr = ["cat", "cat", "dog"]
  print(repeatedValues(arr))

def repeatedValues(array):
   for item in array:
      i = 0
      c = 0
      while i < len(array):
        if item == array[i]:
          c += 1
          if c == 2:
             return f"{array[i]} is repeated"
        i += 1
          

main()
