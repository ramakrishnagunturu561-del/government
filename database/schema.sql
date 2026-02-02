CREATE DATABASE IF NOT EXISTS welfare_system;
USE welfare_system;

CREATE TABLE beneficiaries (
    beneficiary_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    mobile_number VARCHAR(15),
    scheme_name VARCHAR(50),
    amount DECIMAL(10,2),
    delivery_mode VARCHAR(20),
    delivery_date DATE,
    status VARCHAR(20),
    updated_by VARCHAR(50),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE call_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    beneficiary_id INT,
    mobile_number VARCHAR(15),
    call_type VARCHAR(50),
    call_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
