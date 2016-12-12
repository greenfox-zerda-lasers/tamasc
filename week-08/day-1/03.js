'use strict';

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)

function Rocket(consumption) {
  this.consumption = consumption;
  this.fuel = 0;
  this.launches = 0;
}

Rocket.prototype.fill = function (amount) {
  this.fuel += amount;
};


Rocket.prototype.launch = function () {
  if (this.fuel > this.consumption) {
    this.fuel -= this.consumption;
    this.launches += 0;
  } else {
    throw RangeError('autsch, Kein Kraftstoff!');
  }
};

var V1 = new Rocket(30);

V1.fill(34);

console.log(V1.fuel);

V1.launch();

console.log(V1.fuel);

V1.launch();
