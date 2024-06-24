import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}
        self._countries = DAO.getAllCountries()

    def _creaGrafo(self, country, anno):
        self._nodes = DAO.getAllNodes(country)
        self._grafo.add_nodes_from(self._nodes)
        for u in self._nodes:
            for v in self._nodes:
                if u != v:
                    arco = DAO.getEdge(u, v, anno)
                    if arco[0][0] != None:
                        self._grafo.add_edge(u, v, weight=arco[0][2])

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def getVolumiVendite(self):
        volumi = []
        for n in self._nodes:
            vicini = self._grafo.neighbors(n)
            volumeVicini = 0
            for v in vicini:
                peso = self._grafo[n][v]["weight"]
                volumeVicini += peso
            volumi.append((n, volumeVicini))
        volumi.sort(key=lambda x: x[1], reverse=True)
        return volumi

    def getPercorso(self, lunghezza):
        self._bestPath = []
        self._bestPeso = 0
        for n in self._nodes:
            self._ricorsione(n, [], n, lunghezza)

        return self._bestPath, self._bestPeso

    def _ricorsione(self, nodo, parziale, arrivo, lunghezza):
        pesoParziale = self.getPesoParziale(parziale)
        if len(parziale) > 0:
            if nodo == arrivo and pesoParziale > self._bestPeso and len(parziale) == lunghezza:
                self._bestPeso = pesoParziale
                self._bestPath = copy.deepcopy(parziale)
                return
        vicini = self._grafo.neighbors(nodo)
        for v in vicini:
            if len(parziale) <= lunghezza - 2:
                if self.filtroNodi(v, parziale):
                    peso = self._grafo[nodo][v]["weight"]
                    parziale.append((nodo, v, peso))
                    self._ricorsione(v, parziale, arrivo, lunghezza)
                    parziale.pop()
            elif len(parziale) == lunghezza - 1:
                peso = self._grafo[nodo][v]["weight"]
                parziale.append((nodo, v, peso))
                self._ricorsione(v, parziale, arrivo, lunghezza)
                parziale.pop()

    def filtroNodi(self, v, parziale):
        for a in parziale:
            if a[0] == v or a[1] == v:
                return False
        return True

    def filtroArchi(self, n, v, parziale):
        pass

    def getPesoParziale(self, parziale):
        totP = 0
        for a in parziale:
            totP += a[2]
        return totP
