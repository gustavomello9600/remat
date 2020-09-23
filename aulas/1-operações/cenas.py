import sys
sys.path.append("/home/gustavomello/PycharmProjects/remat")

from manimlib.imports import *

from aulas import TabelaDeDefinições, Cena


class TabelaDeDefiniçõesARetrospectiva(TabelaDeDefinições):
    def construct(self):
        self.apresentar_se()


class EAgoraJosé(Cena):
    def construct(self):
        self.título_de_seção("E agora, José?")


class SinalDeX(Cena):
    def construct(self):
        self.título_de_seção("$\\times$", escala=5)


class MostrarCriaçãoDoEixoX(Cena):
    def construct(self):
        eixo_x = NumberLine()
        self.play(ShowCreation(eixo_x), run_time=3)


class TabelaDeDefiniçõesBAtualizarNúmero(TabelaDeDefinições):
    def construct(self):
        self.apresentar_se()
        self.atualizar_definição("Número", "Uma abstração dos conceitos de intensidade e sentido")


class TabelaDeDefiniçõesCAdicionarOperações(TabelaDeDefinições):
    def construct(self):
        self.apresentar_se(definições=TabelaDeDefiniçõesBAtualizarNúmero.definições)
        self.wait(1)
        self.adicionar_definição("Soma", "Resultado da mistura de quantidades.")
        self.wait(1)
        self.adicionar_definição("Multiplicação", "Adição repetida.")
        self.wait(1)
        self.adicionar_definição("Potência", "Multiplicação repetida.")
        self.wait(1)


class IdaSoma3(Cena):
    def construct(self):
        eixo_x = NumberLine(x_max=2*FRAME_X_RADIUS, x_min=-2*FRAME_X_RADIUS, line_to_number_buff=MED_LARGE_BUFF)
        referência = eixo_x.get_number_mobjects().copy()
        self.play(ShowCreation(eixo_x), Write(referência))
        self.wait(1)
        self.play(ApplyMethod(eixo_x.shift, 3*RIGHT), run_time=2)
        self.wait(2)


class VoltaSoma3(Cena):
    def construct(self):
        eixo_x = NumberLine(x_max=2*FRAME_X_RADIUS, x_min=-2*FRAME_X_RADIUS)
        self.add(eixo_x.shift(3*RIGHT))
        self.wait(1)
        self.play(ApplyMethod(eixo_x.shift, 3*LEFT), run_time=2)
        self.wait(2)


class IdaMult2(Cena):
    def construct(self):
        eixo_x = NumberLine(xmax=2*FRAME_X_RADIUS, xmin=-2*FRAME_X_RADIUS)
        ponto1 = Dot(RIGHT, color=YELLOW)
        self.add(eixo_x)
        self.play(FadeIn(ponto1))
        self.wait(1)
        self.play(ApplyMethod(eixo_x.scale, 2), ApplyMethod(ponto1.shift, RIGHT), run_time=2)
        self.wait(2)


class Mult2Mult2(Cena):
    def construct(self):
        eixo_x = NumberLine(xmax=2 * FRAME_X_RADIUS, xmin=-2 * FRAME_X_RADIUS)
        ponto1 = Dot(RIGHT, color=YELLOW)
        self.add(eixo_x)
        self.play(FadeIn(ponto1))
        self.wait(1)
        self.play(ApplyMethod(eixo_x.scale, 2), ApplyMethod(ponto1.shift, RIGHT), run_time=2)
        self.wait(2)
        self.play(ApplyMethod(eixo_x.scale, 2), ApplyMethod(ponto1.shift, 2*RIGHT), run_time=2)
        self.wait(2)


class Virar1Virar1(Cena):
    def construct(self):
        eixo_x = NumberLine(xmax=2 * FRAME_X_RADIUS, xmin=-2 * FRAME_X_RADIUS)
        ponto1 = Dot(RIGHT, color=YELLOW)
        self.add(eixo_x)
        self.play(FadeIn(ponto1))
        self.wait(1)
        self.play(ApplyMethod(eixo_x.scale, -1), ApplyMethod(ponto1.shift, 2*LEFT), run_time=2)
        self.wait(2)
        self.play(ApplyMethod(eixo_x.scale, -1), ApplyMethod(ponto1.shift, 2*RIGHT), run_time=2)
        self.wait(2)


class VoltaMult2(Cena):
    def construct(self):
        eixo_x = NumberLine(xmax=2*FRAME_X_RADIUS, xmin=-2*FRAME_X_RADIUS).scale(2)
        ponto1 = Dot(2*RIGHT, color=YELLOW)
        self.add(eixo_x)
        self.add(ponto1)
        self.wait(1)
        self.play(ApplyMethod(eixo_x.scale, 1/2), ApplyMethod(ponto1.shift, LEFT), run_time=2)
        self.wait(2)


class MostrarCriaçãoPlanoComplexo(Cena):
    def construct(self):
        plano = ComplexPlane()
        self.play(ShowCreation(plano), run_time=4)
        self.wait(3)


class MultiplicaçãoPori(Cena):
    def construct(self):
        ponto = Dot(RIGHT, color=YELLOW)
        plano = ComplexPlane()
        self.add(plano)
        self.play(FadeIn(ponto))
        self.add_foreground_mobject(ponto)
        self.wait()
        self.play(Rotate(VGroup(ponto, plano), PI/2))
        self.wait()
        self.play(Rotate(VGroup(ponto, plano), PI/2))


class SomaComplexa(Cena):
    def construct(self):
        número = TexMobject("3 + 2i").to_edge(UP)
        self.add_foreground_mobject(número)
        plano = ComplexPlane(xmin=-2*FRAME_X_RADIUS,
                             xmax=2*FRAME_X_RADIUS,
                             ymin=-2*FRAME_Y_RADIUS,
                             ymax=2*FRAME_Y_RADIUS)
        alvo = Dot(3*RIGHT + 2*UP, color=BLUE)
        bala = Dot(color=YELLOW)
        self.play(ShowCreation(plano), run_time=3)
        self.play(FadeIn(alvo), FadeIn(bala))
        self.play(ApplyMethod(plano.shift, 3*RIGHT + 2*UP),
                  ReplacementTransform(bala, alvo),
                  FadeOut(alvo),
                  run_time=3)
        self.wait()


class MultiplicaçãoComplexa(Cena):
    def construct(self):
        número = TexMobject("3 + 2i").to_edge(UP)
        self.add_foreground_mobject(número)
        plano = ComplexPlane()
        alvo = Dot(3*RIGHT + 2*UP, color=BLUE)
        bala = Dot(RIGHT, color=YELLOW)
        self.add(plano, alvo, bala)
        self.play(ApplyMethod(plano.apply_function, lambda v: (3*v[0] - 2*v[1])*RIGHT + (2*v[0] + 3*v[1])*UP),
                  ReplacementTransform(bala, alvo),
                  run_time=3)
        self.wait()
