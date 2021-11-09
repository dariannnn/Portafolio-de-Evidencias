# -*- encoding: utf-8 -*-

import argparse
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os
import requests
from lxml import html

description = """ Modo de uso:
    MetadatosURL.py -link [ Analiza las imágenes tomadas de una dirección web ]"""

parser = argparse.ArgumentParser(description='Se buscan metadatos en imágenes.',
                                epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-link', metavar='LINK', dest="link", 
                    help="analiza imágenes desde una URL")
params = parser.parse_args()

def scrapingImages(url):
    print("\nObteniendo imagenes de la url:"+ url)
    try:
        response = requests.get(url)  
        parsed_body = html.fromstring(response.text)
        images = parsed_body.xpath('//img/@src')
        print ('Imagenes %s encontradas' % len(images))
        os.system("mkdir Imagenes_Descargadas")
        for image in images:
            if image.startswith("http") == False: 
                download = url + image
            else:
                download = image
            print("Descarga realizada")
            # download images in images directory
            r = requests.get(download)
            f = open('Imagenes_Descargadas/%s' % download.split('/')[-1], 'wb')
            f.write(r.content)
            f.close()
    except Exception as e:
            print(e)
            print ("Error conexion con " + url)
            pass

def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2]
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][1] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
        input()

 
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret
    
def printMeta():
    os.chdir("Imagenes_Descargadas")
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
            print ("[+] Metadata for file: %s " %(name))
            input()
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    file = open(name+'.txt','a')
                    print ("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                    file.write("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                    file.write("\n")
                    file.close()
                print ("\n")
                decode_gps_info(exif)
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)
                    
if __name__ == "__main__":
        if params.link != None:
            scrapingImages(params.link)
            printMeta()
        else:
            print("Es necesario ingresar una URL")
