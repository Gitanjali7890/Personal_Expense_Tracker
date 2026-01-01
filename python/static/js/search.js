// JavaScript code for searching expense by description
(function () {
  const searchInput = document.getElementById('searchDescription');
  const table = document.getElementById('expenseTable');

  if (!searchInput || !table) return;

  const rows = table.getElementsByTagName('tr');

  searchInput.addEventListener('keyup', function () {
    const filter = searchInput.value.toLowerCase();

    // Skip header row
    for (let i = 1; i < rows.length; i++) {
      const descriptionCell = rows[i].getElementsByTagName('td')[4]; // 5th column
      if (descriptionCell) {
        const text = descriptionCell.textContent || descriptionCell.innerText;
        rows[i].style.display = text.toLowerCase().includes(filter)
          ? ''
          : 'none';
      }
    }
  });
})();
