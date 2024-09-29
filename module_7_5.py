# Домашнее задание по теме "Файлы в операционной системе"

import os
from datetime import datetime

for root, dirs, files in os.walk('.'):
  for file in files:
      full_path = os.path.abspath(os.path.join(root, file))
      file_size = os.path.getsize(full_path)
      mod_time = os.path.getmtime(full_path)
      mod_time_1 = datetime.fromtimestamp(mod_time)
      par_dir = os.path.dirname(full_path)

      print(f'Обнаружен файл: {file}, путь: {full_path}, размер: {file_size}, время изменения: {mod_time_1}, родительская '
            f'директория: {par_dir}')






