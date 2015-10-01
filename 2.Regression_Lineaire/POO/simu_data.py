import numpy as np

def generate_data(N=100, params=(0,1), var=1):
    """ Fonction simulant les donnees : on genere une distribution de points au
        voisinage d'une droite avec la fonction lineaire : f(x)=a*x+b+N(0,1)
        (cf la fonction linear de Regression_1.ipynb)
        
        N      : nombre de points pour generer le vecteur x
        params : parametres de la fonction : b=params[0] et a=params[1]
        var    : facteur faisant varier la variance de la fonction normale N(0,1)
    """
    x = 10*np.random.random(N)
    y = params[0] + params[1]*x + var*np.random.normal(size=len(x))
    return x, y


# Partie du script qui sera execute seulement lorsqu'on lance le script directement (python generate_data.py), 
# mais qui ne sera pas execute si on l'importe dans un autre script (import generate_data).
# Remarque : np.savetxt permet de sauvegarder les donnees dans un fichier texte au format .csv .
def main():
    x,y = generate_data()
    np.savetxt("generated.csv", np.column_stack((x,y))) 


if __name__ == '__main__':
    main()