

a = [1,2,3,4,5]
b = [1,3,5,6]
# O(n)
# use set and shift it bitwise
print(list(set(a) & set(b)))


O(n^2)
list comprehension
Intercep = [x for x in a if x in b]
print(Intercep)
