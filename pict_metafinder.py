#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import argparse
from PIL import Image
from PIL.ExifTags import TAGS


def getMetaData(imgname, out):
    """
    функция ниже получает на вход имя файла(картинки) и имя файла(для вывода информации)
    :param imgname: имя файла(картинки)
    :param out: имя файла(для вывода информации)
    :return:
    """
    try:
        metaData = {}
        imgFile = Image.open(imgname)
        print("Getting meta data...")
        info = imgFile._getexif()

        if info:
            print("Found meta data!")
            # перебор данных в словаре с метаданными
            for (tag, value) in info.items():
                tagname = TAGS.get(tag, tag)
                metaData[tagname] = value
                if not out:
                    print(tagname, value)
            # если указано имя файла то выводим в файл
        if out:
            print("Outputting to file...")
            with open(out, 'w') as f:
                for (tagname, value) in metaData.items():
                    f.write(str(tagname) + "\t" + str(value) + "\n")
        # если произошла ошибка выводим сообщение о ней
    except:
        print("Failed")


# функция main(). Парсим в ней аргументы командной строки.

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("img", help="name of img file.")
    parser.add_argument("-o", "--output", help="dump data out to file")
    args = parser.parse_args()
    if args.img:
        getMetaData(args.img, args.output)
    else:
        print(parser.usage)


# точка входа
if __name__ == '__main__':
    main()
