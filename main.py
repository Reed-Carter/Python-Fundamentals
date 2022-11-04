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

