import java.util.Comparator;
import java.util.LinkedList;

/**
 * This Heap class is implemented using a binary tree.
 * @param <E> The type of element that will be stored
 */
public class Heap<E> {

    private int size;
    private Node<E> root;
    private Comparator<E> comp;
    LinkedList<Node<E>> nodesWithZeroOrOneChild;

    public Heap(Comparator<E> comp)
    {
        this.comp = comp;
        nodesWithZeroOrOneChild = new LinkedList<>();
        size = 0;
        root = null;
    }

    public Node<E> getRoot() { return root; }
    public int size() { return size; }

    /*
    Swap 1 node in the tree for another
    This also changes the references to the nodes in each parent and set of children
    Lastly, update the nodesWithOneOrZeroChildren LinkedList with the swap
     */
    public void swap(Node<E> n1, Node<E> n2)
    {
        //Check if root needs to be reset
        if(n1 == root)
            root = n2;
        else if(n2 == root)
            root = n1;

        //Check n1 left
        if(n1.getLeftChild() != null && n1.getLeftChild() != n2)
            n1.getLeftChild().setParent(n2);

        //Check n1 right
        if(n1.getRightChild() != null && n1.getRightChild() != n2)
            n1.getRightChild().setParent(n2);

        //Check n1 parent
        if(n1.getParent() != null && n1.getParent() != n2)
        {
            if(n1.getParent().getLeftChild() == n1)
                n1.getParent().setLeftChild(n2);
            else
                n1.getParent().setRightChild(n2);
        }

        //Check n2 left
        if(n2.getLeftChild() != null && n2.getLeftChild() != n1)
            n2.getLeftChild().setParent(n1);

        //Check n2 right
        if(n2.getRightChild() != null && n2.getRightChild() != n1)
            n2.getRightChild().setParent(n1);

        //Check n2 parent
        if(n2.getParent() != null && n2.getParent() != n1)
        {
            if(n2.getParent().getLeftChild() == n2)
                n2.getParent().setLeftChild(n1);
            else
                n2.getParent().setRightChild(n1);
        }

        //Get defaults for swapping n1 and n2
        Node<E> p1 = n1.getParent();
        Node<E> l1 = n1.getLeftChild();
        Node<E> r1 = n1.getRightChild();
        Node<E> p2 = n2.getParent();
        Node<E> l2 = n2.getLeftChild();
        Node<E> r2 = n2.getRightChild();

        //Check if n1 or n2 is a parent of the other node.
        //If so, change the defaults so that we do not create looping reference
        if(n1.getLeftChild() == n2)
        {
            p2 = n2;
            l1 = n1;
        }
        else if(n1.getRightChild() == n2)
        {
            p2 = n2;
            r1 = n1;
        }
        else if(n2.getLeftChild() == n1)
        {
            p1 = n1;
            l2 = n2;
        }
        else if(n2.getRightChild() == n1)
        {
            p1 = n1;
            r2 = n2;
        }

        //Swap n1 and n2
        n1.setParent(p2);
        n1.setLeftChild(l2);
        n1.setRightChild(r2);

        n2.setParent(p1);
        n2.setLeftChild(l1);
        n2.setRightChild(r1);

        //Swap n1 and n2 in the nodesWithZeroOrOneChild LinkedList
        int n1Index = nodesWithZeroOrOneChild.indexOf(n1);
        int n2Index = nodesWithZeroOrOneChild.indexOf(n2);

        if(n1Index != -1 && n2Index != -1)
        {
            nodesWithZeroOrOneChild.remove(n1Index);
            nodesWithZeroOrOneChild.add(n1Index, n2);
            nodesWithZeroOrOneChild.remove(n2Index);
            nodesWithZeroOrOneChild.add(n2Index, n1);
        }
        else if(n1Index != -1)
        {
            nodesWithZeroOrOneChild.remove(n1Index);
            nodesWithZeroOrOneChild.add(n1Index, n2);
        }
        else if(n2Index != -1)
        {
            nodesWithZeroOrOneChild.remove(n2Index);
            nodesWithZeroOrOneChild.add(n2Index, n1);
        }
    }

    /*
    Returns true if the tree is empty
     */
    public boolean isEmpty()
    {
        return size == 0;
    }

    /*
    Returns true if node is a leaf
     */
    public boolean isLeaf(Node<E> node)
    {
        if(node == null)
            throw new IllegalArgumentException("Node given in isLeaf() method is null");

        //<Your Code Here>
        if (node.getLeftChild() == null && node.getRightChild() == null) {
            return true;
        } else {
            return false;
        }
    }

