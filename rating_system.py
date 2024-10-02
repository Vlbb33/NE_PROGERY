import tkinter as tk
from tkinter import ttk
from tkinter import font

class Employee:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.level = 1
        self.achievements = []

    def add_points(self, points):
        self.points += points
        self.update_level()

    def update_level(self):
        if self.points >= 100:
            self.level = 2
        if self.points >= 200:
            self.level = 3
        if self.points >= 300:
            self.level = 4

    def add_achievement(self, achievement):
        self.achievements.append(achievement)

    def get_info(self):
        return {
            'name': self.name,
            'points': self.points,
            'level': self.level,
            'achievements': self.achievements
        }

class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Achievements")
        self.root.geometry("800x600")

        self.employees = []

        self.create_widgets()
        self.style_widgets()

    def create_widgets(self):
        self.header_label = tk.Label(self.root, text="Employee Achievements", font=("Helvetica", 20, "bold"))
        self.header_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.name_label = tk.Label(self.root, text="Name:", font=("Helvetica", 12))
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.name_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.points_label = tk.Label(self.root, text="Points:", font=("Helvetica", 12))
        self.points_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.points_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.points_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.add_button = tk.Button(self.root, text="Add Points", command=self.add_points, font=("Helvetica", 12))
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Rank", "Name", "Points", "Level", "Achievements"), show="headings")
        self.tree.heading("Rank", text="Rank")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Points", text="Points")
        self.tree.heading("Level", text="Level")
        self.tree.heading("Achievements", text="Achievements")
        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def style_widgets(self):
        style = ttk.Style()
        style.configure("Treeview", font=("Helvetica", 12))
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))

        self.root.configure(bg="#f0f0f0")
        self.header_label.configure(bg="#f0f0f0")
        self.name_label.configure(bg="#f0f0f0")
        self.points_label.configure(bg="#f0f0f0")

        self.add_button.configure(bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white")

    def add_points(self):
        name = self.name_entry.get()
        points = int(self.points_entry.get())

        employee = next((emp for emp in self.employees if emp.name == name), None)
        if not employee:
            employee = Employee(name)
            self.employees.append(employee)

        employee.add_points(points)
        self.update_achievements()
        self.update_treeview()

    def update_achievements(self):
        if self.employees:
            best_employee = max(self.employees, key=lambda emp: emp.points)
            for employee in self.employees:
                if "Лучший сотрудник" in employee.achievements:
                    employee.achievements.remove("Лучший сотрудник")
            best_employee.add_achievement("Лучший сотрудник")

    def update_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        sorted_employees = sorted(self.employees, key=lambda emp: emp.points, reverse=True)

        for rank, employee in enumerate(sorted_employees, start=1):
            info = employee.get_info()
            self.tree.insert("", "end", values=(rank, info['name'], info['points'], info['level'], ", ".join(info['achievements'])))

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()
