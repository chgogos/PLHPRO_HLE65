# ΠΛΗΠΡΟ 

HLE65

## ΟΣΣ1

## ΟΣΣ2

## ΟΣΣ3

## ΟΣΣ4

## ΟΣΣ5

### 5.1 Παραδείγματα με pyinstaller

Εγκατάσταση pyinstaller

<https://pyinstaller.org/en/stable/usage.html>


**Παραδείγματα**

```
$ pip install pyinstaller
```

Μέσα από τον φάκελο pyinstaller2 στον οποίο βρίσκονται τα αρχεία myapplication.py και weatherdata.xlsx δίνουμε την εντολή:

```
$ pyinstaller --onefile --add-data "weatherdata.xlsx;." myapplication.py
```