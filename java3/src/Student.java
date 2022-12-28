public class Student {
    private static int count;
    private String name;
    private int id;
    private String classname;

    public Student(String name, int id, String classname){
        this.name = name;
        this.id = id;
        this.classname = classname;
        this.count++;
    }
    public Student(){
        this("s1", 17101, "171");
    }

    public void print(){
        System.out.print(this.name);
        System.out.print(", ");
        System.out.print(this.id);
        System.out.print(", ");
        System.out.print(this.classname);
        System.out.print("; ");
    }
    public static void getCount(){
        System.out.print("count=");
        System.out.println(count);
    }
}
