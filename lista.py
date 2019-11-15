''' Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br) IF969 --
Algoritmos e Estruturas de Dados

Autor:    Saulo de Sousa Joseph
Email:    ssj2@cin.ufpe.br
Data:        10/09/2019

Descricao:  lista de monitoria Q1

Licenca: The MIT License (MIT)
'''


class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__previous = None

    def getNext(self):
        return self.__next
    
    def setNext(self, next):
        self.__next = next
    
    def getPrevious(self):
        return self.__previous
    
    def setPrevious(self, previous):
        self.__previous = previous
    
    def getValue(self):
        return self.__value
    
    def setValue(self, value):
        self.__value = value
       
class DoublyLinkedList:
    def __init__(self, value = False):
        self.__head = None
        self.__tail = None
        self.__length = -1
        if(value):
            self.add(value)
        
    def __str__(self):
        return self.show()
    
    def __repr__(self):        
        return 'DoublyLinkedList([' + self.show() + '])'
    
    def increaseLength(self):
        self.__length += 1
        
    def decreaseLength(self):
        self.__length -= 1
        
    def getLength(self):
        return self.__length
    
    def getHead(self):
        return self.__head
    
    def getTail(self):
        return self.__tail
    
    def setHead(self, head):
        self.__head = head
    
    def setTail(self, tail):
        self.__tail = tail
        
    def __getitem__(self, index):
        return self.getNodeByIndex(index).getValue()
    
    def getNodeByIndex(self, index):
        if(index > self.getLength()):
            raise IndexError('That was no valid index')
        currentNode = self.getHead()
        current = 0
        while(current < index):
            currentNode = currentNode.getNext()
            current += 1
        return currentNode   
    
    def __setitem__(self, index, value):
        self.getNodeByIndex(index).setValue(value)
        
    def append(self, value):
        self.insert(value)
        
    def indice(self, value):
        currentNode = self.getHead()
        length = self.getLength() + 1
        for index in range(length):
            if(currentNode.getValue() == value):
                return index
            currentNode = currentNode.getNext()
        raise ValueError('That was no valid value')
        
    def add(self, value):
        if(isinstance(value, list) or isinstance(value, str)):
            for item in value:  
                self.insert(item)
        else:
            self.insert(value)
              
    def insert(self, value):
        newNode = Node(value)
        if(self.getHead() is None):
            self.setHead(newNode)
            self.setTail(newNode)
        else:
            previousNode = self.getTail()
            previousNode.setNext(newNode)
            newNode.setPrevious(previousNode)
            self.setTail(newNode)
        self.increaseLength()
            
    def remove(self, value):
        currentNode = self.getHead()
        while (currentNode.getValue() != value and currentNode.getValue() is not None):
            currentNode = currentNode.getNext()
        if(currentNode.getValue() is None):
            return False
        previousNode = currentNode.getPrevious()
        previousNode.setNext(currentNode.getNext())
        self.decreaseLength()
        return True
    
    def removeNode(self, node):
        if(node == self.getHead()):
            nextNode = node.getNext()
            nextNode.setPrevious(None)
            self.setHead(nextNode)
        elif(node == self.getTail()):
            previousNode = node.getPrevious()
            previousNode.setNext(None)
            self.setTail(previousNode)
        else:
            previousNode = node.getPrevious()
            nextNode = node.getNext()
            previousNode.setNext(nextNode)
            nextNode.setPrevious(previousNode)
        self.decreaseLength()        
            
    def show(self):
        currentNode = self.getHead()
        list = ''
        if(currentNode is not None):
            while currentNode.getNext() is not None:
                list += str(currentNode.getValue()) + '\n'
                currentNode = currentNode.getNext()
            list += str(currentNode.getValue())
        return list
    
    def inserir(self, index, value):
        newNode = Node(value)
        if(index == 0):
            nextNode = self.getHead()
            previousNode = self.getTail()
            self.setHead(newNode)
            self.getHead().setNext(nextNode)
            self.setTail(newNode)
            self.getTail().setPrevious(previousNode)
        else:
            previousIndexNode = self.getNodeByIndex(index - 1)
            indexNode = previousIndexNode.getNext()
            previousIndexNode.setNext(newNode)
            indexNode.setPrevious(newNode)
            newNode.setNext(indexNode)
            newNode.setPrevious(previousIndexNode)
        self.increaseLength()
        
    def concatenar(self, list):
        self.add(list)
