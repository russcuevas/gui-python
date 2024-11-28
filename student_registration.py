import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    student_id = student_id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    year = year_combobox.get()
    course = course_combobox.get()
    lrn = lrn_entry.get()

    if not all([student_id, name, age, email, phone, year, course, lrn]):
        messagebox.showerror("Error", "Please fill all fields.")
        return

    # Here you can add code to save the data or process it
    registration_details = (
        f"Student LRN: {lrn}"
        f"Student ID: {student_id}\n"
        f"Student Name: {name}\n"
        f"Student Age: {age}\n"
        f"Student Email: {email}\n"
        f"Student Phone: {phone}\n"
        f"Student Year: {year}\n"
        f"Student Course: {course}\n"
    )

    # Show the details in a success message box
    messagebox.showinfo("Registration Successful!", registration_details)

# Create the main window
root = tk.Tk()
root.title("Student Registration Form")
root.configure(bg="#f7f7f7")

# Maximize the window
root.state('zoomed')

# Title label with large font size
title_label = tk.Label(text="Student Registration", font=("Helvetica", 24, "bold"), bg="#4CAF50", fg="#ffffff")
title_label.pack(pady=20, fill=tk.X)

# Create a frame for the form
form_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
form_frame.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)

# Function to create labeled entry fields
def create_labeled_entry(frame, label_text, entry_width=40):
    label = tk.Label(frame, text=label_text, font=("Arial", 12), bg="#ffffff")
    label.pack(pady=5)
    entry = tk.Entry(frame, font=("Arial", 12), width=entry_width, bd=2, relief="solid")
    entry.pack(pady=10)
    return entry

# Create entry fields
student_id_entry = create_labeled_entry(form_frame, "Student ID:")
name_entry = create_labeled_entry(form_frame, "Student Name:")
age_entry = create_labeled_entry(form_frame, "Student Age:")
email_entry = create_labeled_entry(form_frame, "Student Email:")
phone_entry = create_labeled_entry(form_frame, "Student Phone Number:")
lrn_entry = create_labeled_entry(form_frame, "Student LRN (Learner Reference Number):")

# Year label and combobox
year_label = tk.Label(form_frame, text="Student Year:", font=("Arial", 12), bg="#ffffff")
year_label.pack(pady=5)
year_combobox = ttk.Combobox(form_frame, values=["1st Year", "2nd Year", "3rd Year", "4th Year"], font=("Arial", 12), state="readonly", width=38)
year_combobox.pack(pady=10)
year_combobox.current(0)

# Course label and combobox
course_label = tk.Label(form_frame, text="Student Course:", font=("Arial", 12), bg="#ffffff")
course_label.pack(pady=5)
course_combobox = ttk.Combobox(form_frame, values=["Mathematics", "Science", "History", "Art"], font=("Arial", 12), state="readonly", width=38)
course_combobox.pack(pady=10)
course_combobox.current(0)

# Submit button with custom style
submit_button = tk.Button(form_frame, text="Submit", command=submit_form, font=("Arial", 14), bg="#4CAF50", fg="white", bd=0, relief="flat", padx=20, pady=10)
submit_button.pack(pady=30)

# Start the main loop
root.mainloop()