const toggleBtn = document.getElementById("toggleChartBtn");
const chartContainer = document.getElementById("lineChartContainer");

let chartVisible = false;
let lineChart = null;

toggleBtn.addEventListener("click", () => {
    chartVisible = !chartVisible;

    if (chartVisible) {
        chartContainer.classList.remove("hidden");
        toggleBtn.textContent = "❌ Hide Monthly Trend";
        drawLineChart();
    } else {
        chartContainer.classList.add("hidden");
        toggleBtn.textContent = "📈 Show Monthly Trend";
    }
});

function drawLineChart() {
    if (lineChart) return; // prevent redraw

    const ctx = document.getElementById("monthlyLineChart");

    // 🔹 Sample data (replace with backend later)
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"];
    const expenses = [1200, 1800, 1500, 2200, 1900, 2500];

    lineChart = new Chart(ctx, {
        type: "line",
        data: {
            labels: months,
            datasets: [{
                label: "Monthly Expenses (₹)",
                data: expenses,
                borderWidth: 3,
                fill: false,
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: {
                        color: "#ffffff"
                    }
                }
            },
            scales: {
                x: {
                    ticks: { color: "#dcdde1" }
                },
                y: {
                    ticks: { color: "#dcdde1" }
                }
            }
        }
    });
}
