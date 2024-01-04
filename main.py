from pathlib import Path
import shutil
import sys
 
 # Сортування файлів за їхнім розширенням
def sort(path, root_folder):
     folder_path = Path(path)
     for file_path in folder_path.iterdir():
         if file_path.is_file():
             extension = file_path.suffix[1:].upper()  # Отримання розширення файлу без крапки
             moved = False
             for category, extensions in file_categories.items():
                 if extension in extensions:
                     shutil.move(str(file_path), str(root_folder / category / file_path.name))
                     moved = True
                     break
             # Якщо розширення не належить до жодної категорії, перемістимо файл в папку "unknown"
             if not moved:
                 shutil.move(str(file_path), str(root_folder / 'unknown' / file_path.name))
         else:
             sort(file_path, root_folder)
 
 # Шлях до папки, яку потрібно сортувати
folder_path = Path('cp')
 # Створення словника, де ключі - це категорії файлів, а значення - це список розширень цієї категорії
file_categories = {
     'images': ('JPEG', 'PNG', 'JPG', 'SVG'),
     'videos': ('AVI', 'MP4', 'MOV', 'MKV'),
     'documents': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
     'music': ('MP3', 'OGG', 'WAV', 'AMR'),
     'archives': ('ZIP', 'GZ', 'TAR'),
     'unknown': ()
 }
 # Створення папок для кожної категорії, якщо вони ще не існують
for category in file_categories.keys():
     (folder_path / category).mkdir(exist_ok=True)
 
sort(folder_path, folder_path)
 
print("Сортування завершено!")