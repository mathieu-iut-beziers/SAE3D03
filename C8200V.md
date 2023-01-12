# Catalyst 8200

## pres-catalyst-8000-Cisco

Avant c'etais des 1840...

Le 8200 est un boitier de virtualisation, qui tourne sous centos7, et les vm avec du KVM, prevut pour du edge computing (pour les infra 4/5G, proche de l'IOT,...). Les carte d'extention peuvent parmetre de rajouter de la 5G ou du LoRa. Le routeur que l'on a mis en place est le C8200 qui tourene sous IOS Xe (non monolitic), il permet de gere jusqu'a 3 M de packet/s .

But final metre en place une infrastructure avec des aplication virtualiser.

- Resource BGP et MPLS, but ~2-3 BGP et ~2 MPLS
- SLMP ?
- user = admin ; passd = admin123#
- vmConsole [routeur..] #pour le connecter au routeur

## Network Function Virtualization

- idée est de virtualiser des fonctions réseaux (VNF), couch 4 a 7, routeur, firewall, equilibreurs de charges, antiddos (paquet spoof pour changer les ip sources)
- cette idée fonctionne s'appuie sur des boitier de hyperviseur, sur serveur normarle ou boitier specialiser (catalyst 8200)
- capex et opex, idée du cloud c'est plus de capex c'est que du opex

### SRIOV et catalist

- permet de conecter directement la vm a une carte reseau virtuelle emulé par la nic pphisique, adapté au trafic nord-sud
- dpdk permet le trafic est-ouest
- ovs utilise le frame work dpdk (open v switch)