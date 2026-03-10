import arcade

# Defino una clase que dibuje un coche
class Coche:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def extremos_coche(self):
        arcade.draw_triangle_filled(self.x, self.y, self.x, self.y + 50, self.x - 50, self.y, self.color)
        arcade.draw_triangle_filled(self.x + 100, self.y, self.x + 100, self.y + 50, self.x + 150, self.y, self.color)

    def ruedas_coche(self, num, radio):
            for i in range(num):
                arcade.draw_circle_filled(self.x + 15 + i*80, self.y, radio, self.color)
            
    def ventanas_coche(self):
        arcade.draw_polygon_filled(
            [(self.x + 20, self.y + 20), (self.x + 80, self.y + 20), (self.x + 80, self.y + 40), (self.x + 20, self.y + 40)],
            self.color
        )
        arcade.draw_triangle_filled(self.x + 15, self.y + 20, self.x + 15, self.y + 40, self.x - 5, self.y + 20, self.color)
        arcade.draw_triangle_filled(self.x + 85, self.y + 20, self.x + 85, self.y + 40, self.x + 105, self.y + 20, self.color)
    
    def dibujar_coche(self):
        arcade.draw_lbwh_rectangle_filled(self.x, self.y, 100, 50, self.color)
        self.extremos_coche()
        self.ruedas_coche(2, 20)
        self.ventanas_coche()


class Ventana(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Animación")

        self.set_mouse_visible(False)

        arcade.set_background_color((245, 141, 66))

        self.coche = Coche(100, 100,(0, 0, 255))
        
    def fondo_arena(self):
        arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, (237, 164, 69))

    def fondo_cielo_blanco(self):
        arcade.draw_lrbt_rectangle_filled(0, 800, 500, 600, (255, 255, 255))

    def pintar_sol(self):
        arcade.draw_circle_filled(700, 500, 50, (250, 197, 7))

    def pintar_carretera(self):
        arcade.draw_line(0, 250, 800, 350, arcade.color.BLACK, 40)
        for i in range(2):
            k = 18
            if i == 1:
                k = -k
            arcade.draw_line(0, 250 + k, 800, 350 + k, arcade.color.WHITE, 5)

    def pintar_playa(self):
        for i in range(20, 800, 40):
            arcade.draw_arc_filled(i, 0, 40, 20, arcade.color.AERO_BLUE, 0, 180)

    def on_draw(self):
        self.clear()

        self.fondo_arena()
        self.fondo_cielo_blanco()
        self.pintar_sol()
        self.pintar_carretera()
        self.pintar_playa()
        self.coche.dibujar_coche()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.coche.x = x
        self.coche.y = y
        
    
if __name__ == "__main__":
    ventana = Ventana()
    arcade.run()