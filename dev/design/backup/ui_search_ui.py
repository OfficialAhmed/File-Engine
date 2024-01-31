# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_search.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QComboBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 630)
        MainWindow.setMinimumSize(QSize(940, 630))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* \n"
"    \n"
"    === UI STYLE - DRACULA THEME ===\n"
"\n"
"    THEME BY             : Wanderson M. Pimenta (https://github.com/Wanderson-Magalhaes)\n"
"    EDITED & ENHANCED BY : OfficialAhmed        (https://github.com/OfficialAhmed)\n"
"\n"
"    MIT LICENSE:\n"
"    Copyright (c) 2023 OfficialAhmed\n"
"\n"
"    There are limitations on Qt licenses if you want to use your products\n"
"    commercially, I recommend reading them on the official website:\n"
"    https://doc.qt.io/qtforpython/licenses.html\n"
"\n"
"    =======================================================================================================\n"
"    =======================================================================================================\n"
"\n"
" THEME COLORS{\n"
"    rgb(42, 44, 89)\n"
"    rgb(33, 37, 43)\n"
"    rgb(44, 49, 58)\n"
"    rgb(124, 57, 191)\n"
"    rgb(189, 147, 249)\n"
"    rgb(242, 80, 231)\n"
"    rgb(255, 121, 198)\n"
"    rgb(242, 174, 48)\n"
"    rgb(84, 90, 191)\n"
"    \n"
"    rgb(200, 200,"
                        " 200)\n"
