
class Mammal  {
    void main() {
        System.out.println("This mammal walks");
    }
}

class DogMultilevel extends Mammal {
    void bark() {
        System.out.println("The dog barks");
    }
}

public class RunTimePoly{
public static void main(String[] args) {
    System.out.println("Multilevel Inheritance:");
    DogMultilevel dogMultilevel = new DogMultilevel();
    dogMultilevel.bark(); // Inherited from Mammal
    dogMultilevel.bark(); // DogMultilevel's own method
    System.out.println();
}
}