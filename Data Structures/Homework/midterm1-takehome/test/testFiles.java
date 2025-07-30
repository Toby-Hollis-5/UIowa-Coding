import org.junit.Assert;
import org.junit.Test;

public class testFiles {
    @Test
    public void testSearch() {
        try {
            Class.forName("Search");
        } catch (ClassNotFoundException e) {
            Assert.fail("should have a class called Search");
        }
    }
}
