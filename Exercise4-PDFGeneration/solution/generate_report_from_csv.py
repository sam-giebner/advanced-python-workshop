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
from email import header
from pathlib import Path
from fpdf import FPDF
import logging
from helpers import csv_tasks

#
class PDF(FPDF):
    def header(self):
        """configure page header"""
        # Rendering logo:
        input_logo = (
            Path(__file__).parent.absolute().joinpath("beltrami-county-logo.png")
        )
        self.image(input_logo, 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Beltrami County Road Report", align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        """configure page footer"""
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

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

    def export(self, path_to_output_pdf):
        """Generate PDF

        Args:
            path_to_output_pdf (str): path to save the output pdf file
        """
        self.output(path_to_output_pdf)
        logging.info(f"pdf exported to {path_to_output_pdf}")

    def add_row_to_table(self, headers, row=None):
        """Add row to table
            If row data is provided use it,
            otherwise add table headers

        Args:
            row (dict, optional): row from spreadsheet. Defaults to None.
        """
        # check for row data
        # if it's not there, this must be a header row
        if not row:
            for col in headers:
                self.cell(w=40, h=7, txt=col, border=1, align="C")
            self.ln()
            logging.info(f"header row added: {headers}")

        # row data
        else:
            for col in headers:
                self.cell(w=40, h=6, txt=row[col], border=1)
            self.ln()
            logging.info(f"row added: {row}")


def main():
    """
    Script runner
    """

    # Define input csv file
    input_csv_name = "BeltramiCountyRoads.csv"

    # convert to full path
    input_csv = Path(__file__).parent.absolute().joinpath(input_csv_name)

    # Define output pdf file
    output_pdf_name = "BeltramiRoadReport.pdf"
    output_pdf = Path(__file__).parent.absolute().joinpath(output_pdf_name)

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

        # add title to page
        pdf.add_title("Beltrami Road Report, 2022")

        # specify headers
        table_headers = ["FULLNAME", "CTU", "JURS_DESC", "SURF_TYPE", "STATUS"]

        # add headers
        pdf.add_row_to_table(table_headers)

        # add roads pages
        for row in road_data:
            pdf.add_row_to_table(table_headers, row=row)

        # export pdf
        pdf.export(output_pdf)

        # Record successful completion
        logging.info("Script successfully completed!")

    except:

        # Log error message
        logging.exception("Script failed!")


if __name__ == "__main__":
    main()
