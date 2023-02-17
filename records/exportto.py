from io import BytesIO
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas

#Exporting models to txt
def sales_to_txt(model):
    receipts = model.objects.all()
    with open('sales_data.txt', 'w') as file:
        for obj in receipts:
            file.write(str(obj) + "\n")

#Exporting models to pdf
def sales_to_pdf(model):
    res = HttpResponse(content_type='application/pdf')
    res['Content-Disposition'] = 'attachment; filename="sales_data.pdf"'
    
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    
    receipts = model.objects.all()
    
    for obj in receipts:
        pdf.drawString(100, 100, str(obj))
        pdf.showPage()
        
    pdf.save()
    buffer.seek(0)
    return FileResponse(buffer, content_type='application/pdf')
