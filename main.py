list_one = ["desk", "chair", "computer"]
def list_sayer(list_one):
  if len(list_one) == 0:
    print("the list is empty")
    return False
  else:
    for index in range(len(list_one)):
      print(f"index {index} is the value: {list_one[index]}")
    return True  
list_sayer(list_one)


dict_one = {"Burkina_Faso": "Ouagadougou", "Kazakhstan": "Nur-Sultan", "Japan": "Tokyo", "Peru": "Lima"}
def dict_sayer(dict_one):
  if len(dict_one) == 0:
    print("The dictionary is empty!")
    return False
  else:
    for key, value in dict_one.items():
      print(f"the capital of {key} is {value}")
    return True
dict_sayer(dict_one)


dict_age = {"Joey": 28, "Jim": 46, "Billy": 10}
def Greatest(dict_age):
  for key, value in dict_age.items():
    if value == max(dict_age.values()):
      return (key, value)
Greatest(dict_age)

list1 = ["vanilla", "cherry"]
list2 = ["cake", "ice_cream", "pistachio"]
def zipper(list1, list2):
  both_lists_dict = {}
  if len(list1) == len(list2):
    for index in range(len(list1)):
      both_lists_dict[list1[index]] = list2[index]
    print(both_lists_dict)
  else:
    return (list1, len(list1), list2, len(list2))
zipper(list1, list2)