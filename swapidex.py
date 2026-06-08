
n = int(input ("enter input of list :"))

list = []
for _ in range (n):
    num = int(input())
    list.append(num)

idx1 = int(input("enter idx1 :c"))
idx2 = int (input("enter idx2 : "))

print(list)

# swapping values at idx1 And idx2
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2]= temp
print(list)