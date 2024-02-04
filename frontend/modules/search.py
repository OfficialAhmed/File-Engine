
from PySide6.QtCore import QCoreApplication, QSize, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout,  QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget, QVBoxLayout, QWidget
)

from backend.search import Response
from frontend.environment import tables


class Ui(Response):
    """
        UI RENDERING AND TRANSLATING TEXTS
    """

    def __init__(self) -> None:
        super().__init__()

        # fmt: off
        self.widgets = QWidget()
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

        self.advancedTitleLineEdit = QLineEdit(self.advancedTitleGroupBox)
        self.advancedTitleComboBox = QComboBox(self.advancedTitleGroupBox)
        self.advancedTitleComboBox2 = QComboBox(self.advancedTitleGroupBox)
        self.advancedTitleComboBox3 = QComboBox(self.advancedTitleGroupBox)
        self.advancedIsRecuresiveCheckBox = QCheckBox(self.advancedTitleGroupBox)
        self.advancedIsCaseSensitiveCheckBox = QCheckBox(self.advancedTitleGroupBox)

        self.advancedMetadataGroupBox = QGroupBox(self.ADVANCED)
        self.advancedMetadataGroupBoxGL = QGridLayout(self.advancedMetadataGroupBox)
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
        self.tableWidget = QTableWidget(self.RESULT)
        self.moveOptionBtn = QPushButton(self.RESULT)
        self.deleteOptionBtn = QPushButton(self.RESULT)
        self.renameOptionBtn = QPushButton(self.RESULT)
        self.verticalLayout4 = QVBoxLayout(self.RESULT)
        self.duplicateOptionBtn = QPushButton(self.RESULT)

        self.titleLineEditHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.tabsVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tabsWidget.addTab(self.BASIC, "")
        self.tabsWidget.addTab(self.ADVANCED, "")
        self.tabsWidget.addTab(self.RESULT, "")
        
        self.tabsWidget.setTabEnabled(1, False)

        self.advancedTitleLineEditeHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.metadataLineEditHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.otherLineEditHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.advancedBottomVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.set_controller_widgets(
            self.searchTypeComboBox,
            self.pathLineEdit,
            self.titleComboBox,
            self.pathLineEdit,
            self.isRecursiveCheckBox,
            self.startSearchBtn
        )

        tables["SEARCH"].render(self.tableWidget)
        self.resultBottomLHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)


        """
        ===================================================================
                            SET STYLING
        ===================================================================
        """

        size = (20, 20)

        self.set_icon(self.browsePathBtn, "folder_outline", size)

        self.searchMainVL.setSpacing(5)
        self.verticalLayout.setSpacing(10)
        self.advancedTabMainVL.setSpacing(10)

        self.otherLineEdit.setMaxLength(100)
        self.titleLineEdit.setMaxLength(100)
        self.metadataLineEdit.setMaxLength(100)
        self.advancedTitleLineEdit.setMaxLength(100)

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
        self.advancedTitleLineEdit.setMinimumSize(QSize(0, 30))

        self.moveOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browsePathBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.startSearchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.renameOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.duplicateOptionBtn.setCursor(QCursor(Qt.PointingHandCursor))

        color = self.html.get_bg_color("light blue")
        self.moveOptionBtn.setStyleSheet(color)
        self.browsePathBtn.setStyleSheet(color)
        self.startSearchBtn.setStyleSheet(color)
        self.deleteOptionBtn.setStyleSheet(color)
        self.renameOptionBtn.setStyleSheet(color)
        self.duplicateOptionBtn.setStyleSheet(color)

        color = self.html.get_bg_color("dark blue")
        self.pathLineEdit.setStyleSheet(color)
        self.otherComboBox.setStyleSheet(color)
        self.otherLineEdit.setStyleSheet(color)
        self.titleLineEdit.setStyleSheet(color)
        self.titleComboBox.setStyleSheet(color)
        self.otherComboBox3.setStyleSheet(color)
        self.otherComboBox2.setStyleSheet(color)
        self.titleComboBox2.setStyleSheet(color)
        self.titleComboBox3.setStyleSheet(color)
        self.metadataLineEdit.setStyleSheet(color)
        self.metadataComboBox.setStyleSheet(color)
        self.metadataComboBox2.setStyleSheet(color)
        self.metadataComboBox3.setStyleSheet(color)
        self.searchTypeComboBox.setStyleSheet(color)
        self.advancedTitleComboBox.setStyleSheet(color)
        self.advancedTitleLineEdit.setStyleSheet(color)
        self.advancedTitleComboBox2.setStyleSheet(color)
        self.advancedTitleComboBox3.setStyleSheet(color)

        self.foundMatchLabel.setAlignment(Qt.AlignCenter)
        self.verticalLayout3.addLayout(self.basicTabMainVL)

        self.searchMainVL.addLayout(self.topGL)
        self.searchGroupBoxGL.addLayout(self.searchMainVL, 1, 0, 1, 1)
        self.verticalLayout2.addLayout(self.advancedTabMainVL)
        self.resultTabMainVL.addLayout(self.bottomHL)
        self.verticalLayout4.addLayout(self.resultTabMainVL)

        self.searchGroupBoxGL.setContentsMargins(10, 20, 10, 10)
        self.topGL.setContentsMargins(-1, 2, -1, 0)

        self.titleGroupBoxGL.addWidget(self.titleLineEdit, 0, 3, 1, 1)
        self.titleGroupBoxGL.addWidget(self.titleComboBox, 0, 0, 1, 1)
        self.titleGroupBoxGL.addWidget(self.titleComboBox2, 0, 1, 1, 1)
        self.titleGroupBoxGL.addWidget(self.titleComboBox3, 0, 2, 1, 1)
        self.titleGroupBoxGL.addWidget(self.isRecursiveCheckBox, 2, 0, 1, 1)
        self.titleGroupBoxGL.addWidget(self.isCaseSensitiveCheckBox, 3, 0, 1, 1)
        self.basicTabMainVL.addWidget(self.titleGroupBox)
        self.advancedTitleGroupBoxGL.addWidget(self.advancedTitleLineEdit, 0, 3, 1, 1)
        self.advancedTitleGroupBoxGL.addWidget(self.advancedTitleComboBox, 0, 0, 1, 1)
        self.advancedTitleGroupBoxGL.addWidget(self.advancedTitleComboBox2, 0, 1, 1, 1)
        self.advancedTabMainVL.addWidget(self.advancedTitleGroupBox)
        self.advancedTabMainVL.addWidget(self.advancedMetadataGroupBox)
        self.advancedTitleGroupBoxGL.addWidget(self.advancedTitleComboBox3, 0, 2, 1, 1)
        self.advancedTitleGroupBoxGL.addWidget(self.advancedIsRecuresiveCheckBox, 2, 0, 1, 1)
        self.advancedTitleGroupBoxGL.addWidget(self.advancedIsCaseSensitiveCheckBox, 3, 0, 1, 1)
        self.advancedMetadataGroupBoxGL.addWidget(self.metadataComboBox2, 0, 1, 1, 1)
        self.advancedMetadataGroupBoxGL.addWidget(self.metadataComboBox, 0, 0, 1, 1)
        self.advancedMetadataGroupBoxGL.addWidget(self.metadataComboBox3, 0, 2, 1, 1)
        self.advancedMetadataGroupBoxGL.addWidget(self.metadataLineEdit, 0, 3, 1, 1)
        self.advancedOtherGroupBoxGL.addWidget(self.otherComboBox, 0, 0, 1, 1)
        self.advancedOtherGroupBoxGL.addWidget(self.otherComboBox3, 0, 2, 1, 1)
        self.advancedOtherGroupBoxGL.addWidget(self.otherLineEdit, 0, 4, 1, 1)
        self.advancedOtherGroupBoxGL.addWidget(self.otherComboBox2, 0, 1, 1, 1)
        self.advancedTabMainVL.addWidget(self.advancedOtherGroupBox)
        self.resultTabMainVL.addWidget(self.tableWidget)
        self.bottomHL.addWidget(self.deleteOptionBtn)
        self.bottomHL.addWidget(self.renameOptionBtn)
        self.bottomHL.addWidget(self.moveOptionBtn)
        self.bottomHL.addWidget(self.duplicateOptionBtn)
        self.verticalLayout.addWidget(self.tabsWidget)
        self.verticalLayout.addWidget(self.searchGroupBox)
        self.searchMainVL.addWidget(self.foundMatchLabel)
        self.topGL.addWidget(self.pathLineEdit, 0, 1, 1, 1)
        self.topGL.addWidget(self.browsePathBtn, 0, 2, 1, 1)
        self.topGL.addWidget(self.startSearchBtn, 0, 3, 1, 1)
        self.topGL.addWidget(self.searchTypeComboBox, 0, 0, 1, 1)
        self.bottomHL.addItem(self.resultBottomLHSpacer)
        self.titleGroupBoxGL.addItem(self.titleLineEditHSpacer, 2, 3, 1, 1)
        self.basicTabMainVL.addItem(self.tabsVSpacer)
        self.advancedTitleGroupBoxGL.addItem(self.advancedTitleLineEditeHSpacer, 2, 3, 1, 1)
        self.advancedMetadataGroupBoxGL.addItem(self.metadataLineEditHSpacer, 1, 3, 1, 1)
        self.advancedOtherGroupBoxGL.addItem(self.otherLineEditHSpacer, 1, 4, 1, 1)
        self.advancedTabMainVL.addItem(self.advancedBottomVSpacer)

        """
        ===================================================================
                            SET DISPLAY RULES
        ===================================================================
        """

        self.tabsWidget.setCurrentIndex(0)

        self.titleLineEdit.setHidden(True)
        self.metadataLineEdit.setHidden(True)
        self.advancedTitleLineEdit.setHidden(True)

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

        default_options = {

            # _____   BASIC  ________
            # _____   TITLE  ________
            self.titleComboBox: tuple(self.title_options.keys()),
            self.titleComboBox2: tuple(self.title_options["NAME"].keys()),
            self.titleComboBox3: tuple(self.title_options["NAME"]["CONTAIN"]),

            # _____   ADVANCED  ________
            # _____   TITLE  ________
            self.advancedTitleComboBox: tuple(self.title_options.keys()),
            self.advancedTitleComboBox2: tuple(self.title_options["NAME"].keys()),
            self.advancedTitleComboBox3: tuple(self.title_options["NAME"]["CONTAIN"]),

            # _____   METADATA  ________
            self.metadataComboBox: tuple(self.metadata_options.keys()),
            self.metadataComboBox2: tuple(self.metadata_options["VIDEO"].keys()),
            self.metadataComboBox3: tuple(self.metadata_options["VIDEO"]["DIMENSIONS"]),

            # _____   OTHER  ________
            self.otherComboBox: tuple(self.other_options.keys()),
            self.otherComboBox2: tuple(self.other_options["SIZE"].keys()),
            self.otherComboBox3: tuple(self.other_options["SIZE"]["BYTES"]),

            self.searchTypeComboBox: ("FILES", "FOLDERS")
        }

        for cb, values in default_options.items():
            for val in values:
                cb.addItem(val)

        """
        ===================================================================
                            SIGNALS AND CONNECTIONS
        ===================================================================
        """

        self.titleGroupBox.toggled.connect(self.titleComboBox.setEnabled)
        self.titleGroupBox.toggled.connect(self.titleLineEdit.setEnabled)
        self.titleGroupBox.toggled.connect(self.titleComboBox2.setEnabled)
        self.titleGroupBox.toggled.connect(self.titleComboBox3.setEnabled)
        self.titleGroupBox.toggled.connect(self.isRecursiveCheckBox.setEnabled)
        self.titleGroupBox.toggled.connect(self.isCaseSensitiveCheckBox.setEnabled)

        self.startSearchBtn.clicked.connect(
            lambda: self.start_search_clicked()
        )
        self.browsePathBtn.clicked.connect(
            lambda: self.set_user_path(
                self.get_path(),
                False
            )
        )

        # _________________         TITLE-GROUP BEHAVIOUR       ____________________
        self.titleComboBox.currentTextChanged.connect(
            lambda: self.title_cb_changed()
        )
        self.titleComboBox2.currentTextChanged.connect(
            lambda: self.title_cb2_changed()
        )
        self.titleComboBox3.currentTextChanged.connect(
            lambda: self.title_cb3_changed()
        )

        # _________________    ADVANCED TITLE-GROUP BEHAVIOUR   ________________
        self.advancedTitleComboBox2.currentTextChanged.connect(
            lambda: self.title_cb2_changed("advanced")
        )
        self.advancedTitleComboBox3.currentTextChanged.connect(
            lambda: self.title_cb3_changed("advanced")
        )

        # _________________    ADVANCED METADATA-GROUP BEHAVIOUR   ______________
        self.metadataComboBox.currentTextChanged.connect(
            lambda: self.md_option_changed(1)
        )
        self.metadataComboBox2.currentTextChanged.connect(
            lambda: self.md_option_changed(2)
        )
        self.metadataComboBox3.currentTextChanged.connect(
            lambda: self.md_option_changed(3)
        )

        # _________________    ADVANCED OTHER-GROUP BEHAVIOUR   ______________
        self.otherComboBox.currentTextChanged.connect(
            lambda: self.other_option_changed(1)
        )
        self.otherComboBox2.currentTextChanged.connect(
            lambda: self.other_option_changed(2)
        )
        self.otherComboBox3.currentTextChanged.connect(
            lambda: self.other_option_changed(3)
        )

        # OPTIONS NAMING - TO CHANGE THE CURRENT PAGE FROM SEARCH PAGE
        self.deleteOptionBtn.setObjectName("deleteOptionBtn")
        self.renameOptionBtn.setObjectName("renameOptionBtn")
        self.searchTypeComboBox.setObjectName("searchTypeComboBox")


        # CASE-SENSITIVE NOT YET IMPLEMENTED -> ALWAYS CASE-SENSITIVE LOOKUP
        self.isCaseSensitiveCheckBox.setEnabled(False)
        self.advancedIsCaseSensitiveCheckBox.setEnabled(False)
        self.isCaseSensitiveCheckBox.setChecked(True)
        self.advancedIsCaseSensitiveCheckBox.setChecked(True)


        # fmt: on
        self.retranslate()

    def get_widgets(self):
        return self.widgets

    def retranslate(self):

        # TABS RETRANSLATION
        for indx, tab_title in enumerate(self.tabs):
            self.tabsWidget.setTabText(
                indx, QCoreApplication.translate("MainWindow", tab_title, None)
            )

        self.titleGroupBox.setTitle(
            QCoreApplication.translate(
                "MainWindow", u"TITLE LOOKUP", None)
        )
        self.titleLineEdit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", u"Enter values seperated by comma", None)
        )
        self.isRecursiveCheckBox.setText(
            QCoreApplication.translate("MainWindow", u"RECURSIVE", None)
        )
        self.isCaseSensitiveCheckBox.setText(
            QCoreApplication.translate("MainWindow", u"CASE SENSITIVE (ALWAYS ON)", None)
        )
        self.advancedTitleGroupBox.setTitle(
            QCoreApplication.translate("MainWindow", u"TITLE LOOKUP", None)
        )
        self.advancedTitleLineEdit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", u"Enter values seperated by comma", None)
        )
        self.advancedIsRecuresiveCheckBox.setText(
            QCoreApplication.translate("MainWindow", u"RECURSIVE", None)
        )
        self.advancedIsCaseSensitiveCheckBox.setToolTip(
            QCoreApplication.translate(
                "MainWindow", u"Find files recursively through the selected path", None)
        )
        self.advancedIsCaseSensitiveCheckBox.setText(
            QCoreApplication.translate("MainWindow", u"CASE SENSITIVE", None)
        )
        self.advancedMetadataGroupBox.setTitle(
            QCoreApplication.translate("MainWindow", u"METADATA LOOKUP", None)
        )
        self.metadataLineEdit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", u"Enter values seperated by comma", None)
        )
        self.advancedOtherGroupBox.setTitle(
            QCoreApplication.translate("MainWindow", u"OTHER LOOKUPS", None)
        )
        self.otherLineEdit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", u"Enter values seperated by comma", None)
        )
        self.deleteOptionBtn.setText(
            QCoreApplication.translate("MainWindow", u"DELETE", None)
        )
        self.renameOptionBtn.setText(
            QCoreApplication.translate("MainWindow", u"RENAME", None)
        )
        self.moveOptionBtn.setText(
            QCoreApplication.translate("MainWindow", u"MOVE", None)
        )
        self.duplicateOptionBtn.setText(
            QCoreApplication.translate("MainWindow", u"DUPLICATE", None)
        )
        self.searchGroupBox.setTitle(
            QCoreApplication.translate("MainWindow", u"SEARCH", None)
        )
        self.searchTypeComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"FILES", None)
        )
        self.searchTypeComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"FOLDERS", None)
        )
        self.browsePathBtn.setText(
            QCoreApplication.translate("MainWindow", u"OPEN", None)
        )
        self.pathLineEdit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", u"DIRECTORY PATH...", None)
        )
        self.startSearchBtn.setText(
            QCoreApplication.translate("MainWindow", u"START ", None)
        )
        self.foundMatchLabel.setText(
            QCoreApplication.translate(
                "MainWindow", u"FOUND 0 MATCHES ", None)
        )
        self.pathLineEdit.setToolTip(
            QCoreApplication.translate(
                "MainWindow", u"Enter the path where should the lookup process begin", None)
        )
        self.isRecursiveCheckBox.setToolTip(
            QCoreApplication.translate(
                "MainWindow", u"Find files recursively through the selected path", None)
        )
        self.advancedIsRecuresiveCheckBox.setToolTip(
            QCoreApplication.translate(
                "MainWindow", u"Find files recursively through the selected path", None)
        )
        self.import_tab_cache()
