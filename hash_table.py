
class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''

    def __init__(self, size):
        if size <= 0:
            raise ValueError("Hash table size must be positive")

        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0

        for character in key:
            total += ord(character)

        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.data[index]

        # Check whether this contact already exists.
        while current is not None:
            if current.key == key:
                current.value.number = value
                return

            current = current.next

        # Add a new node at the front of the chain.
        contact = Contact(key, value)
        new_node = Node(key, contact)
        new_node.next = self.data[index]
        self.data[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                return current.value

            current = current.next

        return None

    def print_table(self):
        for index in range(self.size):
            current = self.data[index]

            if current is None:
                print(f"Index {index}: Empty")
            else:
                contacts = []

                while current is not None:
                    contacts.append(str(current.value))
                    current = current.next

                print(f"Index {index}: " + " - ".join(contacts))


# Test your hash table implementation here.

# Test the Contact and Node classes.
contact_1 = Contact("Riley", "123-456-7890")
print("Contact test:", contact_1)

node_1 = Node(contact_1.name, contact_1)
print("Node key:", node_1.key)
print("Node value:", node_1.value)
print("Node next:", node_1.next)


# Create an empty hash table.
table = HashTable(10)

print("\nEmpty Hash Table:")
table.print_table()


# Insert some contacts.
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")

print("\nAfter Adding Contacts:")
table.print_table()


# Search for an existing contact.
print("\nSearching for John:")
print(table.search("John"))


# Test collisions.
# Amy and May have the same character sum,
# so they will always hash to the same index.
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")

print("\nAfter Adding Amy and May:")
table.print_table()

print("\nSearching for Colliding Contacts:")
print(table.search("Amy"))
print(table.search("May"))


# Test updating a contact with the same name.
table.insert("Rebecca", "999-444-9999")

print("\nAfter Updating Rebecca:")
table.print_table()

print("Updated contact:", table.search("Rebecca"))


# Test searching for a missing contact.
print("\nSearching for Chris:")
print(table.search("Chris"))


# Test inserting and searching in a smaller table.
small_table = HashTable(2)
small_table.insert("Alex", "111-111-1111")
small_table.insert("Sam", "222-222-2222")
small_table.insert("Taylor", "333-333-3333")

print("\nSmall Hash Table:")
small_table.print_table()

print("\nSearching in Small Table:")
print(small_table.search("Taylor"))
