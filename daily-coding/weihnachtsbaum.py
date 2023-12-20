def create_tree(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        o_chars = 'O' * (2 * i - 1)
        print(spaces + o_chars)

    # Trunk
    trunk_width = 3
    trunk_spaces = ' ' * (height - trunk_width)
    trunk_chars = 'I' * trunk_width
    for _ in range(trunk_width):
        print(trunk_spaces + trunk_chars)

# Set the height of the tree
tree_height = 5

# Create and display the tree
create_tree(tree_height)
