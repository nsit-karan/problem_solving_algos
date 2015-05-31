# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Node:
    
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data
        
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newNext):
        self.next = newNext

class UnorderedList:
    
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
        
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        
        while(current != None):
            count = count + 1
            current = current.getNext()
            
        return count
        
    def search(self, item):
        current = self.head
        found = False
        
        while current != None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()
                
        return found
    
    def print_ulist(self):
        print 'printing the list'
        
        logger_str = ''
        current = self.head
        while current != None:
            logger_str = logger_str + str(current.getData()) + ' , '
            current = current.getNext()
        
        print logger_str

    def remove(self, item):
        current = self.head
        previous = None        
        found = False
        
        while current != None:
            if current.getData() == item:
                found = True
                break
            else:
                previous = current
                current = current.getNext()
        
        if found == False:
            print str(item) + ' : not found'
            return
        if previous == None:
            self.head = current.getNext()            
        else:
            previous.setNext(current.getNext())
            
    def append(self, item):
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
            
        current.setNext(Node(item))
            
        
