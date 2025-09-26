"""Etude de la suite de Syracuse et de ses différentes caractéristiques"""
#### Fonctions secondaires

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

"""Étude de la suite de Syracuse et utilitaires associés."""

def syracuse_sequence(n: int) -> int:  # pylint: disable=invalid-name
    """Retourne le terme suivant de la suite de Syracuse pour ``n``.

    Règle : si ``n`` est pair → ``n // 2`` ; sinon → ``3 * n + 1``.

    Args:
        n: Entier strictement positif.

    Returns:
        Le terme suivant de la suite (entier).

    Raises:
        TypeError: si ``n`` n'est pas un ``int``.
        ValueError: si ``n`` est < 1.
    """
    if not isinstance(n, int):
        raise TypeError("n doit être un entier (int).")
    if n < 1:
        raise ValueError("n doit être >= 1.")
    return n // 2 if n % 2 == 0 else 3 * n + 1


def syracuse_l(n: int) -> list[int]:  # pylint: disable=invalid-name
    """Construit la suite de Syracuse de source ``n`` jusqu'à 1 (inclus).

    Args:
        n: Entier strictement positif.

    Returns:
        La liste des termes, débutant par ``n`` et se terminant par ``1``.

    Raises:
        TypeError, ValueError: si ``n`` est invalide.
    """
    if not isinstance(n, int):
        raise TypeError("n doit être un entier (int).")
    if n < 1:
        raise ValueError("n doit être >= 1.")

    seq: list[int] = [n]
    while n != 1:
        n = syracuse_sequence(n)
        seq.append(n)
    return seq


def temps_de_vol(l: list[int]) -> int:  # pylint: disable=invalid-name
    """Retourne le temps de vol (nombre d'étapes pour atteindre 1).

    Args:
        l: Suite de Syracuse (liste non vide d'entiers positifs).

    Returns:
        Un entier égal à ``len(l) - 1``.

    Raises:
        TypeError: si ``l`` n'est pas une liste.
        ValueError: si ``l`` est vide ou contient des valeurs invalides.
    """
    if not isinstance(l, list):
        raise TypeError("l doit être une liste.")
    if not l:
        raise ValueError("l ne doit pas être vide.")
    if not all(isinstance(x, int) and x >= 1 for x in l):
        raise ValueError("l doit contenir uniquement des entiers positifs.")
    return len(l) - 1


def temps_de_vol_en_altitude(l: list[int]) -> int:  # pylint: disable=invalid-name
    """Durée avant de passer strictement sous la valeur initiale ``l[0]``.

    On part du second terme et on compte combien de termes consécutifs
    restent supérieurs ou égaux à ``l[0]``. Si la liste ne contient qu'un
    élément, on retourne 0.

    Args:
        l: Suite de Syracuse (liste non vide d'entiers positifs).

    Returns:
        Un entier supérieur ou égal à 0.

    Raises:
        TypeError: si ``l`` n'est pas une liste.
        ValueError: si ``l`` est vide ou contient des valeurs invalides.
    """
    if not isinstance(l, list):
        raise TypeError("l doit être une liste.")
    if not l:
        raise ValueError("l ne doit pas être vide.")
    if not all(isinstance(x, int) and x >= 1 for x in l):
        raise ValueError("l doit contenir uniquement des entiers positifs.")
    if len(l) == 1:
        return 0

    source = l[0]
    i = 1
    while i < len(l) and l[i] >= source:
        i += 1
    return i - 1


def altitude_maximale(l: list[int]) -> int:  # pylint: disable=invalid-name
    """Retourne l'altitude maximale (le maximum) d'une suite.

    Args:
        l: Suite de Syracuse (liste non vide d'entiers positifs).

    Returns:
        Le maximum de la suite.

    Raises:
        TypeError: si ``l`` n'est pas une liste.
        ValueError: si ``l`` est vide ou contient des valeurs invalides.
    """
    if not isinstance(l, list):
        raise TypeError("l doit être une liste.")
    if not l:
        raise ValueError("l ne doit pas être vide.")
    if not all(isinstance(x, int) and x >= 1 for x in l):
        raise ValueError("l doit contenir uniquement des entiers positifs.")
    return max(l)

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()