# Form implementation generated from reading ui file 'qt/aqt/forms/findreplace.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from aqt.utils import tr



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(479, 247)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.replace = QtWidgets.QComboBox(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replace.sizePolicy().hasHeightForWidth())
        self.replace.setSizePolicy(sizePolicy)
        self.replace.setEditable(True)
        self.replace.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.replace.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.replace.setObjectName("replace")
        self.gridLayout.addWidget(self.replace, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.field = QtWidgets.QComboBox(parent=Dialog)
        self.field.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.field.setObjectName("field")
        self.gridLayout.addWidget(self.field, 2, 1, 1, 1)
        self.re = QtWidgets.QCheckBox(parent=Dialog)
        self.re.setObjectName("re")
        self.gridLayout.addWidget(self.re, 5, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.ignoreCase = QtWidgets.QCheckBox(parent=Dialog)
        self.ignoreCase.setChecked(True)
        self.ignoreCase.setObjectName("ignoreCase")
        self.gridLayout.addWidget(self.ignoreCase, 4, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.find = QtWidgets.QComboBox(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.find.sizePolicy().hasHeightForWidth())
        self.find.setSizePolicy(sizePolicy)
        self.find.setEditable(True)
        self.find.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.find.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.find.setObjectName("find")
        self.gridLayout.addWidget(self.find, 0, 1, 1, 1)
        self.selected_notes = QtWidgets.QCheckBox(parent=Dialog)
        self.selected_notes.setChecked(True)
        self.selected_notes.setObjectName("selected_notes")
        self.gridLayout.addWidget(self.selected_notes, 3, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Help|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.find, self.replace)
        Dialog.setTabOrder(self.replace, self.field)
        Dialog.setTabOrder(self.field, self.ignoreCase)
        Dialog.setTabOrder(self.ignoreCase, self.re)
        Dialog.setTabOrder(self.re, self.buttonBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(tr.browsing_find_and_replace())
        self.label_2.setText(tr.browsing_replace_with())
        self.label_3.setText(tr.browsing_in())
        self.label.setText(tr.browsing_find())
        self.re.setText(tr.browsing_treat_input_as_regular_expression())
        self.ignoreCase.setText(tr.browsing_ignore_case())
        self.selected_notes.setText(tr.browsing_selected_notes_only())