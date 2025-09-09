from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.

tree1 = Node(1) # Just a single node
tree2 = Node(2, Node(3), Node(4))  #   2
                                   #  / \
                                   # 3   4
tree3 = Node(10, Node(5, Node(2), Node(7)), Node(15, None, Node(20)))
#        10
#       /  \
#      5    15
#     / \     \
#    2   7     20


def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # TODO: Remove pass and write your code here
    if tree is None:
        return 0
    left_height = find_tree_height(tree.left)
    right_height = find_tree_height(tree.right)
    return 1 + max(left_height, right_height)

def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # TODO: Remove pass and write your code here
    if tree is None:
        return True

    # Check left child
    if tree.left:
        if not compare_func(tree.left.value, tree.value):
            return False
        if not is_heap(tree.left, compare_func):
            return False

    # Check right child
    if tree.right:
        if not compare_func(tree.right.value, tree.value):
            return False
        if not is_heap(tree.right, compare_func):
            return False

    return True




if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    # Example usage
    import operator
    # For max heap: child < parent
    print(is_heap(tree3, lambda child, parent: child < parent))  # False
    print(find_tree_height(tree3))  # Should be 3
