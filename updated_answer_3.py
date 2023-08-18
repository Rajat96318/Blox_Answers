# Without using Library

def parse_json(json_str):
    index = 0

    def parse_value():
        nonlocal index
        char = json_str[index]
        if char == '"':
            return parse_string()
        elif char == '{':
            return parse_object()
        elif char == '[':
            return parse_array()
        elif char.isdigit() or char == '-':
            return parse_number()
        elif char == 't' or char == 'f':  
            return parse_boolean()
        elif char == 'n':
            return parse_null()

    def parse_string():
        nonlocal index
        index += 1
        start = index
        while index < len(json_str):
            if json_str[index] == '"':
                index += 1
                return json_str[start:index-1]
            index += 1

    def parse_object():
        nonlocal index
        index += 1
        obj = {}
        while index < len(json_str):
            if json_str[index] == '}':
                index += 1
                return obj
            key = parse_string()
            index += 1  # Skip ":"
            value = parse_value()
            obj[key] = value
            if json_str[index] == '}':
                index += 1
                return obj
            index += 1  # Skip ","

    def parse_array():
        nonlocal index
        index += 1
        arr = []
        while index < len(json_str):
            if json_str[index] == ']':
                index += 1
                return arr
            value = parse_value()
            arr.append(value)
            if json_str[index] == ']':
                index += 1
                return arr
            index += 1  # Skip ","

    def parse_number():
        nonlocal index
        start = index
        while index < len(json_str) and (json_str[index].isdigit() or json_str[index] in '+-.eE'):
            index += 1
        return (json_str[start:index])

    def parse_boolean():
        nonlocal index
        if json_str[index] == 't':
            index += 4
            return True
        else:
            index += 5
            return False

    def parse_null():
        nonlocal index
        index += 4
        return None

    return parse_value()


json_string = '{"string":"Hello, world!","number":42123456789098765432123456789,"float":1234567890123456789012345678901234567890.1234567890123456789012345678901234567890,"boolean":true,"null_value":null,"array":[1, 2, 3, "four", 5.5],"object":{"key1": "value1","key2": 42,"key3":[true, false, null]}}'

parsed_object = parse_json(json_string)
print(parsed_object)

