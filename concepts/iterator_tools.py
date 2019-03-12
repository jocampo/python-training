from itertools import islice, count

# infinite iterators
# count iterates endlessly
# we limit it by only slicing the first 1000 values
print(sum(islice((x for x in count() if x % 2 == 0), 1000)))

genders = ['M', 'M', 'M']
assert any(gender == 'F' for gender in genders) is False
assert all(gender == 'M' for gender in genders) is True

ages = [22, 25, 30, 15, 10, 23]
names = ["Jorge", "Giuseppe", "Armando", "Luis", "Oscar", "Manuel"]

for age, name in zip(ages, names):
    print(name + " is " + str(age) + " years old")
