# Documents
# Word - DOCX (python-docx)
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Cm, Inches, Mm, Pt # для размеров

doc = Document()  # создание экземпляра документа

# Добавление заголовка

doc.add_heading('Отчет за месяц', 1)  # заголовок уровня один
paragraph = doc.add_paragraph() # отступ
paragraph = doc.add_paragraph('В этом отчете представлены ')
# run - что-то внутри абзаца (текст, картинка)
paragraph.add_run(' ключевые показатели').bold = True

paragraph_format = paragraph.paragraph_format
paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
# маркированный список
paragraph = doc.add_paragraph('Первый пункт', style='List Bullet')
paragraph = doc.add_paragraph('Второй пункт', style='List Bullet')
# нумерованный список
paragraph = doc.add_paragraph('Первый пункт', style='List Number')
paragraph = doc.add_paragraph('Второй пункт', style='List Number')

paragraph = doc.add_paragraph() # отступ
# добавляем и заполняем таблицу
table = doc.add_table(3, 2)
for i, a  in enumerate(table.rows):
    for j, b  in enumerate(table.columns):
        b.text = f'Строка {i + 1}, Столбец {j + 1}'

doc.add_paragraph() # отступ
doc.add_picture('images/sunny_day.jpg', width=Mm(50))



doc.save('./documents/report.docx')
