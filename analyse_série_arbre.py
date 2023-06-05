
import os
from math import *
import imageio.v2 as imageio
import imageio as io
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np

#analyser une image pour savoir si elle est vert
def C_vert(luminosite_vert):

    A = np.array([[[i, luminosite_vert, j] for i in range(255)]
                 for j in range(255)])
    X = [i for i in range(luminosite_vert+1)]
    Y = [((luminosite_vert**3-j**3)*0.83)**(1/3) for j in range(luminosite_vert+1)]
    plt.plot(X, Y, 'black')
    plt.imshow(A)
    print("Press q to continue")
    plt.show()

    return A

def test_vert(L):
    if (1/0.83)*L[1]**3 >= 2*((L[0]**3)*0.83+L[2]**3):
        return True

def taux_de_vert(L):
    size_x = len(L)
    size_y = len(L[0])
    nb_pixels = size_x*size_y
    b = 0
    for i in range(size_x):
        for j in range(size_y):
            if test_vert(L[i, j]) == True:
                b += 1
    #print(b/nb_pixels*100)
    return b/nb_pixels*100
#Séléctioner les images voulus 
def lecture(file):
    image = io.imread(file)
    image = np.array(image)
    #plt.imshow(image)
    #plt.show()
    #plt.axis('off')
    return image

def ecriture(image):
    io.imwrite(str(image)+'.png', image)
#affiche uniquement le vert de l'image
def highlight(image) :
    for i in range(len(image)):
        for j in range(len(image[1])):
            if test_vert(image[i,j]) == True :
                image[i,j] = [0,255,0] 
            else :
                image[i,j] = [0,0,0]
    plt.imshow(image)
    plt.show()       
#
def série_photo(nom_générique,nb_photo) :
    Les_images=[f"{nom_générique}.jpeg" for i in range(1)]
    #print(Les_images)
    return Les_images
#donne le pourcentage de vert de chaque image pour une série donnée 
def analyse(nom_génrique,nbphto) :
    résultat=série_photo(nom_génrique,nbphto)
    for i in range(len(résultat)) :
        résultat[i] = lecture(résultat[i])
        résultat[i] = taux_de_vert(résultat[i])
    print(résultat)
    return résultat

## adresse du dossier 
os.chdir("C:/Users/user/OneDrive/Bureau/Bcpst 1 A/TP informatique/TIPE_INFORMATIQUE/")#+nom_dcu_dossier/

# Chargement de l'image
image = lecture("Radis-Montage.jpeg")

# Mise en évidence du vert dans l'image
highlight(image)
