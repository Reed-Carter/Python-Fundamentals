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