# Imports
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

# Read shapefile into pandas
def read_data(in_file="../../data/umd_buildings.shp"):
    """
    Read spatial data into geodataframe

    Args:
        in_file (str, optional): path to spatial data. 
        Defaults to "../../data/umd_buildings.shp".

    Returns:
        geodataframe (obj): geopandas geodataframe created from input data
    """    
    return gpd.read_file(in_file)


# Plot data on map
def plot_data(geodata, out_file="../../output/umd_buildings_test.png"):
    """
    Generate a map from spatial data and save it to file

    Args:
        geodata (geodataframe): input geodata frame
        
        out_file (str, optional): path to output map. 
        Defaults to "../../output/umd_buildings_test.png".
    """    
    # setup plot using shapefile
    ax = geodata.plot(figsize=(12, 8), alpha=0.5, edgecolor="k")
    # add basemap
    ctx.add_basemap(
        ax, crs=geodata.crs.to_string(), source=ctx.providers.CartoDB.Voyager
    )
    # save map to file
    plt.savefig(out_file)
    
def main(in_file, out_file):
    """Run script
    """
    in_data = read_data(in_file)
    plot_data(geodata=in_data, out_file=out_file)
    
# Runner
if __name__ == "__main__":
    in_file="../../data/umd_buildings.shp"
    out_file="../../output/umd_buildings_test.png"
    main(in_file, out_file)
