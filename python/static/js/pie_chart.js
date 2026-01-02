document.addEventListener("DOMContentLoaded", function () {

    const btn = document.getElementById("showChartBtn");
    const chartContainer = document.getElementById("chartContainer");
    const dataTag = document.getElementById("category-data");

    let chart = null; // store chart instance
    let isVisible = false;

    btn.addEventListener("click", function () {

        if (isVisible) {
            // HIDE chart
            chartContainer.style.display = "none";
            btn.innerText = "Show Expense Pie Chart";

            if (chart) {
                chart.destroy();
                chart = null;
            }

            isVisible = false;
            return;
        }

        // SHOW chart
        chartContainer.style.display = "block";
        btn.innerText = "Hide Expense Pie Chart";

        const rawData = JSON.parse(dataTag.textContent);

        const labels = [];
        const values = [];

        rawData.forEach(item => {
            labels.push(item.category);
            values.push(item.total_amount < 3000 ? 3000 : item.total_amount);
        });

        const ctx = document.getElementById("expensePieChart").getContext("2d");

        chart = new Chart(ctx, {
            type: "pie",
            data: {
                labels: labels,
                datasets: [{
                    data: values,
                    backgroundColor: [
                        "#ff6384",
                        "#36a2eb",
                        "#ffce56",
                        "#4caf50",
                        "#9c27b0"
                    ]
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: "top"
                    },
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                const realValue = rawData[context.dataIndex].total_amount;
                                return `${context.label}: ₹${realValue}`;
                            }
                        }
                    }
                }
            }
        });

        isVisible = true;
    });
});
