# Object-detection-for-Rpi-Telepot-mobilenet-ssd-models-OpenCv-
1. Image is captured when we send a command i.e /photo to the telegram bot.
2. Object detection is performed on the captured image.
3. Object detection is performed using mobilenet ssd models and openCv is used to load those models.
4. Then the object detected imgage is sent back to telegram bot.

The raspberry Pi connected to the drone functions as another secondary brain.
It’s main purpose in our project is object detection and receiving commands from the user’s telegram bot. 
As raspberry pi on the drone is on another network whereas the user’s laptop is on another network, in order to communicate with Rpi remote.it application (which is also installed in our Rpi) is used, which enables communication over the internet and using vnc viewer we get GUI of Rpi. It is essential for running python script in the rpi for object detection.
Now the only thing left is to send command to click picture, then Rpi will perform object detection on it.
We have used telepot for building telegram bot API which communicates and sends command to the Rpi. User’s bot I’d is added to the python script so after receiving the specified command i.e  /photo from the user’s telegram bot further functions would be carried out.
Telepots and object detection script has been combined. 
Object detection is a combination of image classification and localization.
For implementation we have used python as a programming language.	
Open Cv is used for loading pre trained tensorflow frozen models.
Algorithm used for image classification is ssd mobile net v3.
SSD Mobile net  (single shot multibox detector)
It divides the whole image into small patches, combining those patches into the most saliant feature of the corresponding image and it asks the classifier i.e mobilenet or yolo etc to classify that image.
Ssd mobile net is most light weight and faster algorithm which goes hand in hand with the Rpi.
Coco dataset which consists of 80 classes is being used.
Deep learning architecture’s pre trained models like mobile net ssd v3 is available on the official page of openCv github link, which is based on tensorflow. We have used openCv to load them. We need to extract the frozen inference graph and configuration file from mobilenet ssd v3 config and weights respectively which in turn are gonna be loaded by open cv as a detection model.
All the 80 coco names need to be copied as there are a total of 80 classes in coco data set as labels, which are essential to check if our detection model has provided us with the correct output or not.
Open Cv and matplotlib are installed.
The python code which loads the detection model (using graph and configuration file), performs object detection on the captured image, cross checks it with the class index’s , adds rectangle boxes and adds the corresponding label based on the class index to the captured image , this script is executed every time after receivin the /photo command from respected user’s telegram bot.
This object detected image is saved in raspberry pi and sent to the user’s telegram bot.
