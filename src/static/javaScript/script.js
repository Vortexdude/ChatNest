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
