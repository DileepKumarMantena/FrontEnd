import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
public class FileReaderExample {
public static void main(String[] args) {
try 
(BufferedReader reader = new BufferedReader(new FileReader("C:\\Users\\user\\Downloads\\Projects\\Mine\\Full_Stack_Development\\Java\\output.txt"))) {
String line;
while 
((line = reader.readLine()) != null) {
System.out.println(line);
}
} catch (IOException e) {
e.printStackTrace();
}
}
}