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

let addFriend = 0;
let form = document.querySelector("form");
form.addEventListener("submit", function (e) {
    e.preventDefault();
    let question = {
        question: "Salut GrandPy! Est-ce que tu connais l'adresse du musée du louvre à paris ?"
    };
    let data = new FormData(form);
    let content = document.getElementById('data');
    createChatFriend(content.value, addFriend);
    addFriend++;
});
function initMap(latitude, longitude) {
    let myLatLng = {lat: latitude, lng: longitude};

    let map = new google.maps.Map(document.getElementsByClassName('map').pop(), {
        zoom: 12,
        center: myLatLng
    });

    let marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'ici!'
    });
    // Permet d'envoyer l'objet au serveur
    ajaxPost(window.location.href + "/question", question,
        function (reponse) {
        console.log("Je connais bien l'adresse que tu me demandes: " + 
        JSON.parse(question) + " Vois-ci son emplacement!");
        initMap(latitude, longitude);

    });
};