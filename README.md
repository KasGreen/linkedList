# Linked List

A Python implementation of a singly linked list data structure with common operations for insertion, deletion, traversal, and cycle detection.

## Features

- **Singly Linked List**: Classic linked list with forward-only traversal
- **Flexible Insertion**: Add nodes at head, tail, or any index
- **Flexible Deletion**: Remove nodes from head, tail, or any index
- **Index-based Access**: Retrieve values by position
- **Cycle Detection**: Floyd's tortoise and hare algorithm implementation

## Installation

```bash
git clone https://github.com/KasGreen/linkedList.git
cd linkedList
```

## Usage

```python
from linkedList import LinkedList

# Create a new linked list
linked_list = LinkedList()

# Add elements
linked_list.addAtHead(5)      # List: 5
linked_list.addAtTail(10)     # List: 5 -> 10
linked_list.addAtIndex(1, 7)  # List: 5 -> 7 -> 10

# Access elements
value = linked_list.getNodeValue(1)  # Returns 7
length = linked_list.getLength()     # Returns 3

# Delete elements
linked_list.deleteAtHead()     # List: 7 -> 10
linked_list.deleteAtTail()     # List: 7
linked_list.deleteAtIndex(0)   # List: empty

# Print all values
linked_list.printValues()
```

## Class Structure

### Node

```python
Node(integer)
```

A single node in the linked list.

| Attribute | Type | Description |
|-----------|------|-------------|
| `integer` | int | The value stored in the node |
| `nextNode` | Node | Reference to the next node |

**Methods:**

| Method | Description |
|--------|-------------|
| `setNextNode(nextNode)` | Set the reference to the next node |

### LinkedList

```python
LinkedList()
```

The main linked list container.

| Attribute | Type | Description |
|-----------|------|-------------|
| `firstNode` | Node | Reference to the head of the list |

## API Reference

### Insertion Methods

| Method | Parameters | Description |
|--------|------------|-------------|
| `addAtHead(value)` | `value`: int | Insert a new node at the beginning of the list |
| `addAtTail(value)` | `value`: int | Insert a new node at the end of the list |
| `addAtIndex(index, value)` | `index`: int, `value`: int | Insert a new node at the specified index |

### Deletion Methods

| Method | Parameters | Description |
|--------|------------|-------------|
| `deleteAtHead()` | None | Remove the first node |
| `deleteAtTail()` | None | Remove the last node |
| `deleteAtIndex(index)` | `index`: int | Remove the node at the specified index |

### Access Methods

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `getNodeValue(index)` | `index`: int | int | Returns the value at the given index, or -1 if invalid |
| `getLength()` | None | int | Returns the total number of nodes |
| `isEmptyList()` | None | bool | Returns `True` if the list is empty |
| `printValues()` | None | None | Prints all values in the list |

### Utility Functions

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `hasCycle(firstNode)` | `firstNode`: Node | bool | Detects if the linked list contains a cycle using Floyd's algorithm |

## Time Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| `addAtHead()` | O(1) |
| `addAtTail()` | O(n) |
| `addAtIndex()` | O(n) |
| `deleteAtHead()` | O(1) |
| `deleteAtTail()` | O(n) |
| `deleteAtIndex()` | O(n) |
| `getNodeValue()` | O(n) |
| `getLength()` | O(n) |
| `hasCycle()` | O(n) |

## Space Complexity

- **LinkedList**: O(n) where n is the number of nodes
- **hasCycle()**: O(1) - uses Floyd's cycle detection (two pointers)

## Example

```python
from linkedList import LinkedList

# Create and populate a linked list
linked_list = LinkedList()
linked_list.addAtHead(9)       # List: 9
linked_list.addAtHead(5)       # List: 5 -> 9
linked_list.addAtIndex(0, 1)   # List: 1 -> 5 -> 9
linked_list.addAtTail(8)       # List: 1 -> 5 -> 9 -> 8
linked_list.addAtTail(2)       # List: 1 -> 5 -> 9 -> 8 -> 2
linked_list.addAtIndex(2, 6)   # List: 1 -> 5 -> 6 -> 9 -> 8 -> 2

# Modify the list
linked_list.deleteAtTail()     # List: 1 -> 5 -> 6 -> 9 -> 8
linked_list.deleteAtIndex(2)   # List: 1 -> 5 -> 9 -> 8

# Display results
linked_list.printValues()
# Output:
# 1
# 5
# 9
# 8
```

## Cycle Detection

The `hasCycle()` function implements Floyd's cycle detection algorithm (also known as the tortoise and hare algorithm):

```python
from linkedList import Node, hasCycle

# Create nodes manually
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Link them: 1 -> 2 -> 3 -> (back to 2, creating a cycle)
node1.setNextNode(node2)
node2.setNextNode(node3)
node3.setNextNode(node2)  # Creates cycle

# Detect cycle
result = hasCycle(node1)  # Returns True
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Author

KasGreen

---

*Note: This is an educational project demonstrating linked list data structure implementation in Python, including common operations and the classic Floyd's cycle detection algorithm.*
