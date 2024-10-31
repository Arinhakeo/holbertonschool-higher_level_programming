# Projet SQL - Gestion des utilisateurs et des bases de données

## Description

Ce projet a pour but de développer des compétences en SQL, en se concentrant sur la gestion des utilisateurs, la création de bases de données, et l'exécution de requêtes complexes. Les utilisateurs apprendront à créer des utilisateurs MySQL, gérer leurs privilèges, et manipuler des données à travers différentes tables.

## Objectifs d'apprentissage

À la fin de ce projet, vous serez capable d'expliquer sans aide externe :

- Comment créer un nouvel utilisateur MySQL
- Comment gérer les privilèges d'un utilisateur sur une base de données ou une table
- Qu'est-ce qu'une clé primaire (PRIMARY KEY)
- Qu'est-ce qu'une clé étrangère (FOREIGN KEY)
- Comment utiliser les contraintes NOT NULL et UNIQUE
- Comment récupérer des données à partir de plusieurs tables en une seule requête
- Qu'est-ce qu'une sous-requête (subquery)
- Qu'est-ce que les JOIN et UNION

## Environnement

- **Système d'exploitation** : Ubuntu 20.04 LTS
- **Version de MySQL** : 8.0.25
- **Éditeurs autorisés** : vi, vim, emacs

## Tâches réalisées

1. **My privileges!** - Script qui liste tous les privilèges des utilisateurs MySQL `user_0d_1` et `user_0d_2`.
2. **Root user** - Création de l'utilisateur MySQL `user_0d_1` avec tous les privilèges.
3. **Read user** - Création de la base de données `hbtn_0d_2` et de l'utilisateur `user_0d_2` avec des privilèges de lecture.
4. **Always a name** - Création de la table `force_name` avec des contraintes appropriées.
5. **ID can't be null** - Création de la table `id_not_null` avec une valeur par défaut pour l'ID.
6. **Unique ID** - Création de la table `unique_id` avec une contrainte d'unicité sur l'ID.
7. **States table** - Création de la base de données `hbtn_0d_usa` et de la table `states`.
8. **Cities table** - Création de la table `cities` avec une clé étrangère vers la table `states`.
9. **Cities of California** - Liste des villes de Californie sans utiliser JOIN.
10. **Cities by States** - Liste de toutes les villes avec leurs états respectifs.
11. **Genre ID by show** - Liste des shows avec leurs genres respectifs.
12. **Genre ID for all shows** - Liste de tous les shows, incluant ceux sans genre.
13. **No genre** - Liste des shows sans genre.
14. **Number of shows by genre** - Compte des shows par genre.
15. **My genres** - Liste des genres pour le show "Dexter".
16. **Only Comedy** - Liste des shows de comédie.
17. **List shows and genres** - Liste de tous les shows avec leurs genres, incluant NULL pour ceux sans genre.

## Ressources

- [MySQL Documentation](https://dev.mysql.com/doc/)
- [MySQL Cheat Sheet](https://www.mysqltutorial.org/mysql-cheat-sheet/)
- [Normalization and ER Modeling](https://www.guru99.com/database-normalization.html)

