#d = open("newtext.txt")
#print(d.read(4))  # Hello world -> Hell
#d.close()

a = "television"
print(a.find("Vision"))  # --> returns -1


a = "television"
print(a.find("#EXTINF"))

for i in range(1, -1, -1):
    print(i)


# file = open('file.txt', 'w')
# file.close()
# file = open('file.txt')
# print(file.read())
# --> empty line


print("Abc" > "abc")    # T
print("abc" > "abcd")   # F


# file = open('newtext.txt', 'r')
# a = [i for i in file]
# print(a)
# file.close()

# file = open('file.txt')
# print(file.readline(5))
# file.close()


import math
print("\u00B2".isdigit())         # csak szám, semmi más (pl. unicode for 0) vagy b = "\u00B2" #unicode for ²
print("367.4".isdecimal())        # 0-9
print("isalpohaCACAC".isalpha())  # csak ABC betüi, semmi +-*...


print(ord('c'))


import platform
print(platform.python_version())


class MyException(Exception):
    pass


try:
    raise MyException("A", "B")
except MyException as e:
    print(e.args)   # -->('A', 'B') as TUPLE!


a = "ab cd"
print('*'.join(a.split()))


# a = "abcdef"
# a[1] = 'x'
# print(a)

a = "abcdef"
b = a[-3:-1]
print("str: ", b)

a = "abcdef"
b = a[:-2:2]
print(b)


example1 = (r"e\x\m\p\l\e")
#example2 = ("e\x\m\p\l\e")
# example = example1.replace("\\", "")
# print(example)

asd = (filter(lambda x: x != "\\", example1))
print("".join(list(asd)))

for i in asd:
    print(i, end="")

print()

mystring = ""


asd2 = [None if y == "\\" else y for y in example1]
for q in asd2:
    if q != None:
        mystring += q

print(mystring)



a = ['aBc', 'def', 'gHi']
qwq = list(filter(lambda y: y[1].isupper(), a))
print(qwq)


b = list(map(lambda x: x.capitalize(), filter(lambda y: y[1].isupper(), a)))
print(b)


class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)
        print("Hello", end=" ")

    def __str__(self):
        return "A"


try:
    raise MyException("B")
except Exception as e:
    print(e)


print("envelope".find("lop") != -1)

a = "ab cd,ef"
print(a.split(','))

a = "engineer"
print(a.rfind('e', 0,-2))

a = "refrigerator"
print("refr: ", a.rfind('r'))


class A:
    __Var = 100

    def __init__(self):
        print(A._A__Var)


a = A()


import math as m
print(m.sqrt(25) - m.hypot(3, 4))


a = "television"
print(a.index("e", 2))


from platform import python_implementation
print(python_implementation())

# filesa = open('xyzy.txt', 'w')
# a = [1, 2, 3, 4, 5]
# for i in a:
#     filesa.write(str(i))
#
# filesa.close()

# a = "abcdef"
# del a[0:2]
# print(a)


class A:
    def __init__(self):
        self.__var = 10

    def get_var(self):
        return self.__var


a = A()
a._A__var = 100
print(a.get_var())

# try:
#     print(i=1 / 0)
# except TypeError as e:
#     print("Hi!", end=" ")
# finally:
#     print("Bye!")


class A:
    def __init__(self):
        self.__var = 10

    def get_var(self):
        return self.__var


class A:
    var = 1

    def __init__(self):
        self.x = 1

    def get_var():
        return A.var

class B(A):
    new_var = 99

    def __init__(self):
        super().__init__()

b = B()
print(hasattr(b,"A"))
print(hasattr(b,"B"))
print(hasattr(B,"x"))
print(hasattr(b,"get_var"))
print(hasattr(b,"var"), b.var, b.new_var)


a = [4, 2, 7, 1]
a.sort()
print(a)

a = [1, 2, 3]
b = [[j for j in range(i)] for i in a]
print(b[1][1])

my_dict = {'a': 1, 'b': 2}
try:
    my_dict['c']
except IndexError:
    print('A', end=' ')
except Exception:
    print("B", end=' ')
except KeyError:
    print("C", end=' ')



if(__name__=='abc'):
    print("Hello!")
elif(__name__=='__main__'):
    print("Hi!")
elif(__name__=='main'):
    print("Aloha!")
else:
    print("Bye!")


class A:
    __Var = 100

    def __init__(self):
        pass

    def get_var(self):
        return A.__Var


a = A()
A._A__Var = 1
b = A()
print(b.get_var())



# file = open('file.txt')
# print("readlines:", end=" ")
# print(len(file.readlines()))


# "library".sort()      # -> nincs ilyen!
# "library".sorted()    # -> nincs ilyen!
print(sorted("library"))


a = "abcdef"
a = a[0:2]
print(a)   # ab


a = "abc"
for i in a:
    i = 'x'

print(a)


# file = open('abc.txt')
# for i in file.read():
#     print(i)
#     break
#
#
a = "television"
print(a.index('vision'))


# a = [1, 2, 3]
# b = [[j for j in range(i)] for i in a]
# print(b)


class MyException(Exception):
    pass


try:
    raise Exception("A", "B")
except MyException:
    print("Hello", end=" ")
except Exception:
    print("London", end=" ")
finally:
    print("Bye")


class A:
    def __init__(self):
        self.__var = 10

    def get_var(self):
        return self.__var


a = A()
a._A__var = 100
print(a.get_var())


print("------------"*30)

kl = ["a", "b", "c", "d", "a", "v", "x", "b", "f", "g"]

unique1 = list(set(kl))
unique1.sort()
print(unique1)

for ll in kl:
    #print(kl.count(ll))
    if kl.count(ll) > 1:
        kl.remove(ll)

print(sorted(kl))
