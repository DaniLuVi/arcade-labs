import arcade

# Defino una clase que dibuje un coche
class Ventana(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Animación")
        arcade.set_background_color((245, 141, 66))

    def extremos_coche(self):
        arcade.draw_triangle_filled(100, 100, 100, 150, 50, 100, (37, 38, 41))
        arcade.draw_triangle_filled(200, 100, 200, 150, 250, 100, (37, 38, 41))

    def ruedas_coche(self, num, radio):
            for i in range(num):
                arcade.draw_circle_filled(115 + i*80, 100, radio, (37, 38, 41))
            
    #def ventanas_coche(self):
     #   arcade.draw_polygon_filled

    def on_draw(self):
        self.clear()

        arcade.draw_lbwh_rectangle_filled(100, 100, 100, 50, (37, 38, 41))
        self.extremos_coche()
        self.ruedas_coche(2, 20) 
    
    

#arcade.open_window(800, 600, "Drawing Example")

#arcade.start_render()

# Dibujo

ventana = Ventana()
#coche.on_draw()

# --- Finish drawing ---

# Keep the window up until someone closes it.
#arcade.finish_render()
arcade.run()