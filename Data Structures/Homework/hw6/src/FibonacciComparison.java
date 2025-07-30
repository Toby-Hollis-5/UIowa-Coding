import java.lang.System;

public class FibonacciComparison {

    // Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8 ....
    /*
        input cases
            1) 0
            2) 3
            3) -1
            4) 9
        output cases
            1) 0
            2) 2
            3) 0
            4) 34
     */
    // Note that you need to return 0 if the input is negative.
    // Please pay close attention to the fact that the first index in our fib sequence is 0.

    // Recursive Fibonacci
    public static int fib(int n) {
        int result = 0;
        if (n <= 0) {
            return result;
        }
        if (n == 1 || n == 2) {
            result = 1;
        } else {
            result = fib(n-1) + fib(n-2);
        }
        return result;
    }

    // Iterative Fibonacci
    public static int fibLinear(int n) {
        int result = 0;
        int add = 1;
        for (int i=0; i<n; i++) {
            int temp = result;
            result = result + add;
            add = temp;
        }
        return result;
    }


    public static void main(String[] args) {
        // list of fibonacci sequence numbers
        int[] nlist = { 5,10, 15, 20, 25, 30, 35, 40, 45};

        // Two arrays (one for fibLinear, other for fibRecursive) to store time for each run.
        // There are a total of nlist.length inputs that we will test
        double[] timingsEF = new double[nlist.length];
        double[] timingsLF = new double[nlist.length];

        // Every number in n_list will be given as input 5 times to both fibonacci functions
        // and an average will be taken to make the results more accurate.
        int numTrials = 5;

        //Iterating over number list
        for ( int i = 0; i < nlist.length; i++ ) {
            int n = nlist[i];

            // ---------------- FibRecursive ---------------------------
            // Start recording time
            long start = System.nanoTime();
            // Run fibRecursive function 5 times
            for ( int k = 0; k < numTrials; k++ )
                fib(n);
            // Stop recording time
            long stop = System.nanoTime();
            // Taking average of the run time and store it in the array
            timingsEF[i] = 1e-9*(stop-start) / numTrials;

            // ---------------- FibLinear ---------------------------
            // Start recording time
            start = System.nanoTime();
            // Run FibLinear 5 times
            for ( int k = 0; k < numTrials; k++ )
                fibLinear(n);
            // Stop recording time
            stop = System.nanoTime();
            //Taking average and store it in the array
            timingsLF[i] = 1e-9*(stop-start) / numTrials;
        }

        // Print out the runtimes for different fib functions.
        System.out.println("Timings for Exponential Fibonacci");
        for ( double time : timingsEF )
            System.out.print("  "+time);
        System.out.println();
        System.out.println();
        System.out.println();
        System.out.println("Timings for Linear Fibonacci");
        for ( double time : timingsLF )
            System.out.print("  "+time);
        System.out.println();
    }
}
