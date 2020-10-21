import sys
from itertools import chain

sys.path.append("/home/gustavomello/PycharmProjects/remat")
from more_itertools import grouper

from manimlib.imports import *

from aulas import TabelaDeDefinições, Cena


class RecapitulandoSoma(Cena):
    def construct(self):
        eixo_x = NumberLine(x_max=2 * FRAME_X_RADIUS, x_min=-2 * FRAME_X_RADIUS, line_to_number_buff=MED_LARGE_BUFF)
        referência = eixo_x.get_number_mobjects().copy()
        self.play(ShowCreation(eixo_x), Write(referência))
        self.wait(1)
        self.play(ApplyMethod(eixo_x.shift, 3*RIGHT),
                  Write(descrição := TexMobject("+3").scale(2).to_edge(UP)),
                  run_time=2)
        self.wait(1)
        self.play(FadeOut(descrição))
        self.wait(1)
        self.play(ApplyMethod(eixo_x.shift, 3*LEFT),
                  Write(descrição := TexMobject("-3").scale(2).to_edge(UP)),
                  run_time=2)
        self.wait(3)


class RecapitulandoMultiplicação(Cena):
    def construct(self):
        eixo_x = NumberLine(x_max=2 * FRAME_X_RADIUS, x_min=-2 * FRAME_X_RADIUS, line_to_number_buff=1.2*MED_LARGE_BUFF)
        referência = eixo_x.get_number_mobjects().copy()
        ponto_da_unidade = Dot(RIGHT, color=YELLOW)

        self.play(ShowCreation(eixo_x), ShowCreation(ponto_da_unidade), Write(referência))
        self.wait(1)
        self.play(ApplyMethod(eixo_x.scale, 2),
                  ApplyMethod(ponto_da_unidade.shift, RIGHT),
                  Write(descrição := TexMobject("\\times 2").scale(2).to_edge(UP)),
                  run_time=2)
        self.wait(1)
        self.play(FadeOut(descrição))
        self.wait(1)
        self.play(ApplyMethod(eixo_x.scale, 1/2),
                  ApplyMethod(ponto_da_unidade.shift, LEFT),
                  Write(descrição := TexMobject("\\divisionsymbol 2").scale(2).to_edge(UP)),
                  run_time=2)
        self.wait(3)


class RecapitulandoSomaComplexa(Cena):
    def construct(self):
        número = TexMobject("+ (3 + 2i)").scale(2).to_edge(UP).add_background_rectangle()
        self.add_foreground_mobject(número)
        plano = ComplexPlane(x_min=-2*FRAME_X_RADIUS,
                             x_max=2*FRAME_X_RADIUS,
                             y_min=-2*FRAME_Y_RADIUS,
                             y_max=2*FRAME_Y_RADIUS)
        referência = plano.get_coordinate_labels().copy()
        alvo = Dot(3*RIGHT + 2*UP, color=YELLOW)
        bala = Dot(color=YELLOW)
        self.play(ShowCreation(plano), ShowCreation(referência), run_time=3)
        self.play(FadeIn(alvo), FadeIn(bala))
        self.play(ApplyMethod(plano.shift, 3*RIGHT + 2*UP),
                  ReplacementTransform(bala, alvo),
                  run_time=3)
        self.wait(3)


