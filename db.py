import sqlite3
from tkinter import messagebox
import os

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.db_file = "hospital.db"
        self.connect()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.cursor = self.connection.cursor()
            self.create_tables()
            return True
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error connecting to database: {err}")
            return False

    def create_tables(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS hospital (
                    NameofTablets TEXT,
                    ref TEXT PRIMARY KEY,
                    Dose TEXT,
                    NumberofTablets TEXT,
                    Lot TEXT,
                    IssueDate TEXT,
                    ExpDate TEXT,
                    DailyDose TEXT,
                    StorageAdvice TEXT,
                    nhsNumber TEXT,
                    PatientName TEXT,
                    DateOfBirth TEXT,
                    PatientAddress TEXT
                )
            """)
            self.connection.commit()
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error creating tables: {err}")

    def check_connection(self):
        if not self.connection or not self.cursor:
            if not self.connect():
                return False
        return True

    def insert_patient(self, data):
        if not self.check_connection():
            return False
            
        try:
            query = """INSERT INTO hospital 
                    (NameofTablets, ref, Dose, NumberofTablets, Lot, IssueDate, 
                    ExpDate, DailyDose, StorageAdvice, nhsNumber, PatientName, 
                    DateOfBirth, PatientAddress) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            self.cursor.execute(query, data)
            self.connection.commit()
            return True
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error inserting data: {err}")
            return False

    def update_patient(self, data):
        if not self.check_connection():
            return False
            
        try:
            query = """UPDATE hospital SET 
                    NameofTablets=?, Dose=?, NumberofTablets=?, Lot=?, 
                    IssueDate=?, ExpDate=?, DailyDose=?, StorageAdvice=?, 
                    nhsNumber=?, PatientName=?, DateOfBirth=?, PatientAddress=? 
                    WHERE ref=?"""
            self.cursor.execute(query, data)
            self.connection.commit()
            return True
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error updating data: {err}")
            return False

    def delete_patient(self, ref):
        if not self.check_connection():
            return False
            
        try:
            query = "DELETE FROM hospital WHERE ref=?"
            self.cursor.execute(query, (ref,))
            self.connection.commit()
            return True
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error deleting data: {err}")
            return False

    def fetch_all_patients(self):
        if not self.check_connection():
            return []
            
        try:
            self.cursor.execute("SELECT * FROM hospital")
            return self.cursor.fetchall()
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error fetching data: {err}")
            return []

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None 