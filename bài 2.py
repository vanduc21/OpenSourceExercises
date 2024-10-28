import cv2
import numpy as np
from tkinter import filedialog, Tk, Button, Label, Frame
from PIL import Image, ImageTk

# Hàm chọn ảnh từ máy tính
def open_image():
    global img_original, img_processed
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        img_original = cv2.imread(file_path)
        img_processed = img_original.copy()  # Tạo bản sao để xử lý
        show_images(img_original, img_processed)

# Hiển thị ảnh gốc và ảnh đã xử lý trên GUI
def show_images(original, processed):
    img_rgb_original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    img_rgb_processed = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)

    img_pil_original = Image.fromarray(img_rgb_original)
    img_pil_processed = Image.fromarray(img_rgb_processed)

    img_tk_original = ImageTk.PhotoImage(img_pil_original)
    img_tk_processed = ImageTk.PhotoImage(img_pil_processed)

    img_display_original.config(image=img_tk_original)
    img_display_original.image = img_tk_original

    img_display_processed.config(image=img_tk_processed)
    img_display_processed.image = img_tk_processed

# Áp dụng bộ lọc tạo độ nét cho ảnh đã xử lý
def apply_filter():
    global img_original, img_processed
    if img_original is None:
        return

    # Tạo các kernel cần thiết
    kernel_identity = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    kernel_3x3 = np.ones((3, 3), np.float32) / 9.0
    kernel_5x5 = np.ones((5, 5), np.float32) / 25.0

    # Áp dụng bộ lọc độ nét
    img_processed = cv2.filter2D(img_original, -1, kernel_identity)  # Bộ lọc nhận diện
    img_processed = cv2.filter2D(img_processed, -5, kernel_3x3)      # Bộ lọc 3x3

    # Áp dụng bộ lọc 5x5 vào vùng ảnh con
    output = cv2.filter2D(img_original[0:100, 0:100], -1, kernel_5x5)
    for i in range(100):
        for j in range(100):
            img_processed[i, j] = output[i, j]

    show_images(img_original, img_processed)

# Lưu ảnh đã xử lý
def save_image():
    global img_processed
    if img_processed is None:
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
    if save_path:
        cv2.imwrite(save_path, img_processed)

# Tạo GUI chính
root = Tk()
root.title("Medical Image Sharpening Application")

# Khung chứa ảnh gốc và ảnh đã xử lý
frame = Frame(root)
frame.pack()

# Khung hiển thị ảnh gốc
Label(frame, text="Original Image").grid(row=0, column=0)
img_display_original = Label(frame)
img_display_original.grid(row=1, column=0)

# Khung hiển thị ảnh đã xử lý
Label(frame, text="Processed Image").grid(row=0, column=1)
img_display_processed = Label(frame)
img_display_processed.grid(row=1, column=1)

# Thêm khung để chứa các nút chức năng theo hàng ngang
button_frame = Frame(root)
button_frame.pack()

# Thêm các nút chức năng và sắp xếp theo hàng ngang
btn_open = Button(button_frame, text="Open Image", command=open_image)
btn_open.pack(side="left")

btn_apply_filter = Button(button_frame, text="Apply Sharpening Filter", command=apply_filter)
btn_apply_filter.pack(side="left")

btn_save = Button(button_frame, text="Save Processed Image", command=save_image)
btn_save.pack(side="left")

# Biến toàn cục để lưu ảnh
img_original = None
img_processed = None

# Chạy vòng lặp chính của GUI
root.mainloop()
