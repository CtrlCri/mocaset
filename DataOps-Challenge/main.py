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
        pass

    def encode(self, object: dict, format: list):
        # Serializar oject
        data = array("i")
        for item in object:  # Me quedo sólo con los valores y los ingreso en un array
            data.append( item[value] ) 
        self.buffer = data.tobytes
        # Obtener tamaño en bits
        count = 0
        for t in format:
            count += t["len"]
        self.size = count
    


if __name__ == "__main__":
    format_1 = [
        {"tag": "PTemp", "type": "int", "len": 12 },
        {"tag": "BattVolt.value", "type": "int", "len": 12 },
        {"tag": "WaterLevel", "type": "int", "len": 8 }
    ]
    data_1 = { "PTemp": 268, "BattVolt.value": 224, "WaterLevel": 115 }

    bp = BinaryParser()
    bp.encode(data_1, format_1)
    print(hexlify(bp.get_buffer()))
    print(bp.get_size())