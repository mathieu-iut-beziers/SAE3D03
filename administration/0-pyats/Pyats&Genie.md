# Pyats & Genie

Au cours des TP cisco on a pu decouvrir Pyats qui est un ecosysteme des test en python.
Genie lui est construi sur Pyats, il est dedier au resaux et pend en compte des protocole comme OSPF et BGP.

## Utilisation

Pour utiliser Genie, il nous faus un fichier yml avec la commance "genie create testbed interactive" :

```yml
devices:
  admin1:
    connections:
      cli:
        ip: 10.202.17.200
        protocol: ssh -o KexAlgorithms=diffie-hellman-group14-sha1
    credentials:
      default:
        password: '%ENC{w5HDncOOw53DocKQwpbCmA==}'
        username: admin1
      enable:
        password: '%ASK{}'
    os: iosxe
    type: iosxe
```

Une foie crée on peut raliser des commande pour par exemple recuperer un interface breaf "genie parse "show ip interface brief" --testbed-file yaml/testbed.yml --devices CSR1kv".

Une partie interesante de Genie est qu'il permet de metre en valeur les diferences entre les configurations (qui on etais au prealable output) cela est possible avec la commande "genie diff".
