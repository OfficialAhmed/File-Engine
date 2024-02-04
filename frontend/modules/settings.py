from main import MainWindow
from frontend.widgets.custom_grips import *


class UiStyle:

    ENABLE_CUSTOM_TITLE_BAR = True
    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """


class UiSettings(MainWindow):
    GLOBAL_STATE = False
    GLOBAL_TITLE_BAR = True

    # RETURN STATUS
    def get_state(self):
        return UiSettings.GLOBAL_STATE

    # MAXIMIZE AND RESTORE WINDOW
    def maximize_restore(self):

        # global GLOBAL_STATE
        is_maximized = UiSettings.GLOBAL_STATE

        if not is_maximized:

            UiSettings.GLOBAL_STATE = True
            self.showMaximized()

            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeAppBtn.setToolTip("Restore")
            self.ui.maximizeAppBtn.setIcon(
                QIcon(u"frontend/icons/minimize_window.svg")
            )

            self.ui.frame_size_grip.hide()
            self.top_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.bottom_grip.hide()

        else:

            UiSettings.GLOBAL_STATE = False
            self.showNormal()

            self.resize(self.width() + 1, self.height() + 1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeAppBtn.setToolTip("Maximize")
            self.ui.maximizeAppBtn.setIcon(
                QIcon(u"frontend/icons/maximize.svg")
            )

            self.ui.frame_size_grip.show()
            self.top_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.bottom_grip.show()

    def toggleMenu(self, is_enabled: bool) -> None:

        if is_enabled:

            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            max_extended = UiStyle.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            width_extended = standard
            if width == 60:
                width_extended = max_extended

            # ANIMATION
            self.animation = QPropertyAnimation(
                self.ui.leftMenuBg,
                b"minimumWidth"
            )
            self.animation.setDuration(UiStyle.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def toggleLeftBox(self, is_enabled) -> None:
        """
            TOGGLE RIGHTSIDE MENU
        """

        if is_enabled:

            # GET WIDTH
            width = self.ui.extraLeftBox.width()
            widthRightBox = self.ui.extraRightBox.width()
            color = UiStyle.BTN_LEFT_BOX_COLOR

            # GET BTN STYLE
            style = self.ui.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:

                # SELECT BTN
                self.ui.toggleLeftBox.setStyleSheet(style + color)

                if widthRightBox != 0:
                    style = self.ui.moreBtn.styleSheet()
                    self.ui.moreBtn.setStyleSheet(
                        style.replace(UiStyle.BTN_RIGHT_BOX_COLOR, ''))
            else:
                # RESET BTN
                self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))

        UiSettings.start_box_animation(self, width, widthRightBox, "left")

    def toggleRightBox(self, is_enabled: bool) -> None:
        """
            TOGGLE RIGHTSIDE MENU
        """

        if is_enabled:

            # GET WIDTH
            width = self.ui.extraRightBox.width()
            widthLeftBox = self.ui.extraLeftBox.width()
            color = UiStyle.BTN_RIGHT_BOX_COLOR

            # GET BTN STYLE
            style = self.ui.moreBtn.styleSheet()

            # SET MAX WIDTH
            if width == 0:

                # SELECT BTN
                self.ui.moreBtn.setStyleSheet(style + color)

                if widthLeftBox != 0:
                    style = self.ui.toggleLeftBox.styleSheet()
                    self.ui.toggleLeftBox.setStyleSheet(
                        style.replace(UiStyle.BTN_LEFT_BOX_COLOR, ''))
            else:
                # RESET BTN
                self.ui.moreBtn.setStyleSheet(style.replace(color, ''))

            UiSettings.start_box_animation(self, widthLeftBox, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):

        right_width = 0
        left_width = 0

        if left_box_width == 0 and direction == "left":
            left_width = 240

        if right_box_width == 0 and direction == "right":
            right_width = 240

        # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(
            self.ui.extraLeftBox,
            b"minimumWidth"
        )
        self.left_box.setDuration(UiStyle.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.right_box = QPropertyAnimation(
            self.ui.extraRightBox,
            b"minimumWidth"
        )
        self.right_box.setDuration(UiStyle.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    # SELECT LEFT MENU OPTION STYLE
    def selectMenu(getStyle):
        return getStyle + UiStyle.MENU_SELECTED_STYLESHEET

    # DESELECT LEFT MENU OPTION STYLE
    def deselectMenu(getStyle):
        return getStyle.replace(UiStyle.MENU_SELECTED_STYLESHEET, "")

    # START SELECTION
    def selectStandardMenu(self, widget):

        for w in self.ui.topMenu.findChildren(QPushButton):

            if w.objectName() == widget:
                w.setStyleSheet(UiSettings.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):

        for w in self.ui.topMenu.findChildren(QPushButton):

            if w.objectName() != widget:
                w.setStyleSheet(UiSettings.deselectMenu(w.styleSheet()))

    # IMPORT THEMES FILES QSS/CSS
    def theme(self, is_light_theme):

        if is_light_theme:

            str = open("Interface\\themes\\py_dracula_light.qss").read()
            self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    def uiDefinitions(self):

        def dobleClickMaximizeRestore(event):

            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(
                    250,
                    lambda: UiSettings.maximize_restore(self)
                )

        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if UiStyle.ENABLE_CUSTOM_TITLE_BAR:

            # STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):

                # IF MAXIMIZED CHANGE TO NORMAL
                if UiSettings.get_state(self):
                    UiSettings.maximize_restore(self)

                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet(
            "width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(
            lambda: UiSettings.showMinimized(self))

        # MAXIMIZE/RESTORE
        self.ui.maximizeAppBtn.clicked.connect(
            lambda: UiSettings.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: UiSettings.close(self))
