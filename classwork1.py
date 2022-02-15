Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 1+1
2
>>> import math
>>> math.sin(1)
0.8414709848078965
>>> math.sin(90)
0.8939966636005579
>>> math.pi
3.141592653589793
>>> math.sin((math.pi/2))
1.0
>>> math.sin(0)
0.0
>>> math.cos(0)
1.0
>>> math.cos(math.pi)
-1.0
>>> math.cos(math.pi/2)
6.123233995736766e-17
>>> lst=[1,2,3,4,5]
>>> lst
[1, 2, 3, 4, 5]
>>> lst[:3]
[1, 2, 3]
>>> lst[2:3]
[3]
>>> lst[2:-1]
[3, 4]
>>> lst[-1]
5
>>> lst[-3]
3
>>> lst[:-3]
[1, 2]
>>> lst1=[6,7,8,9,10]
>>> lst+lst1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> lst.append(3)
>>> lst
[1, 2, 3, 4, 5, 3]
>>> lst2=lst+lst1
>>> lst2
[1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 10]
>>> help(lst2)

>>> lst2
[1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 10]
>>> lst1.insert(0,4)
>>> lst1
[4, 6, 7, 8, 9, 10]
>>> lst1.insert(0,5)
>>> lst1
[5, 4, 6, 7, 8, 9, 10]
>>> lst2
[1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 10]
>>> lst2.sort()
>>> lst2
[1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
>>> lst2.reverse()
>>> lst2
[10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1]
>>> d{}
SyntaxError: invalid syntax
>>> d={}
>>> d["one"] = 1
>>> d["two"]=2
>>> d
{'one': 1, 'two': 2}
>>> len(d)
2
>>> d.keys()
dict_keys(['one', 'two'])
>>> d.values()
dict_values([1, 2])
>>> pprint.pprint(d)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    pprint.pprint(d)
NameError: name 'pprint' is not defined
>>> print(d)
{'one': 1, 'two': 2}
>>> print(lst2)
[10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1]
>>> d["complex"]={}
>>> d
{'one': 1, 'two': 2, 'complex': {}}
>>> print(d)
{'one': 1, 'two': 2, 'complex': {}}
>>> d["complex"]["yellow"] = [255,255,0]
>>> print(d)
{'one': 1, 'two': 2, 'complex': {'yellow': [255, 255, 0]}}
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> d["complex"]["red"]=[255,0,0]
>>> d["complex"]["green"]=[0,255,0]
>>> d["complex"]["blue"]=[0,0,255]
>>> print(d)
{'one': 1, 'two': 2, 'complex': {'yellow': [255, 255, 0], 'red': [255, 0, 0], 'green': [0, 255, 0], 'blue': [0, 0, 255]}}
>>> d
{'one': 1, 'two': 2, 'complex': {'yellow': [255, 255, 0], 'red': [255, 0, 0], 'green': [0, 255, 0], 'blue': [0, 0, 255]}}

>>> def fact(n):
	if n<=1:
		return 1
	else:
		return n*fact(n-1)

	
>>> fact(5)
120
>>> fact(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
>>> fact(200)
788657867364790503552363213932185062295135977687173263294742533244359449963403342920304284011984623904177212138919638830257642790242637105061926624952829931113462857270763317237396988943922445621451664240254033291864131227428294853277524242407573903240321257405579568660226031904170324062351700858796178922222789623703897374720000000000000000000000000000000000000000000000000
>>> 

================ RESTART: /Users/kateryna/Documents/fact.py ================
120
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
788657867364790503552363213932185062295135977687173263294742533244359449963403342920304284011984623904177212138919638830257642790242637105061926624952829931113462857270763317237396988943922445621451664240254033291864131227428294853277524242407573903240321257405579568660226031904170324062351700858796178922222789623703897374720000000000000000000000000000000000000000000000000
>>> 

============== RESTART: /Users/kateryna/Documents/fibonacci.py =============
The first 5 elements of Fibonacci sequence:
[1, 2, 3, 5, 8]
None
The first 10 elements of Fibonacci sequence:
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
None
The first 20 elements of Fibonacci sequence:
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
None
>>> 
