import java.util.Iterator;
import java.util.NoSuchElementException;

public class frogCongoLine implements Iterator<Frog> {

    Frog[] list;
    int index = 0;
    int numberOfFrogs = 0;
    Frog[] newList;

    public frogCongoLine(Frog[] input) {
        list = input;
        int newFrogsInArray = 0;

        for (int i = 0; i<list.length; i++) {
            if(list[i].getName().length() % 2 != 0) {
                if(list[i].getHumidity() > .7) {
                    numberOfFrogs++;
                }
            }
        }
        newList = new Frog[numberOfFrogs];

        for (int j = 0; j<list.length; j++) {
            if(list[j].getName().length() % 2 != 0) {
                if(list[j].getHumidity() > .7) {
                    newList[newFrogsInArray] = list[j];
                    newFrogsInArray++;
                }
            }
        }
    }

    @Override
    public boolean hasNext() {return (index<newList.length); }

    @Override
    public Frog next() {

        if (!hasNext()) {
            throw new NoSuchElementException();
        } else {
            Frog temp;
            temp = newList[index];
            index++;

            return temp;
        }
    }

}
