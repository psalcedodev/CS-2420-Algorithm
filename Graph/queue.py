class Queue:
  def __init__(self):
    self.mQueue = []
  def enqueue(self, item):
    self.mQueue.append(item)
  def dequeue(self):
    return self.mQueue.pop(0)
  def isEmpty(self):
    return len(self.mQueue) <= 0