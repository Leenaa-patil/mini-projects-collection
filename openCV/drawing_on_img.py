# get file location from user, give multiple options - 1, line, 2 circle, 3 rectangle , 4 text
# get x1,y1 points and ask whether to save img or not, for all shapes
 
 
import cv2
imgpath=input("enter location of the image:")
color=(0,255,200)
thickness=3

try:
    image=cv2.imread(imgpath)
    if image is None:
        print("image not found")
    else:
        print("image found!")

        operations = ["line","circle","rectangle","text"]
        print("Available operations:", operations)

        userinput=input("what operations you want to perform?")
        
        for userinput in operations:
            if userinput=="line":
                try:
                    print("to draw a line , we need coordinates")
                    pt1=int(input("enter x1 coordinate:")),int(input("enter Y1 coordinate:"))
                    pt2=int(input("enter X2 coordinate:")),int(input("enter Y2 coordinate:"))
                    cv2.line(image, pt1, pt2, color, thickness)
                    
                except:
                    print("invalid coordinates")

            elif userinput=="circle":
                try:
                    print("to draw a circle we need center coordinates and radius")
                    center=int(input("enter x coordinates=")), int(input("enter y coordinates="))
                    radius=int(input("enter radius="))
                    cv2.circle(image, center, radius, color, thickness)
                    
                except:
                    print("invalid coordinates or radius")

            elif userinput=="rectangle":
                try:
                    print("to draw a rectangle we need two opposite corner coordinates")
                    pt1=int(input("top left= enter x1 coordinate:")),int(input("enter Y1 coordinate:"))
                    pt2=int(input("bottom right= enter X2 coordinate:")),int(input("enter Y2 coordinate:"))
                    cv2.rectangle(image, pt1, pt2, color, thickness)
                    
                except:
                    print("invalid coordinates")   

            elif userinput=="text":
                try:
                    print("you want to add text over image.")
                    text=input("enter text:")
                    org=int(input("enter x coordinate for text:")), int(input("enter y coordinate for text:"))
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    fontscale=1.2
                    cv2.putText(image, text, org, font, fontscale, color, thickness)
                   
                except:
                    print("invalid coordinates")


            else:
                print("invalid operation! select a valid one")               
            
            cv2.imshow("Result", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
             
            save = input("Do you want to save the image? (yes/no): ")

            if save == "yes":
              save_path = input("Enter save location: ")
              cv2.imwrite(save_path, image)
              print("Image saved successfully!") 
             

except:
    print("invalid image location!")
                  