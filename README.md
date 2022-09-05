## Python Flask Authentication

This repository contains the code used in the Python Flask Authentication [video](https://www.youtube.com/watch?v=71EU8gnZqZQ)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies

##### Windows:
```zsh
pip install -r requirements.txt
```

##### macOS/Linux:
```zsh
pip3 install -r requirements.txt
```

## Usage

##### Windows:
```zsh
python app.py
```
##### macOS/Linux:
```zsh
python3 app.py
```

https://github.com/robsontissiano/python-flask-login-form

## Complexity Level 1, 2, 3, 5 or 8
### What was done, step by step:
* [ * ] Create Flask Project                                      [Base Feature]
* [ * ] Create home route, function and template                  [Base Feature]
* [ * ] Create login route, function and template                 [Base Feature]
* [ * ] Create register route, function and template              [Base Feature]
* [ * ] Add SqLite and SQLAlchemy                                 [Base Feature]
* [ * ] Add User model                                            [Base Feature]
* [ * ] Generated database and tables                             [Base Feature]
* [ * ] Add RegisterForm and validators                           [Base Feature]
* [ * ] Add methods to login and register APIs                    [Login and Register Feature]
* [ * ] Add Forms to login and register templates                 [Login and Register Feature]
* [ * ] Add cryptography to password                              [Login and Register Feature]
* [ * ] Add user register logic to Register API and create user to database  [Register Feature]
* [ * ] Add Login Manager and user loader to actually login the user [Login Feature]
* [ * ] Add dashboard template and login required to its API [Dashboard and Login Required Feature]
* [ * ] Add logic to login user                                    [Login Feature]
* [ * ] Add logout API                                             [Logout Feature]
* [ * ] Add logout button to dashboard                             [Logout Feature]

### Improvements to Do:
* [ * ] Add bootstrap to frontend                                         [LVL 2] [Frontend Feature]
* [ * ] Split validators into a module                                    [LVL 3]
* [ * ] Align the content to center                                       [LVL 2]
* [ * ] Split models into modules                                         [LVL 3]
* [ * ] Split forms into modules                                          [LVL 3]
* [ * ] Add Error treatment to API                                        [LVL 5]
* [   ] Add Unit tests                                                    [LVL 3]
* [   ] Add Error messages to frontend                                    [LVL 3]
* [   ] Use a base template, a header and a footer pattern frontend       [LVL 5]
* [   ] Switch database to postgres                                       [LVL 5]
* [   ] Add Delete user API (soft Delete)                                 [LVL 5]
* [   ] Add Update (patch) user API (soft Delete)                         [LVL 5]
* [   ] Implement MVC architecture                                        [LVL 5]
* [   ] Implement recover password Feature                                [LVL 8]
* [   ]
