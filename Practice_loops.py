word_list = ['Subscribe', 'to', 'kylie', 'ying']
for name in word_list:
    if name == 'kylie':
        continue
    print(name)

print("the end")

i = 1
while (i < 5):
    print(i)
    if i == 3:
        break
    i +=1
print('the end')

list_of_strings = ['cat', 'dog', 'cow']
print(list_of_strings)

list_of_numbers = [2, 4, 8, 9, 10, 22]
print(list_of_numbers)

list_of_lists = ['Hellow', 23, 4.0, ['hi, 12'], 'abc']
print(list_of_lists)

listofnumbers = [i for i in range(0,10)]
print(listofnumbers)

listnum = list(range(10))
print(listnum)

listnum2 = [i for i in range(0,10,2)]
print(listnum2)

strings_with_commas = "hi,hello,python,is,cool,an,i,love,python,so,much"
stringlist = strings_with_commas.split(',')
print(stringlist)

str2 = 'HELLO'
str2list = list(str2)
print(str2list)

integer = 12345678993
int_to_list = [int(i) for i in str(integer)]
print(int_to_list)

my_dict = {'a':1, 'b': 2, 'c': 3, 'd': 4}
print(my_dict)

key_list = list(my_dict.keys())
print(key_list)

value_list = list(my_dict.values())
print(value_list)

#list.append()
list_of_strings = ['cat', 'dog', 'cow']
list_of_strings.append('goat')
list_of_strings.append(123)
print(list_of_strings)


#list.extend
list3 = [1, 2, 3, 5, 7, 3, 1, 98]
list_of_strings.extend(list3)
print(list_of_strings)

#list.insert
list4 = ['sparrow', 'crane', 'jayhawk', 'bloodhound']
list4.insert(2, 'owl')
print(list4)

#list.index
j = list4.index('bloodhound')
print(j)

list4.insert(j-1, 'billy')
print(list4)

#list.remove
list4.remove('billy')
print(list4)

#list.pop
popped = list4.pop()
print(list4)
popped1 = list4.pop(2)
print(popped1)
print(list4)

#list.sort
list3 = [1,5,6,7,8,4,5,2,7,8,9,0,2,4,7,2,5,6,1,6,3,6,8,0,3,5,7,9,2]
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)

#list.reverse
list0 = [1,4,3,7,9,4]
list0.reverse()
print(list0)

#len(list)
length = len(list3)
print(length)

#max(list)
max = max(list3)
print(max)

min = min(list3)
print(min)

#list.count
count1 = list3.count(1)
print(count1)

#list.clear
list5 = ['a', 'r', 'h', 't', 'w', 't']
list5.clear()
print(list5)

# if statement
# to check a yes or no, like does this list have the number 5
if 5 in list3:
    print('list3 has 5')

# indexing a list
first = list3[0]
print(first)

last = list3[-1]
print(last)

#slicing
list3[0:3]
print(list3[0:3])
print(list3[0:5:2])
#sclice in reverse
print(list3[::-1])
print(list3[5:0:-1])
#reverse
for i in reversed(list3):
    print(i)

#slice assignment
list3[1:1] = [10,20]
print(list3)
list3[1:3] = [30,40]
print(list3)
list3[1:3] = []
print(list3)

#copying a list to the same address
a=[1,2,3,4]
print(a)
'''b=a
print(b)'''

a[0]=20
print(a)

#how to copy the list values

b=list(a)
print(b)



