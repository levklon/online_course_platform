import React from 'react';
import { loadStripe } from '@stripe/stripe-js';
import VideoPlayer from './VideoPlayer';

const stripePromise = loadStripe('your_stripe_publishable_key');

const Checkout = () => {
    const handleCheckout = async () => {
        const stripe = await stripePromise;

        const response = await fetch('/api/create-checkout-session/', {
            method: 'POST',
        });

        const session = await response.json();

        const result = await stripe.redirectToCheckout({
            sessionId: session.id,
        });

        if (result.error) {
            console.error(result.error.message);
        }
    };

    return (
        <button role="link" onClick={handleCheckout}>
            Checkout
        </button>
    );
};

export default Checkout;
