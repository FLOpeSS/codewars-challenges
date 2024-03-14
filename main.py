

def something_else(array: list):
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if array[j] < array[i]:
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp
  return array

class Node:
  def __init__(self, root):
    self.root = root
    self.next = None

  def __repr__(self):
    return f"this is the root of your Node: {self.root}, this is the next value of your Node: {self.next}"




class Hashtable:
  def __init__(self, name, password, something):
   self.name = name
   self.password = password
   self.something = something

  def __repr__(self):
    return f"this is your user login, name: {self.name}, password: {self.password}"



def is_anagram(test, original):
  return True if sorted(test.lower()) == sorted(original.lower()) else False

def anagram(test, original):


#
# def is_something(test, original):
#   return sorted(test.lower() == sorted(original.lower()))

# print(is_anagram("abc", "bca"))
# print(is_anagram("abc", "fdc"))
#
# print(is_anagram("abc", "bca"))
# print(is_anagram("abc", "fdc"))

def even_odd(n: int):
  return "Even" if n%2 == 0 else "odd"


def even_and_odd(l: list):
  evens = []
  odds = []
  for i in range(len(l)):
    if l[i] % 2 == 0:
      evens.append(l[i])
    else:
      odds.append(l[i])
  
  print("That was printed out")

  return {'odds': odds, 'evens': evens}


def bubble_sort(array: list):
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if array[j] < array[i]:
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp
  return array

def binary_search(array: list, n: int):
  lower, upper = 0, len(array)
  middle = (lower+upper) //2

  while (lower <= upper):
    if array[middle] == n:
      print(f"{n} was founded in the array")
      return n




# def binary_search(array: list, n: int):
#   lower, upper = 0, len(array)
#   middle = (lower + upper) // 2
#
#   while(lower <=upper):
#     if array[middle] == n:
#       return n
#
#     if array[middle] > n:
#       upper = middle + 1
#
#     if array[middle] < n:






array = [9, 3, 5, 7, 50, 1]

def hello_world(hello_world):
  if hello_world.lower() != "hello world":
    return "couldn't reproduce it"

  return hello_world



def sum_array(array: list):
  new_array = []
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      new_array.append(array[i]+array[j])

  return new_array

# print("this is me using default vim")
#
# print(sum_array([1,2,3,4,5]))
#

def main():
  even_odd(2)

main()

