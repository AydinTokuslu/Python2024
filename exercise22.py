# Write a function called count_dots. This function takes a
# string separated by dots as a parameter and counts how many
# dots are in the string. For example, ‘h.e.l.p.’ should return 4
# dots, and ‘he.lp.’ should return 2 dots.

def count_dots(str):
    num_of_dots = 0
    for i in str:
        if i == ".":
            num_of_dots += 1
    print(num_of_dots)

str1 = "h.e.l.p.m.e."
count_dots(str1)