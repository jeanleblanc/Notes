# Pandoc

## Qu'est ce que pandoc

C'est un convertisseur de document.  
Il va convertir un fichier de texte sous forme de balisage (Ex : Markdown) en un autre (Html ou LaTeX).
En gros, pandoc converti du texte, soit en texte autonome d'un balisage à un autre, soit en texte contenu dans un fichier d'un format de fichier à un autre.

## Installer pandoc

     sudo pacman -S pandoc 

## Convertir un document avec pandoc

1. Invoquer "pandoc" grâce à la commande pandoc. Cela va simplement dire au terminal d'executer le programme pandoc.

2. Specifé le fichier qui doit etre converti, en indiquant le nom de celui-ci (example.txt).

3. Générer une citation à l'aide du fichier bib, avec la comande --bibliographiy examplelibrary.bib. Cela dit deux chose, premierement ça dit a pandoc de parcourir le doc et de trouver les citations academique, ça veut dire qu'il y a des citations qu'on voudrait convertir en texte formaté. Et la deuxieme chose dit que toutes les metas-données necessaire aux citation se trouve dans le fichier "examplelibrary.bib".

4. produire une sortie typographiquement correcte, avec la commande --smart