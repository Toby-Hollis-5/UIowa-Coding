import org.junit.Test;
import static org.junit.Assert.*;
public class TestAVLTreePos {
    @Test
    public void test_getBalance() {
        AVLTreeNode<Integer> node = new AVLTreeNode(1, null, null, null);
        assertEquals(node.getBalance(), 0, 0);
    }
}
