public class CircularLinkedList <E> {
    // Instance variables. You cannot add or remove these starting variables
    private Node<E> tail;
    private int size;

    // Default Constructor sets the tail-->null and size-->0
    public CircularLinkedList() {
        tail = null;
        size = 0;
    }

    /** Access Methods */
    // returns current size
    public int getSize() {
        return size;
    }

    // return true if the list is empty
    public boolean isEmpty() {
        if (size == 0) {
            return true;
        } else {
            return false;
        }
    }

    // Returns the value of first element (head) of the list
    public E getFirst() {
        if (tail == null) {
            return null;
        }
        return tail.getNext().getElement();
    }
    // Returns the value of last element (tail) of the list
    public E getLast() {
        if (tail == null) {
            return null;
        }
        return tail.getElement();
    }
    /** Update methods */
    // Left Rotate the elements in the list. (Hint: Tail becomes tail.getNext())
    // list                 --> [1,2,3,4,5]
    // list_after_rotate_1  --> [2,3,4,5,1]
    // list_after_rotate_2  --> [3,4,5,1,2]
    public void rotate(){
        tail = tail.getNext();
    }
    // Add an element at the start of the list. (Hint: The first element of a circular linked list is tail.getNext())
    public void addFirst(E e) {
        Node<E> firstNode = new Node<>(e, null);
        if (tail == null) {
            firstNode.setNext(firstNode);
            tail = firstNode;
        } else {
            firstNode.setNext(tail.getNext());
            tail.setNext(firstNode);
        }
        size++;
    }
    // Adding the element at the tail. Question: Can you implement this function using addFirst and rotate?
    // list = [1,2,3,4,5]
    // list.addLast(6) => [1,2,3,4,5,6]
    public void addLast(E e) {
        Node<E> lastNode = new Node<>(e, null);
        if (tail == null) {
            lastNode.setNext(lastNode);
            tail = lastNode;
        } else {
            lastNode.setNext(tail.getNext());
            tail.setNext(lastNode);
            tail = lastNode;
        }
        size++;
    }
    // Remove the first element of the list and return the removed element.
    public E removeFirst() {
        if (tail == null) {
            return null;
        }
        E value = tail.getNext().getElement();
        tail.setNext(tail.getNext().getNext());
        size--;
        return value;
    }

    // Prints out the list elements.
    // IF these are the elements of the linked list, then they will be matched with the corresponding output
    // 1)--> "prius", "rav4", "subaru", "crv", "pilot"
    // 2)--> 1,2,3,4,5
    // 3)--> []
    // Outputs
    // 1)-->[prius, rav4, subaru, crv, pilot, prius, rav4, subaru, crv, pilot]
    // 2)-->[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    // 3)-->[empty list]
    public String toString(){
        if (isEmpty()) {
            return "[empty list]";
        } else {
            String string = "[";
            for (int i = 0; i < size*2-1; i++) {
                string += getFirst() + ", ";
                //System.out.print(tail.getNext().getElement());
                this.rotate();
            }
            string += tail.getNext().getElement() + "]";
            return string;
        }

    }


    public static void main(String args[]){
        String[] cars = { "prius", "rav4", "subaru", "crv", "pilot"};

        CircularLinkedList<String> carsList = new CircularLinkedList<String>();
        for (String i: cars)
            carsList.addLast(i);

        System.out.println("linkedList:"+ carsList.toString());
        // Output for this should be --> linkedList:[prius, rav4, subaru, crv, pilot, prius, rav4, subaru, crv, pilot]
    }
}
