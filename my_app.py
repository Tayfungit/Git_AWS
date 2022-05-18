import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("This is a title")
st.text("This is some text")
st.markdown("Streamlit is ***really cool*** :+1:")
st.header("This is a header")

# success info error
st.success("This is a success message!")
st.info("This is a purely info message")
st.error("But this is a serious error")

st.help(range(1, 100))  # Herhangi bir komut hakkinda yardim almak icin.

st.write("Hello, world!")
st.write('Hello, *World!* :sunglasses:')

# image!
img = Image.open("images.jpeg")
st.image(img, caption="cattie", width=300)

# st.help("st.image")
st.image(img)

# # Video
# my_video = open("ml.mov", "rb")
# st.video(my_video)
# st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")

# checkbox
cbox = st.checkbox("Hide and seek")
if cbox:
    st.write("Hide")
else:
    st.write("Seek")

# Radio button
st.radio("Select a color", ("blue", "orange", "yellow"))

status = st.radio("Select a color", ("Blue", "Red", "Yellow"))
st.write("Sizin favori renginiz {}".format(status))

#Button
st.button("Button")
if st.button("Press me"):
    st.success("Analyse result are OK")
# else :
#     st.success("Analyse result are NOT")

# Select box
occupation = st.selectbox("My occupation", ["Programmer", "DataScientist", "Doctor"])
st.write("You selected this option:", occupation)

# Multi selectbox
multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])

# Slider
option1 = st.slider("Select a number", min_value=50, max_value=300, value=100, step=5)
option2 = st.slider("Select a number", 50, 100, step=1)
option1+option2

option3 = st.slider("Select a number", min_value=5, max_value=70, value=30, step=5)
option4 = st.slider("Select a number", min_value=0.2, max_value=30.2, value=5.2, step=0.2)
result=option3*option4
result

# Text_input
name = st.text_input("Enter your name", placeholder="Your name here")
if st.button("Submit"):
    st.write("Hello {}".format(name.title()))

#st.snow()
#st.balloons()

# [theme]
# primaryColor="#F63366"
# backgroundColor="#FFFFFF"
# secondaryBackgroundColor="#F0F2F6"
# textColor="#262730"
# font="sans serif"

# Code 
st.code("import pandas as pd" )
st.code("import pandas as pd\nimport numpy as np")

with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
    df

# Date input
import datetime

today = st.date_input("Today is", datetime.datetime.now())
d = st.date_input("When is your Birthday", datetime.date(2022,4,28))

# st.help(st.date_input)

# Time input
the_time = st.time_input("The time is ", datetime.time(12,00))
the_time_now = st.time_input("The time is now")

# Sidebar 
st.sidebar.title("This is a left title")  # Hersey soldan secip sagdan sergilemek üzerine dizayn edilir.
st.title("This is a middle title")

#sidebar
st.sidebar.title("Sidebar Title")
a=st.sidebar.slider("input1", 0,5,2,1)
x=st.sidebar.slider("input2")
st.success(a*x)

# Dataframe
# 3 methods: Write - Table - Dataframe
df=pd.read_csv("Advertising.csv", nrows=100)
st.table(df.head())       #Static tablo yapar.
st.write(df.head())       #Dinamic tablo yapar.
st.dataframe(df.head())   #Dinamic tablo yapar.
df     # BÖylede dinamic tüm datayi verir. Head yapilmiyor.

# Using trained model
import pickle
from sklearn.linear_model import LinearRegression

filename = "finalized_model.sav"
model = pickle.load(open(filename, "rb"))
pred = model.predict([[170, 35, 50]])
st.write("prediction :", pred)
st.write("prediction :", pred[0])



#örn

a= st.sidebar.slider("a",0,50,2,1)
b=st.sidebar.slider("b",50,22,12)
c=st.sidebar.slider("c",50,25,18)   #a,b,c yerine TV, Radio, Newspaper yazilabilir.
if st.button("Predict"):
    pred = model.predict([[a,b,c]])
    st.write("prediction", pred[0])  

d = st.sidebar.number_input("TV:",value=230, step=10)
e = st.sidebar.number_input("radio:",value=37, step=10)
f = st.sidebar.number_input("newspaper:",value=69, step=10)
if st.button("Predict1"): 
    pred = model.predict([[d,e,f]])
    st.write(pred)

# Renkli Baslik
html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Single Customer </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)


# Sergileme

tenure=st.sidebar.slider("Number of months the customer has stayed with the company (tenure)", 1, 72, step=1)
MonthlyCharges=st.sidebar.slider("The amount charged to the customer monthly", 0,100, step=5)
TotalCharges=st.sidebar.slider("The total amount charged to the customer", 0,5000, step=10)
Contract=st.sidebar.selectbox("The contract term of the customer", ('Month-to-month', 'One year', 'Two year'))
OnlineSecurity=st.sidebar.selectbox("Whether the customer has online security or not", ('No', 'Yes', 'No internet service'))
InternetService=st.sidebar.selectbox("Customer’s internet service provider", ('DSL', 'Fiber optic', 'No'))
TechSupport=st.sidebar.selectbox("Whether the customer has tech support or not", ('No', 'Yes', 'No internet service'))
def single_customer():
    my_dict = {"tenure" :tenure,
        "OnlineSecurity":OnlineSecurity,
        "Contract": Contract,
        "TotalCharges": TotalCharges ,
        "InternetService": InternetService,
        "TechSupport": TechSupport,
        "MonthlyCharges":MonthlyCharges}
    df_sample = pd.DataFrame.from_dict([my_dict])
    return df_sample
df = single_customer()
st.table(df)






