class Literature {
    private int sourceCode;
    private String type;
    private String title;
    private int yearPublisher;
    private String publisherName;
    private int pageCount;
    private String[] authors;
    private String language;
    public Literature(int sourceCode, String type, String title, int yearPublisher, String publisherName, int pageCount, String[] authors, String language) {
        this.sourceCode = sourceCode;
        this.type = type;
        this.title = title;
        this.yearPublisher = yearPublisher;
        this.publisherName = publisherName;
        this.pageCount = pageCount;
        this.authors = authors;
        this.language = language;
    }
    public int getSourceCode() { return sourceCode; }
    public void setSourceCode(int sourceCode) { this.sourceCode = sourceCode; }
    public String getType() { return type; }
    public void setType(String type) { this.type = type; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public int getYearPublisher() { return yearPublisher; }
    public void setYearPublisher(int yearPublisher) { this.yearPublisher = yearPublisher; }
    public String getPublisherName() { return publisherName; }
    public void setPublisherName(String publisherName) { this.publisherName = publisherName; }
    public int getPageCount() { return pageCount; }
    public void setPageCount(int pageCount) { this.pageCount = pageCount; }
    public String[] getAuthors() { return authors; }
    public void setAuthors(String[] authors) { this.authors = authors; }
    public String getLanguage() { return language; }
    public void setLanguage(String language) { this.language = language; }
    @Override
    public String toString() {
        return "Код источника литературы: " + this.sourceCode +
                "\nТип литературы: " + this.type +
                "\nНазвание: " + this.title +
                "\nГод издательства: " + this.yearPublisher +
                "\nНазвание издательства: " + this.publisherName +
                "\nЧисло страниц: " + this.pageCount +
                "\nАвторы: " + String.join(", ", this.authors) +
                "\nЯзык: " + this.language;
    }
    public static void main(String[] args) {
        String[] authors = {"Илья Ильф", "Евгений Петров"};
        Literature book = new Literature(838655, "Сборник", "Двенадцать стульев. Золотой теленок. Светлая личность", 2009, "ACT", 288, authors, "русский");
        System.out.println(book.toString());
    }
}