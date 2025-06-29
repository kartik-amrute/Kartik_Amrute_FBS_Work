pri=int(input("enter principle amount:"))
years=int(input("enter no of years:"))
rate=float(input("enter rate of interest:"))
time=int(input("enter the time of: "))

amount=pri*(1+rate/100)**time
compound=amount-pri

print("compund of intrest: ",compound)