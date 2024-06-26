import cv2
import time
camera_id = 0
delay = 1
window_name = 'OpenCV QR Code'
qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)
imageCaptured = False
sOld = ""
while True:
    ret, frame = cap.read()

    if ret:
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
        if ret_qr:
            for s, p in zip(decoded_info, points):
                if s:
                   if s == sOld:
                        color = (0, 0, 255)
                   else:
                        singleFrame = cap.read()
                        print(s)
                        sOld = s 
                        color = (0, 255, 0)    
                        imageCaptured = True
                else:
                    color = (0, 0, 255)
                frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break
    '''if imageCaptured:
        decodedText, points, _ = qcd.detectAndDecode(imageCaptured)
        for s, p in zip(decodedText, points):
            print(s)
            time.sleep(2)
            quit()'''
cv2.destroyWindow(window_name)