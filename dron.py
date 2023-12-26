import cv2
# Добавить флаг cv2.CAP_FFMPEG к URL
url = "rtmp://192.168.0.113:1935/live"
# Создать объект VideoCapture с URL
#sample avi "C:/Users/Nuratan/Documents/earth.avi"
cap = cv2.VideoCapture(url)

cv2.namedWindow('frame', cv2.WINDOW_NORMAL)  # cv2.WINDOW_NORMAL позволяет изменять размер окна
cv2.resizeWindow('frame', 800, 600)
# Читать кадры из потока в цикле
while True:
    ret, frame = cap.read()
    if ret!=0:
        # Показать кадр на экране        
        cv2.imshow('frame', frame)
        # Выход из цикла по нажатию клавиши Q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # Вывести сообщение об ошибке
        print("Can't receive frame")
# Освободить ресурсы
cap.release()
cv2.destroyAllWindows()