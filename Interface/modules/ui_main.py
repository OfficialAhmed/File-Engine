from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *
from ..environment import Constant, Common
from . ui_delete import Ui as Ui_delete


class Ui(object):

    def __init__(self) -> None:
        super().__init__()

        self.constant = Constant()
        self.common_functions = Common()


    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
            
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)

        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
""
"SET APP STYLESHEET - FULL STYLES HERE"
"DARK THEME - DRACULA COLOR BASED"
""
"///////////////////////////////////////////////////////////////////////////////////////////////// */"
""
"QWidget{"
"	color: rgb(221, 221, 221);"
"	font: 10pt \"Segoe UI\";"
"}"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"Tooltip */"
"QToolTip {"
"	color: #ffffff;"
"	background-color: rgba(33, 37, 43, 180);"
"	border: 1px solid rgb(44, 49, 58);"
"	background-image: none;"
"	background-position: left center;"
"    background-repeat: no-repeat;"
"	border: none;"
"	border-left: 2px solid rgb(255, 121, 198);"
"	text-align: left;"
"	padding-left: 8px;"
"	margin: 0px;"
"}"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"Bg App */"
"#bgApp {	"
"	background"
                        "-color: rgb(40, 44, 52);"
"	border: 1px solid rgb(44, 49, 58);"
"}"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"Left Menu */"
"#leftMenuBg {	"
"	background-color: rgb(33, 37, 43);"
"}"
"#topLogo {"
"	background-color: rgb(33, 37, 43);"
"	background-image: url('Interface/images/images/File Engine logo.png');"
"	background-position: centered;"
"	background-repeat: no-repeat;"
"}"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }"
""
"/* MENUS */"
"#topMenu .QPushButton {	"
"	background-position: left center;"
"    background-repeat: no-repeat;"
"	border: none;"
"	border-left: 22px solid transparent;"
"	background-color: transparent;"
"	text-align: left;"
"	padding-left: 44px;"
"}"
"#topMenu .QPushButton:hover {"
"	background-color: rgb(40, 44, 52);"
"}"
"#topMenu .QPushButton:pressed {	"
"	background-color: rgb(18"
                        "9, 147, 249);"
"	color: rgb(255, 255, 255);"
"}"
"#bottomMenu .QPushButton {	"
"	background-position: left center;"
"    background-repeat: no-repeat;"
"	border: none;"
"	border-left: 20px solid transparent;"
"	background-color:transparent;"
"	text-align: left;"
"	padding-left: 44px;"
"}"
"#bottomMenu .QPushButton:hover {"
"	background-color: rgb(40, 44, 52);"
"}"
"#bottomMenu .QPushButton:pressed {	"
"	background-color: rgb(189, 147, 249);"
"	color: rgb(255, 255, 255);"
"}"
"#leftMenuFrame{"
"	border-top: 3px solid rgb(44, 49, 58);"
"}"
""
"/* Toggle Button */"
"#toggleButton {"
"	background-position: left center;"
"    background-repeat: no-repeat;"
"	border: none;"
"	border-left: 20px solid transparent;"
"	background-color: rgb(37, 41, 48);"
"	text-align: left;"
"	padding-left: 44px;"
"	color: rgb(113, 126, 149);"
"}"
"#toggleButton:hover {"
"	background-color: rgb(40, 44, 52);"
"}"
"#toggleButton:pressed {"
"	background-color: rgb("
                        "189, 147, 249);"
