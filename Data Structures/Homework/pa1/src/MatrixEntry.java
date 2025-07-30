import java.util.Iterator;

public class MatrixEntry<E extends Number>
{
    private int row, col;
    private E value;
    /*
        Make a constructor with value
        being a Generic Number of type E
     */
    public MatrixEntry(E value, int row, int col) {
        this.value = value;
        this.row = row;
        this.col = col;
}

    /*
    getters and setters
     */

    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }

    public int getCol() {
        return col;
    }

    public void setCol(int col) {
        this.col = col;
    }

    public E getValue() {
        return value;
    }

    public void setValue(E value) {
        this.value = value;
    }

    /*
        toString in the format:
            Entry at (row,col) = value
         */
    public String toString() {
        return "Entry at (" + this.row + "," + this.col + ") = " + this.value;
    }

}