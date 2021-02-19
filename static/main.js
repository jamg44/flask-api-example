main().catch(err => console.error('Hubo un error,', err));

async function main() {
  // query the API
  const response = await fetch('/api/transaccion');
  if (!response.ok) throw new Error(response.status) // stop if HTTP-status is not 200-299

  // get the response body in json
  let transacciones = await response.json();

  // get the table body element
  const tbody = document.querySelector(".mi-tabla tbody");

  // append objects to table
  for (const transaccion of transacciones) {
    appendObject(tbody, transaccion);
  }
}

// append tr to table and create td cells for object properties
function appendObject(table, object) {
  const tr = table.insertRow();
  for (const prop in object) {
    tr.insertCell().innerHTML = object[prop];
  }
}
