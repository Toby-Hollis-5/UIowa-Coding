import org.junit.Test;
import java.util.Comparator;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import java.util.Arrays;
import java.util.Iterator;


public class MatrixTest {

    @Test
    public void printTest()
    {
        int[][] mat = { {1,2,3}, {4,5,6}, {7,8,9} };
        Integer[][] mat2 = new Integer[mat.length][mat[0].length];
        for ( int i = 0; i < mat.length; i++ )
            for ( int j = 0; j < mat[i].length; j++ )
                mat2[i][j] = mat[i][j];
        Iterator<MatrixEntry<Integer>> iter = new MatrixIterator<>(mat2);
        String sol = "Entry at (0,0) = 1\n" +
                "Entry at (0,1) = 2\n" +
                "Entry at (0,2) = 3\n" +
                "Entry at (1,0) = 4\n" +
                "Entry at (1,1) = 5\n" +
                "Entry at (1,2) = 6\n" +
                "Entry at (2,0) = 7\n" +
                "Entry at (2,1) = 8\n" +
                "Entry at (2,2) = 9\n";
        String given = "";
        while ( iter.hasNext() )
            given = given + iter.next() + "\n";
        assertEquals(sol, given);

    }
}
