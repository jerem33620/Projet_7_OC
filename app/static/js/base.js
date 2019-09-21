function scrollBottom(){
    let inputBox = document.getElementsByClassName('inputBox')[0];
    inputBox.scrollIntoView();
}

function createChatRobot(content){
    let addToChatBox = document.createElement('div');
    let addText = document.createElement('p');
    addToChatBox.setAttribute('class', 'chatRobot');
    document.querySelector('.chatDiscussion').appendChild(addToChatBox);
    addText.textContent = content;
    addToChatBox.appendChild(addText);
    scrollBottom();
}

function createChatFriend(content, wikipedia, url){
    let addToChatBox = document.createElement('div');
    let addText = document.createElement('p');
    let map = document.createElement('div');
    let wikipediaElt = document.createElement('p');
    let wikipediaUrl = document.createElement('a');
    wikipediaUrl.href = url;
    wikipediaUrl.textContent = " En savoir plus..."
    wikipediaElt.textContent = wikipedia;
    map.classList.add('map');
    addToChatBox.setAttribute('class', 'chatFriend');
    document.querySelector('.chatDiscussion').appendChild(addToChatBox);
    addText.textContent = content;
    addToChatBox.appendChild(addText);
    addToChatBox.appendChild(map);
    addToChatBox.appendChild(wikipediaElt);
    wikipediaElt.appendChild(wikipediaUrl);
    scrollBottom();
}

function initMap(latitude, longitude) {
    let myLatLng = {lat: latitude, lng: longitude};

    let maps = document.querySelectorAll('.map');
    let map = new google.maps.Map (maps[maps.length - 1], {
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
let addRobot = 1;
let form = document.querySelector("#main-form");
form.addEventListener("submit", function (e) {
    e.preventDefault();
    let question = {
        question: "Où se trouve Paris?"
    };
    let data = new FormData(form);
    let content = document.getElementById('data');
    ajaxPost(window.location.href + "question", data, function (reponse) {
        let rechercheLocal = JSON.parse(reponse);
        console.log(rechercheLocal);
        let returnAdress = rechercheLocal.grandpy + rechercheLocal.gmaps.address
        createChatFriend(content.value, rechercheLocal.wikip, rechercheLocal.wikip_url);
        createChatRobot(returnAdress, addRobot);
        addRobot++;
        initMap(rechercheLocal.gmaps.latitude, rechercheLocal.gmaps.longitude)
    });
})