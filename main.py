# Documents
# Word - DOCX (python-docx)
# pip install docxtpl
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Cm, Inches, Mm, Pt # для размеров
from docxtpl import DocxTemplate
import pkg_resources

document = DocxTemplate('documents/template.docx')

content = {
    'company': 'ООО "Зеленоглазое такси"',
    'employee': 'Петров П.П.',
    'position': 'Директор',
    'date' : '01/09/2024'
}

document.render(content)
document.save('./documents/about.docx')