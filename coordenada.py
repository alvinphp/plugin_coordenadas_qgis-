# importamos clases para crear los componente del formulario
from qgis.PyQt.QtWidgets import QAction, QMessageBox, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel

from qgis.core import QgsRasterLayer, QgsProject
from .mapa import MapaLocation


# clase principal
class Coordenada:
    
    # Inicializa el plugin y guarda la interfaz de QGIS
    def __init__(self, iface):
        self.iface = iface
        self.action = None

        # creando el objeto de la clase
        self.mapa = MapaLocation(self.iface)
    
    # funcion que muestra el plugin dentro del qgis
    def initGui(self):
        # texto del boton en el qgis
        self.action = QAction("Ingresar Coordenadas", self.iface.mainWindow())

        # cuando ejecutamos el evento click ejecutamos la funcion run
        self.action.triggered.connect(self.run)
         
        # se usa para agregar la herramienta al menu superior de qgis
        self.iface.addPluginToMenu("&Coordenadas", self.action)

        # poner el boton en la barra de herramienta de qgis
        self.iface.addToolBarIcon(self.action)
    
    # esta funcion se usa para limpiar el plugin cuando se desactiva o se recarga
    def unload(self):
        self.iface.removePluginMenu("&Coordenadas", self.action)
        self.iface.removeToolBarIcon(self.action)
    
    # cuando se hace click en el boton ingresar coordenadas se ejecuta esta funcion
    def run(self):
        self.cargar_mapa_base()
        self.abrir_ventana()
    
    # funcion para cargar mapa base
    def cargar_mapa_base(self):

        url = "type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png"
        layer = QgsRasterLayer(url, "OpenStreetMap", "wms")

        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
    
    # funcion que crea y muestra el formulario dentro del qgis
    def abrir_ventana(self):
        # crea la ventana emergente y hace que quede dentro del qgis
        dialog = QDialog(self.iface.mainWindow())
        # titulo de la ventana
        dialog.setWindowTitle("Ingresar Coordenadas")
        # dimensiones de la ventana
        dialog.resize(300, 150)
        
        # contenedor que organiza todos los elementos en posicion vertical
        layout = QVBoxLayout()
         
        # muestra el texto que le muestra al usuario que debe insertar 
        layout.addWidget(QLabel("Coordenada X (Longitud):"))

        # campo o caja de texto donde el usuario insertar un valor en este caso coordenada
        self.x_input = QLineEdit()

        # coloca la caja de texto dentro de la ventana
        layout.addWidget(self.x_input)

        layout.addWidget(QLabel("Coordenada Y (Latitud):"))
        self.y_input = QLineEdit()
        layout.addWidget(self.y_input)
        
        # boton para insertar las coordenadas 
        btn = QPushButton("Mostrar Coordenadas")

        # cuando se hace click en el boton ejecuta la funcion mostrar_coordenadas()
        btn.clicked.connect(self.mostrar_coordenadas)

        # muestra el boton en la interfaz 
        layout.addWidget(btn)
        
        # mete todos los elementos y los organiza dentro de la ventana 
        dialog.setLayout(layout)

        # guardar la ventana para poder usarla después en el plugin
        self.dialog = dialog

        # Muestra la ventana en pantalla
        dialog.exec_()

    def mostrar_coordenadas(self):

        # toma valores que se guardaron en la caja de texto y lo guardamos en variables
        try:
            x = float(self.x_input.text())
            y = float(self.y_input.text())

            # llamando la funcion de la clase 
            self.mapa.agregar_punto(x, y)

        except ValueError:
            QMessageBox.warning(
                self.iface.mainWindow(),
                "Error",
                "Ingrese coordenadas válidas"
            )