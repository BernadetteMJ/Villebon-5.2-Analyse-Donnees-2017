#import matplotlib.pyplot as plt
from simu_data import generate_data
from regression import linear_regression

# Autres manières d'importer directement la classe Linear :
#from regression import linear_regression.Linear as Linear
#from regression.linear_regression import Linear

def main():
    x,y = generate_data(1000, var=5)

    # peut etre try / catch ici
    l = linear_regression.Linear(x,y)
    l.plot_data()
    params_scan = l.fit(optimisation="scan_systematique")
    print "Parametres optimisant les moindres carres, via un scan :", params_scan
    l.plot_fit(params_scan, legende="Params scan systematique", color="g")
    
    params_gd = l.fit(optimisation="descente_gradient")
    print "Parametres optimisant les moindres carres, via la descente de gradient :", params_gd
    l.plot_fit(params_gd, legende="Params descente de gradient", color="r", show=True)
    
    # Autre maniere d'utiliser la classe :
    #plt.plot(l.x_local, l.linear_hypothesis(l.x_local, theta = params_gd))
    #plt.show()

if __name__ == '__main__':
    main()