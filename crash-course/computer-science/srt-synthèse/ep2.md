# Informatique électronique

Le chapitre précedent nous a mené au début du 20ème siècle, à l'époque où des appareils de calcul spécialisés, comme les machines à tabulation, étaient une grande aubaine pour les gouvernements et le commerce ; aidant et parfois remplaçant des tâches manuelles. Cependant l'importance des systèmes humains continua sa progression à une vitesse sans précédent. La première moitié du 20ème siècle vue la population mondiale presque doubler. La 1ère Guerre Mondiale mobilisa 70 millions de personnes, et la 2ème Guerre Mondiale plus de 100 millions. Le commerce global et les réseaux de transports devinrent interconnectés comme jamais auparavant, et la sophistication de l'ingénierie et des recherches scientifiques atteignit de nouveaux sommets ; on commença même à envisager sérieusement à visiter d'autres planètes.

Dés lors, ce fut une explosion de complexité, de bureaucratie et finalement de données, qui conduisit à l'augmentation des besoins d'automatisation et de calcul. Bientôt, les ordinateurs électro-mécaniques de la taille d'une armoire occupèrent d'immenses salles et devinrent coûteux à entretenir et sujet aux erreurs. C'est pourtant ces machines qui allait poser les bases des innovations futures.

## Le Harvard Mark I & les relais

L'un des plus grands ordinateurs électro-mécaniques construit fut le Harvard Mark I, terminé en 1944 par IBM pour les Alliés durant la 2ème Guerre Mondiale.
Il contenait 765 000 composants, 3 millions de connexions et plus de 800km de câbles. Pour conserver la synchronisation de ses mécaniques internes, on utilisait un arbre à cames directement à travers la machine piloté par un moteur de 50 chevaux.

L'une des premières utilisation de cette technologie fut de faire tourner des simulations pour le Projet Manhattan. Les cerveaux de ces immenses monstres électro-mécaniques étaient des relais (interrupteurs mécaniques contrôlés électriquement).
Dans un relais, il y a un fil de contrôle qui détermine si le circuit est ouvert ou fermé. Ce fil de contrôle est connecté à une bobine à l'intérieur du relais. Quand le courant passe à travers la bobine, un champs électromagnétique se créé et attire le bras métallique à l'intérieur du relais en le claquant rapidement pour fermer le circuit. Un relais fonctionne un peu comme un robinet. Le fil de contrôle fonctionne comme la poignée. Ouvrez le robinet et l'eau circule à travers le tuyau. Fermez-le et le flux s'arrête.

Les relais fonctionnent de la même manière, mais avec des électrons à la place de l'eau. Le circuit de contrôle peut alors connecter d'autres circuits, ou quelque chose comme des moteurs, ce qui peut incrémenter le compteur d'un rouage, comme sur la machine à tabulation de Hollerith dont nous avons parler au dernier épisode. Malheureusement, le bras mécanique dans un relais a une masse, et ne passe donc pas instantanément d'un état ouvert à fermé.

Un bon relais dans les années 40 était capable de passer de l'un à l'autre 50 fois par seconde. Ça peut paraître rapide, mais pas assez pour résoudre des gros problèmes complexes. Le Harvard Mark I était capable de faire 3 additions ou soustractions par seconde; les multiplications prenaient 6s et les divisions 15s. Et les opérations plus complexes, comme une fonction trigonométrique, pouvait prendre plus d'une minute.

En plus d'une vitesse de commutation lente, l'autre limitation était l'usure normale de l'appareil. Tout ce qui est mécanique s'use avec le temps. Certaines choses cassent, d'autres se grippent, ralentissent et ne sont plus fiables. Et plus le nombre de relais augmentent, plus la probabilité de défaillance augmente. Le Harvard Mark I avait à peu près 3500 relais. Même en considérant qu'un relais a une durée de vie de 10 ans, cela signifiait de devoir remplacer en moyenne un relais défaillant par jour! C'est un gros problème quand on est en plein milieu d'un calcul important s'étalant sur plusieurs jours.
Et ce n'est pas les seuls problèmes rencontrés par les ingénieurs. Ces immenses machine sombres et chaudes attiraient aussi les insectes. En septembre 1947, les opérateurs du Harvard Mark II retirèrent une mite morte d'un relais défaillant. Grace Hopper, dont nous parlerons plus tard, faisait remarquer *"Dés lors, chaque fois que quelque chose allait mal avec un ordinateur, nous disions qu'il avait des bugs."* Et c'est de là que vient le *bug* informatique.

