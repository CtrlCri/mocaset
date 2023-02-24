import struct
from binascii import hexlify

class BinaryParser:
    def __init__(self, byte_order="big"):
        self.byte_order = byte_order

    def decode(self, buffer, format):
        _object = {}
        offset = 0
        for field in format:
            if field["type"] == "int":
                size = field["len"] // 8
                value = struct.unpack(f">{self.byte_order}{size}s", buffer[offset:offset+size])[0]
                _object[field["tag"]] = int.from_bytes(value, byteorder=self.byte_order, signed=True)
                offset += size
            elif field["type"] == "uint":
                size = field["len"] // 8
                value = struct.unpack(f">{self.byte_order}{size}s", buffer[offset:offset+size])[0]
                _object[field["tag"]] = int.from_bytes(value, byteorder=self.byte_order, signed=False)
                offset += size
            elif field["type"] == "float":
                size = field["len"] // 8
                value = struct.unpack(f">{self.byte_order}f", buffer[offset:offset+size])[0]
                _object[field["tag"]] = value
                offset += size
            elif field["type"] == "ascii":
                value = b""
                while buffer[offset] != 0x00:
                    value += bytes([buffer[offset]])
                    offset += 1
                _object[field["tag"]] = value.decode("ascii")
                offset += 1
        return _object

    def encode(self, _object, format):
        size = 0
        for field in format:
            if field["type"] == "int":
                size += field["len"] // 8
            elif field["type"] == "uint":
                size += field["len"] // 8
            elif field["type"] == "float":
                size += field["len"] // 8
            elif field["type"] == "ascii":
                size += len(_object[field["tag"]]) + 1
        buffer = bytearray(size)
        offset = 0
        for field in format:
            if field["type"] == "int":
                value = int(_object[field["tag"]]).to_bytes(field["len"] // 8, byteorder=self.byte_order, signed=True)
                buffer[offset:offset+len(value)] = value
                offset += len(value)
            elif field["type"] == "uint":
                value = int(_object[field["tag"]]).to_bytes(field["len"] // 8, byteorder=self.byte_order, signed=False)
                buffer[offset:offset+len(value)] = value
                offset += len(value)
            elif field["type"] == "float":
                value = struct.pack(f">{self.byte_order}f", float(_object[field["tag"]]))
                buffer[offset:offset+len(value)] = value
                offset += len(value)
            elif field["type"] == "ascii":
                value = _object[field["tag"]].encode("ascii") + b"\x00"
                buffer[offset:offset+len(value)] = value
                offset += len(value)
        return {"size": size*8, "buffer": buffer}

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
    
    data, format = data_1, format_1 # example
    #data, format = data_2, format_2 # example
    #data, format = data_3, format_3 # example
    #data, format = data_4, format_4 # example mix
    #data, format = data_5, format_5 # example with struct.error

    #data, format = other_data, other_format # other example


    bp.encode(data, format)
    data_encoded = bp.get_buffer()
    #print(data_encoded)
    print(hexlify(data_encoded))
    print(bp.get_size())
    # Decode
    data_decoded = bp.decode(data_encoded, format)
    print(data_decoded)



