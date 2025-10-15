from odoo import models, fields, api

class CashCounter(models.Model):
    _name = 'cash.counter'  
    _description = 'Cash Counter' 
    _rec_name = "cash_counter"
    _order = 'id desc'

    name = fields.Many2many('res.users',string='Name',required=True)
    cash_counter = fields.Char(string='Cash Counter',required=True)