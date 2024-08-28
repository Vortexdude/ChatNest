var client_id = Date.now()
const websocket_host = "192.168.1.76"
const websocket_port = 5000
var websocket_endpoint = `ws://${websocket_host}:${websocket_port}/ws/${client_id}`

document.querySelector("#ws-id").textContent = client_id;
var ws = new WebSocket(websocket_endpoint);
ws.onmessage = function(event) {
    var messages = document.getElementById('messages')
    var message = document.createElement('li')
    var message_span = document.createElement('span')
    var content = document.createTextNode(event.data)
    message_span.appendChild(content)
    message.appendChild(message_span)
    messages.appendChild(message)
};
function sendMessage(event) {
    var input = document.getElementById("messageText")
    ws.send(input.value)
    input.value = ''
    event.preventDefault()
}



async function registerUser(event) {
    const alert_element = document.getElementById("alert_message");
    const alertDiv = document.createElement('div');

    alertDiv.setAttribute('role', 'alert');
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
        alertDiv.className = 'alert alert-danger';
        alertDiv.textContent = "User Already exists";
    }
    else {
        alertDiv.className = 'alert alert-success';
        alertDiv.textContent = 'Register Success!';
    }
    alert_element.appendChild(alertDiv)
}

async function loginUser(event) {

    var user_email = document.getElementById("email")
    var user_password = document.getElementById("password")
    response = await fetch("/api/v1/login", {
        method: "POST",
        body: JSON.stringify({
            email: user_email.value,
            password: user_password.value
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
            "accept": "application/json"
        }
    })
    console.log(response.json())
}