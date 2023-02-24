import struct

class BinaryParser:
    def decode(self, buffer, format):
        obj = {}
        offset = 0
        for field in format:
            field_type = field['type']
            field_len = field.get('len')
            if field_type == 'uint':
                if field_len:
                    uint_format = f'>u{field_len//8}'
                else:
                    uint_format = '>I'
                field_value = struct.unpack_from(uint_format, buffer, offset)[0]
                offset += field_len//8 if field_len else 4
            elif field_type == 'int':
                if field_len:
                    int_format = f'>i{field_len//8}'
                else:
                    int_format = '>i'
                field_value = struct.unpack_from(int_format, buffer, offset)[0]
                offset += field_len//8 if field_len else 4
            elif field_type == 'float':
                field_value = struct.unpack_from('>f', buffer, offset)[0]
                offset += 4
            elif field_type == 'ascii':
                field_value = buffer[offset:].split(b'\x00')[0].decode('ascii')
                offset += len(field_value.encode('ascii')) + 1
            else:
                raise ValueError(f'Invalid field type: {field_type}')
            obj[field['tag']] = field_value
        return obj
    
    def encode(self, obj, format):
        size = 0
        buffer = b''
        for field in format:
            field_tag = field['tag']
            field_type = field['type']
            field_len = field.get('len')
            if field_tag not in obj:
                raise ValueError(f'Missing field: {field_tag}')
            field_value = obj[field_tag]
            if field_type == 'uint':
                if field_len:
                    uint_format = f'>u{field_len//8}'
                    packed_value = struct.pack(uint_format, field_value)
                    size += field_len//8
                else:
                    packed_value = struct.pack('>I', field_value)
                    size += 4
            elif field_type == 'int':
                if field_len:
                    int_format = f'>i{field_len//8}'
                    packed_value = struct.pack(int_format, field_value)
                    size += field_len//8
                else:
                    packed_value = struct.pack('>i', field_value)
                    size += 4
            elif field_type == 'float':
                packed_value = struct.pack('>f', field_value)
                size += 4
            elif field_type == 'ascii':
                ascii_value = field_value.encode('ascii')
                packed_value = ascii_value + b'\x00'*(field_len-len(ascii_value)) if field_len else ascii_value + b'\x00'
                size += len(packed_value)*8
            else:
                raise ValueError(f'Invalid field type: {field_type}')
            buffer += packed_value
        return {'size': size, 'buffer': buffer}
    
if __name__ == '__main__':
    # Define el formato para codificar/decodificar los datos
    format1 = [
        {'tag': 'PTemp', 'type': 'int', 'len': 12},
        {'tag': 'BattVolt.value', 'type': 'int', 'len': 12},
        {'tag': 'WaterLevel', 'type': 'int', 'len': 8},
    ]

    # Define los datos a ser codificados/decodificados
    data = {'PTemp': 268, 'BattVolt.value': 224, 'WaterLevel': 115}

    # Crea una instancia de la clase BinaryParser
    bp = BinaryParser()

    # Codifica los datos
    encoded_data = bp.encode(data, format1)
    print('Encoded data:', encoded_data)

    # Decodifica los datos
    decoded_data = bp.decode(encoded_data, format1)
    print('Decoded data:', decoded_data)
