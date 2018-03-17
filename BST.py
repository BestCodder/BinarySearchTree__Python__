class Node:
    def __init__(self,data):
        self.Data=data
        self.Left=None
        self.Right=None
        self.Parrent=None
class BinaryTree:
    
    Root=None

    def Insert(self,item):
        if self.Root == None:
            self.Root=Node(item)
        else:
            new_node=self.Root
            parrent=new_node
            while True:
                if new_node==None:
                    new_node=Node(item)
                    new_node.Parrent=parrent
                    break
                if new_node.Data<item:
                    if new_node.Right == None:
                        new_node.Right=Node(item)
                        new_node.Right.Parrent=parrent
                        break
                    new_node=new_node.Right
                    parrent=new_node
                elif new_node.Data>item:
                    if new_node.Left == None:
                        new_node.Left=Node(item)
                        new_node.Left.Parrent=parrent
                        break
                    new_node=new_node.Left
                    parrent=new_node
        
    def Get_Node(self,item):
        new_node=self.Root
        while True:
            if new_node.Data==item:
                return new_node
            if new_node.Data<item:
                new_node=new_node.Right
            if new_node.Data>item:
                new_node=new_node.Left
            if new_node == None:
                return None
    
    def LCA(self,item1,item2):
        if ((self.Root.Data-item1)*(self.Root.Data-item2)<0):
            return self.Root.Data
        elif item1==self.Root.Data:
            return item1
        elif item2==self.Root.Data:
            return item2
        elif item1>self.Root.Data and item2>self.Root.Data:
            self.Root=self.Root.Right
        elif item1<self.Root.Data and item2<self.Root.Data:
            self.Root=self.Root.Left
        return self.LCA(item1,item2)   

    def Clear(self):
        self.Root=None
    
    def InOrder(self,root):
        if root is None:
            return 
        print(root.Data)
        self.InOrder(root.Left)
        self.InOrder(root.Right)

    def PostOrder(self,root):
        if root is None:
            return 
        self.InOrder(root.Left)
        self.InOrder(root.Right)
        print(root.Data)

    def PreOrder(self,root):
        if root is None:
            return 
        self.InOrder(root.Left)
        print(root.Data)
        self.InOrder(root.Right)
    
    def Get_Min(self):
        new_node=self.Root
        while not new_node.Left == None:
            new_node=new_node.Left
        return new_node.Data

    def Get_Max(self):
        new_node=self.Root
        while not new_node.Right == None:
            new_node=new_node.Right
        return new_node.Data

    def Delete(self,node):
        if node.Right == None and node.Left == None:
            if not node.Parrent == None:
                if node.Data>node.Parrent.Data:
                    node.Parrent.Right=None
                if node.Data<node.Parrent.Data:
                    node.Parrent.Left=None
            else:self.Clear()   
        else:
            temp=node
            res=temp.Data
            while not temp.Right == None:
                temp=temp.Right
                res=temp.Data
            if not temp.Left == None:
                temp=temp.Left
            node.Data=res
            

bst=BinaryTree()
bst.Insert(10)
bst.Insert(15)
bst.Insert(13)
bst.Insert(16)
bst.Insert(5)
bst.Insert(6)
bst.Insert(4)
bst.Delete(bst.Get_Node(4))
bst.Delete(bst.Get_Node(16))
print('InOrder :')
bst.InOrder(bst.Get_Node(10))
print('\nPreOrder :')
bst.PreOrder(bst.Get_Node(10))
print('\nPostOrder :')
bst.PostOrder(bst.Get_Node(10))
print("\nMax : ",bst.Get_Max())
print("\nMin : ",bst.Get_Min())
