# Tasks-List
SPA Tasks List made with Vue, Python, Flask (with local API), MariaDB. Tablet & Desktop only.

Dependencies: Python Virtual Environment, Flask, MariaDB, Axios


![Screenshot of Tasks List on Desktop](https://i.imgur.com/KiXGzUv.png)


# Project Setup
```
cd frontend/tasklist
npm install
npm install axios
```

To run frontend, must be in frontend/tasklist
```
npm run serve
```

# Backend Project Setup
```
cd backend
python -m venv venv
touch dbcred.py
pip install flask
pip install mariadb
```

To run backend, must be in backend folder
```
python -m flask run
```