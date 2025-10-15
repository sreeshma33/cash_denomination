console.log("===============1===========================")
odoo.define('cash_denomination.cash_denomination', function (require) {
    "use strict";
    document.addEventListener("DOMContentLoaded", function () {
        const countInputs = document.querySelectorAll("counts-input");
        const grandTotalField = document.getElementById("grand_total");
        const form = document.getElementById("cash_denomination_form");

        function updateTotals() {
            let grandTotal = 0;
            countInputs.forEach(function(input) {
                const currency = parseInt(input.dataset.value) || 0;
                const counts = parseInt(input.value) || 0;
                const total = counts * currency;
                input.closest("tr").querySelector(".total-field").value = total;
                grandTotal += total;
            });
            grandTotalField.value = grandTotal;
        }

        countInputs.forEach(function(input) {
            input.addEventListener("input", updateTotals);
        });

        const today = new Date().toISOString().split('T')[0];
        document.getElementById("date_field").value = today;
        updateTotals();

        form.addEventListener("submit", function(event) {
            let hasValue = false;
            let grandTotal = parseFloat(grandTotalField.value) || 0;
            let cashInHand = parseFloat(document.getElementById("cash_in_hand").value) || 0;

            countInputs.forEach(function(input) {
                if (parseInt(input.value) > 0) {
                    hasValue = true;
                }
            });

            if (!hasValue) {
                event.preventDefault();
                alert("Please enter at least one count before submitting!");
                return;
            }

            if (grandTotal !== cashInHand) {
                event.preventDefault();
                alert("Grand total does not match Cash in Hand! Please correct the counts.");
                return;
            }
        });

        const urlParams = new URLSearchParams(window.location.search);
            if (urlParams.has('transfer_success')) {
                alert("Cash transfer record created successfully!");
                const cleanUrl = window.location.origin + window.location.pathname;
                window.history.replaceState({}, document.title, cleanUrl);
            }
         if (urlParams.has('success')) {
            alert("Cash denomination submitted successfully!");
            const cleanUrl = window.location.origin + window.location.pathname;
            window.history.replaceState({}, document.title, cleanUrl);
        }

        const transferModal = document.getElementById("transfer-modal");
        transferModal.addEventListener("show.bs.modal", function () {
            const selectedCounter = document.getElementById("counter").value;
            document.getElementById("from_counter").value = selectedCounter;
        });
    const counterSelect = document.getElementById("counter");

    counterSelect.addEventListener("change", function() {
        localStorage.setItem("selected_counter_id", this.value);
    });

    const saved = localStorage.getItem("selected_counter_id");
    if (saved) {
        counterSelect.value = saved;
    }

    });

});
