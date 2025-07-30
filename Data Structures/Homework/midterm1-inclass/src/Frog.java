public class Frog implements Amphibian {

        private String name;
        private double humidity;
        private String voice;

        public Frog() {
            this.name = "Jeremy";
            this.humidity = .5;
            this.voice = "Ribbit";
        }

        public Frog(String name, String voice, double humidity) {
            this.name = name;
            this.voice = voice;
            this.humidity = humidity;

        }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getHumidity() {
        return humidity;
    }

    public void setHumidity(double humidity) {
        this.humidity = humidity;
    }

    public String getVoice() {
        return voice;
    }

    public void setVoice(String voice) {
        this.voice = voice;
    }

    @Override
        public String toString() {
            return name + " " + humidity;
        }

        @Override
        public String Sound() {
            return name + " " + voice;
        }

        @Override
        public double Environment() {
            return humidity*100;
        }

        public int compare(Frog f1, Frog f2) {
            int comparisonVal = f1.name.compareTo(f2.name);
            if (comparisonVal == 0) {
                comparisonVal = f1.voice.compareTo(f2.voice);
                if (comparisonVal == 0) {
                    return -1;//SOMETHING
                }
            }
            return comparisonVal;
        }





}
