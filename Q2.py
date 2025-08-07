def factorial(satrt,end):
    if(start==0 or end==1):
        return 1
    else:    
        return start * factorial(end - 1)
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))    
result = factorial(start, end)
print(result)