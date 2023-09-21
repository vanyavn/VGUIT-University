import java.util.ArrayList;

public class LiteratureLibrary {
    String sourceCode;
    String literatureType;
    String title;
    int publicationYear;
    String publisher;
    int pageCount;
    String author;

    public LiteratureLibrary(String sourceCode, String literatureType, String title, int publicationYear, String publisher, int pageCount, String author) {
        this.sourceCode = sourceCode;
        this.literatureType = literatureType;
        this.title = title;
        this.publicationYear = publicationYear;
        this.publisher = publisher;
        this.pageCount = pageCount;
        this.author = author;
    }
}

class TechnicalLiterature extends LiteratureLibrary {
    String scienceField;
    int quantity;

    public TechnicalLiterature(String sourceCode, String literatureType, String title, int publicationYear, String publisher, int pageCount, String author, String scienceField, int quantity) {
        super(sourceCode, literatureType, title, publicationYear, publisher, pageCount, author);
        this.scienceField = scienceField;
        this.quantity = quantity;
    }
}

class Periodical extends LiteratureLibrary {
    String periodicalType;
    String publicationPeriod;

    public Periodical(String sourceCode, String literatureType, String title, int publicationYear, String publisher, int pageCount, String author, String periodicalType, String publicationPeriod) {
        super(sourceCode, literatureType, title, publicationYear, publisher, pageCount, author);
        this.periodicalType = periodicalType;
        this.publicationPeriod = publicationPeriod;
    }
}

class ReferenceBooks extends LiteratureLibrary {
    String direction;
    int volume;
    int part;

    public ReferenceBooks(String sourceCode, String literatureType, String title, int publicationYear, String publisher, int pageCount, String author, String direction, int volume, int part) {
        super(sourceCode, literatureType, title, publicationYear, publisher, pageCount, author);
        this.direction = direction;
        this.volume = volume;
        this.part = part;
    }
}

class LiteratureList {
    private ArrayList<LiteratureLibrary> literatureList;
    public LiteratureList() {
        literatureList = new ArrayList<>();
    }
    public void addLiterature(LiteratureLibrary literature) {
        literatureList.add(literature);
    }
    public void printLiteratureList() {
        for (LiteratureLibrary literature : literatureList) {
            System.out.println("Source Code: " + literature.sourceCode);
            System.out.println("Literature Type: " + literature.literatureType);
            System.out.println("Title: " + literature.title);
            System.out.println("Publication Year: " + literature.publicationYear);
            System.out.println("Publisher: " + literature.publisher);
            System.out.println("Page Count: " + literature.pageCount);
            System.out.println("Author: " + literature.author);
            System.out.println("\n- - - - - - - - - -\n");
        }
    }
}

class Vyvod {
    public static void main(String[] args) {
        System.out.println("\n");
        LiteratureList literatureList = new LiteratureList();
        TechnicalLiterature technicalLiterature = new TechnicalLiterature("89754331", "Technical", "Data Science. Basics of data collection, processing, analysis and visualization", 2023, "Self-released", 200, "Ivan Aliev", "Science Field A", 10);
        literatureList.addLiterature(technicalLiterature);
        Periodical periodical = new Periodical("8975432", "Periodical", "{ <> THE_UITS_NEWS <> }", 2023, "IBAS/ISIT/PI/UTS/S", 50, "UITS FACULTY (C)", "Type A", "Monthly");
        literatureList.addLiterature(periodical);
        ReferenceBooks referenceBook = new ReferenceBooks("8975433", "Reference", "Encyclopedia about Dinosaurs", 2008, "Pterodactyl Inc.", 404, "Willy Hendrix", "Direction A", 1, 2);
        literatureList.addLiterature(referenceBook);
        literatureList.printLiteratureList();
    }
}