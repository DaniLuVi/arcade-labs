import arcade

WIDTH = 800
HEIGHT = 600

arcade.open_window(WIDTH, HEIGHT, "Example")

arcade.start_render()
arcade.draw_text("Aquí esta mi primer proyecto con Arcade :)", 280, 300, arcade.color.WHITE)
arcade.finish_render()

arcade.run()
