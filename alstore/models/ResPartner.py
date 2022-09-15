from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    is_direksi = fields.Boolean(string='Is Direksi')
    pelanggan = fields.Boolean(string='Pelanggan')
    id_member = fields.Char(string='ID Member', required=False, domain="[('pelanggan', '=', True)]")
    
    poin = fields.Integer(string = 'Poin', domain="[('pelanggan', '=', True)]")
    level = fields.Char(string='Level')
    
