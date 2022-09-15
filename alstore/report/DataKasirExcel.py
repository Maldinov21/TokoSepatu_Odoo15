from odoo import api, fields, models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.alstore.report_kasir_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    
    #Laporan dalam 1 Sheet
    tgl_lap = fields.Date.today()
    
    def generate_xlsx_report(self, workbook, data, kasir):
        sheet = workbook.add_worksheet('Data Kasir')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'ID Kasir')
        sheet.write(1, 1, 'Nama')
        sheet.write(1, 2, 'Alamat')
        sheet.write(1, 3, 'Tanggal Lahir')
        row = 2
        col = 0
        for obj in kasir:
            col = 0
            sheet.write(row, col, obj.id_kasir)
            sheet.write(row, col+1, obj.name)
            sheet.write(row, col+2, obj.alamat)
            sheet.write(row, col+3, str(obj.tgl_lahir))
            row += 1