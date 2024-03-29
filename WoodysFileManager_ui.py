# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WoodysFileManager.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1277, 689)
        MainWindow.setMinimumSize(QSize(1277, 689))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(43, 60, 80, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(64, 90, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(53, 75, 100, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(21, 30, 40, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 40, 53, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(84, 159, 176, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush9 = QBrush(QColor(255, 255, 255, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush10 = QBrush(QColor(21, 30, 40, 127))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush7)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, 0, 0, 0)
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(22, 22))
        self.label_2.setMaximumSize(QSize(22, 22))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u":/images/icon/woody-the-dev.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	padding-left: 6px;\n"
"	color: white;\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.windowMinimizeButton = QPushButton(self.frame_9)
        self.windowMinimizeButton.setObjectName(u"windowMinimizeButton")
        self.windowMinimizeButton.setMinimumSize(QSize(48, 32))
        self.windowMinimizeButton.setMaximumSize(QSize(48, 32))
        self.windowMinimizeButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(84,159,176,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(84,159,176,0.5);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/icon/window-minimize-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.windowMinimizeButton.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.windowMinimizeButton)

        self.windowCloseButton = QPushButton(self.frame_9)
        self.windowCloseButton.setObjectName(u"windowCloseButton")
        self.windowCloseButton.setMinimumSize(QSize(48, 32))
        self.windowCloseButton.setMaximumSize(QSize(48, 32))
        self.windowCloseButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(84,159,176,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(208,55,36);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/icon/xmark-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.windowCloseButton.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.windowCloseButton)

        self.windowCloseButton.raise_()
        self.windowMinimizeButton.raise_()
        self.label_3.raise_()
        self.label_2.raise_()

        self.verticalLayout_11.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 0, 6, 6)
        self.frame = QFrame(self.frame_8)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(92, 240))
        self.frame.setMaximumSize(QSize(92, 16777215))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.overviewButton = QPushButton(self.frame)
        self.overviewButton.setObjectName(u"overviewButton")
        self.overviewButton.setMinimumSize(QSize(92, 120))
        self.overviewButton.setMaximumSize(QSize(92, 120))
        self.overviewButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.overviewButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(84,159,176,0);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	padding-right: 3px;\n"
"	border-left: 3px solid rgb(84, 159, 176);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(84,159,176,0.5);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/images/icon/file-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.overviewButton.setIcon(icon2)
        self.overviewButton.setIconSize(QSize(48, 48))

        self.verticalLayout_15.addWidget(self.overviewButton)

        self.unsortOverviewButton = QPushButton(self.frame)
        self.unsortOverviewButton.setObjectName(u"unsortOverviewButton")
        self.unsortOverviewButton.setMinimumSize(QSize(92, 120))
        self.unsortOverviewButton.setMaximumSize(QSize(92, 120))
        self.unsortOverviewButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.unsortOverviewButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(84,159,176,0);\n"
"	border-radius: 0px;\n"
"	padding-right: 0px;\n"
"	border-left: 0px solid rgb(84, 159, 176);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(84,159,176,0.5);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/images/icon/file-arrow-up-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.unsortOverviewButton.setIcon(icon3)
        self.unsortOverviewButton.setIconSize(QSize(48, 48))

        self.verticalLayout_15.addWidget(self.unsortOverviewButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_4)


        self.horizontalLayout_4.addWidget(self.frame)

        self.mainStackedWidget = QStackedWidget(self.frame_8)
        self.mainStackedWidget.setObjectName(u"mainStackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainStackedWidget.sizePolicy().hasHeightForWidth())
        self.mainStackedWidget.setSizePolicy(sizePolicy1)
        self.mainStackedWidget.setMinimumSize(QSize(506, 0))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy1.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(460, 0))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(454, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 32))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.searchLineEdit = QLineEdit(self.frame_6)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setMinimumSize(QSize(0, 32))
        self.searchLineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(244,244,244);\n"
"	border-radius: 0px;\n"
"	padding-left: 16px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.searchLineEdit)

        self.searchButton = QPushButton(self.frame_6)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMinimumSize(QSize(32, 32))
        self.searchButton.setMaximumSize(QSize(32, 32))
        self.searchButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(244,244,244);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: red;\n"
"	background-color: rgba(84,159,176,0.5);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/images/icon/magnifying-glass-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon4)
        self.searchButton.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.searchButton)


        self.verticalLayout_3.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.displayFilesTableWidget = QTableWidget(self.frame_4)
        if (self.displayFilesTableWidget.columnCount() < 4):
            self.displayFilesTableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.displayFilesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.displayFilesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.displayFilesTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.displayFilesTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.displayFilesTableWidget.setObjectName(u"displayFilesTableWidget")
        self.displayFilesTableWidget.setMinimumSize(QSize(845, 584))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush7)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette1.setBrush(QPalette.Active, QPalette.Accent, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Accent, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Accent, brush7)
        self.displayFilesTableWidget.setPalette(palette1)
        self.displayFilesTableWidget.setStyleSheet(u"")
        self.displayFilesTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.displayFilesTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.displayFilesTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.displayFilesTableWidget.setSortingEnabled(True)
        self.displayFilesTableWidget.setRowCount(0)
        self.displayFilesTableWidget.horizontalHeader().setMinimumSectionSize(95)
        self.displayFilesTableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.displayFilesTableWidget.horizontalHeader().setHighlightSections(False)
        self.displayFilesTableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.displayFilesTableWidget.horizontalHeader().setStretchLastSection(True)
        self.displayFilesTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.displayFilesTableWidget)


        self.horizontalLayout.addWidget(self.frame_4)

        self.mainStackedWidget.addWidget(self.page)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        sizePolicy1.setHeightForWidth(self.page_5.sizePolicy().hasHeightForWidth())
        self.page_5.setSizePolicy(sizePolicy1)
        self.horizontalLayout_7 = QHBoxLayout(self.page_5)
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.page_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(460, 0))
        self.frame_10.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_5 = QSpacerItem(20, 367, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color: rgb(84, 159, 176)\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)


        self.horizontalLayout_7.addWidget(self.frame_10)

        self.mainStackedWidget.addWidget(self.page_5)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        sizePolicy1.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(460, 0))
        self.frame_5.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.unsortTitle = QLabel(self.frame_5)
        self.unsortTitle.setObjectName(u"unsortTitle")
        font2 = QFont()
        font2.setFamilies([u"Lucida Bright"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.unsortTitle.setFont(font2)
        self.unsortTitle.setStyleSheet(u"QLabel {\n"
"	color: rgb(84, 159, 176)\n"
"}")

        self.verticalLayout.addWidget(self.unsortTitle)

        self.unsortedFilesTableWidget = QTableWidget(self.frame_5)
        if (self.unsortedFilesTableWidget.columnCount() < 4):
            self.unsortedFilesTableWidget.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.unsortedFilesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.unsortedFilesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.unsortedFilesTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.unsortedFilesTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.unsortedFilesTableWidget.setObjectName(u"unsortedFilesTableWidget")
        self.unsortedFilesTableWidget.setMinimumSize(QSize(845, 584))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush7)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Active, QPalette.Accent, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Accent, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Accent, brush7)
        self.unsortedFilesTableWidget.setPalette(palette2)
        self.unsortedFilesTableWidget.setStyleSheet(u"")
        self.unsortedFilesTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.unsortedFilesTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.unsortedFilesTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.unsortedFilesTableWidget.setSortingEnabled(True)
        self.unsortedFilesTableWidget.setRowCount(0)
        self.unsortedFilesTableWidget.horizontalHeader().setMinimumSectionSize(95)
        self.unsortedFilesTableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.unsortedFilesTableWidget.horizontalHeader().setHighlightSections(False)
        self.unsortedFilesTableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.unsortedFilesTableWidget.horizontalHeader().setStretchLastSection(True)
        self.unsortedFilesTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.unsortedFilesTableWidget)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.mainStackedWidget.addWidget(self.page_2)

        self.horizontalLayout_4.addWidget(self.mainStackedWidget)

        self.supportStackedWidget = QStackedWidget(self.frame_8)
        self.supportStackedWidget.setObjectName(u"supportStackedWidget")
        self.supportStackedWidget.setMinimumSize(QSize(290, 0))
        self.supportStackedWidget.setMaximumSize(QSize(290, 16777215))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(290, 0))
        self.frame_2.setMaximumSize(QSize(275, 16777215))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.categoryTitle = QLabel(self.widget)
        self.categoryTitle.setObjectName(u"categoryTitle")
        self.categoryTitle.setFont(font2)
        self.categoryTitle.setStyleSheet(u"QLabel {\n"
"	color: rgb(84, 159, 176)\n"
"}")

        self.horizontalLayout_5.addWidget(self.categoryTitle)

        self.exactPathCheckBox = QCheckBox(self.widget)
        self.exactPathCheckBox.setObjectName(u"exactPathCheckBox")
        self.exactPathCheckBox.setTristate(False)

        self.horizontalLayout_5.addWidget(self.exactPathCheckBox)


        self.verticalLayout_2.addWidget(self.widget)

        self.categoryTreeWidget = QTreeWidget(self.frame_2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.categoryTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.categoryTreeWidget.setObjectName(u"categoryTreeWidget")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.categoryTreeWidget.setPalette(palette3)
        font3 = QFont()
        font3.setPointSize(12)
        self.categoryTreeWidget.setFont(font3)
        self.categoryTreeWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.categoryTreeWidget.setStyleSheet(u"QTreeView::item:selected {\n"
"	background-color: rgb(84,159,176);\n"
"	color: white;\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"	background-color: rgba(84,159,176,0.5);\n"
"	color: white;\n"
"}")
        self.categoryTreeWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.categoryTreeWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.categoryTreeWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.categoryTreeWidget.header().setVisible(False)
        self.categoryTreeWidget.header().setCascadingSectionResizes(False)
        self.categoryTreeWidget.header().setMinimumSectionSize(0)
        self.categoryTreeWidget.header().setDefaultSectionSize(0)
        self.categoryTreeWidget.header().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.categoryTreeWidget)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.supportStackedWidget.addWidget(self.page_3)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_12 = QVBoxLayout(self.page_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.page_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_11)

        self.supportStackedWidget.addWidget(self.page_6)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_6 = QVBoxLayout(self.page_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(290, 640))
        self.frame_3.setMaximumSize(QSize(275, 16777215))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
