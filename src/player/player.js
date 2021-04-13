function PlayerInterface(name) {
    this.name = name;
}

function Player(name) {
    this.name = name;
}

Player.prototype = new PlayerInterface();

function Bot() {
    this.name = 'AI';
}

Bot.prototype = new PlayerInterface();