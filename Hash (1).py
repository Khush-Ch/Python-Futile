table_size=int(input("Enter Table Size: "))
choice=int(input("In case you encounter a collision, how would you like to resolve it?\n1.Linear Probing\n2.Quadratic Probing\n3.Double Hashing\n"))

class h:
    hash_table=dict()
    def __init__(self,table_size,choice):
        self.choice=choice
        for i in range(table_size+1):
            h.hash_table[i]=None
        self.table_size=table_size

    def insert(self,value):
        index=self.Hash(value)
        while h.hash_table[index]!=None:
            if ((index==self.table_size) or (index==self.table_size)):
                index=0
                if h.hash_table[index]==None:
                    break
            index=self.collision(index)
        h.hash_table[index]=value

    def Hash(self,element):
            index=element%self.table_size
            return index       
            

    def collision(self,index):
        if(self.choice==1):
            return self.linear(index)
        if(self.choice==2):
            return self.quadratic(index)
        if(self.choice==3):
            return self.double(index)
        else:
            self.collision(index)
            
    def linear(self,index):
        index=(index+1)%self.table_size
        return index
    
    def quadratic(self,index):
        j=1
        index=(index+(j**2))%self.table_size
        j+=1
        return index
    
    def double(self,index):
        index2=7-(self.i%7)
        index=(index+index2)%self.table_size
        return index
    
        
    def search(self,element):
        if len(h.hash_table)==0:
            print("The Hash Table is Empty")
            return 0
        index=self.Hash(element)
        new_index=index
        if h.hash_table[index]!=element:
            while True:
                if ((index==self.table_size) or (index==self.table_size)):
                    new_index=0
                    if h.hash_table[new_index]==None:
                        break
                else:
                  new_index=self.collision(new_index)
                  
                if h.hash_table[new_index]==element:
                    break
        
        if h.hash_table[new_index]==element:
            print("ELement was placed at position: ",(new_index))
        else:
            print("Element Doesn't Exist in the Hash Table")
        

Obj=h(table_size,choice)
while True:
    option=int(input("Which operation do you want to perform?\n1.Save an element\n2.Search for an element\n3.Exit\n"))
    if option==1:
        key=int(input("Enter Value: "))
        Obj.insert(key)
    elif(option==2):
        key=int(input("Enter Value: "))
        Obj.search(key)
    elif(option==3):
        break
    else:
        print("Select a correct option")
        
print(h.hash_table)            
