import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import altair as alt
import leafmap.colormaps as cm
import fiona
import rasterio
import rasterio.mask


enlace2 = 'https://drive.google.com/uc?export=download&id=1VJhV7WkLFLDpex9irLMctGC98fFEalF6'
st.set_page_config(layout="wide")
st.title("Información forestal de Nuevo León")

multi = '''La información de la cubierta forestal fue obtenida a partir de un filtrado de la información de la Agencia Espacial Europea la cual, tiene información de 10 metros de resolución espacial.'''

m = leafmap.Map(google_map="HYBRID",center=[25.67, -100.31847], zoom=7, minimap_control=True)
m2 = leafmap.Map(google_map="HYBRID", center=[25.67, -100.31847], zoom=7, minimap_control=True)
region = 'Capas/Nl.geojson'

raster = 'Forestal/Zonas_arboles.tif'
m.add_raster(raster,colormap="Greens",layer_name='Cubierta Forestal')
m.add_geojson(region,layer_name='Estado de Nuevo León')
st.markdown(multi)
st.markdown("Si deseas descargar la información presiona en el siguiente enlace: [Descarga](%s)" % enlace2)
m.to_streamlit(height=800)