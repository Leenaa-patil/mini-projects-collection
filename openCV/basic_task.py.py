
import cv2

image= input("enter location of image:")
print("loading the image firstly..")
img_location=cv2.imread(image)

features=("show image", "save image")
if img_location is not None:
    print("img loaded")
    grayscaled_img=cv2.cvtColor(img_location, cv2.COLOR_BGR2GRAY)
    while True:
        userip= input("what you want to do- show image or save image?")
        if userip in features:
            print("processing you request..")
            if userip=="show image": 
                print("displaying the image..")
                try: 
                    cv2.imshow("img", grayscaled_img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                except:
                    print("unable to display image") 
            
            elif userip=="save image":
                print("saving image copy..")
                save_location=input("enter location to save copy of image:")

                try:
                    outputsave_location=cv2.imwrite(save_location, grayscaled_img)
                    print("image saved")
                    break
                    
                except:
                    print("unable to save")
          
          
                    
else:
 print("image not loaded")