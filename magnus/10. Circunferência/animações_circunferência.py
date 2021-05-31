import numpy as np
from manimlib.imports import *


class LugarGeométrico(Scene):
    def construct(self):
        título = TextMobject("Lugar Geométrico").scale(3)
        self.play(Write(título), run_time=3)
        self.wait(3)


class IntroduçãoAParabola(Scene):
    def construct(self):
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


class Circunferência(Scene):
    def construct(self):
        centro = Dot(ORIGIN)
        circunferência = Circle(radius=2)
        ponto = Dot(2*RIGHT, color=RED)
        raio = Line(ORIGIN, 2*RIGHT)

        self.play(ShowCreation(centro))
        self.wait()
        self.play(ShowCreation(raio), ShowCreation(ponto))
        self.play(ShowCreation(circunferência),
                  Rotate(ponto, angle=2*PI, about_point=ORIGIN),
                  Rotate(raio, angle=2*PI, about_point=ORIGIN),
                  run_time=3)
        self.wait(3)


class GrausDeLiberdade(Scene):
    def construct(self):
        circunferência = Circle().scale(2)
        centro = Dot(ORIGIN)
        extremidade = Dot(2*RIGHT)

        chaves = always_redraw(lambda : Brace(Line(centro, extremidade), DOWN))

        descrição, raio = etiqueta = VGroup(
            TexMobject("r = "),
            DecimalNumber(
                2,
                show_ellipsis=True,
                num_decimal_places=2
            )
        )
        etiqueta.arrange(RIGHT).add_background_rectangle()

        f_always(raio.set_value, extremidade.get_x)
        always(etiqueta.next_to, chaves, DOWN)

        self.add(circunferência, centro, extremidade)
        self.wait()
        self.play(Write(chaves), Write(etiqueta), run_time=3)
        self.wait(3)
        self.play(ApplyMethod(circunferência.scale, 3/2), ApplyMethod(extremidade.move_to, 3*RIGHT), run_time=2)
        self.wait(2)
        self.play(ApplyMethod(circunferência.scale, 1/3), ApplyMethod(extremidade.move_to, 1*RIGHT), run_time=2)
        self.wait(2)
        self.play(ApplyMethod(circunferência.scale, 4), ApplyMethod(extremidade.move_to, 4*RIGHT), run_time=2)
        self.wait(2)
        self.play(ApplyMethod(circunferência.scale, 1/2), ApplyMethod(extremidade.move_to, 2*RIGHT), run_time=2)
        self.wait(3)
        self.play(ApplyMethod(circunferência.scale, 1/4), ApplyMethod(extremidade.move_to, RIGHT/2), run_time=5)
        self.wait(5)


class Simetria(Scene):
    def construct(self):
        título = TextMobject("Simetria").scale(3)
        self.play(Write(título), run_time=3)
        self.wait(3)


class DemonstraçãoDeSimetria1(ThreeDScene):
    def construct(self):
        triângulo = Polygon(np.array([-2, -2, 0]),
                            np.array([+2, -2, 0]),
                            np.array([0, 2, 0]),
                            color=BLUE,
                            fill_color=BLUE,
                            fill_opacity=0.5)
        axes = ThreeDAxes()

        self.play(FadeInFromPoint(triângulo, ORIGIN), run_time=3)
        self.wait()
        self.move_camera(phi=45 * DEGREES, theta=-80*DEGREES, added_anims=[ShowCreation(axes)], run_time=2)
        self.begin_ambient_camera_rotation(rate=0.05)
        self.wait(3)

        eixo = Line(3*UP, 3*DOWN, color=RED, stroke_width=4)
        self.play(Write(eixo))
        self.wait()
        face_dobrada = Polygon(np.array([0, -2, 0]),
                               np.array([+2, -2, 0]),
                               np.array([0, 2, 0]),
                               color=YELLOW,
                               fill_color=YELLOW,
                               fill_opacity=0.5)
        self.play(Rotate(face_dobrada, about_edge=LEFT, angle=-PI, axis=UP), run_time=3)
        self.wait(3)


class DemonstraçãoDeSimetria2(ThreeDScene):
    def construct(self):
        triângulo = Polygon(np.array([-2.5, -3, 0]),
                            np.array([+2, -2, 0]),
                            np.array([0, 2, 0]),
                            color=BLUE,
                            fill_color=BLUE,
                            fill_opacity=0.5)
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=45 * DEGREES, theta=-80*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.05)

        self.play(FadeInFromPoint(triângulo, ORIGIN), run_time=3)
        self.wait(3)

        eixo = Line(3.5*UP, 3.5*DOWN, color=RED, stroke_width=4)
        self.play(Write(eixo))
        self.wait()
        face_dobrada = Polygon(np.array([0, -2.5, 0]),
                               np.array([+2, -2, 0]),
                               np.array([0, 2, 0]),
                               color=YELLOW,
                               fill_color=YELLOW,
                               fill_opacity=0.5)
        self.play(Rotate(face_dobrada, about_edge=LEFT, angle=-PI, axis=UP), run_time=3)
        erro = Polygon(np.array([-2.5, -3, 0]),
                               np.array([0, -2.5, 0]),
                               np.array([-2, -2, 0]),
                               color=RED,
                               fill_color=RED,
                               fill_opacity=0.5)
        self.play(FadeIn(erro))
        self.wait(3)


