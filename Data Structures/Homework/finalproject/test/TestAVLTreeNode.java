import org.junit.Test;
import static org.junit.Assert.*;
public class TestAVLTreeNode {
    @Test
    public void test_height() {
        AVLTreeNode<Integer> node = new AVLTreeNode(1, null, null, null);
        assertEquals(node.height(), 0, 0);
    }

    @Test
    public void test_setHeight() {
        AVLTreeNode<Integer> node = new AVLTreeNode(1, null, null, null);
        AVLTreeNode<Integer> right = new AVLTreeNode(0, node, null, null);
        node.setRight(right);
        node.setHeight(1);
        assertEquals(node.height(), 1, 0);
    }
}
