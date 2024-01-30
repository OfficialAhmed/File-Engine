
from json import load as jsonLoad
from json import dump as jsonDump
from json import JSONDecodeError
from os import path as osPath
from PySide6.QtCore import QCoreApplication, QSize, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout,  QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget, QVBoxLayout, QWidget
)

from Interface.environment import Common, tables
from lib.find import File, Folder


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
    tabsWidget: QTabWidget = None
    tableWidget: QTableWidget = None
    searchMainVL = None
    pathLineEdit: QLineEdit = None
    moveOptionBtn: QPushButton = None
    browsePathBtn: QPushButton = None
    titleGroupBox = None
    titleLineEdit: QLineEdit = None
    titleComboBox: QComboBox = None
    otherLineEdit: QLineEdit = None
    otherComboBox: QComboBox = None
    titleComboBox2: QComboBox = None
    titleComboBox3: QComboBox = None
    basicTabMainVL = None
    verticalLayout = None
    searchGroupBox = None
    startSearchBtn: QPushButton = None
    otherComboBox3: QComboBox = None
    otherComboBox2: QComboBox = None
    titleGroupBoxGL = None
    resultTabMainVL = None
    deleteOptionBtn: QPushButton = None
    renameOptionBtn: QPushButton = None
    verticalLayout2 = None
    verticalLayout3 = None
    verticalLayout4 = None
    foundMatchLabel = None
    metadataLineEdit: QLineEdit = None
    metadataComboBox: QComboBox = None
    searchGroupBoxGL = None
    advancedTabMainVL = None
    metadataComboBox2: QComboBox = None
    metadataComboBox3: QComboBox = None
    duplicateOptionBtn: QPushButton = None
    searchTypeComboBox: QComboBox = None
    isRecursiveCheckBox: QCheckBox = None
    advancedOtherGroupBox = None
    advancedTitleGroupBox = None
    advancedTitleLineEdit: QLineEdit = None
    advancedTitleComboBox: QComboBox = None
    advancedTitleComboBox2: QComboBox = None
    advancedTitleComboBox3: QComboBox = None
    isCaseSensitiveCheckBox: QCheckBox = None
    advancedTitleGroupBoxGL = None
    advancedOtherGroupBoxGL = None
    advancedMetadataGroupBox = None
    advancedMetadataGroupBoxGL = None
    advancedIsRecuresiveCheckBox: QCheckBox = None
    advancedIsCaseSensitiveCheckBox: QCheckBox = None

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
                "Custom (REGEX)"
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
                "Custom (REGEX)"
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

        if cb.currentText().split(" ")[-1] in ("Excluding", "(REGEX)"):
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

                if self.metadataComboBox3.currentText().split(" ")[-1] in ("(REGEX)", "Excluding"):
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

                if self.otherComboBox3.currentText().split(" ")[-1] in ("(REGEX)", "Excluding"):
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

    def set_clickable_options(self, is_enable: bool) -> None:

        self.moveOptionBtn.setEnabled(is_enable)
        self.deleteOptionBtn.setEnabled(is_enable)
        self.renameOptionBtn.setEnabled(is_enable)
        self.duplicateOptionBtn.setEnabled(is_enable)

    def export_tab_cache(self, tab) -> None:
        """
            STORE CURRENT SEARCH SETTINGS 
        """

        data = {
            "BASIC": {
                "titleComboBox":            self.titleComboBox.currentText(),
                "titleComboBox2":           self.titleComboBox2.currentText(),
                "titleComboBox3":           self.titleComboBox3.currentText(),
                "titleLineEdit":            self.titleLineEdit.text(),
                "isRecursiveCheckBox":      self.isRecursiveCheckBox.isChecked(),
                "isCaseSensitiveCheckBox":  self.isCaseSensitiveCheckBox.isChecked()
            },

            "ADVANCED": {
                "metadataComboBox":         self.metadataComboBox.currentText(),
                "metadataComboBox2":        self.metadataComboBox2.currentText(),
                "metadataComboBox3":        self.metadataComboBox3.currentText(),
                "metadataLineEdit":         self.metadataLineEdit.text(),

                "otherComboBox":            self.otherComboBox.currentText(),
                "otherComboBox2":           self.otherComboBox2.currentText(),
                "otherComboBox3":           self.otherComboBox3.currentText(),
                "otherLineEdit":            self.otherLineEdit.text(),

                "advancedTitleComboBox":            self.advancedTitleComboBox.currentText(),
                "advancedTitleComboBox2":           self.advancedTitleComboBox2.currentText(),
                "advancedTitleComboBox3":           self.advancedTitleComboBox3.currentText(),
                "advancedTitleLineEdit":            self.advancedTitleLineEdit.text(),
                "advancedIsRecuresiveCheckBox":     self.advancedIsRecuresiveCheckBox.isChecked(),
                "advancedIsCaseSensitiveCheckBox":  self.advancedIsCaseSensitiveCheckBox.isChecked(),
            }
        }

        cache: dict = {}

        # RETRIEVE EXISTING CACHE IF AVAILABLE
        if osPath.exists(self.cache_file):
            cache = jsonLoad(open(self.cache_file))
            cache[tab] = data.get(tab)
        else:
            cache = data

        cache["SEARCH"] = {
            "searchTypeComboBox":       self.searchTypeComboBox.currentText(),
            "pathLineEdit":             self.pathLineEdit.text()
        }

        with open(self.cache_file, "w+") as file:
            jsonDump(cache, file)

    def import_tab_cache(self) -> None:

        # fmt: off
        if osPath.exists(self.cache_file):
            cache: dict = jsonLoad(open(self.cache_file))

            data: dict = cache.get("BASIC")

            self.titleComboBox.setCurrentText(data.get("titleComboBox"))
            self.titleComboBox2.setCurrentText(data.get("titleComboBox2"))
            self.titleComboBox3.setCurrentText(data.get("titleComboBox3"))
            self.titleLineEdit.setText(data.get("titleLineEdit"))
            self.isRecursiveCheckBox.setChecked(data.get("isRecursiveCheckBox"))
            self.isCaseSensitiveCheckBox.setChecked(data.get("isCaseSensitiveCheckBox"))

            data: dict = cache.get("ADVANCED")

            self.advancedTitleComboBox.setCurrentText(data.get("advancedTitleComboBox"))
            self.advancedTitleComboBox2.setCurrentText(data.get("advancedTitleComboBox2"))
            self.advancedTitleComboBox3.setCurrentText(data.get("advancedTitleComboBox3"))
            self.advancedTitleLineEdit.setText(data.get("advancedTitleLineEdit"))
            self.advancedIsRecuresiveCheckBox.setChecked(data.get("advancedIsRecuresiveCheckBox"))
            self.advancedIsCaseSensitiveCheckBox.setChecked(data.get("advancedIsCaseSensitiveCheckBox"))

            self.metadataComboBox.setCurrentText(data.get("metadataComboBox"))
            self.metadataComboBox2.setCurrentText(data.get("metadataComboBox2"))
            self.metadataComboBox3.setCurrentText(data.get("metadataComboBox3"))
            self.metadataLineEdit.setText(data.get("metadataLineEdit"))

            self.otherComboBox.setCurrentText(data.get("otherComboBox"))
            self.otherComboBox2.setCurrentText(data.get("otherComboBox2"))
            self.otherComboBox3.setCurrentText(data.get("otherComboBox3"))
            self.otherLineEdit.setText(data.get("otherLineEdit"))

            data: dict = cache.get("SEARCH")

            self.searchTypeComboBox.setCurrentText(data.get("searchTypeComboBox"))
            self.pathLineEdit.setText(data.get("pathLineEdit"))

        # fmt: on

    def start_search_clicked(self):

        path = self.pathLineEdit.text()

        if not path:
            self.dialog.show(
                msg="PATH IS EMPTY!",
                mode="w",
                is_dialog=False
            )
            return

        if not self.dialog.show(
            "WOULD YOU LIKE TO START THE SEARCHING PROCESS?",
            "ARE YOU SURE?"
        ):
            return

        # IF CACHE DOESNT EXIST CREATE ONE
        if osPath.exists(self.cache_file):
            self.export_tab_cache("BASIC")
            self.export_tab_cache("ADVANCED")

        try:
            match self.tabs[self.tabsWidget.currentIndex()]:

                case "BASIC":

                    self.export_tab_cache("BASIC")
                    search_type: str = self.searchTypeComboBox.currentText()
                    custom_input: list = self.titleLineEdit.text().replace(" ", "").split(",")
                    
                    tables["RENAME"].data_type = search_type
                    tables["DELETE"].data_type = search_type
                    
                    finder = File()
                    if search_type == "FOLDERS":
                        finder = Folder()

                    finder.update_finder_param(
                        path,
                        self.isRecursive.isChecked(),
                        self.isCaseSensitiveCheckBox.isChecked()
                    )

                    search = self.titleComboBox.currentText()

                    if self.titleComboBox2.currentText() != "CONTAIN":

                        if search == "NAME":
                            self.data = finder.get_by_title(custom_input)
                        else:
                            self.data = finder.get_by_extension(custom_input)

                    else:

                        match self.titleComboBox3.currentText():
                            case "Symbols only":        self.data = finder.get_only_symbols(search)
                            case "Alphabets only":      self.data = finder.get_only_alphabets(search)
                            case "Numbers & Symbols":   self.data = finder.get_num_symbol(search)
                            case "Numbers Excluding":   self.data = finder.get_num_exclude(search, custom_input)
                            case "Symbols Excluding":   self.data = finder.get_symbol_exclude(search, custom_input)
                            case "Alphabets Excluding": self.data = finder.get_alpha_exclude(search, custom_input)
                            case "Alphabets & Numbers": self.data = finder.get_alpha_num(search)
                            case "Alphabets & Symbols": self.data = finder.get_alpha_symbol(search)
                            case "Custom (REGEX)":      self.data = finder.get_custom(search, self.titleLineEdit.text().strip())

                    tables["SEARCH"].fill(self.data)

                    # SHOW THE RESULT PAGE AFTER RENDERING TABLE
                    self.foundMatchLabel.setText(
                        f"{len(self.data)} MATCHES FOUND"
                    )
                    self.tabsWidget.setCurrentIndex(self.tabs.index("RESULT"))

                    if not self.data:
                        self.set_clickable_options(False)
                        self.dialog.show(
                            "NO DATA HAS BEEN FOUND!",  # MESSAGE
                            "ITEMS CANNOT BE FOUND!",   # WINDOW TITLE
                            is_dialog=False             # FALSE = INFORMATIONAL
                        )
                        return

                    self.set_clickable_options(True)

                case "ADVANCED":
                    self.export_tab_cache("ADVANCED")

                case "RESULT":
                    self.dialog.show(
                        "CANNOT START THE PROCESS. CHANGE THE TAB TO BASIC OR ADVANCED",
                        "INVALID TAB SELECTED",
                        is_dialog=False
                    )

        except JSONDecodeError:
            self.dialog.show(
                f"THE CACHE FILE WAS CURRUPTED. PLEASE CLOSE THE APP AND REMOVE IT FROM ({self.cache_file})",
                "c",
                is_dialog=False
            )

        except Exception as e:
            self.dialog.show(
                f"UNKNOWN ERROR OCCURED | {str(e)}",
                "c",
                is_dialog=False
            )


class Ui(Response):
    """
        UI RENDERING AND TRANSLATING TEXTS
    """

    def __init__(self) -> None:
        super().__init__()

    def render_page(self):

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
        self.import_tab_cache()
