import java.awt.*; import java.awt.event.*; import javax.swing.*;
import javax.swing.event.TableModelEvent; import javax.swing.event.TableModelListener;
import javax.swing.table.DefaultTableModel; import java.util.Comparator; import java.util.List;
import java.util.ArrayList; import java.io.*; import com.google.gson.Gson;
import com.google.gson.GsonBuilder; import com.google.gson.reflect.TypeToken;
public class PeopleTableApp extends JFrame {
    private DefaultTableModel model;
    private JTable table;
    private Phonebook phonebook;
    public PeopleTableApp() {
        setTitle("Телефонный справочник");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(747, 474);
        model = new DefaultTableModel();
        model.addColumn("Фамилия");
        model.addColumn("Имя");
        model.addColumn("Телефон 1");
        model.addColumn("Телефон 2");
        model.addColumn("Телефон 3");
        phonebook = new Phonebook();
        phonebook.loadFromJson("phonebook.json");
        List<Phonebook.RowData> rowDataList = phonebook.getRowDataList();
        for (Phonebook.RowData rowData : rowDataList) {
            model.addRow(new Object[]{rowData.getLastName(), rowData.getFirstName(),
                    rowData.getPhone1(), rowData.getPhone2(), rowData.getPhone3()});
        }
        table = new JTable(model); JScrollPane scrollPane = new JScrollPane(table);
        add(scrollPane, BorderLayout.CENTER);
        JPanel buttonPanel = new JPanel();
        addButton(buttonPanel, "Добавить", e -> addPerson());
        addButton(buttonPanel, "Удалить", e -> removePerson());
        addButton(buttonPanel, "Поиск по фамилии", e -> searchByLastName());
        addButton(buttonPanel, "Поиск по номеру телефона", e -> searchByPhoneNumber());
        add(buttonPanel, BorderLayout.SOUTH);
        model.addTableModelListener(new TableModelListener() {
            @Override
            public void tableChanged(TableModelEvent e) {
                if (e.getType() == TableModelEvent.UPDATE || e.getType() == TableModelEvent.INSERT) {
                    sortTable();
                }
            }
        });
        setVisible(true);
    }
    private void addButton(Container container, String text, ActionListener actionListener) {
        JButton button = new JButton(text);
        button.addActionListener(actionListener);
        container.add(button);
    }
    private void addPerson() {
        String lastName = JOptionPane.showInputDialog("Введите фамилию:");
        String firstName = JOptionPane.showInputDialog("Введите имя:");
        String phone1 = JOptionPane.showInputDialog("Введите телефон 1:");
        String phone2 = JOptionPane.showInputDialog("Введите телефон 2:");
        String phone3 = JOptionPane.showInputDialog("Введите телефон 3:");
        model.addRow(new Object[]{lastName, firstName, phone1, phone2, phone3});
        phonebook.addRowData(new Phonebook.RowData(lastName, firstName, phone1, phone2, phone3));
        updatePersonData();
    }
    private void removePerson() {
        int selectedRow = table.getSelectedRow();
        if (selectedRow != -1) {
            model.removeRow(selectedRow);
            phonebook.removeRowData(selectedRow);
            updatePersonData();
        } else { JOptionPane.showMessageDialog(this, "Выберите строку для удаления"); }
    }
    private void searchByLastName() {
        String searchLastName = JOptionPane.showInputDialog("Введите фамилию для поиска:");
        List<Integer> matchingIndexes = new ArrayList<>();
        for (int i = 0; i < model.getRowCount(); i++) {
            String lastName = (String) model.getValueAt(i, 0);
            if (lastName.equalsIgnoreCase(searchLastName)) {
                matchingIndexes.add(i);
            }
        }
        if (!matchingIndexes.isEmpty()) {
            int[] indexesArray = matchingIndexes.stream().mapToInt(Integer::intValue).toArray();
            table.setRowSelectionInterval(indexesArray[0], indexesArray[indexesArray.length - 1]);
            table.scrollRectToVisible(table.getCellRect(indexesArray[0], 0, true));
        }
        else { JOptionPane.showMessageDialog(this, "Человек с фамилией '" + searchLastName + "' не найден"); }
    }
    private void searchByPhoneNumber() {
        String searchNumber = JOptionPane.showInputDialog("Введите номер телефона для поиска:");
        for (int i = 0; i < model.getRowCount(); i++) {
            for (int j = 2; j <= 4; j++) {
                String phoneNumber = (String) model.getValueAt(i, j);
                if (phoneNumber.equals(searchNumber)) {
                    table.setRowSelectionInterval(i, i);
                    table.scrollRectToVisible(table.getCellRect(i, 0, true));
                    return;
                }
            }
        }
        JOptionPane.showMessageDialog(this, "Человек с номером телефона '" + searchNumber + "' не найден");
    }
    private boolean sorting = false;
    private void sortTable() {
        if (sorting) { return; }
        sorting = true;
        List<Phonebook.RowData> rowDataList = new ArrayList<>();
        for (int i = 0; i < model.getRowCount(); i++) {
            String lastName = (String) model.getValueAt(i, 0);
            String firstName = (String) model.getValueAt(i, 1);
            String phone1 = (String) model.getValueAt(i, 2);
            String phone2 = (String) model.getValueAt(i, 3);
            String phone3 = (String) model.getValueAt(i, 4);
            rowDataList.add(new Phonebook.RowData(lastName, firstName, phone1, phone2, phone3));
        }
        rowDataList.sort(Comparator
                .comparing(Phonebook.RowData::getLastName)
                .thenComparing(Phonebook.RowData::getFirstName)
                .thenComparing(Phonebook.RowData::getPhone1)
                .thenComparing(Phonebook.RowData::getPhone2)
                .thenComparing(Phonebook.RowData::getPhone3)
        );
        model.setRowCount(0);
        for (Phonebook.RowData rowData : rowDataList) {
            model.addRow(new Object[]{rowData.getLastName(), rowData.getFirstName(),
                    rowData.getPhone1(), rowData.getPhone2(), rowData.getPhone3()});
        }
        updatePersonData();
        sorting = false;
    }
    private void updatePersonData() {
        List<Phonebook.RowData> rowDataList = new ArrayList<>();
        for (int i = 0; i < model.getRowCount(); i++) {
            String lastName = (String) model.getValueAt(i, 0);
            String firstName = (String) model.getValueAt(i, 1);
            String phone1 = (String) model.getValueAt(i, 2);
            String phone2 = (String) model.getValueAt(i, 3);
            String phone3 = (String) model.getValueAt(i, 4);
            rowDataList.add(new Phonebook.RowData(lastName, firstName, phone1, phone2, phone3));
        }
        phonebook.updateAllRowData(rowDataList);
    }
    public static void main(String[] args) { SwingUtilities.invokeLater(() -> new PeopleTableApp()); }
}
class Phonebook {
    private List<RowData> rowDataList = new ArrayList<>();
    private Gson gson;
    public Phonebook() { gson = new GsonBuilder().setPrettyPrinting().create(); }
    public List<RowData> getRowDataList() { return rowDataList; }
    public void addRowData(RowData rowData) {
        rowDataList.add(rowData);
        saveToJson("phonebook.json");
    }
    public void removeRowData(int index) {
        if (index >= 0 && index < rowDataList.size()) {
            rowDataList.remove(index);
            saveToJson("phonebook.json");
        }
    }
    public void updateAllRowData(List<RowData> newData) {
        rowDataList = newData;
        saveToJson("phonebook.json");
    }
    public void loadFromJson(String filename) {
        try (Reader reader = new FileReader(filename)) {
            rowDataList = gson.fromJson(reader, new TypeToken<List<RowData>>() {}.getType());
            if (rowDataList == null) { rowDataList = new ArrayList<>(); }
        } catch (IOException e) { e.printStackTrace(); }
    }
    private void saveToJson(String filename) {
        try (Writer writer = new FileWriter(filename)) { gson.toJson(rowDataList, writer); }
        catch (IOException e) { e.printStackTrace(); }
    }
    public static class RowData {
        private String lastName; private String firstName;
        private String phone1; private String phone2; private String phone3;
        public RowData(String lastName, String firstName, String phone1, String phone2, String phone3) {
            this.lastName = lastName;
            this.firstName = firstName;
            this.phone1 = phone1;
            this.phone2 = phone2;
            this.phone3 = phone3;
        }
        public String getLastName() { return lastName; }
        public String getFirstName() { return firstName; }
        public String getPhone1() { return phone1; }
        public String getPhone2() { return phone2; }
        public String getPhone3() { return phone3; }
    }
}