import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class DrawingApp extends JFrame {
    private Color currentColor = Color.BLACK;
    private int currentThickness = 2;
    private Point startPoint = null;
    private Point endPoint = null;

    public DrawingApp() {
        setTitle("Простой рисовальщик");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JMenuBar menuBar = new JMenuBar();
        setJMenuBar(menuBar);
        
        JMenu colorMenu = new JMenu("Цвет");
        menuBar.add(colorMenu);
        
        JMenuItem blackMenuItem = new JMenuItem("Черный");
        blackMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) { currentColor = Color.BLACK; }
        });
        colorMenu.add(blackMenuItem);
        
        JMenuItem redMenuItem = new JMenuItem("Красный");
        redMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) { currentColor = Color.RED; }
        });
        colorMenu.add(redMenuItem);
        
        JMenu thicknessMenu = new JMenu("Толщина линии");
        menuBar.add(thicknessMenu);
        
        JMenuItem thinMenuItem = new JMenuItem("Тонкая");
        thinMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                currentThickness = 2;
            }
        });
        thicknessMenu.add(thinMenuItem);
        
        JMenuItem mediumMenuItem = new JMenuItem("Средняя");
        mediumMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                currentThickness = 5;
            }
        });
        thicknessMenu.add(mediumMenuItem);
        
        JMenuItem thickMenuItem = new JMenuItem("Толстая");
        thickMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                currentThickness = 10;
            }
        });
        thicknessMenu.add(thickMenuItem);
        
        addMouseListener(new MouseAdapter() {
            public void mousePressed(MouseEvent e) {
                startPoint = e.getPoint();
            }
            
            public void mouseReleased(MouseEvent e) {
                endPoint = e.getPoint();
                repaint();
            }
        });

        addMouseMotionListener(new MouseMotionAdapter() {
            public void mouseDragged(MouseEvent e) {
                endPoint = e.getPoint();
                repaint();
            }
        });
    }

    public void paint(Graphics g) {
        if (startPoint != null && endPoint != null) {
            Graphics2D g2d = (Graphics2D) g;
            g2d.setColor(currentColor);
            g2d.setStroke(new BasicStroke(currentThickness));
            g2d.drawLine(startPoint.x, startPoint.y, endPoint.x, endPoint.y);
            startPoint = endPoint;
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                DrawingApp app = new DrawingApp();
                app.setVisible(true);
            }
        });
    }
}