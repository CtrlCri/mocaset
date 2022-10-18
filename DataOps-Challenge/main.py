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
        """
        Decode

        This method decodes/deserializes a given frame; 
        convert a binary object to a dictionary object.

        Parameters: 
            - trama: bytearray, frame to deserialize
            - format: list, serialization format
    
        Returns a object: 
            - object: dictionary, "composition" 
            (frame deserialized into tag = value fields)
        """ 
        object = {}
        i = 0
        for f in format:           
            if f["type"] == "int" or f["type"] == "uint":
                n_bytes = self.__n_bytes(f["len"]) # call to a function to calculate number of bytes
            else: n_bytes = 4
            value = bytearray()
            value = trama[i:(i+n_bytes)] # takes the part of the frame that corresponds to the value in question
            object[f["tag"]] = int.from_bytes(value, byteorder="big") # decode value
            i += n_bytes # move frame index           

        return object

    def encode(self, object: dict, format: list):
        """
        Encode

        This method encodes/serializes a given frame;
          convert a dictionary object to a binary object.

        Parameters: 
            - object: dictionary 
            - format: list, serialization format
    
        Setter-method: 
            - _self.buffer: bytearray, frame serialized 
            - _self.size: int, frame bit size
        """ 
        data = bytearray()
        i = 0
        for item in object.values(): 
            if format[i]["type"] == "int" or format[i]["type"] == "uint":
                n_bytes = self.__n_bytes(format[i]["len"]) # call to a function to calculate number of bytes
            else: n_bytes = 4
            value = int(item).to_bytes(n_bytes, byteorder="big") # code value
            data += value # add binary data
            i += 1
        self.buffer = data # add binary data to buffer
        count = self.__c_bytes(format) * 8 # calculate bits
        self.size = count # add bit count to frame size
    
    def __n_bytes(self, len):
        if len <= 8: n = 1
        elif len <= 16: n =2
        else: n = 4
        
        return n

    def __c_bytes(self, format):
        count = 0
        for f in format:
            if f["type"] == "int" or f["type"] == "uint":
                count += self.__n_bytes(f["len"])
            else: count += 4
        return count    
   

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

    other_data = { "V0": 1, "V1": 2, "V2": 3 }
    other_format = [
        { "tag": "v0", "type": "int", "len": 8 },
        { "tag": "v1", "type": "int", "len": 8 },
        { "tag": "v2", "type": "int", "len": 8 }
        ]    


    # Encode
    bp = BinaryParser()
    
    #data, format = data_1, format_1 # example
    #data, format = data_2, format_2 # example
    data, format = other_data, other_format # other example


    bp.encode(data, format)
    data_encoded = bp.get_buffer()
    #print(data_encoded)
    print(hexlify(data_encoded))
    print(bp.get_size())
    # Decode
    data_decoded = bp.decode(data_encoded, format)
    print(data_decoded)



