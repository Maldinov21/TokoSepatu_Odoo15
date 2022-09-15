from odoo import api, fields, models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.alstore.report_merek_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    
    #Laporan dalam 1 Sheet
    tgl_lap = fields.Date.today()
    
    def generate_xlsx_report(self, workbook, data, merek):
        sheet = workbook.add_worksheet('Data Merek')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Nama Merek')
        sheet.write(1, 1, 'Kode Merek')
        sheet.write(1, 2, 'Deskripsi')
        sheet.write(1, 3, 'Rak Letak Sepatu')
        sheet.write(1, 4, 'Daftar Sepatu')
        row = 2
        col = 0
        for obj in merek:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.merek_kode)
            sheet.write(row, col+2, obj.keterangan)
            sheet.write(row, col+3, obj.rak)
            sheet.write(row, col+4, obj.daftar)
            row += 1