--- Banco de dados Padrão ---

CREATE DATABASE braco WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';

create user robo with encrypted password 'robolegal';
grant all privileges on database braco to robo;

CREATE TABLE movimento_manual (
    id SERIAL PRIMARY KEY,
    moveUp INTEGER,
    moveDown INTEGER,
    moveRight INTEGER,
    moveLeft INTEGER
);

ALTER TABLE movimento_manual OWNER TO robo;

commit;