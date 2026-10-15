# Cours : utiliser Git et GitHub dans VS Code

## Objectifs

Apprendre à suivre les versions d’un projet avec Git, connecter un compte GitHub dans VS Code et partager ses changements en ligne.

## 1\. Comprendre les outils

- **Git** enregistre l’historique des modifications sur votre ordinateur.  
- **GitHub** héberge des dépôts Git en ligne et permet de collaborer.  
- **VS Code** fournit une interface graphique et un terminal pour utiliser Git.

## 2\. Installer et configurer Git (chez vous !!!!)

Installez [Git](https://git-scm.com/downloads) et [Visual Studio Code](https://code.visualstudio.com/), puis créez un compte sur [GitHub](https://github.com/) si nécessaire.

Dans VS Code, ouvrez **Terminal \> Nouveau terminal** et vérifiez Git :

```sh
git --version
```

&nbsp;

Configurez le nom et l’adresse e-mail qui seront associés à vos commits :

```sh
git config --global user.name "Votre nom"
git config --global user.email "vous@example.com"
```

&nbsp;

Cette configuration identifie l’auteur des commits ; elle ne connecte pas votre compte GitHub.

## 3\. Connecter GitHub à VS Code

1. Cliquez sur l’icône **Comptes** en bas à gauche de VS Code.  
2. Choisissez **GitHub: Sign in** (ou **Se connecter à GitHub**).  
3. Autorisez l’ouverture du navigateur, connectez-vous à GitHub et autorisez VS Code.  
4. Revenez dans VS Code et vérifiez votre compte dans le menu **Comptes**.

Vous pouvez aussi être invité à vous connecter lorsque vous clonez ou publiez un dépôt. Suivez alors l’authentification dans le navigateur. Ne placez jamais votre mot de passe ni un jeton d’accès dans un fichier du projet.

## 4\. Créer un dépôt Git local

1. Dans VS Code, ouvrez le terminal.  
2. verifiez que vous êtes dans le dossier du projet.  
3. tapez la commande suivante pour initialiser un dépôt Git :

```sh
git init
```

&nbsp;

## 5\. Ajouter des elements au dépôt

Pour suivre un fichier avec Git, il faut l’ajouter au dépôt.&nbsp;

Dans le terminal : git status montre l’état des fichiers. Le fichier est **non suivi** (*untracked*) en rouge, en vert les fichiers **suivis** (*tracked*). ajouter avec `git add` permet d'ajouter tous les fichiers du projet à la zone de staging (zone de préparation) pour le prochain commit.

```sh
git status
git add . #permet d'ajouter tous les fichiers du projet à la zone de staging (zone de préparation) pour le prochain commit.
```
## 6\. Enregistrer des changements

Un **commit** est un instantané enregistré dans l’historique du dépôt. Dans le terminal : `git commit -m "message"` enregistre les changements préparés avec un message descriptif.

```sh
git status
git commit -m "Ajoute le guide de démarrage"
```

&nbsp;

`git status` montre l’état des fichiers. Le commit reste local jusqu’à son envoi sur GitHub.

## 6\. Publier le dépôt sur GitHub

### Avec Github

1. Créez un dépôt (Python pour y deposer vos cours python et tp) vide sur GitHub.

### dans vscode Avec le terminal

Créez un dépôt vide sur GitHub, puis remplacez l’URL ci-dessous par celle de votre dépôt : changer la branche principale en `main` avec `git branch -M main`, puis envoyez le dépôt avec : git push \-u origin main. En terminal :

```sh
git remote add origin https://github.com/VOTRE-NOM/VOTRE-DEPOT.git
git branch -M main
git push -u origin main
```

&nbsp;

`git push` envoie les commits vers GitHub. Suivez les instructions de connexion affichées par VS Code ou le navigateur.

## 7\. Bonnes pratiques

- Faites des commits petits et réguliers, avec des messages précis.  
- Vérifiez les changements et les fichiers préparés avant chaque commit.  
- Ne publiez jamais de mot de passe, clé API, jeton ou donnée confidentielle. Utilisez un fichier `.gitignore` pour exclure les fichiers concernés.  
- Choisissez un dépôt privé si le contenu ne doit pas être public.  
- Consultez l’historique avec `git log --oneline`.

## Exercice pratique

1. Créez un dossier de projet PYTHON et ouvrez-le dans VS Code.  
2. Initialisez Git, créez un `README.md` et enregistrez un premier commit.  
3. Connectez votre compte GitHub et publiez le dépôt en privé.  
4. Modifiez le README, créez un second commit et envoyez-le sur GitHub.  
5. Vérifiez sur le site GitHub que le fichier et les commits sont présents.  
6. refaire les étapes 4 et 5 pour les fichiers python que vous avez créés depuis le début du cours.(copier coller les fichiers dans le dossier TP\_PYTHON, puis les ajouter, commiter et pousser sur GitHub)

## Récapitulatif des commandes

| Commande | Action |
| :---- | :---- |
| `git status` | Consulter l’état du dépôt |
| `git add fichier` | Préparer un fichier |
| `git commit -m "message"` | Enregistrer les changements |
| `git pull` | Récupérer les changements distants |
| `git push` | Envoyer les commits |
| `git log --oneline` | Consulter l’historique |

&nbsp;