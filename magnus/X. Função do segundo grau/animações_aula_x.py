from manimlib.imports import *


class Função(Scene):
    def construct(self):
        texto = TextMobject("O que é função?").scale(2)
        self.play(Write(texto), run_time=3)
        self.wait(3)


class SegundoGrau(Scene):
    def construct(self):
        texto = TextMobject("2º grau?").scale(3)
        self.play(Write(texto), run_time=3)
        self.wait(3)


class Representação(Scene):
    def construct(self):
        texto = TextMobject("Como se representa?").scale(2)
        self.play(Write(texto), run_time=3)
        self.wait(3)

        self.play(ApplyMethod(texto.to_edge, UP))
        definição = TexMobject("\\begin{aligned}"
                               "& f: \\mathbb{R} \\rightarrow \\mathbb{R} \\\\"
                               "& f(x) = ax^2 + bx + c, \\ a, b, c \\in \\mathbb{R}"
                               "\\end{aligned}").shift((FRAME_HEIGHT/2 - texto.get_y())*DOWN/2)
        self.play(Write(definição))
        self.wait(3)


class Gráfico(Scene):
    def construct(self):
        texto = TextMobject("Qual a forma do gráfico?").scale(2)
        self.play(Write(texto), run_time=3)
        self.wait(3)

        self.play(ApplyMethod(texto.to_edge, UP))
        curva = FunctionGraph(lambda x: x**2).shift((FRAME_HEIGHT/2 + texto.get_y())*DOWN/2)
        self.play(ShowCreation(curva))
        self.wait(3)


class IntroduçãoAParabola(Scene):
    def construct(self):
        texto = TextMobject("O que é uma parábola?").scale(2).add_background_rectangle()
        self.play(Write(texto), run_time=3)
        self.wait(3)


        self.add_foreground_mobject(texto)
        self.play(ApplyMethod(texto.scale, 0.5))
        self.play(ApplyMethod(texto.to_edge, UP))

        plano = NumberPlane()
        self.play(ShowCreation(plano), run_time=3)
        self.wait(3)

        parabola = FunctionGraph(lambda x: x**2, x_min=-2, x_max=2)
        ponto = Dot(-2*RIGHT + 4*UP)
        foco = Dot(UP/4)
        diretriz = Line(start=8*LEFT + DOWN/4, end=8*RIGHT + DOWN/4)

        self.play(AnimationGroup(FadeIn(foco),
                                 ShowCreation(diretriz)))
        self.wait(3)
        self.play(FadeIn(ponto))
        self.wait()
        self.play(AnimationGroup(ShowCreation(parabola),
                                 MoveAlongPath(ponto, parabola), run_time=5))
        self.wait(3)


class ParabolaGeral(Scene):
    def construct(self):
        plano = NumberPlane()
        self.play(ShowCreation(plano), run_time=3)

        texto = TexMobject("f(x) = x^2").add_background_rectangle().to_edge(UP)
        self.add_foreground_mobject(texto)
        self.play(Write(texto))

        parabola = FunctionGraph(lambda x: x**2)
        self.play(ShowCreation(parabola), run_time=3)
        self.wait(5)

        self.play(AnimationGroup(Transform(parabola, FunctionGraph(lambda x: (x - 2)**2)),
                                 Transform(texto, TexMobject("f(x) = (x - 2)^2"
                                                                        ).add_background_rectangle().to_edge(UP)),
                  run_time=3))
        self.wait(5)

        self.play(AnimationGroup(Transform(parabola, FunctionGraph(lambda x: (1/2)*((x - 2)) ** 2)),
                                 Transform(texto, TexMobject("f(x) = \\frac{1}{2}(x - 2)^2"
                                                                        ).add_background_rectangle().to_edge(UP)),
                                 run_time=3))
        self.wait(5)

        self.play(AnimationGroup(Transform(parabola, FunctionGraph(lambda x: (1/2)*((x - 2)) ** 2 - 3)),
                                 Transform(texto, TexMobject("f(x) = \\frac{1}{2}(x - 2)^2 - 3"
                                                                        ).add_background_rectangle().to_edge(UP)),
                                 run_time=3))
        self.wait(5)

        self.play(AnimationGroup(Transform(parabola, FunctionGraph(lambda x: (-2) * ((x - 2)) ** 2 - 3)),
                                 Transform(texto, TexMobject("f(x) = -2(x - 2)^2 - 3"
                                                             ).add_background_rectangle().to_edge(UP)),
                                 run_time=3))
        self.wait(5)

        self.play(AnimationGroup(Transform(parabola, FunctionGraph(lambda x: ((1 / 2) * (x - 2)) ** 2 + 3)),
                                 Transform(texto, TexMobject("f(x) = \\frac{1}{2}(x - 2)^2 + 3"
                                                             ).add_background_rectangle().to_edge(UP)),
                                 run_time=3))
        self.wait(5)






