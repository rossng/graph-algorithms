class DisjointSetItem:
    def __init__(self, item):
        self.item = item
        self.parent = self

    def find(self):
        if self.parent == self:
            return self
        else:
            return self.parent.find()

    def union(self, item):
        # Naive implementation - will create unbalanced trees
        # TODO: fix this!
        self_root = self.find()
        item_root = item.find()
        self_root.parent = item_root
