# Lab 6.2 – Architecture réseau à trois niveaux

## Objectif
Mettre en place une architecture Docker composée d'un proxy, d'une application et d'une base de données, en utilisant deux réseaux séparés.

## Architecture

- **Proxy :** Nginx 1.27 Alpine (`proxy62`), connecté au réseau `frontend`.
- **Application :** conteneur `app62`, connecté aux réseaux `frontend` et `backend`.
- **Base de données :** PostgreSQL 16 Alpine (`db62`), connecté au réseau `backend`.
- **Réseau frontend :** réseau bridge personnalisé.
- **Réseau backend :** réseau interne créé avec `--internal`.
- **Volume :** `pgdata-reseau-62`.

## Conteneurs et réseaux

| Conteneur | Réseau |
|---|---|
| proxy62 | frontend |
| app62 | frontend et backend |
| db62 | backend |

## Publication des ports

Seul le proxy publie un port sur l'hôte :

`127.0.0.1:8080 -> 80/tcp`

Les conteneurs `app62` et `db62` ne publient aucun port sur l'hôte.

## Tests effectués

1. Accès à Nginx avec `curl http://localhost:8080` : réussi.
2. Communication entre `proxy62` et `app62` : réussie.
3. Résolution de `db62` depuis `proxy62` : impossible, comme attendu.
4. Connexion PostgreSQL depuis `app62` vers `db62` avec `pg_isready` : réussie.
5. Résolution de `proxy62` depuis `db62` : impossible, comme attendu.
6. Accès Internet depuis `db62` : impossible.
7. Accès Internet depuis `proxy62` : réussi.

## Schéma de l'architecture

```mermaid
flowchart TB
    Client["Hôte Ubuntu - port 8080"]
    Proxy["proxy62 - Nginx"]
    App["app62 - Application"]
    DB[("db62 - PostgreSQL")]

    Client --> Proxy
    Proxy <--> App
    App --> DB
