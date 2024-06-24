import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self._title = None
        self.txt_name = None

        self.btn_graph = None
        self.btn_countedges = None
        self.btn_search = None

        self.txt_result = None
        self.txt_result2 = None
        self.txt_result3 = None

        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Esame 18-09-2023", color="blue", size=24)
        self._page.controls.append(self._title)

        self._ddAnno = ft.Dropdown(label="Anno", width=400)
        self._ddNazione = ft.Dropdown(label="Nazione", width=400)
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph, width=200)

        self._controller.fillDDAnno()
        self._controller.fillDDCountries()

        row1 = ft.Row([self._ddAnno, self._ddNazione, self.btn_graph], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._btnVolumi = ft.ElevatedButton(text="Calcola volumi", disabled=True, on_click=self._controller.handleVolumi)
        self._btnRappresentativi = ft.ElevatedButton(text="Retailer Rappresentativi", disabled=True, on_click=self._controller.handleRappresentativi)

        row2 = ft.Row([self._btnVolumi, self._btnRappresentativi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.txt_result1 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        self._page.controls.append(self.txt_result1)

        self._txtLenPercorso = ft.TextField(label="Lunghezza perorso", width=300, disabled=True)

        self._btnCammino = ft.ElevatedButton(text="Calcola percorso", on_click=self._controller.handle_percorso, width=200, disabled=True)
        row3 = ft.Row([self._txtLenPercorso, self._btnCammino], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result2 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        self._page.controls.append(self.txt_result2)
        self._page.update()

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
