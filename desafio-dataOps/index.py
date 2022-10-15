
# def special_tree( values, k ) :
	####### DO NOT MODIFY THE CODE BELOW #######
	#myTree = MySpecialTree(values)
	#soln = []
	#for val in range(k):
	#	soln.append(myTree.pop_max_value())

	#return soln
	####### DO NOT MODIFY THE CODE ABOVE #######

class BinaryParser():
    # def __init__(self, values=None):
    #    self.data = values or []
    #    for x in range(len(values)//2, -1, -1):
    #        self.__max_treeify__(x)
    
    def decode(buffer, format):
        object = {}
        #ToDo
        return object
        
    def encode(_object, format):
        buffer = "seraa" #Buffer.alloc(?)
        # ToDo
        size = "seraaa" #
        return { size, buffer };

    """     
    def parent(self, x):
        return x >> 1
            
    def left_child(self, x):
        return (x << 1) + 1
            
    def right_child(self, x):
        return (x << 1) + 2
        
    def __max_treeify__(self, x):
        if self.right_child(x) in range(len(self.data)):
         
            if self.data[self.right_child(x)] > self.data[self.parent(x)]:
                self.data[self.parent(x)], self.data[self.right_child(x)] = self.data[self.right_child(x)], self.data[self.parent(x)]
            
            if self.data[self.left_child(x)] > self.data[self.parent(x)]:
                self.data[self.parent(x)], self.data[self.left_child(x)] = self.data[self.left_child(x)], self.data[self.parent(x)]

                
         
    
    def pop_max_value(self):
        result = self.data.pop(0)
        for x in range(len(self.data)//2, -1 ,-1):
            self.__max_treeify__(x)

        return result
"""
if __name__ == "__main__":
    #values = [1, 8, 3, 0, 4, 2, 9,]
    #k = 3
    #myTree = MySpecialTree(values)
    #print(myTree.data)
    #print(special_tree(values, k))

    format1 = [
        { tag: "PTemp", type: "int", len: 12 },
        { tag: "BattVolt.value", type: "int", len: 12 },
        { tag: "WaterLevel", type: "int", len: 8 }
        ]
    data = { "PTemp": 268, "BattVolt.value": 224, "WaterLevel": 115 }
    bp = new BinaryParser()
    dataEncoded = bp.encode(data, format1)
    print(dataEncoded.buffer.toString('hex')); #prints 10C0E073
    print(dataEncoded.size); #prints 32
    dataDecoded = bp.decode(dataEncoded.buffer, format1)
    print(dataDecoded) //prints { PTemp: 268, ‘BattVolt.value’: 224, WaterLevel: 115 }
 

    