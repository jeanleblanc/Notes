# Logique booléenne et portes logiques

Nous allons maintenant commencer notre ascension de l'échelle de l'abstraction, où l'on perdra la capacitéde voir chaque interrupteur et rouage, mais où l'on gagnera la possibilité d'assembler des systèmes de plus en plus complexes.

## Le binaire

Ci-dessus, nous avions abordé comment les ordinateurs avaient évolué depuis les appareils électromécanique qui n'avaient souvent qu'une représentation décimale des nombres - représentés par les dents d'un rouage - vers les ordinateurs électroniques utilisant des transistors capables d'éteindre ou d'allumer le courant électrique.

Fort heureusement, même avec seulement 2 états électriques, on peut représenter d'importantes informations. Nous appelons Binaire cette représentation ; ce qui signifie littéralement "à deux états", de la même manière qu'une bicyclette a deux roues ou qu'un bipède a deux jambes.

Vous devez penser que deux états ne sont pas suffisants, et vous auriez raison ! Cependant, c'est exactement ce dont vous avez besoin pour représenter les valeurs "vrai" et "faux".
Dans les ordinateurs, l'état "allumé", quand le courant passe, représente vrai.
L'état "éteint", le courant ne passe pas, représente faux.
On peut aussi écrire le binaire à l'aide de 1 et de 0 au lieux de vrai et faux ; ils ne sont qu'une expression différente d'un même signal.

Ainsi, nous pouvons utiliser les transistors non plus seulement pour laisser passer ou non le courant mais aussi pour autoriser différents niveaux de courant.

Certains anciens ordinateurs électroniques était ternaires, à trois états, voir même quinaires, utilisant 5 états. Le problème est que, plus il y a d'états intermédiaires, plus il est difficile de les différencier ; si votre batterie de téléphone est faible ou qu'il y a des perturbations électriques à cause d'un four à micro-ondes en marche à proximité, les signaux peuvent se mélanger... et ce problème empire avec des transistors changeant d'état des millions de fois par seconde ! Donc, en plaçant deux signaux aussi éloignés que possible - en utilisant seulement "allumé" ou "éteint" - nous permet de mieux distinguer les signaux et de minimiser ces problèmes.

## l'Algèbre de Boole

Une autre raison pour laquelle les ordinateurs utilisent le binaire est qu'une des branches des mathématiques existe déjà et traite justement des valeurs "vrai" et "faux". Elle a d'ailleurs déjà résolu les règles et les opérations nécessaires pour les manipuler. Elle s'appelle l'Algèbre de Boole !

George Boole, qui donna son nom à l'Algèbre de Boole, était un mathématicien autodidacte anglais du 19ème siècle. Il était intéressé dans la représentation logique des assertions qui allaient "sous, sur et au delà" de l'approche Aristotélicienne de la logique, qui était, sans surprise, encrée dans la philosophie. L'approche de Boole permettait de prouver systématiquement et formellement la vérité, grâce aux équations logiques qu'il introduisit dans son premier livre "L'analyse mathématique de la logique" en 1847.

En algèbre "normale" - la classique - les valeurs des variables sont des nombres, et les opérations sur ces nombres peuvent être par exemple les additions et les multiplications. Cependant en Algèbre de Boole, les valeurs des variables sont vraies ou fausses, et les opérations sont logiques.

Il existe 3 opérations fondamentales en Algèbre de Boole : NON, ET, OU.

NON prend une seule valeur booléenne, vrai ou faux, et l'inverse.
Il transforme vrai en faux et faux en vrai.

On peut écrire une petite table logique qui montre les valeurs d'entrées originale, et celles de sorties après l'application de l'opération.
On peut facilement construire une logique booléenne à l'aide de transistors.

Comme vu précedement, les transistors ne sont réellement que des interrupteurs contrôlés électriquement. Ils sont composés de 3 fils : deux électrodes et un fil de contrôle.
**Lorsqu'on applique un courant électrique sur le fil de contrôle, il laisse le courant passer à travers depuis une électrode, à travers le transistor, jusqu'à la seconde électrode.**

