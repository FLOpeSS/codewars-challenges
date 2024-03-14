def digital_root(n):
  numbers: list = [int(i) for i in str(n)]
  summed = sum(numbers)
  while summed > 9:
    numbers = [int(i) for i in str(summed)]
    summed = sum(numbers)
  return numbers

   
  
# digital_root(16)
# digital_root(942)
# digital_root(132189)
# digital_root(493193)

def digital_rot(n):
  numbers: list = [int(i) for i in str(n)]

  summed = sum(numbers)
  while summed > 10:
    numbers = [int(i) for i in str(summed)]
    summed = sum(numbers)
    print(summed)

  # print(summed)
  return numbers

def bubble_sort(array: list):
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if array[j] < array[i]:
        tmp = array[i]
        array[i] = array[i]
        array[j] = tmp
  return array

    


# bubble_sort()




def disevowel(string_: str):
  vowels = ["a", "e", "i", "o", "u"]
  for i in vowels:
    if i in string_:
      print(i)
      stringed = string_.replace(i, "")

  print(stringed)

print(disevowel("hello world"))








