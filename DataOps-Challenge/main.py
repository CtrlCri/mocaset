from array import array
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
        # Deserializar trama en Array
        data = array("i")
        data.frombytes(trama)
        # Deserializar en Object
        _object = {}


        return data

    def encode(self, object: dict, format: list):
        # Serializar oject
        data = array("i")
        for item in object.values():  # Me quedo sólo con los valores y los ingreso en un array
            data.append(item) 
        self.buffer = data.tobytes()
        # Obtener tamaño en bits
        count = 0
        for f in format:
            count += f["len"]
        self.size = count
    


if __name__ == "__main__":
    format_1 = [
        {"tag": "PTemp", "type": "int", "len": 12 },
        {"tag": "BattVolt.value", "type": "int", "len": 12 },
        {"tag": "WaterLevel", "type": "int", "len": 8 }
    ]
    data_1 = { "PTemp": 268, "BattVolt.value": 224, "WaterLevel": 115 }
    # Encode
    bp = BinaryParser()
    bp.encode(data_1, format_1)
    data_encoded = bp.get_buffer()
    print(hexlify(data_encoded))
    print(bp.get_size())
    # Decode
    data_decoded = bp.decode(data_encoded, format_1)
    print(data_decoded)



