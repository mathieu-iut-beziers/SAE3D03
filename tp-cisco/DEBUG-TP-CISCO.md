# Les TP cisco

<link rel="stylesheet" type="text/css" href="style.css">

### TP1

#### 7.0.3-lab---install-the-csr1000v-vm_fr-FR.pdf

Ici tout vas bien, c'est normal il est en anglais.

### TP2

#### 7.6.3-lab---automated-testing-using-pyats-and-genie_fr-FR.pdf

Ici de meme, tout vas bien le seul probléme etant le code est mal interpreter par le pdf ce qui cause la creation d'espace lors du copier, coller.

### TP3

#### 8.3.5-lab---explore-yang-models_fr-FR.pdf

Ici tout vas bien.

### TP4

#### 8.3.6-lab---use-netconf-to-access-an-ios-xe-device_fr-FR.pdf

Probleme a la page 4, il manque une ">".

![p1](./img/Capture%20d’écran%20du%202023-01-11%2012-57-30.png)

### TP5

#### 8.3.7-lab---use-restconf-to-access-an-ios-xe-device_fr-FR.pdf

Premier probleme page 7, des simples quotes a la place des doubles sont utiliser.

![p7](img/Capture%20d’écran%20du%202023-01-11%2013-02-34.png)

De même page 8.

![p8](./img/Capture%20d’écran%20du%202023-01-11%2013-05-36.png)

De même pages 12.

![p12](./img/Capture%20d’écran%20du%202023-01-11%2013-08-34.png)

Ici, pages 12, headers a été traduit.

![p12](./img/Capture%20d’écran%20du%202023-01-11%2013-10-07.png)

Ici, encore pages 12, il manque des "\\".

![p12](./img/Capture%20d’écran%20du%202023-01-11%2013-11-29.png)

Correction :

```python
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Code d\'état : {} \n Message d\'erreur : {} '.format(resp.status_code, resp.json()))
```
