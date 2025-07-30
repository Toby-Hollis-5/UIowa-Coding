public class Rectangle implements Polygon {

    private double width;
    private double height;

    public Rectangle() {
        this.width = 1;
        this.height = 1;
    }

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public void setWidth(double width) {
        this.width = width;
    }

    public double getWidth() {
        return width;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public double getHeight() {
        return height;
    }

    @Override
    public String toString() {
        return "Rectangle width & height: " + width + ", " + height;
    }

    //Now implement Polygon.

    @Override
    public double area() {
        return width*height;
    }

    @Override
    public double perimeter() {
        return 2*width+2*height;
    }

}

/*
Create a class called Rectangle that implements the Polygon interface
Must have a default constructor that sets:
    double: width = 1
    double: height = 1

Must have another Constructor that takes in:
    double: width --> 1st argument
    double: height --> 2nd argument

Must have setters and getters for width and height.
double getWidth()
double getHeight()
void setHeight()
void setWidth()


Must have a toString (test Provided)
    "String toString()" should return the following:
        "Rectangle width & height: " + width + ", " + height
 */

