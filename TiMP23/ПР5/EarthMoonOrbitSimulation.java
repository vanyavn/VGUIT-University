import java.awt.*;
import javax.swing.*;
public class EarthMoonOrbitSimulation extends JPanel {
    private int earthRadius = 100;
    private int moonRadius = 25;
    private double earthAngle = 0;
    private double moonAngle = 0;
    private double earthOrbitRadius = 200;
    private double moonOrbitRadius = 60;
    private double moonDistance = 0;
    public EarthMoonOrbitSimulation() {
        Timer timer = new Timer(50, e -> {
            earthAngle += 0.02; // Угол вращения Земли
            moonAngle += 0.05; // Угол вращения Луны
            moonDistance = moonOrbitRadius * Math.sin(moonAngle); // Расстояние Луны от Земли
            repaint();
        });
        timer.start();
    }
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        int centerX = getWidth() / 2;
        int centerY = getHeight() / 2;
        // Задаем фон
        g.setColor(new Color(0, 0, 50)); // Темно-синий фон
        g.fillRect(0, 0, getWidth(), getHeight());

        // Рисуем Землю
        g.setColor(new Color(0, 100, 255)); // Светло-синяя Земля
        g.fillOval(centerX - earthRadius, centerY - earthRadius, earthRadius * 2, earthRadius * 2);

        // Рисуем ось вращения Земли
        g.setColor(Color.WHITE);
        g.drawLine(centerX, centerY, centerX, centerY + earthRadius);

        // Рисуем Луну
        int moonX = centerX + (int) (earthOrbitRadius * Math.cos(earthAngle)) - moonRadius;
        int moonY = centerY + (int) (earthOrbitRadius * Math.sin(earthAngle)) - moonRadius;
        g.setColor(new Color(192, 192, 192)); // Серебристая Луна
        g.fillOval(moonX, moonY, moonRadius * 2, moonRadius * 2);

        // Рисуем ось вращения Луны
        g.setColor(Color.WHITE);
        g.drawLine(centerX, centerY, moonX + moonRadius, moonY + moonRadius);

        // Скрываем Луну, когда она находится за Землей
        if (moonX + moonRadius >= centerX) {
            g.setColor(new Color(0, 0, 50)); // Скрываем Луну
            g.fillOval(moonX, moonY, moonRadius * 2, moonRadius * 2);
        }
    }
    public static void main(String[] args) {
        JFrame frame = new JFrame("Моделирование Земли и Луны");
        EarthMoonOrbitSimulation simulation = new EarthMoonOrbitSimulation();
        frame.add(simulation);
        frame.setSize(1000, 555);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}