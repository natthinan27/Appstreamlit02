import streamlit as st
st.image('./pic/01.jpg')
col1,col2=st.colums(2)
with col1 :
    st.header('ณัฐินันท์ เข็มทอง')
with col2 :
    st.subheader('สาขาวิทยาการข้อมูล')
    st.text('คณะวิทยาศาสตร์และเทคโนโลยี')

st.header('Natthinan Khemthong')