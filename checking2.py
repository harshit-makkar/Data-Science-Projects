Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> h=[1,2,3,a,4,5]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    h=[1,2,3,a,4,5]
NameError: name 'a' is not defined
>>> h=[1,2,4,"a",4,5]
>>> for i in h:
	print(h)

	
[1, 2, 4, 'a', 4, 5]
[1, 2, 4, 'a', 4, 5]
[1, 2, 4, 'a', 4, 5]
[1, 2, 4, 'a', 4, 5]
[1, 2, 4, 'a', 4, 5]
[1, 2, 4, 'a', 4, 5]
>>> for i in h:
	print(i+" hi!")

	
Traceback (most recent call last):
  File "<pyshell#7>", line 2, in <module>
    print(i+" hi!")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