C'est un peu comme un robinet sur un tuyau : quand on ouvre le robinet, l'eau s'écoule, quand on le ferme, l'eau s'arrête.

On peut utiliser le fil de contrôle comme une entrée et le fil sortant de l'électrode en bas comme une sortie. Donc avec un seul transistor, nous avons une sortie et une entrée. Si l'on active l'entrée, la sortie est également active car le courant peut passer au travers. Si l'entrée est désactivée, la sortie l'est également et le courant ne passe plus au travers.
Ou en terme booléen, quand l'entrée est vraie, la sortie est vraie. Et quand l'entrée est fausse, la sortie est fausse.
On peut aussi le montrer à l'aide d'une table logique.
Ce n'est pas très intéressant car le circuit ne fait pas grand chose ; l'entrée et la sortie sont identique. Cependant, on peut juste un peu modifier le circuit pour créer un NON.

Au lieu d'avoir le fil de sortie après le transistor, on peut le déplacer avant. Si on active l'entrée, le transistor fait passer le courant vers la "masse", et le fil de sortie ne recevra aucun courant, il sera éteint. Dans notre métaphore avec l'eau, mettre à la masse sera comme si toute l'eau de la maison coulait à travers un gros tuyau afin qu'il n'y ait plus aucune pression pour la douche.

Dans ce cas, si l'entrée est activée, la sortie est inactive.
Lorsqu'on éteint le transistor, en revanche, le courant ne peut plus s'écouler vers la masse et s'écoule donc vers le fil de sortie.
Donc l'entrée est inactive et la sortie est active.

Cela correspond à la table logique du NON, nous venons de construire un circuit qui calcul NON !

Nous les appelons des portes NON (on les appelle des portes car elle contrôle le chemin que prend le courant).

L'opération booléenne ET prend deux entrées mais toujours qu'une seule sortie.
Dans ce cas, la sortie n'est vraie que si les deux entrées sont vraies.

Voyez le comme dire la vérité. Vous n'êtes honnêtes que si vous ne mentez même pas un peu. Par exemple, prenons l'assertion "Mon nom est Jean ET je porte une un t-shirt gris". Ces deux assertions sont vraies, l'ensemble de la proposition est donc vraie.
Mais si je dit "Mon nom est Jean ET je porte un pantalon", ça devient faux.
Parce que je ne porte pas un pantalon...
La partie "Jean" est certes vraie, mais vrai ET faux, c'est toujours faux.
Si je voulais inverser cette assertion, elle serait toujours fausse, et si je voulais vous dire deux mensonges complets, ça serait également faux, et encore une fois on peut écrire toutes ces combinaisons dans la table.

Pour fabriquer une porte ET, nous aurons besoin de deux transistors connectés ensembles afin d'avoir nos deux entrées et une sortie.
Si on active seulement le transistor A, le courant ne passe pas car il est stoppé par le transistor B. Et inversement, si le transistor B est actif mais pas le transistor A, idem, le courant ne passe pas. Le fil de sortie n'a du courant que si le transistor A ET le transistor B son actifs.

La dernière opération booléenne est OU, où une seule des entrées doit être vraie pour que la sortie soit vraie ; c'est un peu l'inverse de ET.

Par exemple "mon nom est Zinnedine Zidanne OU je porte un t-shirt gris".

C'est une assertion vraie car même si je ne suis pas Zinnedine Zidanne, malheureusement, je porte bien un t-shirt gris, donc l'ensemble de la proposition est vraie.
Une assertion OU est également vraie si les deux faits sont vrais.
La seule fois où l'assertion OU est fausse c'est quand les deux entrées sont fausses.

