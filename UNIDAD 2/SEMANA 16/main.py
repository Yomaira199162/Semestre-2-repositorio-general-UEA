import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas Pro")
        self.root.geometry("400x500")

        self.task_entry = tk.Entry(root, font=("Arial", 14))
        self.task_entry.pack(pady=20, padx=20, fill=tk.X)
        self.task_entry.focus_set()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        self.add_button = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(btn_frame, text="Marcar Completada", command=self.mark_completed, bg="#2196F3", fg="white")
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task, bg="#F44336", fg="white")
        self.delete_button.grid(row=0, column=2, padx=5)

        self.tasks_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.mark_completed())
        self.root.bind('<C>', lambda event: self.mark_completed())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.destroy())

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "¡No puedes añadir una tarea vacía!")

    def mark_completed(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            task = self.tasks_listbox.get(index)
            if not task.startswith("✔ "):
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, f"✔ {task}")
                self.tasks_listbox.itemconfig(index, fg="gray", bg="#e1f5fe")
        except IndexError:
            messagebox.showwarning("Atención", "Por favor, selecciona una tarea.")

    def delete_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Atención", "Por favor, selecciona una tarea.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