    /*
    Start at startNode and recursively check down the tree to make each nodes satisfy the heap property. You must do this recursively using swap() and heapify(). This is what heapifyDown() in our lecture does.
     */
    private void heapify(Node<E> startNode)
    {
        if(startNode == null || isLeaf(startNode))
            return;

        if(startNode.getRightChild() != null && startNode.getLeftChild() != null)
        {
            //<Your Code Here>
            if (comp.compare(startNode.getLeftChild().getElement(), startNode.getRightChild().getElement()) > 0) {
                swap(startNode, startNode.getLeftChild());
            } else {
                swap(startNode, startNode.getRightChild());
            }

        }
        else if(startNode.getRightChild() != null && comp.compare(startNode.getElement(), startNode.getRightChild().getElement()) < 0)
        {
            //<Your Code Here>
            swap(startNode, startNode.getRightChild());
            heapify(startNode);
        }
        else if(startNode.getLeftChild() != null && comp.compare(startNode.getElement(), startNode.getLeftChild().getElement()) < 0)
        {
            //<Your Code Here>
            swap(startNode, startNode.getLeftChild());
            heapify(startNode);
        }
    }

    /*
    Add a node to the bottom right most of the tree.
    Then, bring the new node up the tree until the tree becomes a valid heap
     */
    public Node<E> addNode(E element)
    {
        Node<E> node = new Node(element, null, null, null);
        nodesWithZeroOrOneChild.add(node);
        if(root == null)
            root = node;
        else
        {
            Node<E> nextNode = nodesWithZeroOrOneChild.get(0);
            if(nextNode.getLeftChild() == null)
            {
                nextNode.setLeftChild(node);
                node.setParent(nextNode);
            }
            else
            {
                if(nextNode.getRightChild() == null)
                {
                    nextNode.setRightChild(node);
                    node.setParent(nextNode);
                    nodesWithZeroOrOneChild.remove(0);
                }
                else
                    throw new IllegalStateException("A node in nodesWithZeroOrOneChild LinkedList has 2 children");
            }
        }

        //Start moving the new node up the tree until the tree becomes valid
        Node<E> parent = node.getParent();
        while (parent != null && comp.compare(parent.getElement(), node.getElement()) < 0) {
            swap(parent, node);
            if(parent == root)
                root = node;

            parent = node.getParent();
        }

        size++;
        return node;
    }

    //remove node
    public E removeRoot()
    {
        if(root == null)                        //Tree is empty
            throw new IllegalStateException("No root to remove in Heap");
        else if(root.getLeftChild() == null)    //Tree only has 1 node (root)
        {
            E element = root.getElement();
            root = null;
            size--;
            return element;
        }
        else if(root.getRightChild() == null)   //Tree only has 2 nodes
        {
            E element = root.getElement();
            swap(root, root.getLeftChild());
            root.setLeftChild(null);
            size--;
            return element;
        }
        else                                    //Tree has 2 or more nodes
        {
            E element = root.getElement();
            Node<E> oldRoot = root;
            swap(oldRoot, nodesWithZeroOrOneChild.getLast());  //Get the bottom right most node in the tree and place it at root
            Node<E> parentOldRoot = oldRoot.getParent();

            //If we are removing a node off of a complete level, add the parent to the LinkedList since it now has 1 child.
            if(parentOldRoot.getRightChild() != null && parentOldRoot.getLeftChild() != null)
                nodesWithZeroOrOneChild.add(0, parentOldRoot);

            //Delete old root
            if(oldRoot.getParent().getRightChild() == oldRoot)
                oldRoot.getParent().setRightChild(null);
            else
                oldRoot.getParent().setLeftChild(null);

            //Remove old root if it was in LinkedList
            nodesWithZeroOrOneChild.remove(oldRoot);
            heapify(root);

            size--;
            return element;
        }
    }

    public void printTree()
    {
        BTreePrinter<E> printer = new BTreePrinter<E>();
        printer.printNode(root);
    }

    public static void main(String[] args)
    {
        Heap<Integer> maxHeap = new Heap<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1.compareTo(o2);
            }
        });

        Node<Integer> n1 = maxHeap.addNode(7);
        Node<Integer> n2 = maxHeap.addNode(1);
        Node<Integer> n3 = maxHeap.addNode(10);
        Node<Integer> n4 = maxHeap.addNode(8);
        Node<Integer> n5 = maxHeap.addNode(4);
        maxHeap.addNode(15);

        maxHeap.removeRoot();

        //The following line will print the tree to the console.
        maxHeap.printTree();
        /*
            If your heapify() method is working, the tree in the console should look like:
                   10
                  / \
                 /   \
                 8   7
                / \
                1 4
         */
        System.out.println("The following outputs are whether nodes are leaves or not (testing isLeaf() method):");
        System.out.println("n1 (true): " + maxHeap.isLeaf(n1));
        System.out.println("n2 (true): " + maxHeap.isLeaf(n2));
        System.out.println("n3 (false): " + maxHeap.isLeaf(n3));
        System.out.println("n4 (false): " + maxHeap.isLeaf(n4));
        System.out.println("n5 (true): " + maxHeap.isLeaf(n5));
    }
}
