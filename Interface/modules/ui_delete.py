from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ..environment import Constant, Common, Html


class Ui:

    def __init__(self) -> None:
        self.constant = Constant()
        self.common_functions = Common()
        self.html = Html()

        self.user_path = ""


    def render(self):

        self.widgets = QWidget()

        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)

        self.widgets.setObjectName(u"widgets")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_content_wid_3 = QFrame(self.widgets)
        self.frame_content_wid_3.setObjectName(u"frame_content_wid_3")
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_content_wid_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.first_layout = QGridLayout()
        self.first_layout.setObjectName(u"first_layout")
        self.PageTitle_label = QLabel(self.frame_content_wid_3)
        self.PageTitle_label.setObjectName(u"PageTitle_label")
        self.PageTitle_label.setFont(font)

        self.first_layout.addWidget(self.PageTitle_label, 0, 0, 1, 1)

        self.LookupType_comboBox = QComboBox(self.frame_content_wid_3)
        self.LookupType_comboBox.setObjectName(u"LookupType_comboBox")
        self.LookupType_comboBox.setFont(font)
        self.LookupType_comboBox.setAutoFillBackground(False)
        self.LookupType_comboBox.setStyleSheet(self.html.get_bg_color("dark blue"))
        self.LookupType_comboBox.setFrame(True)

        self.first_layout.addWidget(self.LookupType_comboBox, 1, 0, 1, 1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.first_layout.addItem(self.horizontalSpacer, 1, 1, 1, 1)
        self.horizontalLayout_11.addLayout(self.first_layout)
        self.verticalLayout.addWidget(self.frame_content_wid_3)

        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.row_1)

        self.frame_content_wid_4 = QFrame(self.widgets)
        self.frame_content_wid_4.setObjectName(u"frame_content_wid_4")
        self.frame_content_wid_4.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_content_wid_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.second_layout = QGridLayout()
        self.second_layout.setObjectName(u"second_layout")
        self.second_layout.setContentsMargins(-1, -1, -1, 0)
        self.currentPath_lineEdit = QLineEdit(self.frame_content_wid_4)
        self.currentPath_lineEdit.setObjectName(u"currentPath_lineEdit")
        self.currentPath_lineEdit.setMinimumSize(QSize(0, 30))
        self.currentPath_lineEdit.setStyleSheet(self.html.get_bg_color("dark blue"))

        self.second_layout.addWidget(self.currentPath_lineEdit, 0, 1, 1, 1)

        self.browseCurrentPath_btn = QPushButton(self.frame_content_wid_4)
        self.browseCurrentPath_btn.setObjectName(u"browseCurrentPath_btn")
        self.browseCurrentPath_btn.setMinimumSize(QSize(150, 30))
        self.browseCurrentPath_btn.setFont(font)
        self.browseCurrentPath_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browseCurrentPath_btn.setStyleSheet(self.html.get_bg_color("lightblue"))

        self.second_layout.addWidget(self.browseCurrentPath_btn, 0, 2, 1, 1)
        self.horizontalLayout_13.addLayout(self.second_layout)
        self.verticalLayout.addWidget(self.frame_content_wid_4)

        self.frame_content_wid_2 = QFrame(self.widgets)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.third_layout = QGridLayout()
        self.third_layout.setObjectName(u"third_layout")
        self.third_layout.setContentsMargins(-1, -1, -1, 0)
        self.currentLookupInput_lineEdit = QLineEdit(self.frame_content_wid_2)
        self.currentLookupInput_lineEdit.setObjectName(u"currentLookupInput_lineEdit")
        self.currentLookupInput_lineEdit.setMinimumSize(QSize(0, 30))
        self.currentLookupInput_lineEdit.setStyleSheet(self.html.get_bg_color("dark blue"))

        self.third_layout.addWidget(self.currentLookupInput_lineEdit, 1, 1, 1, 1)

        self.startLookup_btn = QPushButton(self.frame_content_wid_2)
        self.startLookup_btn.setObjectName(u"startLookup_btn")
        self.startLookup_btn.setMinimumSize(QSize(150, 30))
        self.startLookup_btn.setFont(font)
        self.startLookup_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.startLookup_btn.setStyleSheet(self.html.get_bg_color("lightblue"))

        self.third_layout.addWidget(self.startLookup_btn, 1, 2, 1, 1)

        self.currentLookupBy_comboBox = QComboBox(self.frame_content_wid_2)
        self.currentLookupBy_comboBox.setObjectName(u"currentLookupBy_comboBox")
        self.currentLookupBy_comboBox.setFont(font)
        self.currentLookupBy_comboBox.setAutoFillBackground(False)
        self.currentLookupBy_comboBox.setStyleSheet(self.html.get_bg_color("dark blue"))
        self.currentLookupBy_comboBox.setFrame(True)

        self.third_layout.addWidget(self.currentLookupBy_comboBox, 1, 0, 1, 1)

        self.isRecursive_checkBox = QCheckBox(self.frame_content_wid_2)
        self.isRecursive_checkBox.setObjectName(u"isRecursive_checkBox")
        self.isRecursive_checkBox.setAutoFillBackground(False)
        self.isRecursive_checkBox.setChecked(True)

        self.third_layout.addWidget(self.isRecursive_checkBox, 2, 0, 1, 1)

        self.LookuByTitle_label = QLabel(self.frame_content_wid_2)
        self.LookuByTitle_label.setObjectName(u"LookuByTitle_label")
        self.LookuByTitle_label.setStyleSheet(u"color: rgb(113, 126, 149)")
        self.LookuByTitle_label.setLineWidth(1)
        self.LookuByTitle_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.third_layout.addWidget(self.LookuByTitle_label, 0, 0, 1, 1)
        self.horizontalLayout_10.addLayout(self.third_layout)
        self.verticalLayout.addWidget(self.frame_content_wid_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.table_layout = QTableWidget(self.row_3)
        
        if (self.table_layout.columnCount() < 4):
            self.table_layout.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_layout.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_layout.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_layout.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_layout.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.table_layout.rowCount() < 5):
            self.table_layout.setRowCount(5)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4)
        self.table_layout.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_layout.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_layout.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_layout.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_layout.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_layout.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_layout.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_layout.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setCheckState(Qt.Checked)
        self.table_layout.setItem(0, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_layout.setItem(1, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_layout.setItem(1, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_layout.setItem(1, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setCheckState(Qt.Checked)
        self.table_layout.setItem(1, 3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_layout.setItem(2, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_layout.setItem(2, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_layout.setItem(2, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setCheckState(Qt.Checked)
        self.table_layout.setItem(2, 3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_layout.setItem(3, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_layout.setItem(3, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_layout.setItem(3, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setCheckState(Qt.Checked)

        self.table_layout.setItem(3, 3, __qtablewidgetitem24)
        self.table_layout.setObjectName(u"table_layout")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table_layout.sizePolicy().hasHeightForWidth())
        self.table_layout.setSizePolicy(sizePolicy3)
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
        self.table_layout.setPalette(palette)
        self.table_layout.setFrameShape(QFrame.NoFrame)
        self.table_layout.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_layout.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_layout.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_layout.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_layout.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_layout.setShowGrid(True)
        self.table_layout.setGridStyle(Qt.SolidLine)
        self.table_layout.setSortingEnabled(True)
        self.table_layout.horizontalHeader().setVisible(False)
        self.table_layout.horizontalHeader().setCascadingSectionResizes(True)
        self.table_layout.horizontalHeader().setDefaultSectionSize(200)
        self.table_layout.horizontalHeader().setStretchLastSection(True)
        self.table_layout.verticalHeader().setVisible(False)
        self.table_layout.verticalHeader().setCascadingSectionResizes(False)
        self.table_layout.verticalHeader().setHighlightSections(False)
        self.table_layout.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.table_layout)

        self.optionBtns_layout = QVBoxLayout()
        self.optionBtns_layout.setObjectName(u"optionBtns_layout")
        self.delete_btn = QPushButton(self.row_3)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setEnabled(False)
        self.delete_btn.setMinimumSize(QSize(150, 30))
        self.delete_btn.setFont(font)
        self.delete_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_btn.setStyleSheet(self.html.get_bg_color("lightblue"))

        self.optionBtns_layout.addWidget(self.delete_btn)

        self.restore_btn = QPushButton(self.row_3)
        self.restore_btn.setObjectName(u"restore_btn")
        self.restore_btn.setEnabled(False)
        self.restore_btn.setMinimumSize(QSize(150, 30))
        self.restore_btn.setFont(font)
        self.restore_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restore_btn.setStyleSheet(self.html.get_bg_color("lightblue"))

        self.optionBtns_layout.addWidget(self.restore_btn)

        self.save_btn = QPushButton(self.row_3)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setEnabled(False)
        self.save_btn.setMinimumSize(QSize(150, 30))
        self.save_btn.setFont(font)
        self.save_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_btn.setStyleSheet(self.html.get_bg_color("lightblue"))

        self.optionBtns_layout.addWidget(self.save_btn)

        self.load_btn = QPushButton(self.row_3)
        self.load_btn.setObjectName(u"load_btn")
        self.load_btn.setEnabled(False)
        self.load_btn.setMinimumSize(QSize(150, 30))
        self.load_btn.setFont(font)
        self.load_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.load_btn.setStyleSheet(self.html.get_bg_color("lightblue"))

        self.optionBtns_layout.addWidget(self.load_btn)
        self.horizontalLayout_12.addLayout(self.optionBtns_layout)
        self.verticalLayout.addWidget(self.row_3)
        
        self.retranslateUi()
        self.render_page_icons()

        """
        ////////////////////////////////////////////////
                BUTTONS SIGNAL
        ////////////////////////////////////////////////
        """

        self.browseCurrentPath_btn.clicked.connect(lambda: self.set_user_path())

        self.LookupType_comboBox.currentTextChanged.connect(lambda: self.change_lookup_format())


        return self.widgets
    

    def retranslateUi(self):
        """
            Translate the ui text
        """


        """
        ////////////////////////////////////////////////
                COMOBOXES ITEMS
        ////////////////////////////////////////////////
        """

        data = {
            self.LookupType_comboBox      : ("FILES", "FOLDERS"),
            self.currentLookupBy_comboBox : ("NAME", "PATTERN", "EXTENSION")
        }

        for widget, info in data.items():

            for indx, text in enumerate(info):

                widget.addItem("")
                widget.setItemText(indx, QCoreApplication.translate("MainWindow", text, None))


        """
        ////////////////////////////////////////////////
                SET TEXT / TOOL TIPS
        ////////////////////////////////////////////////
        """

        data = {
            self.delete_btn           :  ("DELETE"   ,"Delete All Selected Items"),
            self.restore_btn          :  ("RESTORE"  ,"Restore Last Deleted Process"),
            self.save_btn             :  ("SAVE"     ,"Store Current Lookup"),
            self.load_btn             :  ("LOAD"     ,"Load Previous Lookup"),
            self.startLookup_btn      :  ("START"    ,"Start Lookup Process"),
            self.isRecursive_checkBox :  ("RECURSIVE","Find Files Recursively Through The Selected Path") 
        }

        for widget, info in data.items():
            
            widget.setText(QCoreApplication.translate("MainWindow", info[0], None))
            widget.setToolTip(QCoreApplication.translate("MainWindow", info[1], None))
            

        self.PageTitle_label.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))

        self.currentPath_lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Enter the path where should the lookup process begin", None))
        self.currentPath_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter the path here", None))
        self.browseCurrentPath_btn.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.currentLookupInput_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your input", None))
        self.LookuByTitle_label.setText(QCoreApplication.translate("MainWindow", u"LOOKUP BY", None))

        ___qtablewidgetitem = self.table_layout.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem1 = self.table_layout.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        ___qtablewidgetitem2 = self.table_layout.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        ___qtablewidgetitem3 = self.table_layout.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None))

        ___qtablewidgetitem4 = self.table_layout.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None))
        ___qtablewidgetitem5 = self.table_layout.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None))
        ___qtablewidgetitem6 = self.table_layout.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None))
        ___qtablewidgetitem7 = self.table_layout.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None))
        ___qtablewidgetitem8 = self.table_layout.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None))

        __sortingEnabled = self.table_layout.isSortingEnabled()
        self.table_layout.setSortingEnabled(True)

        """
        ////////////////////////////////////////////////
                TABLE CONTENT
        ////////////////////////////////////////////////
        """
        ___qtablewidgetitem9 = self.table_layout.item(0, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"SOURCE", None))
        ___qtablewidgetitem10 = self.table_layout.item(0, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"FILE", None))
        ___qtablewidgetitem11 = self.table_layout.item(0, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"File", None))
        ___qtablewidgetitem12 = self.table_layout.item(0, 3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"SELECT", None))

        ___qtablewidgetitem13 = self.table_layout.item(1, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"test (c 0, r 0)", None))
        ___qtablewidgetitem14 = self.table_layout.item(1, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"test (c 1, r 0)", None))
        ___qtablewidgetitem15 = self.table_layout.item(1, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"test (c 2, r 0)", None))
        ___qtablewidgetitem16 = self.table_layout.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"test (c 0, r 1)", None))
        ___qtablewidgetitem17 = self.table_layout.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"test (c 1, r 1)", None))
        ___qtablewidgetitem18 = self.table_layout.item(2, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"test (c 2, r 1)", None))
        ___qtablewidgetitem19 = self.table_layout.item(3, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"test (c 0, r 2)", None))
        ___qtablewidgetitem20 = self.table_layout.item(3, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"test (c 1, r 2)", None))
        ___qtablewidgetitem21 = self.table_layout.item(3, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"test (c 2 r 2)", None))
        self.table_layout.setSortingEnabled(__sortingEnabled)


    def render_page_icons(self):
        
        size = 20
        self.common_functions.set_icon(self.browseCurrentPath_btn, "folder_outline", (size, size))
        self.common_functions.set_icon(self.startLookup_btn, "start", (size, size))
        self.common_functions.set_icon(self.delete_btn, "delete sign", (size, size))
        self.common_functions.set_icon(self.restore_btn, "restore file", (size, size))
        self.common_functions.set_icon(self.load_btn, "file upload", (size, size))
        self.common_functions.set_icon(self.save_btn, "file download", (size, size))


class Model(Ui):

    pass


class Controller(Ui):

    def set_user_path(self):
        """
            update user path input
        """
        
        path = self.common_functions.get_user_path()

        # RESET USER PATH
        if not path:
            self.user_path = ""
            return 

        self.user_path = path
        self.currentPath_lineEdit.setText(path)


    def change_lookup_format(self) -> None:
        """
            Change lookup format options according to the lookup type
        """

        current_type = self.LookupType_comboBox.currentText()
        total_formats = self.currentLookupBy_comboBox.count()

        # ADD THE OPTION 'EXTENSION' IF 'FILES' SELECTED
        if current_type == "FILES":
            if total_formats == 2:
                self.currentLookupBy_comboBox.addItem("EXTENSION")
                return
            
        if total_formats == 3:
            self.currentLookupBy_comboBox.removeItem(2)