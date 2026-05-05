class Node:
	def __init__(self, interger):
		self.interger = interger

	def setNextNode(self, nextNode):
		self.nextNode = nextNode


class LinkedList:
	def __init__(self):
		self.firstNode = None

	def getNodeValue(self, index):
		if index < 0:
			return -1
		if self.firstNode == None:
			return -1
		node = self.firstNode
		for i in range(0, index):
			node = node.nextNode
			if node == None:
				return -1
		return(node.interger)

	def getLength(self):
		length = 0
		node = self.firstNode
		while node != None:
			length += 1
			node = node.nextNode
		return length

	def _createFirstNodeIfEmpty(self, value):
		if self.firstNode == None:
			self.firstNode = Node(value)
			self.firstNode.setNextNode(None)
			return True

	def addAtHead(self, value):
		if self._createFirstNodeIfEmpty(value) == True:
			return
		node = self.firstNode
		self.firstNode = Node(value)
		self.firstNode.setNextNode(node)

	def addAtTail(self, value):
		if self._createFirstNodeIfEmpty(value) == True:
			return
		node = self.firstNode
		while node.nextNode != None:
			node = node.nextNode
		newNode = Node(value)
		newNode.setNextNode(None)
		node.setNextNode(newNode)

	def addAtIndex(self, index, value):
		if index < 0:
			return
		if self._createFirstNodeIfEmpty(value) == True:
			return
		node = self.firstNode
		newNode = Node(value)
		if index == 0:
			self.firstNode = newNode
			newNode.setNextNode(node)
			return
		for i in range(0, index - 1):
			if node.nextNode != None:
				node = node.nextNode
			else:
				break
		newNode.setNextNode(node.nextNode)
		node.setNextNode(newNode)

	def deleteAtHead(self):
		if self.isEmptyList() == True:
			return
		self.firstNode = self.firstNode.nextNode

	def deleteAtTail(self):
		if self.isEmptyList() == True:
			return
		if self.firstNode.nextNode == None:
			self.firstNode = None
			return
		node = self.firstNode
		previousNode = None
		while node.nextNode != None:
			previousNode = node
			node = node.nextNode
		previousNode.setNextNode(None)

	def deleteAtIndex(self, index):
		if index < 0:
			return
		if self.isEmptyList() == True:
			return
		if index == 0:
			self.deleteAtHead()
			return
		if self.firstNode.nextNode == None:
			self.firstNode = None
			return 
		node = self.firstNode
		previousNode = None
		for i in range(0, index):
			if node.nextNode != None:
				previousNode = node
				node = node.nextNode
			else:
				break
		previousNode.setNextNode(node.nextNode)
		
	def isEmptyList(self):
		if self.firstNode == None:
			return True

	def printValues(self):
		node = self.firstNode
		if node == None:
			return
		while node.nextNode != None:
			print(node.interger)
			node = node.nextNode
		print(node.interger)

def hasCycle(firstNode):
		node = firstNode
		node2 = firstNode
		while node.nextNode != None:
			node = node.nextNode
			node2 = node2.nextNode.nextNode
			if node is node2:
				return True
			if node2 == None:
				break
		return False		
	
linkedList = LinkedList()


linkedList.addAtHead(9)
linkedList.addAtHead(5)
linkedList.addAtIndex(0,1)
linkedList.addAtTail(8)
linkedList.addAtTail(2)
linkedList.addAtIndex(2,6)
linkedList.addAtIndex(10,3)
linkedList.deleteAtTail()
linkedList.deleteAtIndex(2)
linkedList.printValues()

