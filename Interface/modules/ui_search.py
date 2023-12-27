
from PySide6.QtCore import QCoreApplication, QSize, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QAbstractItemView, QAbstractScrollArea, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout,  QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget, QVBoxLayout, QWidget
)

from Interface.environment import Common


class Page(Common):
    """
        QWIDGETS STORED IN THIS CLASS TO BE SHARED TO ALL CHILDREN
    """

    topGL = None
    BASIC = None
    RESULT = None
    widgets = None
    ADVANCED = None
    bottomHL = None
    tabsWidget = None
    tableWidget = None
    searchMainVL = None
    pathLineEdit = None
    moveOptionBtn = None
    browsePathBtn = None
    titleGroupBox = None
    titleLineEdit = None
    titleComboBox = None
    otherLineEdit = None
    otherComboBox = None
    titleComboBox2 = None
    titleComboBox3 = None
    basicTabMainVL = None
    verticalLayout = None
    searchGroupBox = None
    startSearchBtn = None
    otherComboBox3 = None
    otherComboBox2 = None
    titleGroupBoxGL = None
    resultTabMainVL = None
    deleteOptionBtn = None
    renameOptionBtn = None
    verticalLayout2 = None
    verticalLayout3 = None
    verticalLayout4 = None
    foundMatchLabel = None
    metadataLineEdit = None
    metadataComboBox = None
    searchGroupBoxGL = None
    advancedTabMainVL = None
    metadataComboBox2 = None
    metadataComboBox3 = None
    duplicateOptionBtn = None
    searchTypeComboBox = None
    isRecursiveCheckBox = None
    advancedOtherGroupBox = None
    advancedTitleGroupBox = None
    advancedTitleLineEdit = None
    advancedTitleComboBox = None
    advancedTitleComboBox2 = None
    advancedTitleComboBox3 = None
    isCaseSensitiveCheckBox = None
    advancedTitleGroupBoxGL = None
    advancedOtherGroupBoxGL = None
    advancedMetadataGroupBox = None
    advancedMetadataGroupBoxGL = None
    advancedIsRecuresiveCheckBox = None
    advancedIsCaseSensitiveCheckBox = None

    tabs = ("BASIC", "ADVANCED", "RESULT")

    search_options = {
        "NAME": ("FILES", "FOLDERS"),
        "EXTENSION": ("FILES",)
    }

    title_options = {
        "NAME": {
            "CONTAIN": (
                "Alphabets only",
                "Alphabets & Symbols",
                "Alphabets & Numbers",
                "Alphabets Excluding",
                "Numbers & Symbols",
                "Numbers Excluding",
                "Symbols only",
                "Symbols Excluding",
                "Custom"
            ),
            "EQUAL TO": ()
        },
        "EXTENSION": {
            "CONTAIN": (
                "Alphabets only",
                "Alphabets & Symbols",
                "Alphabets & Numbers",
                "Alphabets Excluding",
                "Numbers & Symbols",
                "Numbers Excluding",
                "Symbols only",
                "Symbols Excluding",
                "Custom"
            ),
            "EQUAL TO": ()
        }
    }

    metadata_options = {
        "VIDEO": {
            "DIMENSIONS": (
                "1920x1080",
                "720x420",
                "Custom"
            ),
            "DURATION": (
                "Custom",
            ),
            "BIT RATE": (
                "Custom",
            ),
            "FRAME RATE": (
                "Custom",
            ),
            "FPS": (
                "Custom",
            )
        },
        "IMAGE": {
            "DIMENSIONS": (
                "Custom",
            ),
        },
        "AUDIO": {
            "ALBUM": (
                "Custom",
            ),
            "AUTHOR": (
                "Custom",
            ),
            "DURATION": (
                "Custom",
            )
        },
        "DOCS": {
            "AUTHOR": (
                "Custom",
            )
        }
    }

    other_options = {
        "SIZE": {
            "BYTES": (
                "Custom",
            ),
            "KILOBYTES": (
                "Custom",
            ),
            "MEGABYTES": (
                "Custom",
            ),
            "GIGABYTES": (
                "Custom",
            )
        },
        "DATE CREATED": {
            "EQUAL TO": (
                "Custom",
            ),
            "LESS THAN": (
                "Custom",
            ),
            "GREATER THAN": (
                "Custom",
            )
        }
    }

    def __init__(self) -> None:
        super().__init__()


