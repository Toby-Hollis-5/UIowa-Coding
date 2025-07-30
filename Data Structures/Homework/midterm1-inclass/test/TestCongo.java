import org.junit.Test;

import java.util.NoSuchElementException;

import static org.junit.Assert.assertEquals;


public class TestCongo {


    @Test()
    public void LI_toString(){
        Frog[] F = new Frog[4];

        F[0] = new Frog("John", "Ribbit", .5);
        F[1] = new Frog("Ashley", "Ribbit", .3);
        F[2] = new Frog("Xio", "Ribbit", .9);
        F[3] = new Frog("tayshawna", "Ribbit", .71);

        frogCongoLine LI = new frogCongoLine(F);

        String given = "";
        while(LI.hasNext())
        {
            given = given + LI.next() + " ";
        }

        assertEquals("Xio 0.9 tayshawna 0.71 ", given);

    }


}
