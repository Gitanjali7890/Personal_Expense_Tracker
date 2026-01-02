let budgetAmount = 0;

document.addEventListener("DOMContentLoaded", () => {
  const setBudgetBtn = document.getElementById("setBudgetBtn");
  const budgetInput = document.getElementById("budgetInput");
  const budgetAlert = document.getElementById("budgetAlert");
  const table = document.getElementById("expenseTable");

  if (!setBudgetBtn || !budgetInput || !budgetAlert || !table) return;

  // Set budget
  setBudgetBtn.addEventListener("click", () => {
    budgetAmount = parseFloat(budgetInput.value);

    if (isNaN(budgetAmount) || budgetAmount <= 0) {
      alert("Please enter a valid budget amount");
      return;
    }

    checkBudget();
    alert(`Budget set to ₹${budgetAmount}`);
  });

  function getTotalExpense() {
    const rows = table.getElementsByTagName("tr");
    let total = 0;

    // start from 1 to skip header row
    for (let i = 1; i < rows.length; i++) {
      const amountCell = rows[i].getElementsByTagName("td")[2];
      if (amountCell) {
        const amount = parseFloat(
          amountCell.innerText.replace("₹", "").trim()
        );
        if (!isNaN(amount)) total += amount;
      }
    }
    return total;
  }

  function checkBudget() {
    const totalExpense = getTotalExpense();

    if (budgetAmount > 0 && totalExpense > budgetAmount) {
      budgetAlert.style.display = "block";
    } else {
      budgetAlert.style.display = "none";
    }
  }
});
