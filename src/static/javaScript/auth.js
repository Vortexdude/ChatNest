

async function registerUser(event) {
    var alert_element = document.getElementById("alert_message");
    var html = '<div class="alert alert-success alert-dismissible fade show" role="alert">User Registered successfully <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'

    var user_email = document.getElementById("email")
    var user_username = document.getElementById("username")
    var user_password = document.getElementById("password")

    response = await fetch("/api/v1/users", {
        method: "POST",
        body: JSON.stringify({
            username: user_username.value,
            email: user_email.value,
            password: user_password.value
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
            "accept": "application/json"
        }
    })
    if (response.status != 201) {
        alert_element.innerHTML = '<div class="alert alert-danger alert-dismissible fade show" role="alert">User already exists <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    }
    else {
        alert_element.innerHTML = html
    }
}

document.getElementById('loginForm').addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Get the username and password values
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        var alert_element = document.getElementById("alert_message");
        var html = '<div class="alert alert-success alert-dismissible fade show" role="alert">Successfully logged In. <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
        try {
            // Send a POST request to the server
            const response = await fetch('/api/v1/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password })
            });

            // Check if the request was successful
            if (!response.ok) {
                alert_element.innerHTML = '<div class="alert alert-danger alert-dismissible fade show" role="alert">Invalid user <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>';
            }
            else {
                alert_element.innerHTML = html;
            }

            // Parse the JSON response
            const data = await response.json();

            // Log the access token or handle successful login
            localStorage.setItem('accessToken', data.access_token);

        } catch (error) {
            // Handle any errors
            console.error('Error:', error);
        }
    });
