"""
biblioteca_tk_comentada.py
Sistema de préstamos de una biblioteca con interfaz gráfica hecha en Tkinter.

Este archivo incluye:
- Registro de préstamos
- Consulta de préstamos (activos y todos)
- Devoluciones
- Guardado/lectura automática en JSON
- Comentarios detallados para facilitar su comprensión
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

# Archivo donde se guardarán los préstamos en formato JSON
DATA_FILE = "loans.json"
# ----------------------------------------------------------------------
#      CLASE QUE GESTIONA LOS PRÉSTAMOS (LÓGICA DEL PROGRAMA)
# ----------------------------------------------------------------------
class LoanManager:
    def __init__(self):
        # Diccionario que almacena todos los préstamos
        self.loans = {}  
        # Contador para generar IDs únicos
        self._next_id = 1  
        # Cargar datos existentes (si los hay)
        self.load()

    def _generate_id(self):
        """Genera un identificador numérico único para cada préstamo."""
        id_ = self._next_id
        self._next_id += 1
        return id_

    def register(self, usuario: str, libro: str, fecha: str = None):
        """Registra un nuevo préstamo en el sistema."""
        if not usuario.strip() or not libro.strip():
            raise ValueError("Usuario y libro son obligatorios.")

        # Si no se proporciona fecha, se asigna la fecha y hora actual
        fecha = fecha or datetime.now().strftime("%d/%m/%Y %H:%M")

        # Generar ID único
        id_ = self._generate_id()

        # Guardar el préstamo
        self.loans[id_] = {
            "usuario": usuario.strip(),
            "libro": libro.strip(),
            "fecha": fecha,
            "devuelto": False
        }

        return id_

    def mark_returned(self, id_):
        """Marca un préstamo como devuelto."""
        if id_ not in self.loans:
            raise KeyError("ID no encontrado.")
        if self.loans[id_]["devuelto"]:
            raise ValueError("El préstamo ya fue devuelto.")
        self.loans[id_]["devuelto"] = True

    def get_all(self):
        """Devuelve una lista de todos los préstamos (incluye devueltos)."""
        return sorted(self.loans.items())

    def get_active(self):
        """Devuelve solo los préstamos NO devueltos."""
        return [(i, d) for i, d in self.get_all() if not d["devuelto"]]

    def save(self):
        """Guarda todos los datos en un archivo JSON."""
        data = {
            "next_id": self._next_id,
            "loans": self.loans
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        """Carga datos desde el archivo JSON si existe."""
        if not os.path.exists(DATA_FILE):
            return
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Convertimos las llaves a enteros (el JSON las guarda como strings)
            self.loans = {int(k): v for k, v in data.get("loans", {}).items()}
            self._next_id = int(data.get("next_id", max(self.loans.keys(), default=0) + 1))
        except Exception:
            # Si ocurre error al cargar, se reinicia todo
            self.loans = {}
            self._next_id = 1


# ----------------------------------------------------------------------
#      INTERFAZ GRÁFICA HECHA CON TKINTER
# ----------------------------------------------------------------------
class BibliotecaApp(tk.Tk):
    def __init__(self, manager: LoanManager):
        super().__init__()

        # Configuración general de la ventana
        self.title("Sistema de Préstamos - Biblioteca")
        self.geometry("800x500")
        self.resizable(False, False)

        # Instancia de la lógica de préstamos
        self.manager = manager

        # Crear los elementos de la interfaz
        self.create_widgets()

        # Llenar la tabla con los datos existentes
        self.populate_tree()

    # ==============================================================
    #   CREAR TODOS LOS ELEMENTOS DE LA INTERFAZ
    # ==============================================================
    def create_widgets(self):

        # -----------------------------
        # FRAME SUPERIOR: Registro
        # -----------------------------
        frm_top = ttk.LabelFrame(self, text="Registrar préstamo", padding=(10, 10))
        frm_top.place(x=10, y=10, width=780, height=110)

        ttk.Label(frm_top, text="Usuario:").grid(row=0, column=0, sticky="w")
        self.entry_usuario = ttk.Entry(frm_top, width=30)
        self.entry_usuario.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frm_top, text="Título del libro:").grid(row=0, column=2, sticky="w")
        self.entry_libro = ttk.Entry(frm_top, width=40)
        self.entry_libro.grid(row=0, column=3, padx=5, pady=5)

        ttk.Button(frm_top, text="Registrar préstamo", command=self.on_register).grid(
            row=1, column=3, sticky="e", pady=(5, 0)
        )

        # -----------------------------
        # FRAME DE ACCIONES Y FILTROS
        # -----------------------------
        frm_actions = ttk.Frame(self)
        frm_actions.place(x=10, y=130, width=780, height=40)

        # Botones para mostrar activos o todos
        self.view_var = tk.StringVar(value="activos")
        ttk.Radiobutton(frm_actions, text="Activos", variable=self.view_var, value="activos",
                        command=self.populate_tree).pack(side="left", padx=8)
        ttk.Radiobutton(frm_actions, text="Todos", variable=self.view_var, value="todos",
                        command=self.populate_tree).pack(side="left")

        # Botones de acción
        ttk.Button(frm_actions, text="Marcar devolución", command=self.on_return).pack(side="right", padx=8)
        ttk.Button(frm_actions, text="Guardar ahora", command=self.on_save).pack(side="right")

        # -----------------------------
        # TABLA (TREEVIEW)
        # -----------------------------
        cols = ("ID", "Usuario", "Libro", "Fecha", "Estado")
        self.tree = ttk.Treeview(self, columns=cols, show="headings", selectmode="browse")

        # Configurar columnas
        for c in cols:
            self.tree.heading(c, text=c)

        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Usuario", width=160, anchor="w")
        self.tree.column("Libro", width=300, anchor="w")
        self.tree.column("Fecha", width=160, anchor="center")
        self.tree.column("Estado", width=90, anchor="center")

        # Scrollbar
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)

        # Ubicar tabla y scrollbar
        self.tree.place(x=10, y=180, width=760, height=300)
        vsb.place(x=770, y=180, height=300)

        # Doble clic = ver detalles del préstamo
        self.tree.bind("<Double-1>", self.on_show_details)

    # ==============================================================
    #   MANEJO DE EVENTOS (REGISTRO, DEVOLUCIÓN, GUARDADO)
    # ==============================================================

    def on_register(self):
        """Se ejecuta al presionar 'Registrar préstamo'."""
        usuario = self.entry_usuario.get()
        libro = self.entry_libro.get()

        try:
            # Registrar en la lógica
            id_ = self.manager.register(usuario, libro)
            # Guardar en JSON
            self.manager.save()
            # Mensaje al usuario
            messagebox.showinfo("Éxito", f"Préstamo registrado con ID: {id_}")
            # Limpiar campos
            self.entry_usuario.delete(0, tk.END)
            self.entry_libro.delete(0, tk.END)
            # Actualizar tabla
            self.populate_tree()

        except ValueError as e:
            messagebox.showwarning("Datos incompletos", str(e))

    def populate_tree(self):
        """Actualiza la tabla según el filtro elegido (activos/todos)."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        view = self.view_var.get()
        items = self.manager.get_active() if view == "activos" else self.manager.get_all()

        for id_, data in items:
            estado = "Devuelto" if data["devuelto"] else "No devuelto"
            self.tree.insert("", "end", iid=str(id_),
                             values=(id_, data["usuario"], data["libro"], data["fecha"], estado))

    def on_return(self):
        """Marca como devuelto el préstamo seleccionado en la tabla."""
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Selecciona un préstamo", "Elige un préstamo de la lista primero.")
            return

        id_ = int(sel[0])

        try:
            if self.manager.loans[id_]["devuelto"]:
                messagebox.showinfo("Info", "Este préstamo ya fue devuelto.")
                return

            confirm = messagebox.askyesno("Confirmar devolución",
                                          f"¿Marcar como devuelto el préstamo ID {id_}?")

            if confirm:
                self.manager.mark_returned(id_)
                self.manager.save()
                messagebox.showinfo("Devolución", "La devolución se registró correctamente.")
                self.populate_tree()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_save(self):
        """Guarda manualmente los datos en JSON."""
        try:
            self.manager.save()
            messagebox.showinfo("Guardado", "Datos guardados correctamente.")
        except Exception as e:
            messagebox.showerror("Error al guardar", str(e))

    def on_show_details(self, event):
        """Muestra un cuadro con todos los detalles del préstamo."""
        sel = self.tree.selection()
        if not sel:
            return

        id_ = int(sel[0])
        data = self.manager.loans.get(id_)

        estado = "Devuelto" if data["devuelto"] else "No devuelto"

        details = (
            f"ID: {id_}\n"
            f"Usuario: {data['usuario']}\n"
            f"Libro: {data['libro']}\n"
            f"Fecha: {data['fecha']}\n"
            f"Estado: {estado}"
        )

        messagebox.showinfo("Detalles del préstamo", details)


# ----------------------------------------------------------------------
#                  EJECUCIÓN PRINCIPAL DEL PROGRAMA
# ----------------------------------------------------------------------
def main():
    manager = LoanManager()  # lógica
    app = BibliotecaApp(manager)  # interfaz gráfica
    app.mainloop()  # ejecutar app
def abrir_biblioteca():
    manager = LoanManager()
    app = BibliotecaApp(manager)
    app.mainloop()

if __name__ == "__main__":
    main()
