# Write a function called longest_value that takes a dictionary
# as an argument and returns the first longest value of the
# dictionary. For example, the following dictionary should return
# – apple as the longest value.
# fruits = {'fruit': 'apple', 'color': 'green'}

def longest_value(dic):
    max = {}
    for i in dic:
        print(dic[i])
        if len(dic[i]) > len(max) :
            max = dic[i]
    return max, len(max)

fruits = {"fruit": "appppppppppple", "color": "greeeeeeeen", "shape": "circleee"}
print(longest_value(fruits))