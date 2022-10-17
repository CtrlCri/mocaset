#from array import array
from binascii import hexlify

def encode(object: dict, format: list):
    buffer = bytearray(len(format))
    #values = ""
    i = 0
    for item in object.values():
        buffer[i] = item
        i += 1
        #print(item)
        #values += bin(item)[2:]
    #print(values)
    count = 0    
    for f in format:
        count += f["len"]
    size = count    
    #buuffer = bytearray(values, 'utf-8')
    return buffer, size

def decode(trama: bytearray, format:list):

    for element in trama:
        print(element)



if __name__ == "__main__":
    data_1 = { 
    "Var1": 255, 
    "Var2": 224, 
    "Var3": 115 
    }   
    format_1 = [

        {"tag": "var1", "type": "int", "len": 12},
        {"tag": "var2", "type": "int", "len": 12},
        {"tag": "var3", "type": "int", "len": 8}
    ]
    data_encoded, size = encode(data_1, format_1)
    print(data_encoded)
    print( hexlify(data_encoded) )
    print(size)
    print()
    decode(data_encoded, format_1)
    #print(int.from_bytes(data_encoded, "little"))
