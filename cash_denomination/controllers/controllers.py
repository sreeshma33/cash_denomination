from odoo import http
from odoo.http import request
from datetime import date

class MyPageController(http.Controller):

    @http.route('/cash/denomination', type='http', auth='user', website=True)
    def my_page(self, **kw):
        user = request.env.user
        counters = request.env['cash.counter'].sudo().search([('name', 'in', user.ids)])
        to_counter = request.env['cash.counter'].sudo().search([])
        today = date.today()

        payment_receive = request.env['account.payment'].sudo().search([('journal_id.type','=','cash'),
                                                                ('payment_type','=','inbound'),
                                                                ('state', '=', 'paid'),
                                                                ('date', '=', today)
                                                                ])
        payment_send = request.env['account.payment'].sudo().search([('journal_id.type','=','cash'),
                                                                ('payment_type','=','outbound'),
                                                                ('state', '=', 'paid'),
                                                                ('date', '=', today)
                                                                ])
        total_received_amt = sum(payment_receive.mapped('amount'))
        total_send_amt = sum(payment_send.mapped('amount'))
        sub_total= total_received_amt - total_send_amt

        return request.render("cash_denomination.website_cash_denomination", {
            'counters': counters,
            'user': user,
            'total_cash': sub_total,
            'to_counter': to_counter,
        })
    
    # @http.route(['/cash/denomination/submit'], type='http', auth='user', methods=['POST'], website=True, csrf=False)
    # def cash_denomination_submit(self, **post):
    #     counter_id = post.get('counter')
    #     date_str = post.get('date')
    #     user = request.env.user
    #     line_values = [
    #         (0, 0, {
    #             'counts': int(value),
    #             'currency': key.split('_')[1],
    #         })
    #         for key, value in post.items()
    #         if key.startswith('counts_') and value and int(value) > 0
    #     ]
    #     transfer_records = request.env['cash.transfer'].sudo().search([
    #         ('name', '=', user.id),
    #         ('from_counter', '=', int(counter_id)),
    #         ('create_date', '>=', f"{date_str} 00:00:00"),
    #         ('create_date', '<=', f"{date_str} 23:59:59"),
    #     ])
    #     print("transfer_records--------------",transfer_records)
    #     transfer_lines = []
    #     for tr in transfer_records:
    #         transfer_lines.append((0, 0, {
    #             'from_counter': tr.from_counter.id,
    #             'to_counter': tr.to_counter.id,
    #             'amount': tr.amount,
    #             'remarks': tr.remarks,
    #             'transfer_date': tr.create_date,
    #         }))
    #     print("transfer_lines--------------",transfer_lines)
    #
    #     # Create main record with lines
    #     request.env['cash.denomination'].sudo().create({
    #         'date': post.get('date'),
    #         'user': request.env.user,
    #         'counter': post.get('counter'),
    #         'line_ids': line_values,
    #         'transfer_line_ids': transfer_lines,
    #     })
    #
    #     return request.redirect('/cash/denomination?success=1')

    @http.route(['/cash/denomination/submit'], type='http', auth='user', methods=['POST'], website=True, csrf=False)
    def cash_denomination_submit(self, **post):
        counter_id = post.get('counter')
        date_str = post.get('date')
        user = request.env.user

        line_values = [
            (0, 0, {
                'counts': int(value),
                'currency': key.split('_')[1],
            })
            for key, value in post.items()
            if key.startswith('counts_') and value and int(value) > 0
        ]

        transfer_records = request.env['cash.transfer'].sudo().search([
            ('name', '=', user.id),
            ('from_counter', '=', int(counter_id)),
            ('create_date', '>=', f"{date_str} 00:00:00"),
            ('create_date', '<=', f"{date_str} 23:59:59"),
        ])
        print("transfer_records--------------", transfer_records)

        transfer_lines = []
        for tr in transfer_records:
            transfer_lines.append((0, 0, {
                'from_counter': tr.from_counter.id,
                'to_counter': tr.to_counter.id,
                'amount': tr.amount,
                'remarks': tr.remarks,
                'transfer_date': tr.create_date,
                'to_user': tr.transfer_to_user.id if tr.transfer_to_user else False,
            }))
        print("transfer_lines--------------", transfer_lines)

        # ✅ FIXED HERE
        request.env['cash.denomination'].sudo().create({
            'date': date_str,
            'user': user.id,  # Pass ID, not record
            'counter': int(counter_id),  # Ensure it's an integer
            'line_ids': line_values,
            'transfer_line_ids': transfer_lines,
        })

        return request.redirect('/cash/denomination?success=1')

    @http.route(['/cash/transfer/submit'], type='http', auth='user', methods=['POST'], website=True, csrf=False)
    def transfer_cash_submit(self, **post):
        """Handles transfer form submission from modal"""
        user = request.env.user

        # Extract form data
        from_counter_id = post.get('from_counter')
        to_counter_id = post.get('to_counter')
        transfer_amount = post.get('transfer_amount')
        remarks = post.get('remarks')
        transfer_to_user = post.get('transfer_to_user')

        request.env['cash.transfer'].sudo().create({
            'name': request.env.user.id,
            'from_counter': int(from_counter_id) if from_counter_id else False,
            'transfer_to_user': transfer_to_user,
            'to_counter': int(to_counter_id) if to_counter_id else False,
            'amount': float(transfer_amount) if transfer_amount else 0.0,
            'remarks': remarks or '',
        })

        # Redirect back to page with success flag
        return request.redirect('/cash/denomination?transfer_success=1')

