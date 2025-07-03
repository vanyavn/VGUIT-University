import java.util.ArrayList;

public class SchoolSubjectDemo {
    public static void main(String[] args) {
        SchoolSubject math = new SchoolSubject("Математика", "Иванова О.П.");
        math.addStudent("Петров А.И.");
        math.addStudent("Сидорова М.В.");
        math.addStudent("Козлов Д.С.");
        System.out.println("\nИнформация о предмете:");
        math.printInfo();
        math.removeStudent("Сидорова М.В.");
        System.out.println("\nПосле удаления ученика:");
        math.printInfo();
    }
}

class SchoolSubject {
    private String name;
    private String teacher;
    private ArrayList<String> students;
    public SchoolSubject(String name, String teacher) {
        this.name = name;
        this.teacher = teacher;
        this.students = new ArrayList<>();
    }
    public void addStudent(String student) { students.add(student); }
    public void removeStudent(String student) { students.remove(student); }
    public void printInfo() {
        System.out.println("Предмет: " + name);
        System.out.println("Учитель: " + teacher);
        System.out.println("Ученики: " + String.join(", ", students));
    }
}