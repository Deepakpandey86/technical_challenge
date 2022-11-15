def getKey(obj: dict):
    keys = list(obj)
    if len(keys) != 1:
        raise Exception('either multiple keys or empty dict found')
    else:
        return keys[0]


def getNestedValue(obj: dict, key: str, isFound = False):
    # print(obj, key, isFound)
    if type(obj) is not dict and not isFound:
        return None
    if (isFound or (key in obj.keys())) :
        if type(obj[key]) is dict:
            return getNestedValue(obj[key], getKey(obj[key]), True)
        else:
            # print(f'obj[getKey(obj)]: {obj[getKey(obj)]}')
            return obj[getKey(obj)]
    else:
        nestedKey = getKey(obj)
        return getNestedValue(obj[nestedKey], key, False)

if __name__ == '__main__':
    obj = {'a': {'b': {'c': 'd'}}}
    value1 = getNestedValue(obj, 'a')
    value2 = getNestedValue(obj, 'b')
    value3 = getNestedValue(obj, 'c')
    print("input:a has output: " + value1)
    print("input:b has output: " + value2)
    print("input:c has output " + value3)
    object = {"x":{"y":{"z":"a"}}}
    value4 = getNestedValue(object, 'x')
    value5 = getNestedValue(object, 'y')
    value6 = getNestedValue(object, 'z')
    print("input:x has output "+ value4)
    print("input:y has output " + value5)
    print("input:z has output "+ value6)