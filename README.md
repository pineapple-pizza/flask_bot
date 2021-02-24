## the api
- `cd api`
- create a virtual env (`python3 -m venv venv`)
- activate virtual env (`. venv/bin/activate`)
- install dependencies (`pip3 install requirements.txt`)
- `python3 app.py`

## the web app (vue.js)
- `cd client`
- `yarn install`
- to run the vue app : `yarn serve`
- to build the vue app (for prod or deployment purposes) : `yarn build`

## api routes
_can be used seperatly from the front (ex : on postman)_
- `/api/data?query` : 1 query param needed (**query**)
- `/api/map?` : 3 query params needed (**lat**, **lon**, **name** (address))
- `/api/wiki?query` : 1 query param needed (**query**)
- `/api/weather?query` : 1 query param needed (**query**)