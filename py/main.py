#
#
# class Ship:
#
#   def __init__(self, draft, crew):
#     self.draft = draft
#     self.crew = crew
#     self.total = draft + crew
#     self.result = False
#
#   def is_worth_it(self):
#     if self.total - self.crew < 20:
#       self.result = False
#     else:
#       self.result = True
#
#     return True if self.total - self.crew < 20 else False
#
#
#
#
# # print(returnin_nothing("hello world         "))
#
#
#
# def sep_str(st):
#   splited = st.split(" ")
#   # print(splited)
#   new_array = []
#   for i in range(len(splited)):
#     print(i)
#       # new_array.append(splited[i][i])
#     # for j in range(i):
#     #   print(j)
#
#   print(new_array)
#
# # sep_str("Just Live Life man")
#
# def bubble_sort(array: list):
#   for i in range(len(array)):
#     for j in range(i+1, len(array)):
#       if array[j] < array[i]:
#         tmp = array[i]
#         array[i] = array[j]
#         array[j] = tmp
#
#   return array
#
# def bubbleSort(array: list):
#   for i in range(len(array)):
#     for j in range(i+1, len(array)):
#       if array[j] < array[i]:
#         tmp = array[i]
#         array[i] = array[j]
#         array[j] = tmp
#
#   return array
#
#
# array = [9, 3, 5, 7, 50, 1]
# print(bubbleSort(array))
#
#
#

def reverse_words(s: str):
  splited = s.split(" ")
  print(splited[::-1])

reverse_words("hello world")


