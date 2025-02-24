def function_with_uncommon_bug(x):
    if x == 0:
        return 0  #This line is correct
    else:
        return 1 / x

#This will cause a ZeroDivisionError
result = function_with_uncommon_bug(0)