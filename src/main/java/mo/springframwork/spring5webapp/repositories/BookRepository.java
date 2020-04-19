package mo.springframwork.spring5webapp.repositories;

import mo.springframwork.spring5webapp.domain.Book;
import org.springframework.data.repository.CrudRepository;

public interface BookRepository extends CrudRepository<Book,Long> {
}
