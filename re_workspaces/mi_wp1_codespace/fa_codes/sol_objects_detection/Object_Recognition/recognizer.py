# importing the required library  
from imageai.Detection import ObjectDetection  

# instantiating the class  
recognizer = ObjectDetection()  

# defining the paths  
path_model = ".\\re_workspaces\\mi_wp1_codespace\\fa_codes\\sol_objects_detection\\object_recognition\\Models\\yolo-tiny.h5"  
path_input = ".\\re_workspaces\\mi_wp1_codespace\\fa_codes\\sol_objects_detection\\object_recognition\\Input\\images.jpg"  
path_output = ".\\re_workspaces\\mi_wp1_codespace\\fa_codes\\sol_objects_detection\\object_recognition\\Output\\newimage.jpg"

# using the setModelTypeAsTinyYOLOv3() function  
recognizer.setModelTypeAsTinyYOLOv3()  

# setting the path to the pre-trained Model  
recognizer.setModelPath(path_model)  

# loading the model  
recognizer.loadModel()  

# calling the detectObjectsFromImage() function  
recognition = recognizer.detectObjectsFromImage(input_image = path_input, output_image_path = path_output)  

# iterating through the items found in the image  
for eachItem in recognition:  
    print(eachItem["name"] , " : ", eachItem["percentage_probability"])  


#--------------------------------------------------------------------------------------------------------

print('Im good')