import numpy as np
import matplotlib.pyplot as plt


class Linear():
    def __init__(self, x, y):
        if (type(x) is not np.ndarray) and (type(y) is not np.ndarray):
            raise ValueError("Inputs must be numpy arrays")
        self.x_local = x 
        self.y_local = y
    
    def linear_hypothesis(self, x, theta=(0,1)):
        """ Linear function f(x)=a*x+b
        
        Args:
            x (numpy.array()) : vector used to generate the output
            theta (tuple of size 2) : b=params[0] and a=params[1]
        
        Returns:
            numpy.array()
        """
        a, b = theta[1], theta[0]
        return b+a*x
    
    def cost(self, x, y, func, func_args):
        """ Cost function associated with (x,y) couple and function to fit
        
        Args:
            x : feature vector 
            y : explained variable
            func : target function
            func_args : arguments of function
        
        Returns:
            scalar value of cost
        """
        return 1./len(x)*sum(np.square(y-func(x,func_args)))
    
    def params_search(self, x, y):
        """ Estimation des parametres : scan systematique.
        
        Args : x : feature vector 
               y : explained variable
        
        Returns:
            Parametres optimaux de la fonction linear_hypothesis
        """
        errors = []
        params = []
        for p0 in np.linspace(0,10):
            for p1 in np.linspace(0,10):
                p = (p0,p1)
                c = self.cost(x, y, self.linear_hypothesis, p)
                errors.append(c)
                params.append(p)
        return params[errors.index(min(errors))]
    
    def gradient_descent(self, x, y, theta=None, alpha=0.001, iterations=10000):
        """ Estimation des parametres : descente de gradient.
        
        Args : x : feature vector 
               y : explained variable
               theta : starting parameters
               alpha : step
               iterations : iteration number
        
        Returns:
            Parametres optimaux de la fonction linear_hypothesis
        """
        if theta is None:
            theta = (5,10)

        theta = list(theta)
        N=len(y)
        
        for i in range(iterations):
            theta[0] = theta[0]-(alpha/N)*sum(self.linear_hypothesis(x,theta)-y)
            theta[1] = theta[1]-(alpha/N)*(self.linear_hypothesis(x,theta)-y).dot(x)

        return theta
    
    def fit(self, optimisation=None):
        """ Fonction retournant les parametres estimes a l'aide de la methode des moindres carres.
            
            Args: 
                optimisation : doit etre scan_systematique ou descente_gradient
        """
        if optimisation == "scan_systematique":
            return self.params_search(self.x_local, self.y_local)
        elif optimisation == "descente_gradient":
            return self.gradient_descent(self.x_local, self.y_local, (5,10), alpha=0.01, iterations=5000)
        else:
            raise ValueError("The parameter optimisation must be 'scan_systematique' or 'descente_gradient'")
    
    def plot_data(self, show=False):
        """ Graphe : points de donnees x en fonction de y. 
            
        Args :
            show : affichage optionnel
        """
        plt.scatter(self.x_local,self.y_local)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('')
        if show : 
            plt.show()

    def plot_fit(self, parameters, legende, color='b', show=False):
        """ Graphe : droite de la fonction lineaire f(x)=a*x+b .
        
        Args :
            parameters : parametres de la droite (b=params[0] and a=params[1])
            legende : donne une legende a la droite
            color : change la couleur de la droite => 'b'         blue
                                                      'g'         green
                                                      'r'         red
                                                      'c'         cyan
                                                      'm'         magenta
                                                      'y'         yellow
                                                      'k'         black
                                                      'w'         white
            show : affichage optionnel
        """
        plt.plot(self.x_local, self.linear_hypothesis(self.x_local, parameters), color, label=legende)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.title('')
        if show : 
            plt.show()

