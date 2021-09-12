try:
    with open("Exceptions.py") as file:
        print("opening file")
        print("File opened sucessfully")
    # open returns a file object
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):  # as ex
    # since this is different error from the other one you have to creata another exception
    # you can define a variable that will include the details about the function
    # print(ex)
    # print(type(ex))
    print("You didn't enter a valid age.")
# except ZeroDivisionError:
#     print("You didn't enter a valid age.")
    # this message won't be printed if there are similar statements
    # if it was printed it will be shown twice
    # so you can put the exception in line
else:
    print("no exceptions were thrown. lol.")
finally:#this is executed 
    file.close
# this code will be executed because we are handling it properly
print("Execution continues.")
# When there's a  try statement it will run everything
# but if there is an exception the code in the except clause will be run
# you can use files for closing files and more
