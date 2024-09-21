class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, data=[]):
        self.root = None
        for item in data:
            self.insert(item)

    def insert(self, item):
        if not self.root:
            self.root = Node(item)
        else:
            self._insert(self.root, item)

    def _insert(self, node, item):
        if item < node.data:
            if not node.left:
                node.left = Node(item)
            else:
                self._insert(node.left, item)
        elif item > node.data:
            if not node.right:
                node.right = Node(item)
            else:
                self._insert(node.right, item)

    def preorder(self):
        if self.root:
            yield from self._preorder(self.root)

    def _preorder(self, node):
        if node:
            yield node.data
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    def inorder(self):
        if self.root:
            yield from self._inorder(self.root)

    def _inorder(self, node):
        if node:
            yield from self._inorder(node.left)
            yield node.data
            yield from self._inorder(node.right)

    def postorder(self):
        if self.root:
            yield from self._postorder(self.root)

    def _postorder(self, node):
        if node:
            yield from self._postorder(node.left)
            yield from self._postorder(node.right)
            yield node.data

    def delete(self, item):
        self.root = self._delete(self.root, item)

    # Watch this: https://www.youtube.com/watch?v=LFzAoJJt92M
    def _delete(self, node, item):
        if not node:
            # no child node case
            return node
        # finding the node
        if item > node.data:
            node.right = self._delete(node.right, item)
        elif item < node.data:
            node.left = self._delete(node.left, item)
        else:
            # we've found the node, now delete it
            # 1 child node case
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # 2 child nodes case
            current = node.right
            while current.left:
                current = current.left
            node.data = current.data
            node.right = self._delete(node.right, node.data)
        return node


def test_():
    bst = BinarySearchTree([3, 4, 10, 9, 23, 0, 1, 2])
    assert list(bst.inorder()) == [0, 1, 2, 3, 4, 9, 10, 23]
    bst.delete(23)
    assert list(bst.inorder()) == [0, 1, 2, 3, 4, 9, 10]
