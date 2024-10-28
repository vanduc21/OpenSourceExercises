import pygame, sys
from pygame.locals import *
import random
import time

# Kích thước cửa sổ game
WINDOWWIDTH = 800
WINDOWHEIGHT = 500

# Khởi tạo Pygame
pygame.init()
w = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Game Ăn Trái Cây')

# Tải hình ảnh nền, các loại trái cây và bom
BG = pygame.image.load('bg2.jpg')
BG = pygame.transform.scale(BG, (WINDOWWIDTH, WINDOWHEIGHT))

tao = pygame.image.load('tao.png')
tao = pygame.transform.scale(tao, (40, 50))

cam = pygame.image.load('cam.png')
cam = pygame.transform.scale(cam, (40, 50))

xoai = pygame.image.load('xoai.png')
xoai = pygame.transform.scale(xoai, (40, 50))

bom = pygame.image.load('bom.png')
bom = pygame.transform.scale(bom, (40, 50))

# Thiết lập FPS và tốc độ di chuyển
FPS = 20
fpsClock = pygame.time.Clock()

# Biến điểm số và thời gian
diem = 0
time0 = time.time()

# Số lượng hoa quả rơi cùng lúc
so_luong_hoa_qua = 5  # Số lượng hoa quả rơi cùng lúc


# Hàm tạo ra một trái cây hoặc bom ngẫu nhiên
def tao_hoa_qua():
    loai = random.choice(['tao', 'cam', 'xoai', 'bom'])  # Chọn ngẫu nhiên loại (bao gồm cả bom)
    x = random.randint(0, WINDOWWIDTH - 40)  # Vị trí x ngẫu nhiên
    y = 0  # Bắt đầu từ cạnh trên
    toc_do = random.randint(1, 10)  # Tốc độ ngẫu nhiên
    return {'loai': loai, 'x': x, 'y': y, 'toc_do': toc_do}


# Tạo danh sách các đối tượng hoa quả (bao gồm cả bom)
hoa_qua = [tao_hoa_qua() for _ in range(so_luong_hoa_qua)]


# Hàm kiểm tra nếu không có bom, thêm bom vào
def dam_bao_bom():
    co_bom = any(item['loai'] == 'bom' for item in hoa_qua)
    if not co_bom:
        # Nếu không có bom, chọn ngẫu nhiên một phần tử và biến nó thành bom
        vi_tri = random.randint(0, so_luong_hoa_qua - 1)
        hoa_qua[vi_tri]['loai'] = 'bom'


# Hàm xử lý ăn trái cây hoặc trúng bom
def kiem_tra_an_trai_cay(pos, item):
    return pos[0] > item['x'] and pos[0] < item['x'] + 40 and pos[1] > item['y'] and pos[1] < item['y'] + 50


# Hàm điều chỉnh tốc độ dựa trên điểm
def dieu_chinh_toc_do(diem, item):
    item['toc_do'] = 1 + diem // 10


# Hàm vẽ hoa quả hoặc bom lên màn hình
def ve_hoa_qua(hoa_qua):
    for item in hoa_qua:
        if item['loai'] == 'tao':
            w.blit(tao, (item['x'], item['y']))
        elif item['loai'] == 'cam':
            w.blit(cam, (item['x'], item['y']))
        elif item['loai'] == 'xoai':
            w.blit(xoai, (item['x'], item['y']))
        elif item['loai'] == 'bom':
            w.blit(bom, (item['x'], item['y']))


# Hàm khởi động lại trò chơi
def khoi_dong_lai():
    global diem, time0, hoa_qua
    diem = 0
    time0 = time.time()
    hoa_qua = [tao_hoa_qua() for _ in range(so_luong_hoa_qua)]
    dam_bao_bom()  # Đảm bảo có bom sau khi khởi động lại


# Hàm hiển thị nút "Chơi lại" và xử lý sự kiện bấm vào
def hien_thi_nut_choi_lai():
    font_game_over = pygame.font.SysFont('Arial', 60)
    text_game_over = font_game_over.render('Game Over', True, (255, 0, 0))
    w.blit(text_game_over, (WINDOWWIDTH // 2 - 150, WINDOWHEIGHT // 2 - 100))

    # Vẽ nút "Chơi lại"
    font_button = pygame.font.SysFont('Times New Roman', 40)
    text_button = font_button.render('Chơi lại', True, (255, 255, 255))
    button_rect = pygame.Rect(WINDOWWIDTH // 2 - 100, WINDOWHEIGHT // 2, 200, 60)
    pygame.draw.rect(w, (0, 128, 0), button_rect)
    w.blit(text_button, (WINDOWWIDTH // 2 - 70, WINDOWHEIGHT // 2 + 10))

    pygame.display.update()

    # Kiểm tra sự kiện bấm vào nút "Chơi lại"
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return  # Bắt đầu lại trò chơi


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Sự kiện bấm chuột
        if event.type == pygame.MOUSEBUTTONDOWN:
            for item in hoa_qua:
                if kiem_tra_an_trai_cay(event.pos, item):
                    if item['loai'] == 'bom':
                        # Trúng bom -> hiện thông báo "Game Over" và hiển thị nút "Chơi lại"
                        hien_thi_nut_choi_lai()
                        khoi_dong_lai()  # Khởi động lại trò chơi
                    else:
                        if item['loai'] == 'tao':
                            diem += 5
                        elif item['loai'] == 'cam':
                            diem += 3
                        elif item['loai'] == 'xoai':
                            diem += 7

                        # Reset lại vị trí của trái cây/bom khi ăn
                        item['x'] = random.randint(0, WINDOWWIDTH - 40)
                        item['y'] = 0
                        item['toc_do'] = random.randint(1, 10)  # Tốc độ mới

    # Điều chỉnh tốc độ của hoa quả dựa trên điểm
    for item in hoa_qua:
        dieu_chinh_toc_do(diem, item)

    # Đảm bảo luôn có ít nhất 1 bom
    dam_bao_bom()

    # Vẽ nền
    w.blit(BG, (0, 0))

    # Vẽ hoa quả và bom
    ve_hoa_qua(hoa_qua)

    # Di chuyển các hoa quả
    for item in hoa_qua:
        item['y'] += item['toc_do']

        # Reset lại vị trí khi hoa quả rơi qua màn hình
        if item['y'] > WINDOWHEIGHT:
            item['x'] = random.randint(0, WINDOWWIDTH - 40)
            item['y'] = 0
            item['toc_do'] = random.randint(1, 10)  # Tốc độ mới

    # Thời gian chơi
    time1 = time.time()

    # Hiển thị điểm số và thời gian
    font = pygame.font.SysFont('Times New Roman', 30)
    text_diem = font.render(f'Tổng điểm: {diem}', True, (255, 0, 0))
    text_time = font.render(f'Thời gian: {int(time1 - time0)}', True, (255, 0, 0))

    w.blit(text_diem, (50, 50))
    w.blit(text_time, (50, 80))

    # Cập nhật màn hình
    pygame.display.update()
    fpsClock.tick(FPS)
