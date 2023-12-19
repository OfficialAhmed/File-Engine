
from PySide6.QtCore import (
    QCoreApplication, QMetaObject, QRect, QSize, Qt
)
from PySide6.QtGui import (
    QBrush, QColor, QCursor, QFont, QIcon, QPalette
)
from PySide6.QtWidgets import (
    QAbstractItemView, QAbstractScrollArea, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout,  QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget
)

from Interface.environment import Common


class Ui(Common):

    def __init__(self) -> None:
        super().__init__()

    def render_page(self):
        
        # self.widgets = QWidget()
        self.widgets = QWidget()

        font = QFont()
        self.widgets.setObjectName(u"widgets")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.tabsWidget = QTabWidget(self.widgets)
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
        self.titleComboBox2.setStyleSheet(
            u"background-color: rgb(33, 37, 43);")
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
        self.titleComboBox3.setStyleSheet(
            u"background-color: rgb(33, 37, 43);")
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

        self.titleLineEditHSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.third_layout_6.addItem(self.titleLineEditHSpacer, 2, 3, 1, 1)

        self.basicTabMainVL.addWidget(self.titleGroupBox)

        self.tabsVSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        self.advancedTitleGroupBox.setFlat(False)
        self.advancedTitleGroupBox.setCheckable(True)
        self.advancedTitleGroupBox.setChecked(True)
        self.third_layout_8 = QGridLayout(self.advancedTitleGroupBox)
        self.third_layout_8.setObjectName(u"third_layout_8")
        self.third_layout_8.setContentsMargins(10, 20, 10, 10)
        self.advancedTitleLineEdite = QLineEdit(self.advancedTitleGroupBox)
        self.advancedTitleLineEdite.setObjectName(u"advancedTitleLineEdite")
        self.advancedTitleLineEdite.setMinimumSize(QSize(0, 30))
        self.advancedTitleLineEdite.setStyleSheet(
            u"background-color: rgb(33, 37, 43);")
        self.advancedTitleLineEdite.setMaxLength(100)

        self.third_layout_8.addWidget(self.advancedTitleLineEdite, 0, 3, 1, 1)

        self.advancedTitleComboBox = QComboBox(self.advancedTitleGroupBox)
        self.advancedTitleComboBox.addItem("")
        self.advancedTitleComboBox.addItem("")
        self.advancedTitleComboBox.setObjectName(u"advancedTitleComboBox")
        self.advancedTitleComboBox.setFont(font)
        self.advancedTitleComboBox.setAutoFillBackground(False)
        self.advancedTitleComboBox.setStyleSheet(
            u"background-color: rgb(33, 37, 43);")
        self.advancedTitleComboBox.setIconSize(QSize(16, 16))
        self.advancedTitleComboBox.setFrame(True)

        self.third_layout_8.addWidget(self.advancedTitleComboBox, 0, 0, 1, 1)

        self.advancedTitleComboBox2 = QComboBox(self.advancedTitleGroupBox)
        self.advancedTitleComboBox2.addItem("")
        self.advancedTitleComboBox2.addItem("")
        self.advancedTitleComboBox2.setObjectName(u"advancedTitleComboBox2")
        self.advancedTitleComboBox2.setFont(font)
        self.advancedTitleComboBox2.setAutoFillBackground(False)
        self.advancedTitleComboBox2.setStyleSheet(
            u"background-color: rgb(33, 37, 43);")
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
        self.advancedTitleComboBox3.setStyleSheet(
            u"background-color: rgb(33, 37, 43);")
        self.advancedTitleComboBox3.setIconSize(QSize(16, 16))
        self.advancedTitleComboBox3.setFrame(True)

        self.third_layout_8.addWidget(self.advancedTitleComboBox3, 0, 2, 1, 1)

        self.advancedIsRecuresiveCheckBox = QCheckBox(
            self.advancedTitleGroupBox)
        self.advancedIsRecuresiveCheckBox.setObjectName(
            u"advancedIsRecuresiveCheckBox")
        self.advancedIsRecuresiveCheckBox.setEnabled(True)
        self.advancedIsRecuresiveCheckBox.setAutoFillBackground(False)
        self.advancedIsRecuresiveCheckBox.setChecked(True)

        self.third_layout_8.addWidget(
            self.advancedIsRecuresiveCheckBox, 2, 0, 1, 1)

        self.advancedIsCaseSensitiveCheckBox = QCheckBox(
            self.advancedTitleGroupBox)
        self.advancedIsCaseSensitiveCheckBox.setObjectName(
            u"advancedIsCaseSensitiveCheckBox")
        self.advancedIsCaseSensitiveCheckBox.setEnabled(True)
        self.advancedIsCaseSensitiveCheckBox.setAutoFillBackground(False)

        self.third_layout_8.addWidget(
            self.advancedIsCaseSensitiveCheckBox, 3, 0, 1, 1)

        self.advancedTitleLineEditeHSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.third_layout_8.addItem(
            self.advancedTitleLineEditeHSpacer, 2, 3, 1, 1)

        self.advancedTabMainVL.addWidget(self.advancedTitleGroupBox)

        self.advancedMetadataGroupBox = QGroupBox(self.ADVANCED)
        self.advancedMetadataGroupBox.setObjectName(
            u"advancedMetadataGroupBox")
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
        self.metadataComboBox2.setStyleSheet(
            u"background-color: rgb(33, 37, 43);")
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
        self.metadataComboBox.setStyleSheet(
            u"background-color: rgb(33, 37, 43);")
        self.metadataComboBox.setIconSize(QSize(16, 16))
        self.metadataComboBox.setFrame(True)

        self.third_layout_9.addWidget(self.metadataComboBox, 0, 0, 1, 1)

        self.metadataLineEditHSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.third_layout_9.addItem(self.metadataLineEditHSpacer, 1, 3, 1, 1)

        self.metadataComboBox3 = QComboBox(self.advancedMetadataGroupBox)
        self.metadataComboBox3.addItem("")
        self.metadataComboBox3.addItem("")
        self.metadataComboBox3.addItem("")
        self.metadataComboBox3.setObjectName(u"metadataComboBox3")
        self.metadataComboBox3.setFont(font)
        self.metadataComboBox3.setAutoFillBackground(False)
        self.metadataComboBox3.setStyleSheet(
            u"background-color: rgb(33, 37, 43);")
        self.metadataComboBox3.setIconSize(QSize(16, 16))
        self.metadataComboBox3.setFrame(True)

        self.third_layout_9.addWidget(self.metadataComboBox3, 0, 2, 1, 1)

        self.metadataLineEdit = QLineEdit(self.advancedMetadataGroupBox)
        self.metadataLineEdit.setObjectName(u"metadataLineEdit")
        self.metadataLineEdit.setMinimumSize(QSize(0, 30))
        self.metadataLineEdit.setStyleSheet(
            u"background-color: rgb(33, 37, 43);")
        self.metadataLineEdit.setMaxLength(100)

        self.third_layout_9.addWidget(self.metadataLineEdit, 0, 3, 1, 1)

        self.advancedTabMainVL.addWidget(self.advancedMetadataGroupBox)

        self.advancedOtherGroupBox = QGroupBox(self.ADVANCED)
        self.advancedOtherGroupBox.setObjectName(u"advancedOtherGroupBox")
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
        self.otherComboBox3.setStyleSheet(
            u"background-color: rgb(33, 37, 43);")
        self.otherComboBox3.setIconSize(QSize(16, 16))
        self.otherComboBox3.setFrame(True)

        self.third_layout_11.addWidget(self.otherComboBox3, 0, 2, 1, 1)

        self.otherLineEdit = QLineEdit(self.advancedOtherGroupBox)
        self.otherLineEdit.setObjectName(u"otherLineEdit")
        self.otherLineEdit.setMinimumSize(QSize(0, 30))
        self.otherLineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.otherLineEdit.setMaxLength(100)

        self.third_layout_11.addWidget(self.otherLineEdit, 0, 4, 1, 1)

        self.otherLineEditHSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.third_layout_11.addItem(self.otherLineEditHSpacer, 1, 4, 1, 1)

        self.otherComboBox2 = QComboBox(self.advancedOtherGroupBox)
        self.otherComboBox2.addItem("")
        self.otherComboBox2.addItem("")
        self.otherComboBox2.addItem("")
        self.otherComboBox2.addItem("")
        self.otherComboBox2.setObjectName(u"otherComboBox2")
        self.otherComboBox2.setFont(font)
        self.otherComboBox2.setAutoFillBackground(False)
        self.otherComboBox2.setStyleSheet(
            u"background-color: rgb(33, 37, 43);")
        self.otherComboBox2.setIconSize(QSize(16, 16))
        self.otherComboBox2.setFrame(True)

        self.third_layout_11.addWidget(self.otherComboBox2, 0, 1, 1, 1)

        self.advancedTabMainVL.addWidget(self.advancedOtherGroupBox)

        self.advancedBottomVSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        __qtablewidgetitem4.setFont(font4)
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
        __qtablewidgetitem12.setCheckState(Qt.Checked)
        self.table.setItem(0, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table.setItem(1, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table.setItem(1, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table.setItem(1, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setCheckState(Qt.Checked)
        self.table.setItem(1, 3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table.setItem(2, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table.setItem(2, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table.setItem(2, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setCheckState(Qt.Checked)
        self.table.setItem(2, 3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table.setItem(3, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table.setItem(3, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table.setItem(3, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setCheckState(Qt.Checked)
        self.table.setItem(3, 3, __qtablewidgetitem24)
        self.table.setObjectName(u"table")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.table.sizePolicy().hasHeightForWidth())
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
        self.deleteOptionBtn.setStyleSheet(
            u"background-color: rgb(52, 59, 72);")

        self.bottomHL.addWidget(self.deleteOptionBtn)

        self.renameOptionBtn = QPushButton(self.RESULT)
        self.renameOptionBtn.setObjectName(u"renameOptionBtn")
        self.renameOptionBtn.setEnabled(False)
        self.renameOptionBtn.setMinimumSize(QSize(150, 30))
        self.renameOptionBtn.setFont(font)
        self.renameOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.renameOptionBtn.setStyleSheet(
            u"background-color: rgb(52, 59, 72);")

        self.bottomHL.addWidget(self.renameOptionBtn)

        self.moveOptionBtn = QPushButton(self.RESULT)
        self.moveOptionBtn.setObjectName(u"moveOptionBtn")
        self.moveOptionBtn.setEnabled(False)
        self.moveOptionBtn.setMinimumSize(QSize(150, 30))
        self.moveOptionBtn.setFont(font)
        self.moveOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.moveOptionBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.bottomHL.addWidget(self.moveOptionBtn)

        self.duplicateOptionBtn = QPushButton(self.RESULT)
        self.duplicateOptionBtn.setObjectName(u"duplicateOptionBtn")
        self.duplicateOptionBtn.setEnabled(False)
        self.duplicateOptionBtn.setMinimumSize(QSize(150, 30))
        self.duplicateOptionBtn.setFont(font)
        self.duplicateOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.duplicateOptionBtn.setStyleSheet(
            u"background-color: rgb(52, 59, 72);")

        self.bottomHL.addWidget(self.duplicateOptionBtn)

        self.resultBottomLHSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomHL.addItem(self.resultBottomLHSpacer)

        self.resultTabMainVL.addLayout(self.bottomHL)

        self.verticalLayout_23.addLayout(self.resultTabMainVL)

        self.tabsWidget.addTab(self.RESULT, "")

        self.verticalLayout.addWidget(self.tabsWidget)

        self.searchGroup = QGroupBox(self.widgets)
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
        self.searchTypeComboBox.setStyleSheet(
            u"background-color: rgb(33, 37, 43);")
        self.searchTypeComboBox.setIconSize(QSize(16, 16))
        self.searchTypeComboBox.setFrame(True)

        self.topGL.addWidget(self.searchTypeComboBox, 0, 0, 1, 1)

        self.browsePathBtn = QPushButton(self.searchGroup)
        self.browsePathBtn.setObjectName(u"browsePathBtn")
        self.browsePathBtn.setMinimumSize(QSize(150, 30))
        self.browsePathBtn.setFont(font)
        self.browsePathBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browsePathBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

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
        self.startSearchBtn.setStyleSheet(
            u"background-color: rgb(52, 59, 72);")

        self.topGL.addWidget(self.startSearchBtn, 0, 3, 1, 1)

        self.searchMainVL.addLayout(self.topGL)

        self.foundMatchLabel = QLabel(self.searchGroup)
        self.foundMatchLabel.setObjectName(u"foundMatchLabel")
        self.foundMatchLabel.setAlignment(Qt.AlignCenter)

        self.searchMainVL.addWidget(self.foundMatchLabel)

        self.third_layout_7.addLayout(self.searchMainVL, 1, 0, 1, 1)

        self.verticalLayout.addWidget(self.searchGroup)

        # self.mainFrame.addWidget(self.widgets)

        # MainWindow.setCentralWidget(self.widgets)

        self.retranslateUi()
        self.titleGroupBox.toggled.connect(self.titleComboBox.setEnabled)
        self.titleGroupBox.toggled.connect(self.titleComboBox2.setEnabled)
        self.titleGroupBox.toggled.connect(self.titleComboBox3.setEnabled)
        self.titleGroupBox.toggled.connect(self.titleLineEdit.setEnabled)
        self.titleGroupBox.toggled.connect(self.isRecursiveCheckBox.setEnabled)
        self.titleGroupBox.toggled.connect(self.isCaseSensitiveCheckBox.setEnabled)

        # self.mainFrame.setCurrentIndex(1)
        self.tabsWidget.setCurrentIndex(0)

        # QMetaObject.connectSlotsByName(MainWindow)
        self.widgets.setObjectName("widgets")
        
        return self.widgets

    def retranslateUi(self):
        self.titleGroupBox.setTitle(QCoreApplication.translate(
            "MainWindow", u"TITLE LOOKUP", None))
        self.titleLineEdit.setText("")
        self.titleLineEdit.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Enter values to look for seperated by comma", None))
        self.titleComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"NAME", None))
        self.titleComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"EXTENSION", None))

        self.titleComboBox2.setItemText(
            0, QCoreApplication.translate("MainWindow", u"CONTAIN", None))
        self.titleComboBox2.setItemText(
            1, QCoreApplication.translate("MainWindow", u"EQUAL TO", None))

        self.titleComboBox3.setItemText(0, QCoreApplication.translate(
            "MainWindow", u"Alphabets only", None))
        self.titleComboBox3.setItemText(1, QCoreApplication.translate(
            "MainWindow", u"Alphabets & Symbols", None))
        self.titleComboBox3.setItemText(2, QCoreApplication.translate(
            "MainWindow", u"Alphabets & Numbers", None))
        self.titleComboBox3.setItemText(3, QCoreApplication.translate(
            "MainWindow", u"Alphabets Excluding", None))
        self.titleComboBox3.setItemText(
            4, QCoreApplication.translate("MainWindow", u"Numbers only", None))
        self.titleComboBox3.setItemText(5, QCoreApplication.translate(
            "MainWindow", u"Numbers & Symbols", None))
        self.titleComboBox3.setItemText(6, QCoreApplication.translate(
            "MainWindow", u"Numbers Excluding", None))
        self.titleComboBox3.setItemText(
            7, QCoreApplication.translate("MainWindow", u"Symbols only", None))
        self.titleComboBox3.setItemText(8, QCoreApplication.translate(
            "MainWindow", u"Symbols Excluding", None))
        self.titleComboBox3.setItemText(
            9, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.isRecursiveCheckBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Find files recursively through the selected path", None))
        self.isRecursiveCheckBox.setText(
            QCoreApplication.translate("MainWindow", u"RECURSIVE", None))
        self.isCaseSensitiveCheckBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Find files recursively through the selected path", None))
        self.isCaseSensitiveCheckBox.setText(
            QCoreApplication.translate("MainWindow", u"CASE SENSITIVE", None))
        self.tabsWidget.setTabText(self.tabsWidget.indexOf(
            self.BASIC), QCoreApplication.translate("MainWindow", u"BASIC", None))
        self.advancedTitleGroupBox.setTitle(
            QCoreApplication.translate("MainWindow", u"TITLE LOOKUP", None))
        self.advancedTitleLineEdite.setText("")
        self.advancedTitleLineEdite.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Enter values to look for seperated by comma", None))
        self.advancedTitleComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"NAME", None))
        self.advancedTitleComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"EXTENSION", None))

        self.advancedTitleComboBox2.setItemText(
            0, QCoreApplication.translate("MainWindow", u"CONTAIN", None))
        self.advancedTitleComboBox2.setItemText(
            1, QCoreApplication.translate("MainWindow", u"EQUAL TO", None))

        self.advancedTitleComboBox3.setItemText(
            0, QCoreApplication.translate("MainWindow", u"Alphabets only", None))
        self.advancedTitleComboBox3.setItemText(
            1, QCoreApplication.translate("MainWindow", u"Alphabets & Symbols", None))
        self.advancedTitleComboBox3.setItemText(
            2, QCoreApplication.translate("MainWindow", u"Alphabets & Numbers", None))
        self.advancedTitleComboBox3.setItemText(
            3, QCoreApplication.translate("MainWindow", u"Alphabets Excluding", None))
        self.advancedTitleComboBox3.setItemText(
            4, QCoreApplication.translate("MainWindow", u"Numbers only", None))
        self.advancedTitleComboBox3.setItemText(
            5, QCoreApplication.translate("MainWindow", u"Numbers & Symbols", None))
        self.advancedTitleComboBox3.setItemText(
            6, QCoreApplication.translate("MainWindow", u"Numbers Excluding", None))
        self.advancedTitleComboBox3.setItemText(
            7, QCoreApplication.translate("MainWindow", u"Symbols only", None))
        self.advancedTitleComboBox3.setItemText(
            8, QCoreApplication.translate("MainWindow", u"Symbols Excluding", None))
        self.advancedTitleComboBox3.setItemText(
            9, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.advancedIsRecuresiveCheckBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Find files recursively through the selected path", None))
        self.advancedIsRecuresiveCheckBox.setText(
            QCoreApplication.translate("MainWindow", u"RECURSIVE", None))
        self.advancedIsCaseSensitiveCheckBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Find files recursively through the selected path", None))
        self.advancedIsCaseSensitiveCheckBox.setText(
            QCoreApplication.translate("MainWindow", u"CASE SENSITIVE", None))

        self.advancedMetadataGroupBox.setTitle(
            QCoreApplication.translate("MainWindow", u"METADATA LOOKUP", None))
        self.metadataComboBox2.setItemText(
            0, QCoreApplication.translate("MainWindow", u"DIMENSIONS", None))
        self.metadataComboBox2.setItemText(
            1, QCoreApplication.translate("MainWindow", u"DURATION", None))
        self.metadataComboBox2.setItemText(
            2, QCoreApplication.translate("MainWindow", u"BIT RATE", None))
        self.metadataComboBox2.setItemText(
            3, QCoreApplication.translate("MainWindow", u"FRAME RATE", None))
        self.metadataComboBox2.setItemText(
            4, QCoreApplication.translate("MainWindow", u"FPS", None))

        self.metadataComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"VIDEO", None))
        self.metadataComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"IMAGE", None))
        self.metadataComboBox.setItemText(
            2, QCoreApplication.translate("MainWindow", u"AUDIO", None))
        self.metadataComboBox.setItemText(
            3, QCoreApplication.translate("MainWindow", u"DOCS", None))

        self.metadataComboBox3.setItemText(
            0, QCoreApplication.translate("MainWindow", u"1920x1080", None))
        self.metadataComboBox3.setItemText(
            1, QCoreApplication.translate("MainWindow", u"720x420", None))
        self.metadataComboBox3.setItemText(
            2, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.metadataLineEdit.setText("")
        self.metadataLineEdit.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Enter values to look for seperated by comma", None))
        self.advancedOtherGroupBox.setTitle(
            QCoreApplication.translate("MainWindow", u"OTHER LOOKUPS", None))
        self.otherComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"SIZE", None))
        self.otherComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"DATE CREATED", None))

        self.otherComboBox3.setItemText(
            0, QCoreApplication.translate("MainWindow", u"EQUAL TO", None))
        self.otherComboBox3.setItemText(
            1, QCoreApplication.translate("MainWindow", u"LESS THAN", None))
        self.otherComboBox3.setItemText(
            2, QCoreApplication.translate("MainWindow", u"GREATER THAN", None))

        self.otherLineEdit.setText("")
        self.otherLineEdit.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Enter values to look for seperated by comma", None))
        self.otherComboBox2.setItemText(
            0, QCoreApplication.translate("MainWindow", u"BYTES", None))
        self.otherComboBox2.setItemText(
            1, QCoreApplication.translate("MainWindow", u"KILOBYTES", None))
        self.otherComboBox2.setItemText(
            2, QCoreApplication.translate("MainWindow", u"MEGABYTES", None))
        self.otherComboBox2.setItemText(
            3, QCoreApplication.translate("MainWindow", u"GIGABYTES", None))

        self.tabsWidget.setTabText(self.tabsWidget.indexOf(
            self.ADVANCED), QCoreApplication.translate("MainWindow", u"ADVANCED", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"1", None))
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"2", None))
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", u"3", None))
        ___qtablewidgetitem4 = self.table.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"New Row", None))
        ___qtablewidgetitem5 = self.table.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", u"New Row", None))
        ___qtablewidgetitem6 = self.table.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate("MainWindow", u"New Row", None))
        ___qtablewidgetitem7 = self.table.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindow", u"New Row", None))
        ___qtablewidgetitem8 = self.table.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate("MainWindow", u"New Row", None))

        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.table.item(0, 0)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("MainWindow", u"Test", None))
        ___qtablewidgetitem10 = self.table.item(0, 1)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate("MainWindow", u"Text", None))
        ___qtablewidgetitem11 = self.table.item(0, 2)
        ___qtablewidgetitem11.setText(
            QCoreApplication.translate("MainWindow", u"Cell", None))
        ___qtablewidgetitem12 = self.table.item(0, 3)
        ___qtablewidgetitem12.setText(
            QCoreApplication.translate("MainWindow", u"SELECT", None))
        ___qtablewidgetitem13 = self.table.item(1, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate(
            "MainWindow", u"test (c 0, r 0)", None))
        ___qtablewidgetitem14 = self.table.item(1, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate(
            "MainWindow", u"test (c 1, r 0)", None))
        ___qtablewidgetitem15 = self.table.item(1, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate(
            "MainWindow", u"test (c 2, r 0)", None))
        ___qtablewidgetitem16 = self.table.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate(
            "MainWindow", u"test (c 0, r 1)", None))
        ___qtablewidgetitem17 = self.table.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate(
            "MainWindow", u"test (c 1, r 1)", None))
        ___qtablewidgetitem18 = self.table.item(2, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate(
            "MainWindow", u"test (c 2, r 1)", None))
        ___qtablewidgetitem19 = self.table.item(3, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate(
            "MainWindow", u"test (c 0, r 2)", None))
        ___qtablewidgetitem20 = self.table.item(3, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate(
            "MainWindow", u"test (c 1, r 2)", None))
        ___qtablewidgetitem21 = self.table.item(3, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate(
            "MainWindow", u"test (c 2 r 2)", None))
        self.table.setSortingEnabled(__sortingEnabled)

        self.deleteOptionBtn.setText(
            QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.renameOptionBtn.setText(
            QCoreApplication.translate("MainWindow", u"RENAME", None))
        self.moveOptionBtn.setText(
            QCoreApplication.translate("MainWindow", u"MOVE", None))
        self.duplicateOptionBtn.setText(
            QCoreApplication.translate("MainWindow", u"DUPLICATE", None))
        self.tabsWidget.setTabText(self.tabsWidget.indexOf(
            self.RESULT), QCoreApplication.translate("MainWindow", u"RESULT", None))
        self.searchGroup.setTitle(
            QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.searchTypeComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"FILES", None))
        self.searchTypeComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"FOLDERS", None))

        self.browsePathBtn.setText(
            QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.pathLineEdit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Enter the path where should the lookup process begin", None))
        self.pathLineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"DIRECTORY PATH...", None))
        self.startSearchBtn.setText(
            QCoreApplication.translate("MainWindow", u"START ", None))
        self.foundMatchLabel.setText(QCoreApplication.translate(
            "MainWindow", u"FOUND 0 MATCHES ", None))
