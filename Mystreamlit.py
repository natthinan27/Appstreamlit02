import streamlit as st
st.image('./pic/01.jpg')
col1,col2=st.columns(2)
with col1 :
    st.header('ณัฐินันท์ เข็มทอง')
with col2 :
    st.subheader('สาขาวิทยาการข้อมูล')
    st.text('คณะวิทยาศาสตร์และเทคโนโลยี')
html_1 = """
<div style="background-color:#AEC3AE;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd
dt=pd.read_csv('./data/iris.csv')
st.write(dt.head(10))

dt1 = dt['petal.length'].sum()
dt2 = dt['petal.width'].sum()
dt3 = dt['sepal.length'].sum()
dt4 = dt['sepal.width'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])

if st.button("show bar chart"):
    st.bar_chart(dx2)
    st.button("Not show bar chart")
else :
    st.button("Not show bar chart") 

html_2 = """
<div style="background-color:#D2E0FB;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายคลาสดอกไม้</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")   
ptlen = st.slider("กรุณาเลือกข้อมูล petal.length",0,10)
ptwd = st.slider("กรุณาเลือกข้อมูล petal.width",0,10)

splen = st.number_input("กรุณาเลือกข้อมูล sepal.length")
spwd = st.number_input("กรุณาเลือกข้อมูล sepal.width")

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

if st.button("ทำนายผล"):
   # ทำนาย
   #dt = pd.read_csv("./data/iris.csv") 

   X = dt.drop('variety', axis=1)
   y = dt.variety   

   Knn_model = KNeighborsClassifier(n_neighbors=3)
   Knn_model.fit(X, y)

    #ข้อมูล input สำหรับทดลองจำแนกข้อมูล
   x_input = np.array([[ptlen, ptwd, splen, spwd]])
    # เอา input ไปทดสอบ
   st.write(Knn_model.predict(x_input))
   out=Knn_model.predict(x_input)

   if out[0]=="Setosa":
      st.image("./pic/02.jpg")
      st.header("Setosa")
   elif out[0]=="Versicolor":
      st.image("./pic/03.jpg")
      st.header("Versicolor")
   else:
      st.image("./pic/04.jpg")  
      st.header("Verginiga")
   st.button("ไม่ทำนายผล")
else :
    st.button("ไม่ทำนายผล")