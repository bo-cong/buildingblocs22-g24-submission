import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data=pickle.load(file)
    return data

data=load_model()

regressor=data['model']
le_lts=data['le_lts']
le_la=data['le_la']

def show_predict_page():
    st.title('Study app')

    st.write('''### Please enter some info: ''')
    topic1=('Work, Energy and Power','Measurements','Kinematics','Dynamics','Forces','Motion in a circle','Functions',
     'Price Mechanisms and its applications','Market Failure','Graphs and Transformations','Vectors','Central Economic Problem'
)
    la1=('U','S',"E",'D','C','B','A')
    la2=('U','S',"E",'D','C','B','A')
    la3=('U','S',"E",'D','C','B','A')
    top1=st.selectbox("Topic 1",topic1)
    top2=st.selectbox("Topic 2",topic1)
    top3=st.selectbox("Topic 3",topic1)
    la1=st.selectbox("Grade for last assessment/practice for "+ str(top1),la1)
    la2=st.selectbox("Grade for last assessment/practice for "+ str(top2),la2)
    la3=st.selectbox("Grade for last assessment/practice for "+ str(top3),la3)
    ltstudied1=st.slider("I Last Studied "+str(top1)+' ( ) days ago',0,100,3)
    ltstudied2=st.slider("I Last Studied "+str(top2)+' ( ) days ago',0,100,3)
    ltstudied3=st.slider("I Last Studied "+str(top3)+' ( ) days ago',0,100,3)
    ok=st.button('What should I study?')
    if ok:
        X=np.array([[la1,ltstudied1 ]])
        X[:, 0]=le_la.transform(X[:,0])
        X[:, 1]=le_lts.transform(X[:,1])
        X=X.astype(float)
        TA=regressor.predict(X)
        st.subheader(f'You should study: {TA[0]}')

   