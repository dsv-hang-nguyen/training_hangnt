#!/usr/bin/python

class List():
   def create_list():
      list_i = []
      return list_i

   def add_element(list1):
      print("Mời bạn nhập thêm phần tử vào list (Nếu muốn dừng vui lòng nhấn phím N)")
      element = ''
      while(element != 'N'):
         element = input()
         if(element != 'N'):
            list1.append(element)

class Dictionary():
   def base_program():
      # 4 cach khoi tao dictionary

      # dictionary with integer keys
      my_dict0 = {1: 'apple', 2: 'ball'}
      print(my_dict0) #access elements from a dictionary
      # dictionary with mixed keys
      my_dict1 = {'name': 'John', 1: [2, 4, 3]}
      print(my_dict1['name'])
      # using dict()
      my_dict3 = dict({1: 'apple', 2: 'ball'})
      print(my_dict3)
      # from sequence having each item as a pair
      my_dict4 = dict([(1, 'apple'), (2, 'ball')])
      print(my_dict4.get(1)) #access elements from a dictionary
      return my_dict4
   def add_element():
      dict1 = dictionary.base_program()
      dict1[3] = 'milk' # add element in a dictionary
      print(dict1)
   def del_element():
      dict1 = dictionary.base_program()

      # remove element key = 1
      print(dict1.pop(1))

      # xoa item dau tien trong dictionary
      print(dict1.popitem())

      # delete a particular item
      del dict1[2]

      # remove all items
      dict1.clear()


      # delete the dictionary itself
      del dict1
class Tuple():
   def base_tuple():
      # Empty tuple
      my_tuple = ()
      print(my_tuple)

      # Tuple having integers
      my_tuple = (1, 2, 3)
      print(my_tuple)

      # tuple with mixed datatypes
      my_tuple = (1, "Hello", 3.4)
      print(my_tuple)
      # nested tuple
      my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
      print(my_tuple)

      my_tuple = 3, 4.6, "dog"
      print(my_tuple)

      # tuple unpacking is also possible
      a, b, c = my_tuple
      print(a)
      print(b)
      print(c)
def main():
   # list1 = list.create_list()
   # list.add_element(list1)
   # print(list1)
   # dictionary.add_element()
   # dictionary.del_element()
   tuple.base_tuple()
if __name__ == '__main__':
   main()






