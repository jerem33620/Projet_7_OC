function scrollBottom(){
    let chatBox = document.getElementsByClassName("chatDiscussion")[0];
    chatBox.scrollTop = chatBox.scrollHeight;
}
  
function createChatFriend(content, number){
    let addToChatBox = document.createElement('div');
    let addText = document.createElement('p');
    addToChatBox.setAttribute('class', 'chatFriend');
    document.getElementsByClassName('chatDiscussion')[0].appendChild(addToChatBox);
    addText.textContent = content;
    document.getElementsByClassName('chatFriend')[number].appendChild(addText);
    scrollBottom();
}
  
function createChatRobot(content, number){
    let addToChatBox = document.createElement('div');
    let addText = document.createElement('p');
    addToChatBox.setAttribute('class', 'chatRobot');
    document.getElementsByClassName('chatDiscussion')[0].appendChild(addToChatBox);
    addText.textContent = content;
    document.getElementsByClassName('chatRobot')[number].appendChild(addText);
    scrollBottom();
}

function initMap(latitude, longitude) {
    let myLatLng = {lat: latitude, lng: longitude};

    let maps = document.querySelectorAll('.map')
    let lastmap = maps[maps.length - 1];
    let map = new google.maps.Map(lastmap, {
        zoom: 12,
        center: myLatLng
    });

    let marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'trouvé par grandpy'
    });
}

let addFriend = 0;
let form = document.querySelector("#main-form");
form.addEventListener("submit", function (event) {
    event.preventDefault();
    let question = {
        question: "Salut, où se trouve la tour eiffel?"
    };
    let data = new FormData(form);
    let content = document.getElementById('data');
    createChatFriend(content.value, addFriend);
    addFriend++;

    // Permet d'envoyer l'objet au serveur
    ajaxPost(window.location.href + "question", data,
        function (reponse) {
            response = JSON.parse(response);
            
            createChatFriend(response.content, response.number);
            createChatRobot(response.content, response.number);
            initMap(response.latitude, response.longitude);
    });
})