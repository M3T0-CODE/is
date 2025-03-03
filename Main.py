import tkinter as tk
from tkinter import messagebox
import itertools
import string

CORRECT_PASSWORD = "abcde"

def dictionary_attack(username, dictionary):
    for word in dictionary:
        if word == CORRECT_PASSWORD:
            return True
    return False

def brute_force_attack():
    chars = string.ascii_letters
    for combo in itertools.product(chars, repeat=5):
        password = ''.join(combo)
        if password == CORRECT_PASSWORD:
            return password
    return None

def run_dictionary_attack():
    username = username_entry.get()
    if not username:
        messagebox.showerror("Error", "Please enter a username")
        return

    dictionary = ["hello", "world", "python", "apple", "password", "test"]

    if dictionary_attack(username, dictionary):
        messagebox.showinfo("Success", f"Dictionary Attack: Password found - {CORRECT_PASSWORD}")
    else:
        messagebox.showerror("Failure", "Password could not be cracked using Dictionary Attack")

def run_brute_force_attack():
    username = username_entry.get()
    if not username:
        messagebox.showerror("Error", "Please enter a username")
        return

    brute_password = brute_force_attack()
    if brute_password:
        messagebox.showinfo("Success", f"Brute Force Attack: Password found - {brute_password}")
    else:
        messagebox.showerror("Failure", "Password could not be cracked using Brute Force Attack")


root = tk.Tk()
root.title("Password Cracker")
root.geometry("400x300")

label = tk.Label(root, text="Enter Username:")
label.pack(pady=10)

username_entry = tk.Entry(root)
username_entry.pack(pady=5)

dictionary_button = tk.Button(root, text="Dictionary Attack", command=run_dictionary_attack)
dictionary_button.pack(pady=10)

brute_force_button = tk.Button(root, text="Brute Force Attack", command=run_brute_force_attack)
brute_force_button.pack(pady=10)

root.mainloop()