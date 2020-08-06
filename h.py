class H:
    def __init__(self,size):
        self.size=size
        self.map=[None]*self.size
        self.count=0
    def hash(self,element):
        index=element%self.size
        return index
    def insert(self,element):
        if self.isfull() is False:
            self.count+=1
            index=self.hash(element)
            if self.map[index] is None:
                self.map[index]=element
            else:
                while self.map[index]!=None:
                    index=self.collision(index)
                self.map[index]=element
            print('Insert successfully at: ',index)
        else:
            print("HashTable is full")
            self.count-=1
    def collision(self,index):
        index=(index+1)%self.size
        return index
    def search(self,element):
        index=self.hash(element)
        while self.map[index]!=element:
            index=self.collision(index)
        if self.map[index]==element:
            return index
        else:
            print('ELement not found')
    def delete(self,element):
        if self.count!=0:
            index=self.search(element)
            self.map[index]=None
            print("Element deleted at: ",index)
            self.count-=1
        else:
            print("HashTable is empty")
    def isfull(self):
        if self.count==self.size:
            return True
        return False

Obj=H(int(input("Enter the size of ur table: ")))
while True:
    s=int(input("1.Insert\n2.Delete\n3.Search\n4.Exit\n"))
    if s==1:
        Obj.insert(int(input("Enter the element to be inserted: ")))
    elif s==2:
        Obj.delete(int(input("Enter the element to be deleted: ")))
    elif s==3:
        ans=Obj.search(int(input("Enter the element to be searched: ")))
        print("Element found at: ",ans)
    elif s==4:
        exit(0)
    else:
        print("Not in the choice")
