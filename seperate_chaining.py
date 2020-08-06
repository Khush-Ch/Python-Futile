class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class H:
    def __init__(self,size):
        self.map=[None]*size
        self.size=size
    def hash(self,element):
        index=element%self.size
        return index
    def insert(self,element):
        new=Node(element)
        index=self.hash(element)
        if self.map[index]==None:
            self.map[index]=new
        else:
            ptr=self.map[index]
            while ptr.next:
                ptr=ptr.next
            ptr.next=new
        print("Inserted at index: ",index)
    def search(self,element):
        index=self.hash(element)
        ptr=self.map[index]
        flag=0
        while ptr:
            if ptr.data==element:
                print("Found element!!")
                flag=1
                break
            ptr=ptr.next
        if flag==0:
            print("Element is not in the table")
    def delete(self,element):
        index=self.hash(element)
        ptr=self.map[index]
        preptr=None
        while ptr.data!=element:
            preptr=ptr
            ptr=ptr.next
        if preptr==None:
            self.map[index]=ptr.next
            print("Element deleted successfully!")
        elif ptr==None:
            print("Element is not in the table")
        else:
            preptr.next=ptr.next
            print("Element deleted successfully!")            
Obj=H(int(input("Enter the size of ur table: ")))
while True:
    s=int(input("1.Insert\n2.Delete\n3.Search\n4.Exit\n"))
    if s==1:
        Obj.insert(int(input("Enter the element to be inserted: ")))
    elif s==2:
        Obj.delete(int(input("Enter the element to be deleted: ")))
    elif s==3:
        Obj.search(int(input("Enter the element to be searched: ")))
    elif s==4:
        exit(0)
    else:
        print("Not in the choice")
