import tkinter as tk
from tkinter import ttk, messagebox
from db import Database
from utils import validate_required_fields, format_prescription, clear_fields
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import datetime

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        
        # Make it fullscreen and responsive
        self.root.state('zoomed')  # Windows fullscreen
        self.root.configure(bg='#f8f9fa')
        
        # Get screen dimensions for responsive design
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        # Set minimum window size
        self.root.minsize(1200, 800)
        
        # Set modern style
        self.style = ttk.Style(theme='cosmo')
        
        # Initialize database
        self.db = Database()
        if not self.db.check_connection():
            messagebox.showerror("Error", "Could not connect to database. Please check your database configuration.")
            self.root.destroy()
            return
        
        # Initialize variables
        self.init_variables()
        self.selected_item = None
        
        # Create GUI components
        self.create_title()
        self.create_frames()
        self.create_input_fields()
        self.create_search_frame()
        self.create_buttons()
        self.create_table()
        self.create_status_bar()
        
        # Load initial data
        self.fetch_data()
        
        # Bind resize event for responsive design
        self.root.bind('<Configure>', self.on_resize)

    def init_variables(self):
        self.NameofTablets = tk.StringVar()
        self.ref = tk.StringVar()
        self.Dose = tk.StringVar()
        self.NumberofTablets = tk.StringVar()
        self.Lot = tk.StringVar()
        self.IssueDate = tk.StringVar()
        self.ExpDate = tk.StringVar()
        self.DailyDose = tk.StringVar()
        self.sideEffects = tk.StringVar()
        self.FurtherInformation = tk.StringVar()
        self.StorageAdvice = tk.StringVar()
        self.DrivingUsingMachine = tk.StringVar()
        self.HowToUseMedication = tk.StringVar()
        self.PatientId = tk.StringVar()
        self.nhsNumber = tk.StringVar()
        self.PatientName = tk.StringVar()
        self.DateOfBirth = tk.StringVar()
        self.PatientAddress = tk.StringVar()
        self.search_var = tk.StringVar()

    def on_resize(self, event):
        """Handle window resize for responsive design"""
        if event.widget == self.root:
            # Update screen dimensions
            self.screen_width = event.width
            self.screen_height = event.height
            
            # Adjust font sizes based on screen size
            self.adjust_font_sizes()
            
            # Adjust column widths for table
            self.adjust_table_columns()

    def adjust_font_sizes(self):
        """Adjust font sizes based on screen size"""
        if self.screen_width < 1400:
            # Smaller screens
            title_font = ("Segoe UI", 20, "bold")
            subtitle_font = ("Segoe UI", 10)
            header_font = ("Segoe UI", 12, "bold")
            body_font = ("Segoe UI", 9)
            button_font = ("Segoe UI", 9)
        elif self.screen_width < 1800:
            # Medium screens
            title_font = ("Segoe UI", 24, "bold")
            subtitle_font = ("Segoe UI", 12)
            header_font = ("Segoe UI", 14, "bold")
            body_font = ("Segoe UI", 10)
            button_font = ("Segoe UI", 10)
        else:
            # Large screens
            title_font = ("Segoe UI", 28, "bold")
            subtitle_font = ("Segoe UI", 14)
            header_font = ("Segoe UI", 16, "bold")
            body_font = ("Segoe UI", 11)
            button_font = ("Segoe UI", 11)
        
        # Update fonts if widgets exist
        if hasattr(self, 'title_label'):
            self.title_label.configure(font=title_font)
        if hasattr(self, 'subtitle_label'):
            self.subtitle_label.configure(font=subtitle_font)

    def adjust_table_columns(self):
        """Adjust table column widths based on screen size"""
        if hasattr(self, 'hospital_table'):
            # Calculate column width based on screen size
            base_width = max(100, self.screen_width // 15)
            
            columns = ["nameoftablets", "ref", "dose", "nooftablets", "lot", "issuedate",
                      "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"]
            
            for col in columns:
                self.hospital_table.column(col, width=base_width, minwidth=80)

    def create_title(self):
        # Main title frame with gradient effect
        title_frame = tk.Frame(self.root, bg='#1e3a8a', height=self.screen_height//10)
        title_frame.pack(side=tk.TOP, fill=tk.X)
        title_frame.pack_propagate(False)
        
        # Title with responsive styling
        self.title_label = tk.Label(title_frame, text="HOSPITAL MANAGEMENT SYSTEM",
                                   fg="white", bg="#1e3a8a", 
                                   font=("Segoe UI", 28, "bold"))
        self.title_label.pack(expand=True)
        
        # Subtitle
        self.subtitle_label = tk.Label(title_frame, text="Patient Care & Prescription Management System",
                                      fg="#e5e7eb", bg="#1e3a8a",
                                      font=("Segoe UI", 14))
        self.subtitle_label.pack()

    def create_frames(self):
        # Main container with responsive padding
        padding = min(25, self.screen_width // 60)
        main_container = tk.Frame(self.root, bg='#f8f9fa')
        main_container.pack(fill=tk.BOTH, expand=True, padx=padding, pady=padding)
        
        # Top frames container
        top_frames = tk.Frame(main_container, bg='#f8f9fa')
        top_frames.pack(fill=tk.X, pady=(0, padding))
        
        # Left frame - Patient Information
        self.DataframeLeft = tk.LabelFrame(top_frames, text="Patient Information", 
                                         font=("Segoe UI", 16, "bold"),
                                         bg='white', fg='#1e3a8a',
                                         relief=tk.FLAT, bd=2)
        self.DataframeLeft.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, padding//2))

        # Right frame - Prescription
        self.DataframeRight = tk.LabelFrame(top_frames, text="Prescription Details", 
                                          font=("Segoe UI", 16, "bold"),
                                          bg='white', fg='#1e3a8a',
                                          relief=tk.FLAT, bd=2)
        self.DataframeRight.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(padding//2, 0))

        # Button frame
        self.Buttonframe = tk.Frame(main_container, bg='#f8f9fa')
        self.Buttonframe.pack(fill=tk.X, pady=(0, padding))

        # Search frame
        self.Searchframe = tk.LabelFrame(main_container, text="Search & Filter", 
                                       font=("Segoe UI", 14, "bold"),
                                       bg='white', fg='#1e3a8a',
                                       relief=tk.FLAT, bd=2)
        self.Searchframe.pack(fill=tk.X, pady=(0, padding))

        # Table frame
        self.Detailsframe = tk.LabelFrame(main_container, text="Patient Records", 
                                        font=("Segoe UI", 16, "bold"),
                                        bg='white', fg='#1e3a8a',
                                        relief=tk.FLAT, bd=2)
        self.Detailsframe.pack(fill=tk.BOTH, expand=True)

    def create_input_fields(self):
        # Left frame inputs
        self.create_left_frame_inputs()
        
        # Right frame prescription text
        padding = min(20, self.screen_width // 80)
        prescription_frame = tk.Frame(self.DataframeRight, bg='white')
        prescription_frame.pack(fill=tk.BOTH, expand=True, padx=padding, pady=padding)
        
        # Add a label for the prescription
        prescription_label = tk.Label(prescription_frame, text="Generated Prescription:",
                                    font=("Segoe UI", 12, "bold"),
                                    bg='white', fg='#1e3a8a')
        prescription_label.pack(anchor='w', pady=(0, 10))
        
        self.txtPrescription = tk.Text(prescription_frame, 
                                     font=("Consolas", 11),
                                     bg='#f8f9fa', fg='#1e3a8a',
                                     relief=tk.FLAT, bd=1,
                                     padx=15, pady=15)
        self.txtPrescription.pack(fill=tk.BOTH, expand=True)

    def create_left_frame_inputs(self):
        # Create scrollable frame for inputs
        canvas = tk.Canvas(self.DataframeLeft, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.DataframeLeft, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create all input fields with responsive sizing
        fields = [
            ("Name Of Tablets", self.NameofTablets, 0, 0, True),
            ("Reference No", self.ref, 1, 0, False),
            ("Dose", self.Dose, 2, 0, False),
            ("No Of Tablets", self.NumberofTablets, 3, 0, False),
            ("Lot", self.Lot, 4, 0, False),
            ("Issue Date", self.IssueDate, 5, 0, False),
            ("Exp Date", self.ExpDate, 6, 0, False),
            ("Daily Dose", self.DailyDose, 7, 0, False),
            ("Side Effect", self.sideEffects, 8, 0, False),
            ("Further Information", self.FurtherInformation, 0, 2, False),
            ("Blood Pressure", self.DrivingUsingMachine, 1, 2, False),
            ("Storage Advice", self.StorageAdvice, 2, 2, False),
            ("Medication", self.HowToUseMedication, 3, 2, False),
            ("Patient Id", self.PatientId, 4, 2, False),
            ("NHS Number", self.nhsNumber, 5, 2, False),
            ("Patient Name", self.PatientName, 6, 2, False),
            ("Date Of Birth", self.DateOfBirth, 7, 2, False),
            ("Patient Address", self.PatientAddress, 8, 2, False)
        ]

        # Responsive padding and sizing
        field_padding = min(20, self.screen_width // 80)
        field_pady = min(10, self.screen_height // 100)
        
        for label_text, var, row, col, is_combobox in fields:
            # Create frame for each field
            field_frame = tk.Frame(scrollable_frame, bg='white')
            field_frame.grid(row=row, column=col, sticky='ew', padx=field_padding, pady=field_pady)
            
            # Label with responsive styling
            label = tk.Label(field_frame, text=label_text,
                           font=("Segoe UI", 12, "bold"),
                           bg='white', fg='#1e3a8a',
                           anchor='w')
            label.pack(anchor='w', pady=(0, 8))

            if is_combobox:
                combo = ttk.Combobox(field_frame, textvariable=var, state="readonly",
                                   font=("Segoe UI", 11), width=32)
                combo["values"] = ("Nice", "Corona Vaccine", "Acetaminophen", "Adderall", 
                                 "Amlodipine", "Ativan", "Ibuprofen", "Aspirin", "Paracetamol")
                combo.current(0)
                combo.pack(fill='x')
            else:
                entry = tk.Entry(field_frame, font=("Segoe UI", 11),
                               textvariable=var, relief=tk.FLAT, bd=1,
                               bg='#f8f9fa', fg='#1e3a8a',
                               insertbackground='#3b82f6')
                entry.pack(fill='x', ipady=10)
                
                # Add focus effects
                entry.bind('<FocusIn>', lambda e, ent=entry: self.on_entry_focus_in(ent))
                entry.bind('<FocusOut>', lambda e, ent=entry: self.on_entry_focus_out(ent))

        # Configure grid weights
        scrollable_frame.grid_columnconfigure(0, weight=1)
        scrollable_frame.grid_columnconfigure(2, weight=1)

        # Pack canvas and scrollbar with responsive padding
        canvas.pack(side="left", fill="both", expand=True, padx=field_padding, pady=field_padding)
        scrollbar.pack(side="right", fill="y")

    def create_search_frame(self):
        padding = min(20, self.screen_width // 80)
        search_container = tk.Frame(self.Searchframe, bg='white')
        search_container.pack(fill=tk.X, padx=padding, pady=padding)
        
        # Search label
        search_label = tk.Label(search_container, text="Search Patient:",
                              font=("Segoe UI", 12, "bold"),
                              bg='white', fg='#1e3a8a')
        search_label.pack(side=tk.LEFT, padx=(0, 10))
        
        # Search entry with responsive width
        search_width = min(30, self.screen_width // 50)
        search_entry = tk.Entry(search_container, textvariable=self.search_var,
                              font=("Segoe UI", 11),
                              relief=tk.FLAT, bd=1,
                              bg='#f8f9fa', fg='#1e3a8a',
                              width=search_width)
        search_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        # Search button
        search_btn = ttk.Button(search_container, text="Search",
                              command=self.search_records,
                              style="primary.TButton")
        search_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear search button
        clear_search_btn = ttk.Button(search_container, text="Clear Search",
                                    command=self.clear_search,
                                    style="secondary.TButton")
        clear_search_btn.pack(side=tk.LEFT)
        
        # Bind search to Enter key
        search_entry.bind('<Return>', lambda e: self.search_records())

    def on_entry_focus_in(self, entry):
        entry.configure(bg='white', relief=tk.SOLID, bd=1)

    def on_entry_focus_out(self, entry):
        entry.configure(bg='#f8f9fa', relief=tk.FLAT, bd=1)

    def create_buttons(self):
        # Button container with responsive styling
        button_container = tk.Frame(self.Buttonframe, bg='#f8f9fa')
        button_container.pack(expand=True)
        
        buttons = [
            ("Generate Prescription", self.iprescription, "success"),
            ("Save New Record", self.iprescriptionData, "primary"),
            ("Update Record", self.update, "warning"),
            ("Delete Record", self.idelete, "danger"),
            ("Clear All Fields", self.clear, "secondary"),
            ("Exit Application", self.iExit, "dark")
        ]

        # Responsive button width
        button_width = min(18, self.screen_width // 100)
        button_padding = min(8, self.screen_width // 200)

        for i, (text, command, style) in enumerate(buttons):
            btn = ttk.Button(button_container, text=text, command=command,
                           style=f"{style}.TButton", width=button_width)
            btn.pack(side=tk.LEFT, padx=button_padding)

    def create_table(self):
        # Table container with responsive padding
        padding = min(20, self.screen_width // 80)
        table_container = tk.Frame(self.Detailsframe, bg='white')
        table_container.pack(fill=tk.BOTH, expand=True, padx=padding, pady=padding)
        
        # Create scrollbars
        scroll_x = ttk.Scrollbar(table_container, orient=tk.HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_container, orient=tk.VERTICAL)

        # Create treeview with responsive height
        table_height = max(8, self.screen_height // 80)
        self.hospital_table = ttk.Treeview(table_container, 
            columns=("nameoftablets", "ref", "dose", "nooftablets", "lot", "issuedate",
                    "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"),
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set,
            show="headings", height=table_height)

        # Configure scrollbars
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        # Configure columns with responsive headers
        columns = [
            ("nameoftablets", "Medication"),
            ("ref", "Reference"),
            ("dose", "Dose"),
            ("nooftablets", "Quantity"),
            ("lot", "Lot"),
            ("issuedate", "Issue Date"),
            ("expdate", "Exp Date"),
            ("dailydose", "Daily Dose"),
            ("storage", "Storage"),
            ("nhsnumber", "NHS Number"),
            ("pname", "Patient Name"),
            ("dob", "DOB"),
            ("address", "Address")
        ]

        # Responsive column width
        base_width = max(100, self.screen_width // 15)
        for col, heading in columns:
            self.hospital_table.heading(col, text=heading)
            self.hospital_table.column(col, width=base_width, minwidth=80)

        self.hospital_table.pack(fill=tk.BOTH, expand=True)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        
        # Add selection styling
        self.hospital_table.tag_configure('selected', background='#3b82f6', foreground='white')

    def create_status_bar(self):
        # Status bar with responsive font
        status_font = ("Segoe UI", max(8, self.screen_height // 120))
        self.status_bar = tk.Label(self.root, text="Ready", 
                                 relief=tk.SUNKEN, anchor=tk.W,
                                 bg='#1e3a8a', fg='white',
                                 font=status_font)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def search_records(self):
        search_term = self.search_var.get().lower()
        if not search_term:
            self.fetch_data()
            return
            
        rows = self.db.fetch_all_patients()
        if rows is not None:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for row in rows:
                # Search in patient name, medication, and reference
                if (search_term in str(row[10]).lower() or  # Patient name
                    search_term in str(row[0]).lower() or   # Medication
                    search_term in str(row[1]).lower()):    # Reference
                    self.hospital_table.insert("", tk.END, values=row)
            
            self.status_bar.config(text=f"Found {len(self.hospital_table.get_children())} matching records")

    def clear_search(self):
        self.search_var.set("")
        self.fetch_data()
        self.status_bar.config(text="Ready")

    def iprescriptionData(self):
        required_fields = {
            "Name of Tablets": self.NameofTablets,
            "Reference No": self.ref
        }
        
        if not validate_required_fields(required_fields):
            return

        data = (
            self.NameofTablets.get(),
            self.ref.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get()
        )

        if self.db.insert_patient(data):
            self.fetch_data()
            self.status_bar.config(text="Record saved successfully")
            messagebox.showinfo("Success", "Record has been saved successfully!")

    def update(self):
        if not self.selected_item:
            messagebox.showwarning("Warning", "Please select a record to update")
            return
            
        data = (
            self.NameofTablets.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
            self.ref.get()
        )

        if self.db.update_patient(data):
            self.fetch_data()
            self.status_bar.config(text="Record updated successfully")
            messagebox.showinfo("Success", "Record has been updated successfully!")

    def fetch_data(self):
        rows = self.db.fetch_all_patients()
        if rows is not None:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for row in rows:
                self.hospital_table.insert("", tk.END, values=row)
            
            self.status_bar.config(text=f"Loaded {len(rows)} records")

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        
        if row:
            self.selected_item = cursor_row
            self.NameofTablets.set(row[0])
            self.ref.set(row[1])
            self.Dose.set(row[2])
            self.NumberofTablets.set(row[3])
            self.Lot.set(row[4])
            self.IssueDate.set(row[5])
            self.ExpDate.set(row[6])
            self.DailyDose.set(row[7])
            self.StorageAdvice.set(row[8])
            self.nhsNumber.set(row[9])
            self.PatientName.set(row[10])
            self.DateOfBirth.set(row[11])
            self.PatientAddress.set(row[12])
            
            self.status_bar.config(text=f"Selected: {row[10]} - {row[0]}")

    def iprescription(self):
        data = {
            'NameofTablets': self.NameofTablets.get(),
            'ref': self.ref.get(),
            'Dose': self.Dose.get(),
            'NumberofTablets': self.NumberofTablets.get(),
            'Lot': self.Lot.get(),
            'IssueDate': self.IssueDate.get(),
            'ExpDate': self.ExpDate.get(),
            'DailyDose': self.DailyDose.get(),
            'sideEffects': self.sideEffects.get(),
            'FurtherInformation': self.FurtherInformation.get(),
            'StorageAdvice': self.StorageAdvice.get(),
            'DrivingUsingMachine': self.DrivingUsingMachine.get(),
            'PatientId': self.PatientId.get(),
            'nhsNumber': self.nhsNumber.get(),
            'PatientName': self.PatientName.get(),
            'DateOfBirth': self.DateOfBirth.get(),
            'PatientAddress': self.PatientAddress.get()
        }
        
        self.txtPrescription.delete("1.0", tk.END)
        self.txtPrescription.insert(tk.END, format_prescription(data))
        self.status_bar.config(text="Prescription generated")

    def idelete(self):
        if not self.selected_item:
            messagebox.showwarning("Warning", "Please select a record to delete")
            return
            
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?"):
            if self.db.delete_patient(self.ref.get()):
                self.fetch_data()
                self.selected_item = None
                self.status_bar.config(text="Record deleted successfully")
                messagebox.showinfo("Success", "Record has been deleted successfully!")

    def clear(self):
        fields = {
            'NameofTablets': self.NameofTablets,
            'ref': self.ref,
            'Dose': self.Dose,
            'NumberofTablets': self.NumberofTablets,
            'Lot': self.Lot,
            'IssueDate': self.IssueDate,
            'ExpDate': self.ExpDate,
            'DailyDose': self.DailyDose,
            'sideEffects': self.sideEffects,
            'FurtherInformation': self.FurtherInformation,
            'StorageAdvice': self.StorageAdvice,
            'DrivingUsingMachine': self.DrivingUsingMachine,
            'HowToUseMedication': self.HowToUseMedication,
            'PatientId': self.PatientId,
            'nhsNumber': self.nhsNumber,
            'PatientName': self.PatientName,
            'DateOfBirth': self.DateOfBirth,
            'PatientAddress': self.PatientAddress
        }
        
        clear_fields(fields)
        self.txtPrescription.delete("1.0", tk.END)
        self.selected_item = None
        self.status_bar.config(text="Fields cleared")

    def iExit(self):
        if messagebox.askyesno("Hospital Management System", "Are you sure you want to exit?"):
            self.db.close()
            self.root.destroy()

if __name__ == "__main__":
    root = ttk.Window()
    app = Hospital(root)
    root.mainloop() 