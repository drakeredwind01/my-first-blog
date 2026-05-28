console.log("Sanity check!");

fetch("/payments/config/")
  .then(result => result.json())
  .then(data => {
    const stripe = Stripe(data.publicKey);

    document.querySelectorAll(".buy-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const productId = btn.dataset.productId;
        btn.disabled = true;
        btn.textContent = "Loading...";

        fetch(`/payments/create-checkout-session/?product_id=${productId}`)
          .then(result => result.json())
          .then(data => {
            if (data.error) {
              alert(data.error);
              btn.disabled = false;
              btn.textContent = "Buy";
              return;
            }
            return stripe.redirectToCheckout({ sessionId: data.sessionId });
          });
      });
    });
  });
