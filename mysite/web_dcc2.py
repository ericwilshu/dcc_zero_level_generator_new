"""
This is a flask webapp that provides a web interface for outputing Dungeon Crawl
Classics RPG zero level characters in .pdf format.

Functions:
    hello()
    character_funnel()

Dependencies:
    Modules:
        flask
        datetime
        cairosvg
        char_sheet_assembler2
        char_sheet_creator2
        import_data
    Files:
        2x2_template_blank.svg
        char_sheet_blank.svg
        Table1_1_Ability_Score_Modifiers.csv
        Table1_2_Luck_Score.txt
        Human_Occupations.csv
        Dwarf_Occupations.csv
        Elf_Occupations.csv
        Halfling_Occupations.csv
        Table1_3a_Farmer_Type.txt
        Table1_3b_Animal_Type.txt
        Table1_3c_Whats_In_The_Cart.txt
        Table3_4_Equipment.txt
        AppendixL.csv
"""

from flask import Flask, render_template, request, send_from_directory
from datetime import datetime
from cairosvg import svg2pdf as s2p
import char_sheet_assembler2
from import_data import getDataFiles
import dcc_root_path

app = Flask(__name__)

ROOT_PATH = dcc_root_path.get_root_path()

#Get the rulebook data!
dataDict = getDataFiles('{}data_files/'.format(ROOT_PATH))

@app.route('/')
def hello() -> 'html':
    """Provide a simple web interface for the app."""
    return render_template('index.html', the_title="DCC Character Funnel", the_heading='Dungeon Crawl Classics 0 level character generator')



@app.route('/character_funnel', methods=['POST'])
def character_funnel():
    """Run the character creation and sheet creation code, output the results in the browser."""
    #Get the checked value from the 5 check boxes on the form.
    suitability = request.form.get('suitability')
    nohuman = request.form.get('nohuman')
    nodwarf = request.form.get('nodwarf')
    noelf = request.form.get('noelf')
    nohalfling = request.form.get('nohalfling')

    #Get the current date and time to label the .pdf file.
    now = datetime.today().strftime("%Y-%m-%d_%H:%M:%S")
    #NEW_SHEET_PDF = "/home/ericws/mysite/static/new_sheets/" + now + ".pdf"
    NEW_SHEET_PDF = "{}static/new_sheets/{}.pdf".format(ROOT_PATH, now)
    #NEW_SHEET_PDF_TO_RETURN = "/static/new_sheets/" + now + ".pdf"
    NEW_SHEET_PDF_TO_RETURN = "{}.pdf".format(now)

    #Assemble the sheet by running char_sheet_assembler2.
    new_sheet = char_sheet_assembler2.assemble_sheets(dataDict, suitability, nohuman, nodwarf, noelf, nohalfling)
    #Convert from .svg to .pdf with cairosvg module.
    s2p(url=new_sheet, write_to=NEW_SHEET_PDF)
    #Render a new webpage with the .pdf on it for the user to save if they want.
    #return render_template('display_sheet.html', the_title="DCC 0 level characters", the_sheet=NEW_SHEET_PDF_TO_RETURN)
    return send_from_directory('{}static/new_sheets/'.format(ROOT_PATH), NEW_SHEET_PDF_TO_RETURN)

app.run()
