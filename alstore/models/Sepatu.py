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
    jumlah_supplier = fields.Char(compute="_compute_jumlah_supplier", string='Jumlah Supplier')
    daftar_supplier = fields.Char(string='Daftar Supplier')

    @api.depends('supplier_id')
    def _compute_jumlah_supplier(self):
        for rec in self:
            a = self.env['alstore.supplier'].search([('sepatu_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jumlah_supplier = b
            rec.daftar_supplier = a