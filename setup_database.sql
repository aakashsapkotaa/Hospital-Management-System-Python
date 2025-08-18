-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS new_schema;

-- Use the database
USE new_schema;

-- Create the hospital table if it doesn't exist
CREATE TABLE IF NOT EXISTS hospital (
    NameofTablets VARCHAR(100),
    ref VARCHAR(50) PRIMARY KEY,
    Dose VARCHAR(50),
    NumberofTablets VARCHAR(50),
    Lot VARCHAR(50),
    IssueDate VARCHAR(50),
    ExpDate VARCHAR(50),
    DailyDose VARCHAR(50),
    StorageAdvice VARCHAR(100),
    nhsNumber VARCHAR(50),
    PatientName VARCHAR(100),
    DateOfBirth VARCHAR(50),
    PatientAddress VARCHAR(200)
); 