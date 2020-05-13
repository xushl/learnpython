numbers=[]
sum=0
count=0
while True:
    ans=input('enter a number or Enter to finish: ')
    if ans=='':
        if count==0:
            continue
        else: 
            break
    else:
            num = int(ans)
            numbers.append(num)
            sum+=num
            count+=1
for i in range(count):
    for m in range(count-i-1):
        if numbers[m] > numbers[m+1]:
            numbers[m],numbers[m+1]=numbers[m+1],numbers[m]
lowest=numbers[0]
highest=numbers[-1]
if count%2==0:
    median=(numbers[count//2-1]+numbers[count//2])/2
else:
    median=numbers[count//2]
print('numbers:',numbers)
print('count =',count,'sum =',sum,'lowest =',lowest,'highest =',highest,'mean =',sum/count,'median =',median)