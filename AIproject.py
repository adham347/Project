from collections import deque
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import networkx as nx
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from heapq import heappop, heappush
from math import inf


# the first window class that contains the directed and undirected choice

class Ui_FirstWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 346)
        MainWindow.setToolTipDuration(0)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)  # directed graph push button
        self.pushButton.clicked.connect(self.directedButtonClick)
        self.pushButton.setGeometry(QtCore.QRect(110, 180, 141, 81))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)  # undirected graph push button
        self.pushButton_2.clicked.connect(self.undirectedButtonClick)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 180, 141, 81))

        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 601, 61))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AI Searching Algorithms"))
        self.pushButton.setText(_translate("MainWindow", "Directed Graph"))
        self.pushButton_2.setText(_translate("MainWindow", "Undirected Graph"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Choose the type of graph you want to solve</span></p></body></html>"))

    # the function that opens the graph window when any of the choices is clicked
    def directedButtonClick(self):
        self.w = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.w)
        self.w.show()
        global graph
        graph = nx.DiGraph()
        MainWindow.close()

    def undirectedButtonClick(self):
        self.w = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.w)
        self.w.show()
        global graph
        graph = nx.Graph()
        MainWindow.close()


# the graph window class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 681))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setStyleSheet("background-color: rgb(167, 245, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.FnodeIn = QtWidgets.QLineEdit(self.frame)
        self.FnodeIn.setGeometry(QtCore.QRect(10, 30, 113, 22))
        self.FnodeIn.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.FnodeIn.setObjectName("FnodeIn")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 30, 81, 16))
        self.label.setObjectName("label")

        self.SnodeIn = QtWidgets.QLineEdit(self.frame)
        self.SnodeIn.setGeometry(QtCore.QRect(10, 60, 113, 22))
        self.SnodeIn.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.SnodeIn.setObjectName("SnodeIn")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 81, 16))
        self.label_2.setObjectName("label_2")
        self.CostIn = QtWidgets.QLineEdit(self.frame)
        self.CostIn.setGeometry(QtCore.QRect(10, 90, 113, 22))
        self.CostIn.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.CostIn.setObjectName("CostIn")

        self.hIn=QtWidgets.QLineEdit(self.frame)
        self.hIn.setGeometry(QtCore.QRect(10, 120, 113, 22))
        self.hIn.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.hIn.setObjectName("hIn")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(130, 90, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(130, 120, 221, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(130, 140, 55, 16))
        self.label_5.setObjectName("label_5")
        self.AddEdgeButton = QtWidgets.QPushButton(self.frame)
        self.AddEdgeButton.setGeometry(QtCore.QRect(190, 80, 93, 28))
        self.AddEdgeButton.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.AddEdgeButton.setObjectName("AddEdgeButton")
        # Button Event
        self.AddEdgeButton.clicked.connect(self.addEdge)

        self.SetHeuristicButton=QtWidgets.QPushButton(self.frame)
        self.SetHeuristicButton.setGeometry(QtCore.QRect(190,120,93,28))
        self.SetHeuristicButton.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.SetHeuristicButton.setObjectName("SetHeuristicButton")
        self.SetHeuristicButton.clicked.connect(self.setH)

        self.startNodeLabel = QtWidgets.QLabel(self.frame)
        self.startNodeLabel.setGeometry(QtCore.QRect(130, 170, 81, 16))
        self.startNodeLabel.setObjectName("startNodeLabel")
        self.startNodeLabel.setText("Start Node")

        self.SetStartNodeIn = QtWidgets.QLineEdit(self.frame)
        self.SetStartNodeIn.setGeometry(QtCore.QRect(10, 170, 113, 22))
        self.SetStartNodeIn.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.SetStartNodeIn.setObjectName("SetStartNodeIn")

        self.goalNodeLabel = QtWidgets.QLabel(self.frame)
        self.goalNodeLabel.setGeometry(QtCore.QRect(130, 200, 81, 16))
        self.goalNodeLabel.setObjectName("goalNodeLabel")
        self.goalNodeLabel.setText("Goal Node")

        self.SetGoalNodeIn = QtWidgets.QLineEdit(self.frame)
        self.SetGoalNodeIn.setGeometry(QtCore.QRect(10, 200, 113, 22))
        self.SetGoalNodeIn.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.SetGoalNodeIn.setObjectName("SetGoalNodeIn")

        self.ResetButton = QtWidgets.QPushButton(self.frame)
        self.ResetButton.setGeometry(QtCore.QRect(12, 250, 271, 28))
        self.ResetButton.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.ResetButton.setObjectName("ResetButton")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 300, 171, 16))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 320, 201, 22))
        self.comboBox.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.RunButton = QtWidgets.QPushButton(self.frame)
        self.RunButton.setGeometry(QtCore.QRect(10, 580, 271, 28))
        self.RunButton.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.RunButton.setObjectName("RunButton")
        self.RunButton.clicked.connect(lambda x: self.algoPicker(self.comboBox.currentText()))

        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 291, 16))
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(299, -1, 821, 681))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setGeometry(QtCore.QRect(299, -1, 821, 681))
        MainWindow.layout().addWidget(self.canvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "First Node"))
        self.label_2.setText(_translate("MainWindow", "Second Node"))
        self.label_3.setText(_translate("MainWindow", "Cost"))
        self.label_4.setText(_translate("MainWindow", "Heuristic"))
        self.label_5.setText(_translate("MainWindow", "eg: A,5"))
        self.AddEdgeButton.setText(_translate("MainWindow", "Add Edge"))
        self.SetHeuristicButton.setText(_translate("MainWindow", "Set Heuristic"))

        self.ResetButton.setText(_translate("MainWindow", "Reset"))
        self.label_6.setText(_translate("MainWindow", "Choose Searching Algorithm:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Breadth First"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Depth First"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Uniform Cost"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Depth Limited"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Iterative Deepening"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Greedy"))
        self.comboBox.setItemText(6, _translate("MainWindow", "A star"))
        self.RunButton.setText(_translate("MainWindow", "Run"))
        self.label_7.setText(_translate("MainWindow", "Fill in the 3 text boxes below then press add edge"))

    def showError(self, err_msg, extra=""):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Invalid Operation")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setInformativeText(err_msg)
        msg.setDetailedText(extra)
        x = msg.exec_()

    def addEdge(self):
        try:
            Cost = float(self.CostIn.text())
            Node1 = self.FnodeIn.text()
            Node2 = self.SnodeIn.text()
            if len(Node1) == 0: raise Exception
            if len(Node2) == 0: raise Exception
            graph.add_edge(Node1, Node2, weight=Cost)
            nx.set_node_attributes(graph,{Node1:Node1, Node2:Node2},name="label")
            self.showGraphWithH()
            # print(graph.nodes)
        except:
            self.showError("Please enter a Node")

    def setH(self):
        input=self.hIn.text()
        Sinput=input.split(',')
        Node=Sinput[0]
        h=Sinput[1]
        nx.set_node_attributes(graph,{Node: h},name="H")
        nx.set_node_attributes(graph,{Node: Node+'\n'+"H="+h}, name="label")
        self.showGraphWithH()

    def showGraphWithH(self):
        self.figure.clear()
        pos = nx.spring_layout(graph)
        label = nx.get_node_attributes(graph, "label")
        nx.draw(graph, pos,labels=label,node_size=1100)
        edgeLabels = nx.get_edge_attributes(graph, "weight")
        nx.draw_networkx_edge_labels(graph, pos, edgeLabels)
        plt.draw()

    def showGraph(self):
        self.figure.clear()
        pos = nx.spring_layout(graph)
        label = nx.get_node_attributes(graph, "label")
        nx.draw_networkx(graph,pos)
        edgeLabels = nx.get_edge_attributes(graph, "weight")
        nx.draw_networkx_edge_labels(graph, pos, edgeLabels)
        plt.draw()

    # to choose which  search algo
    def algoPicker(self, algoType):
        print("clicked")
        if algoType == "Depth First":
            traced_path = self.depth_first_search(self.SetStartNodeIn.text(), self.SetGoalNodeIn.text(), graph)
            if (traced_path): print('Path:', end=' '); self.print_path(traced_path, self.SetGoalNodeIn.text(),graph); print()

        if algoType == "Breadth First":
            traced_path = self.breadth_first_search(self.SetStartNodeIn.text(), self.SetGoalNodeIn.text(), graph)
            if (traced_path): print('Path:', end=' '); self.print_path(traced_path, self.SetGoalNodeIn.text(),graph); print()

        if algoType == "Depth Limited":
            traced_path = self.depth_limited_search(self.SetStartNodeIn.text(), self.SetGoalNodeIn.text(), graph, -1)
            if (traced_path): print('Path:', end=' '); self.print_path(traced_path, self.SetGoalNodeIn.text(),graph); print()

        if algoType == "Iterative Deepening":
            traced_path = self.iterative_deepening_dfs(self.SetStartNodeIn.text(), self.SetGoalNodeIn.text(), graph)
            if (traced_path): print('Path:', end=' '); self.print_path(traced_path, self.SetGoalNodeIn.text(),graph); print()

        if algoType == "Uniform Cost":
            traced_path, cost = self.uniform_cost_search(self.SetStartNodeIn.text(), self.SetGoalNodeIn.text(), graph)
            if (traced_path): print('Path:', end=' '); self.print_path(traced_path, self.SetGoalNodeIn.text(),graph); print('\n cost:', cost)

        if algoType == "Greedy":
            traced_path, cost = self.greedy_search(self.SetStartNodeIn.text(), self.SetGoalNodeIn.text(), graph)
            if (traced_path): print('Path:', end=' '); self.print_path(traced_path, self.SetGoalNodeIn.text(),graph); print('\nCost:', cost)

        if algoType == "A star":
            traced_path, cost = self.a_star_search(self.SetStartNodeIn.text(), self.SetGoalNodeIn.text(), graph)
            if (traced_path): print('Path:', end=' '); self.print_path(traced_path, self.SetGoalNodeIn.text(),graph); print('\nCost:', cost)

    def breadth_first_search(self, start, goal, graph):
        found, fringe, visited, came_from = False, deque([start]), set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))
        traversal = []
        while not found and len(fringe):
            current = fringe.pop()
            # traversal.append(current)
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in graph.neighbors(current):
                if node not in visited: visited.add(node); fringe.appendleft(node); came_from[node] = current
            print(', '.join(fringe))
        if found:
            print();
            return came_from
        else:
            print('No path from {} to {}'.format(start, goal))
            return

    def depth_first_search(self, start, goal, graph):
        found, fringe, visited, came_from = False, deque([start]), set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))
        while not found and len(fringe):
            current = fringe.pop()
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in graph.neighbors(current):
                if node not in visited: visited.add(node); fringe.append(node); came_from[node] = current
            print(', '.join(fringe))
        if found:
            print();
            return came_from
        else:
            print('No path from {} to {}'.format(start, goal))

    def iterative_deepening_dfs(self, start, goal, graph):
        prev_iter_visited, depth = [], 0
        while True:
            traced_path, visited = self.depth_limited_searc(start, goal, graph, depth)
            if traced_path or len(visited) == len(prev_iter_visited):
                return traced_path
            else:
                prev_iter_visited = visited;
                depth += 1

    def depth_limited_searc(self, start, goal, graph, limit=-1):
        print('Depth limit =', limit)
        found, fringe, visited, came_from = False, deque([(0, start)]), set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))
        while not found and len(fringe):
            depth, current = fringe.pop()
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            if limit == -1 or depth < limit:
                for node in graph.neighbors(current):
                    if node not in visited:
                        visited.add(node);
                        fringe.append((depth + 1, node))
                        came_from[node] = current
            print(', '.join([n for _, n in fringe]))
        if found:
            print();
            return came_from, visited
        else:
            print('No path from {} to {}'.format(start, goal));
            return None, visited

    def depth_limited_search(self, start, goal, graph, limit):
        print('Depth limit =', limit)
        found, fringe, visited, came_from = False, deque([(0, start)]), set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))
        while not found and len(fringe):
            depth, current = fringe.pop()
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            if limit == -1 or depth < limit:
                for node in graph.neighbors(current):
                    if node not in visited:
                        visited.add(node);
                        fringe.append((depth + 1, node))
                        came_from[node] = current
            print(', '.join([n for _, n in fringe]))
        if found:
            print();
            return came_from
        else:
            print('No path from {} to {}'.format(start, goal))
            return

    def uniform_cost_search(self, start, goal, graph):
        found, fringe, visited, came_from, cost_so_far = False, [(0, start)], set([start]), {start: None}, {start: 0}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', str((0, start))))
        while not found and len(fringe):
            _, current = heappop(fringe)
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in graph.neighbors(current):
                new_cost = cost_so_far[current] + nx.path_weight(graph, [current, node], "weight")
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node);
                    came_from[node] = current;
                    cost_so_far[node] = new_cost
                    heappush(fringe, (new_cost, node))
            print(', '.join([str(n) for n in fringe]))
        if found:
            print();
            return came_from, cost_so_far[goal]
        else:
            print('No path from {} to {}'.format(start, goal));
            return None, inf

    def greedy_search(self, start, goal, graph):
        H=nx.get_node_attributes(graph,'H')
        found, fringe, visited, came_from, cost_so_far = False, [(H[start], start)], set([start]), {start: None}, {start: 0}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', str(fringe[0])))
        while not found and len(fringe):
            _, current = heappop(fringe)
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in graph.neighbors(current):
                new_cost = cost_so_far[current] + nx.path_weight(graph, [current, node], "weight")
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node);
                    came_from[node] = current;
                    cost_so_far[node] = new_cost
                    heappush(fringe, (H[node], node))
            print(', '.join([str(n) for n in fringe]))
        if found:
            print(); return came_from, cost_so_far[goal]
        else:
            print('No path from {} to {}'.format(start, goal)); return None, inf

    def a_star_search(self,start, goal, graph):
        H=nx.get_node_attributes(graph,'H')
        found, fringe, visited, came_from, cost_so_far = False, [(H[start], start)], set([start]), {
            start: None}, {start: 0}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', str(fringe[0])))
        while not found and len(fringe):
            _, current = heappop(fringe)
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in graph.neighbors(current):
                new_cost = cost_so_far[current] + nx.path_weight(graph, [current, node], "weight")
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node);
                    came_from[node] = current;
                    cost_so_far[node] = new_cost
                    heappush(fringe, (new_cost + float(H[node]), node))  # heappush(fringe, (new_cost + H[node], node)
            print(', '.join([str(n) for n in fringe]))
        if found:
            print();
            return came_from, cost_so_far[goal]
        else:
            print('No path from {} to {}'.format(start, goal));
            return None, inf

    def print_path(self, came_from, goal, graph):

        parent = came_from[goal]
        if parent:

            self.print_path(came_from, parent, graph)
        else:
            print(goal, end='');
            return

        print(' =>', goal, end='')

    def dfs(self, theGraph, node, visited):
        # visited = set()
        print(graph)
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in graph[node]:
                self.dfs(theGraph, neighbour, visited)




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FirstWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())