from binascii import hexlify

class BinaryParser():
    def __init__(self) -> None:
        self.buffer: bytearray
        self.size: int
    
    def get_buffer(self):
        return self.buffer
    
    def get_size(self):
        return self.size

    def decode(self, trama: bytearray, format: list):
 
        _object = {}
        i = 0
        for f in format:
           
            n_bytes = self.__n_bytes(f["len"])
            value = bytearray()
           
            value = trama[i:(i+n_bytes)]
                
            _object[f["tag"]] = int.from_bytes(value, byteorder="big")
            i += n_bytes            

        return _object

    def __n_bytes(self, len):
        if len <= 8: n = 1
        elif len <= 16: n =2
        else: n = 4
        return n

    def encode(self, object: dict, format: list):

        data = bytearray()

        i = 0
        for item in object.values(): 
            n_bytes = self.__n_bytes(format[i]["len"])
            value = int(item).to_bytes(n_bytes, byteorder="big")
            data += value 
            i += 1
        self.buffer = data
        
        count = 0
        for f in format:
            if f["type"] == "int" or f["type"] == "uint":
                count += f["len"]
            elif f["type"] == "float":
                    count += 32 
        self.size = count
    
   

if __name__ == "__main__":
    # Ejemplos
    format_1 = [
        {"tag": "PTemp", "type": "int", "len": 12 },
        {"tag": "BattVolt.value", "type": "int", "len": 12 },
        {"tag": "WaterLevel", "type": "int", "len": 8 }
    ]
    data_1 = { "PTemp": 268, "BattVolt.value": 224, "WaterLevel": 115 }
    
    format_2 = [
        { "tag": "var0.value", "type": "uint", "len": 2 },
        { "tag": "var1.value", "type": "uint", "len": 2 },
        { "tag": "var2.value", "type": "uint", "len": 7 },
        { "tag": "var3.value", "type": "uint", "len": 11 },
        { "tag": "var4.value", "type": "int", "len": 10 },
        { "tag": "var5.value", "type": "uint", "len": 16 },
        { "tag": "var6.value", "type": "float" },
        { "tag": "var7.value", "type": "uint", "len": 16 },
        { "tag": "var8.value", "type": "uint", "len": 32 },
        { "tag": "var9.value", "type": "uint", "len": 8 }
        ] 
    data_2 = { "var0.value": 2, "var1.value": 3, "var2.value": 1,"var3.value": 255, 
    "var4.value": 222, "var5.value": 2255,"var6.value": 2.2, "var7.value": 3150, 
    "var8.value": 111125, "var9.value": 147}


    # Encode
    bp = BinaryParser()
    
    data, format = data_1, format_1 # test1
    #data, format = data_2, format_2 # test2

    bp.encode(data, format)
    data_encoded = bp.get_buffer()
    print(data_encoded)
    print(hexlify(data_encoded))
    print(bp.get_size())
    # Decode
    data_decoded = bp.decode(data_encoded, format)
    print(data_decoded)



