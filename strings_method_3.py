p='pooja'
print(p.isascii())#true
a=chr(32)
c=chr(0)
print(a.isspace())#true
print(c.isspace())#false
print(chr(65))#A
print(ord('A'))#65
print(ord(' '))#32
print(ord('!'))#33
v=bin(6)
print(v)#0b110
print(0B110)#6
print(hex(22))#0x16
print(0X16)#22
print(oct(16))#0o20
print(0o20)#16
print(0O20)#16
print(0xa)#10
print(0XA)#10
print(0xf)#15
p='pOOjA'
print(p.swapcase())#PooJa
