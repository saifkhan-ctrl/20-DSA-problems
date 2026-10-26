def insert_at_bottom(stack, value):
    if not stack:
        stack.append(value)
        return

    top_element = stack.pop()

    insert_at_bottom(stack, value)

    stack.append(top_element)


def reverse_stack(stack):
    if not stack:
        return

    top_element = stack.pop()

    reverse_stack(stack)

    insert_at_bottom(stack, top_element)


stack = list(map(int, input("Enter stack elements (bottom to top): ").split()))

reverse_stack(stack)

print("Reversed stack (bottom to top):", stack)