class DemonstraçãoDeSimetria3(ThreeDScene):
    def construct(self):
        círculo = Circle(color=BLUE, fill_color=BLUE, fill_opacity=0.5).scale(2)
        eixo = DashedLine(2.5*DOWN, 2.5*UP, color=RED, stroke_width=3, stroke_opacity=1)
        self.play(FadeIn(círculo), run_time=3)
        self.play(ShowCreation(eixo), run_time=2)
        self.play(Rotate(eixo), run_time=5)
        self.wait()
        self.play(Rotate(eixo, angle=-5*PI/2), run_time=3)
        self.wait(5)


class ComprimentoDaCircunferência(Scene):
    círculo = Circle(color=WHITE, radius=2)
    interno = RegularPolygon(3).scale(2).move_to(círculo, aligned_edge=UP)
    externo = RegularPolygon(3).scale(2/np.cos(PI/3)).move_to(círculo, aligned_edge=DOWN)
    n = 3

    def gerar_polígono_interno(self, n, radius=2):
        polígono = RegularPolygon(n).scale(radius)
        if n % 2 == 1:
            polígono.move_to(self.círculo, aligned_edge=UP)
        return polígono

    def gerar_polígono_externo(self, n, radius=2):
        theta = TAU/n
        polígono = RegularPolygon(n).scale(radius/np.cos(theta/2))
        if n % 2 == 1:
            polígono.move_to(self.círculo, aligned_edge=DOWN)
        return polígono

    def update_n_to(self, n=2):
        self.n = n
        self.play(Transform(self.interno, self.gerar_polígono_interno(n)),
                  Transform(self.externo, self.gerar_polígono_externo(n)),
                  run_time=2)
        self.wait(2)

    def construct(self):
        self.play(ShowCreation(self.círculo),
                  run_time=3)
        self.wait(3)
        self.play(ShowCreation(self.externo),
                  ShowCreation(self.interno),
                  run_time=2)
        self.wait(3)

        self.update_n_to(4)
        self.update_n_to(5)
        self.update_n_to(6)
        self.update_n_to(10)
        self.update_n_to(20)
        self.wait(5)
        self.update_n_to(6)
        self.wait(3)

        self.play(FadeOut(self.externo))

        self.play(ApplyMethod(VGroup(*self.get_mobjects()).shift, 3.5*LEFT), run_time=2)
        self.wait(10)


class RelaçõesComRetas(Scene):
    def rodar_ponto(self, ponto, teta, t=1):
        self.play(Rotate(ponto, teta, about_point=ORIGIN), run_time=t)

    def gerar_secante(self):
        meio = (self.ponto_1.get_center() + self.ponto_2.get_center())/2
        if not np.isclose(self.ponto_1.get_center(), self.ponto_2.get_center()).all():
            direção = self.ponto_1.get_center() - self.ponto_2.get_center()
        else:
            direção = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]) @ self.ponto_1.get_center()
        direção_unitária = direção/(np.sqrt(direção.dot(direção)))
        return Line(meio - 3.5*direção_unitária,
                    meio + 3.5*direção_unitária,
                    color=YELLOW)

    def construct(self):
        círculo = Circle(color=WHITE, radius=2)

        teta_1 = 40*DEGREES
        teta_2 = 70*DEGREES

        self.ponto_1 = Dot(np.cos(teta_1)*2*RIGHT + np.sin(teta_1)*2*UP, color=YELLOW)
        self.ponto_2 = Dot(np.cos(teta_2)*2*RIGHT + np.sin(teta_2)*2*UP, color=YELLOW)

        secante = always_redraw(self.gerar_secante)

        self.play(ShowCreation(círculo), run_time=2)
        self.wait()
        self.play(ShowCreation(self.ponto_1), ShowCreation(self.ponto_2))
        self.wait(3)
        self.play(ShowCreation(secante))
        self.wait()
        self.rodar_ponto(self.ponto_2, 40*DEGREES, t=3)
        self.wait(3)
        self.rodar_ponto(self.ponto_1, -240 * DEGREES, t=3)
        self.wait(3)
        self.rodar_ponto(self.ponto_2, -130 * DEGREES, t=3)
        self.wait(3)
        self.rodar_ponto(self.ponto_1, 180 * DEGREES, t=5)
        self.wait(3)