## ?

Il était clair qu'une alternative aux relais électro-mécaniques, plus rapide et fiable, était nécessaire si l'on voulait faire avancer l'informatique et, heureusement, l'alternative existait déjà !

En effet, en 1904 , le physicien John Ambrose Fleming développa un nouveau composant électrique appelé une valve thermo-ionique, composée de deux électrodes à l'intérieur d'une ampoule hermétique ; il s'agissait du premier tube sous vide.
L'une des électrodes était chauffée, ce qui provoquait l'émission d'électrons ; un procédé appelé émission thermo-ionique. L'autre électrode attirait alors les électrons pour créer un courant dans notre robinet électrique, mais seulement si elle était chargée positivement, si elle était chargée négativement ou était neutre, les électrons n'étaient plus attirés à travers le vide et donc le courant ne passait plus.

Un composant électronique permettant de ne faire passer le courant que dans un sens s'appelle un diode, mais ce dont on avait besoins c'était d'un interrupteur pour ouvrir ou fermer le courant. Par chance, peu après, en 1906, l'inventeur étasunien Lee de Forest ajouta une 3ème électrode de "contrôle" entre les deux électrodes du modèle de Fleming.
En appliquant une charge positive sur l'électrode de contrôle, on permettait au courant de passer. Mais si l'électrode de contrôle était chargée négativement, le courant ne passait plus. Donc en manipulant le fil de contrôle, on pouvait ouvrir ou fermer un circuit.

C'est presque identique à un relais, sauf que justement les tube sous vide n'ont aucun élément mobile. Ce qui signifie moins d'usure, et surtout qu'il peuvent commuter des centaines de fois par seconde.
Ces tubes sous vide triodes deviendront l'élément de base de la radio, du téléphone longue distance, et de plein d'autres appareils électroniques durant près d'un demi-siècle.
Précisons que les tubes sous vide n'étaient pas parfait, il sont plutôt fragiles, et peuvent brûler comme des ampoules, mais ils sont une importante amélioration par rapport aux relais mécaniques. De plus, les tubes sou vide étaient coûteux ; un poste radio n'en avait généralement qu'un, mais un ordinateur pouvait nécessiter des centaines ou des milliers d'interrupteurs électriques.

Mais dés les années 40, leur coût et fiabilité s'était amélioré au point qu'on pouvait en fabriquer pour les ordinateurs... à condition d'en avoir les moyens comme les gouvernements. Ceci marqua le basculement de l'informatique électro-mécanique à l'électronique.
Allons voir ça dans la Thought Bubble.

## ??

La première utilisation à grande échelle des tubes sous vide dans l'informatique fut dans le Colossus Mk 1, conçu par l'ingénieur Tommy Flowers et terminé en décembre 1943. Le Colossus fut installé à Bletchley Park aux Royaumes-Unis et aida à déchiffrer les communication nazies.

A noter que, deux ans plus tôt, Alan Turing (le boss), avait créé un appareil électro-mécanique, également à Bletchley Park, mais appelée la Bombe. C'était une machine électro-mécanique conçue pour casse les codes Enigma nazis, cependant la Bombe n'était pas techniquement un ordinateur, et nous reviendrons sur les contributions d'Alan Turing plus tard.

La première version de Colossus, contenait 1600 tubes sous vide, et on construisit au total 10 Colossi pour aider au cassage de code.
Colossus est vu comme le premier ordinateur électronique et programmable. La programmation se faisait en branchant des centaines de câbles dans des tableaux de bord, un peu comme les vieille table de commutation téléphonique, afin d'initialiser l'ordinateur afin qu'il réalise les bonnes opérations.
Donc même "programmable", il était nécessaire de le configurer pour effectuer des calculs spécifiques.

