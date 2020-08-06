bt=['']*100
def printing():
        print("Binary Tree: \n",bt)
def insert():
        if bt[0]=='':
                bt[0]=int(input("Enter the value to be inserted: "))
        else:
                printing()
                par=int(input("Give the parent whose child you want to insert: "))
                for x in range(len(bt)) :
                        if bt[x]==par:
                                i=x
                                break
                parent=(i-1)//2
                lchild=2*i+1
                rchild=2*i+2
                choice=0
                if bt[lchild]=='' and bt[rchild]=='':
                        choice=int(input("Both left and right children are free. Where do you want to insert\n1.Left child\n2.Right child"))
                elif bt[lchild]=='' and bt[rchild]!='':
                        print("Only left child is free")
                        choice=1
                elif bt[lchild]!='' and bt[rchild]=='':
                        print("Only right child is free")
                        choice=2
                elif bt[lchild]!='' and bt[rchild]!='':
                        print("No free child")
                if choice!=0:
                        value=int(input("Enter the value to be inserted: "))
                        if choice==1:
                                bt[lchild]=value
                        elif choice==2:
                                bt[rchild]=value
def inorder(i):
        if bt[i]!='':
                inorder(2*i+1)
                print(bt[i])
                inorder(2*i+2)

def preorder(i):
        if bt[i]!='':
                print(bt[i])
                preorder(2*i+1)
                preorder(2*i+2)

def postorder(i):
        if bt[i]!='':
                postorder(2*i+1)
                postorder(2*i+2)
                print(bt[i])
while(1):
        option=int(input("1.Insert\n2.Inorder\n3.Preorder\n4.Postorder\n5.Print\n6.Exit "))
        if (option==1):
                insert()
        elif option==2:
                inorder(0)
        elif option==3:
                preorder(0)
        elif option==4:
                postorder(0)
        elif option==5:
                printing()
        elif option==6:
                exit(0)
        else:
                print("Not in the choice")
