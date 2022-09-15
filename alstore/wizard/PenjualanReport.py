from odoo import api, fields, models


class PenjualanReport(models.Model):
    _name = 'alstore.penjualanreport'
    _description = 'New Description'

    pelanggan_id = fields.Many2one(comodel_name='res.partner', 
                                  string='Pelanggan',
                                  required=False)
    dari_tgl = fields.Date(string='Dari Tanggal',
                           rquired=False)
    ke_tgl = fields.Date(string='Ke Tanggal',
                         required=False)

    def action_penjualan_report(self):
        filter = []
        pelanggan_id = self.pelanggan_id
        dari_tgl = self.dari_tgl
        ke_tgl = self.ke_tgl
        if pelanggan_id:
            filter += [('nama_pembeli', '=', pelanggan_id.id)]
        if dari_tgl:
            filter += [('tgl_penjualan', '>=', dari_tgl)]
        if ke_tgl:
            filter += [('tgl_penjualan', '<=', ke_tgl)]
        print(filter)
        penjualan = self.env['alstore.penjualan'].search_read(filter)
        print(penjualan)
        data = {
            'form':self.read()[0],
            'penjualanx': penjualan
        }
        print(data)
        return self.env.ref('alstore.wizard_penjualanreport_pdf').report_action(self, data=data)
    
    
    
