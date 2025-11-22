import numpy as np

print("=== 1. Bir Boyutlu Array ===")
arr1 = np.array([3, 7, 12, 5, 9], dtype=int)
print("Array:", arr1)
print("Boyut (ndim):", arr1.ndim)
print("Eleman sayısı (size):", arr1.size)
print("Şekil (shape):", arr1.shape)

print("\n=== 2. İki ve Üç Boyutlu Arrayler ===")

# İki boyutlu array
arr2 = np.array([[1, 2, 6, 7],
                 [4, 3, 9, 5]])

print("\n2 Boyutlu Array:")
print(arr2)
print("Boyut:", arr2.ndim)
print("Eleman sayısı:", arr2.size)
print("Şekil:", arr2.shape)

# Üç boyutlu array
arr3 = np.array([[[7, 5, 14], [21, 8, 11]],
                 [[8, 6, 20], [14, 3, 9]]])

print("\n3 Boyutlu Array:")
print(arr3)
print("Boyut:", arr3.ndim)
print("Eleman sayısı:", arr3.size)
print("Şekil:", arr3.shape)

print("\n=== 3. Indexleme İşlemleri ===")

print("2D arraydeki 2 elemanı:", arr2[0, 1])
print("2D arraydeki 7 elemanı:", arr2[0, 3])
print("3D arraydeki 9 elemanı:", arr3[1, 1, 2])
print("3D arraydeki 5 elemanı:", arr3[0, 0, 1])

print("\n=== 4. Slicing İşlemleri ===")

print("2D arrayden 2 ve 6 elemanları:", arr2[0, 1:3])
print("2D arrayden 3, 9, 5 elemanları:", arr2[1, 1:4])
print("3D arrayden 21, 8, 11 elemanları:", arr3[0, 1, :])
print("3D arrayden 6 ve 20 elemanları:", arr3[1, 0, 1:3])

print("\n=== 5. Sıfır ve Birlerden Oluşan 5x3 Arrayler ===")

zeros_arr = np.zeros((5, 3), dtype=int)
ones_arr = np.ones((5, 3), dtype=int)

print("\nZeros Array:")
print(zeros_arr)

print("\nOnes Array:")
print(ones_arr)

# Satır bazında birleştirme (alt alta)
concat_rows = np.vstack((zeros_arr, ones_arr))
print("\nSatır Bazında Birleştirme:")
print(concat_rows)

# Sütun bazında birleştirme (yan yana)
concat_cols = np.hstack((zeros_arr, ones_arr))
print("\nSütun Bazında Birleştirme:")
print(concat_cols)
