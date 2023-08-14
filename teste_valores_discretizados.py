import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo (idades)
idades = np.array([18, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

# Plot do gráfico não discretizado
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(idades, np.zeros_like(idades), 'bo', markersize=8)
plt.title('Gráfico Não Discretizado')
plt.xlabel('Idade')
plt.yticks([])

# Plot do gráfico discretizado
plt.subplot(1, 2, 2)
plt.plot(idades, np.zeros_like(idades), 'bo', markersize=8)
plt.title('Gráfico Discretizado')
plt.xlabel('Idade')
plt.yticks([])

# Divisões para discretização (exemplo)
limites_discretizacao = [25, 40, 60, 80]

# Adicionando linhas verticais para mostrar a discretização
for limite in limites_discretizacao:
    plt.subplot(1, 2, 2)
    plt.axvline(x=limite, color='r', linestyle='--')

plt.tight_layout()
plt.show()