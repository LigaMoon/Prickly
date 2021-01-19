const stripePublicKey = document.querySelector('#id_stripe_public_key').text.slice(1, -1);
const clientSecret = document.querySelector('#id_client_secret').text.slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
const card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (e) {
    const errorDiv = document.querySelector('#card-errors');
    if (e.error) {
        const html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${e.error.message}</span>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';
    }
});


// Handle form submit
const form = document.querySelector('#order-info-form');
const submitButton = document.querySelector('#submit-button');

// On submit, desable the submit button to prevent resubmission
form.addEventListener('submit', function(e) {
    e.preventDefault();
    card.update({ 'disabled': true});
    submitButton.setAttribute('disabled', true);
    $('#order-info-form').fadeToggle(100);
    $('#loading-container').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        // If an error occurs, print out the error message 
        if (result.error) {
            const errorDiv = document.querySelector('#card-errors');
            const html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            errorDiv.innerHTML = html;
            $('#order-info-form').fadeToggle(100);
            $('#loading-container').fadeToggle(100);
            // re-enable the submit button so the user can fix the erron and re-submit
            card.update({ 'disabled': false});
            submitButton.setAttribute('disabled', false);
        } else {
            // otherwise, submit the form with successful status
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
