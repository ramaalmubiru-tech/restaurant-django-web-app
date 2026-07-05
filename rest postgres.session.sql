DROP USER IF EXISTS ramaal_user;
CREATE DATABASE ramaal_restaurant_db;
CREATE USER ramaal_user WITH PASSWORD '1998musa';
GRANT ALL PRIVILEGES ON DATABASE ramaal_restaurant_db TO ramaal_user;
\q

