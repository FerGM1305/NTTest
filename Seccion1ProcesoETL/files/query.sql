CREATE DATABASE ntgroup;

USE ntgroup;


CREATE TABLE companies (
    company_id VARCHAR(24) NOT NULL PRIMARY KEY,
    name VARCHAR(130)
);

CREATE TABLE charges (
    id VARCHAR(24) NOT NULL PRIMARY KEY,
    company_id VARCHAR(24) NOT NULL,
    amount DECIMAL(16, 2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    paid_at TIMESTAMP NULL,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE VIEW total_transactions_per_day AS
SELECT name, DATE(created_at) AS transaction_date, SUM(amount) AS total_amount
FROM charges
JOIN companies ON charges.company_id = companies.company_id
GROUP BY name, DATE(created_at);

