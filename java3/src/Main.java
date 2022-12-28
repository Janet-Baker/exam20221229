public class Main {
    public static void main(String[] args) {
        Student s1 = new Student();
        Student s2 = new Student("s2", 17102, "171");
        s1.print();
        s2.print();
        Student.getCount();
    }
}