import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class BouncingShapeApp extends JFrame implements ActionListener {
private static final int WIDTH = 700;
    private static final int HEIGHT = 500;
    private static final int SHAPE_SIZE = 50;
    private static final int DELTA = 1;
    private static final int CIRCLE_SIZE = 50;
    private int square1X;
    private int square1Y;
    private int square2X;
    private int square2Y;
    private int rectangleX;
    private int rectangleY;
    private int triangleX;
    private int triangleY;
    private int dx;
    private int dy;
    private int dx1;
    private int dy1;
    private int dx2;
    private int dy2;
    private int dx3;
    private int dy3;
    private int dx4;
    private int dy4;
    private int circley;
    private int circlex;
    public BouncingShapeApp() {
square1X = 0;
square1Y = 0;
square2X = 100;
square2Y = 100;
rectangleX = 300;
rectangleY = 200;
triangleX = 150;
triangleY = 200;
circlex = 350;
circley = 350;
dx = DELTA;
dy = DELTA;
dx1 = DELTA;
dy1 = DELTA;
dx2 = DELTA;
dy2 = DELTA;
dx3 = DELTA;
dy3 = DELTA;
dx4 = DELTA;
dy4 = DELTA;
initializeGUI();
startAnimation();
}
private void initializeGUI() {
        setTitle("Алиев");
setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
setSize(WIDTH, HEIGHT);
setResizable(false);
JPanel panel = new JPanel() {
@Override
protected void paintComponent(Graphics g) {
super.paintComponent(g);
g.setColor(Color.BLUE);
g.fillRect(square1X, square1Y, SHAPE_SIZE, SHAPE_SIZE);
g.setColor(Color.CYAN);
g.fillRect(square2X, square2Y, SHAPE_SIZE, SHAPE_SIZE);
g.setColor(Color.GREEN);
g.fillRect(rectangleX, rectangleY, SHAPE_SIZE*2, SHAPE_SIZE);
g.setColor(Color.RED);
                int[] xPoints = {triangleX, triangleX + SHAPE_SIZE, triangleX + SHAPE_SIZE / 2};
                int[] yPoints = {triangleY + SHAPE_SIZE, triangleY + SHAPE_SIZE, triangleY};
g.fillPolygon(xPoints, yPoints, 3);

g.setColor(Color.DARK_GRAY);
g.fillOval(circlex, circley, CIRCLE_SIZE, CIRCLE_SIZE);
}
        };
getContentPane().add(panel);
}
private void startAnimation() {
        Timer timer = new Timer(1, this);//this указывает, что start Animation будет обрабатывать события, генерируемые таймером
timer.start();
}
@Override
public void actionPerformed(ActionEvent e) {
        square1X += dx1;
        square1Y += dy1;
        square2X += dx2;
        square2Y += dy2;
        rectangleX += dx;
        rectangleY += dy;
        triangleX += dx3;
        triangleY += dy3;
        circlex += dx4;
        circley += dy4;
        if (square1X <= 0 || square1X >= WIDTH - SHAPE_SIZE) { dx1 = -dx1; } // по горизонтали
        if (square1Y <= 0 || square1Y >= HEIGHT - SHAPE_SIZE) { dy1 = -dy1; } //квадрат = длина окна минус длина квадрата; по вертикали
        if (square2X <= 0 || square2X >= WIDTH - SHAPE_SIZE) { dx2 = -dx2; } // по горизонтали
        if (square2Y <= 0 || square2Y >= HEIGHT - SHAPE_SIZE) { dy2 = -dy2; } // по вертикали
        if (rectangleX <= 0 || rectangleX >= WIDTH - SHAPE_SIZE) { dx = -dx; } // по горизонтали
        if (rectangleY <= 0 || rectangleY >= HEIGHT - SHAPE_SIZE) { dy = -dy; } // по вертикали
        if (triangleX <= 0  || triangleX >= WIDTH - SHAPE_SIZE) { dx3 = -dx3; } // по горизонтали
        if (triangleY <= 0 || triangleY >= HEIGHT - SHAPE_SIZE) { dy3 = -dy3; } // повертикали
        if (circlex <= 0 || circlex >= WIDTH - CIRCLE_SIZE) { dx4 = -dx4; } // погоризонтали
        if (circley <= 0 || circley >= HEIGHT - CIRCLE_SIZE) { dy4 = -dy4; } // повертикали
        repaint();
}
public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {//для выполнения кода в потоке обработки событий Swing
BouncingShapeApp app = new BouncingShapeApp();
app.setVisible(true);//true указывает, чтоокнодолжнобытьвидимым
});
}
}
