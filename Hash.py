elements=list(map(int,input("Enter Elements: ").split()))
table_size=int(input("Enter Table Size: "))
class h:
    hash_table=dict()
    def __init__(self,table_size):
        for i in range(table_size+1):
            h.hash_table[i]=None
        self.table_size=table_size

    def Hash(self,elements):
        self.elements=elements
        for i in elements:
            self.i=i
            index=i%self.table_size
            while h.hash_table[index]!=None:
                index=self.collision(index)
                
            h.hash_table[index]=i

    def collision(self,index):
        print("You have Encountered a collision")
        choice=int(input("How would you like to resolve it?\n1.LinearProbing\n2.Quadratic Probing\n3.Double Hashing\n"))
        if(choice==1):
            return self.linear(index)
        if(choice==2):
            return self.quadratic(index)
        if(choice==3):
            return self.double(index)
        else:
            self.collision(index)
    def linear(self,index):
        index=(index+1)%self.table_size
        return index
    
    def quadratic(self,index):
        j=2
        index=(index+(j**2))%self.table_size
        return index
    
    def double(self,index):
        index2=7-(self.i%7)
        index=(index+index2)%self.table_size

        return index
    
        
    def print_table(self):
        for i in h.hash_table:
            print(i," ",h.hash_table[i])

Obj=h(table_size)
Obj.Hash(elements)
Obj.print_table()
            
