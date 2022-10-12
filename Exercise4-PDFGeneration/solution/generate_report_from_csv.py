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
from operator import add
from sys import path_hooks
from fpdf import FPDF
import logging
from helpers import csv_tasks

# 
class PDF(FPDF):
    def header(self):
        """ configure page header
        """        
        # Rendering logo:
        self.image("beltrami-county-logo".png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Beltrami County Road Report", align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        """ configure page footer
        """    
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


def start_pdf(self):
    """Instansiate PDF object and do some basic configuration

    Returns:
        pdf (pdf [obj]): pdf object from PDF class (extended from FPDF class)
    """
    pdf = PDF(
        orientation="P",  # portrait layout
        unit="mm",  # millimeters
        format="Letter",
    )

    # Add a page
    pdf.add_page()

    # Specify font
    pdf.set_font(family="helvetica", size=16)

    logging.info("PDF started")

    return pdf


def add_title(self, title):
    """Add title to report

    Args:
        title (str): text string to add to report
    """

    # move starting point to middle of the page
    self.set_y(100)

    # add text to page
    self.cell(
        w=200,
        h=10,
        txt=title,
        align="C",  # center align
        border=True,  # nice for debugging
    )

    logging.info(f"{title} added to pdf")


def export_pdf(self, path_to_output_pdf):
    """Generate PDF

    Args:
        path_to_output_pdf (str): path to save the output pdf file
    """
    self.output(path_to_output_pdf)
    logging.info(f"pdf exported to {path_to_output_pdf}")


def main():
    """
    Script runner
    """

    # Define input csv file
    input_csv = "BeltramiCountyRoads.csv"

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

        # start PDF
        pdf = PDF()
        
        # add title to page
        pdf.add_title('Beltrami Road Report, 2022')
        
        # add roads pages
        


        # Export data to csv
        csv_tasks.dict_to_csv(
            csv_path=output_csv,
            headers_list=["Surface", "Miles"],
            data_list=summary_data,
        )

        logging.info("Exported data to summary CSV.")

        # Record successful completion
        logging.info("Script successfully completed!")

    except:

        # Log error message
        logging.exception("Script failed!")


if __name__ == "__main__":
    main()
