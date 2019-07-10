class MyCllass:
    pass

def test_fn(param):
    def inner_fn():
        pass
    val1 = 5
    val2 = 8
    for item in locals().items():
        print("\t{0} : {1}".format(item[0], item[1]))

value1 = 10
value2 = 20

obj1 = MyCllass()

g = dict(globals())
print(g)
print("globals()")

for item in g.items():
    print("\t{0} : {1}".format(item[0],item[1]))

# print("locals()")

# test_fn(10)