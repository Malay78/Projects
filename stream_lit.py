#Importing Libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Head for the Home Page
st.title("Diamond Price Prediction")

#Image
st.image("streamlit.png", width = 300)
st.title("Case study on Diamond Dataset")
data = sns.load_dataset("diamonds")
st.write("Shape of a dataset", data.shape)
menu = st.sidebar.radio("Menu",["Home", "Prediction price"])

if menu == "Home":
    st.image("diamond.jpg")
    st.header("Tabular Data of a diamond")
    if st.checkbox("Tabular Data"):
        st.table(data.head(50))

    st.header("Statistical Summary of a Dataframe")

    if st.checkbox("Statistical Data"):
        st.table(data.describe())

    if st.header("Correlation graph"):
        fig, ax= plt.subplots(figsize = (5,2.5))
        sns.heatmap(data.corr(), annot =True, cmap = "coolwarm")
        st.pyplot(fig)

#Sketching graphs and Histograms
    st.title("Graphs")
    graph = st.selectbox("Different types of graphs", ["Scatter Plot", "Bar Graph", "Histogram"])
    if graph == "Scatter Plot":
        value = st.slider("Filter data using carat", 0,6)
        data = data.loc[data["carat"]>=value]
        fig, ax=plt.subplots(figsize = (10,5))
        sns.scatterplot(data = data, x= "carat", y= "price", hue="cut")
        st.pyplot(fig)

    if graph == "Bar Graph":
        fig, ax = plt.subplots(figsize = (3.5,2))
        sns.barplot(x="cut", y=data.cut.index, data= data)
        st.pyplot(fig)

    if graph == "Histogram":
        fig,ax=plt.subplots(figsize=(5,3))
        sns.distplot(data.price, kde= True)
        st.pyplot(fig)
#For Price Prediction

if menu == "Prediction price":
    st.title("Prediction price of a diamond")

#importing Scikit Learn Library

    from sklearn.linear_model import LinearRegression
    lr = LinearRegression()
    X=np.array(data["carat"]).reshape(-1,1)
    y=np.array(data["price"]).reshape(-1,1)
    lr.fit(X,y)
    value = st.number_input("Carat", 0.20,5.01, step = 0.15)
    value = np.array(value).reshape(1,-1)
    prediction = lr.predict(value)[0]
    if st.button("price Prediction(in dollars)"):
        st.write(f"{prediction}")
#To run just write streamlit run file_name.py in cmd
        