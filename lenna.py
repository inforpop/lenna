import cv2

def rgb_to_gray(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def rgb_to_binary(image, threshold=127):
    gray_image = rgb_to_gray(image)
    _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image

# Carregando a imagem
image = cv2.imread('lenna.jpg')

# Convertendo para níveis de cinza
gray_image = rgb_to_gray(image)

# Convertendo para binarizada
binary_image = rgb_to_binary(image)

# Exibindo as imagens
cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem em Níveis de Cinza', gray_image)
cv2.imshow('Imagem Binarizada', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
