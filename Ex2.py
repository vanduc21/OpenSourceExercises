import numpy as np


def main():
    print("Tạo ma trận A và B")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("Ma trận A:")
    print(A)
    print("\nMa trận B:")
    print(B)

    print("\nPhép cộng A + B:")
    C = A + B
    print(C)

    print("\nPhép trừ A - B:")
    D = A - B
    print(D)

    print("\nPhép nhân A * B:")
    E = np.dot(A, B)
    print(E)

    print("\nTính giá trị trung bình và phương sai của ma trận A:")
    mean_A = np.mean(A)
    var_A = np.var(A)

    print(f"Giá trị trung bình của A: {mean_A}")
    print(f"Phương sai của A: {var_A}")


if __name__ == "__main__":
    main()
