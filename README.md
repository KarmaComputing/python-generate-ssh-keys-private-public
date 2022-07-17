# How to generate public/private ssh keys using python

See https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
Observe:

> "This is a “Hazardous Materials” module. You should ONLY use it if you’re 100% absolutely sure that you know what you’re doing because this module is full of land mines, dragons, and dinosaurs with laser guns." [cryptography.io](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/)

## Install
```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Run
```
. venv/bin/activate
python main.py
```
