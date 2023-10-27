import folium
import os
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd




def merge_and_validate(merge_name, org_df, supplement_df, left_on = [], right_on = [], merge_on_cols = [], strict_matching = True, validate = 'm:1'): 
    # Set merge keys 
    if(not(left_on) and not(right_on)):
        left_on = merge_on_cols
        right_on = merge_on_cols

    output_df = org_df.merge(
        supplement_df,
        how = 'left',
        right_on = right_on,
        left_on= left_on,
        indicator = '_match',
        validate = validate
    )

    # Optional check to see if all rows were matched
    if(strict_matching and output_df['_match'].value_counts()['both'] != len(org_df)):
        print(f"[ERROR] merge_and_validate failed for {merge_name}")
        no_match_df = output_df[output_df['_match'] != 'both']
        print(no_match_df)

    output_df = output_df.drop('_match', axis = 'columns')
    return output_df




# Plotting function
def plot_map(df_merged, tar_column, title, save_html=False):
    df_merged = df_merged.dropna()

    ax = df_merged.boundary.plot(edgecolor='black', linewidth=0.2, figsize=(10,5))

    df_merged.plot(
        ax=ax, 
        column= tar_column, 
        legend=True, 
        cmap='RdBu', 
        legend_kwds = {
        'shrink': 0.3,
        'orientation': 'horizontal',
        'format': '%.1f%%'
        }
    )

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    edges = ['left', 'right', 'top', 'bottom']

    for edge in edges:
        ax.spines[edge].set_visible(False)

    ax.set_title(title)
    plt.show()
    if save_html:
        plt.save(f"{title}.html", format='html')


'''

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


tar_column="Total_women"
title = "Number of Women Candidates in the Karnataka State Assembly Elections 2023"

#plot_map(df_merged, tar_column, title, save_html=False)

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
m.save('map.html')

'''