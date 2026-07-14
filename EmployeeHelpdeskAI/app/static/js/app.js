async function sendPrompt() {

    const chatHistory = document.getElementById("chatHistory");
    const prompt = document.getElementById("prompt").value.trim();
    const model = document.getElementById("model").value;
    const temperature = parseFloat(document.getElementById("temperature").value);

    const sendButton = document.getElementById("sendButton");

    if (!prompt) {
        alert("Please enter a question.");
        return;
    }

    chatHistory.innerHTML += `
        <div class="user-message">
            <strong>👤 You</strong><br>
            ${prompt}
        </div>
    `;

    sendButton.disabled = true;
    sendButton.innerHTML = "⏳ Thinking...";

    chatHistory.innerHTML += `
        <div class="ai-message">
            🤖 <em>Thinking...</em>
        </div>
        `;

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                prompt,
                model,
                temperature
            })

        });

        if (!response.ok) {
            throw new Error("Server returned an error.");
        }

        const data = await response.json();

        chatHistory.innerHTML += `
            <div class="ai-message">
                <strong>🤖 Employee Helpdesk AI</strong><br>
                ${data.response}
            </div>
        `;

        chatHistory.scrollTop = chatHistory.scrollHeight;

    }
    catch (error) {

        chatHistory.innerHTML += `
        <div class="ai-message text-danger">
            ❌ ${error.message}
        </div>
        `;
       
    }
    finally {

        sendButton.disabled = false;
        sendButton.innerHTML = "Send";

    }

}