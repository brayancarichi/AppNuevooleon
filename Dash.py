import streamlit as st
import plotly.express as px
import pandas as pd
import os 
import warnings


def Display_Map(location_sata):
    fig = px.scatter_mapbox(location_sata,lat='Lat',zoom=4,
                            lon='Long',hover_name='nombres',color_discrete_sequence=["red"],height=900)
    
    fig.update_layout(mapbox_style='open-street-map')
    return fig
    

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Prueba",page_icon=":chart:",layout="wide")

st.title(":chart: Esto es un ejemplo")

st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)

#cFuncion para que el usuario cargue sus propios archivos

uploaded_file = st.file_uploader("Subir archivo CSV")
    
    
if uploaded_file:
    st.header("Distribucion del Cilantro")
    df = pd.read_csv(uploaded_file,
                     usecols=["nombre","x","y"])
    
    df.columns = ["nombres","Long","Lat"]
    px_map = Display_Map(df)
    
    st.plotly_chart(px_map)
    
    
    
    #streamlit run .\Dash.py --server.port 8888