"""
    Importante toga.MapView no esta en la version 4.2.0, hasta el momento
    Marzo 2024, esta en la rama de desarrollo y aún no es accesible por pip.
"""

import toga
from toga.constants import COLUMN, ROW


def build(app):
    # Crear una instancia de la ventana principal
    main_window = toga.MainWindow(title="MapView Demo", size=(800, 600))

    # Crear una instancia de la clase MapView
    mapview = toga.MapView()

    # Establecer la ubicación inicial del mapa (latitud y longitud)
    # Coordenadas de Nueva York como ejemplo
    mapview.location = (40.7128, -74.0060)

    # Establecer el nivel de zoom inicial del mapa
    mapview.zoom = 10

    # Agregar la vista MapView a la ventana principal
    main_window.content = mapview

    # Mostrar la ventana
    main_window.show()


def main():
    # Crear una instancia de la aplicación
    app = toga.App('MapView Demo', 'org.example.mapviewdemo', startup=build)

    # Ejecutar la aplicación
    app.main_loop()


if __name__ == '__main__':
    main()
