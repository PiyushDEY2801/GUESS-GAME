document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("game-form");
    const input = document.getElementById("guess-input");
    const message = document.getElementById("message");

    form.addEventListener("submit", (event) => {
        if (input.value === "") {
            event.preventDefault();
            message.textContent = "Please enter a number!";
            message.style.color = "red";
        }
    });
});
