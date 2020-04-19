package mo.springframwork.spring5webapp.repositories;

import mo.springframwork.spring5webapp.domain.Author;
import org.springframework.data.repository.CrudRepository;

public interface AuthorRepository extends CrudRepository<Author,Long > {
}
