# RENDU TP1
### Par Lacour Félix et Latifa Lechlech

Lors du premier rendu nous étions perdu et n'avons pas créé de branche rendu_1 ni ce fichier RENDU.md
Pour cette deuxième vague de rendu nous avons ajouté comme prévu la branche rendu_2, mais aussi rendu_1 sans modifier les fichiers.

Pour cette deuxième étape de rendu nous avons commencé par réparer les fonctions kmer2str() et str2kmer()
En ayant pu comparé à la solution, notre stream_kmer ne renvoie pas un vrai stream.

après avoir fix le code et tourné les valeures : 

|                 | GCA_000013265.1 | GCA_000005845.2 | GCA_000069965.1 | GCA_000008865.2 | GCA_030271835.1 |
| :-: | :-: | :-: | :-: | :-: | :-: |
| (1) GCA_000013265.1 | 1.0             | 0.3426          | 0.0010          | 0.3148          | 0.0010 |
| (2) GCA_000005845.2 |                 | 1.0             | 0.0010          | 0.4518          | 0.0010 |
| (3) GCA_000069965.1 |                 |                 | 1.0             | 0.0009          | 0.0280 |
| (4) GCA_000008865.2 |                 |                 |                 | 1.0             | 0.0009 |
| (5) GCA_030271835.1 |                 |                 |                 |                 | 1.0 |

On peut voir que les valeures sont différentes de la solution donné, mais elles restent prochent.
Donc nous arrivont aux mêmes conclusions.