class Response(Page):
    """
        SIGNALS HANDLING AND UI BEHAVIOUR
    """

    def __init__(self) -> None:
        super().__init__()

    def title_cb_changed(self):
        """
            ### CHANGE SEARCH TYPE OPTIONS 
        """

        self.searchTypeComboBox.clear()
        for option in self.search_options.get(self.titleComboBox.currentText()):
            self.searchTypeComboBox.addItem(option)

    def title_cb2_changed(self, type=""):
        """
            ### BASIC TITLE GROUP OPTIONS CHANGED
            GENERATE AVAILABLE OPTIONS BASED ON TITLE CHECKBOX2
        """
        le = self.titleLineEdit     # LINE EDIT
        cb = self.titleComboBox2    # CHECKBOX
        cb3 = self.titleComboBox3   # CHECKBOX TO HIDE

        if type == "advanced":
            le = self.advancedTitleLineEdit
            cb = self.advancedTitleComboBox2
            cb3 = self.advancedTitleComboBox3

        match cb.currentText():

            # SHOW FIXED OPTIONS & HIDE CUSTOM
            case "CONTAIN":
                cb3.setHidden(False)
                le.setHidden(True)

            # SHOW CUSTOM OPTION ONLY
            case "EQUAL TO":
                cb3.setHidden(True)
                le.setHidden(False)

    def title_cb3_changed(self, type=""):
        """
            RERENDER OPTIONS BASED ON TITLE CHECKBOX3
        """

        cb = self.titleComboBox3    # CHECKBOX
        le = self.titleLineEdit     # LINE EDIT

        if type == "advanced":
            cb = self.advancedTitleComboBox3
            le = self.advancedTitleLineEdit

        if cb.currentText().split(" ")[-1] in ("Excluding", "Custom"):
            le.setHidden(False)
        else:
            le.setHidden(True)

    def md_option_changed(self, changed_cb: int):
        """
            ### METADATA GROUP OPTIONS CHANGED
            GENERATE AVAILABLE OPTIONS BASED ON CURRENT OPTION
        """

        # DISABLE THE FUNCTION TEMPORARLY
        self.metadataComboBox.currentTextChanged.disconnect()
        self.metadataComboBox2.currentTextChanged.disconnect()
        self.metadataComboBox3.currentTextChanged.disconnect()

        match changed_cb:

            case 1:

                options = self.metadata_options[
                    self.metadataComboBox.currentText()
                ]

                # 2nd COMBOBOX OPTIONS
                self.metadataComboBox2.clear()
                for option in options.keys():
                    self.metadataComboBox2.addItem(option)

                options = options[tuple(options.keys())[0]]

            case 2:

                options = self.metadata_options[
                    self.metadataComboBox.currentText()
                ][self.metadataComboBox2.currentText()]

            case 3:

                if self.metadataComboBox3.currentText().split(" ")[-1] in ("Custom", "Excluding"):
                    self.metadataLineEdit.setHidden(False)
                else:
                    self.metadataLineEdit.setHidden(True)

        if changed_cb != 3:

            # 3rd COMBOBOX OPTIONS
            self.metadataComboBox3.clear()
            for option in options:
                self.metadataComboBox3.addItem(option)

        # ENABLE THE FUNCTION AGAIN
        self.metadataComboBox.currentTextChanged.connect(
            lambda: self.md_option_changed(1))
        self.metadataComboBox2.currentTextChanged.connect(
            lambda: self.md_option_changed(2))
        self.metadataComboBox3.currentTextChanged.connect(
            lambda: self.md_option_changed(3))

    def other_option_changed(self, changed_cb: int):
        """
            ### METADATA GROUP OPTIONS CHANGED
            GENERATE AVAILABLE OPTIONS BASED ON CURRENT OPTION
        """

        # DISABLE THE FUNCTION TEMPORARLY
        self.otherComboBox.currentTextChanged.disconnect()
        self.otherComboBox2.currentTextChanged.disconnect()
        self.otherComboBox3.currentTextChanged.disconnect()

        match changed_cb:

            case 1:

                options = self.other_options[
                    self.otherComboBox.currentText()
                ]

                # 2nd COMBOBOX OPTIONS
                self.otherComboBox2.clear()
                for option in options.keys():
                    self.otherComboBox2.addItem(option)

                options = options[tuple(options.keys())[0]]

            case 2:

                options = self.other_options[
                    self.otherComboBox.currentText()
                ][self.otherComboBox2.currentText()]

            case 3:

                if self.otherComboBox3.currentText().split(" ")[-1] in ("Custom", "Excluding"):
                    self.otherLineEdit.setHidden(False)
                else:
                    self.otherLineEdit.setHidden(True)

        if changed_cb != 3:

            # 3rd COMBOBOX OPTIONS
            self.otherComboBox3.clear()
            for option in options:
                self.otherComboBox3.addItem(option)

        # ENABLE THE FUNCTION AGAIN
        self.otherComboBox.currentTextChanged.connect(
            lambda: self.other_option_changed(1))
        self.otherComboBox2.currentTextChanged.connect(
            lambda: self.other_option_changed(2))
        self.otherComboBox3.currentTextChanged.connect(
            lambda: self.other_option_changed(3))

    def start_search_clicked(self):

        path = self.pathLineEdit.text()

        if not path:
            print("invalid: path input empty")
            return

        self.controller.update_finder_param(
            path,
            self.isRecursiveCheckBox.isChecked()
        )

        match self.tabs[self.tabsWidget.currentIndex()]:

            case "BASIC":

                custom_input: str = self.titleLineEdit.text()
                search_type: str = self.titleComboBox.currentText()

                if self.titleComboBox2.currentText() == "CONTAIN":

                    txt: str = self.titleComboBox3.currentText()
                    last_word = txt.split(" ")[-1]

                    if last_word == "Custom":
                        pass
                    elif last_word == "Excluding":
                        pass
                    else:

                        match txt:
                            case "Alphabets only":
                                self.data = self.controller.get_files_by_title_only_alphabets()
                            case "Alphabets & Symbols":
                                pass
                            case "Alphabets & Numbers":
                                pass
                            case "Alphabets Excluding":
                                pass
                            case "Numbers & Symbols":
                                pass
                            case "Numbers Excluding":
                                pass
                            case "Symbols only":
                                pass
                            case "Symbols Excluding":
                                pass
                            case "Custom":
                                pass

                else:
                    pass

                self.generate_table(self.tableWidget)
                self.foundMatchLabel.setText(f"{len(self.data)} MATCHES FOUND")
                self.tabsWidget.setCurrentIndex(self.tabs.index("RESULT"))

            case "ADVANCED":
                pass

            case "RESULT":
                # TODO: SHOW A DIALOG HERE
                print("CANNOT START PROCESS. CHANGE THE TAB TO BASIC OR ADVANCED")


