const API_BASE = "http://127.0.0.1:5000/api";

function loadBeneficiaries() {
  fetch(`${API_BASE}/beneficiaries/`)
    .then((res) => res.json())
    .then((data) => {
      const tbody = document.querySelector("#beneficiaryTable tbody");
      tbody.innerHTML = "";

      data.forEach((b) => {
        let actionBtn = "";

        if (b.scheme_name === "Pension" && b.status === "Pending") {
            actionBtn = `<button onclick="autoDeliver(${b.beneficiary_id})">Deliver</button>`;
        } else {
            actionBtn = "—";
        }

        tbody.innerHTML += `
                    <tr>
                        <td>${b.beneficiary_id}</td>
                        <td>${b.name}</td>
                        <td>${b.scheme_name}</td>
                        <td>${b.amount}</td>
                        <td>${b.status}</td>
                        <td>${actionBtn}</td>
                    </tr>
                `;
      });
    });
}

function deliverPension() {
  const id = document.getElementById("beneficiaryId").value;
  const date = document.getElementById("deliveryDate").value;

  fetch(`${API_BASE}/pension/deliver`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      beneficiary_id: id,
      delivery_date: date,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      alert(data.message);
      loadBeneficiaries();
    });
}

function saveSchedule() {
  const option = document.getElementById("scheduleOption").value;

  fetch(`${API_BASE}/pension/schedule`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ delivery_day: option })
  })
  .then(res => res.json())
  .then(data => alert(data.message));
}

function uploadExcel() {
  const fileInput = document.getElementById("excelFile");
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  fetch(`${API_BASE}/beneficiaries/upload`, {
    method: "POST",
    body: formData
  })
  .then(res => res.json())
  .then(data => alert(data.message));
}

function autoDeliver(id) {
    fetch(`${API_BASE}/pension/deliver`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            beneficiary_id: id,
            delivery_date: new Date().toISOString().split("T")[0]
        })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}

// Auto refresh every 5 seconds
setInterval(() => {
    loadBeneficiaries();
}, 5000);
