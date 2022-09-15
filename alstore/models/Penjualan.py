from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Penjualan(models.Model):
    _name = 'alstore.penjualan'
    _description = 'New Description'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Many2one(comodel_name="res.partner", string='Nama Pembeli')
    id_member = fields.Char(compute="_compute_id_member",
                            string='ID member',
                            required=False)
    tgl_penjualan = fields.Datetime(string='Tgl. Transaksi', 
                                default=fields.Datetime.now())
    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Pembayaran')
    detailpenjualan_ids = fields.One2many (comodel_name='alstore.detailpenjualan', 
                                           inverse_name='penjualan_id', 
                                           string='Detail Penjualan')
    state = fields.Selection\
            (string='Status', 
            selection=[('draft', 'Draft'), 
                       ('confirm', 'Confirm'),
                       ('done', 'Done'),
                       ('cancelled', 'Cancelled')],
            required=True, readonly=True, default='draft')
    
    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancelled(self):
        self.write({'state': 'cancelled'})
    
    def action_draft(self):
        self.write({'state': 'draft'})
    
    @api.depends('nama_pembeli')
    def _compute_id_member(self):
        for rec in self:
            rec.id_member = rec.nama_pembeli.id_member

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['alstore.detailpenjualan'].search([('penjualan_id','=',rec.id)]).mapped('subtotal'))
            rec.total_bayar = a
    
    @api.ondelete(at_uninstall=False)
    def __ondelete_penjualan(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise ValidationError("Tidak dapat menghapus jika status BUKAN DRAFT")
        else:
            if self.detailpenjualan_ids:
                a = []
                for rec in self:
                    a = self.env['alstore.detailpenjualan'].search([('penjualan_id','=',rec.id)])
                    print(a)
                for ob in a:
                    print(str(ob.sepatu_id.name) + ' ' + str(ob.qty))
                ob.sepatu_id.stok += ob.qty
    
    def write(self,vals):
        for rec in self:
            a = self.env['alstore.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.sepatu_id.name)+' '+str(data.qty)+' '+str(data.sepatu_id.stok))
                data.sepatu_id.stok += data.qty
                
        record = super(Penjualan,self).write(vals)
        for rec in self:
            b = self.env['alstore.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            print(b) 
            for databaru in b:
                if databaru in a:
                    print(str(databaru.sepatu_id.name)+' '+str(databaru.qty)+' '+str(databaru.sepatu_id.stok))
                    databaru.sepatu_id.stok -= databaru.qty   
                else:
                    pass
        return record

    # @api.constrains('id_member')
    # def check_id_member(self):
    #     for rec in self:
    #         if rec.id_member == rec.self:
    #             raise ValidationError("ID Member {} tidak bisa digunakan, karena sudah ada".format(rec.nama_pembeli.id_member))

    _sql_constraints = [
        ('no_nota_unik', 'unique (name)', 'Nomor Nota tidak boleh sama !!!')
    ]

class DetailPenjualan(models.Model):
    _name = 'alstore.detailpenjualan'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(comodel_name='alstore.penjualan', string='Detail Penjualan')
    sepatu_id = fields.Many2one(comodel_name='alstore.sepatu', string='List Barang')
    harga = fields.Integer(string='Harga')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute ='_compute_subtotal', string='Subtotal')
        
    @api.depends('harga','qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga
        
    @api.onchange('sepatu_id')
    def _onchange_sepatu_id(self):
        if (self.sepatu_id.harga_jual):
            self.harga = self.sepatu_id.harga_jual
    
    @api.model
    def create(self,vals):
        record = super(DetailPenjualan,self).create(vals)
        if record.qty:
            self.env['alstore.sepatu'].search([('id','=',record.sepatu_id.id)]).write({'stok' : record.sepatu_id.stok - record.qty})
        return record
    
    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("Mau belanja {} berapa pasang ?  ".format(rec.sepatu_id.name))
            elif (rec.sepatu_id.stok < rec.qty):
                raise ValidationError("Stok {} tidak mencukupi, hanya tersedia {}".format(rec.sepatu_id.name, rec.sepatu_id.stok))
    
    

        