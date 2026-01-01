// JavaScript code for budget alert feature
let budgetAmount = 0;

const setBudgetBtn = document.getElementById('setBudgetBtn');
const budgetInput = document.getElementById('budgetInput');
const budgetAlert = document.getElementById('budgetAlert');
const table = document.getElementById('expenseTable');

if (setBudgetBtn && budgetInput && budgetAlert && table) {

  // Set budget
  setBudgetBtn.addEventListener('click', () => {
    budgetAmount = parseFloat(budgetInput.value);

    if (isNaN(budgetAmount) || budgetAmount <= 0) {
      alert('Please enter a valid budget amount');
      return;
    }

    checkBudget();
    alert(`Budget set to ₹${budgetAmount}`);
  });

  // Calculate total expense
  function getTotalExpense() {
    const rows = table
      .getElementsByTagName('tbody')[0]
      .getElementsByTagName('tr');

    let total = 0;
    for (let i = 0; i < rows.length; i++) {
      const amountCell = rows[i].getElementsByTagName('td')[2]; // 3rd column
      if (amountCell) {
        let amount = parseFloat(
          amountCell.textContent.replace('₹', '')
        ) || 0;
        total += amount;
      }
    }
    return total;
  }

  // Check budget status
  function checkBudget() {
    const totalExpense = getTotalExpense();
    if (budgetAmount > 0 && totalExpense > budgetAmount) {
      budgetAlert.classList.remove('hidden');
    } else {
      budgetAlert.classList.add('hidden');
    }
  }

  // Optional: live budget check
  budgetInput.addEventListener('input', checkBudget);
}
