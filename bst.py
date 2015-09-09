__author__ = 'Henry'


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return repr({self.key: self.value, 'left': self.left is not None, 'right': self.right is not None})


class BST(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def _put(self, key, value, node):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, value)
                self.size += 1
            else:
                self._put(key, value, node.left)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, value)
                self.size += 1
            else:
                self._put(key, value, node.right)
        else:  # key exists, update value
            node.value = value

    def put(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            self.size += 1
        else:
            self._put(key, value, self.root)

    def __setitem__(self, key, value):
        self.put(key, value)

    def _get(self, key, node):
        if key < node.key:
            if node.left is None:
                return None
            else:
                return self._get(key, node.left)
        elif key > node.key:
            if node.right is None:
                return None
            else:
                return self._get(key, node.right)
        else:  # match
            return node.value

    def get(self, key):
        return self._get(key, self.root)

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.get(key) is not None

    @property
    def to_dict(self):
        if self.root is None:
            return {}
        else:
            return self._to_dict(self.root)

    def _to_dict(self, node):
        node_dict = {node.key: node.value}
        if node.left is not None:
            node_dict.update(left=self._to_dict(node.left))
        if node.right is not None:
            node_dict.update(right=self._to_dict(node.right))
        return node_dict
