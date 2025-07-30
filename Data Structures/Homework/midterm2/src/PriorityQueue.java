import java.util.Comparator;

public class PriorityQueue<E> {

    Heap<E> heap;

    public PriorityQueue(Comparator<E> comp)
    {
        heap = new Heap<>(comp);
    }

    /*
    This method gets, without removing, the root of the heap and returns its element.
     */
    public E peek()
    {
        if(heap.isEmpty())
            return null;

        return heap.getRoot().getElement();
    }

    /*
    This method gets, and removes, the root of the heap and returns the element.

    The method is task 3.
     */
    public E poll()
    {
        //Task 3: replace return statement below with your code...
        if (heap.isEmpty()) {
            return null;
        }
        E heapRootElement = heap.getRoot().getElement();
        heap.removeRoot();
        return heapRootElement;
    }

    /*
    Adds a new element to the heap.
     */
    public void add(E element)
    {
        heap.addNode(element);
    }


    /*
    Removes all nodes from the heap.
    This method should not throw any errors on an empty heap

    The method is task 4, and should be the last method to implement
     */
    public void clear()
    {
        while (!heap.isEmpty()) {
            heap.removeRoot();
        }
    }

    //size
    public int size() { return heap.size(); }

    public void printQueueTree()
    {
        heap.printTree();
    }

    public static void main(String[] args)
    {
        PriorityQueue<Integer> maxPQ = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1.compareTo(o2);
            }
        });

        maxPQ.add(7);
        maxPQ.add(1);
        maxPQ.add(10);
        maxPQ.add(8);
        maxPQ.add(4);
        maxPQ.add(15);

        System.out.print("Largest, and first, element in the queue (should be 15): ");
        System.out.println(maxPQ.peek());

        System.out.println("Showing poll() method. First return should be 15, second should be 10:");
        System.out.println(maxPQ.poll());
        System.out.println(maxPQ.poll());

        System.out.println("Showing clear() method. Size before should be 4 and size after should be 0:");
        System.out.println(maxPQ.size());
        maxPQ.clear();
        System.out.println(maxPQ.size());

        System.out.println("Clear should not throw any errors if run on an empty queue:");
        maxPQ.clear();
    }
}
