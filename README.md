# Talana-Kombat-JRPG
Software Support Developer Application

## Run dockerized app with

```sh 
source run.sh
```

### or

```sh 
./run.sh
```

***Atention!! If you are using Windows, then you must use git bash to run the script***

## It´s Ready. Now you can play at [Swagger Interface](http://0.0.0.0:8008/docs)

If you send a JSON using the POST method to the /game route like the one shown below, the API will respond with the story of the fight.

```json
{
   "player1":{
      "movimientos":["D", "DSD", "S", "DSD", "SD"],
      "golpes":["K", "P", "", "K", "P"]
   },
   "player2":{
      "movimientos":[ "SA", "SA", "SA", "ASA", "SA"],
      "golpes":["K", "", "K", "P", "P"]
   }
}
```

#### Developed by OsmaniCR