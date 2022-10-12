# fpdf_example.py
#
# Generate a PDF that includes a map


# Imports

import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import os
from fpdf import FPDF


def read_data(path_to_input_data):
    """Read spatial data into geopandas

    Args:
        path_to_input_data (str): path to input spatial data

    Returns:
        geodataframe [obj]: geopandas geodataframe
    """
    return gpd.read_file(path_to_input_data)


def generate_map(geodata, path_to_output_map):
    """Generate a map from the geodataframe

    Args:
        geodata (geodataframe [obj]): geopandas geodataframe
        path_to_output_map (str): path to save the output map
    """
    # Setup plot using shapefile
    ax = geodata.plot(figsize=(6, 6), alpha=0.5, edgecolor="k")
    # Add basemap
    ctx.add_basemap(
        ax, crs=geodata.crs.to_string(), source=ctx.providers.CartoDB.Voyager
    )
    # Save map to file
    plt.savefig(path_to_output_map)


def start_pdf():
    """Instansiate PDF object and do some basic configuration

    Returns:
        pdf (pdf [obj]): pdf object from FPDF class
    """
    pdf = FPDF(
        orientation="P",  # portrait layout
        unit="mm",  # millimeters
        format="Letter",
    )

    # Add a page
    pdf.add_page()

    # Specify font
    pdf.set_font(family="helvetica", size=16)

    return pdf


def add_title(pdf, title):
    """Add title to report

    Args:
        title (str): text string to add to report
    """

    pdf.cell(
        w=200,
        h=10,
        txt=title,
        align="C",  # center align
        border=True,  # nice for debugging
    )


def add_map(pdf, path_to_output_map):
    """Add map to PDF

    Args:
        pdf (pdf [obj]): pdf object from FPDF class
        path_to_output_map (str): path to map produced by generate_map()
    """

    pdf.image(path_to_output_map, x=10, y=10, w=400)


def export_pdf(pdf, path_to_output_pdf):
    """Generate PDF

    Args:
        pdf (pdf [obj]): pdf object from FPDF class
        path_to_output_pdf (str): path to save the output pdf file
    """
    pdf.output(path_to_output_pdf)


def main():
    """Run that script"""

    # Setup paths
    data_dir = "../data"
    output_dir = "../output"
    # base_dir = ".."  # because we need to climb out of sub directory
    input_data_filename = "umd_buildings.shp"
    output_map_filename = "umd_buildings.png"
    output_pdf_filename = "fpdf2_report_test.pdf"
    path_to_input_data = os.path.join(data_dir, input_data_filename)
    path_to_output_map = os.path.join(output_dir, output_map_filename)
    path_to_output_pdf = os.path.join(output_dir, output_pdf_filename)

    # generate map
    geodata = read_data(path_to_input_data)
    generate_map(geodata=geodata, path_to_output_map=path_to_output_map)

    # generate pdf
    pdf = start_pdf()
    add_title(pdf, title="FPDF2 Test Report")
    add_map(pdf, path_to_output_map=path_to_output_map)
    export_pdf(pdf, path_to_output_pdf=path_to_output_pdf)


if __name__ == "__main__":
    main()
