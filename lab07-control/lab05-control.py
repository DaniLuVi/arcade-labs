import arcade

# Defino una clase que dibuje un coche
class Ventana(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Animación")
        arcade.set_background_color((245, 141, 66))

        self.contador_animacion = 0

    def on_update(self, delta_time):     
        self.contador_animacion += 1
        if self.contador_animacion > 100:
            self.contador_animacion = 0
        
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

    def extremos_coche(self, contador, k):
        arcade.draw_triangle_filled(100 + contador * k, 100, 100 + contador * k, 150, 50 + contador * k, 100, (37, 38, 41))
        arcade.draw_triangle_filled(200 + contador * k, 100, 200 + contador * k, 150, 250 + contador * k, 100, (37, 38, 41))

    def ruedas_coche(self, num, radio, contador, k):
            for i in range(num):
                arcade.draw_circle_filled(115 + i*80 + contador * k, 100, radio, (37, 38, 41))
            
    def ventanas_coche(self, contador, k):
        arcade.draw_polygon_filled(
            [(120 + contador * k, 120), (180 + contador * k, 120), (180 + contador * k, 140), (120 + contador * k, 140)],
            (89, 185, 189)
        )
        arcade.draw_triangle_filled(115 + contador * k, 120, 115 + contador * k, 140, 95 + contador * k, 120, (89, 185, 189))
        arcade.draw_triangle_filled(185 + contador * k, 120, 185 + contador * k, 140, 205 + contador * k, 120, (89, 185, 189))

    def on_draw(self):
        self.clear()

        self.fondo_arena()
        self.fondo_cielo_blanco()
        self.pintar_sol()
        self.pintar_carretera()
        self.pintar_playa()
        k = 10
        arcade.draw_lbwh_rectangle_filled(100 + self.contador_animacion * k, 100, 100, 50, (37, 38, 41))
        self.extremos_coche(self.contador_animacion, k)
        self.ruedas_coche(2, 20, self.contador_animacion, k) 
        self.ventanas_coche(self.contador_animacion, k)
    
    

if __name__ == "__main__":
    ventana = Ventana()
    arcade.run()