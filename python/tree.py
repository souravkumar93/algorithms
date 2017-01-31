class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


def inOrder(root):
	if root:
		inOrder(root.left)
		print(root.data)
		inOrder(root.right)

def postOrder(root):
	if root:
		postOrder(root.left)
		postOrder(root.right)
		print(root.data)


def preOrder(root):
	if root:
		print(root.data)
		preOrder(root.left)
		preOrder(root.right)

def size(root):
	if not root:
		return 0
	else:
		return size(root.left) + 1 +  size(root.right)

def maximum(root):
	if root == None:
		return 0
	res = root.data
	leftMax = maximum(root.left)
	rightMax = maximum(root.right)
	if leftMax > res:
		res = leftMax
	elif rightMax > res:
		res = rightMax
	return res

def minimum(root):
	if root == None:
		return 0
	res = root.data
	leftmin = minimum(root.left)
	rightmin = minimum(root.right)
	if leftmin < res:
		res = leftmin
	elif rightmin < res:
		res = rightmin
	return res 


def height(root):
	if not root:
		return 0
	else:
		return 1 + max(height(root.left) , height(root.right))

def diameter(root):
	if not root:
		return 0
	else:
		leftHeight = height(root.left)
		rightHeight = height(root.right)
		ldiameter = diameter(root.left)
		rdiameter = diameter(root.right)
		return max(leftHeight + rightHeight + 1 , max(ldiameter,rdiameter))

def levelOrderTraversal(root):
	if root is None:
		return
	traversal = []
	queue = []
	queue.append(root)
	while len(queue) > 0:
		traversal.append(queue[0].data)
		node = queue.pop(0)
		if node.left is not None:
			queue.append(node.left)
		if node.right is not None:
			queue.append(node.right)
	return traversal

def widthOfTree(root):
	


node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)
node.right.right = Node(7)

print(' in order traversal')
inOrder(node)
print(' post order traversal')
postOrder(node)
print(' pre order traversal')
preOrder(node)

print("size of the tree --- " + str(size(node)))
print("maximum node --- " + str(maximum(node)))
print("minimum node --- " + str(minimum(node)))
print("height of the tree --- " + str(height(node)))
print("diameter of the tree --- " + str(diameter(node)))
print(levelOrderTraversal(node))
