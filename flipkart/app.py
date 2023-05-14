import streamlit as st
import pickle

#Loading the Model
pickle_in = open("rf_regressor.pkl","rb")
regressor=pickle.load(pickle_in)

def predict(BRAND, PROCESSOR, RAM_TYPE, RAM_Size, Storage, Disk_Type, OS_Type):
    prediction = regressor.predict([[BRAND, PROCESSOR, RAM_TYPE, RAM_Size, Storage, Disk_Type, OS_Type]])
    result = int(prediction)
    return result


#Giving a Title
st.title("Laptop Prediction  App")

#Getting the input data from the user

BRAND = st.selectbox("Brand",('Lenovo', 'ASUS', 'HP', 'DELL', 'RedmiBook', 'realme', 'acer','MSI', 'APPLE', 'Infinix', 'SAMSUNG', 'Ultimus', 'Vaio',
       'GIGABYTE', 'Nokia', 'ALIENWARE'))
#BRAND
if BRAND == "Lenovo":
    BRAND = 7
if BRAND == "ASUS":
    BRAND = 2
if BRAND == "HP":
    BRAND = 5
if BRAND =="DELL":
    BRAND = 3
if BRAND == "RedmiBook":
    BRAND = 10
if BRAND == "realme":
    BRAND = 15
if BRAND == "acer":
    BRAND = 14
if BRAND == "MSI":
    BRAND = 8
if BRAND =="APPLE":
    BRAND = 1
if BRAND == "Infinix":
    BRAND = 6
if BRAND == "SAMSUNG":
    BRAND = 11
if BRAND == "Ultimus":
    BRAND = 12

#Processor
PROCESSOR = st.selectbox("Processor",('Intel', 'AMD', 'Others'))
if PROCESSOR == "Intel":
    PROCESSOR = 1
if PROCESSOR == "AMD":
    PROCESSOR = 0
if PROCESSOR == "Others":
    PROCESSOR = 2

#RAM_TYPE
RAM_TYPE = st.selectbox("RAM_Type",('DDR4', 'DDR5', 'LPDDR4','LPDDR4X', 'LPDDR5', 'LPDDR3'))
if RAM_TYPE == "DDR4":
    RAM_TYPE = 0
if RAM_TYPE == "DDR5":
    RAM_TYPE = 1
if RAM_TYPE == "LPDDR4":
    RAM_TYPE = 3
if RAM_TYPE == "LPDDR4X":
    RAM_TYPE = 4
if RAM_TYPE == "LPDDR5":
    RAM_TYPE = 5
if RAM_TYPE == "LPDDR3":
    RAM_TYPE = 2

RAM_Size = st.selectbox("RAM_Size",( 8, 16,  4,  1, 32))
Storage = st.selectbox("Storage",(32, 128, 256, 512, 1024))

#Disk_Type
Disk_Type = st.selectbox("Disk_Type",('HDD','SSD'))
if Disk_Type == "HDD":
    Disk_Type = 0
if Disk_Type == "SSD":
    Disk_Type = 1

#OS_TYPE
OS_Type = st.selectbox("OS_Type",("Windows","Mac OS","Others"))
if OS_Type == "Windows":
    OS_Type = 2
if OS_Type == "Mac OS":
    OS_Type = 0
if OS_Type == "Others":
    OS_Type = 1

result = ""

button = st.button("Predict")

#if button is pressed:

if button:
    result = predict(BRAND, PROCESSOR, RAM_TYPE, RAM_Size, Storage, Disk_Type, OS_Type)

st.success(f'The Predicted price of the laptop is ${result}')
st.success(f"The app is successfully deployed")


