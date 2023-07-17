# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from Find import Ui_Dialog
import Function
from PyQt5 import  uic
from PyQt5.QtCore import QModelIndex
import os
from PyQt5.QtWidgets import QFileSystemModel, QTableWidgetItem, QTreeWidgetItem
from PyQt5.QtWidgets import QFileDialog
from threading import Thread
from FunctionAndVariableDetection.DirectoryTree import directory_tree
from Tools.DatabaseOperation import SQL
from PyQt5.QtCore import  QRegExp
from PyQt5.QtGui import  QFont, QSyntaxHighlighter
from FunctionManagement import CMD

from PyQt5.QtGui import QTextCharFormat, QColor

class UI(Ui_Dialog):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('Find.ui', self)

class fu_ui(Function.Ui_Dialog):
    def __init__(self):
        super(fu_ui, self).__init__()
        uic.loadUi('Function.ui', self)

def count_lines(file_path):
    line_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
    return line_count

def calculate_risk_level(line_count):
    # 根据行数确定风险水平
    if line_count <= 100:
        return 'Low'
    elif line_count <= 500:
        return 'Medium'
    else:
        return 'High'

from PyQt5 import QtCore, QtGui, QtWidgets


class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super().__init__(parent)
        self.highlighting_rules = []

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Code_Audit")
        MainWindow.resize(1294, 710)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 351, 681))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeView = QtWidgets.QTreeView(self.horizontalLayoutWidget)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(900, 0, 401, 681))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeWidget_1 = QtWidgets.QTreeWidget(self.horizontalLayoutWidget_2)
        self.treeWidget_1.setStyleSheet("QTreeView::branch:closed:has-children\n"
                                        "{\n"
                                        "    image: url(./resource/icon/expand-positive.png);/*图标*/\n"
                                        "    border-image: none;\n"
                                        "}\n"
                                        "\n"
                                        "QTreeView::branch:open:has-children\n"
                                        "{\n"
                                        "    image: url(./resource/icon/shrink-positive.png);/*图标*/\n"
                                        "    border-image: none;\n"
                                        "}")
        self.treeWidget_1.setObjectName("treeWidget_1")
        self.treeWidget_1.header().setDefaultSectionSize(110)
        self.treeWidget_1.header().setHighlightSections(False)
        self.treeWidget_1.header().setMinimumSectionSize(30)
        self.horizontalLayout_2.addWidget(self.treeWidget_1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 0, 551, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(349, 449, 551, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.verticalLayoutWidget_2)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.tab_2.setFont(font)
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1294, 23))
        self.menubar.setObjectName("menubar")
        self.File = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.File.setFont(font)
        self.File.setObjectName("File")
        self.Edit = QtWidgets.QMenu(self.menubar)
        self.Edit.setObjectName("Edit")
        self.Window = QtWidgets.QMenu(self.menubar)
        self.Window.setObjectName("Window")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.New = QtWidgets.QAction(MainWindow)
        self.New.setObjectName("New")
        self.Open = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.Open.setFont(font)
        self.Open.setObjectName("Open")
        self.Opendir = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.Opendir.setFont(font)
        self.Opendir.setObjectName("Opendir")
        self.Save = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.Save.setFont(font)
        self.Save.setObjectName("Save")
        self.Saveas = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.Saveas.setFont(font)
        self.Saveas.setObjectName("Saveas")
        self.Undo = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.Undo.setFont(font)
        self.Undo.setObjectName("Undo")
        self.Copy = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.Copy.setFont(font)
        self.Copy.setObjectName("Copy")
        self.Cut = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.Cut.setFont(font)
        self.Cut.setObjectName("Cut")
        self.Paste = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.Paste.setFont(font)
        self.Paste.setObjectName("Paste")
        self.Function = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.Function.setFont(font)
        self.Function.setObjectName("Function")
        self.Find = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.Find.setFont(font)
        self.Find.setObjectName("Find")
        self.Goto = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.Goto.setFont(font)
        self.Goto.setObjectName("Goto")
        self.Close = QtWidgets.QAction(MainWindow)
        self.Close.setObjectName("Close")
        self.Closeall = QtWidgets.QAction(MainWindow)
        self.Closeall.setObjectName("Closeall")
        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setObjectName("Exit")
        self.Pie = QtWidgets.QAction(MainWindow)
        self.Pie.setObjectName("Pie")
        self.Compile = QtWidgets.QAction(MainWindow)
        self.Compile.setObjectName("Compile")
        self.Run = QtWidgets.QAction(MainWindow)
        self.Run.setObjectName("Run")
        self.CMD = QtWidgets.QAction(MainWindow)
        self.CMD.setObjectName("CMD")
        self.File.addAction(self.Open)
        self.File.addAction(self.Save)
        self.File.addAction(self.Saveas)
        self.File.addSeparator()
        self.File.addAction(self.Close)
        self.File.addAction(self.Closeall)
        self.File.addAction(self.Exit)
        self.Edit.addAction(self.Undo)
        self.Edit.addAction(self.Copy)
        self.Edit.addAction(self.Cut)
        self.Edit.addAction(self.Paste)
        self.Edit.addAction(self.Goto)
        self.Window.addAction(self.Function)
        self.Window.addAction(self.Find)
        self.Window.addAction(self.Pie)
        self.Window.addAction(self.CMD)
        self.menu.addAction(self.Compile)
        self.menu.addAction(self.Run)
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Edit.menuAction())
        self.menubar.addAction(self.Window.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(1)
        self.Open.triggered.connect(self.open_directory)  # type: ignore
        self.Find.triggered.connect(self.find_qa)
        self.Function.triggered.connect(self.function_qa)
        self.Pie.triggered.connect(self.pie_qa)
        self.CMD.triggered.connect(self.cmd_qa)
        self.Compile.triggered.connect(self.complie_qa)
        self.Run.triggered.connect(self.run_qa)
        self.Undo.triggered.connect(self.undo_qa)
        self.Copy.triggered.connect(self.copy_qa)
        self.Cut.triggered.connect(self.cut_qa)
        self.Paste.triggered.connect(self.paste_qa)
        self.Goto.triggered.connect(self.goto_qa)
        self.Save.triggered.connect(self.save_qa)
        self.Saveas.triggered.connect(self.saveas_qa)
        self.Close.triggered.connect(self.close_qa)
        self.Closeall.triggered.connect(self.colseall_qa)
        self.Exit.triggered.connect(self.exit_qa)
        self.treeView.clicked['QModelIndex'].connect(self.on_tree_item_clicked)  # type: ignore
        self.treeWidget_1.clicked['QModelIndex'].connect(self.variable_choose)  # type: ignore
        self.pushButton.clicked.connect(self.run_cmd)  # type: ignore
        self.treeWidget_1.clicked['QModelIndex'].connect(self.right_tree_clicked)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget_1.headerItem().setText(0, _translate("MainWindow", "函数ID"))
        self.treeWidget_1.headerItem().setText(1, _translate("MainWindow", "函数和变量"))
        self.treeWidget_1.headerItem().setText(2, _translate("MainWindow", "类型"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "文件名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "行数"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "风险等级"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "解决方法"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "输出"))
        self.pushButton.setText(_translate("MainWindow", "执行"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "终端"))
        self.File.setTitle(_translate("MainWindow", "文件"))
        self.Edit.setTitle(_translate("MainWindow", "编辑"))
        self.Window.setTitle(_translate("MainWindow", "窗口"))
        self.menu.setTitle(_translate("MainWindow", "调试"))
        self.New.setText(_translate("MainWindow", "新建"))
        self.New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.Open.setText(_translate("MainWindow", "打开文件"))
        self.Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.Opendir.setText(_translate("MainWindow", "打开文件夹"))
        self.Opendir.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.Save.setText(_translate("MainWindow", "保存"))
        self.Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.Saveas.setText(_translate("MainWindow", "另存为"))
        self.Saveas.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.Undo.setText(_translate("MainWindow", "撤销"))
        self.Undo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.Copy.setText(_translate("MainWindow", "复制"))
        self.Copy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.Cut.setText(_translate("MainWindow", "剪切"))
        self.Cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.Paste.setText(_translate("MainWindow", "粘贴"))
        self.Paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.Function.setText(_translate("MainWindow", "风险函数管理"))
        self.Find.setText(_translate("MainWindow", "查找和替换"))
        self.Find.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.Goto.setText(_translate("MainWindow", "转到定义"))
        self.Close.setText(_translate("MainWindow", "关闭标签"))
        self.Closeall.setText(_translate("MainWindow", "关闭所有标签"))
        self.Exit.setText(_translate("MainWindow", "退出"))
        self.Pie.setText(_translate("MainWindow", "生成饼状图"))
        self.Compile.setText(_translate("MainWindow", "编译"))
        self.Run.setText(_translate("MainWindow", "运行"))
        self.CMD.setText(_translate("MainWindow", "终端"))

    def open_directory(self):
        self.file_choosed_flag = False
        folderDialog = QFileDialog.getExistingDirectory(self, '打开文件夹')
        self.lines = 0
        if folderDialog:
            # 获取选中的文件夹路径
            self.folderPath = folderDialog
            #清空function_tree和scan_function表

            # 进行函数检测
            directory_tree1 = directory_tree(folderDialog)
            mysql = SQL()
            # functions=process_c_files(directory_tree1,folderDialog)
            # #扫描函数，并填入scan_function表
            # for function in functions:
            #     print(mysql.insert_scan_function(mysql.cnx, mysql.cursor, function))
            # mysql.close_SQL(mysql.cursor, mysql.cnx)
            # #构建函数关系树，填入function_tree
            # return_preandsub()
            # mysql = SQL()
            ss = mysql.select_scan_function(mysql.cursor)
            self.treeWidget_1.clear()  # 清空所有元素
            for function in ss:
                try:
                    item = QTreeWidgetItem()
                    item.setText(0, str(function['id']))
                    item.setText(1, function['function'] + ';' + function['parameter'])
                    item.setText(2, function['return_type'])
                    # item.setText(1, function['path'])
                    self.treeWidget_1.addTopLevelItem(item)
                except Exception as e:
                    print("发生异常:", str(e))
            mysql.close_SQL(mysql.cursor, mysql.cnx)
            try:
                self.thread1 = Thread(target=self.generate_tree)
                self.thread1.start()
            except Exception as e:
                print("发生异常:", str(e))



    def generate_tree(self):
        model = QFileSystemModel()
        model.setRootPath(self.folderPath)
        model.setNameFilters(['*.c'])
        self.treeView.setModel(model)

        # 设置 QTreeView 的根索引为项目根目录
        root_index = model.setRootPath(self.folderPath)
        self.treeView.setRootIndex(root_index)
        parent_path = model.filePath(root_index)
        for name in os.listdir(parent_path):
            path = os.path.join(parent_path, name)
            after_name = path.split(".",path.count("."))[-1]
            if after_name != "c":
                continue
            index = model.index(path)
            if os.path.isdir(path):
                self.file_system_model = model
                self.populate_directory_tree(index)
            else:
                self.tableWidget.setRowCount(self.lines+1)
                self.tableWidget.setItem(self.lines,0,QTableWidgetItem(name))
                self.tableWidget.setItem(self.lines,1,QTableWidgetItem(str(count_lines(path))))
                self.tableWidget.setItem(self.lines,2,QTableWidgetItem(calculate_risk_level(count_lines(path))))
                self.lines = self.lines + 1

    def populate_directory_tree(self, parent_index):
            parent_path = self.file_system_model.filePath(parent_index)
            for name in os.listdir(parent_path):
                    path = os.path.join(parent_path, name)
                    index = self.file_system_model.index(path)
                    if os.path.isdir(path):
                            self.populate_directory_tree(index)
                    else:
                        self.tableWidget.setRowCount(self.lines + 1)
                        self.tableWidget.setItem(self.lines, 0, QTableWidgetItem(name))
                        self.tableWidget.setItem(self.lines, 1, QTableWidgetItem(str(count_lines(path))))
                        self.tableWidget.setItem(self.lines, 2,   QTableWidgetItem(calculate_risk_level(count_lines(path))))
                        self.lines = self.lines+1

    def right_tree_clicked(self, index: QModelIndex):
        if self.file_choosed_flag == False:
            return
        selected_item = self.treeWidget_1.itemFromIndex(index)

        if selected_item.parent() is not None or selected_item.childCount() > 0 :
            # 选中的是子条目
            var_id = int(selected_item.text(0)) - 1
            mysql = SQL()
            ss = mysql.select_value_of_function(mysql.cursor)
            # ss2 = mysql.select_scan_function(mysql.cursor)
            # function_id = ss[var_id][0]
            format = QTextCharFormat()
            format.setForeground(QColor("red"))
            current_text = self.textBrowser.toPlainText()
            #self.textBrowser.clear()
            for item in ss[var_id][1]:
                if selected_item.text(1) == item[0]:
                    for pos in item[2]:
                        pos_split = pos.split("-")
                        num = mysql.select_start_by_id(mysql.cursor, ss[var_id][0])[0]
                        f_place = int(num[0])-1
                        row = int(pos_split[0])
                        row += f_place
                        column = int(pos_split[1])
                        len_var = len(item[0])
                        highlighted_content = self.highlight_str(current_text, row, column, len_var)
                        self.textBrowser.setText(highlighted_content)
            mysql.close_SQL(mysql.cursor, mysql.cnx)
        else:
            return


    def highlight_str(self, content, row, column, length):
        lines = content.split('\n')
        highlighted_lines = []
        for i, line in enumerate(lines, start=1):
            if i == row:
                highlighted_line = ""
                for j, char in enumerate(line, start=1):
                    if column <= j < column + length:
                        highlighted_line += f"<span class='highlight' style='background-color: red;'>{char}</span>"
                    else:
                        highlighted_line += char
                highlighted_lines.append(highlighted_line)
            else:
                highlighted_lines.append(line)
        highlighted_content = "<pre>" + "\n".join(highlighted_lines) + "</pre>"
        return highlighted_content

    def on_tree_item_clicked(self, index: QModelIndex):
        self.file_choosed_flag = True
        file_path = self.treeView.model().filePath(index)
        if not file_path:
                return

        try:
                with open(file_path, 'r') as file:
                        file_content = file.read()
                        self.setFont(QFont("Courier New", 10))
                        self.textBrowser.setPlainText(file_content)
                mysql = SQL()
                ss = mysql.select_scan_function(mysql.cursor)
                self.treeWidget_1.clear()  # 清空所有元素
                self.treeWidget_1.setColumnWidth(0, 300)
                file = QTreeWidgetItem(self.treeWidget_1)
                file.setText(0, "文件名：" + file_path)
                fun = QTreeWidgetItem(self.treeWidget_1)
                for function in ss:
                    if(function['belong_file']==file_path):
                        try:
                            func_id=function['id']
                            child = QTreeWidgetItem(fun)
                            child.setText(0,str(func_id))
                            child.setText(1, function['function'])
                            child.setText(2, function['return_type'])
                            mysql.close_SQL(mysql.cursor, mysql.cnx)
                            mysql = SQL()
                            vallists = mysql.select_value_of_function(mysql.cursor)
                            for valitem in vallists:
                                # print(type(valitem))
                                # print(valitem)
                                if int(valitem[0])==int(func_id):
                                    for val in valitem[1]:
                                        child1 = QTreeWidgetItem(child)
                                        child1.setText(0,str(func_id))
                                        child1.setText(1, val[0])
                                        child1.setText(2, val[1])
                        except Exception as e:
                            print("发生异常:", str(e))
                self.treeWidget_1.expandAll()

        except IOError as e:
                print('无法打开文件:', e)

    def variable_choose(self,item):
        if self.file_choosed_flag == True:
            return
        clicked_item = self.treeWidget_1.itemFromIndex(item)
        item = clicked_item.text(0)
        print(item)
        mysql = SQL()
        ss = mysql.select_scan_function(mysql.cursor)
        for function in ss:
            if function['id'] == int(item):
                path = function['belong_file']
                begin = function['start']
                end = function['end']
                with open(path, "r") as file_read:
                    content = file_read.read()
                    highlighted_content = self.highlight_code(content, begin, end)
                    self.textBrowser.setText(highlighted_content)
                file_read.close()  # 关闭文件资源
                break


    def highlight_code(self, content, begin, end):
        lines = content.split('\n')
        highlighted_lines = []
        for i, line in enumerate(lines, start=1):
            if begin <= i <= end:
                highlighted_lines.append(f"<span class='highlight' style='background-color: red;'>{line}</span>")
            else:
                highlighted_lines.append(f"<span class='normal'>{line}</span>")
        highlighted_content = "<pre>" + "\n".join(highlighted_lines) + "</pre>"
        return highlighted_content

    def format_line(self, line, format):
        return f"<span style='color:{format.foreground().color().name()};background-color:{format.background().color().name()}'>{line}</span>"


    def run_cmd(self):
        command = self.lineEdit.text()
        result = CMD.run_cmd(command)
        self.textEdit_2.append(result)

    def function_qa(self):
        self.function_window = fu_ui()
        self.function_window.show()

    def find_qa(self):
        self.find_window = UI()
        self.find_window.show()

    def cmd_qa(self):
        print('CMD')
        pass

    def pie_qa(self):
        print('Pie')
        pass

    def complie_qa(self):
        print('Compile')
        pass
    def run_qa(self):
        print('Run')
        pass

    def undo_qa(self):
        print('Undo')
        pass

    def copy_qa(self):
        print('Copy')
        pass

    def cut_qa(self):
        print('Cut')
        pass
    def paste_qa(self):
        print('Paste')
        pass

    def goto_qa(self):
        print('Goto')
        pass

    def save_qa(self):
        print('Save')
        pass
    def saveas_qa(self):
        print('Saveas')
        pass
    def close_qa(self):
        print('Close')
        pass
    def colseall_qa(self):
        print('Closeall')
        pass
    def exit_qa(self):
        print('Exit')
        pass