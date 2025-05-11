# 3.2. Rewrite your pay program using try and except so that your rogram handles non-numeric input gracefully by printing a message an exiting program.

hrs = input("Enter Hours:")
rte = input("Enter Rate:")
try:
   fh = float(hrs)
   fr = float(rte)
except:
    print("Error please enter numeric input")
    quit()
    
print(fh,fr)
if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    pay = reg + otp
else: 
    pay = fh * fr
print("Pay:",pay)
