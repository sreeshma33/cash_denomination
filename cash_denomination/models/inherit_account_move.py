from odoo import models, fields, api

class CashCounter(models.Model):
    _inherit = 'account.move'


    journal_type = fields.Char(string='Journal Type')


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    def action_create_payments(self):
        print("=== Inside payment register ===")

        res = super().action_create_payments()
        print("res >>>>", res)

        moves = self.line_ids.move_id
        for move in moves:
            if self.journal_id:
                move.journal_type = self.journal_id.type
                print("move.journal_type=====",move.journal_type)
        print("--", )
        return res