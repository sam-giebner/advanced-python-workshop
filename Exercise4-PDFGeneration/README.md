# Exercise 4: PDF Generation

In this exercise you will automate the generation of a series of PDFs for a report. To do so you will extend an existing class by adding functionality to it to suit your specific needs.

## Task

### 1. Install [PyFPDF](https://github.com/PyFPDF/fpdf2)

You will need to install the non-standard library PyFPDF. Something like command below should do the trick:

```sh
pip install fpdf2
```

### 2. Create a PDF generation `Class`

You have been provided with a script (`generate_report_from_csv.py`) that:

- takes an input spreadsheet (CSV file)
- creates an empty PDF document
- adds a page to the PDF for each record in the spreadsheet
  - using attributes of interest
- exports the PDF document to an output file

The script makes use of the same CSV modules (`helpers/csv_tasks`) as exercise 3.

The script is also organized into methods that make use of the `FPDF` module (the library you installed in step 1).

The script could be improved, however, by creating our own class that extends the existing `FPDF` class. This way all our methods can be class methods and data can be managed internally by the class.
This will also allow you to upgrade existing class methods (eg. `header()` and `footer()`) to better suit our needs.

As a reminder here is some code to get you started with creating the class:

```python
class CLassName(CLassIamExtending):
    class_method(self, other_class_methods):
    ....
```
