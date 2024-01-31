import streamlit as st
import joblib
import pandas as pd
from ipynb import text_process
import os
def main1():
    html_temp = """
            <div style="background-color:lightblue;padding:16px">
            <h2 style="color:black";text-align:center>Fake Review Detection</h2>
            </div>
            """
    st.markdown(html_temp,unsafe_allow_html=True)
    user_input=[]
    pred_model=joblib.load('model')
    p1 = st.text_input("Test your review here:")
    p1=p1.strip()
    user_input.append(p1)

    #u_dataframe = pd.DataFrame(user_input)

    if st.button('PREDICT'):
        model_path = os.path.abspath('best_model.sav')
        if os.path.exists(model_path):
            pred_model = joblib.load(model_path)
                # Rest of your code...
        else:
            print(f"Model file '{model_path}' not found.")
        res = pred_model.predict(user_input )
        if res[0]=="OR":
            st.write("""The Review Is ORIGINAL""")
        else:
            st.write("""The Review is Computer Generated""")

if __name__=='__main__':
    main1()   
    