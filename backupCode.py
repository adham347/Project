import copy
import queue as Q
import networkx as nx
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1109, 837)
        MainWindow.showMaximized()
        MainWindow.setWindowIcon(QtGui.QIcon(resource_path("icon.png")))
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.coloring)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 640, 571, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setEnabled(False)
        self.label.setHidden(True)
        self.inputnodes = QtWidgets.QLineEdit(self.centralwidget)
        self.inputnodes.setGeometry(QtCore.QRect(480, 680, 113, 22))
        self.inputnodes.setObjectName("inputnodes")
        self.inputnodes.setEnabled(False)
        self.inputnodes.setHidden(True)
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(440, 720, 93, 28))
        self.add.setObjectName("add")
        self.add.setEnabled(False)
        self.add.setHidden(True)
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(540, 720, 93, 28))
        self.reset.setObjectName("reset")
        self.reset.setEnabled(False)
        self.reset.setHidden(True)
        self.done = QtWidgets.QPushButton(self.centralwidget)
        self.done.setEnabled(False)
        self.done.setHidden(True)
        self.done.setGeometry(QtCore.QRect(470, 720, 131, 41))
        self.done.setObjectName("done")
        self.done.setEnabled(False)
        self.done.setHidden(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 750, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setHidden(True)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 660, 1064, 29))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setEnabled(False)
        self.label_3.setHidden(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.algochoose = QtWidgets.QComboBox(self.widget)
        self.algochoose.setEnabled(False)
        self.algochoose.setHidden(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.algochoose.setFont(font)
        self.algochoose.setObjectName("algochoose")
        self.algochoose.addItem("")
        self.algochoose.addItem("")
        self.algochoose.addItem("")
        self.algochoose.addItem("")
        self.algochoose.addItem("")
        self.algochoose.addItem("")
        self.horizontalLayout.addWidget(self.algochoose)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setEnabled(False)
        self.label_4.setHidden(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.initialnodechoose = QtWidgets.QComboBox(self.widget)
        self.initialnodechoose.setEnabled(False)
        self.initialnodechoose.setHidden(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.initialnodechoose.setFont(font)
        self.initialnodechoose.setObjectName("initialnodechoose")
        self.horizontalLayout.addWidget(self.initialnodechoose)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setEnabled(False)
        self.label_5.setHidden(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.finalnodechoose = QtWidgets.QComboBox(self.widget)
        self.finalnodechoose.setEnabled(False)
        self.finalnodechoose.setHidden(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.finalnodechoose.setFont(font)
        self.finalnodechoose.setObjectName("finalnodechoose")
        self.horizontalLayout.addWidget(self.finalnodechoose)
        self.backbtn = QtWidgets.QPushButton(self.centralwidget)
        self.backbtn.setGeometry(QtCore.QRect(1000, 10, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backbtn.setFont(font)
        self.backbtn.setObjectName("backbtn")
        self.backbtn.setEnabled(False)
        self.backbtn.setHidden(True)
        self.iconmainscreen = QtWidgets.QLabel(self.centralwidget)
        self.iconmainscreen.setGeometry(QtCore.QRect(100, 175, 311, 301))
        self.iconmainscreen.setText("")
        self.iconmainscreen.setPixmap(QtGui.QPixmap(resource_path("icon.png")))
        self.iconmainscreen.setScaledContents(True)
        self.iconmainscreen.setObjectName("iconmainscreen")
        self.labelmainscreen = QtWidgets.QLabel(self.centralwidget)
        self.labelmainscreen.setGeometry(QtCore.QRect(380, 275, 601, 101))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelmainscreen.setFont(font)
        self.labelmainscreen.setObjectName("labelmainscreen")
        self.undirectedsolvebtn = QtWidgets.QPushButton(self.centralwidget)
        self.undirectedsolvebtn.setGeometry(QtCore.QRect(370, 420, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.undirectedsolvebtn.setFont(font)
        self.undirectedsolvebtn.setAutoRepeatDelay(301)
        self.undirectedsolvebtn.setAutoDefault(False)
        self.undirectedsolvebtn.setDefault(False)
        self.undirectedsolvebtn.setFlat(False)
        self.undirectedsolvebtn.setObjectName("undirectedsolvebtn")
        self.directedsolvebtn = QtWidgets.QPushButton(self.centralwidget)
        self.directedsolvebtn.setGeometry(QtCore.QRect(560, 420, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.directedsolvebtn.setFont(font)
        self.directedsolvebtn.setAutoRepeatDelay(301)
        self.directedsolvebtn.setAutoDefault(False)
        self.directedsolvebtn.setDefault(False)
        self.directedsolvebtn.setFlat(False)
        self.directedsolvebtn.setObjectName("directedsolvebtn")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(1150, 160, 441, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.devmenu = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.devmenu.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.devmenu.setContentsMargins(0, 0, 0, 0)
        self.devmenu.setObjectName("devmenu")
        self.devucs = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.devucs.setObjectName("devucs")
        self.devmenu.addWidget(self.devucs, 1, 0, 1, 1)
        self.devdfs = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.devdfs.setObjectName("devdfs")
        self.devmenu.addWidget(self.devdfs, 0, 1, 1, 1)
        self.deviddfs = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.deviddfs.setObjectName("deviddfs")
        self.devmenu.addWidget(self.deviddfs, 1, 1, 1, 1)
        self.devbfs = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.devbfs.setMaximumSize(QtCore.QSize(216, 16777215))
        self.devbfs.setObjectName("devbfs")
        self.devmenu.addWidget(self.devbfs, 0, 0, 1, 1)
        self.devgreedy = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.devgreedy.setObjectName("devgreedy")
        self.devmenu.addWidget(self.devgreedy, 2, 1, 1, 1)
        self.devastar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.devastar.setObjectName("devastar")
        self.devmenu.addWidget(self.devastar, 2, 0, 1, 1)
        self.devaddnides = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.devaddnides.setObjectName("devaddnides")
        self.devmenu.addWidget(self.devaddnides, 3, 0, 1, 1)
        self.devnocolor = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.devnocolor.setObjectName("devnocolor")
        self.devmenu.addWidget(self.devnocolor, 3, 1, 1, 1)
        self.testheu = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.testheu.setObjectName("testheu")
        self.devmenu.addWidget(self.testheu, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1109, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dev_count = 0
        self.dev_flag = False

        self.add.clicked.connect(self.add_click)
        self.reset.clicked.connect(lambda : self.reset_click(True))
        self.done.clicked.connect(self.done_click)
        self.pushButton.clicked.connect(self.done_click)
        self.initialnodechoose.activated.connect(self.refresh_combobox)
        self.inputnodes.returnPressed.connect(self.add_click)
        self.directedsolvebtn.clicked.connect(self.directed_click)
        self.undirectedsolvebtn.clicked.connect(self.undirected_click)
        self.backbtn.clicked.connect(self.back_click)
        self.iconmainscreen.mousePressEvent = self.dev_mode
        self.devaddnides.clicked.connect(self.add_click)
        self.devbfs.clicked.connect(lambda : self.BFS(True))
        self.devdfs.clicked.connect(lambda : self.DFS(True))
        self.devucs.clicked.connect(lambda : self.UCS(True))
        self.deviddfs.clicked.connect(lambda : self.IDDFS(True))
        self.devastar.clicked.connect(lambda : self.ASTAR(True))
        self.devgreedy.clicked.connect(lambda : self.GFS(True))
        self.devnocolor.clicked.connect(self.togglecolor)
        self.testheu.clicked.connect(self.test)
        #self.inputnodes.textChanged.connect(self.get_active_nodes)

        self.Visualizer = nx.Graph()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setGeometry(QtCore.QRect(130, 20, 841, 611))
        MainWindow.layout().addWidget(self.canvas)
        self.canvas.setEnabled(False)
        self.canvas.setHidden(True)
        self.shortest_path = []
        self.ufccost = 0
        self.dfsparent = dict()
        self.dfspathfound = False
        self.nodes = []
        self.edges = []
        self.node_atrr = dict()
        self.edge_labels = dict()
        self.drawing_counter = 0
        self.iddfs_paths = []
        self.iddfs_path_index = 0
        self.colorof = False
        self.test_case_counter = 0
        self.static_graph_pos = nx.spring_layout
        self.static_check = False

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def directed_click(self):
        self.Visualizer = nx.DiGraph()
        self.start_click()
    def undirected_click(self):
        self.Visualizer = nx.Graph()
        self.start_click()
    def test(self):
        pass
        #############################################
        # HEURISTIC TEST
        #############################################
        heu = dict()
        for node in list(self.Visualizer.nodes):
            heu[node], done = QtWidgets.QInputDialog.getText(MainWindow, "H(N)", f"Enter heuristic of Node: {node}")
        for node, heu_val in heu.items():
            self.node_atrr[node] = int(heu_val)
        self.draw_graph()
    def togglecolor(self):
        self.colorof = not self.colorof
    def start_click(self):
        self.label.setEnabled(True)
        self.label.setHidden(False)
        self.inputnodes.setEnabled(True)
        self.inputnodes.setHidden(False)
        self.add.setEnabled(True)
        self.add.setHidden(False)
        self.reset.setEnabled(True)
        self.reset.setHidden(False)
        self.pushButton.setEnabled(True)
        self.pushButton.setHidden(False)
        self.canvas.setEnabled(True)
        self.canvas.setHidden(False)
        self.backbtn.setEnabled(True)
        self.backbtn.setHidden(False)

        self.iconmainscreen.setEnabled(False)
        self.iconmainscreen.setHidden(True)
        self.labelmainscreen.setEnabled(False)
        self.labelmainscreen.setHidden(True)
        self.directedsolvebtn.setEnabled(False)
        self.directedsolvebtn.setHidden(True)
        self.undirectedsolvebtn.setEnabled(False)
        self.undirectedsolvebtn.setHidden(True)
    def back_click(self):
        if self.inputnodes.isHidden() == True :
            self.done.setEnabled(False)
            self.label_3.setEnabled(False)
            self.algochoose.setEnabled(False)
            self.label_4.setEnabled(False)
            self.initialnodechoose.setEnabled(False)
            self.label_5.setEnabled(False)
            self.finalnodechoose.setEnabled(False)
            self.done.setHidden(True)
            self.label_3.setHidden(True)
            self.algochoose.setHidden(True)
            self.label_4.setHidden(True)
            self.initialnodechoose.setHidden(True)
            self.label_5.setHidden(True)
            self.finalnodechoose.setHidden(True)

            self.add.setHidden(False)
            self.pushButton.setHidden(False)
            self.inputnodes.setHidden(False)
            self.label.setHidden(False)
            self.reset.setHidden(False)
            self.add.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.inputnodes.setEnabled(True)
            self.label.setEnabled(True)
            self.reset.setEnabled(True)

            self.initialnodechoose.clear()
            self.finalnodechoose.clear()
            self.static_check = False
        else:
            self.label.setEnabled(False)
            self.label.setHidden(True)
            self.inputnodes.setEnabled(False)
            self.inputnodes.setHidden(True)
            self.add.setEnabled(False)
            self.add.setHidden(True)
            self.reset.setEnabled(False)
            self.reset.setHidden(True)
            self.pushButton.setEnabled(False)
            self.pushButton.setHidden(True)
            self.canvas.setEnabled(False)
            self.canvas.setHidden(True)
            self.backbtn.setEnabled(False)
            self.backbtn.setHidden(True)

            self.iconmainscreen.setEnabled(True)
            self.iconmainscreen.setHidden(False)
            self.labelmainscreen.setEnabled(True)
            self.labelmainscreen.setHidden(False)
            self.directedsolvebtn.setEnabled(True)
            self.directedsolvebtn.setHidden(False)
            self.undirectedsolvebtn.setEnabled(True)
            self.undirectedsolvebtn.setHidden(False)
    def add_click(self):
        if self.dev_flag:
            if self.test_case_counter>1:self.test_case_counter=0
            if self.test_case_counter == 0:
                self.reset_click(True)
                self.Visualizer.add_edge("A", "B")
                self.edge_labels[("A", "B")] = 6
                self.Visualizer.add_edge("A", "F")
                self.edge_labels[("A", "F")] = 3
                self.Visualizer.add_edge("B", "C")
                self.edge_labels[("B", "C")] = 3
                self.Visualizer.add_edge("B", "D")
                self.edge_labels[("B", "D")] = 2
                self.Visualizer.add_edge("C", "D")
                self.edge_labels[("C", "D")] = 1
                self.Visualizer.add_edge("C", "E")
                self.edge_labels[("C", "E")] = 5
                self.Visualizer.add_edge("D", "E")
                self.edge_labels[("D", "E")] = 8
                self.Visualizer.add_edge("E", "J")
                self.edge_labels[("E", "J")] = 5
                self.Visualizer.add_edge("E", "I")
                self.edge_labels[("E", "I")] = 5
                self.Visualizer.add_edge("J", "I")
                self.edge_labels[("J", "I")] = 3
                self.Visualizer.add_edge("I", "G")
                self.edge_labels[("I", "G")] = 3
                self.Visualizer.add_edge("I", "H")
                self.edge_labels[("I", "H")] = 2
                self.Visualizer.add_edge("F", "H")
                self.edge_labels[("F", "H")] = 7
                self.Visualizer.add_edge("F", "G")
                self.edge_labels[("F", "G")] = 1
                self.node_atrr["A"] = 10
                self.node_atrr["B"] = 8
                self.node_atrr["C"] = 5
                self.node_atrr["D"] = 7
                self.node_atrr["E"] = 3
                self.node_atrr["F"] = 6
                self.node_atrr["G"] = 5
                self.node_atrr["H"] = 3
                self.node_atrr["I"] = 1
                self.node_atrr["J"] = 0
                self.test_case_counter += 1
            elif self.test_case_counter == 1:
                self.reset_click(True)
                self.Visualizer.add_edge("S", "A")
                self.edge_labels[("S", "A")] = 1
                self.Visualizer.add_edge("S", "G")
                self.edge_labels[("S", "G")] = 12
                self.Visualizer.add_edge("A", "B")
                self.edge_labels[("A", "B")] = 3
                self.Visualizer.add_edge("A", "C")
                self.edge_labels[("A", "C")] = 1
                self.Visualizer.add_edge("B", "D")
                self.edge_labels[("B", "D")] = 3
                self.Visualizer.add_edge("C", "D")
                self.edge_labels[("C", "D")] = 1
                self.Visualizer.add_edge("C", "G")
                self.edge_labels[("C", "G")] = 2
                self.Visualizer.add_edge("D", "G")
                self.edge_labels[("D", "G")] = 3
                self.node_atrr["S"] = 10
                self.node_atrr["A"] = 8
                self.node_atrr["G"] = 5
                self.node_atrr["B"] = 7
                self.node_atrr["C"] = 3
                self.node_atrr["D"] = 6
                self.test_case_counter+=1
            self.static_check = False
            self.draw_graph()
            self.static_graph_pos = nx.spring_layout(self.Visualizer)
            self.static_check = True
            self.nodes = list(self.Visualizer.nodes)
            self.edges = list(self.Visualizer.edges)
            return
        self.reset_click()
        try:
            inputs = self.inputnodes.text()
            decompose =inputs.split(",")
            if len(decompose)>3 : raise Exception
            self.edge_labels[(str(decompose[0]),str(decompose[1]))] = int(decompose[2])
            self.Visualizer.add_edge(str(decompose[0]),str(decompose[1]))
            self.Visualizer.add_nodes_from(self.nodes)
            self.Visualizer.add_edges_from(self.edges)
            self.static_check = False
            self.draw_graph()
            self.static_graph_pos = nx.spring_layout(self.Visualizer)
            self.static_check = True
            self.nodes = list(self.Visualizer.nodes)
            self.edges = list(self.Visualizer.edges)
        except:
            self.error_popup("Please Enter Edges In Correct Format","Format Example: 1,2,3 or 2,5,6")
    def reset_click(self, check = False):
        if check:
            self.edges = list()
            self.nodes = list()
            self.node_atrr = dict()
            self.edge_labels = dict()
        self.Visualizer.clear()
        self.draw_graph()
    def get_parent_path(self, parents, node):
        shortest_path = [node]
        curr = node
        while parents[curr] is not None:
            shortest_path.append(parents[curr])
            curr = parents[curr]
        shortest_path.reverse()
        return shortest_path
    def done_click(self):
        if self.label_5.isHidden() == True:
            if len(list(self.Visualizer.nodes)) == 0 :
                self.error_popup("Please Enter At Least One Edge.")
                return
            self.done.setEnabled(True)
            self.label_3.setEnabled(True)
            self.algochoose.setEnabled(True)
            self.label_4.setEnabled(True)
            self.initialnodechoose.setEnabled(True)
            self.label_5.setEnabled(True)
            self.finalnodechoose.setEnabled(True)
            self.done.setHidden(False)
            self.label_3.setHidden(False)
            self.algochoose.setHidden(False)
            self.label_4.setHidden(False)
            self.initialnodechoose.setHidden(False)
            self.label_5.setHidden(False)
            self.finalnodechoose.setHidden(False)

            self.add.setHidden(True)
            self.pushButton.setHidden(True)
            self.inputnodes.setHidden(True)
            self.label.setHidden(True)
            self.reset.setHidden(True)
            self.add.setEnabled(False)
            self.pushButton.setEnabled(False)
            self.inputnodes.setEnabled(False)
            self.label.setEnabled(False)
            self.reset.setEnabled(False)

            for i in list(self.Visualizer.nodes):
                self.initialnodechoose.addItem(str(i))
            for i in list(self.Visualizer.nodes):
                if self.initialnodechoose.currentText() == str(i) : continue
                self.finalnodechoose.addItem(str(i))

            self.path = ""
        else:
            if self.algochoose.currentText() == "Breadth First" : self.BFS()
            elif self.algochoose.currentText() == "Depth First" : self.DFS()
            elif self.algochoose.currentText() == "Uniform Cost" : self.UCS()
            elif self.algochoose.currentText() == "Iterative Deepening" : self.IDDFS()
            elif self.algochoose.currentText() == "Greedy First":
                self.test()
                self.GFS()
            elif self.algochoose.currentText() == "A* Search":
                self.test()
                self.ASTAR()

            if self.colorof:
                self.show_solution()
                self.path = ""
                self.shortest_path = []
                self.ufccost = 0
                self.dfsparent = dict()
                self.dfspathfound = False
                self.drawing_counter = 0
                self.iddfs_path_index = 0
                self.iddfs_paths = []
                return
            self.done.setEnabled(False)
            self.label_3.setEnabled(False)
            self.algochoose.setEnabled(False)
            self.label_4.setEnabled(False)
            self.initialnodechoose.setEnabled(False)
            self.label_5.setEnabled(False)
            self.finalnodechoose.setEnabled(False)
            self.backbtn.setEnabled(False)

            self.timer.start()
    def refresh_combobox(self):
        self.finalnodechoose.clear()
        for i in list(self.Visualizer.nodes):
            if self.initialnodechoose.currentText() == str(i): continue
            self.finalnodechoose.addItem(str(i))
    def BFS(self, devcheck = False):
        if devcheck:
            if self.test_case_counter == 0:
                self.initialnodechoose.setCurrentText("A")
                self.finalnodechoose.setCurrentText("J")
            elif self.test_case_counter == 1:
                self.initialnodechoose.setCurrentText("S")
                self.finalnodechoose.setCurrentText("G")
        visited = [False] * len(self.Visualizer.nodes)
        queue = []
        color_map = []
        nodes = list(self.Visualizer.nodes)
        queue.append(nodes[nodes.index(str(self.initialnodechoose.currentText()))])
        visited[nodes.index(str(self.initialnodechoose.currentText()))] = True
        parent = dict()
        parent[self.initialnodechoose.currentText()] = None
        path_found = False
        while len(queue) > 0 :
            s = queue.pop(0)
            print(s, end=" ")
            if self.path == "" : self.path = str(s)
            else: self.path = self.path + "->" + str(s)
            if str(s) == self.finalnodechoose.currentText() : path_found = True
            for i in list(self.Visualizer.adj.get(s)):
                if visited[nodes.index(i)] == False:
                    queue.append(i)
                    parent[str(i)] = str(s)
                    visited[nodes.index(i)] = True
        target_node = self.finalnodechoose.currentText()
        if path_found:
            self.shortest_path = self.get_parent_path(parent,target_node)
        if self.colorof:
            for i in visited:
                if i:
                    color_map.append("red")
                else:
                    color_map.append("black")
            color_map[nodes.index(str(self.initialnodechoose.currentText()))] = "yellow"
            color_map[nodes.index(str(self.finalnodechoose.currentText()))] = "green"
            self.draw_graph(color_map)
        if devcheck:
            self.algochoose.setCurrentText("Breadth First")
            self.show_solution()
            self.path = ""
            self.shortest_path = []
            self.ufccost = 0
            self.dfsparent = dict()
            self.dfspathfound = False
            self.drawing_counter = 0
    def GFS(self, devcheck = False):
        if devcheck:
            if self.test_case_counter == 0:
                self.initialnodechoose.setCurrentText("A")
                self.finalnodechoose.setCurrentText("J")
            elif self.test_case_counter == 1:
                self.initialnodechoose.setCurrentText("S")
                self.finalnodechoose.setCurrentText("G")
        visited = [False] * len(self.Visualizer.nodes)
        queue = []
        not_chosen = dict()
        nodes = list(self.Visualizer.nodes)
        queue.append(nodes[nodes.index(str(self.initialnodechoose.currentText()))])
        visited[nodes.index(str(self.initialnodechoose.currentText()))] = True
        parents = dict()
        parents[self.initialnodechoose.currentText()] = None
        while len(queue) > 0:
            s = queue.pop(0)
            print(s, end=" ")
            if s in not_chosen.keys():not_chosen.pop(s)
            if self.path == "":self.path = str(s)
            else:self.path = self.path + "->" + str(s)
            if str(s) == self.finalnodechoose.currentText(): break
            minim_hue = 10 ** 8
            minim_node = ""
            for i in list(self.Visualizer.adj.get(s)):
                if visited[nodes.index(i)] == False:
                    if self.node_atrr[i] < minim_hue:
                        minim_hue = self.node_atrr[i]
                        minim_node = i
                    else:
                        not_chosen[i] = self.node_atrr[i]
            if len(not_chosen.items()) > 0:
                node_to_add = []
                node_to_remove = []
                flag = False
                for node, hue in not_chosen.items():
                    if hue < minim_hue:
                        flag = True
                        node_to_remove.append(node)
                        node_to_add.append(minim_node)
                        minim_hue = hue
                        minim_node = node
                if flag:
                    for node in node_to_remove:not_chosen.pop(node)
                    for node in node_to_add:not_chosen[node] = self.node_atrr[node]
            queue.append(minim_node)
            parents[minim_node] = s
            visited[nodes.index(minim_node)] = True
        self.shortest_path = self.path.split("->")
        if self.colorof:
            color_map = []
            for i in visited:
                if i:
                    color_map.append("red")
                else:
                    color_map.append("black")
            color_map[nodes.index(str(self.initialnodechoose.currentText()))] = "yellow"
            color_map[nodes.index(str(self.finalnodechoose.currentText()))] = "green"
            self.draw_graph(color_map)
        if devcheck:
            self.algochoose.setCurrentText("Uniform Cost")
            self.initialnodechoose.setCurrentText("1")
            self.finalnodechoose.setCurrentText("6")
            self.show_solution()
            self.path = ""
            self.shortest_path = []
            self.dfsparent = dict()
            self.dfspathfound = False
            self.drawing_counter = 0
    def draw_graph(self, color_map = []):
        pos = nx.spring_layout(self.Visualizer)
        if self.static_check: pos = self.static_graph_pos
        try:
            if not color_map:
                self.figure.clear()
                nx.draw_networkx(self.Visualizer, pos)
                nx.draw_networkx_edge_labels(self.Visualizer, pos, edge_labels=self.edge_labels)
                if len(self.node_atrr) > 0:
                    for node in list(self.Visualizer.nodes):
                        x, y = pos[node]
                        plt.text(x, y + 0.07, s=self.node_atrr[node], color="red", zorder=20.0,
                                 horizontalalignment='center')
                plt.draw()
            else:
                self.figure.clear()
                nx.draw_networkx(self.Visualizer, pos, node_color=color_map)
                nx.draw_networkx_edge_labels(self.Visualizer, pos, edge_labels=self.edge_labels)
                if len(self.node_atrr)>0:
                    for node in list(self.Visualizer.nodes):
                        x, y = pos[node]
                        plt.text(x, y+0.07, s=self.node_atrr[node], color="red", zorder=20.0,
                                 horizontalalignment='center')
                plt.draw()
        except:
            self.figure.clear()
            nx.draw_networkx(self.Visualizer, pos)
            if len(self.node_atrr) > 0:
                for node in list(self.Visualizer.nodes):
                    x, y = pos[node]
                    plt.text(x, y + 0.07, s=self.node_atrr[node], color="red", zorder=20.0,
                             horizontalalignment='center')
            plt.draw()
    def DFSUtil(self, visited, current):
        visited.append(current)
        print(current, end=' ')
        if self.path == "": self.path = str(current)
        else: self.path = self.path + "->" + str(current)
        if str(current) == self.finalnodechoose.currentText(): self.dfspathfound = True
        for adj in list(self.Visualizer.adj.get(current)):
            if adj not in visited:
                self.dfsparent[str(adj)] = str(current)
                self.DFSUtil(visited, adj)
    def DFS(self, devcheck = False):
        if devcheck:
            if self.test_case_counter == 0:
                self.initialnodechoose.setCurrentText("A")
                self.finalnodechoose.setCurrentText("J")
            elif self.test_case_counter == 1:
                self.initialnodechoose.setCurrentText("S")
                self.finalnodechoose.setCurrentText("G")
        self.dfsparent[self.initialnodechoose.currentText()] = None
        nodes = list(self.Visualizer.nodes)
        visited = []
        self.DFSUtil(visited, nodes[nodes.index(str(self.initialnodechoose.currentText()))])
        target_node = self.finalnodechoose.currentText()
        if self.dfspathfound:
            print(self.get_parent_path(self.dfsparent, target_node))
            self.shortest_path = self.get_parent_path(self.dfsparent,target_node)
        if self.colorof:
            color_map = []
            for i in visited:
                if i:
                    color_map.append("red")
                else:
                    color_map.append("black")
            color_map[nodes.index(str(self.initialnodechoose.currentText()))] = "yellow"
            color_map[nodes.index(str(self.finalnodechoose.currentText()))] = "green"
            self.draw_graph(color_map)
        if devcheck:
            self.algochoose.setCurrentText("Depth First")
            self.show_solution()
            self.path = ""
            self.shortest_path = []
            self.dfsparent = dict()
            self.ufccost = 0
            self.dfspathfound = False
            self.drawing_counter = 0
    def ASTAR(self, devcheck = False):
        if devcheck:
            if self.test_case_counter == 0:
                self.initialnodechoose.setCurrentText("A")
                self.finalnodechoose.setCurrentText("J")
            elif self.test_case_counter == 1:
                self.initialnodechoose.setCurrentText("S")
                self.finalnodechoose.setCurrentText("G")
        nodes = list(self.Visualizer.nodes)
        queue = Q.PriorityQueue()
        queue.put((0, [self.initialnodechoose.currentText()]))
        while not queue.empty():
            node = queue.get()
            current = node[1][len(node[1]) - 1]
            if self.finalnodechoose.currentText() in node[1]:
                self.shortest_path = node[1]
                self.ufccost = node[0]
                break
            cost = node[0]
            for neighbor in list(self.Visualizer.adj.get(current)):
                temp = node[1][:]
                temp.append(neighbor)
                if (current, neighbor) in self.edge_labels.keys():
                    queue.put((cost + self.node_atrr[neighbor] + self.edge_labels[(current, neighbor)], temp))
                else:
                    queue.put((cost + self.node_atrr[neighbor] + self.edge_labels[(neighbor, current)], temp))
        if self.colorof:
            color_map = ["black"] * len(nodes)
            for node in self.shortest_path:
                color_map[nodes.index(node)] = "red"
            color_map[nodes.index(str(self.initialnodechoose.currentText()))] = "yellow"
            color_map[nodes.index(str(self.finalnodechoose.currentText()))] = "green"
            self.draw_graph(color_map)
        if devcheck:
            self.algochoose.setCurrentText("A* Search")
            self.show_solution()
            self.path = ""
            self.shortest_path = []
            self.dfsparent = dict()
            self.dfspathfound = False
            self.drawing_counter = 0
    def IDDFSUtil(self, visited, current, depth):
        if dict(nx.all_pairs_shortest_path_length(self.Visualizer))[self.initialnodechoose.currentText()][str(current)]>depth:
            return False
        visited.append(current)
        if self.path == "":
            self.path = str(current)
        else:
            self.path = self.path + "->" + str(current)
        if str(current) == self.finalnodechoose.currentText(): self.dfspathfound = True
        for adj in list(self.Visualizer.adj.get(current)):
            if adj not in visited:
                self.dfsparent[str(adj)] = str(current)
                self.IDDFSUtil(visited, adj, depth)
    def IDDFS(self, devcheck = False):
        if devcheck:
            if self.test_case_counter == 0:
                self.initialnodechoose.setCurrentText("A")
                self.finalnodechoose.setCurrentText("J")
            elif self.test_case_counter == 1:
                self.initialnodechoose.setCurrentText("S")
                self.finalnodechoose.setCurrentText("G")
        nodes = list(self.Visualizer.nodes)
        for i in range(1,1000):
            self.dfsparent[self.initialnodechoose.currentText()] = None
            visited = []
            self.IDDFSUtil(visited, nodes[nodes.index(str(self.initialnodechoose.currentText()))], i)
            self.iddfs_paths.append(self.path.split("->"))
            if self.dfspathfound: break
            print("\n")
            self.dfsparent.clear()
            self.ufccost = 0
            self.dfspathfound = False
            self.path = ""
        if self.colorof:
            color_map = []
            for i in visited:
                if i:
                    color_map.append("red")
                else:
                    color_map.append("black")
            color_map[nodes.index(str(self.initialnodechoose.currentText()))] = "yellow"
            color_map[nodes.index(str(self.finalnodechoose.currentText()))] = "green"
            self.draw_graph(color_map)
        if devcheck:
            self.algochoose.setCurrentText("Iterative Deepening")
            self.show_solution()
            self.path = ""
            self.shortest_path = []
            self.dfsparent = dict()
            self.dfspathfound = False
            self.ufccost = 0
            self.drawing_counter = 0
            self.iddfs_path_index = 0
            self.iddfs_paths = []
    def UCS(self, devcheck = False):
        if devcheck:
            if self.test_case_counter == 0:
                self.initialnodechoose.setCurrentText("A")
                self.finalnodechoose.setCurrentText("J")
            elif self.test_case_counter == 1:
                self.initialnodechoose.setCurrentText("S")
                self.finalnodechoose.setCurrentText("G")
        nodes = list(self.Visualizer.nodes)
        queue = Q.PriorityQueue()
        queue.put((0, [self.initialnodechoose.currentText()]))
        while not queue.empty():
            node = queue.get()
            current = node[1][len(node[1]) - 1]
            if self.finalnodechoose.currentText() in node[1]:
                self.shortest_path = node[1]
                self.ufccost = node[0]
                break
            cost = node[0]
            for neighbor in list(self.Visualizer.adj.get(current)):
                temp = node[1][:]
                temp.append(neighbor)
                if (current, neighbor) in self.edge_labels.keys():
                    queue.put((cost + self.edge_labels[(current, neighbor)], temp))
                else:
                    queue.put((cost + self.edge_labels[(neighbor, current)], temp))
        if self.colorof:
            color_map = ["black"] * len(nodes)
            for node in self.shortest_path:
                color_map[nodes.index(node)] = "red"
            color_map[nodes.index(str(self.initialnodechoose.currentText()))] = "yellow"
            color_map[nodes.index(str(self.finalnodechoose.currentText()))] = "green"
            self.draw_graph(color_map)
        if devcheck:
            self.algochoose.setCurrentText("Uniform Cost")
            self.show_solution()
            self.path = ""
            self.shortest_path = []
            self.dfsparent = dict()
            self.dfspathfound = False
            self.drawing_counter = 0
    def show_solution(self):
        search_path = self.path.split("->")
        path_to_FinalNode = ""
        for node in search_path:
            if str(node) == self.initialnodechoose.currentText() :
                path_to_FinalNode = str(node)
                continue
            if str(node) == self.finalnodechoose.currentText() :
                path_to_FinalNode = path_to_FinalNode + "->" + str(node)
                break
            path_to_FinalNode = path_to_FinalNode + "->" + str(node)
        shortest_path = ""
        for node in self.shortest_path:
            if str(node) == self.initialnodechoose.currentText():
                shortest_path = str(node)
                continue
            shortest_path = shortest_path + "->" + str(node)
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Solution")
        msg.setWindowIcon(QtGui.QIcon(resource_path("icon.png")))
        msg.setText("Problem Solved!")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        if self.algochoose.currentText() == "Iterative Deepening":
            shortest_path = []
            shortest_path_str = ""
            target_node = self.finalnodechoose.currentText()
            shortest_path.append(target_node)
            while self.dfsparent[target_node] is not None:
                shortest_path.append(self.dfsparent[target_node])
                target_node = self.dfsparent[target_node]
            shortest_path.reverse()
            for node in shortest_path:
                if str(node) == self.initialnodechoose.currentText():
                    shortest_path_str = str(node)
                    continue
                shortest_path_str = shortest_path_str + "->" + str(node)
            display_text = "Problem was solved using: " + self.algochoose.currentText() + "\nInitial State: " + self.initialnodechoose.currentText() + "\nFinal State: " + self.finalnodechoose.currentText()
            for path in self.iddfs_paths:
                temp_path = ""
                for index in range(0, len(path)):
                    if temp_path == "":
                        temp_path = path[index] + "->"
                        continue
                    if index == len(path)-1:
                        temp_path = temp_path + path[index]
                        continue
                    temp_path = temp_path + path[index] + "->"
                display_text = display_text + f"\nSearch path with depth limit = {self.iddfs_paths.index(path)} is: " + temp_path
            display_text = display_text +"\nPath To Solution is: "+path_to_FinalNode+"\nShortest Path To Solution is: "+shortest_path_str
            msg.setInformativeText(display_text)
            x = msg.exec_()
            return
        if self.algochoose.currentText() == "Uniform Cost" or self.algochoose.currentText() == "A* Search":
            paz = ""
            for node in self.shortest_path:
                if paz == "":
                    paz = str(node)
                    continue
                paz = paz + "->" + str(node)
            if self.algochoose.currentText() == "Uniform Cost":
                msg.setInformativeText("Problem was solved using: " + self.algochoose.currentText() + "\nInitial State: " + self.initialnodechoose.currentText() + "\nFinal State: " + self.finalnodechoose.currentText() + "\nSolution Path is: "+paz+"\nPath Cost is : " + str(self.ufccost))
            if self.algochoose.currentText() == "A* Search":
                cost_without_heu = self.ufccost
                for node in self.shortest_path:
                    if node == self.initialnodechoose.currentText(): continue
                    cost_without_heu -= self.node_atrr[node]
                msg.setInformativeText("Problem was solved using: " + self.algochoose.currentText() + "\nInitial State: " + self.initialnodechoose.currentText() + "\nFinal State: " + self.finalnodechoose.currentText() + "\nSolution Path is: " + paz + "\nPath Cost Without Heuristic is : " + str(cost_without_heu) + "\nPath Cost With Heuristic is : " + str(self.ufccost))
            x = msg.exec_()
            return
        msg.setInformativeText("Problem was solved using: "+self.algochoose.currentText()+"\nInitial State: "+self.initialnodechoose.currentText()+"\nFinal State: "+self.finalnodechoose.currentText()+"\nSearch Path Taken is: "+self.path+"\nPath To Solution is: "+path_to_FinalNode+"\nShortest Path To Solution is: "+shortest_path)
        x = msg.exec_()
    def get_active_nodes(self):
        self.reset_click()
        self.Visualizer.add_nodes_from(self.nodes)
        self.Visualizer.add_edges_from(self.edges)
        if len(self.inputnodes.text()) == 1:
            try:
                self.Visualizer.add_node(int(self.inputnodes.text()))
                self.draw_graph()
            except:
                self.reset_click()
                self.Visualizer.add_nodes_from(self.nodes)
                self.Visualizer.add_edges_from(self.edges)
                self.draw_graph()
                return
        elif len(self.inputnodes.text()) == 3:
            try:
                inputs = self.inputnodes.text()
                decompose = inputs.split(",")
                self.Visualizer.add_edge(int(decompose[0]), int(decompose[1]))
                self.draw_graph()
            except:
                self.reset_click()
                self.Visualizer.add_nodes_from(self.nodes)
                self.Visualizer.add_edges_from(self.edges)
                self.draw_graph()
                return
        elif len(self.inputnodes.text()) == 0:
            self.reset_click()
            self.Visualizer.add_nodes_from(self.nodes)
            self.Visualizer.add_edges_from(self.edges)
            self.draw_graph()
        else:
            self.reset_click()
            self.Visualizer.add_nodes_from(self.nodes)
            self.Visualizer.add_edges_from(self.edges)
            self.draw_graph()
            return
    def error_popup(self,err_msg,extra=""):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setWindowIcon(QtGui.QIcon(resource_path("icon.png")))
        msg.setText("An Error Occurred!")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setInformativeText(err_msg)
        if extra != "" : msg.setDetailedText(extra)
        x = msg.exec_()
    def btn_popup_click(self, i):
        if i.text() == "OK":
            self.dev_flag = True
            self.dev_count = 0
            MainWindow.resize(1632, 837)
            MainWindow.setFixedSize(1632, 837)
        else:
            print("cancel")
            MainWindow.resize(1109, 837)
            MainWindow.setFixedSize(1109, 837)
            self.dev_flag = False
            self.dev_count = 0
    def dev_mode(self, event):
        self.dev_count += 1
        if self.dev_count == 7:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Welcome")
            msg.setWindowIcon(QtGui.QIcon(resource_path("icon.png")))
            msg.setText("You Have Entered Dev Mode!\nEnjoy \U0001f44d")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msg.buttonClicked.connect(self.btn_popup_click)
            x = msg.exec_()
    def coloring(self):
        if self.algochoose.currentText() == "Iterative Deepening":
            color_map = ["grey"] * len(self.Visualizer.nodes)
            if self.iddfs_path_index == len(self.iddfs_paths):
                for path in self.iddfs_paths:
                    print(path)
                self.show_solution()
                self.path = ""
                self.shortest_path = []
                self.dfsparent = dict()
                self.dfspathfound = False
                self.drawing_counter = 0
                self.ufccost = 0
                self.iddfs_path_index = 0
                self.iddfs_paths = []
                self.done.setEnabled(True)
                self.label_3.setEnabled(True)
                self.algochoose.setEnabled(True)
                self.label_4.setEnabled(True)
                self.initialnodechoose.setEnabled(True)
                self.label_5.setEnabled(True)
                self.finalnodechoose.setEnabled(True)
                self.backbtn.setEnabled(True)
                self.timer.stop()
                return
            if self.drawing_counter == len(self.iddfs_paths[self.iddfs_path_index]):
                self.drawing_counter = 0
                self.iddfs_path_index += 1
                return
            for i in range(0, self.drawing_counter + 1):
                color_map[list(self.Visualizer.nodes).index(self.iddfs_paths[self.iddfs_path_index][i])] = "red"
                color_map[list(self.Visualizer.nodes).index(self.initialnodechoose.currentText())] = "green"
            if self.drawing_counter == len(self.iddfs_paths[self.iddfs_path_index]) - 1 and self.iddfs_path_index == len(self.iddfs_paths)-1:
                color_map[list(self.Visualizer.nodes).index(self.finalnodechoose.currentText())] = "yellow"
            self.draw_graph(color_map)
            self.drawing_counter += 1
            return
        if self.algochoose.currentText() == "Uniform Cost" or self.algochoose.currentText() == "A* Search":
            color_map = ["grey"] * len(self.Visualizer.nodes)
            if self.drawing_counter == len(self.shortest_path):
                self.show_solution()
                self.path = ""
                self.shortest_path = []
                self.dfsparent = dict()
                self.ufccost = 0
                self.dfspathfound = False
                self.drawing_counter = 0
                self.done.setEnabled(True)
                self.label_3.setEnabled(True)
                self.algochoose.setEnabled(True)
                self.label_4.setEnabled(True)
                self.initialnodechoose.setEnabled(True)
                self.label_5.setEnabled(True)
                self.finalnodechoose.setEnabled(True)
                self.backbtn.setEnabled(True)
                self.timer.stop()
                return
            for i in range (0,self.drawing_counter+1):
                color_map[list(self.Visualizer.nodes).index(self.shortest_path[i])] = "red"
                color_map[list(self.Visualizer.nodes).index(self.initialnodechoose.currentText())] = "green"
            if self.drawing_counter == len(self.shortest_path)-1:
                color_map[list(self.Visualizer.nodes).index(self.finalnodechoose.currentText())] = "yellow"
            self.draw_graph(color_map)
            self.drawing_counter+=1
            return
        if self.path != "":
            color_map = ["grey"] * len(self.Visualizer.nodes)
            if self.drawing_counter == len(self.path.split("->")):
                self.show_solution()
                self.path = ""
                self.shortest_path = []
                self.dfsparent = dict()
                self.ufccost = 0
                self.dfspathfound = False
                self.drawing_counter = 0
                self.done.setEnabled(True)
                self.label_3.setEnabled(True)
                self.algochoose.setEnabled(True)
                self.label_4.setEnabled(True)
                self.initialnodechoose.setEnabled(True)
                self.label_5.setEnabled(True)
                self.finalnodechoose.setEnabled(True)
                self.backbtn.setEnabled(True)
                self.timer.stop()
                return
            for i in range (0,self.drawing_counter+1):
                color_map[list(self.Visualizer.nodes).index(self.path.split("->")[i])] = "red"
                color_map[list(self.Visualizer.nodes).index(self.initialnodechoose.currentText())] = "green"
            if self.drawing_counter == len(self.path.split("->"))-1:
                color_map[list(self.Visualizer.nodes).index(self.finalnodechoose.currentText())] = "yellow"
            self.draw_graph(color_map)
            self.drawing_counter+=1
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Problem Solver"))
        self.label.setText(_translate("MainWindow", "Please Enter Graph Edges (Note: Format is (Node,Node,Weight) EX: 1,2,3 ):"))
        self.add.setText(_translate("MainWindow", "ADD"))
        self.reset.setText(_translate("MainWindow", "RESET"))
        self.done.setText(_translate("MainWindow", "SOLVE"))
        self.pushButton.setText(_translate("MainWindow", "Done"))
        self.label_3.setText(_translate("MainWindow", "Please Select An Algorithm:"))
        self.algochoose.setItemText(0, _translate("MainWindow", "Depth First"))
        self.algochoose.setItemText(1, _translate("MainWindow", "Breadth First"))
        self.algochoose.setItemText(2, _translate("MainWindow", "Uniform Cost"))
        self.algochoose.setItemText(3, _translate("MainWindow", "Iterative Deepening"))
        self.algochoose.setItemText(4, _translate("MainWindow", "Greedy First"))
        self.algochoose.setItemText(5, _translate("MainWindow", "A* Search"))
        self.label_4.setText(_translate("MainWindow", "Please Select An Initial Node:"))
        self.label_5.setText(_translate("MainWindow", "Please Select Final Node:"))
        self.backbtn.setText(_translate("MainWindow", "Back"))
        self.labelmainscreen.setText(_translate("MainWindow", "Welcome To Problem Solver!"))
        self.directedsolvebtn.setText(_translate("MainWindow", "Solve Directed \nGraph"))
        self.undirectedsolvebtn.setText(_translate("MainWindow", "Solve Undirected \nGraph"))
        self.devucs.setText(_translate("MainWindow", "UCS"))
        self.devdfs.setText(_translate("MainWindow", "DFS"))
        self.deviddfs.setText(_translate("MainWindow", "IDDFS"))
        self.devbfs.setText(_translate("MainWindow", "BFS"))
        self.devgreedy.setText(_translate("MainWindow", "GREEDY"))
        self.devastar.setText(_translate("MainWindow", "A* SEARCH"))
        self.devaddnides.setText(_translate("MainWindow", "ADD NODES"))
        self.devnocolor.setText(_translate("MainWindow", "DISABLE COLORING"))
        self.testheu.setText(_translate("MainWindow", "test h(n)"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())