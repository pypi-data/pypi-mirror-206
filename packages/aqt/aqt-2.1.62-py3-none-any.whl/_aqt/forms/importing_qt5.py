# Form implementation generated from reading ui file 'qt/aqt/forms/importing.ui'
#
# Created by: PyQt5 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from aqt.utils import tr



class Ui_ImportDialog(object):
    def setupUi(self, ImportDialog):
        ImportDialog.setObjectName("ImportDialog")
        ImportDialog.resize(553, 466)
        self.vboxlayout = QtWidgets.QVBoxLayout(ImportDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox = QtWidgets.QGroupBox(parent=ImportDialog)
        self.groupBox.setObjectName("groupBox")
        self.toplayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.toplayout.setObjectName("toplayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.deckArea = QtWidgets.QWidget(parent=self.groupBox)
        self.deckArea.setObjectName("deckArea")
        self.gridLayout_2.addWidget(self.deckArea, 0, 3, 1, 1)
        self.modelArea = QtWidgets.QWidget(parent=self.groupBox)
        self.modelArea.setObjectName("modelArea")
        self.gridLayout_2.addWidget(self.modelArea, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.toplayout.addLayout(self.gridLayout_2)
        self.autoDetect = QtWidgets.QPushButton(parent=self.groupBox)
        self.autoDetect.setText("")
        self.autoDetect.setObjectName("autoDetect")
        self.toplayout.addWidget(self.autoDetect)
        self.importMode = QtWidgets.QComboBox(parent=self.groupBox)
        self.importMode.setObjectName("importMode")
        self.importMode.addItem("")
        self.importMode.addItem("")
        self.importMode.addItem("")
        self.toplayout.addWidget(self.importMode)
        self.allowHTML = QtWidgets.QCheckBox(parent=self.groupBox)
        self.allowHTML.setObjectName("allowHTML")
        self.toplayout.addWidget(self.allowHTML, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.tagModifiedLayout = QtWidgets.QHBoxLayout()
        self.tagModifiedLayout.setObjectName("tagModifiedLayout")
        self.tagModifiedLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.tagModifiedLabel.setObjectName("tagModifiedLabel")
        self.tagModifiedLayout.addWidget(self.tagModifiedLabel)
        self.tagModified = TagEdit(parent=self.groupBox)
        self.tagModified.setObjectName("tagModified")
        self.tagModifiedLayout.addWidget(self.tagModified)
        self.toplayout.addLayout(self.tagModifiedLayout)
        self.vboxlayout.addWidget(self.groupBox)
        self.mappingGroup = QtWidgets.QGroupBox(parent=ImportDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mappingGroup.sizePolicy().hasHeightForWidth())
        self.mappingGroup.setSizePolicy(sizePolicy)
        self.mappingGroup.setObjectName("mappingGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mappingGroup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mappingArea = QtWidgets.QScrollArea(parent=self.mappingGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mappingArea.sizePolicy().hasHeightForWidth())
        self.mappingArea.setSizePolicy(sizePolicy)
        self.mappingArea.setMinimumSize(QtCore.QSize(400, 150))
        self.mappingArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.mappingArea.setWidgetResizable(True)
        self.mappingArea.setObjectName("mappingArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 529, 251))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.mappingArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.mappingArea, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.vboxlayout.addWidget(self.mappingGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=ImportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Close|QtWidgets.QDialogButtonBox.StandardButton.Help)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ImportDialog)
        self.buttonBox.accepted.connect(ImportDialog.accept) # type: ignore  # type: ignore
        self.buttonBox.rejected.connect(ImportDialog.reject) # type: ignore  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ImportDialog)

    def retranslateUi(self, ImportDialog):
        _translate = QtCore.QCoreApplication.translate
        ImportDialog.setWindowTitle(tr.actions_import())
        self.groupBox.setTitle(tr.importing_import_options())
        self.label.setText(tr.notetypes_type())
        self.label_2.setText(tr.decks_deck())
        self.importMode.setItemText(0, tr.importing_update_existing_notes_when_first_field())
        self.importMode.setItemText(1, tr.importing_ignore_lines_where_first_field_matches())
        self.importMode.setItemText(2, tr.importing_import_even_if_existing_note_has())
        self.allowHTML.setText(tr.importing_allow_html_in_fields())
        self.tagModifiedLabel.setText(tr.importing_tag_modified_notes())
        self.mappingGroup.setTitle(tr.importing_field_mapping())
from aqt.tagedit import TagEdit