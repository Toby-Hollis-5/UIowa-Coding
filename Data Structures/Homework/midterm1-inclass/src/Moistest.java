import java.util.Comparator;

public class Moistest implements Comparator<Frog> {

    public int compare(Frog f1, Frog f2) {
        int compareVal = 0;
        if (f1.Environment() > f2.Environment()) {
            compareVal = 1;
        }
        if (f1.Environment() == f2.Environment()) {
            compareVal = 0;
        }
        if (f1.Environment() < f2.Environment()) {
            compareVal = -1;
        }
        return compareVal;
    }

}
