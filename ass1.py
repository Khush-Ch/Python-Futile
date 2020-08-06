import math
class h:
    hash_table=list()

    def __init__(self,t):
        self.table_size=t
        self.collisions=0
        self.number=0
        for i in range(self.table_size):
            h.hash_table.insert(i,None)

    def insert(self,value):
        self.number+=1
        self.Hash(value)
        while h.hash_table[self.index]!=None:
            self.collisions+=1
            self.index=self.collision(value)

        h.hash_table[self.index]=value

    def Hash(self,value):
        self.index=value%self.table_size

    def collision(self,value):
        offset=math.floor(value/self.table_size)
        index=(offset+self.index)%self.table_size
        return index

    def search(self,value):
        self.Hash(value)
        count=0
        while h.hash_table[self.index]!=value:
            self.index=self.collision(value)
            count+=1
            if count==self.collisions:
                break

        if h.hash_table[self.index]==value:
            print("The Key has been found at the address: ",self.index)

        else:
            print("Key doesnt exist in the hash table")

obj=h(19)
while True:
    choice=int(input("\nWhich operation do you want to perform?\n1.Insert\n2.Search\n3.Exit\n"))
    if choice==1:
        key=int(input("Enter the key: "))
        obj.insert(key)

    elif choice==2:
        key=int(input("Enter the key you want to search for: "))
        obj.search(key)

    elif choice==3:
        print("The number of collisions that took place were: ",obj.collisions)
        print("The density of the hash table is: ",(obj.collisions/obj.table_size))
        break
    else:
        print("\nEnter an appropriate option")
               
        
        
