import java.util.Comparator;

public class StudentsByName implements Comparator<Student> {
    public int compare(Student s1, Student s2) {
        // sort names alphabetically, and it can be used to sort an array of Students by name

        // below are two ways to achieve, but there can be other ways,
        // we do not limit your implementation, you can do any way you want
        //
        // (1) concatenating last and first name, and then sort them alphabetically
        // (2) sort by the last name alphabetically, and if there is a tie,
        //     then continue sorting by the first name
        int comparisonVal = s1.getLastName().compareTo(s2.getLastName());
        if (comparisonVal == 0) {
            comparisonVal = s1.getFirstName().compareTo(s2.getFirstName());
        }
        return comparisonVal;

        

    }
}
