import tkinter as tk
import tkinter.font as font
from tkinter import *
import os.path
from os import path


def callback():
    tblRowData(brandEntry.get(), dateFeedEntry.get(),eggCollectEntry.get(),dateEggCollectEntry.get(),priceOfFeedEntry.get(),lbsOfFeedEntry.get())
    window.destroy()


def button_pressed(values):
    expression_field_value.set(expression_field_value.get() + str(values))


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Data Collector")
    myFont = font.Font(family='Helvetica')
    expression_field_value = StringVar()

    # Labels
    tk.Label(window, text="Brand Name", font=myFont).grid(row=0)
    tk.Label(window, text="Date Feed Went In", font=myFont).grid(row=1)
    tk.Label(window, text="Eggs Collected", font=myFont).grid(row=2)
    tk.Label(window, text="Date Eggs Collected", font=myFont).grid(row=3)
    tk.Label(window, text="Price of Feed", font=myFont).grid(row=4)
    tk.Label(window, text="How many lbs bag", font=myFont).grid(row=5)
    Submit = Button(text="Submit", width=10, command=callback)
    # Input Fields
    brandEntry = tk.Entry(window)
    dateFeedEntry = tk.Entry(window)
    eggCollectEntry = tk.Entry(window)
    dateEggCollectEntry = tk.Entry(window)
    priceOfFeedEntry = tk.Entry(window)
    lbsOfFeedEntry = tk.Entry(window)
    # Grid Entry
    brandEntry.grid(row=0, column=1)
    dateFeedEntry.grid(row=1, column=1)
    eggCollectEntry.grid(row=2, column=1)
    dateEggCollectEntry.grid(row=3, column=1)
    priceOfFeedEntry.grid(row=4, column=1)
    lbsOfFeedEntry.grid(row=5, column=1)
    Submit.grid(row=6, column=1)

    input_file: bool = os.path.exists('C:\\PythonProject\\EggMaker.html')


    def createPage():
        with open('C:\\PythonProject\\EggMaker.html', "w") as newFile:
            newFile.write("<!DOCTYPE html>\n")
            newFile.write('<html>\n')
            newFile.write('<head>\n')
            # Start Style sheet
            newFile.write('<style>\n')
            # Table
            newFile.write('table {\n')
            newFile.write('font-family: arial, sans-serif;\n')
            newFile.write('border-collapse: collapse;\n')
            newFile.write('width: 100%;\n')
            newFile.write('table-layout: fixed;\n')
            newFile.write('}\n')
            # Table data and header
            newFile.write('td, th {\n')
            newFile.write('border: 1px solid #89a4fa;\n')
            newFile.write('text-align: center;\n')
            newFile.write('padding: 8px;\n')
            newFile.write('}\n')
            newFile.write('th {text-align: center;}\n')
            # Table Row
            newFile.write('tr:nth-child(even) {\n')
            newFile.write('background-color: #c2d0ff;\n')
            newFile.write('}\n')
            # H2
            newFile.write('h2 { text-align: center;}')
            # End of style sheet
            newFile.write('</style>\n')
            newFile.write('</head>\n')


def tableCreator():
    with open('C:\\PythonProject\\EggMaker.html', "a") as editFile:
        editFile.write('<h2>Egg-amining The Costs To Raise Chickens</h2>\n')
        editFile.write('<table>\n')
        editFile.write(f' <tr>\n')
        editFile.write(f'\t<th>Brand</th>\n')
        editFile.write(f'\t<th>Date Feed Went In</th>\n')
        editFile.write(f'\t<th>Eggs Collected</th>\n')
        editFile.write(f'\t<th>Date Eggs Collected</th>\n')
        editFile.write(f'\t<th>Price Paid</th>\n')
        editFile.write(f'\t<th>Pounds</th>\n')
        editFile.write(f' </tr>\n')


def tblRowData(brandEntry, dateFeedEntry,eggCollectEntry,dateEggCollectEntry,priceOfFeedEntry,lbsOfFeedEntry):
    with open('C:\\PythonProject\\EggMaker.html',
              "a") as insertRowData:
        insertRowData.write(f'<tr>')
        insertRowData.write(f'\t<td>{brandEntry}</td>\n')
        insertRowData.write(f'\t<td>{dateFeedEntry}</td>\n')
        insertRowData.write(f'\t<td>{eggCollectEntry}</td>\n')
        insertRowData.write(f'\t<td>{dateEggCollectEntry}</td>\n')
        insertRowData.write(f'\t<td>${priceOfFeedEntry}</td>\n')
        insertRowData.write(f'\t<td>{lbsOfFeedEntry} lbs</td>\n')
        insertRowData.write(f'</tr>')
        insertRowData.close()


if not input_file:
    createPage()
    tableCreator()

window.mainloop()
