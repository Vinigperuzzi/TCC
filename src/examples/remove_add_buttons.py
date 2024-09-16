mainWindow = None
field = None
grid = None
ButtonsAction = None

def QPushButton():
    ...

field = mainWindow.gridLayout
while field.count() > 0:
    item = field.takeAt(0)
    widget = item.widget()
    if widget is not None:
        widget.deleteLater()


grid = ButtonsAction.window.gridLayout
button = QPushButton("Opa")
grid.addWidget(button)