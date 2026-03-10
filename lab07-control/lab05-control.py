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

class Nube:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = 0
        self.change_y = 0

    def dibujar_nube(self):
        arcade.draw_circle_filled(self.x, self.y, 30, arcade.color.WHITE)
        arcade.draw_circle_filled(self.x + 25, self.y + 15, 45, arcade.color.WHITE)
        arcade.draw_circle_filled(self.x + 50, self.y, 30, arcade.color.WHITE)

    def actualizar(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < 0:
            self.x = 0
            arcade.play_sound(arcade.sound.Sound(":resources:sounds/error4.wav"))
            
        if self.x > 740:
            self.x = 740
            arcade.play_sound(arcade.sound.Sound(":resources:sounds/error4.wav"))

            
        if self.y < 0:
            self.y = 0
            arcade.play_sound(arcade.sound.Sound(":resources:sounds/error4.wav"))

        if self.y > 560:
            self.y = 560
            arcade.play_sound(arcade.sound.Sound(":resources:sounds/error4.wav"))


class Ventana(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Animación")

        self.set_mouse_visible(False)

        arcade.set_background_color((245, 141, 66))

        self.coche = Coche(100, 100,(0, 0, 255))
        self.nube = Nube(400, 450)

        self.sonido_clic = arcade.Sound(":resources:sounds/hit5.wav")
        
    def fondo_arena(self):
        arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, (237, 164, 69))

    def fondo_cielo_blanco(self):
        arcade.draw_lrbt_rectangle_filled(0, 800, 500, 600, arcade.color.LIGHT_CORNFLOWER_BLUE)

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
        self.nube.dibujar_nube()

    def on_update(self, delta_time):
        self.nube.actualizar()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.coche.x = x
        self.coche.y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Se llama automáticamente cuando haces clic con cualquier botón del ratón """
        # Comprobamos si el botón que se ha pulsado es el izquierdo
        if button == arcade.MOUSE_BUTTON_LEFT:
            # Reproducimos el sonido que cargamos en el __init__
            self.sonido_clic.play()

    def on_key_press(self, key, modifiers):
        """ Se llama cuando se PRESIONA una tecla para mover la nube """
        if key == arcade.key.UP:
            self.nube.change_y = 5
        elif key == arcade.key.DOWN:
            self.nube.change_y = -5
        elif key == arcade.key.LEFT:
            self.nube.change_x = -5
        elif key == arcade.key.RIGHT:
            self.nube.change_x = 5

    def on_key_release(self, key, modifiers):
        """ Se llama cuando se SUELTA una tecla para detener la nube """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.nube.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.nube.change_x = 0
        
    
if __name__ == "__main__":
    ventana = Ventana()
    arcade.run()