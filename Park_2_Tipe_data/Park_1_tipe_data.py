
#tipe data comment
#integer 
a = 32767
print("Tipe Data Integer (int) : {0}".format(a))
#Float 
b = 1.5
print("Tipe Data Float (float) : {0}".format(b))
#Complex 
c = 1 + 2.5j
print("Tipe Data Complex (Complex) : {0}".format(c))

#Sequensial
#list
d = [1, 2, 3, 4, 5]
print("Tipe Data List (list) : {0}".format(d))
#truplet
e = (1, 2, 3, 4, 5)
print("Tipe Data truplet (truplet) : {0}".format(e))
#range
f = range(1, 6)
print("Tipe Data range (range) : {0}".format(f))

#Set
g = {1, 2, 3, 4, 5}
print("Tipe Data Set (set) : {0}".format(g))
#frozenset
h = frozenset({1, 2, 3, 4, 5})
print("Tipe Data frozenset (frozenset) : {0}".format(h))

# Mapping
#dictionary
i = {
        "satu": 1, 
        "dua": 2, 
        "tiga": 3
    }
print("Tipe Data Dictionary (dictionary) : {0}".format(i))

# String
j = "Hello World"
print("Tipe Data String (string) : {0}".format(j))

# Char
k = 'A'
print("Tipe Data Char (char) : {0}".format(k))  

#Boolean
# Nilainya hanya True(1) atau False(0)
l = True
print("Tipe Data Boolean (boolean) : {0}".format(l))

# Binary
# Nilainya hanya 0 dan 1
m = 0b01000001
print("Tipe Data Binary (binary) : {0}".format(m)) 
desimal = int(m)
print("Nilai desimal : {0}".format(desimal))
char = chr(desimal)
print("Nilai char : {0}".format(char))
# Memory View
n = memoryview(b'Hello')
print("Tipe Data Memory View (memoryview) : {0}".format(n)) 
# bitearray
o = bytearray(d)
print("Tipe Data Bytearray (bytearray) : {0}".format(o))
