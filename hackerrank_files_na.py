#Find the runner score!

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    max1=arr[-1]
    arr.sort(reverse=True)
    for x in arr:
        if x!=max1:
            result = x
            print(result)
            break


#Nested lists

if __name__ == '__main__':
    dic={}
    s=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dic:
            dic[score]. append(name)
        else:
            dic[score]= [name]
        if score not in s:
            s.append(score)
            
    m=min(s)
    s.remove(m)
    m1=min(s)
    dic[m1].sort()
    for i in dic[m1]:
        print(i)

#Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks:
        j = student_marks.get(i)
        if i==query_name:
            result = 0
            for k in j:
                result+= float(k)
            print("{:.2f}".format((result/len(j))))
            break
        else:
            continue

#lists

if __name__ == '__main__':
    lst = []
    N = int(input())
    for i in range(N):
        mn= list(input("").split(" "))
        
        if mn[0]=="insert":
            a , b = map(int , (mn[1],mn[2]))
            lst.insert(a,b)
            
        elif mn[0]=="print":
            print(lst)
            
        elif mn[0]=="remove":
                lst.remove(int(mn[1]))

        elif mn[0]=="append":
            lst.append(int(mn[1]))
            
        elif mn[0]=="sort":
            lst.sort()
        
        elif mn[0]=="pop":
            
            lst.pop()
        elif mn[0]=="reverse":
            lst.reverse()

#Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))

#Swap Case

def swap_case(s):
    return s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#string split and join

def split_and_join(line):
    return line.replace(' ','-')
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



#what's your name?

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a ,b))
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#Mutations

def mutate_string(string, position, character):
    return string[:position]+character + string[(position+1):]
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Find a string

def count_substring(string, sub_string):
    len_SubString= len(sub_string)
    result = 0
    for i in range(len(string)+1-len_SubString):
        if string[i:i+len_SubString]==sub_string:
            result+=1
        else:
            continue
    
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#itertools.product()

import itertools as it
a = list(map(int , input("").split(' ')))
b = list(map(int , input("").split(' ')))
lst = list(x for x in it.product(a,b))
for i in lst:
    print(i, end = ' ' )

    collections.counter()
    x = int(input())
    shoe_size = list(map(int,input().split()))
    n = int(input())
    sell = 0
for i in range(n):
    s, p = map(int,input().split())
    if s in shoe_size:
        sell = sell + p
        shoe_size.remove(s)
    print(sell)

#polar coordinates

import cmath
m=complex(input())
print(abs(complex(m.real,m.imag)),'\n',cmath.phase(complex(m.real,m.imag)))

#DefaultDict Tutorial

from collections import defaultdict
d = defaultdict(list)
n,m=map(int,input().split())
for i in range(n):
    w = input()
    d[w].append(str(i+1))
for j in range(m):
    w = input()
    print(' '.join(d[w]) or -1)

#Find Angle MBC

import math
AB,BC=int(input()),int(input())
hype=math.hypot(AB,BC)                      #to calculate hypotenuse
res=round(math.degrees(math.acos(BC/hype))) #to calculate required angle 
degree=chr(176)                                #for DEGREE symbol
print(res,degree, sep='')

#Collection.orderedDict()

import collections, re
n = int(input())
item_od = collections.OrderedDict()
for i in range(n):
    record_list = re.split(r'(\d+)$',input().strip())
    item_name = record_list[0]
    item_price = int(record_list[1])
    if item_name not in item_od:
        item_od[item_name]=item_price
    else:
        item_od[item_name]=item_od[item_name]+item_price
            
for i in item_od:
    print(i+str(item_od[i]))

itertools.combinations()
import itertools as it
iterr ,n = input().split(" ")
lst1= list(i for i in iterr)
str(lst1.sort())
result = []
for i in range(1,int(n)+1):
    x = list(m for m in it.combinations(lst1, i))
    result.append(x)
for m in range(len(result)):
    for j in result[m]:
        for k in j:
            print(k, end ="" )
        print()


Set.add()
n=int(input(""))
s = set()
for i in range(n):
    m=input("")
    s.add(m)

print(len(s))

set.discard(). Remove()&pop()
n = int(input())
s = set(map(int, input().split(" ")))
m = int(input())
for i in range(0,m):
    x=list(input().split(" "))
    if x[0]=="pop":
        s.pop()
    elif x[0]=="remove":
        j = int(x[1])
        s.remove(j)
    elif x[0]=="discard":
        j = int(x[1])
        s.discard(j)
print(sum(s))






collections.deque()
import collections
n = int(input())
d = collections.deque()
for i in range(n):
    cmd = list(input().strip().split())
    opt = cmd[0]
    if opt == 'pop':
        d.pop()
    elif opt == 'popleft':
        d.popleft()
    elif opt == 'append':
        d.append(int(cmd[1]))
    elif opt == 'appendleft':
        d.appendleft(int(cmd[1]))
for i in d:
    print(i,end=' ')

compress thestring!
from itertools import groupby as a
s=input("")
key=[k for k, g in a(s)]
word= [list(g) for k, g in a(s)]
for i in range(len(key)):
    print("({}, {})".format(len(word[i]),key[i]),end=" ")

 set.union()operation
n1 = int(input(""))
ls1=set(map(int , input("").split(" ")))
n2 = int(input(""))
ls2=set(map(int , input("").split(" ")))
ma = set(ls1.union(ls2))
output =0
for i in ma:
    output+=1

output = str(output)
print(output)


set.intersection()operation
n1 = int(input(""))
ls1=set(map(int , input("").split(" ")))
n2 = int(input(""))
ls2=set(map(int , input("").split(" ")))
ma = set(ls1.intersection(ls2))
output=0
for i in ma:
  output+=1
print(output)

#Mod DIVMOD

a = int(input(""))
b = int(input(""))
print('{}\n{}\n{}'.format((a//b),(a%b),divmod(a,b)))

POWER- MOD POWER
a = int(input(""))
b = int(input(""))
c = int(input(""))
print(a**b)
print(a**b%c)

#Maximize it!

from itertools import product
K,M = map(int,input().split())
nums = []
for _ in range(K):
    row = map(int,input().split()[1:])
    nums.append(map(lambda x:x**2%M, row))
print(max(map(lambda x: sum(x)%M, product(*nums))))








