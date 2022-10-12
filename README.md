![Alt text](https://github.com/molly-muffin/P9_LITReview/blob/1999fd90339998c96009dd2a22ec897284fde6e0/LITReview_app/connexion/static/connexion/logo.png)

# Gestionnaire de demandes de critiques de livres

## Contexte du projet : 
Rencontre avec une entreprise dont l'objectif est de commercialiser un produit permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande


### Le site permet  :
De créer des critiques et demander des critiques de livres.
L'utilisateur s'inscrit, puis peut alors s'abonner à d'autres utilisateurs, voir leurs publications, et gérer les siennes.

Voici les différentes pages du site :

- **La page de connexion**
    L'utilisateur peut se connecter ou s'inscrire avec un nom d'utilisateur et un mot de passe.
- **La page flux**
    Une fois connecté, l'utilisateur peut faire une demande de critique (ticket) ou faire une critique (review).
    Il peut voir ses tickets, ses reviews et celles de ceux à qui il est abonné.
    Il peut répondre aux tickets de ceux à qui il est abonné.
    Il peut voir les reviews de ses propres tickets écrits par les autres utilisateurs, même s'il n'est pas abonné à eux.
    Il ne peut y avoir qu'une seule review par ticket.
- **La page des posts**
    L'utilisateur peut voir, gérer, modifier ou supprimer ses propres publications.
- **La page des abonnements**
    C'est ici que l'utilisateur peut rechercher le nom des personnes qu'il souhaite suivre.
    Il peut voir le nom des personnes qu'il suit déjà et le nom de ceux qui le suivent .
    Il peut se désabonner de n'importe quelle personne qu'il suit.
- **La page de deconnexion**
    A tout moment, l'utilisateur peut se déconnecter.
    Il sera alors redirigé à la page de connexion.
- **La page d'administration**
    Si vous vous connectez en tant qu'Admin vous serez redirigez vers : http://127.0.0.1:8000/admin, il vous sera alors possible de gérer tickets, reviews et abonnements directement sur l'interface d'administration.

    Le fichier db.sqlite3 déjà présent, contient, pour l'exemple des utilisateurs fictifs qui ont publié plusieurs tickets et reviews. Ils ont également différents abonnements.

    Il y a déjà des utilisateurs fictifs pour tester l'application ils donnent un aperçu clair du fonctionnement de l'application, voici quelques identifiants :
    - Utilisateurs : ``Molly``, ``Coffee``, ``Pito``, ``Hello`` et ``Aloha``
    - Super utilisateur ou administrateur : ``Admin``
    - Ils ont tous le même mot de passe : ``MotDePassword`` 


### Environnement de développement :
`Django`


### Instruction d’installation et d’utilisation :
- Prérequis
    - Dans le terminal, aller dans le dossier ou vous souhaitez placer le projet et copier le projet 
    ```bash
    git clone https://github.com/molly-muffin/P9_LITReview.git
    ```
    - Dans ce dossier
    ```bash
    cd P9_LITReview\LITReview_app\
    ```
    - Créer un environnement virtuel
    ```bash
    python -m venv env
    ```
    - Activer le script
    ```bash
    # Windows :
    .\env\Scripts\activate
    ```
    ```bash
    # Linux :
    source env\bin\activate
    ```
    - Installer les packages dans le requirements.txt
    ```bash
    pip install -r requirements.txt
    ```

- Lancement
    - Lancer le  **serveur local**, avec la commande
    ```bash
    python manage.py runserver
    ```
    - Puis rendez vous sur http://127.0.0.1:8000/ et accéder à la page de connexion du site. Le fichier de données db.sqlite3 sera automatiquement chargé.


### Vérification du code
- Contrôle du code avec **flake8** (avec max lenght à 80), tapez :
```bash
flake8 --max-line-length 150 --format=html --htmldir=flake-report --exclude=migrations
```


> Laureenda Demeule
> OpenClassroom

