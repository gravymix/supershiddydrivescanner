import os
import subprocess
import tkinter as tk
from tkinter import messagebox, filedialog

def scan_drive():
    # Define the path to scan
    path = "C:\\"

    # Run the built-in Windows command to check for file system errors
    result = subprocess.run(["chkdsk", path], stdout=subprocess.PIPE)

    # Check the output for any errors
    output = result.stdout.decode("utf-8")
    if "errors" in output:
        messagebox.showwarning("Scan Results", "There are file system errors on drive C.")
    else:
        messagebox.showinfo("Scan Results", "No errors were found on drive C.")

    # Write the results to a text file
    desktop_path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
    filename = filedialog.asksaveasfilename(initialdir=desktop_path, title="Save Scan Results", filetypes=(("Text Files", "*.txt"),))
    if filename:
        with open(filename, "w") as f:
            f.write(output)

    # Update the status bar
    status_bar.config(text="Scan complete.")

# Create the main window
root = tk.Tk()
root.title("Simple Shitty Drive Scanner")
root.geometry("300x150")

# Create the button to scan the drive
scan_button = tk.Button(root, text="Scan Drive", command=scan_drive)
scan_button.pack(pady=20)

# Create the button to open the GitHub page
def open_github():
    os.system("start https://github.com/gravymix")
github_button = tk.Button(root, text="My GitHub", command=open_github)
github_button.pack()

# Create the status bar
status_bar = tk.Label(root, text="Ready.")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Start the main event loop
root.mainloop()
