import org.junit.Test;

import java.io.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;
import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;

public class WordOccurrenceTest {

    public void test(Scanner input,String testFile) {
        HashMap<String,Integer> wordCount = WordOccurrence.countWords(input);
        ArrayList<Pair<String,Integer>> wcListTest = new ArrayList<>();


        BufferedReader reader;
        try {
            reader = new BufferedReader(new FileReader(testFile));
            String line = reader.readLine();
            while (line != null) {
                String[] strSplit = line.split("\t",0);
                String word = strSplit[0];
                Integer count = Integer.valueOf(strSplit[1]);
                Pair<String,Integer> p = new Pair(word,count);
                wcListTest.add(p);
//                assertEquals(count,wordCount.get(word));
//                read next line
                line = reader.readLine();
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        assertEquals(wordCount.size(),wcListTest.size());

        ArrayList<Pair<String,Integer>>  wcList   = WordOccurrence.sortWordCounts(wordCount);
        //print the ordered pairs of wclist
        for ( int i = 0;i < wordCount.size();i++ ) {
            Pair<String,Integer> p1 = wcList.get(i);
            Pair<String,Integer> p2 = wcListTest.get(i);
            assertEquals(p1.getKey(),p2.getKey());
            assertEquals(p1.getValue(),p2.getValue());
        }

    }

    @Test
    public void test1_text() {
        Scanner input = new Scanner("Now is the time for all good men to come to the aid of the party."+
                "How now brown cow? "+"Time flies like an arrow, but fruit flies like a banana."+
                "To be or not to be, that is the question.");
        test(input,"./resources/test1.txt");

    }

    @Test
    public void test2_text() throws FileNotFoundException {
        Scanner input = new Scanner(new File("./resources/romeo+juliet.txt"));
        test(input,"./resources/test2.txt");
    }


    @Test
    public void test4_Comparator(){
        ArrayList<Pair<String,Integer>> wcListTest = new ArrayList<>();
        wcListTest.add(new Pair("me", 5));
        wcListTest.add(new Pair("you", 1));
        wcListTest.add(new Pair("both", 2));

        ArrayList<Pair<String,Integer>> wcListSorted = new ArrayList<>();
        wcListSorted.add(new Pair("you", 1));
        wcListSorted.add(new Pair("both", 2));
        wcListSorted.add(new Pair("me", 5));


        Collections.sort(wcListTest, new ComparingPairs());
        for (int i=0; i<3; i++){
            assertEquals(wcListSorted.get(i).getKey(), wcListTest.get(i).getKey());
            assertEquals(wcListSorted.get(i).getValue(), wcListTest.get(i).getValue());
        }
    }

    @Test
    public void test5_Comparator(){
        ArrayList<Pair<String,Integer>> wcListTest = new ArrayList<>();
        wcListTest.add(new Pair("me", 1));
        wcListTest.add(new Pair("you", 1));
        wcListTest.add(new Pair("both", 2));

        ArrayList<Pair<String,Integer>> wcListSorted = new ArrayList<>();
        wcListSorted.add(new Pair("me", 1));
        wcListSorted.add(new Pair("you", 1));
        wcListSorted.add(new Pair("both", 2));


        Collections.sort(wcListTest, new ComparingPairs());
        for (int i=0; i<3; i++){
            assertEquals(wcListSorted.get(i).getKey(), wcListTest.get(i).getKey());
            assertEquals(wcListSorted.get(i).getValue(), wcListTest.get(i).getValue());
        }
    }


    @Test
    public void test7_countWords(){
        Scanner input = new Scanner("now now no No.");
        HashMap<String,Integer> wordCount = WordOccurrence.countWords(input);

        assertEquals(true, wordCount.containsKey("now"));
        assertEquals(true, wordCount.containsKey("no"));
        assertEquals(false, wordCount.containsKey("Ding"));
        assertEquals(false, wordCount.containsKey("Noo"));
    }

}
