async function loadDashboardData() {
    try {
        const response = await fetch('data/processed/dashboard.json');
        if (!response.ok) {
            throw new Error('Failed to load dashboard data');
        }
        const data = await response.json();
        renderSummary(data.summary);
        renderCharts(data.charts);
        renderTransactions(data.recentTransactions);
    } catch (error) {
        console.error('Error loading dashboard data:', error);
        document.getElementById('summary-stats').innerHTML = 
            '<p>Error loading data. Please run the ETL pipeline first.</p>';
    }
}

function renderSummary(summary) {
    const container = document.getElementById('summary-stats');
    container.innerHTML = `
        <div class="stat-card">
            <h3>Total Transactions</h3>
            <div class="value">${summary.totalTransactions || 0}</div>
        </div>
        <div class="stat-card">
            <h3>Total Amount</h3>
            <div class="value">${formatCurrency(summary.totalAmount || 0)}</div>
        </div>
        <div class="stat-card">
            <h3>Transaction Types</h3>
            <div class="value">${summary.transactionTypes || 0}</div>
        </div>
        <div class="stat-card">
            <h3>Date Range</h3>
            <div class="value" style="font-size: 1rem;">${summary.dateRange || 'N/A'}</div>
        </div>
    `;
}

function renderCharts(chartData) {
    const container = document.getElementById('chart-container');
    container.innerHTML = '<p>Chart visualization will be implemented here.</p>';
}

function renderTransactions(transactions) {
    const tbody = document.getElementById('transactions-body');
    if (!transactions || transactions.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5">No transactions found</td></tr>';
        return;
    }
    
    tbody.innerHTML = transactions.map(tx => `
        <tr>
            <td>${formatDate(tx.date)}</td>
            <td>${tx.name || 'N/A'}</td>
            <td>${formatCurrency(tx.amount)}</td>
            <td>${tx.phone || 'N/A'}</td>
            <td>${tx.category || 'Uncategorized'}</td>
        </tr>
    `).join('');
}

function formatCurrency(amount) {
    if (!amount) return 'N/A';
    return new Intl.NumberFormat('en-RW', {
        style: 'currency',
        currency: 'RWF',
        minimumFractionDigits: 0
    }).format(amount);
}

function formatDate(dateString) {
    if (!dateString) return 'N/A';
    return new Date(dateString).toLocaleDateString();
}

document.addEventListener('DOMContentLoaded', loadDashboardData);

