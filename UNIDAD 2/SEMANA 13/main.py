import tkinter as tk
from tkinter import messagebox, ttk


class GestorTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA DE GESTIÓN DE TAREAS - SEMANA 13")
        self.root.geometry("450x500")
        self.root.configure(bg="#e1e8f0")

        # --- DISEÑO DE LA INTERFAZ ---
        # Etiqueta de encabezado (Label)
        self.header = tk.Label(root, text="Panel de Control de Tareas",
                               font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="white", pady=10)
        self.header.pack(fill=tk.X)

        # Contenedor para la entrada de datos
        frame_entrada = tk.Frame(root, bg="#e1e8f0", pady=15)
        frame_entrada.pack()

        tk.Label(frame_entrada, text="Nueva Tarea:", font=("Arial", 10), bg="#e1e8f0").pack(side=tk.LEFT)

        # Campo de texto (Entry)
        self.entry_tarea = tk.Entry(frame_entrada, font=("Arial", 12), width=25)
        self.entry_tarea.pack(side=tk.LEFT, padx=5)

        # Botón "Agregar"
        self.btn_agregar = tk.Button(frame_entrada, text="Agregar", command=self.agregar_tarea,
                                     bg="#27ae60", fg="white", font=("Arial", 10, "bold"))
        self.btn_agregar.pack(side=tk.LEFT)

        # Lista para mostrar datos (Listbox con Scrollbar para mejor UX)
        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self.frame_lista)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_tareas = tk.Listbox(self.frame_lista, width=45, height=12, font=("Arial", 11),
                                       yscrollcommand=self.scrollbar.set)
        self.lista_tareas.pack(side=tk.LEFT)
        self.scrollbar.config(command=self.lista_tareas.yview)

        # Botón "Limpiar" (Borrar seleccionada)
        self.btn_limpiar = tk.Button(root, text="ELIMINAR TAREA SELECCIONADA", command=self.eliminar_tarea,
                                     bg="#c0392b", fg="white", font=("Arial", 10, "bold"), width=30)
        self.btn_limpiar.pack(pady=15)

    # --- FUNCIONALIDADES (EVENTOS) ---
    def agregar_tarea(self):
        """Añade la información del campo de texto a la lista."""
        tarea = self.entry_tarea.get().strip()
        if tarea:
            self.lista_tareas.insert(tk.END, f"• {tarea}")
            self.entry_tarea.delete(0, tk.END)  # Limpia el campo después de agregar
        else:
            messagebox.showwarning("Campo Vacío", "Por favor, escribe una tarea antes de agregar.")

    def eliminar_tarea(self):
        """Borra la información seleccionada por el usuario."""
        try:
            indice = self.lista_tareas.curselection()
            self.lista_tareas.delete(indice)
        except:
            messagebox.showwarning("Selección Requerida", "Selecciona una tarea de la lista para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareasApp(root)
    root.mainloop()