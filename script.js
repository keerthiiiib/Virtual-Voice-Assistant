// Initialize the recognition object for voice commands
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.continuous = true;
recognition.interimResults = true;

let micButton = document.getElementById("micBtn");
let statusText = document.getElementById("statusText");
let outputArea = document.getElementById("output");

// Start listening to the microphone
function startListening() {
    micButton.disabled = true; // Disable button while listening
    statusText.innerHTML = "Listening...";
    
    recognition.start();

    recognition.onresult = function (event) {
        let transcript = event.results[event.results.length - 1][0].transcript;
        console.log("You said: " + transcript);

        // Display the recognized text
        outputArea.innerHTML = `<p>You said: <strong>${transcript}</strong></p>`;
        
        // Process the command after listening is complete
        if (event.results[0].isFinal) {
            processCommand(transcript);
        }
    };

    recognition.onerror = function (event) {
        statusText.innerHTML = "Sorry, I couldn't hear you. Try again.";
        micButton.disabled = false;
    };
}

// Stop listening and process the command
recognition.onend = function() {
    micButton.disabled = false;
    statusText.innerHTML = "What can I assist you with?";
};

// Process the recognized command
function processCommand(command) {
    // Simulate different responses based on command
    if (command.includes("time")) {
        let currentTime = new Date().toLocaleTimeString();
        statusText.innerHTML = `The current time is ${currentTime}`;
    } else if (command.includes("date")) {
        let currentDate = new Date().toLocaleDateString();
        statusText.innerHTML = `Today's date is ${currentDate}`;
    } else if (command.includes("weather")) {
        // You can replace this with an actual weather API call
        statusText.innerHTML = "The weather today is sunny with a temperature of 25°C.";
    } else if (command.includes("joke")) {
        // You can replace this with an actual joke API
        statusText.innerHTML = "Why don't skeletons fight each other? They don't have the guts!";
    } else if (command.includes("open google")) {
        window.open("https://www.google.com", "_blank");
    } else {
        statusText.innerHTML = "Sorry, I didn't catch that. Can you repeat?";
    }
}
