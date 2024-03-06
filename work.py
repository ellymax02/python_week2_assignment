#empty list
my_list=[]
#append 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert value of 15 at the second position in list
my_list.insert(1,15)

new_list={50,60,70}
#extend my_list with new_list
my_list.extend(new_list)

#remove the last item in the list
del my_list[-1]
#sort my list ascending
my_list.sort()

#find and display index of 30
index_of_30=my_list.index(30)
print(f'The index of 30 in a list is {index_of_30}')

print(my_list)