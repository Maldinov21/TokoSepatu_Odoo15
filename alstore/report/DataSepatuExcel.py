from odoo import api, fields, models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.alstore.report_sepatu_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    
    #Laporan dalam 1 Sheet
    tgl_lap = fields.Date.today()
    
    def generate_xlsx_report(self, workbook, data, sepatu):
        sheet = workbook.add_worksheet('Data Sepatu')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Nama Sepatu')
        sheet.write(1, 1, 'Size (EU)')
        sheet.write(1, 2, 'Merek')
        sheet.write(1, 3, 'Harga Modal')
        sheet.write(1, 4, 'Harga Jual')
        sheet.write(1, 5, 'Supplier')
        row = 2
        col = 0
        for obj in sepatu:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.size)
            sheet.write(row, col+2, str(obj.merek_id.name))
            sheet.write(row, col+3, obj.harga_beli)
            sheet.write(row, col+4, obj.harga_jual)
            sheet.write(row, col+5, obj.daftar_supplier)
            row += 1