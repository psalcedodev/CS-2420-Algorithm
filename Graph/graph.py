from queue import Queue

class Stack:
  def __init__(self):
    self.mStack = []
  def push(self, value):
    self.mStack.append(value)
  def pop(self):
    return self.mStack.pop()
  def isEmpty(self):
    return len(self.mStack) < 1
  def size(self):
    return len(self.mStack)
  def top(self):
    if self.isEmpty():
      return ""
    return self.mStack[-1]

class Graph:
  def __init__(self, numVertices):
    self.mVertices = [[] for i in range(numVertices)]
    self.mNumVertices = numVertices

  def indexValid(self, v):
    return (0 <= v and v < self.mNumVertices)

  def addEdge(self, v0, v1): # returns False on bad edge
    if not (self.indexValid(v0) and self.indexValid(v1)):
      return False
    if self.isEdge(v0, v1) or v0 == v1:
      return False
    self.mVertices[v0].append(v1)
    return True

  def findPathDepth(self, v0, v1): # Returns None if no path is found
    s = Stack()
    s.push(v0)
    visited = [False] * len(self.mVertices)
    visited[v0] = True
    while not s.isEmpty():
      if s.top() == v1:
        path = [s.pop()]
        while not s.isEmpty():
          path.append(s.pop())
        path.reverse()
        return path
      deadEnd = True
      neighbors = self.mVertices[s.top()]
      for neighbor in neighbors:
        if not visited[neighbor]:
          s.push(neighbor)
          visited[neighbor] = True
          deadEnd = False
          break
      if deadEnd:
        s.pop()
    return None

  def findPathBreadth(self, v0, v1): # Returns None if no path is found
    q = Queue()
    f = [-1] * self.mNumVertices
    q.enqueue(v0)
    f[v0] = v0
    while not q.isEmpty():
      current = q.dequeue()
      if current == v1:
        path = [current]
        index = f[current]
        while not index == v0:
          path.append(index)
          index = f[index]
        path.append(v0)
        path.reverse()
        return path
      for neighbor in self.getNeighbors(current):
        if f[neighbor] == -1:
          q.enqueue(neighbor)
          f[neighbor] = current
    return None

  def getNeighbors(self, v):
    if not self.indexValid(v):
      return None
    return self.mVertices[v]

  def isEdge(self, v0, v1):
    if not (self.indexValid(v0) and self.indexValid(v1)):
      return False
    for i in range(len(self.mVertices[v0])):
      if self.mVertices[i] == v1:
        return True
    return False
