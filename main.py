"""Etude de la suite de Syracuse et de ses différentes caractéristiques"""
#### Fonctions secondaires

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Génère un plot de la suite de Syracuse"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr))) #plutôt que [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')

#######################

def syracuse_sequence(n):
    """Calcule la n+1 ième valeur de la suite de Syracuse de source n"""

    if n % 2 ==0:
        n = n/2
    else :
        n = 3*n+1
    return n


def syracuse_l(n):
    """retourne les valeurs de la suite de Syracuse de source n tant que 1 n'apparaît pas

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    seq = [n]
    while n != 1:
        seq.append(syracuse_sequence(n))
        n = syracuse_sequence(n)
    return seq


def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse de source n

    Args:
        l (list): la suite de Syracuse

    Returns:
        n (int): le temps de vol
    """
    return len(l) - 1

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse de source n

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    i = 1
    while l[i] >= l[0]:
        i += 1
    return i - 1

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse de source n

    Args:
        l (list): la suite de Syracuse

    Returns:
        n (int): l'altitude maximale
    """
    return max(l)

#### Fonction principale


def main():
    """Fait des appels de test"""
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()
