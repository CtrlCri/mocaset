import struct
from binascii import hexlify

class BinaryParser:
    """
    Clase para codificar y decodificar estructuras de datos en tramas binarias
    según un formato definido.

    Atributos:
    ----------
    endian: str
        Orden de bytes utilizado en la codificación/decodificación de los datos. 
        Puede ser 'little' (poco endian) o 'big' (gran endian). Por defecto es 'big'.

    Métodos:
    --------
    encode(data, format)
        Codifica los datos de un objeto de acuerdo al formato especificado.

    decode(buffer, format)
        Decodifica los datos de una trama binaria de acuerdo al formato especificado.
    """

    def __init__(self, endian='big'):
        """
        Constructor de la clase BinaryParser.

        Parámetros:
        -----------
        endian: str, opcional
            Orden de bytes utilizado en la codificación/decodificación de los datos. 
            Puede ser 'little' (poco endian) o 'big' (gran endian). Por defecto es 'big'.
        """
        self.endian = endian

def encode(self, _object, format):
    """
    Codifica un objeto _object de acuerdo al formato especificado.

    Parámetros:
    _object (dict): Objeto a codificar.
    format (list): Formato de codificación.

    Retorna:
    dict: Tamaño en bits de la trama y la trama binaria codificada.

    Raises:
    TypeError: Si algún tipo de dato del objeto a codificar no coincide con el formato especificado.

    """

    # Inicializar el tamaño de la trama en bits y la trama binaria
    size = 0
    buffer = bytearray()

    # Codificar cada campo del objeto según el formato
    for field in format:
        tag = field['tag']
        data_type = field['type']
        data_len = field['len']

        # Verificar si el campo existe en el objeto
        if tag not in _object:
            raise TypeError(f"El campo {tag} no existe en el objeto a codificar.")

        # Obtener el valor del campo
        value = _object[tag]

        # Verificar el tipo de dato del campo
        if data_type == 'uint':
            # Codificar un entero sin signo de longitud variable
            encoded_value, value_size = self.encode_uint(value, data_len)
        elif data_type == 'int':
            # Codificar un entero con signo de longitud variable
            encoded_value, value_size = self.encode_int(value, data_len)
        elif data_type == 'float':
            # Codificar un punto flotante de precisión simple
            encoded_value, value_size = self.encode_float(value)
        elif data_type == 'ascii':
            # Codificar una cadena ASCII terminada en #0
            encoded_value, value_size = self.encode_ascii(value)
        else:
            raise TypeError(f"Tipo de dato no soportado: {data_type}")

        # Agregar el valor codificado a la trama binaria
        buffer += encoded_value

        # Actualizar el tamaño de la trama en bits
        size += value_size

    # Retornar el tamaño de la trama en bits y la trama binaria codificada
    return {'size': size, 'buffer': bytes(buffer)}


if __name__ == "__main__":
    # Definir formato de la trama
    format1 = [
        { "tag": "PTemp", "type": "int", "len": 12 },
        { "tag": "BattVolt.value", "type": "int", "len": 12 },
        { "tag": "WaterLevel", "type": "int", "len": 8 },
    ]
    
    # Definir datos a serializar
    data = { "PTemp": 268, "BattVolt.value": 224, "WaterLevel": 115 }
    
    # Instanciar objeto BinaryParser
    bp = BinaryParser()
    
    # Codificar datos en formato binario
    data_encoded = bp.encode(data, format1)
    
    # Imprimir resultado
    print("Trama codificada:", data_encoded["buffer"].hex())
    print("Tamaño en bits:", data_encoded["size"])
    
    # Decodificar trama binaria
    data_decoded = bp.decode(data_encoded["buffer"], format1)
    
    # Imprimir resultado
    print("Datos decodificados:", data_decoded)
