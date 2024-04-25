import cv2
import time
import datetime


def readThing(input1):
    camera_id = 0
    count = 0
    delay = 1
    input2 = "photo_0.png"
    usedArray = []
    window_name = 'OpenCV QR Code'
    qcd = cv2.QRCodeDetector()
    cap = cv2.VideoCapture(camera_id)
    imageCaptured = False
    sOld = ""
    returned = False
    while (returned == False):
        ret, frame = cap.read()
        frame = cv2.imread(input2, cv2.IMREAD_COLOR)
        if ret:
            ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
            if ret_qr:
                for s, p in zip(decoded_info, points):
                    if s:
                       returned = True
                       if(len(usedArray) == 0):
                            if s == sOld:
                                color = (0, 0, 255)
                            else:
                                usedArray.append(s)
                                singleFrame = cap.read()
                                print(s + ", " + str(camera_id) + ", "+ str(datetime.datetime.now() ))
                                #print(moistureValues[int(s)])
                                #print(plantValues[int(s)])
                                sOld = s 
                                color = (0, 255, 0)    
                                imageCaptured = True
                                #name = "photo_" + str(count) + ".png" #+ str(datetime.datetime.now()) + ".png"
                                #cv2.imwrite(name, frame) 
                                count += 1
                                return s;   
                                #time.sleep(5)
                       else:
                           if s in usedArray:
                                color = (0, 0, 255)
                           else:
                                usedArray.append(s)
                                singleFrame = cap.read()
                                print(s + ", " + str(camera_id) + ", "+ str(datetime.datetime.now    ))                                     
                                sOld = s 
                                color = (0, 255, 0)    
                                imageCaptured = True
                                #name = "photo_" + str(count) + ".png" #+ str(datetime.datetime.now()) + ".png"
                                #cv2.imwrite(name, frame) 
                                count += 1
                                return s;   
                                #time.sleep(5)
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

def getPlant(id):
    plantValues = ["plant_1", "plant_2", "plant_3", "plant_4", "plant_5", "plant_6"]
    return plantValues[id]
def getMoisture(id):
    moistureValues = [0.75, 0.65, 0.12, 1.24, 1.23, 1]
    return moistureValues[id]

def getReturn(id, plant, moisture):
    return "Id of: " + id + ", plant type: " + plant + ", moisture requirement of: " + moisture + "."

''' sample code
s = readThing("photo_0.png")

q = (getPlant(int(s)))

g = getMoisture(int(s))

print(getReturn(s, q, str(g)))'''