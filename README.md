# A Tchoung té
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
> Langue [Yemba](https://fr.wikipedia.org/wiki/Yemba) siginifiant association/groupe en français

L'objectif du projet est de de fédérer les métadonnées de toutes les associations camerounaises de France afin de les rendre plus accessible à la communauté.
 

## Contexte fonctionnel

[Vidéo de présentation](https://peertube.stream/w/qmMMLyMbzAU8HWWAk1LAQJ)


## Contexte technique

Si vous êtes ici, c'est que vous intéressez par un déploiement maison de la solution. Suivez le guide :) !


### Prérequis

* Avoir un minimum de compétence sur le cloud AWS et Terraform
* Avoir les accès admin sur une carte [Gogocarto](https://gogocarto.fr/projects)
* Parcourir les [tutoriels Gogocarto](https://peertube.openstreetmap.fr/c/gogo_tutos/videos)
* Installez localement tous les outils ( scripts `init` et `command` du fichier [.gitpod.yml](.gitpod.yml) **ou** utilisez un environnement de développement déjà prêt à l'emploi sur gitpod :

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/mongulu-cm/tchoung-te)


### Déploiement

* Créez un fichier `.env` à la racine contenant:
  ```
    cd etl/
    touch .env
    echo 'BING_SUBSCRIPTION_KEY=XXXXXXXXXXXXXXXXXX' >> .env
  ```
  
Ensuite, éxécutez les commandes suivantes pour uploader le site web:  
  ```
    pushd infra ; terraform apply && popd
    pushd html ; aws s3 cp html/index.html s3://tchoung-te.mongulu.cm/index.html
  ```

Puis éxécutez les notebooks `filter-cameroon.ipynb` et `enrich-database.ipynb` :
  ```
    cd etl && pipenv pipenv install -r requirements.txt && pipenv install -r requirements-dev.txt --dev
    pipenv shell
    python3 -m ipykernel install --user --name=etl
    jupyter trust filter-cameroon.ipynb && jupyter trust enrich-database.ipynb
    aws s3 cp s3://mongulu-files/enrich_cache.sqlite enrich_cache.sqlite
    jupyter lab
  ```

Enfin utilisez le fichier csv résultat comme source de donnée dans Gogocarto et personnalisez là.
Vous pouvez par exemple définir des icônes par catégorie(objet social) ; les notres étant dans `html/icons`.
> Celles-ci ont été construites à partir de ces icônes de bases https://thenounproject.com/behanzin777/kit/favorites/
## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/billmetangmo"><img src="https://avatars.githubusercontent.com/u/25366207?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bill Metangmo</b></sub></a><br /><a href="https://github.com/mongulu-cm/tchoung-te/commits?author=billmetangmo" title="Code">💻</a> <a href="#data-billmetangmo" title="Data">🔣</a> <a href="#ideas-billmetangmo" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/mongulu-cm/tchoung-te/commits?author=billmetangmo" title="Tests">⚠️</a> <a href="#tutorial-billmetangmo" title="Tutorials">✅</a></td>
    <td align="center"><a href="http://flomint.github.io"><img src="https://avatars.githubusercontent.com/u/33840477?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Flomin TCHAWE</b></sub></a><br /><a href="https://github.com/mongulu-cm/tchoung-te/commits?author=flominT" title="Code">💻</a> <a href="#tutorial-flominT" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/hsiebenou"><img src="https://avatars.githubusercontent.com/u/45689273?v=4?s=100" width="100px;" alt=""/><br /><sub><b>hsiebenou</b></sub></a><br /><a href="#data-hsiebenou" title="Data">🔣</a> <a href="https://github.com/mongulu-cm/tchoung-te/commits?author=hsiebenou" title="Tests">⚠️</a> <a href="#tutorial-hsiebenou" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/fabiolatagne97"><img src="https://avatars.githubusercontent.com/u/60782218?v=4?s=100" width="100px;" alt=""/><br /><sub><b>fabiolatagne97</b></sub></a><br /><a href="#tutorial-fabiolatagne97" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/DimitriTchapmi"><img src="https://avatars.githubusercontent.com/u/15048420?v=4?s=100" width="100px;" alt=""/><br /><sub><b>DimitriTchapmi</b></sub></a><br /><a href="#tutorial-DimitriTchapmi" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/pdjiela"><img src="https://avatars.githubusercontent.com/u/36527810?v=4?s=100" width="100px;" alt=""/><br /><sub><b>pdjiela</b></sub></a><br /><a href="#tutorial-pdjiela" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/GNOKAM"><img src="https://avatars.githubusercontent.com/u/60141878?v=4?s=100" width="100px;" alt=""/><br /><sub><b>GNOKAM</b></sub></a><br /><a href="#tutorial-GNOKAM" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/gttakam"><img src="https://avatars.githubusercontent.com/u/62386113?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ghislain TAKAM</b></sub></a><br /><a href="#tutorial-gttakam" title="Tutorials">✅</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
