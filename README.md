# Plugin coordenada - Plugin QGIS

## Descripción

**Plugin coordenada** es un plugin desarrollado para QGIS utilizando Python y PyQGIS.

El proyecto fue creado con fines educativos para aprender:

- El flujo de funcionamiento de QGIS.
- El desarrollo de plugins.
- Automatización dentro de QGIS.
- Programación en Python aplicada a sistemas GIS.
- Manejo del canvas y navegación de mapas.

El plugin permite buscar coordenadas y enfocar automáticamente el mapa en la ubicación indicada.

---

# Características

- Buscar coordenadas geográficas.
- Centrar automáticamente el mapa.
- Aplicar zoom dinámico.
- Navegación automática en el canvas.
- Interfaz simple para aprendizaje.

---

# Tecnologías utilizadas

- QGIS
- Python
- PyQGIS
- PyQt5
- Qt Designer

---

# Estructura del proyecto

```plaintext
MapFocus/
│
├── __init__.py
├── metadata.txt
├── mapfocus.py
├── mapfocus_dialog.py
├── mapfocus_dialog_base.ui
├── resources.py
├── resources.qrc
├── icon.png
└── README.md
```

---

# Funcionamiento

El plugin realiza el siguiente flujo:

1. Recibe coordenadas.
2. Crea un punto geográfico.
3. Cambia la extensión del mapa.
4. Centra el canvas.
5. Aplica zoom automáticamente.

---

# Instalación

## Windows

Copiar la carpeta del plugin en:

```plaintext
C:\Users\TU_USUARIO\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins
```

---

# Activación

1. Abrir QGIS.
2. Ir a:

```plaintext
Complementos > Administrar e instalar complementos
```

3. Activar el plugin **coordenada**.

---

# Requisitos

- QGIS 3.x
- Python 3.x

---



# Objetivo educativo

Este plugin fue desarrollado para comprender:

- Arquitectura de plugins QGIS.
- Automatización GIS.
- Programación orientada a objetos.
- Integración entre Python y QGIS.
- Navegación y manipulación de mapas.

---

# Autor

Alvin Gil Saldaña

Proyecto desarrollado con fines de aprendizaje y práctica en automatización GIS y desarrollo de plugins para QGIS.

---

# Licencia

Proyecto educativo y de código abierto.
