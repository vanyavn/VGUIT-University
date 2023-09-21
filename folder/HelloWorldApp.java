import javax.swing.*;
public class HelloWorldApp {
public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> { //запускаем приложение Swing в потоке обработки событий
JFrame frame = new JFrame("Hello World");
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
JLabel label = new JLabel("Hello World!");
frame.getContentPane().add(label);
frame.pack(); //подгоняем размер окна под содержимое
frame.setVisible(true);
        });
    }
}
