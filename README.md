
---

# Smart Job Search Agent (Python Desktop Application)

## Overview

The **Smart Job Search Agent** is a Python-based desktop application designed to simplify and accelerate job discovery. It provides a clean popup UI where users can enter job keywords and preferred locations, and instantly access live job postings via Google Jobs in the Chrome browser.

This solution avoids unstable scraping and instead leverages intelligent query redirection, ensuring **reliable, real-time, and scalable job search results**.

---

## Key Features

* Popup-based **desktop UI (Tkinter)**
* Keyword and location-driven job search
* Automatically opens results in **Google Chrome**
* Generates **live Google Jobs links**
* Clean, minimal, professional design
* Lightweight and fast execution
* Easily convertible to `.exe`

---

## Technology Stack

* **Language:** Python 3.10+
* **UI Framework:** Tkinter
* **Browser Automation:** webbrowser
* **Platform:** Windows

---

## Installation & Setup

### 1. Clone or Download

```bash
git clone <repository-url>
```

### 2. Install Dependencies

```bash
pip install requests beautifulsoup4
```

### 3. Run the Application

```bash
python "Smart Job Search.py"
```

---

## How It Works

1. User enters job keywords and location in the popup UI
2. Application generates an optimized Google Jobs search URL
3. Results open automatically in **Chrome**
4. User views and applies directly from trusted job sources

---

## Use Cases

* Job seekers looking for fast discovery
* Freshers and professionals exploring roles
* Recruiters sharing quick job discovery tools
* Portfolio project for AI / Python / Automation roles

---

## Future Scope

This project is designed with extensibility in mind. Potential enhancements include:

* AI-based job ranking using resume matching
* Resume upload and skill extraction
* Multi-source aggregation (LinkedIn, Indeed, Naukri)
* Job alerts and notifications
* Save jobs to CSV / Excel
* Fully autonomous job search agent
* Android APK and cross-platform support
* LLM-powered career recommendations

---

Absolutely — here’s a **clean, production-ready `requirements.txt`** aligned with your current implementation and future scalability.

---

## requirements.txt

```txt
python>=3.10
requests>=2.31.0
beautifulsoup4>=4.12.2
```

---

## Why these dependencies

* **python>=3.10**
  Ensures modern language features and long-term compatibility

* **requests**
  HTTP handling (future-ready for API integrations)

* **beautifulsoup4**
  HTML parsing (kept for extensibility, even if not heavily used now)

> Tkinter, webbrowser, urllib, and os are part of Python’s standard library and **do not** need to be added.

---

## Installation Command

```bash
pip install -r requirements.txt
```
---
## Developer Information

**Developer Name:** Kajal Dadas
**Contact Number:** +91 7972244559
**Email:** [kajaldadas149@gmail.com](mailto:kajaldadas149@gmail.com)

---

## License

This project is open for learning, portfolio, and personal use.
For commercial or enterprise usage, please contact the developer.

---

