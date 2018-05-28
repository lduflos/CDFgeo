$(document).ready(function() {
// Création de la carte à l'id "map"
var map = L.map('map');

// Centrer la vue sur 51.505;-0.09 avec un zoom de 2
map.setView([51.505, -0.09], 2);

// Usage des tuiles de carte d'OpenStreetMap puis ajout à la carte map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Création d'un point aux coordonnées 51.5;-0.09
var point = L.marker([51.5, -0.09]);
// Ajout de ce point à la carte
point.addTo(map);
// Connexion d'un PopUp qui affichera "A pretty CESS3 popup..." qui accepte le HTML
point.bindPopup('A pretty CSS3 popup.<br> Easily customizable.');
// Ouverture automatique du Popup
point.openPopup();
});
