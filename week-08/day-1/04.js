// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake

// ***********************Aircrafts**************************

function Aircraft(type) {
  if (type === 'F-35') {
    this.type = 'F-35';
    this.maxAmmo = 12;
    this.baseDamage = 50;
  } else {
    this.type = 'F-16';
    this.maxAmmo = 8;
    this.baseDamage = 30;
  }
  this.ammo = 0;
}

Aircraft.prototype.allDamage = function () {
  return this.baseDamage * this.ammo;
};

Aircraft.prototype.status = function () {
  console.log('Type  %s, Ammo: %d, Base Damage: %d, All Damage: %d',
   this.type, this.ammo, this.baseDamage, this.allDamage());
};

Aircraft.prototype.fight = function () {
  damage = this.ammo * this.baseDamage;
  this.ammo = 0;
  return damage;
};

Aircraft.prototype.refill = function (ammo) {

  this.ammo += ammo;
  var ammoBack = 0;
  if (this.maxAmmo < this.ammo) {
    ammoBack = this.ammo - this.maxAmmo;
    this.ammo = this.maxAmmo;
  }
  return ammoBack;
};

// ***********************Carriers****************************

function Carrier(ammo) {
  this.aircrafts = [];
  this.totalAmmo = ammo;
  this.healthPoints = 3000;
}

Carrier.prototype.status_report = function () {
  if (this.healthPoints < 1) {
    return "It's dead Jim, :(";
  }
  console.log('\nAircraft count: %d, Ammo Storage: %d, Total damage: %d, Health Remaining: %d',
   this.aircrafts.length, this.totalAmmo, this.aircrafts.reduce(
     function(a, e) {return a + e.allDamage();}, 0), this.healthPoints);
  this.aircrafts.forEach(function(e) {e.status();});
};

Carrier.prototype.add_aircraft = function (aircraft) {
  this.aircrafts.push(aircraft);
};

Carrier.prototype.fill = function () {
  if (this.totalAmmo === 0){
      throw Error('Oh, keine Munition!');
  }
  this.aircrafts.forEach(function (e) {
    this.totalAmmo = e.refill(this.totalAmmo);}, this);
};

Carrier.prototype.fight = function () {
  return this.aircrafts.reduce(function(a, e) {
    return a + e.fight();
  }, 0);
};


var plane1 = new Aircraft('F16');
var plane2 = new Aircraft('F16');
var carrier = new Carrier(100);
carrier.add_aircraft(plane1);
carrier.add_aircraft(plane2);
carrier.status_report();
carrier.fill();
carrier.status_report();
carrier.fight();
carrier.fight();
carrier.status_report();
carrier.status_report();
