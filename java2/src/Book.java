public class Book {
    private String bookname;
    private double price;
    private String publisher;
    private String author;
    public Book(String bookname, double price, String publisher, String author){
        this.bookname = bookname;
        this.price = price;
        this.publisher = publisher;
        this.author = author;
    }
    public void print(){
        StringBuilder cache = new StringBuilder();
        cache.append(bookname);
        cache.append(", ");
        cache.append(String.format("%.2f", price));
        cache.append(", ");
        cache.append(publisher);
        cache.append(", ");
        cache.append(author);
        System.out.println(cache);
    }
}
