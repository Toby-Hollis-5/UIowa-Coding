public class main {
    public static void main(String[] args) {
        Polygon[] shapes = new Polygon[3];
        shapes[0] = new Triangle(3.0,4.0,5.0);
        shapes[1] = new Triangle(17.0,12.0,9.0);
        shapes[2] = new Rectangle(6.0,2.0);

        System.out.println("Shapes: ");
        for ( Polygon p : shapes ) {
            System.out.println(p);
            System.out.println("has area " + p.area() +
                    " and perimeter " + p.perimeter() );
            System.out.println();
        }
    }
}