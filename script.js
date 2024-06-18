document.getElementById('food-order-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;
    const location = document.getElementById('location').value;
    const restaurant = document.getElementById('restaurant').value;
    const food = document.getElementById('food').value;
    const price = document.getElementById('price').value;

    const orderSummary = `
        <h2>Order Summary</h2>
        <p><strong>Name:</strong> ${name}</p>
        <p><strong>Phone No:</strong> ${phone}</p>
        <p><strong>Location:</strong> ${location}</p>
        <p><strong>Restaurant Name:</strong> ${restaurant}</p>
        <p><strong>Food Name:</strong> ${food}</p>
        <p><strong>Price:</strong> ${price}</p>
    `;

    const orderSummaryDiv = document.getElementById('order-summary');
    orderSummaryDiv.innerHTML = orderSummary;
    orderSummaryDiv.style.display = 'block';
});