"}"
""
"/* Title Menu */"
"#titleRightInfo { padding-left: 10px; }"
""
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"Extra Tab */"
"#extraLeftBox {	"
"	background-color: rgb(44, 49, 58);"
"}"
"#extraTopBg{	"
"	background-color: rgb(189, 147, 249)"
"}"
""
"/* Icon */"
"#extraIcon {"
"	background-position: center;"
"	background-repeat: no-repeat;"
"	background-image: url(:images/images/icons/settings.svg);"
"}"
""
"/* Label */"
"#extraLabel { color: rgb(255, 255, 255); }"
""
"/* Btn Close */"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }"
""
"/* Extra Content */"
"#extraContent{"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);"
"}"
""
"/* Extra Top Menus */"
"#extraTopMenu .QPushButton {"
"background-position: left center;"
"    background-repeat: no-repeat;"
"	border: none;"
"	border-left: 22px solid transparent;"
"	background-color:transparent;"
"	text-align: left;"
"	padding-left: 44px;"
"}"
"#extraTopMenu .QPushButton:hover {"
"	background-color: rgb(40, 44, 52);"
"}"
"#extraTopMenu .QPushButton:pressed {	"
"	background-color: rgb(189, 147, 249);"
"	color: rgb(255, 255, 255);"
"}"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"Content App */"
"#contentTopBg{	"
"	background-color: rgb(33, 37, 43);"
"}"
"#contentBottom{"
"	border-top: 3px solid rgb(44, 49, 58);"
"}"
""
"/* Top Buttons */"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }"
""
"/* Theme Settings */"
"#extraRightBox { background-color: rgb(44, 49, 58); }"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }"
""
"/* Bottom Bar */"
"#bottomBar { background-color: rgb(44, 49, 58); }"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }"
""
"/* CONTENT SETTINGS */"
"/* MENUS */"
"#contentSettings .QPushButton {	"
"	background-position: left center;"
"    background-repeat: no-repeat;"
"	border: none;"
"	border-left: 22px solid transparent;"
"	background-color:transparent;"
"	text-align: left;"
"	padding-left: 44px;"
"}"
"#contentSettings .QPushButton:hover {"
"	background-color: rgb(40, 44, 52);"
"}"
"#contentSettings .QPushButton:pressed {	"
"	background-color: rgb(189, 147, 249);"
"	color: rgb"
                        "(255, 255, 255);"
"}"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"QTableWidget */"
"QTableWidget {	"
"	background-color: transparent;"
"	padding: 10px;"
"	border-radius: 5px;"
"	gridline-color: rgb(44, 49, 58);"
"	border-bottom: 1px solid rgb(44, 49, 60);"
"}"
"QTableWidget::item{"
"	border-color: rgb(44, 49, 60);"
"	padding-left: 5px;"
"	padding-right: 5px;"
"	gridline-color: rgb(44, 49, 60);"
"}"
"QTableWidget::item:selected{"
"	background-color: rgb(189, 147, 249);"
"}"
"QHeaderView::section{"
"	background-color: rgb(33, 37, 43);"
"	max-width: 30px;"
"	border: 1px solid rgb(44, 49, 58);"
"	border-style: none;"
"    border-bottom: 1px solid rgb(44, 49, 60);"
"    border-right: 1px solid rgb(44, 49, 60);"
"}"
"QTableWidget::horizontalHeader {	"
"	background-color: rgb(33, 37, 43);"
"}"
"QHeaderView::section:horizontal"
"{"
"    border: 1px solid rgb(33, 37, 43);"
"	background-co"
                        "lor: rgb(33, 37, 43);"
"	padding: 3px;"
"	border-top-left-radius: 7px;"
"    border-top-right-radius: 7px;"
"}"
"QHeaderView::section:vertical"
"{"
"    border: 1px solid rgb(44, 49, 60);"
"}"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"LineEdit */"
"QLineEdit {"
"	background-color: rgb(33, 37, 43);"
"	border-radius: 5px;"
"	border: 2px solid rgb(33, 37, 43);"
"	padding-left: 10px;"
"	selection-color: rgb(255, 255, 255);"
"	selection-background-color: rgb(255, 121, 198);"
"}"
"QLineEdit:hover {"
"	border: 2px solid rgb(64, 71, 88);"
"}"
"QLineEdit:focus {"
"	border: 2px solid rgb(91, 101, 124);"
"}"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"PlainTextEdit */"
"QPlainTextEdit {"
"	background-color: rgb(27, 29, 35);"
"	border-radius: 5px;"
"	padding: 10px;"
"	selection-color: rgb(255, 255, 255);"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);"
"}"
"QPlainTextEdit  QScrollBar:vertical {"
"    width: 8px;"
" }"
"QPlainTextEdit  QScrollBar:horizontal {"
"    height: 8px;"
" }"
"QPlainTextEdit:hover {"
"	border: 2px solid rgb(64, 71, 88);"
"}"
"QPlainTextEdit:focus {"
"	border: 2px solid rgb(91, 101, 124);"
"}"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"ScrollBars */"
"QScrollBar:horizontal {"
"    border: none;"
"    background: rgb(52, 59, 72);"
"    height: 8px;"
"    margin: 0px 21px 0 21px;"
"	border-radius: 0px;"
"}"
"QScrollBar::handle:horizontal {"
"    background: rgb(189, 147, 249);"
"    min-width: 25px;"
"	border-radius: 4px"
"}"
"QScrollBar::add-line:horizontal {"
"    border: none;"
"    background: rgb(55, 63, 77);"
"    width: 20px;"
"	border-top-right-radius: 4px;"
"    border-bottom-right-radius: 4px;"
"    subcontrol-position: right;"
"    subcontrol-origin: margin;"
"}"
""
                        "QScrollBar::sub-line:horizontal {"