class RecapitulandoMultiplicaçãoComplexa(Cena):
    def construct(self):
        número = TexMobject("\\times (3 + 2i)").scale(2).to_edge(UP).add_background_rectangle()
        self.add_foreground_mobject(número)
        plano = ComplexPlane(x_min=-2 * FRAME_X_RADIUS,
                             x_max=2 * FRAME_X_RADIUS,
                             y_min=-2 * FRAME_Y_RADIUS,
                             y_max=2 * FRAME_Y_RADIUS)
        plano_de_fundo = ComplexPlane(color=LIGHT_GREY, background_line_style={"stroke_color": DARK_GREY})
        referência = plano.get_coordinate_labels().copy()
        alvo = Dot(3 * RIGHT + 2 * UP, color=YELLOW)
        bala = Dot(RIGHT, color=YELLOW)
        self.add(plano_de_fundo)
        self.play(ShowCreation(plano), ShowCreation(referência), run_time=3)
        self.play(FadeIn(alvo), FadeIn(bala))
        self.play(ApplyMethod(plano.apply_function, lambda v: (3*v[0] - 2*v[1])*RIGHT + (2*v[0] + 3*v[1])*UP),
                  ReplacementTransform(bala, alvo),
                  run_time=3)
        self.wait(3)


class RecapitulandoMultiplicaçãoComplexa(Cena):
    def construct(self):
        número = TexMobject("\\times (3 + 2i)").scale(2).to_edge(UP).add_background_rectangle()
        self.add_foreground_mobject(número)
        plano = ComplexPlane(x_min=-2 * FRAME_X_RADIUS,
                             x_max=2 * FRAME_X_RADIUS,
                             y_min=-2 * FRAME_Y_RADIUS,
                             y_max=2 * FRAME_Y_RADIUS)
        plano_de_fundo = ComplexPlane(color=LIGHT_GREY, background_line_style={"stroke_color": DARK_GREY})
        referência = plano.get_coordinate_labels().copy()
        alvo = Dot(3 * RIGHT + 2 * UP, color=YELLOW)
        bala = Dot(RIGHT, color=YELLOW)
        self.add(plano_de_fundo)
        self.play(ShowCreation(plano), Write(referência), run_time=3)
        self.play(FadeIn(alvo), FadeIn(bala))
        self.play(ApplyMethod(plano.apply_function, lambda v: (3*v[0] - 2*v[1])*RIGHT + (2*v[0] + 3*v[1])*UP),
                  ReplacementTransform(bala, alvo),
                  run_time=3)
        self.wait(3)


class RecapitulandoIQuadrado(Cena):
    def construct(self):
        número = TexMobject("i^2").scale(2).to_edge(UP).add_background_rectangle()
        self.add_foreground_mobject(número)
        plano = ComplexPlane(x_min=-2 * FRAME_X_RADIUS,
                             x_max=2 * FRAME_X_RADIUS,
                             y_min=-2 * FRAME_Y_RADIUS,
                             y_max=2 * FRAME_Y_RADIUS)
        plano_de_fundo = ComplexPlane(color=LIGHT_GREY, background_line_style={"stroke_color": DARK_GREY})
        referência = plano.get_coordinate_labels().copy()
        ponto = Dot(RIGHT, color=YELLOW)
        self.add(plano_de_fundo)
        self.play(ShowCreation(plano), Write(referência), run_time=3)
        self.play(FadeIn(ponto))
        self.play(Rotate(plano, angle=PI/2), Rotate(ponto, angle=PI/2, about_point=ORIGIN), run_time=2)
        self.wait()
        self.play(Rotate(plano, angle=PI/2), Rotate(ponto, angle=PI/2, about_point=ORIGIN), run_time=2)
        self.wait(4)


TabelaDeDefinições.definições.update({"Número": "Uma abstração dos conceitos de intensidade e sentido. \\\\",
                                      "Soma": "Resultado da Mistura de Quantidades.",
                                      "Multiplicação": "Adição repetida.",
                                      "Potência": "Multiplicação repetida."})


class TabelaDeDefiniçõesARecapitulando(TabelaDeDefinições):
    def construct(self):
        self.apresentar_se()
        self.atualizar_definição("Número", "Uma abstração dos conceitos de intensidade, direção e\\\\"
                                           " sentido.")
        self.atualizar_definição("Soma", "Translação da reta real ou plano complexo.")
        self.atualizar_definição("Multiplicação", "Transformação da reta real ou plano complexo.")


