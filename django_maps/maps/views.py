from django.shortcuts import render
from django.http import HttpResponse
import folium
from map import merge_and_validate
import os
import pandas as pd
import geopandas as gpd


# Create your views here.
def index(request):
    return render(request, 'maps/index.html')


def karnataka(request):

    # Shape file - to be used by map
    shape_path = os.path.join('state_maps','Karnataka', 'AC_Boundary_SHP_Karnataka', 'AC_Boundary.shp')
    state_shape = gpd.read_file(shape_path)
    state_shape['Constituency_No'] = state_shape['AC_CODE'].astype('int64')

    data_path = os.path.join('state_data', 'Karnataka',"Number of Women Candidates in the Karnataka State Assembly Elections 2023.csv")
    df_women = pd.read_csv(data_path)

    df_merged = merge_and_validate(
    "Python Shape Viz", 
    state_shape,
    df_women, 
    merge_on_cols=['Constituency_No'], 
    strict_matching=True, 
    validate="1:1"
    )

    m = folium.Map(location=[14, 77], zoom_start = 5.5, tiles='cartodbpositron')
    folium.Choropleth(df_merged,
                    data=df_merged,
                    key_on = 'feature.properties.AC_NAME_KN',
                    columns=['AC_NAME_KN', 'Total_women'],
                    fill_color= 'RdPu',
                    line_weight=0.4,
                    line_opacity=0.2,
                    legend_name="Women Candidate Count"
                    ).add_to(m)
  
    m = m._repr_html_()

    context = {
        'm':m
    }
    return render(request, 'maps/maps.html', context)


def world(request):

    m = folium.Map()
  
    m = m._repr_html_()

    context = {
        'm':m
    }
    return render(request, 'maps/world.html', context)

def india(request):

    m = folium.Map(
        location=[21.20606352190694, 79.07278820936767],
        zoom_start=5)
    
    folium.Marker(location=[28.95, 77.1],
                  tooltip='click for more', popup='Ashoka University').add_to(m)
    
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)

    folium.LayerControl().add_to(m)
    m = m._repr_html_()

    context = {
        'm':m
    }
    return render(request, 'maps/india.html', context)