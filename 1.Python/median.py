# On importe les modules dont on a besoin.
from random import shuffle

# On definit nos fonctions
def mediane(v):
    sorted_v = sorted(v) #pour etre sur que les elements de v sont dans un ordre croissant.
    n = len(v)
    m = n-1
    return (sorted_v[n/2]+sorted_v[m/2])/2.

# Partie du script qui sera execute lorsqu'on lance le script directement (python median.py), 
# mais qui ne sera pas execute si on l'importe dans un autre script (import median).
def main():
    v = [1,1,1,2,3]
    shuffle(v) #mettre dans le desordre les elements de v.
    print 'v is now', v
    
    print mediane(v)
    print mediane(v[1:])
    assert mediane(v) == 1
    assert mediane(v[1:]) == 1.5

if __name__ == "__main__":
    main()

