# note video "LES BASES DE GIT (tuto débutant)" de Graven - Développement
 
logiciel permetant de controlé versions projet info
 *exemple* : qq fait un projet J1 > index.html creation
                               J2 > Style.css creation 
                               J3 > il faut travailler avec qq d'autre
                               probleme chiant de transferer, etc.
regler si on utilise git
    J1 il dessite d'utiliser git avec github
    crée un depot git (new repository)
    personne n'a acces a ce depot > crée une copie (git clone)
pret au travail
 J1 > index.html fin de la journé enregistre chagement github
        cd depot
        git add index.html (* > pour tout mettre) > ajoute fichier liste d'attente
        git commit -m "petite note"> boite qui va contenir les changement
        pour envoyer la caisse il faut faire un git push
        
J2 > modifie index.html et ajoute style.css
    il doit faire pareil que hier
    git add -A pour mettre les nv fichier
    puis generer commit

J3 > il doit travailler avec qq d'autre
    faut qu'il ai git et doit faire git clone
    compliquer faut une bonne com
    envoyer push / recuperer pull
    faut comparé pour voir si rien a été supp

analyse de ce qu'il se passe quand les deux personne colabore
push > nvl version du projet sur une ligne temp
sans ecrasé les precedente
on appelle ca une branche (ligne de vie du projet) elle s'appelle master
master = branche final (que ce qu'on doit avoir a la fin)
pour crée une branche (pour le dev d'une app ou autre) git brache dev
pour aller decu git checkout dev
git push --set-upstream origin dev pour envoyer la nvl branche
    DEV =nom de la brache

git fetch
ajouter la branche 

il peuvent crée plusieurs branche pour pouvoir travailler sur le memme projet  enssemble pour 
ne pas modifier la version de l'autre ou pour differente partie du projet (style, code, etc.)
comme ils ont crée plusieurs braches il leur faut a la fin les rassembler
il faut qu'il fasse un git merge pour fusionner leur deux commit en 1 seul pour ensuite le deporter sur le branche de dev
branche dev ok ? evoyer la vers master avec encore un git merge  