from manimlib.imports import *


class Título(Scene):
    def construct(self):
        texto = TextMobject("Introdução\\\\"
                            "à Matemática").scale(3)
        self.play(Write(texto), run_time=3)
        self.wait(3)


class Apresentação(Scene):
    def construct(self):
        gustavo = TextMobject("Gustavo Mello").scale(1.5)
        nota_gustavo = TextMobject("942,9 pts.", color=YELLOW)

        gabriel = TextMobject("Gabriel Luciano").scale(1.5)
        nota_gabriel = TextMobject("920,8 pts.", color=YELLOW)

        def formar_bloco(pessoa, nota):
            ligadura_na_nota = nota.get_corner(UL)
            ligadura_na_pessoa = pessoa.get_corner(DL)
            ajuste = ligadura_na_pessoa - ligadura_na_nota

            nota.shift(ajuste + DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*DOWN)

            return VGroup(pessoa, nota)

        k = 1

        bloco_gustavo = formar_bloco(gustavo, nota_gustavo).to_edge(LEFT, buff=4*DEFAULT_MOBJECT_TO_EDGE_BUFFER).shift(k*UP)
        bloco_gabriel = formar_bloco(gabriel, nota_gabriel).to_edge(LEFT, buff=4*DEFAULT_MOBJECT_TO_EDGE_BUFFER).shift(k*DOWN)

        self.play(Write(bloco_gustavo))
        self.wait(1)
        self.play(Write(bloco_gabriel))


class Número(Scene):
    def construct(self):
        três = TextMobject("3").scale(5)
        self.play(Write(três, run_time=5))
        self.wait(2)


class José(Scene):
    def construct(self):
        josé = TextMobject("José").scale(3)
        self.play(Write(josé, run_time=5))
        self.wait(2)


class Ovelhas(Scene):
    def construct(self):
        ovelha = SVGMobject("sheep")
        self.play(Write(ovelha))
        self.wait(3)


class Familiar(Scene):
    def construct(self):
        texto = TextMobject("Familiar?").scale(3)
        self.play(Write(texto, run_time=5))
        self.wait(2)


class Expressão(Scene):
    def construct(self):
        expressão = TexMobject(r"\frac{n_o \times (1 + i)^t}{n_f}").scale(2)
        self.play(Write(expressão, run_time=5))
        self.wait(2)


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
        self.play(Write(enunciado, run_time=5))
        self.wait(2)


class QueTal(Scene):
    def construct(self):
        despedida = TextMobject("Que tal?").scale(2)
        self.play(Write(despedida, run_time=5))
        self.wait(2)
