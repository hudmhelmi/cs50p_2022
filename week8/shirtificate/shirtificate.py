from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.image("shirtificate.png", w=pdf.epw, x=(210 - pdf.epw)/2, y=pdf.eph/4)
pdf.set_font("helvetica", "B", 50)
pdf.cell(txt="CS50 Shirtificate", center=True)
pdf.set_font("helvetica", size=30)
pdf.set_text_color(r=255, g=255, b=255)
pdf.cell(txt=f"{name} took CS50", center=True, h=pdf.eph)
pdf.output("shirtificate.pdf")