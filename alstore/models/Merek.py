from odoo import api, fields, models


class Merek(models.Model):
    _name = 'alstore.merek'
    _description = 'New Description'

    name = fields.Selection ([
        ('nike', 'Nike'),
        ('adidas', 'Adidas'),
        ('newbalance', 'New Balance'),
        ('converse', 'Converse'),
        ('vans', 'Vans'),
        ('puma', 'Puma'),
        ('ardiles', 'Ardiles'),
        ('brodo', 'Brodo'),
        ('compass', 'Compass'),],
        string = 'Nama Merek')
    
    merek_kode = fields.Char(string='Kode Merek')
    keterangan = fields.Char(string='Keterangan')
    rak = fields.Char(string='Rak')
    sepatu_ids = fields.One2many(comodel_name='alstore.sepatu', 
                                 inverse_name='merek_id', 
                                 string='List Sepatu')
    jumlah_barang = fields.Char(compute="_compute_jumlah_barang", string='Jumlah Barang')
    daftar = fields.Char(string='Daftar Isi')

    @api.onchange('name')
    def _compute_merek_kode(self):
    # def _onchange_merek_kode(self):
        if (self.name == 'nike'):
            self.merek_kode = 'nike'
        if (self.name == 'adidas'):
            self.merek_kode = 'Adidas'
        elif (self.name == 'newbalance'):
            self.merek_kode = 'newbalance'
        elif (self.name =='converse'):
            self.merek_kode = 'converse'
        elif (self.name == 'vans'):
            self.merek_kode = 'vans'
        elif (self.name == 'puma'):
            self.merek_kode = 'puma'
        elif (self.name == 'ardiles'):
            self.merek_kode = 'ardiles'
        elif (self.name == 'brodo'):
            self.merek_kode = 'brodo'
        elif (self.name == 'compass'):
            self.merek_kode = 'compass'
    
    @api.depends('sepatu_ids')
    def _compute_jumlah_barang(self):
        for rec in self:
            a = self.env['alstore.sepatu'].search([('merek_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jumlah_barang = b
            rec.daftar = a