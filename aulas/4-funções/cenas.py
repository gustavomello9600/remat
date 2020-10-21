import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from manimlib.imports import *

from aulas import TabelaDeDefinições, Cena


class FunçãoMindBlown(ThreeDScene):
    def construct(self):
        setA = VGroup(regionA := Circle(radius=1, color=BLUE, fill_color=BLUE, fill_opacity=0.2).shift(2.7*LEFT),
                      labelA := TexMobject("A").next_to(regionA, UP))
        setB = VGroup(regionB := Circle(radius=3, color=YELLOW, fill_color=YELLOW, fill_opacity=0.2).shift(2.7*RIGHT),
                      labelB := TexMobject("B").next_to(regionB, UP))
        self.set_camera_orientation(phi=0, theta=-PI/2)
        self.play(FadeInFromPoint(setA, setA.get_center()))
        self.play(FadeInFromPoint(setB, setB.get_center()))

        elements_in_A = [VGroup(dot := SmallDot(regionA.get_center()
                                                + np.array([0.5 * np.cos(i*TAU/5),
                                                            0.5 * np.sin(i*TAU/5),
                                                            0])),
                                label := TexMobject(f"{i + 1}").scale(0.5).next_to(dot, UP,
                                                                                   buff=SMALL_BUFF))
                         for i in range(5)]
        self.play(Write(VGroup(*elements_in_A)), run_time=2)

        elements_in_B = [VGroup(dot := SmallDot(regionB.get_center()
                                                + np.array([(0.5 + i*0.5) * np.cos(i * TAU / 5 + PI/3),
                                                            (0.5 + i*0.5) * np.sin(i * TAU / 5 + PI/3),
                                                            0])),
                                label := TexMobject(f"{(i + 1)**2}").scale(0.5).next_to(dot, UP,
                                                                                   buff=SMALL_BUFF))
                         for i in range(5)]
        self.play(Write(VGroup(*elements_in_B)), run_time=2)

        arrows = [CurvedArrow(start_point=elements_in_A[i].submobjects[0].get_center(),
                              end_point=elements_in_B[i].submobjects[0].get_center(),
                              stroke_width=1,
                              tip_length=0.2)
                  for i in range(5)]
        for arrow in arrows:
            self.play(Write(arrow))

        self.wait(5)

        new_elements_in_B = [VGroup(dot := SmallDot(regionB.get_center() + 1.5*DOWN
                                                    + np.array([0.5 * np.cos(i * TAU / 5),
                                                                0.5 * np.sin(i * TAU / 5),
                                                                0])),
                                    label := TexMobject(f"{(i + 1) ** 2}").scale(0.5).next_to(dot, UP,
                                                                                              buff=SMALL_BUFF))
                             for i in range(5)]

        new_arrows = [CurvedArrow(start_point=elements_in_A[i].submobjects[0].get_center(),
                                  end_point=new_elements_in_B[i].submobjects[0].get_center(),
                                  stroke_width=1,
                                  tip_length=0.2)
                      for i in range(5)]

        imA = VGroup(region_imA := Circle(radius=1, color=BLUE, fill_color=BLUE, fill_opacity=0.2
                                          ).move_to(regionB).shift(1.5*DOWN),
                     label_imA := TexMobject("?").next_to(region_imA, UP))

        self.play(FadeInFromPoint(imA, imA.get_center()),
                  ReplacementTransform(VGroup(*elements_in_B),
                                       VGroup(*new_elements_in_B)),
                  ReplacementTransform(VGroup(*arrows),
                                       VGroup(*new_arrows)),
                  run_time = 5)

        self.wait(10)

        self.move_camera(phi=PI/4, theta=-PI/4, run_time=4)
        self.begin_ambient_camera_rotation(rate=0.0075)
        self.play(FadeOut(VGroup(*new_arrows)), run_time=3)

        self.play(ApplyMethod(VGroup(setA, *elements_in_A).shift, 2.7*RIGHT + 1.5*DOWN + 1.5*OUT),
                  ApplyMethod(VGroup(setB, imA, *new_elements_in_B).shift, 2.7*LEFT - 1.5*OUT),
                  run_time=5)

        self.wait(6)

        arrows = [Vector(3*RIGHT,
                         stroke_width=1,
                         tip_length=0.2
                         ).rotate_about_origin(PI/2, UP).shift(element.submobjects[0].get_center())
                  for element in elements_in_A]
        for arrow in arrows:
            self.play(Write(arrow))

        self.wait(3)
        self.play(FadeOut(VGroup(region_imA, *new_elements_in_B)))
        self.play(TransformFromCopy(VGroup(regionA, *elements_in_A), VGroup(region_imA, *new_elements_in_B)),
                  ReplacementTransform(label_imA, true_label := TexMobject("Im(f)").next_to(region_imA, UP)),
                  run_time=3)

        self.wait(5)
        self.play(FadeOut(VGroup(*arrows, *elements_in_A, *new_elements_in_B)))

        not_injective_imA = VGroup(region_not_injective_imA := Circle(radius=0.75, color=RED,
                                                                      fill_color=RED, fill_opacity=0.2
                                                                      ).move_to(region_imA),
                                   label_not_injective_imA := TexMobject("Im(g)").next_to(region_not_injective_imA, UP))

        self.wait(3)

        backup_imA = imA.deepcopy()
        self.remove(true_label)
        self.play(ReplacementTransform(imA, not_injective_imA))
        self.wait(5)
        self.remove(not_injective_imA)
        self.play(ReplacementTransform(imA, backup_imA))

        self.wait(10)

        newB = VGroup(region_newB := Circle(radius=1, color=YELLOW, fill_color=YELLOW, fill_opacity=0.2
                                            ).move_to(region_imA),
                      label_newB := TexMobject("B").next_to(region_newB, UP)
                      ).rotate(PI/3, about_point=region_newB.get_center())
        self.play(ReplacementTransform(setB, newB), run_time=3)
        self.add(imA)

        for arrow in arrows:
            self.play(Write(arrow))

        self.wait(4)
        new_arrows = [arrow.deepcopy().rotate(PI, UP) for arrow in arrows]

        self.play(ReplacementTransform(VGroup(*arrows), VGroup(*new_arrows)), run_time=3)

        self.wait(10)