" #frame_3 {\n"
"	padding: 8px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.verticalSpacer = QSpacerItem(20, 115, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(105, 140))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setStyleSheet(u"QLabel {\n"
"	background-image: url(:/images/icon/file-solid.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.sortFilenameLineEdit = QLineEdit(self.frame_3)
        self.sortFilenameLineEdit.setObjectName(u"sortFilenameLineEdit")
        self.sortFilenameLineEdit.setMinimumSize(QSize(0, 32))
        self.sortFilenameLineEdit.setFont(font1)
        self.sortFilenameLineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(244,244,244);\n"
"	border-radius: 0px;\n"
"	padding-left: 6px;\n"
"	padding-right: 6px;\n"
"}")
        self.sortFilenameLineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.sortFilenameLineEdit)

        self.categoryScrollArea = QScrollArea(self.frame_3)
        self.categoryScrollArea.setObjectName(u"categoryScrollArea")
        self.categoryScrollArea.setMaximumSize(QSize(16777215, 179))
        self.categoryScrollArea.setStyleSheet(u"QScrollArea {\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.categoryScrollArea.setFrameShape(QFrame.NoFrame)
        self.categoryScrollArea.setLineWidth(0)
        self.categoryScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 262, 77))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setAutoFillBackground(True)
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_category_choosing = QFrame(self.scrollAreaWidgetContents)
        self.frame_category_choosing.setObjectName(u"frame_category_choosing")
        self.frame_category_choosing.setFrameShape(QFrame.NoFrame)
        self.frame_category_choosing.setFrameShadow(QFrame.Sunken)
        self.frame_category_choosing.setLineWidth(0)
        self.verticalLayout_10 = QVBoxLayout(self.frame_category_choosing)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.categoryLabel = QLabel(self.frame_category_choosing)
        self.categoryLabel.setObjectName(u"categoryLabel")
        self.categoryLabel.setFont(font3)
        self.categoryLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.categoryLabel)

        self.categoryComboBox = QComboBox(self.frame_category_choosing)
        self.categoryComboBox.setObjectName(u"categoryComboBox")
        self.categoryComboBox.setMinimumSize(QSize(0, 32))
        self.categoryComboBox.setMaximumSize(QSize(189, 16777215))
        self.categoryComboBox.setEditable(True)
        self.categoryComboBox.setIconSize(QSize(32, 32))

        self.verticalLayout_10.addWidget(self.categoryComboBox)


        self.verticalLayout_7.addWidget(self.frame_category_choosing)

        self.categoryScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.categoryScrollArea)

        self.addSubcategoryPushButton = QPushButton(self.frame_3)
        self.addSubcategoryPushButton.setObjectName(u"addSubcategoryPushButton")
        self.addSubcategoryPushButton.setMinimumSize(QSize(140, 24))
        self.addSubcategoryPushButton.setMaximumSize(QSize(140, 24))
        self.addSubcategoryPushButton.setFont(font3)
        self.addSubcategoryPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSubcategoryPushButton.setLayoutDirection(Qt.LeftToRight)
        self.addSubcategoryPushButton.setAutoFillBackground(False)
        self.addSubcategoryPushButton.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"	color: rgb(84, 159, 176);\n"
