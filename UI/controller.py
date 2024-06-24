import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDAnno(self):
        anni = ["2015", "2016", "2017", "2018"]
        for a in anni:
            self._view._ddAnno.options.append(ft.dropdown.Option(data=a, text=a, on_click=self.selectAnno))
        self._view.update_page()

    def fillDDCountries(self):
        countries = self._model._countries
        for c in countries:
            self._view._ddNazione.options.append(ft.dropdown.Option(data=c, text=c, on_click=self.selectCountry))
        self._view.update_page()

    def selectAnno(self, e):
        if e.control.data is None:
            self._choiceAnno = None
        else:
            self._choiceAnno = e.control.data

    def selectCountry(self, e):
        if e.control.data is None:
            self._choiceCountry = None
        else:
            self._choiceCountry = e.control.data

    def handle_graph(self, e):
        self._model._creaGrafo(self._choiceCountry, self._choiceAnno)
        nNodi, nArchi = self._model.getGraphDetails()
        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text(f"Grafo correttamente creato. Il grafo ha {nNodi} nodi e {nArchi} archi."))
        self._view._btnVolumi.disabled = False
        self._view._btnRappresentativi.disabled = False
        self._view._txtLenPercorso.disabled = False
        self._view._btnCammino.disabled = False
        self._view.update_page()


    def handleVolumi(self, e):
        volumi = self._model.getVolumiVendite()
        self._view.txt_result1.controls.append(ft.Text("Il volume di vendita dei retailer nel grafo è:"))
        for v in volumi:
            self._view.txt_result1.controls.append(ft.Text(f"{v[0]} : {v[1]}"))
        self._view.update_page()

    def handleRappresentativi(self, e):
        pass

    def handle_percorso(self, e):
        lunghezza = self._view._txtLenPercorso.value
        try:
            intLunghezza = int(lunghezza)
        except ValueError:
            print("Errore, lunghezza inserita non numerica.")
            self._view.txt_result2.controls.clear()
            self._view.txt_result2.controls.append(ft.Text("Inserire una lunghezza numerica."))
            self._view.update_page()
            return
        if intLunghezza < 3:
            print("Errore, lunghezza non valida, inserire un valore maggiore di 2.")
            self._view.txt_result2.controls.clear()
            self._view.txt_result2.controls.append(ft.Text("Errore, lunghezza non valida, inserire un valore maggiore di 2."))
            self._view.update_page()
            return
        percorso, peso = self._model.getPercorso(intLunghezza)
        self._view.txt_result2.controls.clear()
        self._view.txt_result2.controls.append(ft.Text(f"Il percorso trovato ha peso: {peso}."))
        for p in percorso:
            self._view.txt_result2.controls.append(ft.Text(f"{p}"))
        self._view.update_page()
