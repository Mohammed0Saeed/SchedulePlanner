def main():
  arr = ["cat", "bird", "dog"]
  arr = remove(arr, "cat")
  print(arr)

def remove(arr, el):
  newArr = []
  for item in arr:
    if item != el:
      newArr.append(item)
  return newArr

          

main()
