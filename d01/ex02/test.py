from vector import Vector


v1 = Vector([3.0, 6.0, 2.0, 1.0])
print(v1)
v2 = Vector(4)
print(v2)
v3 = Vector((42, 55))
print(v3)
print()

v4 = Vector()
v4 = v1 + v2
print(v4)
print()

v5 = Vector((12, 20))
print(v5)
v5 = 4.4 + v5
print(v5)
v5 = 4.4 + v5
print(v5)
print()

v5 = v5 - 1
print(v5)
v5 = 100 - v5
print(v5)
print()

v5 = v5 / 2
print(v5)
v5 = 100 / v5
print(v5)
print()

v5 = v5 * 2
print(v5)
v5 = 100 * v5
print(v5)
print()

print(repr(v5))
print(str(v5))
