# -*- coding: utf-8 -*-

"""
Author(s): Kris Johnson
Date created: 10/11/2022
Date last modified: 10/12/2022
Python Version: 3
Run time: Dynamic
Description: 
    Takes in a CSV spreadsheet and generates a series of PDF pages,
    one for each record, to be compiled into a report.
    Based on tutorials provided by PyFPDF.
"""

# Import modules
from fpdf import FPDF
import logging
from helpers import csv_tasks

# define methods
def header(pdf):
    """configure page header"""
    # Rendering logo:
    input_logo = "paul-bunyan-logo.jpg"
    pdf.image(input_logo, 10, 8, 33)
    # Setting font: helvetica bold 15
    pdf.set_font("helvetica", "B", 15)
    # Moving cursor to the right:
    pdf.cell(80)
    # Printing title:
    pdf.cell(30, 10, "Beltrami County Road Report", align="C")
    # Performing a line break:
    pdf.ln(50)


def footer(pdf):
    """configure page footer"""
    # Position cursor at 1.5 cm from bottom:
    pdf.set_y(-15)
    # Setting font: helvetica italic 8
    pdf.set_font("helvetica", "I", 8)
    # Printing page number:
    pdf.cell(0, 10, f"Page {pdf.page_no()}/{{nb}}", align="C")


def add_title(pdf, title):
    """Add title to report

    Args:
        title (str): text string to add to report
    """

    # move starting point to middle of the page
    pdf.set_y(100)

    # add text to page
    pdf.cell(
        w=200,
        h=10,
        txt=title,
        align="C",  # center align
        # border=True,  # nice for debugging
    )

    logging.info(f"{title} added to pdf")


def export(pdf, path_to_output_pdf):
    """Generate PDF

    Args:
        path_to_output_pdf (str): path to save the output pdf file
    """
    pdf.output(path_to_output_pdf)
    logging.info(f"pdf exported to {path_to_output_pdf}")


def add_label_text(pdf, label_text):
    """insert label text into page

    Args:
        label_text (str): attribute label
    """
    # add attribute label
    pdf.cell(w=40, h=6, txt=label_text)
    # add new line
    pdf.ln()


def add_data_text(pdf, data_text):
    """insert data text into page

    Args:
        data_text (str): attribute value to insert
    """
    # shift text over to offset from label
    pdf.set_x(20)
    # add data value based on attribute
    pdf.cell(w=40, h=6, txt=data_text)
    # add new line
    pdf.ln(15)


def generate_road_page(pdf, attribute_mapping, row):
    """generate page based on road data

    Args:
        attribute_mapping (dict): column name mappings
        row (dict): row of road data from spreadsheet
    """
    # iterate over attribute mappings dictionary
    for key, value in attribute_mapping.items():
        # add label and data text to page
        pdf.add_label_text(value)
        pdf.add_data_text(row[key])

    # add a new page
    pdf.add_page()

    logging.info("page added")


def main():
    """
    Script runner
    """

    # Define input csv file
    input_csv = "BeltramiCountyRoads_short.csv"

    # Define output pdf file
    output_pdf = "BeltramiRoadReport.pdf"

    # Define log file name as script name, replacing .py with .log
    log_file = __file__.replace(".py", ".log")

    print(log_file)

    # Create and configure logger
    logging.basicConfig(
        filename=log_file,  # Define log file path
        format="%(asctime)s %(message)s",  # Add date/time to log messages
        filemode="w",  # ‘w’ overwrites existing log and ‘a’ appends to existing log
        level=logging.DEBUG,
    )  # Set logger to record debug or higher

    # Add handler to print messages to terminal
    logging.getLogger().addHandler(logging.StreamHandler())

    try:

        # Load csv data a list of of dicts
        road_data = csv_tasks.csv_to_dict(input_csv)
        logging.info("Loaded features from CSV file.")

        # create pdf object from PDF class
        pdf = FPDF(
            orientation="P",  # portrait layout
            unit="mm",  # millimeters
            format="Letter",
        )

        # Add a page
        pdf.add_page()

        # Specify font
        pdf.set_font(family="helvetica", size=16)

        logging.info("PDF started")

        # add title page
        add_title(pdf, "Beltrami Road Report, 2022")
        # add a new page after title page
        pdf.add_page()

        # map spreadsheet column names to comprehensible names
        attribute_mapping = {
            "FULLNAME": "Road Name",
            "CTU": "Location",
            "JURS_DESC": "Jurisdiction",
            "SURF_TYPE": "Surface Type",
            "STATUS": "Status",
        }

        # add roads pages
        for row in road_data:
            generate_road_page(pdf, attribute_mapping=attribute_mapping, row=row)

        # export pdf
        export(pdf, output_pdf)

        # Record successful completion
        logging.info("Script successfully completed!")

    except:

        # Log error message
        logging.exception("Script failed!")


if __name__ == "__main__":
    main()
