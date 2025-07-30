import java.util.Comparator;

public class Names implements Comparator<Frog> {

    public int compare(Frog f1, Frog f2) {
        int comparisonVal = f1.getName().compareTo(f2.getName());
        return comparisonVal;
    }

}
