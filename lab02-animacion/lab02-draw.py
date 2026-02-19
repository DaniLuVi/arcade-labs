import arcade

arcade.open_window(800, 600, "Drawing Example")

arcade.set_background_color((245, 141, 66))
arcade.start_render()

# Dibujo

# --- Finish drawing ---

# Keep the window up until someone closes it.
arcade.finish_render()
arcade.run()