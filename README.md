## Proyecto de Traducción de Comentarios

Este proyecto tiene como objetivo traducir comentarios en archivos .al del español al portugués utilizando la biblioteca googletrans.

## Descripción

El script recorre un proyecto, encuentra todos los comentarios en los archivos .al, y los traduce del español al portugués. Si un comentario ya está traducido, no se vuelve a traducir. Los comentarios traducidos se formatean como ESP=original|PTG=traducción.

## Requisitos

- Python 3.x
- Biblioteca googletrans

Puedes instalar la biblioteca googletrans usando pip:

pip install googletrans==4.0.0-rc1

## Uso

1. Descarga el script en python.
2. Asegúrate de tener todos los requisitos instalados.
3. Modifica la variable project_path en el script principal para que apunte a la ruta de tu proyecto.
4. Ejecuta el script:

python nombre_del_script.py

" > README.md
