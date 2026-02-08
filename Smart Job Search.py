# import tkinter as tk
# from tkinter import messagebox
# import webbrowser
# import urllib.parse
#
# # -------------------------
# # Job Search Logic Microsoft Edge
# # -------------------------
# def search_jobs():
#     keyword = keyword_entry.get().strip()
#     location = location_entry.get().strip()
#
#     if not keyword:
#         messagebox.showwarning("Input Error", "Please enter job keywords")
#         return
#
#     # Encode query safely
#     query = f"{keyword} jobs {location}"
#     encoded_query = urllib.parse.quote(query)
#
#     # Google Job Search URL
#     job_url = f"https://www.google.com/search?q={encoded_query}&ibp=htl;jobs"
#
#     result_box.delete(1.0, tk.END)
#     result_box.insert(tk.END, "🔍 Job Search Link Generated:\n\n")
#     result_box.insert(tk.END, job_url)
#
#     # Open browser automatically
#     webbrowser.open(job_url)
#
#
# # -------------------------
# # UI Setup
# # -------------------------
# root = tk.Tk()
# root.title("Smart Job Search Agent")
# root.geometry("600x400")
# root.resizable(False, False)
#
# # Header
# header = tk.Label(
#     root,
#     text="Smart Job Search Agent",
#     font=("Arial", 18, "bold")
# )
# header.pack(pady=10)
#
# # Keyword Input
# tk.Label(root, text="Job Keywords", font=("Arial", 12)).pack()
# keyword_entry = tk.Entry(root, width=50, font=("Arial", 11))
# keyword_entry.pack(pady=5)
#
# # Location Input
# tk.Label(root, text="Location (City, Country)", font=("Arial", 12)).pack()
# location_entry = tk.Entry(root, width=50, font=("Arial", 11))
# location_entry.pack(pady=5)
#
# # Search Button
# search_btn = tk.Button(
#     root,
#     text="Search Jobs",
#     font=("Arial", 12),
#     bg="#2563eb",
#     fg="white",
#     width=20,
#     command=search_jobs
# )
# search_btn.pack(pady=15)
#
# # Results Box
# result_box = tk.Text(root, height=6, width=70, font=("Arial", 10))
# result_box.pack(pady=10)
#
# # Footer
# footer = tk.Label(
#     root,
#     text="Powered by AI Job Intelligence",
#     font=("Arial", 9),
#     fg="gray"
# )
# footer.pack()
#
# root.mainloop()

"""
-------------------------------------------------------
Project Name   : Smart Job Search Agent
Description    : Desktop-based job discovery application
                 with popup UI and Google Jobs integration
Technology     : Python, Tkinter, Web Automation
Platform       : Windows

Developer Name : Kajal Dadas
Contact Number : +91 7972244559
Email ID       : kajaldadas149@gmail.com

Version        : 1.0.0
Last Updated   : 2026
-------------------------------------------------------
"""

import tkinter as tk
from tkinter import messagebox
import webbrowser
import urllib.parse
import os

# -------------------------
# Force Chrome Browser
# -------------------------
def open_in_chrome(url):
    chrome_paths = [
        "C:/Program Files/Google/Chrome/Application/chrome.exe",
        "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    ]

    for path in chrome_paths:
        if os.path.exists(path):
            webbrowser.register(
                "chrome",
                None,
                webbrowser.BackgroundBrowser(path)
            )
            webbrowser.get("chrome").open(url)
            return

    # Fallback
    webbrowser.open(url)


# -------------------------
# Job Search Logic
# -------------------------
def search_jobs():
    keyword = keyword_entry.get().strip()
    location = location_entry.get().strip()

    if not keyword:
        messagebox.showwarning("Input Required", "Please enter job keywords")
        return

    query = f"{keyword} jobs {location}"
    encoded_query = urllib.parse.quote(query)

    job_url = f"https://www.google.com/search?q={encoded_query}&ibp=htl;jobs"

    result_box.config(state="normal")
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, "✅ Job Search Link Generated\n\n")
    result_box.insert(tk.END, job_url)
    result_box.config(state="disabled")

    open_in_chrome(job_url)


# -------------------------
# UI Setup
# -------------------------
root = tk.Tk()
root.title("Smart Job Search Agent")
root.geometry("640x420")
root.resizable(False, False)
root.configure(bg="#f8fafc")

# Header
header = tk.Label(
    root,
    text="Smart Job Search Agent",
    font=("Segoe UI", 20, "bold"),
    bg="#f8fafc",
    fg="#0f172a"
)
header.pack(pady=(15, 5))

sub_header = tk.Label(
    root,
    text="Developed by Kajal Dadas",
    font=("Segoe UI", 10, "italic"),
    bg="#f8fafc",
    fg="#475569"
)
sub_header.pack(pady=(0, 20))

# Keyword Input
tk.Label(
    root,
    text="Job Keywords",
    font=("Segoe UI", 12),
    bg="#f8fafc"
).pack()

keyword_entry = tk.Entry(
    root,
    width=45,
    font=("Segoe UI", 11),
    relief="solid",
    bd=1
)
keyword_entry.pack(pady=6)

# Location Input
tk.Label(
    root,
    text="Location (City / Country)",
    font=("Segoe UI", 12),
    bg="#f8fafc"
).pack()

location_entry = tk.Entry(
    root,
    width=45,
    font=("Segoe UI", 11),
    relief="solid",
    bd=1
)
location_entry.pack(pady=6)

# Search Button
search_btn = tk.Button(
    root,
    text="Search Jobs",
    font=("Segoe UI", 12, "bold"),
    bg="#2563eb",
    fg="white",
    width=18,
    cursor="hand2",
    command=search_jobs
)
search_btn.pack(pady=18)

# Result Box
result_box = tk.Text(
    root,
    height=5,
    width=72,
    font=("Segoe UI", 10),
    wrap="word",
    relief="solid",
    bd=1
)
result_box.pack(pady=10)
result_box.config(state="disabled")

# Footer
footer = tk.Label(
    root,
    text="AI-powered Job Discovery • Google Jobs Intelligence",
    font=("Segoe UI", 9),
    bg="#f8fafc",
    fg="#64748b"
)
footer.pack(pady=5)

root.mainloop()
