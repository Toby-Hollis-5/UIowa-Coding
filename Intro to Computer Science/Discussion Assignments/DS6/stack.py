# Stacks: a very common and very important CS data structure
#
# A stack is a collection of items supporting three operations:
#  - push(item): add item to the stack
#  - pop(): removes the most recently added item and returns it
#  - isEmpty(): returns True if the stack is empty, else False
#
# The class below implements a Stack.  You can test it with testStack().


class Stack:
   # We represent an empty stack using an empty list of items
   def __init__(self):
      self.items = []                                                                                                        
                                                                                                                           
   # Return True if there are no items in the stack.  Return False otherwise.                                             
   def isEmpty(self):
      return(len(self.items) == 0)

   # Add an item to the stack.
   def push (self, item):
      self.items.append(item)

   # If the stack is not empty, remove and return the item most recently
   # added to the stack (people refer to this as the "top" item of the stack.)
   # In our representation that is the item at the end of the items list.
   # It turns out Python has a list method called pop that does what we want:
   #
   def pop(self):
      if not(self.isEmpty()):
         top = self.items.pop()
         return top
      else:
         print("Error: you can't pop anything from an empty stack")

   # Not a basic stack operation but we'll provide for use in the testing function/demo.
   def size(self):
      return len(self.items)

def testStack():
    s = Stack()
    print("Created an empty Stack")
    print("Size is now: {}".format(s.size()))
    print("Pushing: 3, then 'hi', then 99")
    s.push(3)
    s.push("hi")
    s.push(99)
    print("Size is now: {}".format(s.size()))
    print("Popping ...")
    print(s.pop())
    print("Size is now: {}".format(s.size()))
    print("Popping ..." )
    print(s.pop())
    print("Size is now: {}".format(s.size()))
    print("Pushing [1,2]")
    s.push([1,2])
    print("Size is now: {}".format(s.size()))
    print("Is the stack empty?", "yes" if s.isEmpty() else "no")
    print("Popping ...")
    print( s.pop())
    print("Size is now: {}".format(s.size()))
    print("Popping ...")
    print(s.pop())
    print("Size is now: {}".format(s.size()))
    print("Is the stack empty?", "yes" if s.isEmpty() else "no")
    print("Popping ...")
    print(s.pop())


    
