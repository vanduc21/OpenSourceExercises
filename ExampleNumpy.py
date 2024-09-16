import numpy as np

def nhap_toa_do(diem):
    while True:
        try:
            x = float(input(f"Nhập tọa độ x của điểm {diem}: "))
            y = float(input(f"Nhập tọa độ y của điểm {diem}: "))
            z = float(input(f"Nhập tọa độ z của điểm {diem}: "))
            diem = np.array([x, y, z])
            return diem
        except ValueError:
            print("Vui lòng nhập số hợp lệ cho tọa độ!")

a = nhap_toa_do("A")
b = nhap_toa_do("B")
print(f"Tọa độ điểm A là: {a}")
print(f"Tọa độ điểm B là: {b}")

tich_vo_huong = np.dot(a, b)
print(f"Tích vô hướng của 2 vector A và B là: {tich_vo_huong}")

norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)
print(f"Độ dài vector A là: {norm_a}")
print(f"Độ dài vector B là: {norm_b}")

if norm_a != 0 and norm_b != 0:
    cosin = tich_vo_huong / (norm_a * norm_b)
    print(f"Cosin của góc giữa 2 vector A và B là: {cosin}")
else:
    print("Không thể tính cosin vì một trong hai vector có độ dài bằng 0.")
