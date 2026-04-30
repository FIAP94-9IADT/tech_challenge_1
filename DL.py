import cv2
import numpy as np
import matplotlib.pyplot as plt
import torch
import torchvision.transforms as transforms
from PIL import Image

# =========================
# 1. Carregar imagem
# =========================

image_path = "deep leaning/jpeg/1.3.6.1.4.1.9590.100.1.2.126082211045731020508108042042916052/1-240.jpg" 

img = cv2.imread(image_path, 0)

plt.imshow(img, cmap='gray')
plt.title("Imagem Original")
plt.axis('off')
plt.show()


# =========================
# 2. Pré-processamento
# =========================

# normalização
img_norm = img / 255.0

# redimensionar
img_resized = cv2.resize(img_norm, (224, 224))

plt.imshow(img_resized, cmap='gray')
plt.title("Imagem Processada")
plt.axis('off')
plt.show()


# =========================
# 3. Converter para tensor
# =========================

tensor = torch.tensor(img_resized).unsqueeze(0).unsqueeze(0).float()


# =========================
# 4. Simulação de modelo Deep Learning
# =========================

# simulação (substituível por modelo real)
score = torch.rand(1).item()

if score > 0.7:
    result = "ALTO RISCO"
elif score > 0.4:
    result = "RISCO MODERADO"
else:
    result = "BAIXO RISCO"


# =========================
# 5. Detecção de regiões (tipo heatmap simples)
# =========================

edges = cv2.Canny((img_resized * 255).astype(np.uint8), 50, 150)

plt.imshow(edges, cmap='hot')
plt.title("Mapa de Bordas (atenção da IA)")
plt.axis('off')
plt.show()


# =========================
# 6. Resultado final
# =========================

print("Resultado da IA:", result)
print("Score:", score)