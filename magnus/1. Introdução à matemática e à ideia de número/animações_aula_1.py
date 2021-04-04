from manimlib.imports import *


class Título(Scene):
    def construct(self):
        texto = TextMobject("Introdução\\\\"
                            "à Matemática").scale(3)
        self.play(Write(texto), run_time=3)
        self.wait(3)

class Número(Scene):
    def construct(self):
        três = TextMobject("3").scale(5)
        self.play(Write(três, run_time=5))
        self.wait(2)


class José(Scene):
    def construct(self):
        josé = TextMobject("José").scale(3)
        self.play(Write(josé, run_time=3))
        self.wait(3)


class Rio(Scene):
    def construct(self):
        river = SVGMobject("river", stroke_width=0.1).scale(2)
        self.play(Write(river), run_time=3)
        self.wait(3)


class Maçãs(Scene):
    def construct(self):
        apple = SVGMobject("apple", stroke_width=0.1, color=RED, fill_color=RED).scale(0.4)
        self.play(Write(apple), run_time=3)
        self.wait(3)
        equi = Triangle()
        vértices = equi.get_vertices()
        apple2 = SVGMobject("apple", stroke_width=0.1, color=RED, fill_color=RED).scale(0.4)
        apple3 = SVGMobject("apple", stroke_width=0.1, color=RED, fill_color=RED).scale(0.4)

        new_apples = [apple2, apple3]

        for i, vértice in enumerate(vértices[1:]):
            new_apples[i].move_to(vértice)

        self.play(AnimationGroup(ApplyMethod(apple.move_to, vértices[0]),
                                 Write(apple2),
                                 Write(apple3)),
                  run_time=3)

        self.wait(3)


class BO(Scene):

    def construct(self):
        palitinho = TextMobject("|")

        palitos = self.enfileirar_palitos(palitinho, 17, 43).center()

        self.play(Write(palitos), run_time=5)

        self.wait(20)

        self.play(ApplyMethod(palitos.to_edge, LEFT), run_time=3)

        novos_palitos = self.enfileirar_palitos(palitinho, 14, 42)
        palitos_enfileirados = VGroup(*[novos_palitos.submobjects[i // 3 + 14 * (i % 3)] for i in range(43)]
                                      ).next_to(ORIGIN, buff=DEFAULT_MOBJECT_TO_EDGE_BUFFER)
        excedente = palitinho.deepcopy().next_to(novos_palitos.submobjects[13])

        for i, palito in enumerate(palitos.submobjects):
            if i == 43:
                self.play(Transform(palito, excedente, path_arc=30*DEGREES), run_time=10/43)
            else:
                self.play(Transform(palito, palitos_enfileirados.submobjects[i], path_arc=30*DEGREES),
                          run_time=10/43)
        self.wait(3)


    @staticmethod
    def enfileirar_palitos(palito, palitos_por_linha, palitos_totais):
        palitinhos = [palito.deepcopy()]
        for i in range(palitos_totais):
            if i % palitos_por_linha == palitos_por_linha - 1:
                novo_palito = palito.deepcopy().next_to(palitinhos[i - palitos_por_linha + 1], DOWN)
            else:
                novo_palito = palito.deepcopy().next_to(palitinhos[i])
            palitinhos.append(novo_palito)

        return VGroup(*palitinhos)



class Familiar(Scene):
    def construct(self):
        texto = TextMobject("Familiar?").scale(3)
        self.play(Write(texto, run_time=3))
        self.wait(3)


class Expressão(Scene):
    def construct(self):
        expressão = TexMobject(r"\frac{n_o \times (1 + i)^t}{n_f}").scale(2)
        self.play(Write(expressão, run_time=5))
        self.wait(3)


class SistemaDeNumeração(Scene):
    def construct(self):
        pergunta = TextMobject("Por quê 1\\\\"
                               "e não |?").scale(2.5)
        self.play(Write(pergunta, run_time=5))
        self.wait(2)


class IndoArábico(Scene):
    def construct(self):
        resposta = TextMobject("Indo-arábico").scale(2.5)
        self.play(Write(resposta, run_time=5))
        self.wait(2)


class Abstração(Scene):
    def construct(self):
        enunciado = TextMobject("Princípio da Abstração").scale(2).to_edge(LEFT, buff=3*DEFAULT_MOBJECT_TO_EDGE_BUFFER)
        self.play(Write(enunciado, run_time=3))
        self.wait(2)


class Bônus(Scene):
    def construct(self):
        despedida = TextMobject("O que é Matemática?").scale(2)
        self.play(Write(despedida, run_time=5))
        self.wait(2)
