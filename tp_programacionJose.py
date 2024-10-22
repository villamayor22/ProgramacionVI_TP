import flet as ft
import os

# Configuración inicial de la aplicación
class ShoppingListApp:
    def __init__(self, page):
        self.page = page
        self.tasks = []
        self.current_task = None
        self.setup_ui()
        self.page.update()

    def setup_ui(self):
        # Definimos la interfaz de usuario
        self.logo = ft.Image(src=os.path.abspath("logo1.jpg"), width=300)
        self.header_text = ft.Text("Bienvenido a la app de lista de compras", size=20)

        # Configuramos el tamaño de la ventana y el título
        self.page.window_width = 600
        self.page.window_height = 400
        self.page.title = "Lista de Compras"

        # Añadimos el encabezado
        self.page.add(self.create_header())

        # Campo para nueva tarea
        self.new_task_input = ft.TextField(hint_text="¿Qué necesitas comprar?", width=300)
        
        # Botones de acción
        self.create_buttons()

        # Agregamos todo a la página
        self.page.add(ft.Row([self.new_task_input, *self.buttons]))

    def create_header(self):
        # Genera el encabezado de la aplicación
        return ft.Column(
            [self.logo, self.header_text],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def create_buttons(self):
        # Crea los botones y asigna las funciones
        self.buttons = [
            ft.ElevatedButton("Agregar", on_click=self.add_task),
            ft.ElevatedButton("Modificar", on_click=self.modify_task),
            ft.ElevatedButton("Eliminar", on_click=self.delete_task)
        ]

    def add_task(self, e):
        # Agrega una nueva tarea o actualiza una existente
        task_text = self.new_task_input.value.strip()
        if task_text:
            if self.current_task:
                self.current_task.label = task_text
                self.current_task.update()
                self.current_task = None  # Reseteamos la tarea actual
            else:
                new_checkbox = ft.Checkbox(label=task_text, value=False)
                self.tasks.append(new_checkbox)
                self.page.add(new_checkbox)
            self.new_task_input.value = ""  # Limpia el campo
            self.new_task_input.update()

    def modify_task(self, e):
        # Permite modificar una tarea seleccionada
        for task in self.tasks:
            if task.value:  # Si la tarea está marcada
                self.current_task = task  # Guarda la tarea seleccionada
                self.new_task_input.value = task.label  # Muestra el texto
                self.new_task_input.update()
                break

    def delete_task(self, e):
        # Elimina tareas seleccionadas
        tasks_to_delete = [task for task in self.tasks if task.value]
        for task in tasks_to_delete:
            self.page.controls.remove(task)
            self.tasks.remove(task)
        self.page.update()  # Refresca la página

# Ejecuta la aplicación
def main(page):
    app = ShoppingListApp(page)

# Inicia la aplicación Flet
ft.app(target=main)
