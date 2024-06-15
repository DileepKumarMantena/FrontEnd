import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
public class FileWriterExample {
public static void main(String[] args) {
try (BufferedWriter writer = new BufferedWriter(new FileWriter("output.txt"))) {
String text = "Hello, File I/O in Java!";
writer.write(text);
} catch (IOException e) {
e.printStackTrace();
}
}
}