"    border: none;"
"    background: rgb(55, 63, 77);"
"    width: 20px;"
"	border-top-left-radius: 4px;"
"    border-bottom-left-radius: 4px;"
"    subcontrol-position: left;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal"
"{"
"     background: none;"
"}"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal"
"{"
"     background: none;"
"}"
" QScrollBar:vertical {"
"	border: none;"
"    background: rgb(52, 59, 72);"
"    width: 8px;"
"    margin: 21px 0 21px 0;"
"	border-radius: 0px;"
" }"
" QScrollBar::handle:vertical {	"
"	background: rgb(189, 147, 249);"
"    min-height: 25px;"
"	border-radius: 4px"
" }"
" QScrollBar::add-line:vertical {"
"     border: none;"
"    background: rgb(55, 63, 77);"
"     height: 20px;"
"	border-bottom-left-radius: 4px;"
"    border-bottom-right-radius: 4px;"
"     subcontrol-position: bottom;"
"     su"
                        "bcontrol-origin: margin;"
" }"
" QScrollBar::sub-line:vertical {"
"	border: none;"
"    background: rgb(55, 63, 77);"
"     height: 20px;"
"	border-top-left-radius: 4px;"
"    border-top-right-radius: 4px;"
"     subcontrol-position: top;"
"     subcontrol-origin: margin;"
" }"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {"
"     background: none;"
" }"
""
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {"
"     background: none;"
" }"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"CheckBox */"
"QCheckBox::indicator {"
"    border: 3px solid rgb(52, 59, 72);"
"	width: 15px;"
"	height: 15px;"
"	border-radius: 10px;"
"    background: rgb(44, 49, 60);"
"}"
"QCheckBox::indicator:hover {"
"    border: 3px solid rgb(58, 66, 81);"
"}"
"QCheckBox::indicator:checked {"
"    background: 3px solid rgb(52, 59, 72);"
"	border: 3px solid rgb(52, 59, 72);	"
"	back"
        "ground-image: url('Interface/images/icons/tick-outline.svg');"
"}"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"RadioButton */"
"QRadioButton::indicator {"
"    border: 3px solid rgb(52, 59, 72);"
"	width: 15px;"
"	height: 15px;"
"	border-radius: 10px;"
"    background: rgb(44, 49, 60);"
"}"
"QRadioButton::indicator:hover {"
"    border: 3px solid rgb(58, 66, 81);"
"}"
"QRadioButton::indicator:checked {"
"    background: 3px solid rgb(94, 106, 130);"
"	border: 3px solid rgb(52, 59, 72);	"
"}"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"ComboBox */"
"QComboBox{"
"	background-color: rgb(27, 29, 35);"
"	border-radius: 5px;"
"	border: 2px solid rgb(33, 37, 43);"
"	padding: 5px;"
"	padding-left: 10px;"
"}"
"QComboBox:hover{"
"	border: 2px solid rgb(64, 71, 88);"
"}"
"QComboBox::drop-down {"
"	subcontrol-origin: padding;"
"	subco"
                        "ntrol-position: top right;"
"	width: 25px; "
"	border-left-width: 3px;"
"	border-left-color: rgba(39, 44, 54, 150);"
"	border-left-style: solid;"
"	border-top-right-radius: 3px;"
"	border-bottom-right-radius: 3px;	"
"	background-image: url(:/images/images/icons/arrow down.svg);"
"	background-position: center;"
"	background-repeat: no-reperat;"
" }"
"QComboBox QAbstractItemView {"
"	color: rgb(255, 121, 198);	"
"	background-color: rgb(33, 37, 43);"
"	padding: 10px;"
"	selection-background-color: rgb(39, 44, 54);"
"}"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"Sliders */"
"QSlider::groove:horizontal {"
"    border-radius: 5px;"
"    height: 10px;"
"	margin: 0px;"
"	background-color: rgb(52, 59, 72);"
"}"
"QSlider::groove:horizontal:hover {"
"	background-color: rgb(55, 62, 76);"
"}"
"QSlider::handle:horizontal {"
"    background-color: rgb(189, 147, 249);"
"    border: none;"
"    h"
                        "eight: 10px;"
"    width: 10px;"
"    margin: 0px;"
"	border-radius: 5px;"
"}"
"QSlider::handle:horizontal:hover {"
"    background-color: rgb(195, 155, 255);"
"}"
"QSlider::handle:horizontal:pressed {"
"    background-color: rgb(255, 121, 198);"
"}"
""
"QSlider::groove:vertical {"
"    border-radius: 5px;"
"    width: 10px;"
"    margin: 0px;"
"	background-color: rgb(52, 59, 72);"
"}"
"QSlider::groove:vertical:hover {"
"	background-color: rgb(55, 62, 76);"
"}"
"QSlider::handle:vertical {"
"    background-color: rgb(189, 147, 249);"
"	border: none;"
"    height: 10px;"
"    width: 10px;"
"    margin: 0px;"
"	border-radius: 5px;"
"}"
"QSlider::handle:vertical:hover {"
"    background-color: rgb(195, 155, 255);"
"}"
"QSlider::handle:vertical:pressed {"
"    background-color: rgb(255, 121, 198);"
"}"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"CommandLinkButton */"
"QCommandLi"
                        "nkButton {	"
"	color: rgb(255, 121, 198);"
"	border-radius: 5px;"
"	padding: 5px;"
"	color: rgb(255, 170, 255);"
"}"
"QCommandLinkButton:hover {	"
"	color: rgb(255, 170, 255);"
"	background-color: rgb(44, 49, 60);"
"}"
"QCommandLinkButton:pressed {	"
"	color: rgb(189, 147, 249);"
"	background-color: rgb(52, 58, 71);"
"}"
""
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
"Button */"
"#pagesContainer QPushButton {"
"	border: 2px solid rgb(52, 59, 72);"
"	border-radius: 5px;	"
"	background-color: rgb(52, 59, 72);"
"}"
"#pagesContainer QPushButton:hover {"
"	background-color: rgb(57, 65, 80);"
"	border: 2px solid rgb(61, 70, 86);"
"}"
"#pagesContainer QPushButton:pressed {	"
"	background-color: rgb(35, 40, 49);"
"	border: 2px solid rgb(43, 50, 61);"
"}"
""
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
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
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

        """
        ////////////////////////////////////////////////
                LEFT MENU BUTTONS 
        ////////////////////////////////////////////////
        """

        self.home_page = QPushButton(self.topMenu)
        self.home_page.setObjectName(u"home_page")
        sizePolicy.setHeightForWidth(self.home_page.sizePolicy().hasHeightForWidth())
        self.home_page.setSizePolicy(sizePolicy)
        self.home_page.setMinimumSize(QSize(0, 45))
        self.home_page.setFont(font)
        self.home_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_page.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_8.addWidget(self.home_page)

        self.delete_page = QPushButton(self.topMenu)
        self.delete_page.setObjectName(u"delete_page")
        sizePolicy.setHeightForWidth(self.delete_page.sizePolicy().hasHeightForWidth())
        self.delete_page.setSizePolicy(sizePolicy)
        self.delete_page.setMinimumSize(QSize(0, 45))
        self.delete_page.setFont(font)
        self.delete_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_page.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_8.addWidget(self.delete_page)

        self.rename_page = QPushButton(self.topMenu)
        self.rename_page.setObjectName(u"rename_page")
        sizePolicy.setHeightForWidth(self.rename_page.sizePolicy().hasHeightForWidth())
        self.rename_page.setSizePolicy(sizePolicy)
        self.rename_page.setMinimumSize(QSize(0, 45))
        self.rename_page.setFont(font)
        self.rename_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.rename_page.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_8.addWidget(self.rename_page)

        self.move_page = QPushButton(self.topMenu)
        self.move_page.setObjectName(u"move_page")
        sizePolicy.setHeightForWidth(self.move_page.sizePolicy().hasHeightForWidth())
        self.move_page.setSizePolicy(sizePolicy)
        self.move_page.setMinimumSize(QSize(0, 45))
        self.move_page.setFont(font)
        self.move_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.move_page.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_8.addWidget(self.move_page)

        self.lookup_page = QPushButton(self.topMenu)
        self.lookup_page.setObjectName(u"lookup_page")
        sizePolicy.setHeightForWidth(self.lookup_page.sizePolicy().hasHeightForWidth())
        self.lookup_page.setSizePolicy(sizePolicy)
        self.lookup_page.setMinimumSize(QSize(0, 45))
        self.lookup_page.setFont(font)
        self.lookup_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.lookup_page.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_8.addWidget(self.lookup_page)
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

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)

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
        self.moreBtn = QPushButton(self.rightButtons)
        self.moreBtn.setObjectName(u"moreBtn")
        self.moreBtn.setMinimumSize(QSize(28, 28))
        self.moreBtn.setMaximumSize(QSize(28, 28))
        self.moreBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.moreBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))

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

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))

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
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        

        """
        ////////////////////////////////////////////////
                HOME PAGE CONTENT
        ////////////////////////////////////////////////
        """

        
        self.home = QWidget()
        self.home.setObjectName(u"home")
        
        self.stackedWidget.addWidget(self.home)


        """
        ////////////////////////////////////////////////
                DELETE PAGE CONTENT
        ////////////////////////////////////////////////
        """
        
        self.widgets = Ui_delete().render()

        self.stackedWidget.addWidget(self.widgets)


        """
        ////////////////////////////////////////////////
                LEFT MENU BUTTONS 
        ////////////////////////////////////////////////
        """

        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)
        self.stackedWidget.addWidget(self.new_page)
        self.verticalLayout_15.addWidget(self.stackedWidget)
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

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)

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
        self.render_images()
        self.stackedWidget.setCurrentIndex(1)

        # self.render_delete_page_icons()

        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"File Engine", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Dracula Dark Theme", None))

        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"HIDE", None))
        self.home_page.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.delete_page.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.rename_page.setText(QCoreApplication.translate("MainWindow", u"RENAME", None))
        self.move_page.setText(QCoreApplication.translate("MainWindow", u"MOVE", None))
        self.lookup_page.setText(QCoreApplication.translate("MainWindow", u"LOOKUP", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Settings", None))
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"...", None))


        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">CREDITS</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">UI design by: Wanderson M. Pimenta\nDracula theme by: Zeno Rocha</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">2023</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">DEVELOPER</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">@OfficialAhmed0</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">GitHub</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; "
                        "margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">https://github.com/OfficialAhmed/File-Engine</span></p></body></html>", None))
        
        
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"File Engine - File management and automation tool", None))
        self.moreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        self.minimizeAppBtn.setText("")
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        self.maximizeRestoreAppBtn.setText("")
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        self.closeAppBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"NEW PAGE TEST", None))
        
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"...", None))
        
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Developed by @OfficialAhmed0", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.1.2", None))
        


    def render_images(self) -> None:

        # WINDOW 
        self.common_functions.set_icon(self.moreBtn, "more")
        self.common_functions.set_icon(self.minimizeAppBtn, "minimize")
        self.common_functions.set_icon(self.maximizeRestoreAppBtn, "maximize")
        self.common_functions.set_icon(self.closeAppBtn, "close")
        

        # MAIN PAGE
        self.set_bg_image(
            self.home, 
            "File Engine vertical", 
            False, 
            "background-position: center;\n" + "background-repeat: no-repeat;"
        )

        # MAIN OPTIONS
        self.set_bg_image(self.toggleButton, "menu")
        self.set_bg_image(self.home_page, "home")
        self.set_bg_image(self.delete_page, "trash-can")
        self.set_bg_image(self.rename_page, "rename-outline")
        self.set_bg_image(self.move_page, "file move")
        self.set_bg_image(self.lookup_page, "search-outline")
        self.set_bg_image(self.toggleLeftBox, "settings")

        # LEFT MENU OPTIONS
        self.set_bg_image(self.btn_share, "home")
        self.set_bg_image(self.btn_adjustments, "home")
        self.set_bg_image(self.btn_more, "home")
        self.common_functions.set_icon(self.extraCloseColumnBtn, "close")

        # RIGHT MENU OPTIONS
        self.set_bg_image(self.btn_message, "home")
        self.set_bg_image(self.btn_print, "home")
        self.set_bg_image(self.btn_logout, "home")


    def set_bg_image(self, widget:QWidget, name:str, is_icon = True, extra_style="") -> str:
        """
            return images from resources.rc
        """
        
        # Determine path and extension
        path = "icons" if is_icon else "images"
        ext = "svg" if is_icon else "png"

        widget.setStyleSheet(
            f"background-image: url({self.constant.get_resources_path()}{path}/{name}.{ext});\
            {extra_style}"
        )
