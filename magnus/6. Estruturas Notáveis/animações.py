from manimlib.imports import *


class ConjuntosNuméricos(Scene):
    def construct(self):
        texto = TexMobject("\mathbb{N}, \ \mathbb{Z}, \ \mathbb{Q}, \ \mathbb{R}, \ \mathbb{C}").scale(3)
        self.play(Write(texto), run_time=3)
        self.wait(3)


class Intervalos(Scene):
    def construct(self):
        texto = TextMobject("Intervalos").scale(3)
        self.play(Write(texto), run_time=3)
        self.wait(3)


class Interrogação(Scene):
    def construct(self):
        texto = TextMobject("?").scale(4)
        self.play(Write(texto), run_time=3)
        self.wait(3)


class TeoremaFundamentalDaÁlgebra(Scene):
    def construct(self):
        texto = TextMobject("Teorema Fundamental \\\\da Álgebra").scale(2)
        self.play(Write(texto), run_time=3)
        self.wait(3)