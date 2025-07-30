import java.lang.System;

/*
You can update the method parameters, but do not change the method name
*/
public class Search {
    /*
    Implement a generic linear search with the following requirements:
    1. Method name: linearSearch
    2. Methods parameters:
            i. Generic 1-D array called array
        ii. Generic search item called item
    3. return -1 if not found
    */
    public static int linearSearch(int[] array, int item) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == item) {
                return i;
            }
        }
        return -1;
    }



    /*
        Implement a Generic Comparable binary search function with the following requirements:
        1. Initial search function called binarySearch that taken in parameters (see below)
        and starts the binary search
            i. Generic Comparable array called array (assume sorted)
           ii. Generic Comparable item called item
        2. A comparable generic recursive binary search method called binarySearch
        as discussed in class

     */
    /*public static int binarySearch(int[] array, int item) {
        return -1;
    }*/


    public static int binarySearch(int[] array, int item, int lo, int hi) {

        int mid = lo + ((hi-lo) / 2);

        if (hi < lo) {
            return -1;
        }

        if (item == array[mid]) {
            return mid;
        }
        if (item < array[mid]) {
            return binarySearch(array, item, lo, mid-1);
        } else {
            return binarySearch(array, item, mid + 1, hi);
        }
    }

    /*
        For each element in nlist, populate an array of that size in
        with the array starting at 0 and ending at n-1

        Calculate the time it takes for a linear search to find the value n-1
        in the populated array

        Calculate the time it takes for the binary search to find the value
        n-1 in the populated array

        upload the output to output.txt and push your code


        DO NOT FORGET TO PUSH YOUR CODE AND CHECK THAT IT WAS CORRECTLY PUSHED
     */
    public static void main(String[] args) {
        int[] nlist = { 10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000,
                300000, 1000000, 3000000 };
        // Holds the timing for linear search
        double[] timingsLS = new double[nlist.length];

        // Holds the timing for Binary Search
        double[] timingsBS = new double[nlist.length];

        int num_trials = 100;
        long start;
        long stop;

        for (int i = 0; i < nlist.length; i++) {
            int n = nlist[i];
            int[] linearArray = new int[nlist[i]];
            for (int k = 0; k < n-1; k++) {
                linearArray[k] = k;
            }
            start = System.nanoTime();
            linearSearch(linearArray, n-1);
            stop = System.nanoTime();
            timingsLS[i] = stop-start;
        }

        for (int i = 0; i < nlist.length; i++) {
            int n = nlist[i];
            int[] binaryArray = new int[nlist[i]];
            for (int k = 0; k < n-1; k++) {
                binaryArray[k] = k;
            }
            start = System.nanoTime();
            binarySearch(binaryArray, n-2, 0, n-1);
            stop = System.nanoTime();
            timingsBS[i] = stop-start;
        }

        System.out.println("Timings for linear search");
        for ( double time : timingsLS )
            System.out.print("  "+String.format("%.9f",time)+",");
        System.out.println();
        System.out.println();
        System.out.println("Timings for binary search");
        for ( double time : timingsBS )
            System.out.print("  "+String.format("%.9f",time)+",");
    }
}
