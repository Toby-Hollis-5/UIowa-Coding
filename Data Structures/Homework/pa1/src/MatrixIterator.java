import java.util.Iterator;
import java.util.NoSuchElementException;

public class MatrixIterator<E extends Number> implements Iterator<MatrixEntry<E>>
{
    private E[][] matrix; // matrix to iterate over
    private int row, col; // position in matrix
    /*
        Implement a constructor for the
        matrix iterator that takes in a
        generic type 2-D matrix that contains
        only numbers

        initialize the row and column to be the
        number in the matrix
     */

    public MatrixIterator(E[][] matrix) {
        this.matrix = matrix;
        row = 0; col = 0;
    }



    /*
     Write methods needed for the iterator interface
     if a user tries to access the next location in
     a matrix, and it does not exist, raise a No such
     Element Exception

     */

    @Override
    public boolean hasNext() {
        return (row<matrix.length && col< matrix[row].length);
    }

    @Override
    public MatrixEntry<E> next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        } else {
            MatrixEntry<E> temp = new MatrixEntry<>(matrix[row][col], row, col);
            if (col < matrix[col].length - 1) {
                col++;
            } else {
                col = 0;
                row++;
            }
            return temp;
        }
    }

    public static void main(String[] args) {
        int[][] mat = { {3,4,5}, {7,0,-2}, {5,2,8} };
        Integer[][] mat2 = new Integer[mat.length][mat[0].length];
        for ( int i = 0; i < mat.length; i++ )
            for ( int j = 0; j < mat[i].length; j++ )
                mat2[i][j] = mat[i][j];
        Iterator<MatrixEntry<Integer>> iter = new MatrixIterator<>(mat2);
        while ( iter.hasNext() )
            System.out.println(iter.next());
        //System.out.print("Finally: ");
        //System.out.println(iter.next()); // runtime error: iter.hasNext() is already false
    }


}
