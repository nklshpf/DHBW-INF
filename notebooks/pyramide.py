def create_pyramid(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        o_chars = 'O' * (2 * i - 1)
        print(spaces + o_chars)

# Set the height of the pyramid
pyramid_height = 5

# Create and display the pyramid
create_pyramid(pyramid_height)
