import org.junit.Test;

import java.util.Comparator;

import static org.junit.Assert.*;

public class Mid2Test {

    Comparator<Integer> intComparator = new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            return o1.compareTo(o2);
        }
    };

    //Heap tests
    //======================================================================================

    //Should pass after task 1 is complete
    @Test
    public void isLeafTest()
    {
        Heap<Integer> heap = new Heap<>(intComparator);
        Node<Integer> n1 = new Node(7, null, null, null);
        Node<Integer> n3 = new Node(10, n1, null, null);
        n1.setParent(n3);

        Node<Integer> n4 = new Node(8, null, null, null);
        Node<Integer> n5 = new Node(15, n4, n3, null);
        n3.setParent(n5);
        n4.setParent(n5);

        assertEquals(true, heap.isLeaf(n1));
        assertEquals(false, heap.isLeaf(n3));

        assertEquals(true, heap.isLeaf(n4));
        assertEquals(false, heap.isLeaf(n5));
    }

    //Should pass after tasks 1 and 2 are complete
    @Test
    public void heapifyTest()
    {
        Heap<Integer> heap = new Heap<>(intComparator);
        Node<Integer> n1 = heap.addNode(7);
        Node<Integer> n2 = heap.addNode(1);
        Node<Integer> n3 = heap.addNode(10);
        Node<Integer> n4 = heap.addNode(8);
        Node<Integer> n5 = heap.addNode(4);
        Node<Integer> n6 = heap.addNode(15);

        heap.removeRoot();

        assertEquals(true, heap.isLeaf(n1));
        assertEquals(true, heap.isLeaf(n2));
        assertEquals(true, heap.isLeaf(n5));

        assertEquals(n4, n3.getLeftChild());
        assertEquals(n1, n3.getRightChild());
        assertEquals(n2, n4.getLeftChild());
        assertEquals(n5, n4.getRightChild());

        heap.removeRoot();

        assertEquals(true, heap.isLeaf(n1));
        assertEquals(true, heap.isLeaf(n2));
        assertEquals(false, heap.isLeaf(n5));

        assertEquals(n5, n4.getLeftChild());
        assertEquals(n1, n4.getRightChild());
        assertEquals(n2, n5.getLeftChild());
        assertEquals(null, n5.getRightChild());
    }


    //Should pass after tasks 1, 2, 3, and 4 are complete
    @Test
    public void sizeTest()
    {
        PriorityQueue<Integer> pq = new PriorityQueue<>(intComparator);

        pq.add(7);
        pq.add(1);
        pq.add(10);
        pq.add(8);
        pq.add(4);
        pq.add(15);

        assertEquals(6, pq.size());
        pq.poll();
        assertEquals(5, pq.size());
        pq.peek();
        assertEquals(5, pq.size());
        pq.clear();
        assertEquals(0, pq.size());
    }
    //======================================================================================
}
