CREATE DATABASE pentaho_test;

CREATE USER 'curso' IDENTIFIED BY 'curso';

GRANT ALL PRIVILEGES ON *.* TO 'curso'@'172.15.0.0/255.255.0.0';
GRANT ALL PRIVILEGES ON *.* TO 'curso'@'localhost';

FLUSH PRIVILEGES;