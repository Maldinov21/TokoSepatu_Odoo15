from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'alstore.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    kontak = fields.Char(string='Kontak Supplier')
    sepatu_id = fields.Many2many(comodel_name='alstore.sepatu', string='Sepatu')
    
    

