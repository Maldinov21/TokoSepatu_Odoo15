from odoo import api, fields, models


class InputBarang(models.TransientModel):
    _name = 'alstore.inputbarang'

    sepatu_id = fields.Many2one(comodel_name='alstore.sepatu', 
                                string='Nama Barang',
                                required=True)
    jumlah = fields.Integer(
        string = 'Jumlah',
        required=False)
    
    def button_input_barang(self):
        for rec in self:
            self.env['alstore.sepatu'].search([('id','=', rec.sepatu_id.id)]).write({'stok':rec.sepatu_id.stok + rec.jumlah})
