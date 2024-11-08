# You are given a list of names, and you are asked to write a code
# that returns all the names that start with ‘S’. Your code should
# return a dictionary of all the names that start with S and how
# many times they appear in the dictionary. Here is a list below:
# names = ["Joseph","Nathan", "Sasha", "Kelly",
#  "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
# Your code should return: {"Sasha": 1, "Sera": 2}


names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

def list_of_names(list):
    dic= {}
    for i in list:
        if i.startswith("S"):
            dic.update({i: list.count(i)})
    print(dic)
list_of_names(names)