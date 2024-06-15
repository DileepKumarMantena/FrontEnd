public class ConditionalStatement2 {
    public static void main(String[] args) {
        int score = 85;
        String a="7+5";
       String[] parts=a.split("\\+");
       int num1=Integer.parseInt(parts[0]);
       int num2=Integer.parseInt(parts[1]);
       int result=num1+num2;
       System.out.println("Result++++"+result);





        if (score >= 90) {
            System.out.println("Excellent!");
}       else if (score >= 80) {
            System.out.println("Good!");
}       else if (score >= 70) {
            System.out.println("Average.");
}       else {
            System.out.println("Needs improvement");
}
    }
}