**Illustration**
Voici l'Ectronic Numerical Integrator and Calculator (ENIAC) terminé quelques années plus tard en 1946 à l'Université de Pennsylvanie. Conçu par John Mauchly et J. Presper Eckert, il s'agissait du premier ordinateur générique au monde programmable et électronique.
ENIAC pouvait effectuer 5000 additions ou soustractions à 10 chiffres par seconde, bien plus rapidement que n'importe quelle machine auparavant. Il fut opérationnel pendant 10 ans, et on estime qu'il a réalisé plus d'arithmétique que l'espèce humaine jusqu'alors.

Cependant, avec d'aussi nombreux  tubes sous vides, les défaillances étaient communes, et ENIAC n'étaient généralement opérationnel qu'une demi-journée à l'époque avant de s'arrêter.

À partir des années 50, même les ordinateurs à base de tubes sous vide atteignaient leurs limites.

Afin de réduire le coût et la taille, ainsi qu'améliorer la fiabilité et la rapidité, un nouvel interrupteur électronique serait nécessaire.
En 1947, les scientifiques des laboratoires Bell John Bardeen, Walter Brattain, et Wiliam Shockley inventèrent le transistor, et grâce à lui, une toute nouvelle ère de l'informatique était née !

Les principes physiques utilisés par les transistors sont assez complexes, et s'appuient sur la mécanique quantique, donc on va rester sur les fondamentaux.
Un transistor n'est jamais qu'un relais ou un tube sous vide, c'est un interrupteur qui peut s'ouvrir ou se fermer lorsqu'on applique un courant électrique sur son fil de contrôle. Typiquement, les transistors ont deux électrodes séparées par un matériau qui parfois conduit l'électricité, parfois résiste au courant ; un semi-conducteur. Ici, le fil de contrôle est connecté à l'électrode appelée la "grille". En changeant la charge électrique de la grille, la conductivité du matériau semi-conducteur peut être manipulé, autorisant le courant à passer ou non comme avec l'analogie du robinet vu ci-dessus. Même les tout premiers transistors des labos Bell furent exceptionnellement prometteurs, ils pouvaient commuter 10 000 fois par seconde.

De plus, à la différence des tubes sous vide fait en verre et contenant des composants fragiles et suspendus les transistors étaient faits de matériaux solides appelés composants à semi-conducteur. Presque immédiatement, les transistors furent fabriqués encore plus petit que les plus petits des relais ou tubes sous vide. Ce qui amena à des ordinateurs plus compacts et moins chers comme l'IBM 608 sorti en 1957, le premier ordinateur composé uniquement de transistors et disponible commercialement. Il contenait 3000 transistors et pouvait réaliser 4500 additions, ou à peu près 80 multiplications ou divisions chaque seconde.
IBM fit rapidement évoluer sa gamme de produits vers les transistors, apportant les ordinateurs à base transistor dans les bureaux et, enfin, dans les maisons. 

Aujourd'hui, les ordinateur utilisent des transistors plus petits que 50 nanomètres ; sachant pour comparaison qu'une feuille de papier a une épaisseur d'à peu près 100 000 nanomètres. Et ils ne sont pas seulement incroyablement petits, ils sont super rapide, ils peuvent changer d'état des millions de fois par seconde, et peuvent tourner pendant des décennies.

Une bonne partie du développement de ces transistors et semi-conducteurs se passe dans la vallée de Santa Clara entre San Francisco et San Jose, Californie. Comme l'élément le plus communément utilisé pour les semi-conducteurs est le silicone, la région fut connue rapidement sous le nom de Silicon Valley. Même William Shockley a déménagé là-bas, pour fonder Shockley Semiconductor, dont les employés fondèrent plus tard Fairchild Semiconductors dont les employés fondèrent plus tard Intel ; le plus large fabriquant mondial de puce informatique aujourd'hui.

Ok, nous avons vus les relais, les tubes sous vide et les transistors. Nous pouvons ouvrir ou fermer le courant très très rapidement. Mais comment passe-t-on d'un transistor à calculer quelque chose, particulièrement sans moteurs ou rouages?

C'est ce que nous allons voir par la suite...
