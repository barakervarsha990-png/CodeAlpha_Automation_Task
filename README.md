# 🧠 Task Automation using Python

## 📌 Project Overview

This project is a simple yet powerful **Python-based automation tool** designed to perform common repetitive tasks automatically. It helps reduce manual effort and improves productivity by handling tasks like file organization, data extraction, and web scraping.

---

## 🎯 Objective

The main objective of this project is to demonstrate how Python can be used to **automate real-world tasks efficiently** using built-in and external libraries.

---

## ⚙️ Features

* 📂 Move `.jpg` files from one folder to another
* 📧 Extract email addresses from a text file
* 🌐 Scrape and display the title of a website
* 🧩 Menu-driven interface for easy use

---

## 🛠️ Technologies Used

* Python
* OS Module
* Shutil Module
* Regular Expressions (`re`)
* Requests Library
* BeautifulSoup (bs4)

---

## 📁 Project Structure

```
automation_project/
│
├── automation.py
├── input.txt        # (for email extraction)
├── emails.txt       # (output file)
├── source_images/   # (input folder for images)
└── moved_images/    # (output folder)
```

---

## 🚀 Installation & Setup

### 1️⃣ Install Python

Download and install Python from: https://www.python.org
Make sure to enable **"Add Python to PATH"** during installation.

---

### 2️⃣ Install Required Libraries

Open terminal / command prompt and run:

```
pip install requests beautifulsoup4
```

---

### 3️⃣ Run the Program

Navigate to your project folder and run:

```
python automation.py
```

---

## ▶️ Usage Instructions

After running the program, you will see:

```
--- Task Automation Menu ---
1. Move JPG files
2. Extract Emails from file
3. Scrape Website Title
4. Exit
```

### 🔹 Option 1: Move JPG Files

* Enter source folder path
* Enter destination folder path
* All `.jpg` files will be moved automatically

---

### 🔹 Option 2: Extract Emails

* Provide input file (e.g., `input.txt`)
* Emails will be saved in `emails.txt`

---

### 🔹 Option 3: Scrape Website Title

* Enter website URL (e.g., https://www.google.com)
* Program will display the webpage title

---

## 🧪 Example Outputs

### ✔️ File Moving

```
3 JPG files moved successfully!
```

### ✔️ Email Extraction

```
2 emails extracted successfully!
```

### ✔️ Web Scraping

```
Website Title: Google
```

---

## ⚠️ Common Errors & Fixes

* **pip not recognized**

  ```
  python -m pip install requests beautifulsoup4
  ```

* **Invalid URL**
  → Use full URL with `https://`

* **File not found**
  → Check file name and location

---

## 🌟 Future Enhancements

* Add GUI interface (Tkinter / Web UI)
* Store history of operations
* Detect malicious or spam URLs
* Add support for more file types

---

## 📚 Applications

* File management automation
* Data extraction
* Web data collection
* Beginner-level DevOps automation

---

## 🎤 Conclusion

This project demonstrates the practical use of Python in automating everyday tasks. It is simple, efficient, and can be extended into more advanced applications such as cybersecurity tools and intelligent automation systems.

---

## 👩‍💻 Author

**Varsha**

---

## 📌 License

This project is for educational purposes.