class ÁrvoreExponencial(Cena):
    def crescer_árvore_com_base_(self, base=2):
        nó_inicial = Dot(color=YELLOW)
        níveis = [[nó_inicial]]
        ramos = []
        comprimento_do_braço_maior = 7*(1 - 1/base)

        for geração in range(1, 5):
            y = -geração
            n = base**geração
            comprimento_do_braço_do_nível = ((base**2) * (comprimento_do_braço_maior))/(n)

            x_0 = -sum([comprimento_do_braço_maior/(base**k) for k in range(geração)])
            nós_do_nível_atual = [Dot((x_0 + comprimento_do_braço_do_nível*k)*RIGHT + y*UP, color=YELLOW)
                                  for k in range(n)]

            níveis.append(nós_do_nível_atual)

            nós_do_nível_anterior = níveis[geração - 1]
            ramos_novos = [Line(nós_do_nível_anterior[i].get_center(), nó.get_center(), stroke_width=0.75)
                           for (i, nós) in enumerate(grouper(nós_do_nível_atual, base))
                           for nó in nós]
            ramos.append(ramos_novos)

        VGroup(*chain(*níveis, *ramos)).center()

        for i, nível in enumerate(níveis):
            if i == 0:
                self.play(ShowCreation(nó_inicial))
            else:
                self.play(ShowCreation(VGroup(*ramos[i - 1])),
                          ShowCreation(VGroup(*nível)),
                          run_time=2)


class ÁrvoreÚnica(ÁrvoreExponencial):
    def construct(self):
        self.crescer_árvore_com_base_(2)


class PropriedadeMaisImportante(Cena):
    def construct(self):
        self.título_de_seção("$ e^{a + b} = e^a \\times e^b $")


class ExponencialReal(Cena):
    n_antes = 0

    def ir_para_(self, n):
        self.play(ApplyMethod(self.eixo_da_soma.apply_function,
                              lambda v: v + ((n - self.n_antes)*RIGHT)),
                  ApplyMethod(self.eixo_da_multiplicação.apply_function,
                              lambda v: np.array([2**(n - self.n_antes) * v[0],
                                                  v[1],
                                                  v[2]])),
                  run_time=3)
        self.n_antes = n
        self.wait(2)

    def construct(self):
        frame_da_soma = VGroup(eixo_da_soma := NumberLine(x_max=2 * FRAME_X_RADIUS,
                                                          x_min=-2 * FRAME_X_RADIUS,
                                                          line_to_number_buff=MED_LARGE_BUFF),
                               título_da_soma := TextMobject("Soma").next_to(eixo_da_soma, UP),
                               referência_da_soma := eixo_da_soma.get_number_mobjects().copy()
                               ).shift(2*UP)

        frame_da_multiplicação = VGroup(eixo_da_multiplicação := NumberLine(x_max=5 * FRAME_X_RADIUS,
                                                                            x_min=-5 * FRAME_X_RADIUS,
                                                                            line_to_number_buff=MED_LARGE_BUFF),
                                        título_da_multiplicação := TextMobject("Multiplicação"
                                                                               ).next_to(eixo_da_multiplicação, UP),
                                        referência_da_multiplicação := eixo_da_multiplicação.get_number_mobjects(
                                                                                             ).copy()
                                        ).shift(2*DOWN)

        self.play(ShowCreation(frame_da_soma), ShowCreation(frame_da_multiplicação), run_time=3)
        self.wait(2)

        self.eixo_da_soma = eixo_da_soma
        self.eixo_da_multiplicação = eixo_da_multiplicação

        self.ir_para_(2)
        self.ir_para_(3)
        self.ir_para_(-1)
        self.ir_para_(-2)
        self.ir_para_(0.5)
        self.ir_para_(0)


