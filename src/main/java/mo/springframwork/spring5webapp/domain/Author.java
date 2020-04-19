package mo.springframwork.spring5webapp.domain;

import java.util.Set;

public class Author {
    private String firstname;
    private String lastname;
    private Set<Book> book;

    public Author() {
    }

    public Author(String firstname, String lastname, Set<Book> book) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.book = book;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public Set<Book> getBook() {
        return book;
    }

    public void setBook(Set<Book> book) {
        this.book = book;
    }
}
