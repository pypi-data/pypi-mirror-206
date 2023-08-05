# -*- coding: utf-8 -*-

# File generated according to PMSlot13.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PMSlot13(object):
    def setupUi(self, PMSlot13):
        if not PMSlot13.objectName():
            PMSlot13.setObjectName(u"PMSlot13")
        PMSlot13.resize(899, 470)
        PMSlot13.setMinimumSize(QSize(630, 470))
        PMSlot13.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PMSlot13)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_slot = QLabel(PMSlot13)
        self.img_slot.setObjectName(u"img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WMSlot/SlotM13.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.txt_constraint = QTextEdit(PMSlot13)
        self.txt_constraint.setObjectName(u"txt_constraint")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy1)
        self.txt_constraint.setMaximumSize(QSize(16777215, 50))
        self.txt_constraint.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse
        )

        self.verticalLayout_2.addWidget(self.txt_constraint)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(PMSlot13)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 446))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName(u"in_W0")

        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName(u"lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)

        self.unit_W0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W0.setObjectName(u"unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 0, 2, 1, 1)

        self.in_Wmag = QLabel(self.scrollAreaWidgetContents)
        self.in_Wmag.setObjectName(u"in_Wmag")

        self.gridLayout.addWidget(self.in_Wmag, 1, 0, 1, 1)

        self.lf_Wmag = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_Wmag.setObjectName(u"lf_Wmag")

        self.gridLayout.addWidget(self.lf_Wmag, 1, 1, 1, 1)

        self.unit_Wmag = QLabel(self.scrollAreaWidgetContents)
        self.unit_Wmag.setObjectName(u"unit_Wmag")

        self.gridLayout.addWidget(self.unit_Wmag, 1, 2, 1, 1)

        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName(u"in_H0")

        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)

        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName(u"lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)

        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName(u"unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 2, 2, 1, 1)

        self.in_Hmag = QLabel(self.scrollAreaWidgetContents)
        self.in_Hmag.setObjectName(u"in_Hmag")

        self.gridLayout.addWidget(self.in_Hmag, 3, 0, 1, 1)

        self.lf_Hmag = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_Hmag.setObjectName(u"lf_Hmag")

        self.gridLayout.addWidget(self.lf_Hmag, 3, 1, 1, 1)

        self.unit_Hmag = QLabel(self.scrollAreaWidgetContents)
        self.unit_Hmag.setObjectName(u"unit_Hmag")

        self.gridLayout.addWidget(self.unit_Hmag, 3, 2, 1, 1)

        self.in_Rtopm = QLabel(self.scrollAreaWidgetContents)
        self.in_Rtopm.setObjectName(u"in_Rtopm")

        self.gridLayout.addWidget(self.in_Rtopm, 4, 0, 1, 1)

        self.lf_Rtopm = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_Rtopm.setObjectName(u"lf_Rtopm")

        self.gridLayout.addWidget(self.lf_Rtopm, 4, 1, 1, 1)

        self.unit_Rtopm = QLabel(self.scrollAreaWidgetContents)
        self.unit_Rtopm.setObjectName(u"unit_Rtopm")

        self.gridLayout.addWidget(self.unit_Rtopm, 4, 2, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.w_out = WWSlotOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout_3.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_W0, self.lf_Wmag)
        QWidget.setTabOrder(self.lf_Wmag, self.lf_H0)
        QWidget.setTabOrder(self.lf_H0, self.lf_Hmag)
        QWidget.setTabOrder(self.lf_Hmag, self.txt_constraint)

        self.retranslateUi(PMSlot13)

        QMetaObject.connectSlotsByName(PMSlot13)

    # setupUi

    def retranslateUi(self, PMSlot13):
        PMSlot13.setWindowTitle(QCoreApplication.translate("PMSlot13", u"Form", None))
        self.img_slot.setText("")
        self.txt_constraint.setHtml(
            QCoreApplication.translate(
                "PMSlot13",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'DejaVu Sans'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">Wmag \u2264 W0</span></p></body></html>',
                None,
            )
        )
        self.in_W0.setText(QCoreApplication.translate("PMSlot13", u"W0", None))
        self.unit_W0.setText(QCoreApplication.translate("PMSlot13", u"[m]", None))
        self.in_Wmag.setText(QCoreApplication.translate("PMSlot13", u"Wmag", None))
        self.unit_Wmag.setText(QCoreApplication.translate("PMSlot13", u"[m]", None))
        self.in_H0.setText(QCoreApplication.translate("PMSlot13", u"H0", None))
        self.unit_H0.setText(QCoreApplication.translate("PMSlot13", u"[m]", None))
        self.in_Hmag.setText(QCoreApplication.translate("PMSlot13", u"Hmag", None))
        self.unit_Hmag.setText(QCoreApplication.translate("PMSlot13", u"[m]", None))
        self.in_Rtopm.setText(QCoreApplication.translate("PMSlot13", u"Rtopm", None))
        self.unit_Rtopm.setText(QCoreApplication.translate("PMSlot13", u"[m]", None))

    # retranslateUi
