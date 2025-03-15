function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    let chatLog = document.getElementById("chat-log");

    if (userInput.trim() !== "") {
        chatLog.innerHTML += "<p>You: " + userInput + "</p>";
        document.getElementById("user-input").value = "";

        // Here we will eventually send the message to Python and get a response.
        // For now, let's add a simple "echo" response to test.
        chatLog.innerHTML += "<p>SymphathyBot: " + userInput + "</p>";
    }

    // Scroll to the bottom of the chat log
    chatLog.scrollTop = chatLog.scrollHeight;
}
