import java.util.Comparator;

// Implement the compare method. This method takes in two Pairs and compares them on the basis of their "value" (count).
public class ComparingPairs implements Comparator<Pair<String,Integer>> {

    public int compare(Pair p1, Pair p2) {
        int result = 0;
        int p1Value = (int) p1.getValue();
        int p2Value = (int) p2.getValue();
        if (p1Value > p2Value) {
            result = 1;
        }
        if (p1Value == p2Value) {
            result = 0;
        }
        if (p1Value < p2Value) {
            result = -1;
        }
        return result;
    }

}

