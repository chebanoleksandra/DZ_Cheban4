result = []


def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    if b == 0:
        raise ZeroDivisionError
    if type(a) == "str" or type(a) == 'list':
        raise TypeError
    return a/b


data = {10: 2, 2: 5, "123": 4, 18: 0, '[]': 15, 8: 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except TypeError:
        print('Dictionary Error')
    except ValueError:
        print('Value Error')
    except ZeroDivisionError:
        print("You can't divide by zero")


print(result)
