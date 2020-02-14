/**
1) Basic
*/

// Retrieve
var MongoClient = require('mongodb').MongoClient;
// Connect to the db
MongoClient.connect("mongodb://localhost:27017/exampleDb", function(err, db) {
if(err) { return console.dir(err); }
var collection = db.collection('test');
var docs = [{mykey:1}, {mykey:2}, {mykey:3}];
collection.insert(docs, {w:1}, function(err, result) {
collection.find().toArray(function(err, items) {});
var stream = collection.find({mykey:{$ne:2}}).stream();
stream.on("data", function(item) {});
stream.on("end", function() {});
collection.findOne({mykey:1}, function(err, item) {});
});
});
/**
1) SHELL: Inserta mediante Javascript
*/
use master
for (var i = 1; i <= 20; i++) db.restaurants.save({ borough: "Valladolid", name: "La taberna número "+ i});
db.restaurants.find();
it

// Use functional features of JavaScript
function mensaje(elem){ 
	print("Ven a tomar algo a \""+elem.name+"\" recién abierto en "+elem.borough);
	}
db.restaurants.find().forEach(mensaje);
db.restaurants.find({borough: "Manhattan"}).forEach(mensaje);



/**
2)  SHELL: Insertar documento
*/
db.restaurants.insert(
   {
      "address" : {
         "street" : "Paseo de Belén, 13",
         "zipcode" : "47011",
         "building" : "Edificio de Tecnologías de la Información y las Telecomunicaciones",
         "coord" : [ -4.705925,41.662580 ]
      },
      "borough" : "Valladolid",
      "cuisine" : "Estudiantil",
      "grades" : [
         {
            "date" : ISODate("2016-10-01T00:00:00Z"),
            "grade" : "A",
            "score" : 9
         },
         {
            "date" : ISODate("2015-01-16T00:00:00Z"),
            "grade" : "B",
            "score" : 17
         }
      ],
      "name" : "Telecafé",
      "restaurant_id" : "99470114620"
   }
)

/**
3) SHELL: Actualizar registro
*/
db.restaurants.update(
    { "name" : "Telecafé" },
    {
      $set: { "cuisine": "Menú del día" },
      $currentDate: { "lastModified": true }
    }
)

/**
4) SHELL: Actualizar inexistente
*/
db.restaurants.update(
    { "name" : "Telecaféinfo" },
    {
      $set: { "cuisine": "Menú del día" },
      $currentDate: { "lastModified": true }
    },
	upsert: true,
)

/**
5) SHELL: Buscar restaurantes buenos
*/
db.restaurants.find({ "grades.score": {$gt:30,$lt:34}},{"grades.score":true})
/**
6) SHELL: Diversas búsquedas
*/
db.restaurants.find()
db.restaurants.find({"borough": "Valladolid"}).sort({name:-1})
db.restaurants.find({“address.zipcode": “47011"}) .limit(2)
db.restaurants.find({“grades.grade": “C"}).skip(1)
db.restaurants.find({borough: "Brooklyn",cuisine:"Delicatessen"})
db.restaurants.find({$and:[{borough: "Brooklyn"},{cuisine:"Delicatessen"}]}).pretty();

/**
7) SHELL: Búsqda por distancia 2d
*/
db.restaurants.createIndex( { "address.coord" : "2d" } )
db.restaurants.find({ "address.coord":    { $near: [ -4.705925,41.662580 ] } }).limit(2).pretty()
db.restaurants.find( { "address.coord": { $geoWithin: { $centerSphere: [ [  -4.705925,41.662580 ] , 10 / 6378.1 ] } } } )
/**
8) SHELL: Busq por distancia 2dSphere
*/

db.restaurants_geo.createIndex( { "address.coord" : "2dsphere" } )
db.restaurants.aggregate([
    { "$geoNear": {
        "near": {
            "type": "Point",
            "coordinates": [ -4.705925,41.662580 ]
        }, 
        "maxDistance": 1500 * 1000,
        "spherical": true,
        "distanceField": "distance",
        "distanceMultiplier": 0.000621371
    }}
]).pretty()
db.restaurants.find({ location: { $nearSphere: { $geometry: { type: "Point", coordinates: [ -4.705925,41.662580 ] }, $maxDistance: 5000 } } })

/**
9) SHELL: Agregación. REstaurantes por tipo de cocina.
*/
db.restaurants.aggregate([{$group:{ _id: "$cuisine", num_rests: {$sum :1}}}])

/**
10) SHELL: Agregación. Restaurantes por ciudad
*/
db.restaurants.aggregate([{$group:{ _id: "$borough", num_rests: {$sum :1}}}]).pretty()

/**
10) CMD: Importar películas
bin\mongoimport.exe --db master --collection movies --file moviedata.json --jsonArray