from fpdf import FPDF

from .cv import get_data, iterate_variable_input



def createpdf(path):
        data = get_data(path)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 10)
        pdf = iterate_variable_input_pdf(data,pdf)
        pdf.output("cv.pdf")


def iterate_variable_input_pdf(data, pdf):
    for k, v in data.items():
        if isinstance(v, dict):
            iterate_variable_input_pdf(v,pdf)
        elif isinstance(v, list):
            pdf.ln(10)    
            pdf.write(10, ''.join(str(f"{k}:".encode('UTF-8')).split('b',1)))
            pdf.ln(10)
            for value in v:
                pdf.write(10, ''.join(str(f"  ->  {value}".encode('UTF-8')).split('b',1)))
                pdf.ln(10)
        else:
            pdf.write(10, ''.join(str(f" -> {k} - {v}".encode('UTF-8')).split('b',1)))
            pdf.ln(10)
    return pdf