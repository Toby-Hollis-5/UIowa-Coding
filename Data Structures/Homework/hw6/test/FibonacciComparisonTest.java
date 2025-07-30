
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class FibonacciComparisonTest {
    FibonacciComparison tester;
    public void init(){
        tester = new FibonacciComparison();
    }

    @Test
    public void testFibLinear()
    {
        init();
        assertEquals(0 , tester.fibLinear(0));
        assertEquals(5 , tester.fibLinear(5));
    }
    @Test
    public void testFibRecursive()
    {
        init();
        assertEquals(0, tester.fib(0));
        assertEquals(5 , tester.fib(5));
    }
}

