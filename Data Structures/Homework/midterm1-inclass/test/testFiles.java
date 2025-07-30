import org.junit.Assert;
import org.junit.Test;

public class testFiles {

    @Test
    public void testFrog(){
        try {
            Class.forName("Frog");
            Frog defaultFrog = new Frog();
            Frog conFrog = new Frog("Name", "Sound", .7);
        } catch (ClassNotFoundException e) {
            Assert.fail("should have a class called Frog");
        }
    }

    @Test
    public void testFrogCongoLine(){
        try {
            Class.forName("frogCongoLine");
        } catch (ClassNotFoundException e) {
            Assert.fail("should have a class called frogCongoLine");
        }
    }

    @Test
    public void testFrogInfo(){
        try {
            Class.forName("frogInfo");
        } catch (ClassNotFoundException e) {
            Assert.fail("should have a class called frogInfo");
        }
    }

    @Test
    public void testmoistTest(){
        try {
            Class.forName("Moistest");
        } catch (ClassNotFoundException e) {
            Assert.fail("should have a class called Moistest");
        }
    }

    @Test
    public void testnames(){
        try {
            Class.forName("Names");
        } catch (ClassNotFoundException e) {
            Assert.fail("should have a class called Names");
        }
    }
}
