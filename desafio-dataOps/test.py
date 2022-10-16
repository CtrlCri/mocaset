from array import array
from binascii import hexlify

data = array('i', [268, 224, 115])
data_bytes = data.tobytes()



if __name__ == "__main__":
    #print(data)
    #print(data_bytes)
    #print(hexlify(data_bytes))
    print(data[0])
