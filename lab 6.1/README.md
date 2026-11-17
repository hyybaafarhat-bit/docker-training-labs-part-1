# Lab 6.1 – Réseaux Docker et résolution DNS

## Objectif
Comprendre les réseaux Docker, la communication entre conteneurs, la résolution DNS et l'isolation réseau.

## Travaux réalisés

1. Inspection des réseaux Docker par défaut : bridge, host et none.
2. Création de deux conteneurs sur le réseau bridge par défaut.
3. Vérification de la communication IP entre les conteneurs.
4. Création du réseau personnalisé `reseau-tp`.
5. Déploiement des conteneurs `b1` et `b2` sur ce réseau.
6. Vérification de la résolution DNS avec `ping` et `nslookup`.
7. Déploiement du serveur Nginx `web`.
8. Publication du port `8080` sur l'adresse locale `127.0.0.1`.
9. Connexion et déconnexion d'un conteneur au réseau.
10. Utilisation d'un alias réseau `serveur`.
11. Test d'isolation avec un conteneur utilisant `--network none`.

## Résultats

- La communication entre conteneurs sur un réseau personnalisé fonctionne.
- La résolution DNS Docker fonctionne sur le réseau personnalisé.
- Les réseaux différents assurent l'isolation des conteneurs.
- Un conteneur connecté à plusieurs réseaux peut communiquer avec les membres de ces réseaux.
- Le mode `none` désactive la connectivité réseau externe.

## Conclusion

Ce laboratoire a permis de comprendre les réseaux Docker, la résolution DNS, les alias réseau, la publication des ports et l'isolation des conteneurs.
