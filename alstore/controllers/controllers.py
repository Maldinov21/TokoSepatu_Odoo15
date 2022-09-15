from odoo import http, models, fields
from odoo.http import request
import json

class Alstore(http.Controller):
    @http.route('/alstore/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        barang = request.env['alstore.sepatu'].search([])
        isi = []
        for p in barang:
            isi.append({
                'nama_barang' : p.name,
                'harga_jual' : p.harga_jual,
                'stok' : p.stok
            })
        return json.dumps(isi)

    @http.route('/alstore/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['alstore.supplier'].search([])
        supp = []
        for s in supplier:
            supp.append({
                'nama_perusahaan' : s.name,
                'alamat' : s.alamat,
                'no_telepon' : s.kontak,
                'barang' : s.sepatu_id[0].name
            })
        return json.dumps(supp)