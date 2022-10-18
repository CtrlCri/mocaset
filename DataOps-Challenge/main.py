# Python
from binascii import hexlify
import struct

class BinaryParser():
    """
    v0.1.0 | [autor: Cristian Aramayo] | Primera versión
    """
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
            value = bytearray()
            # depends on the data type, the number of bytes is granted
            if f["type"] == "int" or f["type"] == "uint":
                n_bytes = self.__n_bytes(f["len"]) # call to a function to calculate number of bytes
                value = trama[i:(i+n_bytes)] # takes the part of the frame that corresponds to the value in question
                object[f["tag"]] = int.from_bytes(value, byteorder="big") # decode value
                
            elif f["type"] == "float": # different procedure if float 
                n_bytes = 4
                value = trama[i:(i+n_bytes)]               
                try:
                    object[f["tag"]] = struct.unpack("f", value) # decode value 
                except struct.error: 
                    print("The frame is limited to 32 bytes")
            elif f["type"] == "char": # different procedure if char                  
                n_bytes = 1
                value = trama[i:(i+n_bytes)]               
                object[f["tag"]] = value.decode("utf-8") # decode value 

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
            # depends on the data type, the number of bytes is granted 
            if format[i]["type"] == "int" or format[i]["type"] == "uint":
                n_bytes = self.__n_bytes(format[i]["len"]) # call to a function to calculate number of bytes
                value = int(item).to_bytes(n_bytes, byteorder="big") # code value
            
            elif format[i]["type"] == "float": # different procedure if float 
                n_bytes = 4
                value = struct.pack("f", item) # code value

            elif format[i]["type"] == "char": # different procedure if char
                n_bytes = 1
                value = bytearray(item, "utf-8") # code value

            data += value # add binary data
            i += 1
        self.buffer = data # add binary data to buffer
        count = self.__c_bytes(format) * 8 # calculate bits
        self.size = count # add bit count to frame size
    
    def __n_bytes(self, len):
        # only for data type int and uint
        if len <= 8: n = 1
        elif len <= 16: n =2
        else: n = 4
        
        return n

    def __c_bytes(self, format):
        count = 0
        for f in format:
            if f["type"] == "int" or f["type"] == "uint":
                count += self.__n_bytes(f["len"])
            elif f["type"] == "float":
                count += 4
            elif f["type"] == "char":
                count += 1

        return count    
   

if __name__ == "__main__":
    # Ejemplos
    format_1 = [
        {"tag": "PTemp", "type": "int", "len": 12 },
        {"tag": "BattVolt.value", "type": "int", "len": 8 },
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
      
    format_3 = [
        { "tag": "var0.Temp_C_2_Avg", "type": "float" },
        { "tag": "var0.DOppm", "type": "float" },
        { "tag": "var0.TurbNTU", "type": "float" },
        { "tag": "var0.Lvl_corr_Avg", "type": "float" },
        { "tag": "var0.Cond_Avg", "type": "float" },
        { "tag": "var0.pH_Avg", "type": "float" },
        { "tag": "var0.TimeStamp", "type": "float" },
        { "tag": "var0.BattV_Avg", "type": "float" }
        ] #until 32Bytes
    data_3 = { "var0.Temp_C_2_Avg": 2.5, "var0.DOppm": 3.5, "var0.TurbNTU": 1.5,"var0.Lvl_corr_Avg": 2.5, 
    "var0.pH_Avg": 0.5, "var0.TimeStamp": 5.5,"var0.BattV_Avg": 4.5, "var0.BattV_Min": 3.5}

    format_4 = [
        {"tag": "Initial.LastName", "type": "char"},
        {"tag": "Age", "type": "int", "len": 8},
        {"tag": "salary", "type": "float"}
    ]
    data_4 = {"Initial.LastName": "A", "Age": 39, "Salary": 1411.9}

    format_5 = [
        { "tag": "var0.Temp_C_2_Avg", "type": "float" },
        { "tag": "var0.DOppm", "type": "float" },
        { "tag": "var0.TurbNTU", "type": "float" },
        { "tag": "var0.Lvl_corr_Avg", "type": "float" },
        { "tag": "var0.Cond_Avg", "type": "float" },
        { "tag": "var0.pH_Avg", "type": "float" },
        { "tag": "var0.TimeStamp", "type": "float" },
        { "tag": "var0.BattV_Avg", "type": "float" },
        { "tag": "var0.BattV_Min", "type": "float" },
        { "tag": "var1.Temp_C_2_Avg", "type": "float" }
        ] #until 32Bytes
    data_5 = { "var0.Temp_C_2_Avg": 2.5, "var0.DOppm": 3.5, "var0.TurbNTU": 1.5,"var0.Lvl_corr_Avg": 2.5, 
    "var0.pH_Avg": 0.5, "var0.TimeStamp": 5.5,"var0.BattV_Avg": 4.5, "var0.BattV_Min": 3.5,
    "var0.BattV_Min": 6.2, "var1.Temp_C_2_Avg": 7.4}

    other_data = { "V0": 1, "V1": 2, "V2": 3 }
    other_format = [
        { "tag": "V0", "type": "int", "len": 8 },
        { "tag": "V1", "type": "int", "len": 8 },
        { "tag": "V2", "type": "int", "len": 8 }
        ]    


    # Encode
    bp = BinaryParser()
    
    #data, format = data_1, format_1 # example
    #data, format = data_2, format_2 # example
    #data, format = data_3, format_3 # example
    #data, format = data_4, format_4 # example mix
    data, format = data_5, format_5 # example with struct.error

    #data, format = other_data, other_format # other example


    bp.encode(data, format)
    data_encoded = bp.get_buffer()
    #print(data_encoded)
    print(hexlify(data_encoded))
    print(bp.get_size())
    # Decode
    data_decoded = bp.decode(data_encoded, format)
    print(data_decoded)



