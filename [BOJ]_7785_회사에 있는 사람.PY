n=int(input())

my_dict={}

for _ in range(n):
    a,b=input().split(' ')
    my_dict[a]=b

ans_list=[]

for elem in my_dict:
    if my_dict[elem]=='enter':
        ans_list.append(elem)

ans_list.sort()
for elem in ans_list[::-1]:
    print(elem)