import streamlit as st
view = [100,150,30]
st.write('Youtube view')
view
st.bar_chart(view) 
import pandas as pd
sview= pd.Series(view)
sview