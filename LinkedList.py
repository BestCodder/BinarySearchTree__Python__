class Node:
    def __init__(self,data):
        self.Data=data
        self.Prev=None
        self.Next=None

class LinkedList:
    first=Node(None)
    def Insert_First(self,item):
        if self.first.Data==None:
            self.first.Data=item
        else:
            new_node=Node(item)
            self.first.Prev=new_node
            new_node.Next=self.first
            self.first=new_node

    def Insert_Last(self,item):
        if self.first.Data==None:
            self.first.Data=item
        else:
            ch_node=self.first
            while not ch_node.Next==None:
                ch_node=ch_node.Next
            new_node=Node(item)
            new_node.Prev=ch_node
            ch_node.Next=new_node

    def Remove_First(self):
        if self.first.Data==None:
            print("|!| List is empty |!|")
        else:
            self.first=self.first.Next
            self.first.Prev=None

    def Remove_Last(self):
        if self.first.Data==None:
            print("|!| List is empty |!|")
        else:      
            ch_node=self.first
            while not ch_node.Next==None:
                ch_node=ch_node.Next
            ch_node.Prev.Next=None

    def Remove_By_Value(self,item):
        if self.first.Data==None:
            print("|!| List is empty |!|")
        ch_node=self.first
        while not ch_node==None:
            if ch_node.Data==item:
                if not ch_node.Prev==None:
                    ch_node.Prev.Next=ch_node.Next
                if not ch_node.Next==None:
                    ch_node.Next.Prev=ch_node.Prev
                return
            else:
                ch_node=ch_node.Next
        print("|!| Item not found |!|")
