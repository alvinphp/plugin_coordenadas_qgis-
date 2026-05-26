from qgis.core import (
    QgsRasterLayer, 
    QgsProject, 
    QgsPointXY, 
    QgsCoordinateReferenceSystem, 
    QgsCoordinateTransform,
    QgsCsException
)
from qgis.PyQt.QtWidgets import QMessageBox

class MapaLocation:
    
    def __init__(self, iface):
        self.iface = iface

    def _asegurar_mapa_base(self):
        # Verifica si OpenStreetMap ya existe en el proyecto; si no, lo añade.
        capas_existentes = QgsProject.instance().mapLayersByName("OpenStreetMap")
        if not capas_existentes:
        # crea un mapa desde la internet 
            url = "type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png"
            layer = QgsRasterLayer(url, "OpenStreetMap", "wms")
            if layer.isValid():
                QgsProject.instance().addMapLayer(layer)

    def agregar_punto(self, x, y):
        # Carga el mapa base, transforma las coordenadas de grados a metros, centra y hace zoom.
        
        # VALIDACIÓN BÁSICA: Si metes un número fuera del rango planetario en grados, avisa de inmediato.
        if not (-180 <= x <= 180) or not (-90 <= y <= 90):
            QMessageBox.critical(
                self.iface.mainWindow(),
                "Error de Rango",
                f"Las coordenadas ingresadas (X: {x}, Y: {y}) no corresponden a Grados Decimales (WGS84).\n\n"
                "Asegúrate de ingresar valores correctos (Ej: X = -82.5220, Y = 9.4145)."
            )
            return

        # 1. Asegurar el mapa de fondo
        self._asegurar_mapa_base()
        
        try:
            # 2. Configurar la transformación de coordenadas (De Grados EPSG:4326 a lo que use el proyecto)
            crs_entrada = QgsCoordinateReferenceSystem("EPSG:4326")  
            crs_proyecto = self.iface.mapCanvas().mapSettings().destinationCrs() 
            
            transformacion = QgsCoordinateTransform(crs_entrada, crs_proyecto, QgsProject.instance())
            
            # 3. Crear el punto original en grados y transformarlo
            punto_grados = QgsPointXY(x, y)
            punto_transformado = transformacion.transform(punto_grados)
            
            # 4. Controlar el lienzo con el punto corregido
            canvas = self.iface.mapCanvas()
            canvas.setCenter(punto_transformado)
            canvas.zoomScale(3000)  # Zoom cercano a escala 1:3000
            canvas.refresh()
            
        except QgsCsException:
            # Captura el error si la transformación falla por distorsión matemática matemática
            QMessageBox.warning(
                self.iface.mainWindow(),
                "Error Geográfico",
                "QGIS no pudo transformar estas coordenadas al sistema del proyecto."
            )