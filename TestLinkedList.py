
#  File: TestLinkedList.py

#  Description: Creating LinkedList helper functions and testing them.

#  Student Name: Crystal Le
 
#  Student UT EID: CL44964 

#  Partner Name: Johnny Tran

#  Partner UT EID: jht825

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 4/3/2022

#  Date Last Modified: 4/4/2022
class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  # create a linked list
  # you may add other attributes
  def __init__ (self):
    self.first = None

  # get number of links 
  def get_num_links (self):
    count = 0
    current = self.first

    while current != None:
        current = current.next
        count +=1

    return count

  # add an item at the beginning of the list
  def insert_first (self, data): 
    newLink = Link (data)
    newLink.next = self.first
    self.first = newLink

  # add an item at the end of a list
  def insert_last (self, data): 
    newLink = Link (data)
    current = self.first

    if (current == None):
      self.first = newLink
      return

    while (current.next != None):
      current = current.next

    current.next = newLink

  # add an item in an ordered list in ascending order
  # assume that the list is already sorted
  def insert_in_order (self, data): 
    newLink = Link(data)
    current = self.first
    if current is None or current.data >= newLink.data:
        newLink.next = self.first
        self.first = newLink
        return
    while current.next is not None and current.next.data <= newLink.data:
        current = current.next
    newLink.next = current.next
    current.next = newLink

  # search in an unordered list, return None if not found
  def find_unordered (self, data):
    newLink = Link (data)
    current = self.first
    while current != None :
        if current.data == newLink.data:
            return current.data
        current = current.next
    return None

  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 
    current = self.first

    # goes through the unordered data and will return the data or none if it is not found.
    while current is not None:
        if current.data is data and current.data <= data:
            return current.data
        current = current.next
    return None

  # Delete and return the first occurrence of a Link containing data
  # from an unordered list or None if not found
  def delete_link (self, data):
    current = self.first
    previous = self.first

    if current is None:
        return None

    # will look in current until current is in data:
    while current.data is not data:
        if current.next is None:
            return None
        else:
            current = current.next
            previous = current

    # just in case the first link has been deleted
    if current is self.first:
        self.first = self.first.next
    else:
        previous.next = current.next
    return current.data
    
  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    current = self.first
    string = ''
    count = 0

    while current is not None:
        # makes a new line after 10 lines
        if count % 10 is 0 and count is not 0:
            string += '  \n' + str(current.data)
        # add data to string if it's first
        elif count is 0:
            string = string + str(current.data)
        # puts 2 spaces between each data
        else:
            string = string + '  ' + str(current.data)
        current = current. next
        count += 1
    return string
  # Copy the contents of a list and return new list
  # do not change the original list
  def copy_list (self):
    copy = LinkedList()
    current = self.first

    # goes through the list and adds from the end of the copy list.
    while current is not None:
        copy.insert_last(current.data)
        current = current.next
    return copy

  # Reverse the contents of a list and return new list
  # do not change the original list
  def reverse_list (self): 
    new_list = LinkedList()
    current = self.first

    # goes through the list and adds to the beginning new_list
    while current is not None:
        new_list.insert_first(current.data)
        current = current.next
    return new_list

  # Sort the contents of a list in ascending order and return new list
  # do not change the original list
  def sort_list (self): 
    new_list = LinkedList()
    current = self.first

    # does the sorting and returns a new list after the sorting in ascending order
    while current is not None:
        new_list.insert_in_order(current.data)
        current = current.next
    return new_list

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    current = self.first

    # checks if list is sorted and returns true if is, false if not (ascending order)
    while current.next is not None:
        if current.next.data <= current.data:
            return False
        else:
            current = current.next
    return True

  # Return True if a list is empty or False otherwise
  def is_empty (self): 
    if self.first is None:
        return True
    else:
        return False
  # Merge two sorted lists and return new list in ascending order
  # do not change the original lists
  def merge_list (self, other): 
    new_list = LinkedList()
    current = self.first

    # sorts the first current until current is none
    while current is not None:
        new_list.insert_in_order(current.data)
        current = current.next

    # adds the second current until current is none
    current = other.first
    while current is not None:
        new_list.insert_in_order(current.data)
        current = current.next
    return new_list

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    self_current = self.first
    other_current = other.first

    # checks if one list is empty or not. return false because they are equal
    if self_current is None and other_current is not None:
        return False
    elif self_current is not None and other_current is None:
        return False

    # looks at both lists and then checks to see if they're equal
    while self_current is not None and other_current is not None:
        if self_current is not other_current:
            return False
        else:
            self_current = self_current.next
            other_current = other_current.next
    return True
  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  # do not change the original list
  def remove_duplicates (self):
    new_list = LinkedList()
    current = self.first

    # if the list is empty then return the empty list
    if self.is_empty():
        return new_list

    # check if list has data or not. if not then add to the new_list
    while current is not None:
        if new_list.find_unordered(current.data) is None:
            new_list.insert_last(current.data)
        current = current.next
    return new_list

def main():
    linked_list = LinkedList()
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    for i in range(1, 50, 3):
        linked_list.insert_last(i)
    print(linked_list)

    # Test method insert_last()
    linked_list.insert_last(3)
    print(linked_list)

    # Test method insert_in_order()
    linked_list.insert_last(3)
    linked_list.insert_last(5)
    linked_list.insert_last(74)
    linked_list.insert_in_order(1)
    print(linked_list)

    # Test method get_num_links()
    print(linked_list.get_num_links())

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    unordered = LinkedList()
    unordered.insert_last(23)
    unordered.insert_last(2)
    unordered.insert_last(91)
    print(unordered.find_unordered(23))
    print(unordered.find_unordered(5))

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    print(linked_list.find_ordered(5))
    print(linked_list.find_ordered(69))

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    linked_list.delete_link(5)
    linked_list.delete_link(78)

    # Test method copy_list()
    copy = linked_list.copy_list()

    # Test method reverse_list()
    reversed_list = copy.reverse_list()

    # Test method sort_list()
    sort_list = linked_list.sort_list()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print(sort_list.is_sorted())
    print(linked_list.is_sorted())

    # Test method is_empty()
    is_empty = LinkedList()
    print(is_empty.is_empty())
    print(linked_list.is_empty())

    # Test method merge_list()
    print(linked_list.merge_list(sort_list))

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print(linked_list.is_equal(copy))
    print(linked_list.is_equal(reversed_list))

    # Test remove_duplicates()
    dup = linked_list.remove_duplicates()
    print(dup)
if __name__ == "__main__":
  main()