class Ui(Response):
    """
        UI RENDERING AND TRANSLATING TEXTS
    """

    def __init__(self) -> None:
        super().__init__()

    def render_page(self):

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
        self.tableWidget = QTableWidget(self.RESULT)
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

        self.set_controller_widgets(
            self.searchTypeComboBox,
            self.pathLineEdit,
            self.titleComboBox,
            self.pathLineEdit,
            self.isRecursiveCheckBox,
            self.startSearchBtn
        )

        """
        ===================================================================
                                TABLE CONTENT
        ===================================================================
        """

        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.tableWidget.sizePolicy().hasHeightForWidth()
        )
        self.tableWidget.setSizePolicy(sizePolicy3)

        self.init_table(self.tableWidget)

        """
        ===================================================================
                           PALLETE AND BRUSHES
        ===================================================================
        """

        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.bottomHL.setContentsMargins(-1, 0, -1, -1)

        self.resultBottomLHSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.advancedTitleLineEdit.setStyleSheet(
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
            self.advancedTitleLineEdit, 0, 3, 1, 1
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
            self.tableWidget
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
        self.titleGroupBox.toggled.connect(
            self.isCaseSensitiveCheckBox.setEnabled)

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

        self.retranslate()

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
            QCoreApplication.translate("MainWindow", u"CASE SENSITIVE", None)
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
