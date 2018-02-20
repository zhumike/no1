import sys 
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf 
def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings=Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	#screen=pygame.display.set_mode((1200,800))
	pygame.display.set_caption("alien invasion")

	#创建一艘飞船
	ship=Ship(ai_settings,screen)
    
	#开始游戏的主循环
	while True:
		#监视键盘与鼠标事件
		gf.check_events(ship)
		ship.update()
		#绘制屏幕
		gf.update_screen(ai_settings,screen,ship)
if __name__ == "__main__":
	run_game()
