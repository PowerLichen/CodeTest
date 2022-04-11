# 1991: 트리 순회
def preorder(tree, root):
    if root == ".":
        return
    print(root, end="")
    preorder(tree, tree[root][0])
    preorder(tree, tree[root][1])


def inorder(tree, root):
    if root == ".":
        return
    inorder(tree, tree[root][0])
    print(root, end="")
    inorder(tree, tree[root][1])


def postorder(tree, root):
    if root == ".":
        return
    postorder(tree, tree[root][0])
    postorder(tree, tree[root][1])
    print(root, end="")


n = int(input())
tree = dict()

for _ in range(n):
    root, lch, rch = input().split()
    tree[root] = [lch, rch]

preorder(tree, "A")
print()
inorder(tree, "A")
print()
postorder(tree, "A")
print()
