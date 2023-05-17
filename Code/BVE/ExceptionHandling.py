def division(number):
    try:
        if number == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / number
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        return "No, not 13!"


def division2(number):
    try:
        if number == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / number
    except ZeroDivisionError:
        out = "Enter a number other than zero"
    except TypeError:
        out = "Enter a numerical value"
    except ValueError:
        out = "No, not 13!"
    return "new " + out


##########
print(division(10))
print(division(0))
print(division(13))
print(division2("hello"))