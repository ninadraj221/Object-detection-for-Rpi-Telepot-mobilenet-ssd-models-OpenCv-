Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import telepot
import time
import os
from picamera import PiCamera
import cv2
import matplotlib.pyplot as plt

path=os.getenv("HOME")
print(path)
#Handling message from telegram

def handleMessage(msg):
    id = msg['chat']['id']
    command = msg['text']
    print ('Command ' + command + ' from chat id' + str(id))
    if (command == '/photo'):
        print ("Taking picture…")

        #Initiliazing Camera

        camera = PiCamera()
        camera.start_preview()
        camera.capture(path + '/pic.jpg')
        time.sleep(2)
        camera.stop_preview()
        camera.close()

        #Object Detection

        config_file = r'/home/pi/Downloads/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
        frozen_model =  r'/home/pi/Downloads/frozen_inference_graph.pb'
        model = cv2.dnn_DetectionModel(frozen_model, config_file)
        classLabels = []
        file_name = r'/home/pi/Downloads/Labels.txt'
        with open(file_name, 'rt') as fpt:
            classLabels = fpt.read().rstrip('\n').split('\n')
        model.setInputSize(320, 320)
        model.setInputScale(1.0/127.5)
        model.setInputMean((127.5,127.5,127.5))
        model.setInputSwapRB(True)
        img = cv2.imread(r'/home/pi/pic.jpg')
        #plt.imshow(img)
        #plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        #plt.show()
        ClassIndex, confidece, bbox = model.detect(img,confThreshold=0.6)
        print(ClassIndex)
        font_scale = 3
        font = cv2.FONT_HERSHEY_PLAIN
        for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidece.flatten(), bbox):
            cv2.rectangle(img,boxes,(255, 0,  0), 2)
            cv2.putText(img,classLabels[ClassInd-1],(boxes[0]+10,boxes[1]+40), font, fontScale=font_scale,color=(0, 255, 0), thickness =3)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        #plt.show()
        #resize = cv2.resize(img,(1000,600))
        cv2.imwrite(r'/home/pi/Output.jpg',img)
        #fig = plt.figure()
        #fig.savefig(r'C:\Users\Ninad\Desktop\SAVED.jpg')

        #Sending Picture
        
        bot.sendPhoto(id, open(path + '/Output.jpg', 'rb'))
    else:
        bot.sendMessage(id, "Command not found..")
bot = telepot.Bot('1658601077:AAFXlb192Qjy7KLqsnT4rJAUaS7mK33p-No')
bot.message_loop(handleMessage)
print ("Listening to bot messages….")
while 1:
    time.sleep(10)
