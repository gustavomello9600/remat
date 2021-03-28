from typing import Dict, ClassVar

from manimlib.imports import *


Vetor = np.ndarray


PADRÃO_DE_ESCALA_DA_FONTE_DE_DEFINIÇÃO = 1
DEFINIÇÕES = {"Número"              : "Uma abstração do conceito de quantidade.",
              "Sistema de Numeração": "Conjunto de símbolos e regras utilizados para representar \\\\ "
                                      "e manipular números."}


def snap(bullet: Mobject, target: Mobject, target_corner=DL, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER) -> None:
    bullet_corner = np.array([target_corner[0], -target_corner[1], 0])
    vetor_deslocamento = (target.get_corner(target_corner) - bullet.get_corner(bullet_corner)
                          + bullet_corner[1]*buff*DOWN)
    bullet.shift(vetor_deslocamento)


def identar(texto: Mobject, identação=0.6) -> None:
    texto.shift(RIGHT*identação)
    
    
def colar_no_canto(canto: Vetor, bala: Mobject, alvo: Mobject) -> None:
    vetor_deslocamento = alvo.get_corner(canto) - bala.get_corner(canto)
    bala.shift(vetor_deslocamento)


def ênfase(cena: Scene, text_mobject: TextMobject) -> None:
    texto_enfatizado = text_mobject.copy().scale(1.1).set_color(YELLOW)

    cena.remove(text_mobject)
    tmp_copy = text_mobject.copy()
    cena.play(ReplacementTransform(tmp_copy, texto_enfatizado))
    cena.remove(tmp_copy)
    cena.play(ReplacementTransform(texto_enfatizado, text_mobject))


class Cena(Scene):
    def título_de_seção(self, título, escala=3, tempo=3, espera=3):
        texto = TextMobject(título).scale(escala)
        self.play(Write(texto, run_time=tempo))
        self.wait(espera)
        return texto


class TabelaDeDefinições(Cena):
    texto_do_título: ClassVar[str] = "Tabela de Definições"
    definições: ClassVar[Dict[str, str]] = DEFINIÇÕES

    def apresentar_se(self, definições=None, estático=False):
        if definições is not None:
            self.definições = definições

        título = TextMobject(self.texto_do_título).scale(2).to_corner(UL)
        começo_da_linha = título.get_corner(DL)
        fim_da_linha = np.array([-começo_da_linha[0], começo_da_linha[1], começo_da_linha[2]])
        linha = Line(começo_da_linha, fim_da_linha).shift(DEFAULT_MOBJECT_TO_MOBJECT_BUFFER * DOWN)

        self.y_da_linha = linha.get_y()
        
        self.elementos = {}

        if not estático:
            self.play(Write(título))
            self.play(Write(linha))

        self.cabeçalho_geral = VGroup(título, linha).add_background_rectangle(opacity=1,
                                                                              buff=DEFAULT_MOBJECT_TO_EDGE_BUFFER)
        self.add_foreground_mobject(self.cabeçalho_geral)

        n = len(self.definições)
        anterior = linha
        animações = []
        for i, (conceito, definição) in enumerate(self.definições.items()):
            cabeçalho = TextMobject(f"{i + 1}. {conceito}")
            snap(cabeçalho, anterior, buff=1.5*DEFAULT_MOBJECT_TO_EDGE_BUFFER)

            corpo = TextMobject(definição, alignment="\\flushleft").scale(PADRÃO_DE_ESCALA_DA_FONTE_DE_DEFINIÇÃO)
            snap(corpo, cabeçalho)
            identar(corpo)

            if estático:
                self.add(cabeçalho, corpo)
            else:
                animações.append(AnimationGroup(Write(cabeçalho), Write(corpo), lag_ratio=0.5))

            self.elementos[conceito] = cabeçalho
            self.elementos["Definição de " + conceito] = corpo

            anterior = corpo.copy().shift(0.6*LEFT)

        if not estático:
            self.play(AnimationGroup(*animações, run_time=3, lag_ratio=1))
        
    def atualizar_definição(self, conceito: str, nova_definição) -> None:
        cabeçalho = self.elementos[conceito]
        corpo = self.elementos["Definição de " + conceito]

        self._rolar_até_definição(cabeçalho, corpo)
        ênfase(self, corpo)
        
        novo_corpo = TextMobject(nova_definição, alignment="\\flushleft").scale(PADRÃO_DE_ESCALA_DA_FONTE_DE_DEFINIÇÃO)
        snap(novo_corpo, cabeçalho)
        identar(novo_corpo)
        self.elementos["Definição de " + conceito] = novo_corpo

        self.play(ReplacementTransform(corpo, novo_corpo), run_time=3)

        self.definições.update({conceito: nova_definição})

    def adicionar_definição(self, conceito, definição):
        anterior = next(reversed(self.elementos.values())).copy().shift(0.6*LEFT)

        cabeçalho = TextMobject(f"{int(len(self.elementos)/2) + 1}. {conceito}")
        snap(cabeçalho, anterior, buff=1.5 * DEFAULT_MOBJECT_TO_EDGE_BUFFER)

        corpo = TextMobject(definição, alignment="\\flushleft").scale(PADRÃO_DE_ESCALA_DA_FONTE_DE_DEFINIÇÃO)
        snap(corpo, cabeçalho)
        identar(corpo)

        vetor_deslocamento = self._rolar_até_definição(cabeçalho, corpo)
        VGroup(cabeçalho, corpo).shift(vetor_deslocamento)
        self.play(AnimationGroup(Write(cabeçalho), Write(corpo), lag_ratio=0.5))

        self.elementos[conceito] = cabeçalho
        self.elementos["Definição de " + conceito] = corpo
        self.definições.update({conceito: definição})

    def _rolar_até_definição(self, cabeçalho, corpo):
        desconto_do_cabeçalho_geral = (FRAME_Y_RADIUS - self.y_da_linha)/2 * DOWN

        vetor_deslocamento = VGroup(cabeçalho, corpo).get_center()[1] * DOWN + desconto_do_cabeçalho_geral
        if vetor_deslocamento[1] < 0:
            vetor_deslocamento = ORIGIN

        bloco_de_definições = VGroup(*self.elementos.values())
        self.play(ApplyMethod(bloco_de_definições.shift, vetor_deslocamento), run_time=2)

        return vetor_deslocamento



class Implementação(TabelaDeDefinições):
    def construct(self):
        self.apresentar_se()
        self.atualizar_definição("Número", "Abstrações que representam intensidade e direção.")
        self.atualizar_definição("Operações", "Ações performadas na reta real.")
        self.adicionar_definição("Completude", "Propriedade de uma operação em relação a um \\\\ "
                                               "conjunto numérico que garante que quaisquer \\\\"
                                               "elementos por ela operados resultarão em um \\\\"
                                               "número ainda pertencente ao conjunto.")
