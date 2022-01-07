from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.colors import black, firebrick, lightgreen
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Flowable, TableStyle, Table, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from io import BytesIO
from django.http import HttpResponse
import os
import sqlite3
from .extract_db import return_prediction

sql_path = r"C:\\Users\\TJ\\OneDrive\\Documents\\GitHub\\CS4800\\helloworld\\Games.db"
conn = sqlite3.connect(sql_path, check_same_thread=False)

class MCLine(Flowable):
    def __init__(self, width=500, height=0):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        self.canv.setStrokeColor(black)
        self.canv.setLineWidth(6)
        self.canv.line(0, self.height, self.width, self.height)

def full_img_path(pic_name):
    img = pic_name.replace(":","")
    #return "{% static 'img/" + img + ".png' %}"
    #return "img/" + img + ".png"
    return img + '.png'

def createGraph():
    drawing = Drawing(400, 200)
    data = [
        (50, 50, 50, 45, 40, 40)
    ]
    lc = HorizontalLineChart()
    lc.x = 50
    lc.y = 50
    lc.height = 150
    lc.width = 300
    lc.data = data
    lc.joinedLines = 1
    catNames = "Sep'20 Oct'20 Dec'20 Jan'20 Feb'20 March'20".split(' ')
    lc.categoryAxis.categoryNames = catNames
    lc.categoryAxis.labels.boxAnchor = 'n'
    lc.categoryAxis.labels.fontName = 'Courier-Bold'
    lc.valueAxis.labels.fontName = 'Courier-Bold'
    lc.valueAxis.labelTextFormat = '$%2.0f '
    lc.valueAxis.valueMin = 0
    lc.valueAxis.valueMax = 90
    lc.valueAxis.valueStep = 15
    lc.lines[0].strokeWidth = 3
    lc.lines[0].strokeColor = lightgreen
    lc.fillColor = black
    drawing.add(lc)
    return drawing