Construire une porte OU à partir de transistors requiert quelques fils supplémentaires. Au lieu d'avoir deux transistors en série - l'un après l'autre - on les mets en parallèle, on connecte la source de courant aux deux transistors, on dessine un petit arc pour noter que les file passe l'un au dessus de l'autre et ne sont pas connectés, même s'ils donnent l'impression de se croiser. Si les deux transistors sont inactifs, le courant ne passe pas vers la sortie donc la sortie est inactive.

Maintenant, si on active juste le transistor A, le courant passe vers sortie. De même si le transistor A est inactif et le transistor B est actif. En clair, si A OU B sont actifs, la sortie est active. De plus, si les deux transistors sont actifs, la sortie est active.

OK, maintenant que nous avons les portes NON, ET, OU et que nous pouvons laisser derrière nous les transistors, les composant et prendre un niveau d'abstraction.

Le standard utilisé par les ingénieurs pour ces portes sont un triangle avec un point pour NON, un D pour le ET, et un vaisseau spatial pour le OU.
Les représenter et y penser de cette manière nous permet de construire des composants encore plus grands tout en gardant la complexité générale relativement identique ; rappelez-vous seulement que ce bazar de fils et de transistors est toujours là.

Par exemple, une autre opération booléenne très utile en informatique est appelé le OU eXclusif, ou XOR pour faire court.
XOR est comme un OU normal mais avec une différence, si les deux entrées sont vraies, XOR est faux. La seule fois où XOR est vraie c'est quand une des entrées est vraie et que l'autre est fausse. C'est comme lorsque vous allez diner et que le repas est accompagné d'une salade OU d'une soupe.malheureusement, vous ne pouvez avoir les deux!

Construire ceci à partir de transistors est assez confus, mais on peut montrer comment un XOR est créé à partir de nos portes booléennes basiques. On sait que nous avons encore deux entrées -A et B - et une sortie. Commençons par une porte OU, vu que la table logique est presque identique à celle du OU. Il n'y a qu'un problème - quand A et B sont vraie, la logique est différente par rapport au OU, et la sortie doit être "fausse".
Pour faire cela, on a besoin de portes supplémentaires.
Si nous ajoutons une porte ET, et que les entrées sont toutes deux vraies, la sortie est vraie.
Ce n'est pas ce qu'on veut. Mais si nous ajoutons un NON, tout de suite après, cette valeurs sera inversée à faux. OK, à présent, si nous ajoutons une porte ET, et que nous connectons cette sortie et celle de notre porte OU original, le ET prendra en entrée vrai et faux et comme ET a besoin des deux entrée à vrai
pour être vraie, sa sortie est fausse.
C'est la première ligne de la table logique.

Si nous essayons les combinaisons d'entrées restantes, on voit que ce circuit logique booléen implémente effectivement un OU exclusif.
XOR s'avère être un composant très utile, et nous y reviendrons, tellement utilise qu'en fait les ingénieurs lui donnèrent son propre symbole : un porte OU avec un sourire :)
Le plus important est que maintenant nous pouvons mettre le XOR dans notre boîte à outil métaphorique et ne plus s'inquiéter des portes logiques qui la constituent, ou des transistors qui font ces portes, ou des électrons qui passent à travers un semi-conducteur. Nous prenons un autre niveau d'abstraction.

Quand les ingénieurs en informatique conçoivent des processeurs, ils travaillent rarement au niveau des transistors, et travaillent plutôt avec des blocs bien plus gros comme les portes logiques ou même des composants bien plus grands composés de portes logiques.
Et même si vous êtes un programmeur informatique professionnel, ce n'est pas souvent que vous réfléchissez à comment la logique que vous programmez est implémentée dans le monde physique par ces minuscules composants.

Nous avons également avancé depuis des signaux électriques bruts vers notre première représentation de données - vrai et faux - et nous avons même eu un avant-goût du calcul informatique. Avec seulement l'aide des portes logiques, nous avons pu construire une machine capable d'évaluer des assertions logiques complexes, comme si "Nom est John Green ET après 17H OU est fin de semaine ET proche de Pizza Hut", alors "John voudra une pizza" égal vrai.
