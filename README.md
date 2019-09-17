# Projet_7_OC

## Créez GrandPy bot, le papy robot

Ah, les grands-pères... Je ne sais pas vous, mais le mien connaissait quantité d'histoires. Il me suffisait de lui dire un mot pour le voir parti pendant des heures. "Tu veux l'adresse de la poste ? Ah oui, c'est bien. Mais je t'ai déjà raconté que j'ai aidé à la construire ? C'était en 1974 et..." 😴

Pourtant, j'adore ses récits ! J'ai beaucoup appris et rêvé d'autres contrées en l'écoutant. Voici donc le projet que je vous propose : créer un robot qui vous répondrait comme votre grand-père ! Si vous lui demandez l'adresse d'un lieu, il vous la donnera, certes, mais agrémentée d'un long récit très intéressant. Vous êtes prêt·e ?


## Liens:

- Lien Trello: https://trello.com/b/T42iiXIZ/projet7oc
- Lien github: https://github.com/jerem33620/Projet_7_OC.git
- Adresse URL: https://projet-7-oc.herokuapp.com


### Installer:

Pour installer et faire fonctionner mon projet vous aurez besoin de certains packages et vous aurez besoin de clonner mon projet de github sur votre machine avec git, avec les commandes:

```
- git clone https://github.com/jerem33620/Projet_7_OC.git
```

Puis, pour les packages:

```
- python -m pip install pipenv
- python -m pipenv install googlemaps, flask, requests
```

Sinon, il faut faire:

```
- python -m pip install -r requirements.txt
```


#### API:

Vous aurez aussi besoin de générer 2 API pour faire fonctionner le projet.

Dans le fichier routes.py:

```
- Ligne 11: api_key=os.environ.get('GOOGLE_API_KEY_2')
```

Dans le fichier gomaps.py:

```
- Ligne 10: key=os.getenv("GOOGLE_API_KEY_1")
```

Remplacer les "GOOGLE_API_KEY_1" et "GOOGLE_API_KEY_2" par "VOS_API"


#### Test:

Pour lancer un test, il vous suffit de lancer la commande:

```
- pytest
```

ou

```
- pytest tests.py
```


#### Activer votre projet en local:

Il faudra lancer 2 commandes et vous aurez le projet d'activé.

```
- python -m pipenv shell

- python -m app.routes
```
