import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

def move_jpg_files():
    source = input("Enter source folder path: ")
    destination = input("Enter destination folder path: ")

    os.makedirs(destination, exist_ok=True)

    moved = 0
    for file in os.listdir(source):
        if file.endswith(".jpg"):
            shutil.move(os.path.join(source, file),
                        os.path.join(destination, file))
            moved += 1

    print(f"{moved} JPG files moved successfully!")


def extract_emails():
    input_file = input("Enter input file name (e.g., input.txt): ")
    output_file = input("Enter output file name (e.g., emails.txt): ")

    with open(input_file, "r") as f:
        data = f.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", data)

    with open(output_file, "w") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"{len(emails)} emails extracted successfully!")


def scrape_title():
    url = input("Enter website URL: ")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "No title found"

        print("Website Title:", title)

    except Exception as e:
        print("Error:", e)


# 🔹 Main Menu
while True:
    print("\n--- Task Automation Menu ---")
    print("1. Move JPG files")
    print("2. Extract Emails from file")
    print("3. Scrape Website Title")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        move_jpg_files()
    elif choice == "2":
        extract_emails()
    elif choice == "3":
        scrape_title()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")