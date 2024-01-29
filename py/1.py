class Ship:
  def __init__(self, draft, crew):
    self.draft = draft
    self.crew = crew
    self.total = draft + crew
    self.result = False

  def is_worth_it(self):
    if self.total - self.crew < 20:
      self.result = False
    else:
      self.result = True
      self.result = True

    return True if self.total - self.crew < 20 else False


def sep_str(st):
  splited = st.split(" ")
  # print(splited)
  new_array = []
  for i in range(len(splited)):
    print(i)
      # new_array.append(splited[i][i])
    # for j in range(i):
    #   print(j)

  print(new_array)

# sep_str("Just Live Life man")

def bubble_sort(array: list):
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if array[j] < array[i]:
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp

  return array


array = [9, 3, 5, 7, 50, 1]


def hello(s: str)-> str:
  if type(s) != str:
    return "Can't reproduce it!"

  return s

hello("hello")

def some_odd(array: list):
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if array[j] < array[i]:
        tmp = array[i]
        array[i] = array[i]
        array[j] = tmp
    
  return array

# print(hello_world("soemthing"))


def bubble_sortt(array: list):
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if array[j] < array[i]:
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp

  return array

