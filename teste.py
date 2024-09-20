from matplotlib.image import imread

imagem = imread('/Users/Esquirio/Python/Lenna.png')
print('Altura em pixels: ', end='')
print(imagem.shape[0])
print('Largura em pixels: ', end='')
print(imagem.shape[1])
print('Qtde de dimensoes: ', end='')
print(imagem.shape[2])