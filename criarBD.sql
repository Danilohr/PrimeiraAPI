use API;
create table Movies(
	idMov int primary key, 
  name varchar(50) not null,
  releaseYear smallint,
  duration smallint
);
insert into Movies(idMov, name, releaseYear, duration) values (1, 'Interestellar', 2014, 174);

drop procedure if exists create_movies;
CREATE PROCEDURE create_movies(in starts INT, in ends INT)
BEGIN
    DECLARE i INT DEFAULT starts;
    while i <= ends do 
    	insert into Movies(idMov, name) values (i, concat('Movie ', i));
      set i = i+1;
    end while;
END;

call create_movies(2, 10);