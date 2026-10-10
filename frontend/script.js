
const button = document.getElementById("helloButton");
const result = document.getElementById("result");

button.addEventListener("click", async () => {
    const response = await fetch("http://127.0.0.1:8000/api/hello");

    const data = await response.json();

    result.textContent = data.message;
});