class MultiplicaçãoComplexaRodaEEstica(Cena):
    def construct(self):
        número = TexMobject("\\times (3 + 2i)").scale(2).to_edge(UP).add_background_rectangle()
        self.add_foreground_mobject(número)
        plano = ComplexPlane(x_min=-2 * FRAME_X_RADIUS,
                             x_max=2 * FRAME_X_RADIUS,
                             y_min=-2 * FRAME_Y_RADIUS,
                             y_max=2 * FRAME_Y_RADIUS)
        plano_de_fundo = ComplexPlane(color=LIGHT_GREY, background_line_style={"stroke_color": DARK_GREY})
        referência = plano.get_coordinate_labels().copy()
        alvo = Dot(3 * RIGHT + 2 * UP, color=YELLOW)
        bala = Dot(RIGHT, color=YELLOW)
        self.add(plano_de_fundo)
        self.play(ShowCreation(plano), Write(referência), run_time=3)
        self.play(FadeIn(alvo), FadeIn(bala))
        self.play(ApplyMethod(plano.scale, np.sqrt(13)),
                  ApplyMethod(bala.shift, (np.sqrt(13) - 1)*RIGHT),
                  run_time=3)
        self.wait(2)
        self.play(Rotate(plano, np.arctan(2/3)),
                  Rotate(bala, np.arctan(2/3), about_point=ORIGIN),
                  run_time=3)
        self.wait(3)


class ExponencialComplexa(Cena):
    b_antes = 0

    def ir_para_(self, b):
        self.play(ApplyMethod(self.ponto_imaginário.shift, (b - self.b_antes)*UP),
                  Rotate(self.plano, np.log(2)*(b - self.b_antes)),
                  Rotate(self.ponto_que_roda_com_o_plano, np.log(2)*(b - self.b_antes), about_point=ORIGIN),
                  run_time=3)

        self.wait(2)
        self.b_antes = b

    def construct(self):
        self.plano = ComplexPlane(x_min=-2 * FRAME_X_RADIUS,
                                  x_max=2 * FRAME_X_RADIUS,
                                  y_min=-2 * FRAME_Y_RADIUS,
                                  y_max=2 * FRAME_Y_RADIUS)
        plano_de_fundo = ComplexPlane(color=LIGHT_GREY, background_line_style={"stroke_color": DARK_GREY})
        self.add(plano_de_fundo)

        referência = self.plano.get_coordinate_labels().copy()
        self.play(ShowCreation(self.plano), Write(referência), run_time=3)

        self.ponto_imaginário = Dot(color=YELLOW)
        self.ponto_que_roda_com_o_plano = Dot(RIGHT, color=YELLOW)

        indicador_de_b = TexMobject("bi"
                         ).add_background_rectangle(
                         ).scale(0.7
                         ).add_updater(lambda t: t.next_to(self.ponto_imaginário))
        indicador_de_exponencial = TexMobject("2^{bi}"
                                   ).add_background_rectangle(
                                   ).scale(0.7
                                   ).add_updater(lambda t: t.next_to(self.ponto_que_roda_com_o_plano))

        self.play(ShowCreation(self.ponto_imaginário),
                  Write(indicador_de_b),
                  ShowCreation(self.ponto_que_roda_com_o_plano),
                  Write(indicador_de_exponencial),
                  run_time=3)

        self.ir_para_(1)
        self.ir_para_(3)
        self.ir_para_(0)
        self.ir_para_(-1)
        self.ir_para_(0.5)
        self.ir_para_(-2)
        self.ir_para_(4)
        self.ir_para_(-20)

        self.wait(5)


