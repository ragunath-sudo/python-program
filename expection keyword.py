try:
    n1=int(input("Enter ur number "))
    n2=int(input("Enter ur number "))
    result=n1/n2
    print("result:",result)
except ZeroDivisionError:
    print("division by zero is invalid")
except ValueError:
    print("Invalid input")
except NameError:
    print("you have used a varaiable which is not defined")
except TypeError:
    print("invailed ")
finally:
    print("see you later")
