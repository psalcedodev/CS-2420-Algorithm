class Node:
    def __init__(self, item):
        self.mItem = item
        self.mLeft = None
        self.mRight = None


class BST:
    def __init__(self):
        self.mRoot = None
        self.mSize = 0

# It should support the methods: Exists, Insert, Traverse, Delete, Retrieve, and Size.
# methodR => Recursive

    # Exist
    def exists(self, item):
        return self.existsR(item, self.mRoot)

    def existsR(self, dummy, current):
        if current is None:
            return False
        if dummy < current.mItem:
            return self.existsR(dummy, current.mLeft)
        elif dummy > current.mItem:
            return self.existsR(dummy, current.mRight)
        elif dummy == current.mItem:
            return True

    # Insert
    def insert(self, item):
        if self.exists(item):
            return False
        self.mRoot = self.insertR(item, self.mRoot)
        return True

    def insertR(self, item, current):
        if current is None:
            n = Node(item)
            current = n
            self.mSize += 1
        elif item < current.mItem:
            current.mLeft = self.insertR(item, current.mLeft)
        else:
            current.mRight = self.insertR(item, current.mRight)
        return current

    # Traverse
    def traverse(self, callback):
        self.traverseR(self.mRoot, callback)

    def traverseR(self, current, callback):
        if current:
            callback(current.mItem)
            self.traverseR(current.mLeft, callback)
            self.traverseR(current.mRight, callback)
        return

    # Delete
    def delete(self, dummy):
        if not self.exists(dummy):
            return False
        self.mRoot = self.deleteR(dummy, self.mRoot)
        return True

    def deleteR(self, dummy, current):
        if dummy < current.mItem:

            current.mLeft = self.deleteR(dummy, current.mLeft)
        elif dummy > current.mItem:
            current.mRight = self.deleteR(dummy, current.mRight)
        else:
            if current.mLeft is None and current.mRight is None:
                current = None
            elif current.mLeft is None:
                current = current.mRight
            elif current.mRight is None:
                current = current.mLeft
            else:
                s = current.mRight
                while not s.mLeft is None:
                    s = s.mLeft
                current.mItem = s.mItem
                current.mRight = self.deleteR(s.mItem, current.mRight)
        return current

    # Retrieve
    def retrieve(self, item):
        return self.retrieveR(item, self.mRoot)

    def retrieveR(self, item, current):
        if current is None:
            return None
        if current.mItem == item:
            return current.mItem
        elif item > current.mItem:
            return self.retrieveR(item, current.mRight)
        elif item < current.mItem:
            return self.retrieveR(item, current.mLeft)

    def getSize(self):
        return self.mSize
