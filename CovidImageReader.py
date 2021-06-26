from PIL import Image
import pytesseract
import json

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#Load Image
img = Image.open('C:\\Users\\TK_\\Desktop\\test1.jpeg')
image_name = str(img.filename)

#Get text from image
text = pytesseract.image_to_string(img)
print(text)

#Preprocessing on text
text = text.replace("\n"," ")
text = text.replace("\r"," ")
text = text.replace("!","")
text = text.replace(",","")
text = text.replace(".","")
text = text.replace(":","")
text = text.replace("*","")
text = text.lower()
print(text)

#Lists of keywords
list_of_cities = 'mumbai nagpur patna banglore delhi noida haryana indore jaipur gurgaon dwarka palwal faridabad vadodra gujrat india'
list_of_requirements = 'oxygen bed beds ventilator ventilators fabiflu tocilizumbag "400 mg" plasma remdesivir remedesivir favipiravir'
list_of_availability = 'available required requirement availability need suppliers verified'



#Sets of lists
phrase_set = set(text.split())
list_of_locations_set = set(list_of_cities.split())
list_of_requirements_set = set(list_of_requirements.split())
list_of_availability_set = set(list_of_availability.split())


#Finding required data
location = phrase_set.intersection(list_of_locations_set)
print("Location: ",location)
location_json = str(location)

reqd = phrase_set.intersection(list_of_requirements_set)
print("Requirements: ",reqd)
reqd_json = str(reqd)

avail = phrase_set.intersection(list_of_availability_set)
print("Situation: ", avail)
avail_json = str(avail)

if(location_json!='set()' and avail_json!='set()' and reqd_json= 'set()'):
    # function to add to JSON 
    def write_json(data, filename='G:\Codes\C C++ Codes\Python codes\outputOfCheck.json'): 
	    with open(filename,'w') as f: 
		    json.dump(data, f, indent=4) 
	
    
    with open('G:\Codes\C C++ Codes\Python codes\outputOfCheck.json') as json_file: 
	    data = json.load(json_file) 
	
	    temp = data['screenshot_details'] 

	    # python object to be appended 
	    y = {"File Name": image_name,"Location": location_json, "Requirements": reqd_json, "Situation": avail_json}

	    # appending data to emp_details 
	    temp.append(y) 
	
    write_json(data) 