import java.util.Comparator;

public class StudentsByID implements Comparator<Student> {
    public int compare(Student s1, Student s2) {
        // sort ID by ascending order, and can be used to sort an array of Student by ID
        int compareVal = 0;
        if (s1.getID() > s2.getID()) {
            compareVal = 1;
        }
        if (s1.getID() == s2.getID()) {
            compareVal = 0;
        }
        if (s1.getID() < s2.getID()) {
            compareVal = -1;
        }
        return compareVal;
    }
}
