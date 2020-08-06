class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None
    def insertion(self,value):
        new=Node(value)
        if self.start==None:
            self.start=new
        else:
            s=int(input("1.Starting\n2.Middle\n3.End"))
            if s==1:
                new.next=self.start
                self.start=new
            elif s==2:
                c=int(input("1.By position\n2.Before a number"))
                ptr=self.start
                if c==1:
                    p=int(input("Give the position"))
                    for i in range(p-2):
                        ptr=ptr.next
                    new.next=ptr.next
                    ptr.next=new

                elif c==2:
                    preptr=self.start
                    p=int(input("Give the element value"))
                    while ptr.data!=p:
                        preptr=ptr
                        ptr=ptr.next
                    preptr.next=new
                    new.next=ptr
            elif s==3:
                ptr=self.start
                while ptr.next:
                    ptr=ptr.next
                ptr.next=new
    def printing(self):
        ptr=self.start
        while ptr:
            print(ptr.data)
            ptr=ptr.next
    def deletion(self):
        pass


obj=LinkedList()
while True:
    a=int(input("1.Insertion\n2.Deletion\n3.Printing\n4.Exit\n"))
    if a==1:
        obj.insertion(int(input("Enter the value")))
    elif a==2:
        pass
    elif a==3:
        obj.printing()
    elif a==4:
        exit(0)








                
                        
                                                
                
