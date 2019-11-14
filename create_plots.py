import numpy as np
import matplotlib.pyplot as plt

g = 10
T = np.linspace(0,10,1000)


def equation_trajectoire(x,Vx,Vz):
    return -5*x*x/(Vx*Vx) + (x*Vz)/Vx

def creer_trajectoire(angle,vi):
    vx = np.cos(angle) * vi
    vz = np.sin(angle) * vi
    impact = 0.2 * vx * vz
    print(impact)
    Lx = np.linspace(0,impact,1000)
    return Lx,[equation_trajectoire(x,vx,vz) for x in Lx]


# example_plot = creer_trajectoire(np.pi/4,50)
#
# plt.plot(example_plot[0],example_plot[1])
# plt.xlim(-1,251)
# plt.ylim(-1,70)
# plt.show()


Langles = np.linspace(0.1,np.pi/4,30)
Lvi = np.linspace(1,50,30)

compteur = 0
for Vi in Lvi:
    for Angle in Langles:
        print(compteur)
        compteur += 1
        plot_result = creer_trajectoire(Angle,Vi)
        plt.figure()
        plt.plot(plot_result[0],plot_result[1])
        plt.xlim(-1,251)
        plt.ylim(-1,70)
        plt.savefig(f"plots/plot_{Angle}_{Vi}.jpg")
        plt.clf()
        plt.close()
