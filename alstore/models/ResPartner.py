from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    pelanggan = fields.Boolean(string='Pelanggan')
    id_member = fields.Char(string='ID Member', required=False, domain="[('pelanggan', '=', True)]")
    
    poin = fields.Integer(string = 'Poin', domain="[('pelanggan', '=', True)]")
    level = fields.Char(string='Level')
    
    _sql_constraints = [
        ('id_member_unik', 'unique (id_member)', 'ID Member tidak bisa dipakai, karena sudak digunakan !!!')
    ]