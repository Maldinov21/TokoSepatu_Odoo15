from odoo import api, fields, models


class Sepatu(models.Model):
    _name = 'alstore.sepatu'
    _description = 'New Description'

    name = fields.Char(string='Nama Sepatu')
    size = fields.Char(string='Size Sepatu (EU)')
    harga_beli = fields.Integer(string='Harga Modal',required=True)
    harga_jual = fields.Integer(string='Harga Jual',required=True)
    merek_id = fields.Many2one (comodel_name='alstore.merek', 
                                string='Merek',
                                ondelete='cascade')
    supplier_id = fields.Many2many(comodel_name='alstore.supplier', string='Supplier')
    stok = fields.Integer(string='Stok')
    