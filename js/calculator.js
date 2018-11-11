var bank_rates = document.getElementById("bank-rates");
bank_rates.style.display = "none";

function newfinancingCalculator() {
    alert('You are in the new financing calculator');
}

function refinancingCalculator(){
    var loan_amount = document.getElementById('loan_amount').value;
    var interest_rates = document.getElementById('interest_rates').value;
    var loan_tenure = document.getElementById('loan_tenure').value;
    
    var pmt = PMT(interest_rates/100/12, loan_tenure*(12), loan_amount);
    
    var bank_rates = document.getElementById("bank-rates");
    bank_rates.style.display = "block";

    pmt = pmt.toFixed(2)
    document.getElementById('pmt_rate').innerHTML = 'Monthly Payment: $' + pmt;
}

function PMT(rate_per_period, number_of_payments, present_value){
    if(rate_per_period != 0.0){
        // Interest rate exists
        var q = Math.pow(1 + rate_per_period, number_of_payments);
        return (rate_per_period * q * present_value) / ((-1 + q) * (1 + rate_per_period));

    } 

    return 0;
}