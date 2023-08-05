# Form implementation generated from reading ui file 'qt/aqt/forms/fields.ui'
#
# Created by: PyQt5 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from aqt.utils import tr



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 438)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fieldList = QtWidgets.QListWidget(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldList.sizePolicy().hasHeightForWidth())
        self.fieldList.setSizePolicy(sizePolicy)
        self.fieldList.setMinimumSize(QtCore.QSize(50, 60))
        self.fieldList.setObjectName("fieldList")
        self.horizontalLayout.addWidget(self.fieldList)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fieldAdd = QtWidgets.QPushButton(parent=Dialog)
        self.fieldAdd.setObjectName("fieldAdd")
        self.verticalLayout_3.addWidget(self.fieldAdd)
        self.fieldDelete = QtWidgets.QPushButton(parent=Dialog)
        self.fieldDelete.setObjectName("fieldDelete")
        self.verticalLayout_3.addWidget(self.fieldDelete)
        self.fieldRename = QtWidgets.QPushButton(parent=Dialog)
        self.fieldRename.setObjectName("fieldRename")
        self.verticalLayout_3.addWidget(self.fieldRename)
        self.fieldPosition = QtWidgets.QPushButton(parent=Dialog)
        self.fieldPosition.setObjectName("fieldPosition")
        self.verticalLayout_3.addWidget(self.fieldPosition)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self._2 = QtWidgets.QGridLayout()
        self._2.setObjectName("_2")
        self.label_description = QtWidgets.QLabel(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_description.sizePolicy().hasHeightForWidth())
        self.label_description.setSizePolicy(sizePolicy)
        self.label_description.setObjectName("label_description")
        self._2.addWidget(self.label_description, 0, 0, 1, 1)
        self.label_font = QtWidgets.QLabel(parent=Dialog)
        self.label_font.setObjectName("label_font")
        self._2.addWidget(self.label_font, 1, 0, 1, 1)
        self.fontSize = QtWidgets.QSpinBox(parent=Dialog)
        self.fontSize.setMinimum(5)
        self.fontSize.setMaximum(300)
        self.fontSize.setObjectName("fontSize")
        self._2.addWidget(self.fontSize, 1, 2, 1, 1)
        self.label_sort = QtWidgets.QLabel(parent=Dialog)
        self.label_sort.setObjectName("label_sort")
        self._2.addWidget(self.label_sort, 2, 0, 1, 1)
        self.fontFamily = QtWidgets.QFontComboBox(parent=Dialog)
        self.fontFamily.setMinimumSize(QtCore.QSize(0, 25))
        self.fontFamily.setObjectName("fontFamily")
        self._2.addWidget(self.fontFamily, 1, 1, 1, 1)
        self.rtl = QtWidgets.QCheckBox(parent=Dialog)
        self.rtl.setObjectName("rtl")
        self._2.addWidget(self.rtl, 3, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.plainTextByDefault = QtWidgets.QCheckBox(parent=Dialog)
        self.plainTextByDefault.setEnabled(True)
        self.plainTextByDefault.setObjectName("plainTextByDefault")
        self._2.addWidget(self.plainTextByDefault, 4, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.fieldDescription = QtWidgets.QLineEdit(parent=Dialog)
        self.fieldDescription.setObjectName("fieldDescription")
        self._2.addWidget(self.fieldDescription, 0, 1, 1, 2)
        self.sortField = QtWidgets.QRadioButton(parent=Dialog)
        self.sortField.setObjectName("sortField")
        self._2.addWidget(self.sortField, 2, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.collapseByDefault = QtWidgets.QCheckBox(parent=Dialog)
        self.collapseByDefault.setEnabled(True)
        self.collapseByDefault.setObjectName("collapseByDefault")
        self._2.addWidget(self.collapseByDefault, 5, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.excludeFromSearch = QtWidgets.QCheckBox(parent=Dialog)
        self.excludeFromSearch.setEnabled(True)
        self.excludeFromSearch.setObjectName("excludeFromSearch")
        self._2.addWidget(self.excludeFromSearch, 6, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout.addLayout(self._2)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Help|QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.fieldList, self.fieldAdd)
        Dialog.setTabOrder(self.fieldAdd, self.fieldDelete)
        Dialog.setTabOrder(self.fieldDelete, self.fieldRename)
        Dialog.setTabOrder(self.fieldRename, self.fieldPosition)
        Dialog.setTabOrder(self.fieldPosition, self.fieldDescription)
        Dialog.setTabOrder(self.fieldDescription, self.fontFamily)
        Dialog.setTabOrder(self.fontFamily, self.fontSize)
        Dialog.setTabOrder(self.fontSize, self.sortField)
        Dialog.setTabOrder(self.sortField, self.rtl)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(tr.editing_fields())
        self.fieldAdd.setText(tr.actions_add())
        self.fieldDelete.setText(tr.actions_delete())
        self.fieldRename.setText(tr.actions_rename())
        self.fieldPosition.setText(tr.actions_reposition())
        self.label_description.setText(tr.fields_description())
        self.label_font.setText(tr.fields_editing_font())
        self.label_sort.setText(tr.actions_options())
        self.rtl.setText(tr.fields_reverse_text_direction_rtl())
        self.plainTextByDefault.setText(tr.fields_html_by_default())
        self.fieldDescription.setPlaceholderText(tr.fields_description_placeholder())
        self.sortField.setText(tr.fields_sort_by_this_field_in_the())
        self.collapseByDefault.setText(tr.fields_collapse_by_default())
        self.excludeFromSearch.setText(tr.fields_exclude_from_search())