import os
import glob
from bs4 import BeautifulSoup
import shutil

num = 0
for xml_file in glob.glob('*.xml'):
    with open(xml_file, 'r', encoding='UTF-8') as f:
        soup = BeautifulSoup(f.read(), "lxml-xml")
    path_to_img = soup.select_one('path').text
    old_filename_img = soup.select_one('filename').text
    if not os.path.exists(path_to_img):
        print(f'Файл не найден! {path_to_img}')
        continue
    new_file_name = f'dolgonosik {num:02}'
    new_img_name = new_file_name + '.jpg'
    new_xml_name = new_file_name + '.xml'
    new_path_to_img = os.path.abspath(os.path.join('images/', new_img_name))
    new_path_to_xml = os.path.abspath(os.path.join('labels/', new_xml_name))
    shutil.copy(path_to_img, new_path_to_img)
    # soup.select_one('path').text = new_path_to_img
    with open(new_path_to_xml, 'w', encoding='UTF-8') as f:
        f.write(str(soup).replace(path_to_img, new_path_to_img).replace(old_filename_img, new_img_name))
    print(f'Файл - OK! {path_to_img} -> {new_path_to_img}')
    num += 1




