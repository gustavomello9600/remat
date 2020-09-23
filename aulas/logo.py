from manimlib.imports import *


class Logo1(Scene):
    def construct(self):
        texto = TexMobject("\\mathbb{R}e\\mathbb{M}at").scale(5)
        self.add(texto)


class Logo2(Scene):
    def construct(self):
        texto = TexMobject(r"\begin{aligned}"
                           r"& \mathbb{R}e \\[-2\jot]"
                           r"& \mathbb{M}at"
                           r"\end{aligned}").scale(8)
        self.add(texto)


class Logo3(Scene):
    def construct(self):
        texto = TextMobject("Reinventando\\\\"
                            "a Matemática").scale(3)
        self.add(texto)