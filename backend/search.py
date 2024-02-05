"""

    # HANDLES THE RESPONSE OF THE SEARCH FRONT-END 

"""

from lib.find import File, Folder
from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QLineEdit, QPushButton, QTabWidget, QTableWidget
)

from os import path as osPath
from json import load as jsonLoad
from json import dump as jsonDump
from json import JSONDecodeError

from environment import Common, tables

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

    tabs = ("BASIC", "ADVANCED (SOON!)", "RESULT")

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

