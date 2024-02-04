
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .resources_rc import *
from ..environment import Common, ProgressBar
from .delete import Ui as Ui_delete
from .rename import Ui as Ui_rename
from .search import Ui as Ui_search
from backend.home import Feature


class Ui(object):

    def __init__(self) -> None:
        super().__init__()

        self.ui_function = Feature()
        self.common_functions = Common()

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(1280, 720)
        self.styleSheet = QWidget(MainWindow)

        """
        ////////////////////////////////////////////////
                    QSS UI STYLESHEET
        ////////////////////////////////////////////////
        """
        qss_file = QFile("frontend\\Design\\styles.qss")
        qss_file.open(QFile.ReadOnly | QFile.Text)

        # Apply the CSS stylesheet to the widget
        stylesheet = QTextStream(qss_file).readAll()
        self.styleSheet.setStyleSheet(stylesheet)

        """
        ////////////////////////////////////////////////
                    SET FRAMES - SENSITIVE!
        ////////////////////////////////////////////////
        """
        self.bgApp = QFrame(self.styleSheet)
        self.leftMenuBg = QFrame(self.bgApp)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogo = QFrame(self.topLogoInfo)
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.extraLeftBox = QFrame(self.bgApp)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraContent = QFrame(self.extraLeftBox)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraCenter = QFrame(self.extraContent)
        self.extraBottom = QFrame(self.extraContent)
        self.contentBox = QFrame(self.bgApp)
        self.contentTopBg = QFrame(self.contentBox)
        self.leftBox = QFrame(self.contentTopBg)
        self.rightButtons = QFrame(self.contentTopBg)
        self.contentBottom = QFrame(self.contentBox)
        self.content = QFrame(self.contentBottom)
        self.pagesContainer = QFrame(self.content)
        self.extraRightBox = QFrame(self.content)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.contentSettings = QFrame(self.extraRightBox)
        self.topMenus = QFrame(self.contentSettings)
        self.bottomBar = QFrame(self.contentBottom)
        self.frame_size_grip = QFrame(self.bottomBar)

        """
        ////////////////////////////////////////////////
                    WIDGETS - SENSITIVE!
        ////////////////////////////////////////////////
        """
        self.new_page = QWidget()
        self.home_page_btn = QPushButton(self.topMenu)
        self.move_page_btn = QPushButton(self.topMenu)
        self.btn_print = QPushButton(self.topMenus)
        self.btn_logout = QPushButton(self.topMenus)
        self.search_page_btn = QPushButton(self.topMenu)
        self.delete_page_btn = QPushButton(self.topMenu)
        self.rename_page_btn = QPushButton(self.topMenu)
        self.removeTrashOption = QPushButton(self.topMenus)
        self.moreBtn = QPushButton(self.rightButtons)
        self.btn_more = QPushButton(self.extraTopMenu)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.closeAppBtn = QPushButton(self.rightButtons)
        self.displayModeOption = QPushButton(self.extraTopMenu)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.maximizeAppBtn = QPushButton(self.rightButtons)
        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)

        self.extraLabel = QLabel(self.extraTopBg)
        self.titleRightInfo = QLabel(self.leftBox)
        self.creditsLabel = QLabel(self.bottomBar)
        self.textEdit = QTextEdit(self.extraCenter)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.version = QLabel(self.bottomBar)

        self.extraTopLayout = QGridLayout()
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)

        self.label = QLabel(self.new_page)
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)

        self.progressBar = QProgressBar(self.bottomBar)
        self.stackedWidget = QStackedWidget(self.pagesContainer)

        """
        ////////////////////////////////////////////////
                        WIDGET SPECS
        ////////////////////////////////////////////////
        """

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        font = QFont()
        font1 = QFont()
        font2 = QFont()
        font3 = QFont()
        font5 = QFont()

        font.setBold(False)
        font5.setBold(False)
        font3.setBold(False)

        font.setItalic(False)
        font5.setItalic(False)
        font3.setItalic(False)

        font.setFamily(u"Segoe UI")
        font1.setFamilies([u"Segoe UI Semibold"])
        font2.setFamilies([u"Segoe UI"])
        font3.setFamilies([u"Segoe UI"])
        font5.setFamilies([u"Segoe UI"])

        font.setPointSize(10)
        font1.setPointSize(12)
        font2.setPointSize(8)
        font3.setPointSize(10)

        font3.setStyleStrategy(QFont.PreferDefault)

        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))

        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setHorizontalSpacing(10)

        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setStyleSheet(u"background: transparent;")

        self.label.setAlignment(
            Qt.AlignCenter
        )
        self.titleLeftApp.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop
        )
        self.titleLeftDescription.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop
        )
        self.creditsLabel.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.titleRightInfo.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.version.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        MainWindow.setCentralWidget(self.styleSheet)

        self.btn_more.setFont(font)
        self.home_page_btn.setFont(font)
        self.move_page_btn.setFont(font)
        self.btn_print.setFont(font)
        self.styleSheet.setFont(font)
        self.btn_logout.setFont(font)
        self.delete_page_btn.setFont(font)
        self.rename_page_btn.setFont(font)
        self.search_page_btn.setFont(font)
        self.toggleButton.setFont(font)
        self.titleLeftApp.setFont(font1)
        self.toggleLeftBox.setFont(font)
        self.creditsLabel.setFont(font5)
        self.titleRightInfo.setFont(font)
        self.btn_adjustments.setFont(font)
        self.maximizeAppBtn.setFont(font3)
        self.displayModeOption.setFont(font)
        self.removeTrashOption.setFont(font)
        self.titleLeftDescription.setFont(font2)

        """
        ////////////////////////////////////////////////
                HOME PAGE CONTENT
        ////////////////////////////////////////////////
        """

        self.home_widgets = QWidget()

        """
        ////////////////////////////////////////////////
                PAGES CONTENT
        ////////////////////////////////////////////////
        """
        # SET SHARED WIDGETS AFTER RENDERING
        _UiDelete = Ui_delete()
        self.delete_widgets = _UiDelete.get_widgets()

        _UiRename = Ui_rename()
        self.rename_widgets = _UiRename.get_widgets()

        _UiSearch = Ui_search()
        self.search_widgets = _UiSearch.get_widgets()

        """
        ////////////////////////////////////////////////
                    SET MARGINS
        ////////////////////////////////////////////////
        """

        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)

        """
        ////////////////////////////////////////////////
                    SET SPACING
        ////////////////////////////////////////////////
        """

        self.appLayout.setSpacing(0)
        self.appMargins.setSpacing(0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_6.setSpacing(0)
        self.horizontalLayout.setSpacing(0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_5.setSpacing(0)
        self.extraColumLayout.setSpacing(0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_12.setSpacing(0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_3.setSpacing(0)
        self.verticalMenuLayout.setSpacing(0)
        self.horizontalLayout_2.setSpacing(5)

        """
        ////////////////////////////////////////////////
                    SET LAYOUT DIRECTION
        ////////////////////////////////////////////////
        """
        l_2_r = Qt.LeftToRight

        self.btn_more.setLayoutDirection(l_2_r)
        self.btn_print.setLayoutDirection(l_2_r)
        self.move_page_btn.setLayoutDirection(l_2_r)
        self.home_page_btn.setLayoutDirection(l_2_r)
        self.btn_logout.setLayoutDirection(l_2_r)
        self.removeTrashOption.setLayoutDirection(l_2_r)
        self.search_page_btn.setLayoutDirection(l_2_r)
        self.rename_page_btn.setLayoutDirection(l_2_r)
        self.delete_page_btn.setLayoutDirection(l_2_r)
        self.displayModeOption.setLayoutDirection(l_2_r)
        self.toggleButton.setLayoutDirection(l_2_r)
        self.toggleLeftBox.setLayoutDirection(l_2_r)
        self.btn_adjustments.setLayoutDirection(l_2_r)

        """
        ////////////////////////////////////////////////
                    SET SIZE POLICY 
        ////////////////////////////////////////////////
        """
        _0_45 = QSize(0, 45)
        _28_28 = QSize(28, 28)

        self.btn_more.setMinimumSize(_0_45)
        self.btn_print.setMinimumSize(_0_45)
        self.move_page_btn.setMinimumSize(_0_45)
        self.home_page_btn.setMinimumSize(_0_45)
        self.btn_logout.setMinimumSize(_0_45)
        self.search_page_btn.setMinimumSize(_0_45)
        self.rename_page_btn.setMinimumSize(_0_45)
        self.delete_page_btn.setMinimumSize(_0_45)
        self.toggleButton.setMinimumSize(_0_45)
        self.toggleLeftBox.setMinimumSize(_0_45)
        self.btn_adjustments.setMinimumSize(_0_45)
        self.displayModeOption.setMinimumSize(_0_45)
        self.removeTrashOption.setMinimumSize(_0_45)

        self.moreBtn.setMinimumSize(_28_28)
        self.moreBtn.setMaximumSize(_28_28)
        self.closeAppBtn.setMinimumSize(_28_28)
        self.closeAppBtn.setMaximumSize(_28_28)
        self.maximizeAppBtn.setMinimumSize(_28_28)
        self.maximizeAppBtn.setMaximumSize(_28_28)
        self.minimizeAppBtn.setMaximumSize(_28_28)
        self.minimizeAppBtn.setMinimumSize(_28_28)
        self.extraCloseColumnBtn.setMinimumSize(_28_28)
        self.extraCloseColumnBtn.setMaximumSize(_28_28)

        MainWindow.setMinimumSize(QSize(940, 560))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.extraLabel.setMinimumSize(QSize(150, 0))
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.frame_size_grip.setMinimumSize(QSize(20, 0))

        self.topLogo.setMaximumSize(QSize(42, 42))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.progressBar.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))

        self.toggleButton.setSizePolicy(sizePolicy)
        self.home_page_btn.setSizePolicy(sizePolicy)
        self.delete_page_btn.setSizePolicy(sizePolicy)
        self.rename_page_btn.setSizePolicy(sizePolicy)
        self.move_page_btn.setSizePolicy(sizePolicy)
        self.search_page_btn.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.displayModeOption.setSizePolicy(sizePolicy)
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_more.setSizePolicy(sizePolicy)
        self.leftBox.setSizePolicy(sizePolicy1)
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.removeTrashOption.setSizePolicy(sizePolicy)
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_logout.setSizePolicy(sizePolicy)
        self.progressBar.setSizePolicy(sizePolicy3)

        sizePolicy.setHorizontalStretch(0)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy3.setHorizontalStretch(0)

        sizePolicy.setVerticalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy3.setVerticalStretch(0)

        # fmt: off
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.home_page_btn.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.delete_page_btn.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.rename_page_btn.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.move_page_btn.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.search_page_btn.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.displayModeOption.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.removeTrashOption.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        # fmt: on

        """
        ////////////////////////////////////////////////
                    SET MOUSE CURSOR 
        ////////////////////////////////////////////////
        """
        pointing_hand = QCursor(Qt.PointingHandCursor)
        self.moreBtn.setCursor(pointing_hand)
        self.btn_more.setCursor(pointing_hand)
        self.btn_print.setCursor(pointing_hand)
        self.move_page_btn.setCursor(pointing_hand)
        self.home_page_btn.setCursor(pointing_hand)
        self.btn_logout.setCursor(pointing_hand)
        self.search_page_btn.setCursor(pointing_hand)
        self.rename_page_btn.setCursor(pointing_hand)
        self.delete_page_btn.setCursor(pointing_hand)
        self.closeAppBtn.setCursor(pointing_hand)
        self.toggleButton.setCursor(pointing_hand)
        self.toggleLeftBox.setCursor(pointing_hand)
        self.maximizeAppBtn.setCursor(pointing_hand)
        self.minimizeAppBtn.setCursor(pointing_hand)
        self.btn_adjustments.setCursor(pointing_hand)
        self.displayModeOption.setCursor(pointing_hand)
        self.removeTrashOption.setCursor(pointing_hand)
        self.extraCloseColumnBtn.setCursor(pointing_hand)

        """
        ////////////////////////////////////////////////
                        FRAME SETTING
        ////////////////////////////////////////////////
        """

        no_frame = QFrame.NoFrame

        self.bgApp.setFrameShape(no_frame)
        self.content.setFrameShape(no_frame)
        self.leftBox.setFrameShape(no_frame)
        self.topMenu.setFrameShape(no_frame)
        self.topLogo.setFrameShape(no_frame)
        self.textEdit.setFrameShape(no_frame)
        self.topMenus.setFrameShape(no_frame)
        self.bottomBar.setFrameShape(no_frame)
        self.extraIcon.setFrameShape(no_frame)
        self.toggleBox.setFrameShape(no_frame)
        self.extraTopBg.setFrameShape(no_frame)
        self.leftMenuBg.setFrameShape(no_frame)
        self.bottomMenu.setFrameShape(no_frame)
        self.contentBox.setFrameShape(no_frame)
        self.topLogoInfo.setFrameShape(no_frame)
        self.extraCenter.setFrameShape(no_frame)
        self.extraBottom.setFrameShape(no_frame)
        self.extraTopMenu.setFrameShape(no_frame)
        self.extraContent.setFrameShape(no_frame)
        self.extraLeftBox.setFrameShape(no_frame)
        self.rightButtons.setFrameShape(no_frame)
        self.contentTopBg.setFrameShape(no_frame)
        self.contentBottom.setFrameShape(no_frame)
        self.leftMenuFrame.setFrameShape(no_frame)
        self.extraRightBox.setFrameShape(no_frame)
        self.pagesContainer.setFrameShape(no_frame)
        self.frame_size_grip.setFrameShape(no_frame)
        self.contentSettings.setFrameShape(no_frame)
        self.themeSettingsTopDetail.setFrameShape(no_frame)

        """
        ////////////////////////////////////////////////
                    SET OBJECTS' NAME
        ////////////////////////////////////////////////
        """
        self.bgApp.setObjectName(u"bgApp")
        self.label.setObjectName(u"label")
        self.topLogo.setObjectName(u"topLogo")
        self.topMenu.setObjectName(u"topMenu")
        self.leftBox.setObjectName(u"leftBox")
        self.version.setObjectName(u"version")
        self.content.setObjectName(u"content")
        self.moreBtn.setObjectName(u"moreBtn")
        self.home_widgets.setObjectName(u"home")
        self.textEdit.setObjectName(u"textEdit")
        self.btn_more.setObjectName(u"btn_more")
        self.topMenus.setObjectName(u"topMenus")
        self.new_page.setObjectName(u"new_page")
        self.home_widgets.setObjectName(u"delete")
        self.appLayout.setObjectName(u"appLayout")
        self.extraIcon.setObjectName(u"extraIcon")
        self.move_page_btn.setObjectName(u"move_page")
        self.home_page_btn.setObjectName(u"home_page")
        self.toggleBox.setObjectName(u"toggleBox")
        self.btn_print.setObjectName(u"btn_print")
        self.bottomBar.setObjectName(u"bottomBar")
        self.styleSheet.setObjectName(u"styleSheet")
        self.contentBox.setObjectName(u"contentBox")
        self.appMargins.setObjectName(u"appMargins")
        self.extraLabel.setObjectName(u"extraLabel")
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.btn_logout.setObjectName(u"btn_logout")
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.extraBottom.setObjectName(u"extraBottom")
        self.removeTrashOption.setObjectName(u"btn_message")
        self.progressBar.setObjectName(u"progressBar")
        self.search_page_btn.setObjectName(u"search_page")
        self.rename_page_btn.setObjectName(u"rename_page")
        self.delete_page_btn.setObjectName(u"delete_page")
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.extraCenter.setObjectName(u"extraCenter")
        self.displayModeOption.setObjectName(u"display_mode")
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraContent.setObjectName(u"extraContent")
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.toggleButton.setObjectName(u"toggleButton")
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.rightButtons.setObjectName(u"rightButtons")
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.contentBottom.setObjectName(u"contentBottom")
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.contentSettings.setObjectName(u"contentSettings")
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.maximizeAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")

        """
        ////////////////////////////////////////////////
                LAYOUT WIDGETS - SENSITIVE LAYOUT
        ////////////////////////////////////////////////
        """
        self.verticalLayout_5.addLayout(self.extraTopLayout)

        self.verticalLayout_3.addWidget(self.topLogoInfo)
        self.verticalLayout_3.addWidget(self.leftMenuFrame)

        self.verticalLayout_4.addWidget(self.toggleButton)

        self.verticalLayout_8.addWidget(self.home_page_btn)
        self.verticalLayout_8.addWidget(self.search_page_btn)
        self.verticalLayout_8.addWidget(self.delete_page_btn)
        self.verticalLayout_8.addWidget(self.rename_page_btn)
        self.verticalLayout_8.addWidget(self.move_page_btn)

        self.verticalLayout_9.addWidget(self.toggleLeftBox)
        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)
        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)
        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)
        self.extraColumLayout.addWidget(self.extraTopBg)
        self.verticalLayout_11.addWidget(self.displayModeOption)
        self.verticalLayout_11.addWidget(self.btn_adjustments)
        self.verticalLayout_11.addWidget(self.btn_more)
        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)
        self.verticalLayout_10.addWidget(self.textEdit)
        self.verticalLayout_12.addWidget(self.extraBottom)
        self.horizontalLayout_3.addWidget(self.titleRightInfo)
        self.horizontalLayout_2.addWidget(self.moreBtn)
        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)
        self.horizontalLayout_2.addWidget(self.maximizeAppBtn)
        self.horizontalLayout_2.addWidget(self.closeAppBtn)
        self.stackedWidget.addWidget(self.home_widgets)
        self.stackedWidget.addWidget(self.search_widgets)
        self.stackedWidget.addWidget(self.delete_widgets)
        self.stackedWidget.addWidget(self.rename_widgets)
        self.verticalLayout_20.addWidget(self.label)
        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)
        self.verticalLayout_14.addWidget(self.removeTrashOption)
        self.verticalLayout_14.addWidget(self.btn_print)
        self.verticalLayout_14.addWidget(self.btn_logout)

        self.appLayout.addWidget(self.leftMenuBg)
        self.verticalLayout_12.addWidget(self.extraCenter)
        self.extraColumLayout.addWidget(self.extraContent)
        self.appLayout.addWidget(self.extraLeftBox)
        self.horizontalLayout.addWidget(self.leftBox)
        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.contentTopBg)
        self.verticalLayout_15.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.pagesContainer)
        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.contentSettings)
        self.horizontalLayout_4.addWidget(self.extraRightBox)
        self.verticalLayout_6.addWidget(self.content)
        self.verticalLayout_2.addWidget(self.contentBottom)
        self.appLayout.addWidget(self.contentBox)
        self.appMargins.addWidget(self.bgApp)
        self.horizontalLayout_5.addWidget(self.progressBar)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum
        )
        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)
        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)
        self.horizontalLayout_5.addWidget(self.version)
        self.horizontalLayout_5.addWidget(self.frame_size_grip)
        self.verticalLayout_6.addWidget(self.bottomBar)
        self.verticalMenuLayout.addWidget(self.toggleBox)
        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)
        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)

        # SET SHARABLE WIDGETS
        pb = ProgressBar()
        pb.set_widget(self.progressBar)

        # SET TRASLATIONS
        self.retranslateUi(MainWindow)

        # fmt: off
        # WINDOW
        self.common_functions.set_icon(self.moreBtn, "more")
        self.common_functions.set_icon(self.closeAppBtn, "close")
        self.common_functions.set_icon(self.minimizeAppBtn, "minimize")
        self.common_functions.set_icon(self.maximizeAppBtn, "maximize")
        self.common_functions.set_icon(self.extraCloseColumnBtn, "close")

        # MAIN PAGE
        self.set_bg_image(self.home_widgets,"File Engine vertical", False,"background-position: center; background-repeat: no-repeat")

        # MAIN OPTIONS
        self.set_bg_image(self.toggleButton, "menu")
        self.set_bg_image(self.home_page_btn, "home")
        self.set_bg_image(self.toggleLeftBox, "settings")
        self.set_bg_image(self.move_page_btn, "file move")
        self.set_bg_image(self.delete_page_btn, "trash-can")
        self.set_bg_image(self.rename_page_btn, "rename-outline")
        self.set_bg_image(self.search_page_btn, "search-outline")

        # RIGHT MENU OPTIONS
        self.set_bg_image(self.btn_print, "home")
        self.set_bg_image(self.btn_logout, "home")
        self.set_bg_image(self.removeTrashOption, "empty_recycle_bin")

        # LEFT MENU OPTIONS
        self.set_bg_image(self.displayModeOption, "display-mode-outline")

        # CLICK ACTIONS
        self.displayModeOption.pressed.connect(self.ui_function.set_display_mode)
        self.removeTrashOption.pressed.connect(self.ui_function.empty_trash)
        # fmt: on

        self.stackedWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow", u"MainWindow", None
            )
        )

        objs = {
            # OBJECT:                  (TEXT, TOOLTIP)
            self.displayModeOption:     ("LIGHT/DARK MODE", ""),
            self.btn_adjustments:       ("-", ""),
            self.btn_more:              ("-", ""),
            self.removeTrashOption:     ("REMOVE TRASH", "Deletes cached trash."),
            self.btn_print:             ("-", ""),
            self.btn_logout:            ("-", ""),
            self.toggleButton:          ("HIDE", ""),
            self.home_page_btn:         ("HOME", ""),
            self.move_page_btn:         ("MOVE", ""),
            self.moreBtn:               ("", "More"),
            self.closeAppBtn:           ("", "Close"),
            self.delete_page_btn:       ("DELETE", ""),
            self.rename_page_btn:       ("RENAME", ""),
            self.version:               ("v1.3.0", ""),
            self.search_page_btn:       ("SEARCH", ""),
            self.toggleLeftBox:         ("Settings", ""),
            self.extraLabel:            ("Settings", ""),
            self.minimizeAppBtn:        ("", "Minimize"),
            self.maximizeAppBtn:        ("", "Maximize"),
            self.titleLeftApp:          ("File Engine", ""),
            self.label:                 ("NEW PAGE TEST", ""),
            self.extraCloseColumnBtn:   ("", "Close Settings"),
            self.titleLeftDescription:  ("Dracula Dark Theme", ""),
            self.creditsLabel:          ("Developed by @OfficialAhmed0", ""),
            self.titleRightInfo:        ("File Engine - File management and automation tool", ""),
        }

        # TRANSLATE TEXT AND TOOLTIPS
        for obj, (text, tooltip) in objs.items():

            if text:
                obj.setText(
                    QCoreApplication.translate(
                        "MainWindow", text, None
                    )
                )

            if tooltip:
                obj.setToolTip(
                    QCoreApplication.translate(
                        "MainWindow", tooltip, None
                    )
                )

        self.textEdit.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                self.common_functions.html.get_credits_page(),
                None
            )
        )

    def set_bg_image(self, widget: QWidget, name: str, is_icon=True, extra_style="") -> None:
        """
            SET IMAGES FROM GENERATED RESOURCES.RC
        """

        # Determine path and extension
        path = "icons" if is_icon else "images"
        ext = "svg" if is_icon else "png"

        widget.setStyleSheet(
            f"background-image: url({self.common_functions.paths.RESOURCES_PATH}{path}/{name}.{ext});\
            {extra_style}"
        )
