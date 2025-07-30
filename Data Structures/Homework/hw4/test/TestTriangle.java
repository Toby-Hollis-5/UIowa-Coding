import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestTriangle {
    Triangle t;

    public void init()
    {
        t = new Triangle(3,4,5);
    }

    @Test
    public void test_toString(){
        init();
        String returnvalue = t.toString();
        String actual = "Triangle edge lengths: 3.0, 4.0, 5.0";
        assertEquals(actual, returnvalue);
    }

    @Test
    public void GS_A(){
        init();
        assertEquals(t.getA(),3,0);
        t.setA(4);
        assertEquals(t.getA(),4,0);
    }


}
