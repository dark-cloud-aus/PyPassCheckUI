"""
  #____________   ____ _____    ________ _______  |  |   ___________    ______ ______   ____ |  |__   ____   ____ |  | __
 #/  _ \___   / _/ ___\\__  \  /  ___/  |  \__  \ |  |   \____ \__  \  /  ___//  ___/ _/ ___\|  |  \_/ __ \_/ ___\|  |/ /
#(  <_> )    /  \  \___ / __ \_\___ \|  |  // __ \|  |__ |  |_> > __ \_\___ \ \___ \  \  \___|   Y  \  ___/\  \___|    <
 #\____/_____ \  \___  >____  /____  >____/(____  /____/ |   __(____  /____  >____  >  \___  >___|  /\___  >\___  >__|_ \
  #          \/      \/     \/     \/           \/       |__|       \/     \/     \/       \/     \/     \/     \/     \
"""

import re
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

# check the password strength locally on the machine
def check_password_strength(password):
    if len(password) < 10:
        return False, "Password must be at least 10 characters long."

    numbers = sum(c.isdigit() for c in password)
    if numbers < 2:
        return False, "Password must contain at least 2 numbers."

    # heck for at least two unique special characters
    special_chars = set(re.findall(r"[^a-zA-Z0-9]", password))
    if len(special_chars) < 2:
        return False, "Password must contain at least 2 different special characters."

    return True, "Password strength is good."

# Function to be called when the "Check Password" button is pressed
def on_submit():
    password = password_entry.get()
    is_strong, message = check_password_strength(password)
    messagebox.showinfo("Password Check", message)
    if is_strong:
        pass

# basic programme window
root = Tk()
root.title("OzCazual Password Strength Checker")

password_label = Label(root, text="Enter your OzCazual password:")
password_label.pack()

password_var = StringVar()
password_entry = Entry(root, textvariable=password_var, show="*")
password_entry.pack()

submit_button = Button(root, text="Check Password", command=on_submit)
submit_button.pack()

root.mainloop()



if __name__ == '__main__':
    print_hi('PyCharm')

# Script written with PyCharm
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
