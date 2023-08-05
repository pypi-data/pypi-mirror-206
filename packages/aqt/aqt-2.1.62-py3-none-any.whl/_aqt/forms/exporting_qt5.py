# Form implementation generated from reading ui file 'qt/aqt/forms/exporting.ui'
#
# Created by: PyQt5 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from aqt.utils import tr



class Ui_ExportDialog(object):
    def setupUi(self, ExportDialog):
        ExportDialog.setObjectName("ExportDialog")
        ExportDialog.resize(550, 200)
        self.vboxlayout = QtWidgets.QVBoxLayout(ExportDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtWidgets.QLabel(parent=ExportDialog)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.format = QtWidgets.QComboBox(parent=ExportDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.format.sizePolicy().hasHeightForWidth())
        self.format.setSizePolicy(sizePolicy)
        self.format.setObjectName("format")
        self.gridlayout.addWidget(self.format, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=ExportDialog)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.deck = QtWidgets.QComboBox(parent=ExportDialog)
        self.deck.setMinimumContentsLength(50)
        self.deck.setObjectName("deck")
        self.gridlayout.addWidget(self.deck, 1, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.includeSched = QtWidgets.QCheckBox(parent=ExportDialog)
        self.includeSched.setChecked(True)
        self.includeSched.setObjectName("includeSched")
        self.vboxlayout1.addWidget(self.includeSched, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.includeMedia = QtWidgets.QCheckBox(parent=ExportDialog)
        self.includeMedia.setChecked(True)
        self.includeMedia.setObjectName("includeMedia")
        self.vboxlayout1.addWidget(self.includeMedia, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.includeHTML = QtWidgets.QCheckBox(parent=ExportDialog)
        self.includeHTML.setObjectName("includeHTML")
        self.vboxlayout1.addWidget(self.includeHTML, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.includeTags = QtWidgets.QCheckBox(parent=ExportDialog)
        self.includeTags.setChecked(True)
        self.includeTags.setObjectName("includeTags")
        self.vboxlayout1.addWidget(self.includeTags, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.includeDeck = QtWidgets.QCheckBox(parent=ExportDialog)
        self.includeDeck.setEnabled(True)
        self.includeDeck.setObjectName("includeDeck")
        self.vboxlayout1.addWidget(self.includeDeck, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.includeNotetype = QtWidgets.QCheckBox(parent=ExportDialog)
        self.includeNotetype.setEnabled(True)
        self.includeNotetype.setObjectName("includeNotetype")
        self.vboxlayout1.addWidget(self.includeNotetype, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.includeGuid = QtWidgets.QCheckBox(parent=ExportDialog)
        self.includeGuid.setObjectName("includeGuid")
        self.vboxlayout1.addWidget(self.includeGuid, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.legacy_support = QtWidgets.QCheckBox(parent=ExportDialog)
        self.legacy_support.setChecked(True)
        self.legacy_support.setObjectName("legacy_support")
        self.vboxlayout1.addWidget(self.legacy_support, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.vboxlayout.addLayout(self.vboxlayout1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=ExportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ExportDialog)
        self.buttonBox.accepted.connect(ExportDialog.accept) # type: ignore  # type: ignore
        self.buttonBox.rejected.connect(ExportDialog.reject) # type: ignore  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ExportDialog)
        ExportDialog.setTabOrder(self.format, self.deck)
        ExportDialog.setTabOrder(self.deck, self.includeSched)
        ExportDialog.setTabOrder(self.includeSched, self.includeMedia)
        ExportDialog.setTabOrder(self.includeMedia, self.includeTags)
        ExportDialog.setTabOrder(self.includeTags, self.buttonBox)

    def retranslateUi(self, ExportDialog):
        _translate = QtCore.QCoreApplication.translate
        ExportDialog.setWindowTitle(tr.actions_export())
        self.label.setText(tr.exporting_export_format())
        self.label_2.setText(tr.exporting_include())
        self.includeSched.setText(tr.exporting_include_scheduling_information())
        self.includeMedia.setText(tr.exporting_include_media())
        self.includeHTML.setText(tr.exporting_include_html_and_media_references())
        self.includeTags.setText(tr.exporting_include_tags())
        self.includeDeck.setText(tr.exporting_include_deck())
        self.includeNotetype.setText(tr.exporting_include_notetype())
        self.includeGuid.setText(tr.exporting_include_guid())
        self.legacy_support.setText(tr.exporting_support_older_anki_versions())