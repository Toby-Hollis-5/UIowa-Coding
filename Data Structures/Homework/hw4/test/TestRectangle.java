import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestRectangle {
    Rectangle R;

    public void init()
    {
        R = new Rectangle(6,2);
    }

    @Test
    public void test_default_toString(){
        init();
        String returnvalue = R.toString();
        String actual = "Rectangle width & height: 6.0, 2.0";
        assertEquals(actual, returnvalue);
    }

    @Test
    public void getter_width(){
        init();
        assertEquals(R.getWidth(),6,0);
        R.setWidth(3);
        assertEquals(R.getWidth(),3,0);
    }

}
