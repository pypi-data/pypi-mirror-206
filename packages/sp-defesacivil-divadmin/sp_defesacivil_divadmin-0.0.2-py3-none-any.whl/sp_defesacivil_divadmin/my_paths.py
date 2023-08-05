"""
Pastas
abr.23
"""


from pathlib import Path


project_path = Path(__file__).parents[1]
module_path = Path(__file__).parents[0]

# Data
data_path = module_path / 'data'
data_path.mkdir(exist_ok=True)

# Input
input_path = data_path / 'input'
input_path.mkdir(exist_ok=True)

input_path_shp = input_path / 'shp'
input_path_shp.mkdir(exist_ok=True)

# Output
output_path = data_path / 'output'
output_path.mkdir(exist_ok=True)

output_path_gpkg = output_path / 'gpkg'
output_path_gpkg.mkdir(exist_ok=True)

output_path_tabs = output_path / 'tabs'
output_path_tabs.mkdir(exist_ok=True)

output_path_maps = output_path / 'maps'
output_path_maps.mkdir(exist_ok=True)

output_path_geo = output_path / 'geo'
output_path_geo.mkdir(exist_ok=True)

if __name__ == '__main__':
    print(project_path)
    print(module_path)
