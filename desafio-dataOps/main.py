import pickle

#file = open("binary_file", "wb")
#data = []
#pickle.dump(data, file)
#file.close()

def asignation_item(item):

    with open("binary_file", "r+b") as f:
        results = pickle.loads(f.read()) 
        results.append(item)
        f.seek(0)  
        f.write(pickle.dumps(results)) 

     

#object_one = [268, 224, 115] #trama = "10C0E073"
#for item in object_one:
#    asignation_item(item)



if __name__ == "__main__":
    file = open("binary_file", "rb")
    redata = pickle.load(file)
    #redata = file.read()
    print(redata)
    file.close()
    print(hex(268)+hex(224)+hex(115))