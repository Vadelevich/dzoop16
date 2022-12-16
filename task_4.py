class Meta(type):
    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(Meta, cls).__new__(cls, clsname, bases, uppercase_attr)
class Math(metaclass=Meta):
    pi = 3.141592653589793
    e = 2.718281828459045
    tau = 6.283185307179586

m = Math()
print(m.PI)
# 3.141592653589793
print(m.E)
# 2.718281828459045
# print(m.pi)
# AttributeError: 'Math' object has no attribute 'pi'