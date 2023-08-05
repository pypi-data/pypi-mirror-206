# -*- coding: utf-8 -*-

# File generated according to PMSlot18.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PMSlot18(object):
    def setupUi(self, PMSlot18):
        if not PMSlot18.objectName():
            PMSlot18.setObjectName(u"PMSlot18")
        PMSlot18.resize(887, 470)
        PMSlot18.setMinimumSize(QSize(630, 470))
        PMSlot18.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PMSlot18)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_slot = QLabel(PMSlot18)
        self.img_slot.setObjectName(u"img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WMSlot/SlotM18.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(PMSlot18)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 446))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.unit_Hmag = QLabel(self.scrollAreaWidgetContents)
        self.unit_Hmag.setObjectName(u"unit_Hmag")

        self.gridLayout.addWidget(self.unit_Hmag, 0, 2, 1, 1)

        self.lf_Hmag = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_Hmag.setObjectName(u"lf_Hmag")

        self.gridLayout.addWidget(self.lf_Hmag, 0, 1, 1, 1)

        self.in_Hmag = QLabel(self.scrollAreaWidgetContents)
        self.in_Hmag.setObjectName(u"in_Hmag")

        self.gridLayout.addWidget(self.in_Hmag, 0, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.w_out = WWSlotOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(PMSlot18)

        QMetaObject.connectSlotsByName(PMSlot18)

    # setupUi

    def retranslateUi(self, PMSlot18):
        PMSlot18.setWindowTitle(QCoreApplication.translate("PMSlot18", u"Form", None))
        self.img_slot.setText("")
        self.unit_Hmag.setText(QCoreApplication.translate("PMSlot18", u"[m]", None))
        self.in_Hmag.setText(QCoreApplication.translate("PMSlot18", u"Hmag", None))

    # retranslateUi
