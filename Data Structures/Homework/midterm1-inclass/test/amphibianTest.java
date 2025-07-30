import static org.junit.Assert.*;

import org.junit.Test;
import org.junit.runner.RunWith;

import static junit.framework.TestCase.assertTrue;

class testFrog implements Amphibian
{
    String sound;
    public testFrog(){
        sound = "";
    }

    @Override
    public String Sound() {
        return "";
    }

    @Override
    public double Environment() {
        return 0.0;
    }
}


public class amphibianTest {
     testFrog a;

    public void init()
    {
        this.a = new testFrog();
    }

    @Test
    public void testSoundEnv()
    {
        init();
        assertEquals("",a.Sound());
        init();
        assertEquals(0.0,a.Environment(),0);
    }
}
