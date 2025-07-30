import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;

public class WordOccurrence {
  // Given any Scanner input, this function returns a HashMap of
  public static HashMap<String,Integer> countWords(Scanner scnr) {
    HashMap<String,Integer> wordCount = new HashMap<String,Integer>();

    String line;
    while ( scnr.hasNextLine() ) {
      line = scnr.nextLine();
      // stripping punctuation, and splitting line into words (do not worry if you do not understand)
      // we are creating one words array for each line
      String[] words = line.replaceAll("[^\\p{L}\\s']"," ")
                           .toLowerCase().split("\\s+");
      //loop over "words" array to update the occurrences in the HashMap(wordCount).
      /** Your Code Here **/
      for (int i = 0; i < words.length; i++) {
        String word = words[i];
        if ( !wordCount.containsKey(word) ) {
          wordCount.put(word, 1);
        } else {
          int occ = wordCount.get(word);
          wordCount.replace(word, occ+1);
        }
      }
    }
    return wordCount;
  }

  public static ArrayList<Pair<String,Integer>> sortWordCounts(HashMap<String,Integer> wordCount) {
    ArrayList<Pair<String,Integer>> wcList = new ArrayList<>();
    // copy (word,occurrence) pairs into ArrayList wcList
    /** Your Code Here **/
    Set<String> wordSet = wordCount.keySet();
    Iterator<String> wordIt = wordSet.iterator();
    for (int i = 0; i < wordCount.size(); i++) {
      String word = wordIt.next();
      //System.out.println(word);
      Integer occ = wordCount.get(word);
      Pair<String, Integer> pair = new Pair(word, occ);
      wcList.add(i, pair);
    }
    // Use the comparator in ComparingPairs to sort wcList
    /** Your Code Here **/
    Collections.sort(wcList, new ComparingPairs());
    return wcList;
  }

  public static void main(String[] args) {
    HashMap<String,Integer> wordCount;
    ArrayList<Pair<String,Integer>> wcList;
    Scanner input;
    if ( args.length > 0 ) {
      try {
        input = new Scanner(new File(args[0]));
      }
      catch(FileNotFoundException e) {
        System.out.println("Cannot find file "+args[0]);
        System.out.println("Exiting program");
        input = new Scanner("");
        System.exit(0);
      }
    } else {
      input = new Scanner("Now is the time for all good men to come to the aid of the party."+
        "How now brown cow? "+"Time flies like an arrow, but fruit flies like a banana."+
        "To be or not to be, that is the question.");
    }
    //use countWords method to create HashTable
    wordCount = countWords(input);
    //use sortWordCounts to sort wordCount
    wcList    = sortWordCounts(wordCount);
    //print the ordered pairs of wclist
    for ( Pair<String,Integer> p : wcList ) {
      System.out.println(p.getKey()+"\t"+p.getValue());
    }

  }
}
