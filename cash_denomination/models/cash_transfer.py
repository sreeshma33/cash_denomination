from odoo import models, fields, api

class CashTransfer(models.Model):
    _name = 'cash.transfer'
    _description = 'Cash Transfer'

    name = fields.Many2one('res.users',string='Transferred By', readonly=True)
    from_counter = fields.Many2one('cash.counter', string='From Counter', readonly=True)
    to_counter = fields.Many2one('cash.counter', string='To Counter', readonly=True)
    amount = fields.Integer(string='Cash', readonly=True)
    remarks = fields.Char(string='Remarks', readonly=True)
    date = fields.Datetime(string='Transfer Date', default=fields.Datetime.now, readonly=True)
    transfer_to_user = fields.Many2one('res.users', string='To User', readonly=True)  # <-- fix here
