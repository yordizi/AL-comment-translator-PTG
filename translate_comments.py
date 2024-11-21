import os
import re
from googletrans import Translator

def translate_comment(comment, translator):
    """Traduce un comentario del español al portugués."""
    try:
        # Verifica si el comentario ya está en portugués
        if "PTG=" in comment:
            return comment.split("PTG=")[-1]
        
        translation = translator.translate(comment, src='es', dest='pt')
        if translation is None:
            translation = ""
        return translation.text
    except Exception as e:
        print(f"Error al traducir el comentario: {comment}. Error: {e}")
        return ""

def process_file(file_path, translator):
    """Procesa un archivo .al, traduce los comentarios y los actualiza."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Encuentra todos los comentarios usando regex
        comments = re.findall(r"Comment\s*=\s*'([^']*)'", content)

        for comment in comments:
            # Traduce el comentario al portugués si no está ya traducido
            if "PTG=" not in comment:
                translated_comment = translate_comment(comment, translator)
                # Reemplaza el comentario original con el formato solicitado
                formatted_comment = f"ESP={comment}|PTG={translated_comment}"
                content = content.replace(f"Comment = '{comment}'", f"Comment = '{formatted_comment}'")

        # Escribe el contenido modificado de vuelta al archivo
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error al procesar el archivo {file_path}. Error: {e}")

def process_project(project_path):
    """Recorre el proyecto y procesa todos los archivos .al."""
    translator = Translator()
    
    print("Procesando archivos...")
    try:
        for root, dirs, files in os.walk(project_path):
            for file in files:
                if file.endswith('.al'):
                    file_path = os.path.join(root, file)
                    process_file(file_path, translator)
        print("Comentarios traducidos al portugués!")
    except Exception as e:
        print(f"Error al procesar el proyecto en la ruta {project_path}. Error: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    project_path = r'C:\Users\jramos\ruta_de_tu_proyecto\src'
    process_project(project_path)