def create_report(the_game, game_img, pub, release, platform, lowest_seller,lowest_price):
    lowest_price = lowest_price[1:]
    if lowest_price != "":
        if lowest_seller == "Steam.com":
            commission_percent = "30%"
            commission = str((float(lowest_price) - round((float(lowest_price) * .30),2)))
            commission = "$" + str(round(float(commission), 2))
        elif lowest_seller == "Humblebundle.com":
            commission_percent = "15%"
            commission = str((float(lowest_price) - round((float(lowest_price) * .15),2)))
            commission = "$" + str(round(float(commission), 2))
        elif lowest_seller == "GOG.com":
            commission_percent = "30%"
            commission = str((float(lowest_price) - round((float(lowest_price) * .30),2)))
            commission = "$" + str(round(float(commission), 2))
        elif lowest_seller == "Origin.com":
            commission_percent = "Unknown"
            commission = "Unknown"
        elif lowest_seller == "EpicGames.com": 
            commission_percent = "15%"
            commission = str((float(lowest_price) - round((float(lowest_price) * .12),2)))
            commission = "$" + str(round(float(commission), 2))
        else:
            commission_percent = ""
            commission = ""
    prediction = return_prediction(conn,the_game)
    img = full_img_path(game_img)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    pdf_buff = BytesIO()
    doc = SimpleDocTemplate(pdf_buff)
    Story = []
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    headline_style = styles["Heading1"]
    headline_style.alignment = TA_JUSTIFY
    logo = r"C:\Users\TJ\OneDrive\Documents\GitHub\CS4800\static\img\GAMESEARCH.png"
    im = Image(logo, 2.5 * inch, 1.25 * inch)
    im.hAlign = 'RIGHT'
    Story.append(im)
    Story.append(Spacer(1, 12))
    line = MCLine(460)
    Story.append(line)
    Story.append(Spacer(1, 12))
    launcher_title = '<font size="24" name = "Courier-Bold">GAME SUMMARY</font>'
    Story.append(Paragraph(launcher_title, headline_style))
    Story.append(Spacer(1, 12))
    Story.append(Spacer(1, 12))
    game_path = "C:\\Users\\TJ\\OneDrive\\Documents\\GitHub\\CS4800\\static\\img\\" + img
    gm = Image(game_path, 2.5 * inch, 3.5 * inch)
    Story.append(gm)
    Story.append(Spacer(1, 12))
    data = [
        ['GAME', the_game],
        ['PUBLISHER', pub],
        ['RELEASE DATE', release],
        ['PLATFORMS', platform]]
    t = Table(data)
    t.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 2, colors.black),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (0, -1), colors.black),
        ('BACKGROUND', (-1, 0), (-1, 0), colors.lightgrey),
        ('BACKGROUND', (-1, -1), (-1, 1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.white),
        ('FONTNAME', (0, 0), (-1, -1), 'Courier-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')]))
    Story.append(t)
    Story.append(Spacer(1, 12))
    Story.append(Spacer(1, 12))
    Story.append(line)
    Story.append(Spacer(1, 12))
    launcher_title = '<font size="24" name = "Courier-Bold" color = black>HOTTEST DEAL!!</font>'
    Story.append(Paragraph(launcher_title, headline_style))
    Story.append(Spacer(1, 12))
    Story.append(Spacer(1, 12))
    data = [
        ['SELLER', lowest_seller],
        ['PRICE', lowest_price],
        ['SERVICE COMMISION', commission_percent],
        ['DEVELOPER PAYOUT', commission]]
    t = Table(data)
    t.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 2, colors.black),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (0, -1), colors.firebrick),
        ('BACKGROUND', (-1, 0), (-1, 0), colors.lightgrey),
        ('BACKGROUND', (-1, -1), (-1, 1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.white),
        ('FONTNAME', (0, 0), (-1, -1), 'Courier-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')]))
    Story.append(t)
    Story.append(PageBreak())
    # data = [
    #     ['LAUNCHER SERVICE', 'EPIC GAMES'],
    #     ['PRICE', '$50'],
    #     ['SERVICE COMMISION', '12%'],
    #     ['DEVELOPER PAYOUT', '$44']]
    # t = Table(data)
    # t.setStyle(TableStyle([
    #     ('INNERGRID', (0, 0), (-1, -1), 2, colors.black),
    #     ('BOX', (0, 0), (-1, -1), 2, colors.black),
    #     ('FONTSIZE', (0, 0), (-1, -1), 12),
    #     ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    #     ('BACKGROUND', (0, 0), (0, -1), colors.firebrick),
    #     ('BACKGROUND', (-1, 0), (-1, 0), colors.lightgrey),
    #     ('BACKGROUND', (-1, -1), (-1, 1), colors.lightgrey),
    #     ('TEXTCOLOR', (0, 0), (0, -1), colors.white),
    #     ('FONTNAME', (0, 0), (-1, -1), 'Courier-Bold'),
    #     ('ALIGN', (0, 0), (-1, -1), 'CENTER')]))
    # Story.append(t)
    # Story.append(Spacer(1, 12))
    # Story.append(Spacer(1, 12))
    # Story.append(line)
    # Story.append(Spacer(1, 12))
    # launcher_title = '<font size="24" name = "Courier-Bold" color = black>GAME VALUE OVER TIME</font>'
    # Story.append(Paragraph(launcher_title, headline_style))
    # Story.append(Spacer(1, 12))
    # Story.append(Spacer(1, 12))
    # Story.append(createGraph())
    # Story.append(line)
    # Story.append(Spacer(1, 12))
    launcher_title = '<font size="24" name = "Courier-Bold" color = black>PURCHASE RECOMMENDATION</font>'
    Story.append(Paragraph(launcher_title, headline_style))
    Story.append(Spacer(1, 12))
    Story.append(Spacer(1, 12))
    launcher_title = '<font size="16" name = "Courier" color = black>'+prediction+'</font>'
    Story.append(Paragraph(launcher_title, headline_style))
    doc.build(Story)
    response.write(pdf_buff.getvalue())
    pdf_buff.close()
    return response

