from array import array

def encode(object: dict, format: list):
    buuffer = bytearray()
    i = 0
    for item in object.values():
        value = array("i"[item])
        buuffer[i] = value.tobytes()
        i += 1
    return buuffer

if __name__ == "__main__":
    data_1 = { 
    "Var1": 258, 
    "Var2": 224, 
    "Var3": 5 
    }
    format_1 = [

        {"tag": "var1", "type": "int", "len": 12},
        {"tag": "var2", "type": "float"},
        {"tag": "var3", "type": "uint", "len": 2}
    ]
    data_encoded = encode(data_1, format_1)

    print(data_encoded)