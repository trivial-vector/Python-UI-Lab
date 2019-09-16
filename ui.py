# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_template.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 325)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(640, 325))
        MainWindow.setMaximumSize(QtCore.QSize(640, 325))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 2, 1)
        self.activitiesDone = QtWidgets.QListView(self.centralwidget)
        self.activitiesDone.setObjectName("activitiesDone")
        self.gridLayout.addWidget(self.activitiesDone, 1, 6, 8, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 6, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.lessonProgress = QtWidgets.QProgressBar(self.centralwidget)
        self.lessonProgress.setProperty("value", 0)
        self.lessonProgress.setObjectName("lessonProgress")
        self.gridLayout.addWidget(self.lessonProgress, 10, 0, 1, 7)
        self.pushActivity = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushActivity.sizePolicy().hasHeightForWidth())
        self.pushActivity.setSizePolicy(sizePolicy)
        self.pushActivity.setObjectName("pushActivity")
        self.gridLayout.addWidget(self.pushActivity, 10, 8, 1, 1)
        self.activityList = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.activityList.sizePolicy().hasHeightForWidth())
        self.activityList.setSizePolicy(sizePolicy)
        self.activityList.setMinimumSize(QtCore.QSize(300, 30))
        self.activityList.setMaximumSize(QtCore.QSize(600, 30))
        self.activityList.setObjectName("activityList")
        self.gridLayout.addWidget(self.activityList, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 9, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 10, 7, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 10, 9, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)
        self.lessonList = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lessonList.sizePolicy().hasHeightForWidth())
        self.lessonList.setSizePolicy(sizePolicy)
        self.lessonList.setMinimumSize(QtCore.QSize(300, 30))
        self.lessonList.setMaximumSize(QtCore.QSize(600, 30))
        self.lessonList.setObjectName("lessonList")
        self.gridLayout.addWidget(self.lessonList, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem4, 7, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 4, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 4, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 5, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 5, 4, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 4, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 5, 3, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 4, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 10, 10, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Settings = QtWidgets.QMenu(self.menubar)
        self.menu_Settings.setObjectName("menu_Settings")
        self.menu_Weekly_Setup_Format = QtWidgets.QMenu(self.menu_Settings)
        self.setup_group = QtWidgets.QActionGroup(
            self.menu_Weekly_Setup_Format)
        self.menu_Weekly_Setup_Format.setGeometry(
            QtCore.QRect(1134, 195, 135, 90))
        self.menu_Weekly_Setup_Format.setObjectName("menu_Weekly_Setup_Format")
        self.menu_Commit_Msg = QtWidgets.QMenu(self.menu_Settings)
        self.menu_Commit_Msg.setObjectName("menu_Commit_Msg")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Set_Lesson_Plans = QtWidgets.QAction(MainWindow)
        self.action_Set_Lesson_Plans.setCheckable(True)
        self.action_Set_Lesson_Plans.setObjectName("action_Set_Lesson_Plans")
        self.action_Set_Class_Repo = QtWidgets.QAction(MainWindow)
        self.action_Set_Class_Repo.setCheckable(True)
        self.action_Set_Class_Repo.setObjectName("action_Set_Class_Repo")
        self.action_Dark_Mode = QtWidgets.QAction(MainWindow)
        self.action_Dark_Mode.setCheckable(True)
        self.action_Dark_Mode.setObjectName("action_Dark_Mode")
        self.actionOne_Activity = QtWidgets.QAction(MainWindow)
        self.actionOne_Activity.setCheckable(True)
        self.actionOne_Activity.setObjectName("actionOne_Activity")
        self.actionAll_Unsolved = QtWidgets.QAction(MainWindow)
        self.actionAll_Unsolved.setCheckable(True)
        self.actionAll_Unsolved.setObjectName("actionAll_Unsolved")
        self.actionLesson_Name_Solved = QtWidgets.QAction(MainWindow)
        self.actionLesson_Name_Solved.setCheckable(True)
        self.actionLesson_Name_Solved.setObjectName("actionLesson_Name_Solved")
        self.action00_Solved = QtWidgets.QAction(MainWindow)
        self.action00_Solved.setCheckable(True)
        self.action00_Solved.setObjectName("action00_Solved")
        self.action00_Lesson_name_Solved = QtWidgets.QAction(MainWindow)
        self.action00_Lesson_name_Solved.setCheckable(True)
        self.action00_Lesson_name_Solved.setObjectName(
            "action00_Lesson_name_Solved")
        self.menu_File.addAction(self.action_Set_Lesson_Plans)
        self.menu_File.addAction(self.action_Set_Class_Repo)
        self.menu_Weekly_Setup_Format.addAction(self.actionOne_Activity)
        self.menu_Weekly_Setup_Format.addAction(self.actionAll_Unsolved)
        self.setup_group.addAction(self.actionOne_Activity)
        self.setup_group.addAction(self.actionAll_Unsolved)
        self.setup_group.setExclusive(True)
        self.commit_group = QtWidgets.QActionGroup(self.menu_Commit_Msg)
        self.commit_group.setExclusive(True)
        self.menu_Commit_Msg.addAction(self.actionLesson_Name_Solved)
        self.menu_Commit_Msg.addAction(self.action00_Solved)
        self.menu_Commit_Msg.addAction(self.action00_Lesson_name_Solved)
        self.commit_group.addAction(self.actionLesson_Name_Solved)
        self.commit_group.addAction(self.action00_Solved)
        self.commit_group.addAction(self.action00_Lesson_name_Solved)
        self.menu_Settings.addAction(
            self.menu_Weekly_Setup_Format.menuAction())
        self.menu_Settings.addAction(self.menu_Commit_Msg.menuAction())
        self.menu_Settings.addSeparator()
        self.menu_Settings.addAction(self.action_Dark_Mode)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Settings.menuAction())

        self.retranslateUi(MainWindow)
        self.pushActivity.clicked.connect(self.activitiesDone.update)
        self.pushActivity.clicked.connect(self.lessonProgress.update)
        self.pushActivity.clicked.connect(self.activityList.update)
        self.lessonList.currentIndexChanged['int'].connect(
            self.activityList.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "TA Toolbox - Class Helper"))
        self.label_2.setText(_translate("MainWindow", "Lesson:"))
        self.label_3.setText(_translate("MainWindow", "Pushed Activities:"))
        self.label_5.setText(_translate("MainWindow", "Day:"))
        self.pushActivity.setText(_translate("MainWindow", "Push Activity"))
        self.label.setText(_translate("MainWindow", "Activity:"))
        self.label_4.setText(_translate("MainWindow", "Lesson Progress:"))
        self.radioButton_2.setText(_translate("MainWindow", "2"))
        self.radioButton.setText(_translate("MainWindow", "1"))
        self.radioButton_3.setText(_translate("MainWindow", "3"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Settings.setTitle(_translate("MainWindow", "&Settings"))
        self.menu_Weekly_Setup_Format.setTitle(
            _translate("MainWindow", "&Push Style"))
        self.menu_Commit_Msg.setTitle(_translate("MainWindow", "&Commit Msg"))
        self.action_Set_Lesson_Plans.setText(
            _translate("MainWindow", "Set Lesson Plans"))
        self.action_Set_Class_Repo.setText(
            _translate("MainWindow", "Set Class Repo"))
        self.action_Set_Class_Repo.setStatusTip(_translate(
            "MainWindow", "Set a location for the class repository"))
        self.action_Dark_Mode.setText(_translate("MainWindow", "&Dark Mode"))
        self.actionOne_Activity.setText(
            _translate("MainWindow", "One Activity"))
        self.actionAll_Unsolved.setText(
            _translate("MainWindow", "All Unsolved"))
        self.actionLesson_Name_Solved.setText(
            _translate("MainWindow", "Lesson_Name - Solved"))
        self.action00_Solved.setText(_translate("MainWindow", "00 - Solved"))
        self.action00_Lesson_name_Solved.setText(
            _translate("MainWindow", "00-Lesson_name - Solved"))
