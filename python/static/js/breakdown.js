document.addEventListener("DOMContentLoaded", function () {

    // 1️⃣ Get JSON data from script tag
    const dataTag = document.getElementById("category-data");
    const categoryData = JSON.parse(dataTag.textContent);

    // 2️⃣ Get table body
    const tbody = document.getElementById("breakdownBody");

    // 3️⃣ Insert rows
    categoryData.forEach(item => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${item.category}</td>
            <td>₹ ${item.total_amount.toFixed(2)}</td>
        `;

        tbody.appendChild(row);
    });
});
