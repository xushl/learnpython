numbers=[]
sum=0
count=0
while True:
    ans=input('enter a number or Enter to finish: ')
    if ans =='':
        break
    else:
        num = int(ans)
        numbers.append(num)
        sum+=num
        count+=1
highest=lowest=numbers[0]
for a_num in numbers:
    if a_num >= highest:
        highest = a_num
    if a_num <= lowest:
        lowest = a_num
print('numbers:',numbers)
print('count =',count,'sum =',sum,'lowest =',lowest,'highest =',highest,'mean =',sum/count)