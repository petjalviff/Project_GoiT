# import matplotlib.pyplot as plt
# import numpy as np


# # Функція для обчислення модуля вектора
# def compute_vector_magnitude(vector):
#     return np.sqrt(np.sum(vector ** 2))


# # Створення вектора
# vector_a = np.array([4, 3])


# # Обчислення модуля вектора
# magnitude_a = compute_vector_magnitude(vector_a)


# # Вивід результату
# print(f"Вектор A: {vector_a}")
# print(f"Модуль вектора A: {magnitude_a:.2f}")


# # Візуалізація вектора на площині
# plt.figure(figsize=(6, 6))
# plt.quiver(0, 0, vector_a[0], vector_a[1], angles='xy', scale_units='xy', scale=1, color='g', label='Вектор A')


# # Додавання підпису з модулем вектора
# plt.text(vector_a[0] / 2, vector_a[1] / 2, f'Modulus: {magnitude_a:.2f}', color='b')


# # Налаштування вигляду графіка
# plt.xlim([-1, 7])
# plt.ylim([-1, 7])
# plt.axhline(0, color='b', linewidth=1.5)
# plt.axvline(0, color='b', linewidth=1.5)
# plt.grid(color='gray', linestyle='--', linewidth=0.5)
# plt.gca().set_aspect('equal', adjustable='box')
# plt.title('Модуль вектора на площині')
# plt.xlabel('Вісь X')
# plt.ylabel('Вісь Y')
# plt.legend()
# plt.show()


# *********************************************************************************8
import plotly.graph_objects as go
import numpy as np


# Функція для обчислення модуля вектора
def compute_vector_magnitude(vector):
    return np.sqrt(np.sum(vector ** 2))


# Створення вектора
vector_a = np.array([2, 5, 4])


# Обчислення модуля вектора
magnitude_a = compute_vector_magnitude(vector_a)


# Вивід результату
print(f"Вектор A: {vector_a}")
print(f"Модуль вектора A: {magnitude_a:.2f}")


# Візуалізація вектора у 3D просторі
fig = go.Figure()


# Додавання вектора до графіка
fig.add_trace(go.Scatter3d(x=[0, vector_a[0]], y=[0, vector_a[1]], z=[0, vector_a[2]],
                           mode='lines+markers', marker=dict(size=5), line=dict(color='blue'), name='Вектор A'))


# Додавання підпису з модулем вектора
fig.add_trace(go.Scatter3d(x=[vector_a[0] / 2], y=[vector_a[1] / 2], z=[vector_a[2] / 2],
                           mode='text', text=[f'Modulus: {magnitude_a:.2f}'], textposition='bottom center', name='Modulus'))


# Налаштування вигляду графіка
fig.update_layout(scene=dict(aspectmode='data'))
fig.update_layout(scene=dict(xaxis_title='Вісь X', yaxis_title='Вісь Y', zaxis_title='Вісь Z'))
fig.update_layout(title='Модуль вектора та візуалізація у 3D просторі')


# Відображення графіка
fig.show()
