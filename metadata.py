from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_image_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                metadata = {}
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    metadata[tag_name] = value
                    
                
                # Доступ к размеру изображения
                width, height = img.size
                metadata['ImageWidth'] = width
                metadata['ImageHeight'] = height
                
                # Извлечение GPS-данных
                if 'GPSInfo' in metadata:
                    gps_info = {}
                    for key in metadata['GPSInfo'].keys():
                        tag_name = GPSTAGS.get(key, key)
                        gps_info[tag_name] = metadata['GPSInfo'][key]

                    # Широта
                    if 'GPSLatitude' in gps_info and 'GPSLatitudeRef' in gps_info:
                        latitude = gps_info['GPSLatitude']
                        latitude_ref = gps_info['GPSLatitudeRef']
                        try:
                            metadata['Latitude'] = (latitude[0][0] / latitude[0][1]) + (latitude[1][0] / (latitude[1][1] * 60)) + (latitude[2][0] / (latitude[2][1] * 3600))
                            if latitude_ref == 'S':
                                metadata['Latitude'] *= -1
                        except Exception as e:
                            print(f"Ошибка при извлечении широты: {e}")

                    # Долгота
                    if 'GPSLongitude' in gps_info and 'GPSLongitudeRef' in gps_info:
                        longitude = gps_info['GPSLongitude']
                        longitude_ref = gps_info['GPSLongitudeRef']
                        try:
                            metadata['Longitude'] = (longitude[0][0] / longitude[0][1]) + (longitude[1][0] / (longitude[1][1] * 60)) + (longitude[2][0] / (longitude[2][1] * 3600))
                            if longitude_ref == 'W':
                                metadata['Longitude'] *= -1
                        except Exception as e:
                            print(f"Ошибка при извлечении долготы: {e}")

                    # Высота
                    if 'GPSAltitude' in gps_info and 'GPSAltitudeRef' in gps_info:
                        altitude = gps_info['GPSAltitude']
                        altitude_ref = gps_info['GPSAltitudeRef']
                        try:
                            metadata['Altitude'] = altitude[0] / altitude[1] if altitude_ref == 0 else -altitude[0] / altitude[1]
                        except Exception as e:
                            print(f"Ошибка при извлечении высоты: {e}")

                # Добавляем данные о местоположении и угле
                dji_meta = get_dji_meta(image_path)
                if dji_meta:
                    metadata['Altitude'] = f"AbsAlt: {dji_meta.get('AbsoluteAltitude', 'N/A')}, RelAlt: {dji_meta.get('RelativeAltitude', 'N/A')}"
                    metadata['Angle'] = f"Roll: {dji_meta.get('GimbalRollDegree', 'N/A')}, Yaw: {dji_meta.get('GimbalYawDegree', 'N/A')}, Pitch: {dji_meta.get('GimbalPitchDegree', 'N/A')}"

                return metadata
    except Exception as e:
        print(f"Ошибка при чтении метаданных изображения: {e}")
        return None

def display_metadata(metadata):
    if metadata:
        print("Метаданные изображения:")
        print(f"Size: {metadata.get('ImageWidth')}x{metadata.get('ImageHeight')} pixels")
        print(f"Time: {metadata.get('DateTimeOriginal')}")
        print(f"Location: {metadata.get('Location', 'N/A')}")
        print(f"Angle: {metadata.get('Angle', 'N/A')}")

# Код для get_dji_meta, который ты предоставил
def get_dji_meta(image_path):
    djimeta=["AbsoluteAltitude","RelativeAltitude","GimbalRollDegree","GimbalYawDegree",\
         "GimbalPitchDegree","FlightRollDegree","FlightYawDegree","FlightPitchDegree"]
    fd = open(image_path,'rb')
    d= fd.read()
    xmp_start = d.find(b'<x:xmpmeta')
    xmp_end = d.find(b'</x:xmpmeta')
    xmp_b = d[xmp_start:xmp_end+12]
    xmp_str = xmp_b.decode()
    fd.close()
    xmp_dict={}
    for m in djimeta:
        istart = xmp_str.find(m)
        ss=xmp_str[istart:istart+len(m)+10]
        val = float(ss.split('"')[1])
        xmp_dict.update({m : val})
    return xmp_dict

image_path = r'C:\Users\iskha\Downloads\100_0140 (1)\100_0140\DJI_0001.JPG'  # Измененный путь к файлу
metadata = get_image_metadata(image_path)
display_metadata(metadata)
