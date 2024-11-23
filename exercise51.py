import operator

def person_lister(f):
    def inner(people):
        return name_format(people)
    return inner

person = [
 ['Mike', 'Thomson', 20, 'M'],
 ['Robert', 'Bustle', 32, 'M'],
 ['Andria', 'Bustle', 30, 'F']
]

def sort_and_format_people(people):
    sorted_people = sorted(people)  # Sort by age
    return [name_format(person) for person in sorted_people]

for name in sort_and_format_people(person):
    print(name)

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')