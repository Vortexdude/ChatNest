

async function registerUser(event) {
    var alert_element = document.getElementById("alert_message");
    var html = '<div class="alert alert-success" role="alert">User Registered successfully</div>'

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
        alert_element.innerHTML = '<div class="alert alert-danger" role="alert">User already exists</div>'
    }
    else {
        alert_element.innerHTML = html
    }
}

async function loginUser(event) {

    var user_email = document.getElementById("email")
    var user_password = document.getElementById("password")

    var options = {
        method: 'POST',
        headers: {
            "Content-type": "application/json; charset=UTF-8",
            "accept": "application/json"
        },
        body: JSON.stringify({
            email: user_email.value,
            password: user_password.value
        })
    }

    response = await fetch("/api/v1/login", options)
    if (!response.ok){
        console.log("Error to fetch the data")
    }
    else {
        console.log(response.json())
    }
}