"} \n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               General styling \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"QWidget {\n"
"    color: rgb(221, 221, 221);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               ProgressBar \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"\n"
"QProgressBar {\n"
"    background-color: rgb(33, 37, 43);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    border-radius: 6px;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    color: rgb(33, 37, 43)\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Tooltip \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(33, 37, 43, "
                        "180);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    background-image: none;\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 2px solid rgb(255, 121, 198);\n"
"    text-align: left;\n"
"    padding-left: 8px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Background App \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#bgApp {\n"
"    background-color: rgb(40, 44, 52);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Left Menu \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#leftMenuBg {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"    background-color: rgb(33, 37, 43);\n"
"    background-image: url('Interface/images/images/File Engine logo.png');\n"
"    background-position: center;\n"
"    background-repeat: no-"
                        "repeat;\n"
"}\n"
"#titleLeftApp {\n"
"    font: 63 12pt \"Segoe UI Semibold\";\n"
"}\n"
"#titleLeftDescription {\n"
"    font: 8pt \"Segoe UI\";\n"
"    color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Menus \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#topMenu .QPushButton,\n"
"#bottomMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover,\n"
"#bottomMenu .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed,\n"
"#bottomMenu .QPushButton:pressed {\n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame {\n"
"    border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/*\n"
"////"
                        "/////////////////////////////////////////////////\n"
"               Toggle Button \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#toggleButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: rgb(37, 41, 48);\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"    background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Title Menu \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#titleRightInfo {\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Extra Tab \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#extraLeftBox {\n"
"    b"
                        "ackground-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg {\n"
"    background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Icon \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#extraIcon {\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-image: url(:images/images/icons/settings.svg);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Label \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#extraLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Btn Close \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#extraCloseColumnBtn {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"#extraCloseColumnBtn:hover {\n"
"    background-color: rgb(196, 161, "
                        "249);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"#extraCloseColumnBtn:pressed {\n"
"    background-color: rgb(180, 141, 238);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Extra Content \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#extraContent {\n"
"    border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Extra Top Menus \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#extraTopMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:p"
                        "ressed {\n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Content App \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#contentTopBg {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom {\n"
"    border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Top Buttons \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#rightButtons .QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"#rightButtons .QPushButton:hover {\n"
"    background-color: rgb(44, 49, 57);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"#rightButtons .QPushButton:pressed {\n"
"    background-color: rgb(23, 26, 30);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/*\n"
"/////"
                        "////////////////////////////////////////////////\n"
"               Theme Settings \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#extraRightBox {\n"
"    background-color: rgb(44, 49, 58);\n"
"}\n"
"#themeSettingsTopDetail {\n"
"    background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Bottom Bar \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#bottomBar {\n"
"    background-color: rgb(44, 49, 58);\n"
"}\n"
"#bottomBar QLabel {\n"
"    font-size: 11px;\n"
"    color: rgb(113, 126, 149);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 2px;\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Content Settings \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#contentSettings .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"  "
                        "  border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {\n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               QTableWidget \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 58);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item {\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section {\n"
"    back"
                        "ground-color: rgb(33, 37, 43);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"    background-color: rgb(33, 37, 43);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical {\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               LineEdit \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"QLineEdit {\n"
"    background-color: rgb(33, 37, 43);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding-left: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background"
                        "-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               PlainTextEdit \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"QPlainTextEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit QScrollBar:vertical {\n"
"    width: 8px;\n"
"}\n"
"QPlainTextEdit QScrollBar:horizontal {\n"
"    height: 8px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               ScrollBars \n"
"/////////////////////////////////////////////////////\n"
"*/"
                        "\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-pag"
                        "e:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:v"
                        "ertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               CheckBox \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/images/images/icons/tick-outline.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/images/images/icons/x-outline.svg);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               RadioButton \n"
"/////////////////"
                        "////////////////////////////////////\n"
"*/\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               ComboBox \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"QComboBox {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: "
                        "3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background-image: url(:images/images/icons/arrow down.svg);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(255, 121, 198);\n"
"    background-color: rgb(33, 37, 43);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Sliders \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    "
                        "height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               CommandLinkButton \n"
"//////////////////////////"
                        "///////////////////////////\n"
"*/\n"
"QCommandLinkButton {\n"
"    color: rgb(255, 121, 198);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {\n"
"    color: rgb(255, 170, 255);\n"
"    background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {\n"
"    color: rgb(189, 147, 249);\n"
"    background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/*\n"
"/////////////////////////////////////////////////////\n"
"               Button \n"
"/////////////////////////////////////////////////////\n"
"*/\n"
"#pagesContainer QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {\n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"\n"
"/*					Grou"
                        "pBox				*/\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid rgb(113, 126, 149);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: rgb(113, 126, 149);\n"
"    padding: 0 15px 10px 2px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked {\n"
"    image: url(:/images/images/icons/x-outline.svg);\n"
"}\n"
"\n"
"QGroupBox::indicator:checked {\n"
"    image: url(:/images/images/icons/tick-outline.svg);\n"
"}\n"
"\n"
"/*						Tab						*/\n"
"\n"
"QTabWidget {\n"
"    border: 1px solid rgb(42, 44, 89);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QTabBar {\n"
"    background-color: rgb(44, 49, 58);\n"
"    color: #ffffff;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    padding: 8px 16px;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: rgb(44, 49, 58);\n"
"    border-bottom: 2px solid rgb(189, 147, 249);\n"
"    "
                        "padding: 15px 15px; /* Adjust the padding for the selected tab */\n"
"    margin-top: -2px; /* Move the tab slightly upward to create a pop-out effect */\n"
"\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"}\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")
        icon = QIcon()
        icon.addFile(u"../images/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleButton.setIcon(icon)

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")
        icon1 = QIcon()
        icon1.addFile(u"../images/icons/trash-can.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon2)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon3)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon4)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon5)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.mainFrame = QStackedWidget(self.pagesContainer)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.mainFrame.addWidget(self.home)
        self.FinderPage = QWidget()
        self.FinderPage.setObjectName(u"FinderPage")
        self.FinderPage.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.FinderPage)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.tabsWidget = QTabWidget(self.FinderPage)
        self.tabsWidget.setObjectName(u"tabsWidget")
        self.tabsWidget.setStyleSheet(u"\n"
"QTabBar {\n"
"    background-color: rgb(44, 49, 58);\n"
"    color: #ffffff;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.BASIC = QWidget()
        self.BASIC.setObjectName(u"BASIC")
        self.verticalLayout_21 = QVBoxLayout(self.BASIC)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.basicTabMainVL = QVBoxLayout()
        self.basicTabMainVL.setObjectName(u"basicTabMainVL")
        self.titleGroupBox = QGroupBox(self.BASIC)
        self.titleGroupBox.setObjectName(u"titleGroupBox")
        self.titleGroupBox.setStyleSheet(u"")
        self.titleGroupBox.setFlat(False)
        self.titleGroupBox.setCheckable(True)
        self.titleGroupBox.setChecked(True)
        self.third_layout_6 = QGridLayout(self.titleGroupBox)
        self.third_layout_6.setObjectName(u"third_layout_6")
        self.third_layout_6.setContentsMargins(10, 20, 10, 10)
        self.titleLineEdit = QLineEdit(self.titleGroupBox)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setMinimumSize(QSize(0, 30))
        self.titleLineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.titleLineEdit.setMaxLength(100)

        self.third_layout_6.addWidget(self.titleLineEdit, 0, 3, 1, 1)

        self.titleComboBox = QComboBox(self.titleGroupBox)
        self.titleComboBox.addItem("")
        self.titleComboBox.addItem("")
        self.titleComboBox.setObjectName(u"titleComboBox")
        self.titleComboBox.setFont(font)
        self.titleComboBox.setAutoFillBackground(False)
        self.titleComboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.titleComboBox.setIconSize(QSize(16, 16))
        self.titleComboBox.setFrame(True)

        self.third_layout_6.addWidget(self.titleComboBox, 0, 0, 1, 1)

        self.titleComboBox2 = QComboBox(self.titleGroupBox)
        self.titleComboBox2.addItem("")
        self.titleComboBox2.addItem("")
        self.titleComboBox2.setObjectName(u"titleComboBox2")
        self.titleComboBox2.setFont(font)
        self.titleComboBox2.setAutoFillBackground(False)
        self.titleComboBox2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.titleComboBox2.setIconSize(QSize(16, 16))
        self.titleComboBox2.setFrame(True)

        self.third_layout_6.addWidget(self.titleComboBox2, 0, 1, 1, 1)

        self.titleComboBox3 = QComboBox(self.titleGroupBox)
        self.titleComboBox3.addItem("")
        self.titleComboBox3.addItem("")
        self.titleComboBox3.addItem("")
        self.titleComboBox3.addItem("")
        self.titleComboBox3.addItem("")
        self.titleComboBox3.addItem("")
        self.titleComboBox3.addItem("")
        self.titleComboBox3.addItem("")
        self.titleComboBox3.addItem("")
        self.titleComboBox3.addItem("")
        self.titleComboBox3.setObjectName(u"titleComboBox3")
        self.titleComboBox3.setFont(font)
        self.titleComboBox3.setAutoFillBackground(False)
        self.titleComboBox3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.titleComboBox3.setIconSize(QSize(16, 16))
        self.titleComboBox3.setFrame(True)

        self.third_layout_6.addWidget(self.titleComboBox3, 0, 2, 1, 1)

        self.isRecursiveCheckBox = QCheckBox(self.titleGroupBox)
        self.isRecursiveCheckBox.setObjectName(u"isRecursiveCheckBox")
        self.isRecursiveCheckBox.setEnabled(True)
        self.isRecursiveCheckBox.setAutoFillBackground(False)
        self.isRecursiveCheckBox.setStyleSheet(u"")
        self.isRecursiveCheckBox.setChecked(True)

        self.third_layout_6.addWidget(self.isRecursiveCheckBox, 2, 0, 1, 1)

        self.isCaseSensitiveCheckBox = QCheckBox(self.titleGroupBox)
        self.isCaseSensitiveCheckBox.setObjectName(u"isCaseSensitiveCheckBox")
        self.isCaseSensitiveCheckBox.setEnabled(True)
        self.isCaseSensitiveCheckBox.setAutoFillBackground(False)
        self.isCaseSensitiveCheckBox.setStyleSheet(u"")

        self.third_layout_6.addWidget(self.isCaseSensitiveCheckBox, 3, 0, 1, 1)

        self.titleLineEditHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.third_layout_6.addItem(self.titleLineEditHSpacer, 2, 3, 1, 1)


        self.basicTabMainVL.addWidget(self.titleGroupBox)

        self.tabsVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.basicTabMainVL.addItem(self.tabsVSpacer)


        self.verticalLayout_21.addLayout(self.basicTabMainVL)

        self.tabsWidget.addTab(self.BASIC, "")
        self.ADVANCED = QWidget()
        self.ADVANCED.setObjectName(u"ADVANCED")
        self.verticalLayout_18 = QVBoxLayout(self.ADVANCED)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.advancedTabMainVL = QVBoxLayout()
        self.advancedTabMainVL.setSpacing(10)
        self.advancedTabMainVL.setObjectName(u"advancedTabMainVL")
        self.advancedTitleGroupBox = QGroupBox(self.ADVANCED)
        self.advancedTitleGroupBox.setObjectName(u"advancedTitleGroupBox")
        self.advancedTitleGroupBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid rgb(113, 126, 149);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: rgb(113, 126, 149);\n"
"    padding: 0 15px 10px 2px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked {\n"
"    image: url(:/images/images/icons/x-outline.svg);\n"
"}\n"
"\n"
"QGroupBox::indicator:checked {\n"
"    image: url(:/images/images/icons/tick-outline.svg);\n"
"}\n"
"")
        self.advancedTitleGroupBox.setFlat(False)
        self.advancedTitleGroupBox.setCheckable(True)
        self.advancedTitleGroupBox.setChecked(True)
        self.third_layout_8 = QGridLayout(self.advancedTitleGroupBox)
        self.third_layout_8.setObjectName(u"third_layout_8")
        self.third_layout_8.setContentsMargins(10, 20, 10, 10)
        self.advancedTitleLineEdite = QLineEdit(self.advancedTitleGroupBox)
        self.advancedTitleLineEdite.setObjectName(u"advancedTitleLineEdite")
        self.advancedTitleLineEdite.setMinimumSize(QSize(0, 30))
        self.advancedTitleLineEdite.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.advancedTitleLineEdite.setMaxLength(100)

        self.third_layout_8.addWidget(self.advancedTitleLineEdite, 0, 3, 1, 1)

        self.advancedTitleComboBox = QComboBox(self.advancedTitleGroupBox)
        self.advancedTitleComboBox.addItem("")
        self.advancedTitleComboBox.addItem("")
        self.advancedTitleComboBox.setObjectName(u"advancedTitleComboBox")
        self.advancedTitleComboBox.setFont(font)
        self.advancedTitleComboBox.setAutoFillBackground(False)
        self.advancedTitleComboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.advancedTitleComboBox.setIconSize(QSize(16, 16))
        self.advancedTitleComboBox.setFrame(True)

        self.third_layout_8.addWidget(self.advancedTitleComboBox, 0, 0, 1, 1)

        self.advancedTitleComboBox2 = QComboBox(self.advancedTitleGroupBox)
        self.advancedTitleComboBox2.addItem("")
        self.advancedTitleComboBox2.addItem("")
        self.advancedTitleComboBox2.setObjectName(u"advancedTitleComboBox2")
        self.advancedTitleComboBox2.setFont(font)
        self.advancedTitleComboBox2.setAutoFillBackground(False)
        self.advancedTitleComboBox2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.advancedTitleComboBox2.setIconSize(QSize(16, 16))
        self.advancedTitleComboBox2.setFrame(True)

        self.third_layout_8.addWidget(self.advancedTitleComboBox2, 0, 1, 1, 1)

        self.advancedTitleComboBox3 = QComboBox(self.advancedTitleGroupBox)
        self.advancedTitleComboBox3.addItem("")
        self.advancedTitleComboBox3.addItem("")
        self.advancedTitleComboBox3.addItem("")
        self.advancedTitleComboBox3.addItem("")
        self.advancedTitleComboBox3.addItem("")
        self.advancedTitleComboBox3.addItem("")
        self.advancedTitleComboBox3.addItem("")
        self.advancedTitleComboBox3.addItem("")
        self.advancedTitleComboBox3.addItem("")
        self.advancedTitleComboBox3.addItem("")
        self.advancedTitleComboBox3.setObjectName(u"advancedTitleComboBox3")
        self.advancedTitleComboBox3.setFont(font)
        self.advancedTitleComboBox3.setAutoFillBackground(False)
        self.advancedTitleComboBox3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.advancedTitleComboBox3.setIconSize(QSize(16, 16))
        self.advancedTitleComboBox3.setFrame(True)

        self.third_layout_8.addWidget(self.advancedTitleComboBox3, 0, 2, 1, 1)

        self.advancedIsRecuresiveCheckBox = QCheckBox(self.advancedTitleGroupBox)
        self.advancedIsRecuresiveCheckBox.setObjectName(u"advancedIsRecuresiveCheckBox")
        self.advancedIsRecuresiveCheckBox.setEnabled(True)
        self.advancedIsRecuresiveCheckBox.setAutoFillBackground(False)
        self.advancedIsRecuresiveCheckBox.setChecked(True)

        self.third_layout_8.addWidget(self.advancedIsRecuresiveCheckBox, 2, 0, 1, 1)

        self.advancedIsCaseSensitiveCheckBox = QCheckBox(self.advancedTitleGroupBox)
        self.advancedIsCaseSensitiveCheckBox.setObjectName(u"advancedIsCaseSensitiveCheckBox")
        self.advancedIsCaseSensitiveCheckBox.setEnabled(True)
        self.advancedIsCaseSensitiveCheckBox.setAutoFillBackground(False)

        self.third_layout_8.addWidget(self.advancedIsCaseSensitiveCheckBox, 3, 0, 1, 1)

        self.advancedTitleLineEditeHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.third_layout_8.addItem(self.advancedTitleLineEditeHSpacer, 2, 3, 1, 1)


        self.advancedTabMainVL.addWidget(self.advancedTitleGroupBox)

        self.advancedMetadataGroupBox = QGroupBox(self.ADVANCED)
        self.advancedMetadataGroupBox.setObjectName(u"advancedMetadataGroupBox")
        self.advancedMetadataGroupBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid rgb(113, 126, 149);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: rgb(113, 126, 149);\n"
"    padding: 0 15px 10px 2px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked {\n"
"    image: url(:/images/images/icons/x-outline.svg);\n"
"}\n"
"\n"
"QGroupBox::indicator:checked {\n"
"    image: url(:/images/images/icons/tick-outline.svg);\n"
"}")
        self.advancedMetadataGroupBox.setFlat(False)
        self.advancedMetadataGroupBox.setCheckable(True)
        self.advancedMetadataGroupBox.setChecked(False)
        self.third_layout_9 = QGridLayout(self.advancedMetadataGroupBox)
        self.third_layout_9.setObjectName(u"third_layout_9")
        self.third_layout_9.setContentsMargins(10, 20, 10, 0)
        self.metadataComboBox2 = QComboBox(self.advancedMetadataGroupBox)
        self.metadataComboBox2.addItem("")
        self.metadataComboBox2.addItem("")
        self.metadataComboBox2.addItem("")
        self.metadataComboBox2.addItem("")
        self.metadataComboBox2.addItem("")
        self.metadataComboBox2.setObjectName(u"metadataComboBox2")
        self.metadataComboBox2.setFont(font)
        self.metadataComboBox2.setAutoFillBackground(False)
        self.metadataComboBox2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.metadataComboBox2.setIconSize(QSize(16, 16))
        self.metadataComboBox2.setFrame(True)

        self.third_layout_9.addWidget(self.metadataComboBox2, 0, 1, 1, 1)

        self.metadataComboBox = QComboBox(self.advancedMetadataGroupBox)
        self.metadataComboBox.addItem("")
        self.metadataComboBox.addItem("")
        self.metadataComboBox.addItem("")
        self.metadataComboBox.addItem("")
        self.metadataComboBox.setObjectName(u"metadataComboBox")
        self.metadataComboBox.setFont(font)
        self.metadataComboBox.setAutoFillBackground(False)
        self.metadataComboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.metadataComboBox.setIconSize(QSize(16, 16))
        self.metadataComboBox.setFrame(True)

        self.third_layout_9.addWidget(self.metadataComboBox, 0, 0, 1, 1)

        self.metadataLineEditHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.third_layout_9.addItem(self.metadataLineEditHSpacer, 1, 3, 1, 1)

        self.metadataComboBox3 = QComboBox(self.advancedMetadataGroupBox)
        self.metadataComboBox3.addItem("")
        self.metadataComboBox3.addItem("")
        self.metadataComboBox3.addItem("")
        self.metadataComboBox3.setObjectName(u"metadataComboBox3")
        self.metadataComboBox3.setFont(font)
        self.metadataComboBox3.setAutoFillBackground(False)
        self.metadataComboBox3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.metadataComboBox3.setIconSize(QSize(16, 16))
        self.metadataComboBox3.setFrame(True)

        self.third_layout_9.addWidget(self.metadataComboBox3, 0, 2, 1, 1)

        self.metadataLineEdit = QLineEdit(self.advancedMetadataGroupBox)
        self.metadataLineEdit.setObjectName(u"metadataLineEdit")
        self.metadataLineEdit.setMinimumSize(QSize(0, 30))
        self.metadataLineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.metadataLineEdit.setMaxLength(100)

        self.third_layout_9.addWidget(self.metadataLineEdit, 0, 3, 1, 1)


        self.advancedTabMainVL.addWidget(self.advancedMetadataGroupBox)

        self.advancedOtherGroupBox = QGroupBox(self.ADVANCED)
        self.advancedOtherGroupBox.setObjectName(u"advancedOtherGroupBox")
        self.advancedOtherGroupBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid rgb(113, 126, 149);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: rgb(113, 126, 149);\n"
"    padding: 0 15px 0 2px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked {\n"
"    image: url(:/images/images/icons/x-outline.svg);\n"
"}\n"
"\n"
"QGroupBox::indicator:checked {\n"
"    image: url(:/images/images/icons/tick-outline.svg);\n"
"}")
        self.advancedOtherGroupBox.setFlat(False)
        self.advancedOtherGroupBox.setCheckable(True)
        self.advancedOtherGroupBox.setChecked(False)
        self.third_layout_11 = QGridLayout(self.advancedOtherGroupBox)
        self.third_layout_11.setObjectName(u"third_layout_11")
        self.third_layout_11.setContentsMargins(10, 20, 10, 0)
        self.otherComboBox = QComboBox(self.advancedOtherGroupBox)
        self.otherComboBox.addItem("")
        self.otherComboBox.addItem("")
        self.otherComboBox.setObjectName(u"otherComboBox")
        self.otherComboBox.setFont(font)
        self.otherComboBox.setAutoFillBackground(False)
        self.otherComboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.otherComboBox.setIconSize(QSize(16, 16))
        self.otherComboBox.setFrame(True)

        self.third_layout_11.addWidget(self.otherComboBox, 0, 0, 1, 1)

        self.otherComboBox3 = QComboBox(self.advancedOtherGroupBox)
        self.otherComboBox3.addItem("")
        self.otherComboBox3.addItem("")
        self.otherComboBox3.addItem("")
        self.otherComboBox3.setObjectName(u"otherComboBox3")
        self.otherComboBox3.setFont(font)
        self.otherComboBox3.setAutoFillBackground(False)
        self.otherComboBox3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.otherComboBox3.setIconSize(QSize(16, 16))
        self.otherComboBox3.setFrame(True)

        self.third_layout_11.addWidget(self.otherComboBox3, 0, 2, 1, 1)

        self.otherLineEdit = QLineEdit(self.advancedOtherGroupBox)
        self.otherLineEdit.setObjectName(u"otherLineEdit")
        self.otherLineEdit.setMinimumSize(QSize(0, 30))
        self.otherLineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.otherLineEdit.setMaxLength(100)

        self.third_layout_11.addWidget(self.otherLineEdit, 0, 4, 1, 1)

        self.otherLineEditHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.third_layout_11.addItem(self.otherLineEditHSpacer, 1, 4, 1, 1)

        self.otherComboBox2 = QComboBox(self.advancedOtherGroupBox)
        self.otherComboBox2.addItem("")
        self.otherComboBox2.addItem("")
        self.otherComboBox2.addItem("")
        self.otherComboBox2.addItem("")
        self.otherComboBox2.setObjectName(u"otherComboBox2")
        self.otherComboBox2.setFont(font)
        self.otherComboBox2.setAutoFillBackground(False)
        self.otherComboBox2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.otherComboBox2.setIconSize(QSize(16, 16))
        self.otherComboBox2.setFrame(True)

        self.third_layout_11.addWidget(self.otherComboBox2, 0, 1, 1, 1)


        self.advancedTabMainVL.addWidget(self.advancedOtherGroupBox)

        self.advancedBottomVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.advancedTabMainVL.addItem(self.advancedBottomVSpacer)


        self.verticalLayout_18.addLayout(self.advancedTabMainVL)

        self.tabsWidget.addTab(self.ADVANCED, "")
        self.RESULT = QWidget()
        self.RESULT.setObjectName(u"RESULT")
        self.verticalLayout_23 = QVBoxLayout(self.RESULT)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.resultTabMainVL = QVBoxLayout()
        self.resultTabMainVL.setObjectName(u"resultTabMainVL")
        self.table = QTableWidget(self.RESULT)
        if (self.table.columnCount() < 4):
            self.table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.table.rowCount() < 5):
            self.table.setRowCount(5)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.table.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setCheckState(Qt.Checked);
        self.table.setItem(0, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table.setItem(1, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table.setItem(1, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table.setItem(1, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setCheckState(Qt.Checked);
        self.table.setItem(1, 3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table.setItem(2, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table.setItem(2, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table.setItem(2, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setCheckState(Qt.Checked);
        self.table.setItem(2, 3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table.setItem(3, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table.setItem(3, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table.setItem(3, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setCheckState(Qt.Checked);
        self.table.setItem(3, 3, __qtablewidgetitem24)
        self.table.setObjectName(u"table")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.table.setPalette(palette)
        self.table.setStyleSheet(u"")
        self.table.setFrameShape(QFrame.NoFrame)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setShowGrid(True)
        self.table.setGridStyle(Qt.SolidLine)
        self.table.setSortingEnabled(True)
        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setDefaultSectionSize(200)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setCascadingSectionResizes(False)
        self.table.verticalHeader().setHighlightSections(False)
        self.table.verticalHeader().setStretchLastSection(True)

        self.resultTabMainVL.addWidget(self.table)

        self.bottomHL = QHBoxLayout()
        self.bottomHL.setObjectName(u"bottomHL")
        self.bottomHL.setContentsMargins(-1, 0, -1, -1)
        self.deleteOptionBtn = QPushButton(self.RESULT)
        self.deleteOptionBtn.setObjectName(u"deleteOptionBtn")
        self.deleteOptionBtn.setEnabled(False)
        self.deleteOptionBtn.setMinimumSize(QSize(150, 30))
        self.deleteOptionBtn.setFont(font)
        self.deleteOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteOptionBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u"../images/icons/folder_outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteOptionBtn.setIcon(icon6)

        self.bottomHL.addWidget(self.deleteOptionBtn)

        self.renameOptionBtn = QPushButton(self.RESULT)
        self.renameOptionBtn.setObjectName(u"renameOptionBtn")
        self.renameOptionBtn.setEnabled(False)
        self.renameOptionBtn.setMinimumSize(QSize(150, 30))
        self.renameOptionBtn.setFont(font)
        self.renameOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.renameOptionBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.renameOptionBtn.setIcon(icon6)

        self.bottomHL.addWidget(self.renameOptionBtn)

        self.moveOptionBtn = QPushButton(self.RESULT)
        self.moveOptionBtn.setObjectName(u"moveOptionBtn")
        self.moveOptionBtn.setEnabled(False)
        self.moveOptionBtn.setMinimumSize(QSize(150, 30))
        self.moveOptionBtn.setFont(font)
        self.moveOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.moveOptionBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.moveOptionBtn.setIcon(icon6)

        self.bottomHL.addWidget(self.moveOptionBtn)

        self.duplicateOptionBtn = QPushButton(self.RESULT)
        self.duplicateOptionBtn.setObjectName(u"duplicateOptionBtn")
        self.duplicateOptionBtn.setEnabled(False)
        self.duplicateOptionBtn.setMinimumSize(QSize(150, 30))
        self.duplicateOptionBtn.setFont(font)
        self.duplicateOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.duplicateOptionBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.duplicateOptionBtn.setIcon(icon6)

        self.bottomHL.addWidget(self.duplicateOptionBtn)

        self.resultBottomLHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomHL.addItem(self.resultBottomLHSpacer)


        self.resultTabMainVL.addLayout(self.bottomHL)


        self.verticalLayout_23.addLayout(self.resultTabMainVL)

        self.tabsWidget.addTab(self.RESULT, "")

        self.verticalLayout.addWidget(self.tabsWidget)

        self.searchGroup = QGroupBox(self.FinderPage)
        self.searchGroup.setObjectName(u"searchGroup")
        self.searchGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid rgb(113, 126, 149);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: rgb(113, 126, 149);\n"
"    padding: -10px 15px 0 20px;\n"
"}\n"
"")
        self.searchGroup.setChecked(False)
        self.third_layout_7 = QGridLayout(self.searchGroup)
        self.third_layout_7.setObjectName(u"third_layout_7")
        self.third_layout_7.setContentsMargins(10, 20, 10, 10)
        self.searchMainVL = QVBoxLayout()
        self.searchMainVL.setSpacing(5)
        self.searchMainVL.setObjectName(u"searchMainVL")
        self.topGL = QGridLayout()
        self.topGL.setObjectName(u"topGL")
        self.topGL.setContentsMargins(-1, 2, -1, 0)
        self.searchTypeComboBox = QComboBox(self.searchGroup)
        self.searchTypeComboBox.addItem("")
        self.searchTypeComboBox.addItem("")
        self.searchTypeComboBox.setObjectName(u"searchTypeComboBox")
        self.searchTypeComboBox.setFont(font)
        self.searchTypeComboBox.setAutoFillBackground(False)
        self.searchTypeComboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.searchTypeComboBox.setIconSize(QSize(16, 16))
        self.searchTypeComboBox.setFrame(True)

        self.topGL.addWidget(self.searchTypeComboBox, 0, 0, 1, 1)

        self.browsePathBtn = QPushButton(self.searchGroup)
        self.browsePathBtn.setObjectName(u"browsePathBtn")
        self.browsePathBtn.setMinimumSize(QSize(150, 30))
        self.browsePathBtn.setFont(font)
        self.browsePathBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browsePathBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.browsePathBtn.setIcon(icon6)

        self.topGL.addWidget(self.browsePathBtn, 0, 2, 1, 1)

        self.pathLineEdit = QLineEdit(self.searchGroup)
        self.pathLineEdit.setObjectName(u"pathLineEdit")
        self.pathLineEdit.setMinimumSize(QSize(0, 30))
        self.pathLineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.topGL.addWidget(self.pathLineEdit, 0, 1, 1, 1)

        self.startSearchBtn = QPushButton(self.searchGroup)
        self.startSearchBtn.setObjectName(u"startSearchBtn")
        self.startSearchBtn.setMinimumSize(QSize(150, 30))
        self.startSearchBtn.setFont(font)
        self.startSearchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.startSearchBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.startSearchBtn.setIcon(icon6)

        self.topGL.addWidget(self.startSearchBtn, 0, 3, 1, 1)


        self.searchMainVL.addLayout(self.topGL)

        self.foundMatchLabel = QLabel(self.searchGroup)
        self.foundMatchLabel.setObjectName(u"foundMatchLabel")
        self.foundMatchLabel.setAlignment(Qt.AlignCenter)

        self.searchMainVL.addWidget(self.foundMatchLabel)


        self.third_layout_7.addLayout(self.searchMainVL, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.searchGroup)

        self.mainFrame.addWidget(self.FinderPage)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.mainFrame.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.mainFrame)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)
        self.titleGroupBox.toggled.connect(self.titleComboBox.setEnabled)
        self.titleGroupBox.toggled.connect(self.titleComboBox2.setEnabled)
        self.titleGroupBox.toggled.connect(self.titleComboBox3.setEnabled)
        self.titleGroupBox.toggled.connect(self.titleLineEdit.setEnabled)
        self.titleGroupBox.toggled.connect(self.isRecursiveCheckBox.setEnabled)
        self.titleGroupBox.toggled.connect(self.isCaseSensitiveCheckBox.setEnabled)

        self.mainFrame.setCurrentIndex(1)
        self.tabsWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; "
                        "margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"File Engine - File management and automation tool", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.titleGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"TITLE LOOKUP", None))
        self.titleLineEdit.setText("")
        self.titleLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter values to look for seperated by comma", None))
        self.titleComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"NAME", None))
        self.titleComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"EXTENSION", None))

        self.titleComboBox2.setItemText(0, QCoreApplication.translate("MainWindow", u"CONTAIN", None))
        self.titleComboBox2.setItemText(1, QCoreApplication.translate("MainWindow", u"EQUAL TO", None))

        self.titleComboBox3.setItemText(0, QCoreApplication.translate("MainWindow", u"Alphabets only", None))
        self.titleComboBox3.setItemText(1, QCoreApplication.translate("MainWindow", u"Alphabets & Symbols", None))
        self.titleComboBox3.setItemText(2, QCoreApplication.translate("MainWindow", u"Alphabets & Numbers", None))
        self.titleComboBox3.setItemText(3, QCoreApplication.translate("MainWindow", u"Alphabets Excluding", None))
        self.titleComboBox3.setItemText(4, QCoreApplication.translate("MainWindow", u"Numbers only", None))
        self.titleComboBox3.setItemText(5, QCoreApplication.translate("MainWindow", u"Numbers & Symbols", None))
        self.titleComboBox3.setItemText(6, QCoreApplication.translate("MainWindow", u"Numbers Excluding", None))
        self.titleComboBox3.setItemText(7, QCoreApplication.translate("MainWindow", u"Symbols only", None))
        self.titleComboBox3.setItemText(8, QCoreApplication.translate("MainWindow", u"Symbols Excluding", None))
        self.titleComboBox3.setItemText(9, QCoreApplication.translate("MainWindow", u"Custom", None))

#if QT_CONFIG(tooltip)
        self.isRecursiveCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Find files recursively through the selected path", None))
#endif // QT_CONFIG(tooltip)
        self.isRecursiveCheckBox.setText(QCoreApplication.translate("MainWindow", u"RECURSIVE", None))
#if QT_CONFIG(tooltip)
        self.isCaseSensitiveCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Find files recursively through the selected path", None))
#endif // QT_CONFIG(tooltip)
        self.isCaseSensitiveCheckBox.setText(QCoreApplication.translate("MainWindow", u"CASE SENSITIVE", None))
        self.tabsWidget.setTabText(self.tabsWidget.indexOf(self.BASIC), QCoreApplication.translate("MainWindow", u"BASIC", None))
        self.advancedTitleGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"TITLE LOOKUP", None))
        self.advancedTitleLineEdite.setText("")
        self.advancedTitleLineEdite.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter values to look for seperated by comma", None))
        self.advancedTitleComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"NAME", None))
        self.advancedTitleComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"EXTENSION", None))

        self.advancedTitleComboBox2.setItemText(0, QCoreApplication.translate("MainWindow", u"CONTAIN", None))
        self.advancedTitleComboBox2.setItemText(1, QCoreApplication.translate("MainWindow", u"EQUAL TO", None))

        self.advancedTitleComboBox3.setItemText(0, QCoreApplication.translate("MainWindow", u"Alphabets only", None))
        self.advancedTitleComboBox3.setItemText(1, QCoreApplication.translate("MainWindow", u"Alphabets & Symbols", None))
        self.advancedTitleComboBox3.setItemText(2, QCoreApplication.translate("MainWindow", u"Alphabets & Numbers", None))
        self.advancedTitleComboBox3.setItemText(3, QCoreApplication.translate("MainWindow", u"Alphabets Excluding", None))
        self.advancedTitleComboBox3.setItemText(4, QCoreApplication.translate("MainWindow", u"Numbers only", None))
        self.advancedTitleComboBox3.setItemText(5, QCoreApplication.translate("MainWindow", u"Numbers & Symbols", None))
        self.advancedTitleComboBox3.setItemText(6, QCoreApplication.translate("MainWindow", u"Numbers Excluding", None))
        self.advancedTitleComboBox3.setItemText(7, QCoreApplication.translate("MainWindow", u"Symbols only", None))
        self.advancedTitleComboBox3.setItemText(8, QCoreApplication.translate("MainWindow", u"Symbols Excluding", None))
        self.advancedTitleComboBox3.setItemText(9, QCoreApplication.translate("MainWindow", u"Custom", None))

