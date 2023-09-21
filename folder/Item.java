import java.io.*;
import java.util.ArrayList;
import java.util.List;
class Item {
    protected String title;
    protected double price;
    public Item(String title, double price) {
        this.title = title;
        this.price = price;
    }
    public String getTitle() { return title; }
    public double getPrice() { return price; }
    public void display() {
        System.out.println("Title: " + title);
        System.out.println("Price: $" + price);
    }
}
class Book extends Item {
    private String author;
    private int pageCount;
    public Book(String title, double price, String author, int pageCount) {
        super(title, price);
        this.author = author;
        this.pageCount = pageCount;
    }
    public String getAuthor() { return author; }
    public int getPageCount() { return pageCount; }
    @Override
    public void display() {
        super.display();
        System.out.println("Author: " + author);
        System.out.println("Page Count: " + pageCount);
    }
}
class MusicCD extends Item {
    private String artist;
    private int trackCount;
    public MusicCD(String title, double price, String artist, int trackCount) {
        super(title, price);
        this.artist = artist;
        this.trackCount = trackCount;
    }
    public String getArtist() { return artist; }
    public int getTrackCount() { return trackCount; }
    @Override
    public void display() {
        super.display();
        System.out.println("Artist: " + artist);
        System.out.println("Track Count: " + trackCount);
    }
}
class MusicDVD extends Item {
    private String artist;
    private int duration;
    public MusicDVD(String title, double price, String artist, int duration) {
        super(title, price);
        this.artist = artist;
        this.duration = duration;
    }
    public String getArtist() { return artist; }
    public int getDuration() { return duration; }
    @Override
    public void display() {
        super.display();
        System.out.println("Artist: " + artist);
        System.out.println("Duration: " + duration + " minutes");
    }
}
class Vyvod {
    public static void main(String[] args) {
        List<Item> collection = new ArrayList<>();
        collection.add(new Book("The Great Gatsby", 9.99, "F. Scott Fitzgerald", 180));
        collection.add(new MusicCD("Abbey Road", 14.99, "The Beatles", 17));
        collection.add(new MusicDVD("Live at Wembley Stadium", 19.99, "Queen", 120));
        writeCollectionToFile(collection, "collection.txt");
        List<Item> loadedCollection = readCollectionFromFile("collection.txt");
        if (loadedCollection != null) {
            System.out.println("Loaded Collection:");
            for (Item item : loadedCollection) {
                item.display();
                System.out.println();
            }
        }
    }
    private static void writeCollectionToFile(List<Item> collection, String filename) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(filename))) {
            for (Item item : collection) {
                writer.println(item.getClass().getSimpleName());
                writer.println(item.getTitle());
                writer.println(item.getPrice());
                if (item instanceof Book) {
                    Book book = (Book) item;
                    writer.println(book.getAuthor());
                    writer.println(book.getPageCount());
                } else if (item instanceof MusicCD) {
                    MusicCD musicCD = (MusicCD) item;
                    writer.println(musicCD.getArtist());
                    writer.println(musicCD.getTrackCount());
                } else if (item instanceof MusicDVD) {
                    MusicDVD musicDVD = (MusicDVD) item;
                    writer.println(musicDVD.getArtist());
                    writer.println(musicDVD.getDuration());
                }
                writer.println();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private static List<Item> readCollectionFromFile(String filename) {
        List<Item> collection = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String itemType = line.trim();
                String title = reader.readLine();
                double price = Double.parseDouble(reader.readLine());
                if (itemType.equals("Book")) {
                    String author = reader.readLine();
                    int pageCount = Integer.parseInt(reader.readLine());
                    collection.add(new Book(title, price, author, pageCount));
                } else if (itemType.equals("MusicCD")) {
                    String artist = reader.readLine();
                    int trackCount = Integer.parseInt(reader.readLine());
                    collection.add(new MusicCD(title, price, artist, trackCount));
                } else if (itemType.equals("MusicDVD")) {
                    String artist = reader.readLine();
                    int duration = Integer.parseInt(reader.readLine());
                    collection.add(new MusicDVD(title, price, artist, duration));
                }
                reader.readLine();
            }
        } catch (IOException e) { e.printStackTrace(); }
        return collection;
    }
}