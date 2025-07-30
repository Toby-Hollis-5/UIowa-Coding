import java.lang.Math;
public class Triangle implements Polygon {

    private double a;
    private double b;
    private double c;

    public Triangle() {
        this.a = 3;
        this.b = 4;
        this.c = 5;
    }

    public Triangle(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getA() {
        return a;
    }

    public void setA(double a) {
        this.a = a;
    }

    public double getB() {
        return b;
    }

    public void setB(double b) {
        this.b = b;
    }

    public double getC() {
        return c;
    }

    public void setC(double c) {
        this.c = c;
    }

    @Override
    public String toString() {
        return "Triangle edge lengths: " + a + ", " + b + ", " + c;
    }

    //Now implement Polygon.

    @Override
    public double area() {
        double s=(a+b+c)/2;
        double x = s-a;
        double y = s-b;
        double z = s-c;
        double m = x*y*z;
        //double area = Math.sqrt(s*(s − a)*(s − b)*(s−c))
        double sqrt = s*m;
        double area = Math.sqrt(sqrt);
        return area;
    }

    @Override
    public double perimeter() {
        double perimeter = a+b+c;
        return perimeter;
    }

}


/*
Create a class called Triangle that uses the Polygon interface;
    Assume this is a right triangle

    double  a, b, c;

Must have a default constructor that sets:
    a = 3
    b = 4
    c = 5

Must have a Constructor that takes in 3 variables:
    a --> 1st argument
    b --> 2nd argument
    c --> 3rd argument

Must have setters and getters for all the variables
    double getA()
    void setA()
    ...
    ...

Must have a toString (test Provided)
    "String toString()" Should return the following:
        "Triangle edge lengths: " + a + ", " + b + ", " + c
 */

