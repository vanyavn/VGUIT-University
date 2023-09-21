import java.util.Vector;

public abstract class Item {
    privateString title;
    private double basePrice;
    privateint year;

    public Item(String title, double basePrice, int year) {
        this.title=title;
        this.basePrice=basePrice;
        this.year=year;
    }

    public StringgetTitle() {
        return title;
    }

    public abstract double getPrice();

    public String toString() {
        returnString.format("%s\nYear: %d\nBase price: %.2f", title, year, basePrice);
    }

    public int getYear() {
        return year;
    }
}

class MusicCD extends Item {
    private String albumName;
    private String artistName;
    private int releaseYear;
    private double basePrice;
    private int dlit;

    public MusicCD(String albumName, String artistName, int releaseYear, double basePrice, int dlit) {
        super(albumName, basePrice, releaseYear);
        this.albumName=albumName;
        this.artistName=artistName;
        this.releaseYear=releaseYear;
        this.basePrice=basePrice;
        this.dlit=dlit;
    }

    @Override
    public double getPrice() {
        return basePrice;
    }

    @Override
    public StringtoString() {
        return"MusicCD\n"+
                "Album: "+albumName+
                "\nArtist: "+artistName+
                "\nRelease Year: "+releaseYear+
                "\nDlit: "+dlit+" min"+
                "\nPrice: $"+getPrice();
    }
}

class MovieDVD extends Item {
    private String title2;
    private String directorName;
    private int releaseYear;
    private double basePrice2;
    private int dlit;
    private String genre;
    private Vector<String> languages;
    private Vector<String> subtitles;

    public MovieDVD(String title, String directorName, int releaseYear, double basePrice, int dlit,  String genre,
                    String language, String subtitle) {
        super(title, basePrice, releaseYear);
        this.title=title;
        this.directorName=directorName;
        this.releaseYear=releaseYear;
        this.basePrice=basePrice;
        this.dlit=dlit;
        this.genre=genre;
        this.languages=new Vector<String>();
        this.languages.add(language);
        this.subtitles=new Vector<String>();
        this.subtitles.add(subtitle);

    }

    @Override
    public doubleg etPrice() {
        doubleprice=basePrice;

        switch (genre) {
            case"comedy":
                price *=0.9; // 10%
                break;
            case"drama":
                price *=0.85; // 15% 
                break;
            case"series":
                price *=0.8; // 20% 
                break;
            default:
                break;
        }
        return price;
    }

    @Override
    public String toString() {
        return"MovieDVD\n"+
                "Title: "+ title +
                "\nGenre: "+ genre +
                "\nDirector: "+directorName+
                "\nRelease Year: "+releaseYear+
                "\nDlit: "+dlit+" min"+
                "\nLanguages: "+languages.toString() +
                "\nSubtitles: "+subtitles.toString() +
                "\nPrice: $"+getPrice();
    }
}

classBookextendsItem {
    private String author;
    private String publisher;
    private String title;
    private int numPages;
    private int publicationYear;
    private double basePrice;

    publicBook(String title, String author, String publisher, int publicationYear, 
                double basePrice, int numPages) {
        super(title, basePrice, publicationYear);
        this.author=author;
        this.publisher=publisher;
        this.numPages=numPages;
        this.title=title;
        this.publicationYear=publicationYear;
        this.basePrice=basePrice;

    }

    @Override
    publicStringtoString() {
        return"Book\n"+
                "Title: "+ title +
                "\nAuthor: "+ author +
                "\nPublisher: "+ publisher +
                "\nPublication Year: "+publicationYear+
                "\nNumber of Pages: "+numPages+
                "\nPrice: $"+getPrice();
    }

    @Override
    publicdoublegetPrice() {
        if (publicationYear<2010) {
            returnbasePrice*0.7;
        } else {
            return basePrice;
        }
    }
}

classTestItems {
    publicstaticvoidmain(String[] args) {
        Bookbook=newBook("Java Programming", "John Doe", "ABC Publishing", 2003, 29.99, 500);

        MusicCDmusicCD=newMusicCD("Greatest Hits", "The Beatles", 2000, 14.99, 60);

        MovieDVDmovieDVD=newMovieDVD("New Movie", "Vedmensky", 2011, 1999, 120, "drama", "Russian", "No subtitles");

        Vector<Item> items =new Vector<Item>();

        items.add(book);
        items.add(musicCD);
        items.add(movieDVD);

        for (Item item: items) {
            System.out.println(item);
            System.out.println();
        }
    }
}
