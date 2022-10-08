from ast import Lambda


new_list =[]

# for i in range(1, 11):
#     new_list.append(i)

# print(new_list)

# smart_list = [i for i in range (1, 10)]
# print(smart_list)

# for i in "TechElevate":
#     if i != 'e':
#         new_list.append(i)
#     else:
#         print(f'{i} is e!')

# print(new_list) 

# smart_list = [i if i!='e' else print(f'{i} is e! ') for i in 'TechElevate']
# print(smart_list)

# s = {i for i in range(6)}
# print(f'{s=}')
# d = {i: i +2 for i in range(6)}
# print(f' {d=} ')
# condition = True
# example = 420 if condition else 60
# print(example)
someLambda = lambda a,b: a *(b -1)

print(someLambda(2,3))