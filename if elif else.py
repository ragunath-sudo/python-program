m1=int(input("Enter ur number "))
m2=int(input("Enter ur number "))
m3=int(input("Enter ur number "))
total=m1+m2+m3
print(total)
avg=total//3
print(avg)
if m1>40 and m2>40 and m3>40:
    result="pass"
    print("result is pass")
else:
    result="fail"
    print("result is fail")
if result=="pass":
    if avg>90:
        print("Grade A")
    elif avg>80:
        print("Grade B")
    elif avg>70:
        print("Grade C")
    elif avg>60:
        print("Grade D")
else:
    print("Grade E")



