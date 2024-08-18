import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import altair as alt
import leafmap.colormaps as cm
import fiona
import rasterio
import rasterio.mask

st.set_page_config(layout="wide")

prueba = 'https://github.com/giswqs/streamlit-multipage-template'

link_aguila = 'https://drive.google.com/uc?export=download&id=12q79nwRfPl0UEtOq7pitk7IjKF1ZJY-J'
link_coyote = 'https://drive.google.com/uc?export=download&id=1KvJ_iJ4lH2fX83H-r1_0xBY7Yn68etST'
link_jabali = 'https://drive.google.com/uc?export=download&id=1PfleAgGZh1BDabvtgGXFUJmbVKijB5jb'
link_lince = 'https://drive.google.com/uc?export=download&id=1LngUNcoF8w5uMpqPuNJh-U8O1x7ofnBw'
link_oso = 'https://drive.google.com/uc?export=download&id=1JeYQbHN4qGdo14Is8nvorhEkH-oLRhIF'
link_puma = 'https://drive.google.com/uc?export=download&id=1dSzEM5w7frHnL8fQvbJ25XmXo4HxHEmQ'
link_tortuga = 'https://drive.google.com/uc?export=download&id=1c-tSGUVMYOfy1YRXxvJRbshvb71d2FIl'
link_venado = 'https://drive.google.com/uc?export=download&id=1zi9ZBn1_vX3Q44y55Xn0dS2dgr6Q0Duf'

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: prueba
"""
markdown2 = "Esta aplicación muestra los puntos de presencia de las especies animales más importantes del estado de Nuevo León. Adicionalmente, muestras estadísticas de cada municipio donde hay puntos de presencia de las especies.  "

multi = '''La información de la distribución potencial fue obtenida mediante el uso de MAXENT haciendo uso de variables bioclimáticas. Los resultados fueron filtrados mediante el 10 percentil.'''
multi2 = '''Los datos de presencia de las especies fueron obtenidos de la pagina GBIF. Posteriormente, los archivos Darwing core fueron limpiados y convertidos en formato shapefile.'''
options = list(
    ['Zorra Gris', 'Tortuga del Desierto', 'Águila Real', 'Venado Cola Blanca', 'Puma', 'Coyote', 'Jabalí', 'Oso Negro',
     'Lince'])
index = options.index('Zorra Gris')

grafica_zorro = pd.DataFrame({"Puntos de presencia": ['México: 5817', 'Nuevo León: 118'], "value": [5817, 118]})
grafica_tortuga = pd.DataFrame({"Puntos de presencia": ['México: 1063', 'Nuevo León: 343'], "value": [1063, 343]})
grafica_aguila = pd.DataFrame({"Puntos de presencia": ['México: 2333', 'Nuevo León: 241'], "value": [2333, 241]})
grafica_venado = pd.DataFrame({"Puntos de presencia": ['México: 8864', 'Nuevo León: 333'], "value": [8864, 333]})
grafica_puma = pd.DataFrame({"Puntos de presencia": ['México: 1450', 'Nuevo León: 60'], "value": [1450, 60]})
grafica_coyote = pd.DataFrame({"Puntos de presencia": ['México: 4503', 'Nuevo León: 179'], "value": [4503, 179]})
grafica_jabali = pd.DataFrame({"Puntos de presencia": ['México: 117', 'Nuevo León: 11'], "value": [117, 11]})
grafica_oso = pd.DataFrame({"Puntos de presencia": ['México: 861', 'Nuevo León: 273'], "value": [861, 273]})
grafica_lince = pd.DataFrame({"Puntos de presencia": ['México: 2131', 'Nuevo León: 58'], "value": [2131, 58]})

c = alt.Chart(grafica_zorro).mark_arc().encode(theta="value", color="Puntos de presencia")
c2 = alt.Chart(grafica_tortuga).mark_arc().encode(theta="value", color="Puntos de presencia")
c3 = alt.Chart(grafica_aguila).mark_arc().encode(theta="value", color="Puntos de presencia")
c4 = alt.Chart(grafica_venado).mark_arc().encode(theta="value", color="Puntos de presencia")
c5 = alt.Chart(grafica_puma).mark_arc().encode(theta="value", color="Puntos de presencia")
c6 = alt.Chart(grafica_coyote).mark_arc().encode(theta="value", color="Puntos de presencia")
c7 = alt.Chart(grafica_jabali).mark_arc().encode(theta="value", color="Puntos de presencia")
c8 = alt.Chart(grafica_oso).mark_arc().encode(theta="value", color="Puntos de presencia")
c9 = alt.Chart(grafica_lince).mark_arc().encode(theta="value", color="Puntos de presencia")
# st.sidebar.title("About")
st.sidebar.image("Imagenes/desarrolloreg.png")
st.sidebar.info(markdown2)
# st.sidebar.altair_chart(c,use_container_width=True)

enlace1 = ''

st.title("Fauna mas importante de Nuevo León")

# st.se

i = 1

with st.expander("See source code"):
    selec = st.sidebar.selectbox("Animales mas importantes del matorral", options, index)
    print(selec + "lo seleccionado fue")
    cities = 'Matorral/Zorra.csv'
    cities2 = 'Matorral/Tortuga.csv'
    cities3 = 'Matorral/Aguila.csv'
    cities4 = 'Matorral/Venado.csv'
    cities5 = 'Matorral/Puma.csv'
    cities6 = 'Matorral/Coyote.csv'
    cities7 = 'Matorral/Jabali.csv'
    cities8 = 'Matorral/Oso.csv'
    cities9 = 'Matorral/Lince.csv'
    opcion = selec
    if opcion == 'Zorra Gris':
        seleccionado = cities
        logo = 'Imagenes/Zorra.jpg'
        grafico = c
        print(seleccionado)
        raster = 'Rasters/Distribucion_Aguila.tif'
        enlace = link_venado

    elif opcion == 'Tortuga del Desierto':
        seleccionado = cities2
        logo = 'Imagenes/Tortuga.jpg'
        grafico = c2
        print(seleccionado)
        raster = 'Recortes/Recorte_tortuga.tif'
        enlace = link_tortuga

    elif opcion == 'Águila Real':
        seleccionado = cities3
        logo = 'Imagenes/Aguila.jpg'
        grafico = c3
        raster = 'Recortes/Recorte_aguila.tif'
        enlace = link_aguila

    elif opcion == 'Venado Cola Blanca':
        seleccionado = cities4
        logo = 'Imagenes/Venado.jpg'
        grafico = c4
        raster = 'Recortes/Recorte_venado.tif'
        enlace = link_venado
    elif opcion == 'Puma':
        seleccionado = cities5
        logo = 'Imagenes/Puma.jpg'
        grafico = c5
        raster = 'Recortes/Recorte_puma.tif'
        enlace = link_puma
    elif opcion == 'Coyote':
        seleccionado = cities6
        logo = 'Imagenes/Coyote.jpg'
        grafico = c6
        raster = 'Recortes/Recorte_coyote.tif'
        enlace = link_coyote
    elif opcion == 'Jabalí':
        seleccionado = cities7
        logo = 'Imagenes/Jabali.jpg'
        grafico = c7
        raster = 'Recortes/Recorte_jabali.tif'
        enlace = link_jabali
    elif opcion == 'Oso Negro':
        seleccionado = cities8
        logo = 'Imagenes/Oso.png'
        grafico = c8
        raster = 'Recortes/Recorte_oso.tif'
        enlace = link_oso
    elif opcion == 'Lince':
        seleccionado = cities9
        logo = 'Imagenes/Lince.jpg'
        grafico = c9
        raster = 'Recortes/Recorte_lince.tif'
        enlace = link_lince
    st.sidebar.image(logo)
    st.sidebar.altair_chart(grafico, use_container_width=True)

    m = leafmap.Map(center=[25.67, -100.31847], zoom=7, minimap_control=True)
    m2 = leafmap.Map(google_map="HYBRID", center=[25.67, -100.31847], zoom=7, minimap_control=True)

    regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'
    regions2 = 'Nl.geojson'

    m.add_geojson(regions2, layer_name='Estado de Nuevo León')
    m2.add_geojson(regions2, layer_name='Estado de Nuevo León')

    # m.add_raster(raster,colormap="terrain",layer_name='DEM')

    m.add_points_from_xy(
        seleccionado,
        x="x",
        y="y",
        color_column='Estatus',
        icon_names=['Presencia'],
        spin=True,
        add_legend=True,

    )
    m2.add_raster(raster, colormap="BuGn", layer_name="Distribución")

st.markdown(multi2)
m.to_streamlit(height=800)
st.title("***Distribución potencial de*** " + selec)
st.markdown(multi)
st.markdown("Si deseas descargar la información presiona en el siguiente enlace: [Descarga](%s)" % enlace)
m2.to_streamlit(height=800)

# streamlit run .\Pages\split_map.py --server.port 8888

#streamlit run Homepage.py --server.port 8888