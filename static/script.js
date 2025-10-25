async function uploadPDFs() {
  const input = document.getElementById("pdfs");
  const files = input.files;

  if (!files.length) {
    alert("Please upload at least one PDF file.");
    return;
  }

  const formData = new FormData();
  for (let file of files) {
    formData.append("pdfs", file);
  }

  document.getElementById("response").innerText = "Processing PDFs...";

  const res = await fetch("/upload", {
    method: "POST",
    body: formData,
  });

  const data = await res.json();
  document.getElementById("response").innerText = data.message || data.error;
}

async function askQuestion() {
  const question = document.getElementById("question").value;
  if (!question) {
    alert("Enter a question.");
    return;
  }

  document.getElementById("response").innerText = "Thinking...";

  const res = await fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });

  const data = await res.json();
  document.getElementById("response").innerText = data.answer || data.error;
}
