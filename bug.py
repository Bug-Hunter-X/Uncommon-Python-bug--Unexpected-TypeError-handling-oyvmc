def function_with_uncommon_bug(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "ZeroDivisionError"
    except TypeError:
        if isinstance(x,str):
            return "TypeError: String cannot be divided"
        else:
            return "Unexpected TypeError"

# This will raise a TypeError
print(function_with_uncommon_bug("hello"))

# This will raise a ZeroDivisionError
print(function_with_uncommon_bug(0))

# This will return a numerical value
print(function_with_uncommon_bug(2))