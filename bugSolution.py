def function_with_uncommon_bug(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "ZeroDivisionError"
    except TypeError as e:
        if isinstance(x,str):
            return f"TypeError: String cannot be divided: {e}"
        else:
            return f"Unexpected TypeError: {e}"

# Test Cases
print(function_with_uncommon_bug("hello")) # Output: TypeError: String cannot be divided: unsupported operand type(s) for /: 'int' and 'str'
print(function_with_uncommon_bug(0)) # Output: ZeroDivisionError
print(function_with_uncommon_bug(2)) # Output: 5.0