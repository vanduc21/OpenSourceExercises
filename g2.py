import pygame, sys
from pygame.locals import *
import random

chieu_dai = 800  # Chiều dài cửa sổ
chieu_rong = 500  # Chiều cao cửa sổ
pygame.init()  # Khởi tạo game
w = pygame.display.set_mode((chieu_dai, chieu_rong))  # Tạo 1 cửa sổ game tên là w
pygame.display.set_caption('Game Bắn Chim')

# ------------- tạo nền của game là 1 ảnh -----------------
anh_nen = pygame.image.load('nui.png')
anh_nen = pygame.transform.scale(anh_nen, (chieu_dai, chieu_rong))

# ----------- tạo ảnh các con chim --------------
chim1 = pygame.image.load('chim1.png')
chim1 = pygame.transform.scale(chim1, (40, 50))
chim2 = pygame.image.load('chim2.png')
chim2 = pygame.transform.scale(chim2, (40, 50))

# ----------- tạo ảnh thợ săn --------------
tho_san = pygame.image.load('tho_san.png')
tho_san = pygame.transform.scale(tho_san, (50, 80))

# Vị trí ban đầu của thợ săn
tho_san_x = chieu_dai // 2 - 25
tho_san_y = chieu_rong - 90

# Tạo biến điểm số
diem = 0

# Tạo đạn
dan_list = []

# Vị trí ban đầu của chim
def random_vitri_chim():
    x = random.randint(0, chieu_dai - 80)  # Xác định vị trí ngẫu nhiên trên trục x
    y = random.randint(50, 300)  # Vị trí ngẫu nhiên trên trục y (giới hạn trong màn hình)
    return x, y

# Khởi tạo vị trí ban đầu của chim
x1, y1 = random_vitri_chim()
x2, y2 = random_vitri_chim()

# Khung thời gian
FPS = 60
fpsClock = pygame.time.Clock()

# Hàm vẽ đạn
def ve_dan(dan_list):
    for dan in dan_list:
        pygame.draw.rect(w, (255, 0, 0), dan)

# Hàm kiểm tra va chạm giữa đạn và chim
def kiem_tra_va_cham(dan, chim_rect):
    return dan.colliderect(chim_rect)

# Hàm tạo viên đạn mới từ vị trí thợ săn
def tao_dan(x, y):
    return pygame.Rect(x + 22, y, 5, 10)

while True:  # Tạo vòng lặp game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Sự kiện bắn khi nhấn chuột trái
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            dan_list.append(tao_dan(tho_san_x, tho_san_y))

    # Kiểm tra phím di chuyển thợ săn
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and tho_san_x > 0:
        tho_san_x -= 5
    if keys[K_RIGHT] and tho_san_x < chieu_dai - 50:
        tho_san_x += 5

    # ----- Vẽ ảnh nền ----------------
    w.blit(anh_nen, (0, 0))

    # Vẽ chim
    chim1_rect = w.blit(chim1, (x1, y1))
    chim2_rect = w.blit(chim2, (x2, y2))

    # Di chuyển chim
    x1 += 1
    x2 -= 5
    if x1 > chieu_dai:
        x1, y1 = random_vitri_chim()  # Tạo vị trí mới ngẫu nhiên cho chim 1 khi ra khỏi màn hình
    if x2 < 0:
        x2, y2 = random_vitri_chim()  # Tạo vị trí mới ngẫu nhiên cho chim 2 khi ra khỏi màn hình

    # Di chuyển đạn
    for dan in dan_list:
        dan.y -= 5  # Di chuyển đạn lên trên

    # Kiểm tra va chạm giữa đạn và chim
    for dan in dan_list:
        if kiem_tra_va_cham(dan, chim1_rect):
            diem += 1
            dan_list.remove(dan)  # Xóa viên đạn khi bắn trúng chim
            x1, y1 = random_vitri_chim()  # Reset vị trí chim 1 ngẫu nhiên
        elif kiem_tra_va_cham(dan, chim2_rect):
            diem += 1
            dan_list.remove(dan)  # Xóa viên đạn khi bắn trúng chim
            x2, y2 = random_vitri_chim()  # Reset vị trí chim 2 ngẫu nhiên

    # Vẽ đạn
    ve_dan(dan_list)

    # Vẽ thợ săn
    w.blit(tho_san, (tho_san_x, tho_san_y))

    # Hiển thị điểm số
    font = pygame.font.SysFont('Arial', 30)
    text_diem = font.render(f'Score: {diem}', True, (255, 0, 0))
    w.blit(text_diem, (10, 10))

    # Cập nhật màn hình
    pygame.display.update()
    fpsClock.tick(FPS)
