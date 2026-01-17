# 🐍 Syntecxhub Python Task 3 — Internship Projects

This repository contains the solutions for **Syntecxhub Python Programming Task 3**, completed as part of the internship program.

---

## 📦 **Projects Included**

### ✅ **Project 1: CSV → Excel Converter**
**Features**
- Reads `.csv` file
- Cleans missing values
- Normalizes column names
- Exports to `.xlsx`
- CLI input/output support
- Logging & Error handling

**Run Command**
```bash
python csv_to_excel.py --input input.csv --output output.xlsx
```

---

### ✅ **Project 2: Web Scraper for Headlines**
**Features**
- Scrapes news headlines from websites
- Extracts: Title, URL, Timestamp
- Saves to JSON + CSV
- Optional keyword filter
- Request delays for robots.txt compliance

**Outputs**
- `headlines.json`
- `headlines.csv`

**Example Use**
```bash
python news_scraper.py
```

---

### ✅ **Project 3: Email Sender Bot**
**Features**
- Sends automated emails
- Reads recipients from CSV
- Supports attachments
- Personalized messages
- Gmail SMTP support
- Retry & Logging system

**Usage**
1. Enable Gmail App Passwords
2. Update script credentials
3. Add `recipients.csv` with:

```
name,email
John Doe,johndoe@gmail.com
```

**Run**
```bash
python email_sende_
