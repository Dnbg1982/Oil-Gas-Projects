""" Library Import put on the top"""
import seaborn as sns
import matplotlib.pyplot as plt

"""
#
# This file consist of the essential functions to run the program.
# Please dont change any of this functions
#
"""

def plot_3d_visualization(df, title, x_column_name, y_column_name, z_column_name, color_config, shape_config, figsize=(10,10)):
    temp_df = df.copy()
    colors = 'blue'
    markers = 'o'
    if color_config:
        colors = []
        target_data = temp_df[color_config.get('color_column_name')]
        for data in target_data: 
            for target_color, conditions in color_config.get('conditions').items():
                if eval(f'{data}{conditions}'): 
                    colors.append(target_color)
                    break
                else:
                    continue
        temp_df['colors'] = colors

    plt.figure(figsize=figsize)
    axes = plt.axes(projection='3d')
    
    for target_shape, conditions in shape_config.get('conditions').items():
        target_data = temp_df[temp_df[shape_config.get('shape_column_name')] == conditions]
        axes.scatter3D(target_data[x_column_name], target_data[y_column_name], target_data[z_column_name], c=target_data['colors'] if 'colors' in target_data.columns else colors, marker=target_shape)

    axes.set_title(title)
    axes.set_xlabel(x_column_name)
    axes.set_ylabel(y_column_name)
    axes.set_zlabel(z_column_name)
    plt.show()

"""
#
# Teams, please add your code below. 
#
"""

