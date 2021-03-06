from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class RemoveUserWindow(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		# LAYOUT CODE - GENERATED BY QTDESIGNER
		self.setGeometry(120, 120, 261, 191)
		self.setMinimumSize(QtCore.QSize(261, 191))
		self.setMaximumSize(QtCore.QSize(261, 191))
		self.groupBox = QtGui.QGroupBox(self)
		self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 121))
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.listWidget = QtGui.QListWidget(self.groupBox)
		self.listWidget.setGeometry(QtCore.QRect(10, 20, 221, 91))
		self.listWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
		self.listWidget.setTextElideMode(QtCore.Qt.ElideRight)
		self.listWidget.setUniformItemSizes(False)
		self.listWidget.setSelectionRectVisible(False)
		self.listWidget.setObjectName(_fromUtf8("listWidget"))
		self.selectAllButton = QtGui.QPushButton(self)
		self.selectAllButton.setGeometry(QtCore.QRect(10, 140, 71, 41))
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.selectAllButton.sizePolicy().hasHeightForWidth())
		self.selectAllButton.setSizePolicy(sizePolicy)
		self.selectAllButton.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
		self.selectAllButton.setObjectName(_fromUtf8("selectAllButton"))
		self.removeButton = QtGui.QPushButton(self)
		self.removeButton.setGeometry(QtCore.QRect(90, 140, 161, 41))
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
		self.removeButton.setSizePolicy(sizePolicy)
		self.removeButton.setObjectName(_fromUtf8("removeButton"))

		self.setWindowTitle(_translate("RemoveStreamer", "Remove Streamer", None))
		self.groupBox.setTitle(_translate("RemoveStreamer", "Select stream(s) to remove", None))
		__sortingEnabled = self.listWidget.isSortingEnabled()
		self.listWidget.setSortingEnabled(False)

		self.listWidget.setSortingEnabled(__sortingEnabled)
		self.selectAllButton.setText(_translate("RemoveStreamer", "Select All", None))
		self.removeButton.setText(_translate("RemoveStreamer", "Remove Selected", None))

		file = open("names.txt", "r")
		self.streamer_usernames = file.readlines()
		file.close()

		# Add usernames into list widget
		for streamerName in self.streamer_usernames:
			streamerName = streamerName.rstrip()
			self.listWidget.addItem(QtGui.QListWidgetItem(streamerName))

		self.selectAllButton.clicked.connect(self.selectAllNames)
		self.removeButton.clicked.connect(self.onNameChosen)


	def selectAllNames(self):
		for i in range(0, len(self.listWidget)):
			self.listWidget.item(i).setSelected(True)

	def onNameChosen(self):
		numSelected = 0
		selectedNames = []
		for i in range(0, len(self.listWidget)):
			if self.listWidget.item(i).isSelected():
				selectedNames.append(self.listWidget.item(i).text())
				numSelected+=1

		confirmation = QMessageBox.question(self, "Message", "Are you sure you want to remove " + str(numSelected) + " username(s)?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if confirmation == QMessageBox.Yes:
			file = open("names.txt", "w+")
			for i, l in enumerate(self.streamer_usernames):
				l = l.rstrip()
				if l not in selectedNames:
					if i == len(self.streamer_usernames)-1:
						file.write(l)
					else:
						file.write(l + "\n")
			file.close() # Close file
			self.close() # Close dialog box