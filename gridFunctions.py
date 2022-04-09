import matplotlib.pyplot as plt 

def createGraph():
    plt.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])
    plt.xlabel('Months')
    plt.ylabel('Books Read')
    plt.savefig('static/books_read.png')