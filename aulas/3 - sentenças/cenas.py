import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from manimlib.imports import *

from aulas import TabelaDeDefinições, Cena

TabelaDeDefinições.definições.update({"Número": "Uma abstração dos conceitos de intensidade, direção e\\\\"
                                                " sentido.",
                                      "Soma": "Translação da reta real ou plano complexo.",
                                      "Multiplicação": "Transformação da reta real ou plano complexo.",
                                      "Potência": "Multiplicação repetida."})


class TabelaDeDefiniçõesARecapitulando(TabelaDeDefinições):
    def construct(self):
        self.apresentar_se()
        self.atualizar_definição("Potência", "Uma tradução entre soma e multiplicação.")


class SignificanteSignificadoCarro(Cena):
    def construct(self):
        self.título_de_seção("Carro")


class SignificanteSignificadoNúmero(Cena):
    def construct(self):
        self.título_de_seção("3", escala=5)


class Organon(Cena):
    def construct(self):
        self.título_de_seção("Organon", escala=4)


class OQueÉMatemática(Cena):
    def construct(self):
        self.título_de_seção("Matemática")


class MatemáticaComoLinguagem(Cena):
    def construct(self):
        self.título_de_seção("""
        \\begin{math}
        \\begin{aligned}
        cm &= b^2 \\ \\ \\wedge \\\\
        cn &= a^2 \\to \\\\
        \\\\
        c(m + n) &= a^2 \\to \\\\
        c^2 &= a^2 + b^2
        \\end{aligned}
        \\end{math}""", escala=1)


class MatemáticaComoNaEscola(Cena):
    def construct(self):
        self.título_de_seção("""
        \\begin{math}
        \\begin{aligned}
        x^2 - 7x + 12  &= 0 \\\\
        (x - 3)(x - 4) &= 0 \\\\
        x' = 3 \\ x'' = 4  
        \\end{aligned}
        \\end{math}""", escala=1)


class MatemáticaCerta(Cena):
    def construct(self):
        self.título_de_seção("""
        \\begin{math}
        \\begin{aligned}
        x^2 - 7x + 12  &= 0 \\to \\\\
        (x - 3)(x - 4) &= 0 \\to \\\\
        x = 3 \\ \\lor \\ x = 4  
        \\end{aligned}
        \\end{math}""", escala=1)


class Sentenças(Cena):
    def construct(self):
        self.título_de_seção("Sentenças")


class Elementos(Cena):
    def construct(self):
        self.título_de_seção("Elementos")


class Teorema(Cena):
    def construct(self):
        self.título_de_seção("Teorema")


class Insight(Cena):
    def construct(self):
        self.título_de_seção("Uma gramática \\\\ dos números")
        objetos = self.get_mobjects_from_last_animation()
        self.play(Transform(objetos[0], TextMobject("Uma gramática \\\\ dos padrões").scale(3)))
        self.wait(3)