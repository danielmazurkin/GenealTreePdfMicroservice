import pdfkit
from config.base import PATH_TO_PDF_WKHTML
import os


class FormPDFPeople:

    @staticmethod
    def form_pdf_people(data_about_people):
        """Базовое формирование PDF из HTML"""

        is_live = 'Да' if data_about_people['is_live'] else 'Нет'
        sex_text_people = 'Мужчина' if data_about_people['sex'] == 'MALE' else 'Женщина'
        id_people = data_about_people['id']

        data_with_people_for_pdf = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset='utf-8'>
        </head>
        <body>
        Имя: {data_about_people['name']}  <br />                
        Фамилия: {data_about_people['surname']} <br />
        Отчество: {data_about_people['last_name']} <br />
        Живой: {is_live} <br />
        Пол: {sex_text_people} <br />
        </body>
        </html>
        """

        path_with_pdf_report_directory = os.path.join('./data', str(id_people))
        path_with_pdf_report = os.path.join('./data', str(id_people), 'out.pdf')
        path_template_pdf = os.path.join('./template_pdf', 'index.html')

        if not os.path.exists(path_with_pdf_report_directory):
            os.makedirs(path_with_pdf_report_directory)

        with open(path_template_pdf, "w+") as pdf_file:
            pdf_file.write(data_with_people_for_pdf)

        pdfkit.configuration(wkhtmltopdf=PATH_TO_PDF_WKHTML)
        pdfkit.from_file(path_template_pdf, path_with_pdf_report)


