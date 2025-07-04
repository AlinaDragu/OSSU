#fix this code to use variables "start" and "end" in the "range" , to get the total sum between and including those valiues.
#for example , if "start = 3" and "end = 5" then the sum should be 12.


mysum = 0
start = 3
end = 5
for i in range (start,end+1):
    print('i=',i)
    mysum += i
print(mysum)