#if QT_CONFIG(tooltip)
        self.advancedIsRecuresiveCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Find files recursively through the selected path", None))
#endif // QT_CONFIG(tooltip)
        self.advancedIsRecuresiveCheckBox.setText(QCoreApplication.translate("MainWindow", u"RECURSIVE", None))
#if QT_CONFIG(tooltip)
        self.advancedIsCaseSensitiveCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Find files recursively through the selected path", None))
#endif // QT_CONFIG(tooltip)
        self.advancedIsCaseSensitiveCheckBox.setText(QCoreApplication.translate("MainWindow", u"CASE SENSITIVE", None))
        self.advancedMetadataGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"METADATA LOOKUP", None))
        self.metadataComboBox2.setItemText(0, QCoreApplication.translate("MainWindow", u"DIMENSIONS", None))
        self.metadataComboBox2.setItemText(1, QCoreApplication.translate("MainWindow", u"DURATION", None))
        self.metadataComboBox2.setItemText(2, QCoreApplication.translate("MainWindow", u"BIT RATE", None))
        self.metadataComboBox2.setItemText(3, QCoreApplication.translate("MainWindow", u"FRAME RATE", None))
        self.metadataComboBox2.setItemText(4, QCoreApplication.translate("MainWindow", u"FPS", None))

        self.metadataComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"VIDEO", None))
        self.metadataComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"IMAGE", None))
        self.metadataComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"AUDIO", None))
        self.metadataComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"DOCS", None))

        self.metadataComboBox3.setItemText(0, QCoreApplication.translate("MainWindow", u"1920x1080", None))
        self.metadataComboBox3.setItemText(1, QCoreApplication.translate("MainWindow", u"720x420", None))
        self.metadataComboBox3.setItemText(2, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.metadataLineEdit.setText("")
        self.metadataLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter values to look for seperated by comma", None))
        self.advancedOtherGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"OTHER LOOKUPS", None))
        self.otherComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"SIZE", None))
        self.otherComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"DATE CREATED", None))

        self.otherComboBox3.setItemText(0, QCoreApplication.translate("MainWindow", u"EQUAL TO", None))
        self.otherComboBox3.setItemText(1, QCoreApplication.translate("MainWindow", u"LESS THAN", None))
        self.otherComboBox3.setItemText(2, QCoreApplication.translate("MainWindow", u"GREATER THAN", None))

        self.otherLineEdit.setText("")
        self.otherLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter values to look for seperated by comma", None))
        self.otherComboBox2.setItemText(0, QCoreApplication.translate("MainWindow", u"BYTES", None))
        self.otherComboBox2.setItemText(1, QCoreApplication.translate("MainWindow", u"KILOBYTES", None))
        self.otherComboBox2.setItemText(2, QCoreApplication.translate("MainWindow", u"MEGABYTES", None))
        self.otherComboBox2.setItemText(3, QCoreApplication.translate("MainWindow", u"GIGABYTES", None))

        self.tabsWidget.setTabText(self.tabsWidget.indexOf(self.ADVANCED), QCoreApplication.translate("MainWindow", u"ADVANCED", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.table.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.table.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.table.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.table.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.table.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.table.item(0, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem10 = self.table.item(0, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem11 = self.table.item(0, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem12 = self.table.item(0, 3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"SELECT", None));
        ___qtablewidgetitem13 = self.table.item(1, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"test (c 0, r 0)", None));
        ___qtablewidgetitem14 = self.table.item(1, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"test (c 1, r 0)", None));
        ___qtablewidgetitem15 = self.table.item(1, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"test (c 2, r 0)", None));
        ___qtablewidgetitem16 = self.table.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"test (c 0, r 1)", None));
        ___qtablewidgetitem17 = self.table.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"test (c 1, r 1)", None));
        ___qtablewidgetitem18 = self.table.item(2, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"test (c 2, r 1)", None));
        ___qtablewidgetitem19 = self.table.item(3, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"test (c 0, r 2)", None));
        ___qtablewidgetitem20 = self.table.item(3, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"test (c 1, r 2)", None));
        ___qtablewidgetitem21 = self.table.item(3, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"test (c 2 r 2)", None));
        self.table.setSortingEnabled(__sortingEnabled)

        self.deleteOptionBtn.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.renameOptionBtn.setText(QCoreApplication.translate("MainWindow", u"RENAME", None))
        self.moveOptionBtn.setText(QCoreApplication.translate("MainWindow", u"MOVE", None))
        self.duplicateOptionBtn.setText(QCoreApplication.translate("MainWindow", u"DUPLICATE", None))
        self.tabsWidget.setTabText(self.tabsWidget.indexOf(self.RESULT), QCoreApplication.translate("MainWindow", u"RESULT", None))
        self.searchGroup.setTitle(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.searchTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"FILES", None))
        self.searchTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"FOLDERS", None))

        self.browsePathBtn.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
#if QT_CONFIG(tooltip)
        self.pathLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Enter the path where should the lookup process begin", None))
#endif // QT_CONFIG(tooltip)
        self.pathLineEdit.setText("")
        self.pathLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DIRECTORY PATH...", None))
        self.startSearchBtn.setText(QCoreApplication.translate("MainWindow", u"START ", None))
        self.foundMatchLabel.setText(QCoreApplication.translate("MainWindow", u"FOUND 0 MATCHES ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NEW PAGE TEST", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Developed by @OfficialAhmed0", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.1.2", None))
    # retranslateUi

