import java.util.ArrayList;
import java.util.Collections;

public class frogInfo {

    public ArrayList<Frog> SortByName(ArrayList<Frog> input) {
        ArrayList<Frog> sorted = new ArrayList<Frog>();
        Collections.sort(sorted, new Names());
        return sorted;
    }

}
