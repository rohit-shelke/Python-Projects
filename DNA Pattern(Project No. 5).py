a = int(input('Enter a number between 1 - 9: '))
l = []
for i in range(1,a+1):
    if i==a:
        l.append(' '*(i-1)+str(i))
    else:
        l.append(' '*(i-1)+str(i)+(' '*(((a-i)*2)-1))+str(i))
for i in l:
    print(i)
for i in l[::-1][1:]:
    print(i)