"	background-color: rgba(84,159,176,0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/images/icon/plus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addSubcategoryPushButton.setIcon(icon5)
        self.addSubcategoryPushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.addSubcategoryPushButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.fileSortButton = QPushButton(self.frame_7)
        self.fileSortButton.setObjectName(u"fileSortButton")
        self.fileSortButton.setMinimumSize(QSize(161, 41))
        self.fileSortButton.setMaximumSize(QSize(161, 41))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.fileSortButton.setFont(font4)
        self.fileSortButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.fileSortButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(84,159,176,1);\n"
"	border-radius: 3px;\n"
"	text-align: center;\n"
"	color: white;\n"
"}")

        self.verticalLayout_9.addWidget(self.fileSortButton)

        self.allFilesCheckBox = QCheckBox(self.frame_7)
        self.allFilesCheckBox.setObjectName(u"allFilesCheckBox")
        self.allFilesCheckBox.setEnabled(False)
        self.allFilesCheckBox.setStyleSheet(u"QCheckBox {\n"
"	text-align: center;\n"
"}")

        self.verticalLayout_9.addWidget(self.allFilesCheckBox)


        self.verticalLayout_8.addWidget(self.frame_7, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.supportStackedWidget.addWidget(self.page_4)

        self.horizontalLayout_4.addWidget(self.supportStackedWidget)


        self.verticalLayout_11.addWidget(self.frame_8)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.overviewButton.clicked.connect(MainWindow.onOverviewClicked)
        self.fileSortButton.clicked.connect(MainWindow.onFileSortClicked)
        self.searchButton.clicked.connect(MainWindow.onSearchClicked)
        self.unsortOverviewButton.clicked.connect(MainWindow.onUnsortOverviewClicked)
        self.displayFilesTableWidget.itemDoubleClicked.connect(MainWindow.onFileItemDoubleClicked)
        self.categoryTreeWidget.currentItemChanged.connect(MainWindow.onCategoryTreeCurrentItemChange)
        self.categoryTreeWidget.itemExpanded.connect(MainWindow.onCategoryTreeExpandToggle)
        self.categoryTreeWidget.itemCollapsed.connect(MainWindow.onCategoryTreeExpandToggle)
        self.exactPathCheckBox.stateChanged.connect(MainWindow.onExactPathCheckBoxStateChange)
        self.addSubcategoryPushButton.clicked.connect(MainWindow.onAddSubcategoryClicked)
        self.unsortedFilesTableWidget.itemSelectionChanged.connect(MainWindow.onUnsortedFilesTableSelectionChange)
        self.searchLineEdit.returnPressed.connect(MainWindow.onSearchLineEnterPressed)
        self.windowCloseButton.clicked.connect(MainWindow.onWindowCloseClicked)
        self.windowMinimizeButton.clicked.connect(MainWindow.onWindowMinimizeClicked)

        self.mainStackedWidget.setCurrentIndex(1)
        self.supportStackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Woody\u00b4s File Manager", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Woody\u00b4s File Manager", None))
        self.windowMinimizeButton.setText("")
        self.windowCloseButton.setText("")
        self.overviewButton.setText("")
        self.unsortOverviewButton.setText("")
        self.searchButton.setText("")
        ___qtablewidgetitem = self.displayFilesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Dateiname", None));
        ___qtablewidgetitem1 = self.displayFilesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Dateigr\u00f6\u00dfe", None));
        ___qtablewidgetitem2 = self.displayFilesTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Dateityp", None));
        ___qtablewidgetitem3 = self.displayFilesTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Zuletzt ge\u00e4ndert", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dokumente werden geladen", None))
        self.unsortTitle.setText(QCoreApplication.translate("MainWindow", u"Unsortierte Dateien", None))
        ___qtablewidgetitem4 = self.unsortedFilesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Dateiname", None));
        ___qtablewidgetitem5 = self.unsortedFilesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Dateigr\u00f6\u00dfe", None));
        ___qtablewidgetitem6 = self.unsortedFilesTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Dateityp", None));
        ___qtablewidgetitem7 = self.unsortedFilesTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Zuletzt ge\u00e4ndert", None));
        self.categoryTitle.setText(QCoreApplication.translate("MainWindow", u"Kategorien", None))
        self.exactPathCheckBox.setText(QCoreApplication.translate("MainWindow", u"Mit Unterkatogorien", None))
        self.label.setText("")
        self.sortFilenameLineEdit.setText(QCoreApplication.translate("MainWindow", u"Dateiname", None))
        self.categoryLabel.setText(QCoreApplication.translate("MainWindow", u"Kategorie", None))
        self.addSubcategoryPushButton.setText(QCoreApplication.translate("MainWindow", u"Unterkategorie", None))
        self.fileSortButton.setText(QCoreApplication.translate("MainWindow", u"EINSORTIEREN", None))
        self.allFilesCheckBox.setText(QCoreApplication.translate("MainWindow", u"Alle ausgew\u00e4hlten Dateien", None))
    # retranslateUi

