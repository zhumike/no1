import sys
import pygame
def check_events(ship):
	#相应按键和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				ship.moving_right=True
			elif event.key==pygame.K_LEFT:
				ship.moving_left = True	


		elif event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT:
				ship.moving_right=False
			elif event.key==pygame.K_LEFT:
				ship.moving_left = False	
def update_screen(ai_settings,screen,ship):
		#设置背景颜色
		screen.fill(ai_settings.bg_color)
		
		#将飞船绘制到指定的位置上
		ship.blitme()
		

		#让最近绘制的屏幕可见
		pygame.display.flip()