class CircunferênciaComplexa(Cena):
    def construct(self):
        plano = ComplexPlane()
        referência = plano.get_coordinate_labels().copy()
        self.play(ShowCreation(plano), Write(referência), run_time=3)

        ponto = Dot(RIGHT, color=YELLOW)
        caminho = Arc(angle=PI)

        def conseguir_arco_a_partir_do_(ponto):
            x, y, _ = ponto.get_center()
            if x >= 0:
                return np.arctan(y/x)
            elif x < 0:
                return np.arctan(y/x) + PI

        indicador_de_b = TexMobject("b =").scale(1.5)
        b = DecimalNumber(0,
                          show_ellipsis=True,
                          num_decimal_places=5,
                          include_sign=True,
                          ).scale(1.5
                          ).add_updater(lambda x: x.next_to(indicador_de_b)
                          ).add_updater(lambda x: x.set_value(conseguir_arco_a_partir_do_(ponto)))

        indicador_do_expoente = TexMobject("e^{bi}").add_background_rectangle().add_updater(lambda x: x.next_to(ponto))

        self.play(ShowCreation(ponto))
        self.add_foreground_mobject(ponto)
        self.play(Write(VGroup(indicador_de_b, b).center().to_edge(UP).add_background_rectangle()),
                  Write(indicador_do_expoente))

        self.play(Rotate(ponto, PI, about_point=ORIGIN),
                  ShowCreation(caminho),
                  run_time=15,
                  rate_func=linear)
        self.wait(4)

        indicador_de_teta = TexMobject("\\theta =").scale(1.5).move_to(indicador_de_b)
        indicador_do_expoente_teta = TexMobject("e^{\\theta i}"
                                     ).add_background_rectangle(
                                     ).move_to(indicador_do_expoente)

        self.play(Transform(indicador_de_b, indicador_de_teta),
                  Transform(indicador_do_expoente, indicador_do_expoente_teta),
                  run_time=3)


class CircunferênciaTrigonométrica(Cena):
    def construct(self):
        plano = ComplexPlane().scale(2)
        referência = plano.get_coordinate_labels().copy()
        self.play(ShowCreation(plano), Write(referência), run_time=3)

        self.wait(1)

        circunferência = Circle(radius=2, color=WHITE)
        self.play(ShowCreation(circunferência))

        ponto = Dot(2*RIGHT, color=YELLOW)
        self.play(ShowCreation(ponto))
        self.add_foreground_mobject(ponto)
        self.play(Rotate(ponto, PI/3, about_point=ORIGIN),
                  Write(TexMobject("\\theta = \\pi/3").scale(1.5).to_edge(UP).add_background_rectangle()))
        self.play(ShowCreation(Line(ORIGIN, (v := ponto.get_center()))))

        self.wait(3)

        self.play(ShowCreation(DashedLine(v, v[1]*UP)))

        self.wait(3)

        self.play(ShowCreation(DashedLine(v, v[0]*RIGHT)))

        self.wait(3)

        self.play(ShowCreation(Line(2*(RIGHT + 5*DOWN), 2*(RIGHT + 5*UP))))
        self.wait()
        self.play(ShowCreation(Line(v, 10*v)),
                  ShowCreation(Dot(2*v, color=YELLOW)))

        self.wait(3)

        self.play(ShowCreation(Line(2*(UP+ 5*LEFT), 2*(UP + 5*RIGHT))))
        self.play(ShowCreation(Dot(2*(UP + (1/np.tan(PI/3))*RIGHT), color=YELLOW)))

        self.wait(3)

        self.play(ShowCreation(Line(cossec := 2*(1/np.sin(PI/3))*UP, sec := 2*(1/np.cos(PI/3))*RIGHT)))
        self.wait()
        self.play(ShowCreation(Dot(sec, color=YELLOW)))
        self.wait()
        self.play(ShowCreation(Dot(cossec, color=YELLOW)))

        self.wait(3)


class Poincaré(Cena):
    def construct(self):
        título = self.título_de_seção("Poincaré", escala=3, espera=0)
        novo_título = título.copy()
        citação = TextMobject('"Notação importa"').next_to(novo_título, DOWN)

        VGroup(novo_título, citação).center()
        self.play(Transform(título, novo_título),
                  Write(citação),
                  runt_time=2)



