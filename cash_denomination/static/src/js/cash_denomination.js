import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";

publicWidget.registry.CounterCashDenomination = publicWidget.Widget.extend({
    selector: '.cash_denomination_template',
    events: {
        'click #cash_transfer': '_TransferCash',
        'input .counts-input': '_onCountChange',
        'submit #cash_denomination_form': '_CashDenominationSubmit',
    },

    start: function () {
        this._super.apply(this, arguments);
        this._setCurrentDate();
        this.$('.counts-input').val('')
        this.$('.total-field').val('')
        this.$('#grand_total').val('0.00');

        this._checkTransferSuccess();
        this._checkSameCounterError();
        this._checkInsufficientCash(); 
    },

    _setCurrentDate: function () {
        const today = new Date();
        const formattedDate = today.toISOString().split('T')[0];
        this.$('#date_field').val(formattedDate);
    },

    _onCountChange: function (ev) {
        const $input = $(ev.currentTarget);
        const count = parseInt($input.val()) || 0;
        const currency = parseInt($input.data('value')) || 0;
        const total = count * currency;

        const $row = $input.closest('tr');
        $row.find('.total-field').val(total.toFixed(2));

        this._updateGrandTotal();
    },

    _updateGrandTotal: function () {
        let grandTotal = 0;
        this.$('.total-field').each(function () {
            const val = parseFloat($(this).val()) || 0;
            grandTotal += val;
        });

        this.$('#grand_total').val(grandTotal.toFixed(2));
    },
    _TransferCash: function (ev) {
        const selectedCounterId = this.$('#counter').val();
        const CashInHand = this.$('#cash_in_hand').val();
        const LoggedUser = this.$('#person').val();

        $('#from_counter').val(selectedCounterId);
        $('#transfer_cash_in_hand').val(CashInHand);
        $('#logged_user').val(LoggedUser);

    },
    _CashDenominationSubmit: function (ev) {
        ev.preventDefault();
        const cashInHand = parseFloat(this.$('#cash_in_hand').val()) || 0;
        const grandTotal = parseFloat(this.$('#grand_total').val()) || 0;


        if (grandTotal !== cashInHand) {
            $('#validation-modal').modal('show');
            return;
        }

        $('#success-modal').modal('show');

        $('#success-modal').one('hidden.bs.modal', () => {
            this.$('#cash_denomination_form')[0].submit();
        });
    },
    _checkTransferSuccess: function () {
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('transfer_success') === '1') {
            $('#transfer-success-modal').modal('show');

            const newUrl = window.location.pathname;
            window.history.replaceState({}, document.title, newUrl);
        }
    },

    _checkSameCounterError: function () {
        const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('same_counter_error') === '1') {
        $('#same-counter-modal').modal('show');

            const newUrl = window.location.pathname;
            window.history.replaceState({}, document.title, newUrl);
        }
    },

    _checkInsufficientCash: function () {
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('insufficient_cash') === '1') {
            $('#insufficient-cash-modal').modal('show');
            const newUrl = window.location.pathname;
            window.history.replaceState({}, document.title, newUrl);
        }
    },

});

