
from PySide6.QtCore import (
    QCoreApplication, QSize, Qt
)
from PySide6.QtGui import (
    QBrush, QColor, QCursor, QFont, QPalette
)
from PySide6.QtWidgets import (
    QAbstractItemView, QAbstractScrollArea, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout,  QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget
)

from Interface.environment import Common


class Ui(Common):

    def __init__(self) -> None:
        super().__init__()

    def render_page(self):

        self.widgets = QWidget()

        """
        ===================================================================
                            WIDGETS RENDERING 
        ===================================================================
        """
        self.topGL = QGridLayout()
        self.bottomHL = QHBoxLayout()
        self.searchMainVL = QVBoxLayout()

        # __________   MAIN LAYOUT   ____________________________

        self.tabsWidget = QTabWidget(self.widgets)
        self.verticalLayout = QVBoxLayout(self.widgets)

        self.searchGroupBox = QGroupBox(self.widgets)
        self.searchGroupBoxGL = QGridLayout(self.searchGroupBox)
        self.foundMatchLabel = QLabel(self.searchGroupBox)
        self.pathLineEdit = QLineEdit(self.searchGroupBox)
        self.browsePathBtn = QPushButton(self.searchGroupBox)
        self.startSearchBtn = QPushButton(self.searchGroupBox)
        self.searchTypeComboBox = QComboBox(self.searchGroupBox)

        # __________   BASIC TAB   ______________________________

        self.BASIC = QWidget()
        self.basicTabMainVL = QVBoxLayout()
        self.titleGroupBox = QGroupBox(self.BASIC)
        self.verticalLayout3 = QVBoxLayout(self.BASIC)

        self.titleLineEdit = QLineEdit(self.titleGroupBox)
        self.titleComboBox = QComboBox(self.titleGroupBox)
        self.titleComboBox2 = QComboBox(self.titleGroupBox)
        self.titleComboBox3 = QComboBox(self.titleGroupBox)
        self.titleGroupBoxGL = QGridLayout(self.titleGroupBox)
        self.isRecursiveCheckBox = QCheckBox(self.titleGroupBox)
        self.isCaseSensitiveCheckBox = QCheckBox(self.titleGroupBox)

        # __________   ADVANCED TAB   ____________________________

        self.ADVANCED = QWidget()
        self.advancedTabMainVL = QVBoxLayout()
        self.advancedTitleGroupBox = QGroupBox(self.ADVANCED)

        self.verticalLayout2 = QVBoxLayout(self.ADVANCED)
        self.advancedTitleGroupBoxGL = QGridLayout(self.advancedTitleGroupBox)

        self.advancedTitleLineEdite = QLineEdit(self.advancedTitleGroupBox)
        self.advancedTitleComboBox = QComboBox(self.advancedTitleGroupBox)
        self.advancedTitleComboBox2 = QComboBox(self.advancedTitleGroupBox)
        self.advancedTitleComboBox3 = QComboBox(self.advancedTitleGroupBox)
        self.advancedIsRecuresiveCheckBox = QCheckBox(
            self.advancedTitleGroupBox)
        self.advancedIsCaseSensitiveCheckBox = QCheckBox(
            self.advancedTitleGroupBox)

        self.advancedMetadataGroupBox = QGroupBox(self.ADVANCED)
        self.advancedMetadataGroupBoxGL = QGridLayout(
            self.advancedMetadataGroupBox)
        self.metadataLineEdit = QLineEdit(self.advancedMetadataGroupBox)
        self.metadataComboBox = QComboBox(self.advancedMetadataGroupBox)
        self.metadataComboBox2 = QComboBox(self.advancedMetadataGroupBox)
        self.metadataComboBox3 = QComboBox(self.advancedMetadataGroupBox)

        self.advancedOtherGroupBox = QGroupBox(self.ADVANCED)
        self.advancedOtherGroupBoxGL = QGridLayout(self.advancedOtherGroupBox)
        self.otherLineEdit = QLineEdit(self.advancedOtherGroupBox)
        self.otherComboBox = QComboBox(self.advancedOtherGroupBox)
        self.otherComboBox3 = QComboBox(self.advancedOtherGroupBox)
        self.otherComboBox2 = QComboBox(self.advancedOtherGroupBox)

        # __________   RESULT TAB   ______________________________

        self.RESULT = QWidget()
        self.resultTabMainVL = QVBoxLayout()
        self.table = QTableWidget(self.RESULT)
        self.moveOptionBtn = QPushButton(self.RESULT)
        self.deleteOptionBtn = QPushButton(self.RESULT)
        self.renameOptionBtn = QPushButton(self.RESULT)
        self.verticalLayout4 = QVBoxLayout(self.RESULT)
        self.duplicateOptionBtn = QPushButton(self.RESULT)


        self.titleLineEditHSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.tabsVSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.tabsWidget.addTab(self.BASIC, "")
        self.tabsWidget.addTab(self.ADVANCED, "")
        self.tabsWidget.addTab(self.RESULT, "")


        self.advancedTitleLineEditeHSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.metadataLineEditHSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)


        self.otherLineEditHSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.advancedBottomVSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

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

        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy3)

        """
        ===================================================================
                           PALLETE AND BRUSHES
        ===================================================================
        """

        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)

        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)

        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)

        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)

        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)

        self.table.setFrameShape(QFrame.NoFrame)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setGridStyle(Qt.SolidLine)
        self.table.setShowGrid(True)
        self.table.setSortingEnabled(True)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setDefaultSectionSize(200)
        self.table.verticalHeader().setHighlightSections(False)
        self.table.verticalHeader().setStretchLastSection(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setCascadingSectionResizes(True)

        self.bottomHL.setContentsMargins(-1, 0, -1, -1)

        self.resultBottomLHSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.searchTypeComboBox.addItem("")
        self.searchTypeComboBox.addItem("")

        """
        ===================================================================
                            SET STYLING
        ===================================================================
        """
        self.searchMainVL.setSpacing(5)
        self.verticalLayout.setSpacing(10)
        self.advancedTabMainVL.setSpacing(10)

        self.otherLineEdit.setMaxLength(100)
        self.titleLineEdit.setMaxLength(100)
        self.metadataLineEdit.setMaxLength(100)
        self.advancedTitleLineEdite.setMaxLength(100)

        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.titleGroupBoxGL.setContentsMargins(10, 20, 10, 10)
        self.advancedTitleGroupBoxGL.setContentsMargins(10, 20, 10, 10)
        self.advancedMetadataGroupBoxGL.setContentsMargins(10, 20, 10, 0)
        self.advancedOtherGroupBoxGL.setContentsMargins(10, 20, 10, 0)

        self.otherComboBox.setIconSize(QSize(16, 16))
        self.titleComboBox.setIconSize(QSize(16, 16))
        self.titleComboBox2.setIconSize(QSize(16, 16))
        self.titleComboBox3.setIconSize(QSize(16, 16))
        self.otherComboBox2.setIconSize(QSize(16, 16))
        self.otherComboBox3.setIconSize(QSize(16, 16))
        self.metadataComboBox.setIconSize(QSize(16, 16))
        self.metadataComboBox2.setIconSize(QSize(16, 16))
        self.metadataComboBox3.setIconSize(QSize(16, 16))
        self.searchTypeComboBox.setIconSize(QSize(16, 16))
        self.advancedTitleComboBox.setIconSize(QSize(16, 16))
        self.advancedTitleComboBox2.setIconSize(QSize(16, 16))
        self.advancedTitleComboBox3.setIconSize(QSize(16, 16))

        self.pathLineEdit.setMinimumSize(QSize(0, 30))
        self.titleLineEdit.setMinimumSize(QSize(0, 30))
        self.otherLineEdit.setMinimumSize(QSize(0, 30))
        self.moveOptionBtn.setMinimumSize(QSize(150, 30))
        self.browsePathBtn.setMinimumSize(QSize(150, 30))
        self.startSearchBtn.setMinimumSize(QSize(150, 30))
        self.metadataLineEdit.setMinimumSize(QSize(0, 30))
        self.deleteOptionBtn.setMinimumSize(QSize(150, 30))
        self.renameOptionBtn.setMinimumSize(QSize(150, 30))
        self.duplicateOptionBtn.setMinimumSize(QSize(150, 30))
        self.advancedTitleLineEdite.setMinimumSize(QSize(0, 30))

        self.moveOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browsePathBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.startSearchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.renameOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.duplicateOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.moveOptionBtn.setStyleSheet(
            self.html.get_bg_color("light blue")
        )
        self.browsePathBtn.setStyleSheet(
            self.html.get_bg_color("light blue")
        )
        self.startSearchBtn.setStyleSheet(
            self.html.get_bg_color("light blue")
        )
        self.deleteOptionBtn.setStyleSheet(
            self.html.get_bg_color("light blue")
        )
        self.renameOptionBtn.setStyleSheet(
            self.html.get_bg_color("light blue")
        )
        self.duplicateOptionBtn.setStyleSheet(
            self.html.get_bg_color("light blue")
        )
        self.pathLineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.otherComboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.otherLineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.titleLineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.titleComboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.otherComboBox3.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.otherComboBox2.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.titleComboBox2.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.titleComboBox3.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.metadataLineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.metadataComboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.metadataComboBox2.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.metadataComboBox3.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.searchTypeComboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.advancedTitleComboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.advancedTitleLineEdite.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.advancedTitleComboBox2.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.advancedTitleComboBox3.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.foundMatchLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout3.addLayout(
            self.basicTabMainVL
        )

        self.searchMainVL.addLayout(
            self.topGL
        )
        self.searchGroupBoxGL.addLayout(
            self.searchMainVL, 1, 0, 1, 1
        )
        self.verticalLayout2.addLayout(
            self.advancedTabMainVL
        )
        self.resultTabMainVL.addLayout(
            self.bottomHL
        )
        self.verticalLayout4.addLayout(
            self.resultTabMainVL
        )

        self.searchGroupBoxGL.setContentsMargins(10, 20, 10, 10)
        self.topGL.setContentsMargins(-1, 2, -1, 0)

        self.titleGroupBoxGL.addWidget(
            self.titleLineEdit, 0, 3, 1, 1
        )
        self.titleGroupBoxGL.addWidget(
            self.titleComboBox, 0, 0, 1, 1
        )
        self.titleGroupBoxGL.addWidget(
            self.titleComboBox2, 0, 1, 1, 1
        )
        self.titleGroupBoxGL.addWidget(
            self.titleComboBox3, 0, 2, 1, 1
        )
        self.titleGroupBoxGL.addWidget(
            self.isRecursiveCheckBox, 2, 0, 1, 1
        )
        self.titleGroupBoxGL.addWidget(
            self.isCaseSensitiveCheckBox, 3, 0, 1, 1
        )
        self.basicTabMainVL.addWidget(
            self.titleGroupBox
        )
        self.advancedTitleGroupBoxGL.addWidget(
            self.advancedTitleLineEdite, 0, 3, 1, 1
        )
        self.advancedTitleGroupBoxGL.addWidget(
            self.advancedTitleComboBox, 0, 0, 1, 1
        )
        self.advancedTitleGroupBoxGL.addWidget(
            self.advancedTitleComboBox2, 0, 1, 1, 1
        )
        self.advancedTabMainVL.addWidget(
            self.advancedTitleGroupBox
        )
        self.advancedTabMainVL.addWidget(
            self.advancedMetadataGroupBox
        )
        self.advancedTitleGroupBoxGL.addWidget(
            self.advancedTitleComboBox3, 0, 2, 1, 1
        )
        self.advancedTitleGroupBoxGL.addWidget(
            self.advancedIsRecuresiveCheckBox, 2, 0, 1, 1
        )
        self.advancedTitleGroupBoxGL.addWidget(
            self.advancedIsCaseSensitiveCheckBox, 3, 0, 1, 1
        )
        self.advancedMetadataGroupBoxGL.addWidget(
            self.metadataComboBox2, 0, 1, 1, 1
        )
        self.advancedMetadataGroupBoxGL.addWidget(
            self.metadataComboBox, 0, 0, 1, 1
        )
        self.advancedMetadataGroupBoxGL.addWidget(
            self.metadataComboBox3, 0, 2, 1, 1
        )
        self.advancedMetadataGroupBoxGL.addWidget(
            self.metadataLineEdit, 0, 3, 1, 1
        )
        self.advancedOtherGroupBoxGL.addWidget(
            self.otherComboBox, 0, 0, 1, 1
        )
        self.advancedOtherGroupBoxGL.addWidget(
            self.otherComboBox3, 0, 2, 1, 1
        )
        self.advancedOtherGroupBoxGL.addWidget(
            self.otherLineEdit, 0, 4, 1, 1
        )
        self.advancedOtherGroupBoxGL.addWidget(
            self.otherComboBox2, 0, 1, 1, 1
        )
        self.advancedTabMainVL.addWidget(
            self.advancedOtherGroupBox
        )
        self.resultTabMainVL.addWidget(
            self.table
        )
        self.bottomHL.addWidget(
            self.deleteOptionBtn
        )
        self.bottomHL.addWidget(
            self.renameOptionBtn
        )
        self.bottomHL.addWidget(
            self.moveOptionBtn
        )
        self.bottomHL.addWidget(
            self.duplicateOptionBtn
        )
        self.verticalLayout.addWidget(
            self.tabsWidget
        )
        self.verticalLayout.addWidget(
            self.searchGroupBox
        )
        self.searchMainVL.addWidget(
            self.foundMatchLabel
        )
        self.topGL.addWidget(
            self.pathLineEdit, 0, 1, 1, 1
        )
        self.topGL.addWidget(
            self.browsePathBtn, 0, 2, 1, 1
        )
        self.topGL.addWidget(
            self.startSearchBtn, 0, 3, 1, 1
        )
        self.topGL.addWidget(
            self.searchTypeComboBox, 0, 0, 1, 1
        )
        self.bottomHL.addItem(
            self.resultBottomLHSpacer
        )
        self.titleGroupBoxGL.addItem(
            self.titleLineEditHSpacer, 2, 3, 1, 1
        )
        self.basicTabMainVL.addItem(
            self.tabsVSpacer
        )
        self.advancedTitleGroupBoxGL.addItem(
            self.advancedTitleLineEditeHSpacer, 2, 3, 1, 1
        )
        self.advancedMetadataGroupBoxGL.addItem(
            self.metadataLineEditHSpacer, 1, 3, 1, 1
        )
        self.advancedOtherGroupBoxGL.addItem(
            self.otherLineEditHSpacer, 1, 4, 1, 1
        )
        self.advancedTabMainVL.addItem(
            self.advancedBottomVSpacer
        )

        """
        ===================================================================
                            TOGGLE GROUPS
        ===================================================================
        """

        self.titleGroupBox.toggled.connect(self.titleComboBox.setEnabled)
        self.titleGroupBox.toggled.connect(self.titleLineEdit.setEnabled)
        self.titleGroupBox.toggled.connect(self.titleComboBox2.setEnabled)
        self.titleGroupBox.toggled.connect(self.titleComboBox3.setEnabled)
        self.titleGroupBox.toggled.connect(self.isRecursiveCheckBox.setEnabled)
        self.titleGroupBox.toggled.connect(
            self.isCaseSensitiveCheckBox.setEnabled)

        self.tabsWidget.setCurrentIndex(0)

        self.titleComboBox.setFrame(True)
        self.otherComboBox.setFrame(True)
        self.titleComboBox2.setFrame(True)
        self.titleComboBox3.setFrame(True)
        self.otherComboBox3.setFrame(True)
        self.otherComboBox2.setFrame(True)
        self.metadataComboBox.setFrame(True)
        self.metadataComboBox2.setFrame(True)
        self.metadataComboBox3.setFrame(True)
        self.searchTypeComboBox.setFrame(True)
        self.advancedTitleComboBox.setFrame(True)
        self.advancedTitleComboBox2.setFrame(True)
        self.advancedTitleComboBox3.setFrame(True)

        self.titleGroupBox.setFlat(False)
        self.advancedTitleGroupBox.setFlat(False)
        self.advancedOtherGroupBox.setFlat(False)
        self.advancedMetadataGroupBox.setFlat(False)

        self.titleGroupBox.setCheckable(True)
        self.advancedTitleGroupBox.setCheckable(True)
        self.advancedOtherGroupBox.setCheckable(True)
        self.advancedMetadataGroupBox.setCheckable(True)
        
        self.titleGroupBox.setChecked(True)
        self.searchGroupBox.setChecked(False)
        self.isRecursiveCheckBox.setChecked(True)
        self.advancedOtherGroupBox.setChecked(False)
        self.advancedMetadataGroupBox.setChecked(False)
        self.advancedIsRecuresiveCheckBox.setChecked(True)


        self.moveOptionBtn.setEnabled(False)
        self.deleteOptionBtn.setEnabled(False)
        self.renameOptionBtn.setEnabled(False)
        self.duplicateOptionBtn.setEnabled(False)
        self.isRecursiveCheckBox.setEnabled(True)
        self.isCaseSensitiveCheckBox.setEnabled(True)
        self.advancedIsRecuresiveCheckBox.setEnabled(True)
        self.advancedIsCaseSensitiveCheckBox.setEnabled(True)
        
        self.titleComboBox.addItem("")
        self.titleComboBox.addItem("")

        self.titleComboBox2.addItem("")
        self.titleComboBox2.addItem("")

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
        
        self.advancedTitleComboBox.addItem("")
        self.advancedTitleComboBox.addItem("")

        self.advancedTitleComboBox2.addItem("")
        self.advancedTitleComboBox2.addItem("")

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

        self.metadataComboBox.addItem("")
        self.metadataComboBox.addItem("")
        self.metadataComboBox.addItem("")
        self.metadataComboBox.addItem("")
        
        self.metadataComboBox2.addItem("")
        self.metadataComboBox2.addItem("")
        self.metadataComboBox2.addItem("")
        self.metadataComboBox2.addItem("")
        self.metadataComboBox2.addItem("")

        self.metadataComboBox3.addItem("")
        self.metadataComboBox3.addItem("")
        self.metadataComboBox3.addItem("")

        self.otherComboBox.addItem("")
        self.otherComboBox.addItem("")

        self.otherComboBox2.addItem("")
        self.otherComboBox2.addItem("")
        self.otherComboBox2.addItem("")
        self.otherComboBox2.addItem("")

        self.otherComboBox3.addItem("")
        self.otherComboBox3.addItem("")
        self.otherComboBox3.addItem("")

        self.retranslateUi()
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
        self.searchGroupBox.setTitle(
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
