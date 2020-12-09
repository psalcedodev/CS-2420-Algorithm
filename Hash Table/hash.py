class UUC:

    def __init__(self, dataSize):
        self.mTableSize = 2 * dataSize + 1
        while not self.isPrime(self.mTableSize):
            self.mTableSize += 2
        self.mTable = [None] * self.mTableSize
        self.mSize = 0

    def isPrime(self, n):
        if n == 2:
            return True
        if n == 3:
            return True
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def insert(self, item):
        # checking to see if the item already exists before I insert into the tree
        if self.exists(item):
            return False
        key = int(item)
        index = key % len(self.mTable)
        while self.mTable[index]:
            index += 1
            if index >= len(self.mTable):
                index = 0
        self.mTable[index] = item
        self.mSize += 1

    def delete(self, dummy):
        if not self.exists(dummy):
            return False
        index = int(dummy) % self.mTableSize
        while not (self.mTable[index] and self.mTable[index] == dummy):
            index += 1
            if index >= len(self.mTable):
                index = 0
        self.mTable[index] = False
        return True

    def exists(self, item):
        index = int(item) % self.mTableSize
        while self.mTable[index] is not None:
            if self.mTable[index] is False or self.mTable[index] != item:
                index += 1
            else:
                return True
        return False

    def retrieve(self, item):
        index = int(item) % self.mTableSize
        while self.mTable[index] is not None:
            if self.mTable[index] is False or self.mTable[index] != item:
                index += 1
            else:
                return self.mTable[index]
        return False

    def traverse(self, callback):
        for x in self.mTable:
            if x:
                callback(x)

    def trueSize(self):
        count = 0
        for x in self.mTable:
            if x:
                count += 1
        return count

    def getSize(self):
        return self.mSize
