# 🏥 Hospital Management System

A modern, responsive Hospital Management System built with Python and Tkinter, featuring a beautiful UI with fullscreen support and cross-platform compatibility.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-green.svg)
![ttkbootstrap](https://img.shields.io/badge/ttkbootstrap-UI%20Framework-purple.svg)

## 👨‍💻 **Developer**

**Aakash Sapkota**  
🎓 Bachelor in Cyber Security and Cloud Computing  
🌐 [aakashsapkota.in.net](https://aakashsapkota.in.net)

---

## ✨ **Features**

### 🖥️ **Modern UI/UX**
- **Responsive Design**: Adapts to any screen size
- **Fullscreen Mode**: Always opens in fullscreen with ESC toggle
- **Professional Styling**: Modern blue theme with ttkbootstrap
- **Cross-Platform**: Works on Windows, macOS, and Linux

### 📊 **Core Functionality**
- **Patient Management**: Add, edit, delete, and view patient records
- **Prescription System**: Generate professional prescriptions
- **Search & Filter**: Quick search by patient name, medication, or reference
- **Data Validation**: Input validation and error handling
- **Real-time Status**: Status bar with live feedback

### 🔧 **Technical Features**
- **SQLite Database**: Lightweight and efficient data storage
- **Responsive Layout**: Dynamic sizing based on screen resolution
- **Keyboard Shortcuts**: ESC for fullscreen, Enter for search
- **Scrollable Interface**: Handles large datasets efficiently

---

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.8 or higher
- pip package manager

### **Installation**

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hospital-management-system.git
   cd hospital-management-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

---

## 🎯 **Usage Guide**

### **Starting the Application**
- Application automatically opens in fullscreen mode
- Press `ESC` to toggle between fullscreen and windowed mode
- All elements automatically adjust to your screen size

### **Managing Patients**
1. **Add New Patient**: Fill in the form and click "Save New Record"
2. **Edit Patient**: Select a record from the table, modify fields, click "Update Record"
3. **Delete Patient**: Select a record and click "Delete Record"
4. **Search**: Use the search bar to find patients quickly

### **Generating Prescriptions**
1. Fill in patient and medication details
2. Click "Generate Prescription" to create a professional prescription
3. Prescription appears in the right panel

---

## 📁 **Project Structure**

```
hospital-management-system/
├── main.py              # Main application file
├── db.py                # Database operations
├── utils.py             # Utility functions
├── requirements.txt     # Python dependencies
├── setup_database.sql   # Database schema
├── hospital.db          # SQLite database file
└── README.md           # This file
```

---

## 🛠️ **Technology Stack**

| Component | Technology | Purpose |
|-----------|------------|---------|
| **GUI Framework** | Tkinter + ttkbootstrap | Modern, responsive interface |
| **Database** | SQLite | Lightweight data storage |
| **Language** | Python 3.8+ | Backend logic and data processing |
| **Styling** | ttkbootstrap | Professional UI components |

---

## 🎨 **UI Features**

### **Responsive Design**
- **Small Screens** (< 1400px): Compact layout with smaller fonts
- **Medium Screens** (1400px-1800px): Balanced sizing
- **Large Screens** (> 1800px): Spacious layout with larger fonts

### **Color Scheme**
- **Primary**: Professional blue (`#1e3a8a`)
- **Background**: Light gray (`#f8f9fa`)
- **Text**: Dark gray for readability
- **Accents**: Blue highlights and focus effects

### **Interactive Elements**
- **Focus Effects**: Entry fields highlight when selected
- **Hover States**: Buttons and interactive elements respond to mouse
- **Status Feedback**: Real-time status updates in bottom bar

---

## 🔧 **Configuration**

### **Database Setup**
The application uses SQLite by default. The database file (`hospital.db`) is created automatically on first run.

### **Customization**
- Modify colors in `main.py` by changing the color variables
- Adjust responsive breakpoints in the `adjust_font_sizes()` method
- Customize database schema in `setup_database.sql`

---

## 📊 **Screenshots**

*[Screenshots will be added here]*

---

## 🎮 **Keyboard Shortcuts**

| Key | Function |
|-----|----------|
| `ESC` | Toggle fullscreen mode |
| `Enter` | Search (when in search box) |
| `Tab` | Navigate between fields |

---

## 🔒 **Security Features**

- **Input Validation**: All user inputs are validated
- **SQL Injection Protection**: Parameterized queries
- **Data Integrity**: Database constraints and validation
- **Error Handling**: Graceful error management

---

## 🚀 **Performance**

- **Fast Loading**: Optimized database queries
- **Memory Efficient**: Minimal resource usage
- **Responsive**: Real-time UI updates
- **Scalable**: Handles large datasets efficiently

---

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 **Contact**

**Aakash Sapkota**  
- 🌐 Website: [aakashsapkota.in.net](https://aakashsapkota.in.net)
- 📧 Email: [your-email@example.com]
- 💼 LinkedIn: [Your LinkedIn]
- 🐦 Twitter: [@YourTwitter]

---

## 🙏 **Acknowledgments**

- **ttkbootstrap**: For the beautiful UI components
- **Python Community**: For excellent documentation and support
- **Open Source Contributors**: For inspiration and best practices

---

<div align="center">

**Made with ❤️ by Aakash Sapkota**

*Bachelor in Cyber Security and Cloud Computing*

[![Website](https://img.shields.io/badge/Website-aakashsapkota.in.net-blue)](https://aakashsapkota.in.net)

</div>
