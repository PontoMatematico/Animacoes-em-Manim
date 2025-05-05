# O que é integral

from manim import *
import numpy as np

# Introdução
class vid0(MovingCameraScene):
    def construct(self):

        ax1 = Axes(x_range=[-1, 11], x_length=8,
                   y_range=[-0.75, 6], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0)
        ax1_x_label = always_redraw(lambda: MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2))
        ax1_y_label = always_redraw(lambda: MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2))

        def f(x):
            return 0.07*(x-2-0)*(x-2-PI)*(x-2-2*PI) + 2.5

        gr1 = ax1.plot(f, x_range=[-1, 10], stroke_width=4, color=BLUE).set_z_index(10)
        gr1_label = MathTex('y = f(x)', color=BLUE).next_to(gr1, RIGHT).shift(UP*6.8+LEFT*0.1).scale(0.9)

        X = ValueTracker(2)
        f8 = always_redraw(lambda: ax1.get_area(
            gr1,
            x_range=(2, X.get_value()),
            color=(PURPLE, ORANGE)
            ).set_fill(opacity=0.7).set_stroke(opacity=0))
        
        t1 = MathTex('A = \: ?').shift(UP*1.8+LEFT)
        t1_line = Line(t1.get_bottom(), Dot(radius=0).shift(DOWN*1.5+RIGHT*0), buff=0.25, color=WHITE).set_z_index(11)
        
            # Criando o gráfico
        self.play(LaggedStart(FadeIn(ax1), FadeIn(ax1_x_label, ax1_y_label), Create(gr1), FadeIn(gr1_label), lag_ratio=0.3))
        self.wait(2)
        self.add(f8)
        self.play(LaggedStart(X.animate.set_value(8),
                              FadeIn(t1, t1_line),
                              lag_ratio=0.3), run_time=2)
        self.wait(2)
        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)



# Áreas de retângulo e triângulo
class vid1(MovingCameraScene):
    def construct(self):

            # Retângulo
        f1 = Polygon((0,0,0),
                     (0,1,0),
                     (2,1,0),
                     (2,0,0), color=BLUE, fill_opacity=0.5).scale(1.7).move_to(ORIGIN).shift(DOWN*1)
        f1_new = Polygon((0,0,0),
                     (0,1,0),
                     (2,1,0),
                     (2,0,0),
                     (1.5,0,0), color=BLUE, fill_opacity=0.5).scale(1.7).move_to(ORIGIN).shift(DOWN*1)
        f1_base = Polygon(f1.get_corner(DL), f1.get_corner(DL), f1.get_corner(DR), f1.get_corner(DR), color=BLUE)

        f1_b_brace = Brace(f1, DOWN, color=GRAY)
        f1_b_label = MathTex('b', color=BLUE).next_to(f1_b_brace, DOWN)

        f1_a_brace = Brace(f1, RIGHT, color=GRAY)
        f1_a_label = MathTex('a', color=BLUE).next_to(f1_a_brace, RIGHT)

        f1_t = MathTex(r'A ( \:\:\:\:\:\:\: ) = b \cdot a').next_to(f1, UP, buff=1)
        f1_t[0][4:].set_color(BLUE)
        f1_t[0][5].set_color(WHITE)

        f1_t_figure = f1.copy().scale(0.2).move_to(f1_t[0][1]).shift(RIGHT*0.47)
        f1_t_figure_base = Polygon(f1_t_figure.get_corner(DL), f1_t_figure.get_corner(DL), f1_t_figure.get_corner(DR), f1_t_figure.get_corner(DR), color=BLUE)

        self.play(FadeIn(f1_t[0][0:4], f1))
        self.wait(2)
        self.play(GrowFromEdge(f1_t_figure_base, LEFT),
                  FadeIn(f1_t[0][4:6]),
                  GrowFromEdge(f1_b_brace, LEFT),
                  GrowFromPoint(f1_b_label, f1_b_brace.get_corner(DL)))
        self.wait(2)
        self.play(ReplacementTransform(f1_t_figure_base, f1_t_figure),
                  FadeIn(f1_t[0][6]),
                  GrowFromEdge(f1_a_brace, DOWN),
                  GrowFromPoint(f1_a_label, f1_a_brace.get_corner(DR)))
        self.wait(2)
        self.remove(f1).add(f1_new)
        self.wait(2)



            # Triângulo
        f2 = Polygon((0,0,0),
                     (1.5,1,0),
                     (2,0,0), color=RED, fill_opacity=0.7).scale(1.7).move_to(ORIGIN).shift(DOWN*1).set_z_index(2)
        f2_base = Polygon((0,0,0), (1.5,0,0), (2,0,0), color=RED).scale(1.7).move_to(f2, aligned_edge=DOWN).set_z_index(2)

        f2_t = MathTex(r'A ( \:\:\:\:\:\:\: ) = \frac{b \cdot a}{2}').move_to(f1_t, aligned_edge=LEFT).shift(UP*0.05)
        f2_t[0][4:7].set_color(RED).shift(LEFT*0.05)
        f2_t[0][5].set_color(WHITE)

        f2_t_figure = f2.copy().scale(0.2).move_to(f1_t[0][1]).shift(RIGHT*0.47)
        f2_t_figure_base = f2_base.copy().scale(0.2).move_to(f2_t_figure, aligned_edge=DOWN).set_z_index(-1)

        
        
        # Aparece o triângulo
        f1_t_copy = f1_t.copy().shift(UP*1.5)
        self.add(f2_t_figure_base)
        self.play(TransformFromCopy(f1_t, f1_t_copy),
                  f1_t_figure.animate.move_to(f1_t_copy[0][1]).shift(RIGHT*0.47),
                  FadeIn(f2_base))
        self.wait(2)

        aux1 = Polygon((0,0,0),
                       (0,1,0),
                       (2,1,0),
                       (2,0,0),
                       (1.5,1,0), color=BLUE, fill_opacity=0.5).scale(1.7).move_to(f1, aligned_edge=UL)
        self.play(ReplacementTransform(f2_base, f2),
                  ReplacementTransform(f2_t_figure_base, f2_t_figure),
                  ReplacementTransform(f1_new, aux1),
                  f1_b_label.animate.set_color(RED),
                  f1_a_label.animate.set_color(RED))
        self.wait(2)

        # A área do triângulo é metade da área do retângulo
        f2_hl_1 = Polygon((0,0,0),
                          (1.5,1,0),
                          (0,1,0)).set_color(BLUE).set_fill(opacity=0.5).scale(1.7).move_to(f1, aligned_edge=UL)
        f2_hl_2 = Polygon((2,0,0),
                          (1.5,1,0),
                          (2,1,0)).set_color(BLUE).set_fill(opacity=0.5).scale(1.7).move_to(f1, aligned_edge=UR)

        self.remove(aux1).add(f2_hl_1, f2_hl_2)
        self.wait(2)
        self.remove(f1_new)
        self.play(LaggedStart(Rotate(f2_hl_2, -180*DEGREES),
                              Rotate(f2_hl_1, 180*DEGREES),
                              lag_ratio=0.2),
                  LaggedStart(ReplacementTransform(f1_t[0][4:7], f2_t[0][4:7]),
                              FadeIn(f2_t[0][7:]),
                              lag_ratio=0.2),
                              run_time=1.5)
        self.wait(2)
        self.play(FadeOut(f2_hl_1, f2_hl_2))
        self.wait(2)

        # Destaque nas fórmulas
        aux2 = VGroup(f2, f1_a_brace, f1_a_label, f1_b_brace, f1_b_label)
        self.play(self.camera.frame.animate.move_to(VGroup(f1_t_copy, f2_t)),
                  aux2.animate.shift(DOWN*2.5),
                  run_time=1.5)
        self.wait(2)

        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)



# Áreas de polígonos
class vid2(MovingCameraScene):
    def construct(self):
        
        FILL_OPACITY = 0.5

            # Figura 3 
        f3 = Polygon((0,0,0),
                     (0,1,0),
                     (3,2,0),
                     (3,0,0), color=WHITE, fill_opacity=FILL_OPACITY)
        f3_part_1 = Polygon((0,0,0),
                            (0,1,0),
                            (3,1,0),
                            (3,0,0), color=BLUE, fill_opacity=FILL_OPACITY)
        f3_part_2 = Polygon((0,1,0),
                            (3,2,0),
                            (3,1,0), color=RED, fill_opacity=FILL_OPACITY)
        f3_parts = VGroup(f3_part_1, f3_part_2)
        


            # Figura 4
        f4 = Polygon((0,0,0),
                     (0,1,0),
                     (1.5,2,0),
                     (3,1,0),
                     (3,0,0), color=WHITE, fill_opacity=FILL_OPACITY)
        f4_part_1 = Polygon((0,0,0),
                            (0,1,0),
                            (3,1,0),
                            (3,0,0), color=BLUE, fill_opacity=FILL_OPACITY) 
        f4_part_2 = Polygon((0,1,0),
                            (1.5,2,0),
                            (3,1,0), color=RED, fill_opacity=FILL_OPACITY)      
        f4_parts = VGroup(f4_part_1, f4_part_2)
        

            # Figura 5
        f5 = Polygon((0,0,0),
                     (-0.5,2,0),
                     (1.5,1,0),
                     (3.5,2,0),
                     (3,0,0), color=WHITE, fill_opacity=FILL_OPACITY)
        f5_part_1 = Polygon((0,0,0),
                            (-0.5,2,0),
                            (1.5,1,0), color=RED, fill_opacity=FILL_OPACITY)
        f5_part_2 = Polygon((0,0,0),
                            (1.5,1,0),
                            (3,0,0), color=RED, fill_opacity=FILL_OPACITY)
        f5_part_3 = Polygon((1.5,1,0),
                            (3.5,2,0),
                            (3,0,0), color=RED, fill_opacity=FILL_OPACITY)
        f5_parts = VGroup(f5_part_1, f5_part_2, f5_part_3)


            # Figura 6
        f6 = Polygon((0,0,0),
                     (1,1.5,0),
                     (0.5,2.25,0),
                     (1.5,3,0),
                     (2.5,2.25,0),
                     (2,1.5,0),
                     (3,0,0), color=WHITE, fill_opacity=FILL_OPACITY)
        f6_part_1 = Polygon((0,0,0),
                            (1,1.5,0),
                            (1,0,0), color=RED, fill_opacity=FILL_OPACITY)
        f6_part_2 = Polygon((2,0,0),
                            (2,1.5,0),
                            (3,0,0), color=RED, fill_opacity=FILL_OPACITY)
        f6_part_3 = Polygon((1,0,0),
                            (1,1.5,0),
                            (2,1.5,0),
                            (2,0,0), color=BLUE, fill_opacity=FILL_OPACITY)
        f6_part_4 = Polygon((1,1.5,0),
                            (2,1.5,0),
                            (2.5,2.25,0), color=RED, fill_opacity=FILL_OPACITY)
        f6_part_5 = Polygon((1,1.5,0),
                            (0.5,2.25,0),
                            (2.5,2.25,0), color=RED, fill_opacity=FILL_OPACITY)
        f6_part_6 = Polygon((1.5,3,0),
                            (0.5,2.25,0),
                            (2.5,2.25,0), color=RED, fill_opacity=FILL_OPACITY)
        f6_parts = VGroup(f6_part_1, f6_part_2, f6_part_3, f6_part_4, f6_part_5, f6_part_6)


            # Figura 7
        f7 = Polygon((0, 0, 0),
                     (1, 0, 0),
                     (1, 1, 0),
                     (0.5, 1, 0),
                     (1.5, 2, 0),
                     (2.5, 1, 0),
                     (2, 1, 0),
                     (2, 0, 0),
                     (3, 0, 0),
                     (3, -0.5, 0),
                     (0, -0.5, 0), color=WHITE, fill_opacity=FILL_OPACITY)
        f7_part_1 = Polygon((0, 0, 0),
                            (3, 0, 0),
                            (3, -0.5, 0),
                            (0, -0.5, 0), color=BLUE, fill_opacity=FILL_OPACITY)
        f7_part_2 = Polygon((1, 1, 0),
                            (2, 1, 0),
                            (2, 0, 0),
                            (1, 0, 0), color=BLUE, fill_opacity=FILL_OPACITY)
        f7_part_3 = Polygon((0.5, 1, 0),
                            (2.5, 1, 0),
                            (1.5, 2, 0), color=RED, fill_opacity=FILL_OPACITY)
        f7_parts = VGroup(f7_part_1, f7_part_2, f7_part_3)

        

            # Figura curva
        ax1 = Axes(x_range=[-1, 11], x_length=8,
                   y_range=[-0.75, 6], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.6).scale(0.6)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        def f(x):
            return 0.1*(x-2-0)*(x-2-PI)*(x-2-2*PI) + 2.5
        
        gr1 = ax1.plot(f, x_range=[0+2, 2*PI+2], stroke_width=4, color=BLUE)

        f8 = ax1.get_area(
                gr1,
                x_range=(0+2, 2*PI+2),
                color=WHITE
                ).set_fill(opacity=FILL_OPACITY).set_stroke(width=2, opacity=1).set_z_index(-2)
        
        f8_part_1 = Polygon(ax1.c2p(0+2,0),
                            ax1.c2p(PI+2,0),
                            ax1.c2p(PI+2,f(PI+2)),
                            ax1.c2p(0+2,f(PI+2)), color=BLUE, fill_opacity=FILL_OPACITY)
        f8_part_2 = Polygon(ax1.c2p(PI+2,0),
                            ax1.c2p(2*PI+2,0),
                            ax1.c2p(2*PI+2,f(6.955)),
                            ax1.c2p(PI+2,f(6.955)), color=BLUE, fill_opacity=FILL_OPACITY)
        f8_part_3 = Polygon(ax1.c2p(0+2,f(PI+2)),
                            ax1.c2p(PI+2,f(PI+2)),
                            ax1.c2p(3.328,f(3.328)), color=RED, fill_opacity=FILL_OPACITY)
        f8_part_4 = Polygon(ax1.c2p(PI+2,f(6.955)),
                            ax1.c2p(PI+2,f(PI+2)),
                            ax1.c2p(6.955,f(6.955)), color=RED, fill_opacity=FILL_OPACITY)
        f8_part_5 = Polygon(ax1.c2p(2*PI +2,f(6.955)),
                            ax1.c2p(2*PI +2,f(2*PI +2)),
                            ax1.c2p(6.955,f(6.955)), color=RED, fill_opacity=FILL_OPACITY)
        
        f8_parts = VGroup(f8_part_1, f8_part_2, f8_part_3, f8_part_4, f8_part_5).set_z_index(-1)


        figures = VGroup(VGroup(f3, f3_parts).scale(0.5), 
                         VGroup(f4, f4_parts).scale(0.5),
                         VGroup(f5, f5_parts).scale(0.5),
                         VGroup(f6, f6_parts).scale(0.5),
                         VGroup(f7, f7_parts).scale(0.5),
                         VGroup(f8, f8_parts))
        figures.arrange(RIGHT, buff=1.1, aligned_edge=DOWN)
        VGroup(f8, f8_parts).shift(RIGHT)

        for fig in figures:
            fig.set_stroke(width=2, opacity=1)

        f3_part_1.save_state()
        f3_part_2.save_state()
        
        f4_part_1.save_state()
        f4_part_2.save_state()
        
        f5_part_1.save_state()
        f5_part_2.save_state()
        f5_part_3.save_state()
        
        f6_part_1.save_state()
        f6_part_2.save_state()
        f6_part_3.save_state()
        f6_part_4.save_state()
        f6_part_5.save_state()
        f6_part_6.save_state()

        f7_part_1.save_state()
        f7_part_2.save_state()
        f7_part_3.save_state()

        self.camera.frame.move_to(figures[0:5])


        self.play(LaggedStart(FadeIn(f3),
                              FadeIn(f4),
                              FadeIn(f5),
                              FadeIn(f6),
                              FadeIn(f7),
                              lag_ratio=0.3))
        self.wait(2)
        self.play(LaggedStart(AnimationGroup(f3.animate.set_opacity(0), FadeIn(f3_parts)),
                              AnimationGroup(f4.animate.set_opacity(0), FadeIn(f4_parts)),
                              AnimationGroup(f5.animate.set_opacity(0), FadeIn(f5_parts)),
                              AnimationGroup(f6.animate.set_opacity(0), FadeIn(f6_parts)),
                              AnimationGroup(f7.animate.set_opacity(0), FadeIn(f7_parts)),
                              lag_ratio=0.3))
        self.wait(2)
        self.play(f3_part_1.animate.shift(DOWN*0.1), 
                  f3_part_2.animate.shift(UP*0.1),

                  f4_part_1.animate.shift(DOWN*0.1),
                  f4_part_2.animate.shift(UP*0.1), 

                  f5_part_1.animate.shift(UL*0.1),
                  f5_part_2.animate.shift(DOWN*0.1),
                  f5_part_3.animate.shift(UR*0.1),

                  f6_part_1.animate.shift(DOWN*0.1+LEFT*0.2),
                  f6_part_2.animate.shift(DOWN*0.1+RIGHT*0.2),
                  f6_part_3.animate.shift(DOWN*0.1),
                  f6_part_4.animate.shift(UP*0.1+RIGHT*0.2),
                  f6_part_5.animate.shift(UP*0.1+LEFT*0.2),
                  f6_part_6.animate.shift(UP*0.3),
                  
                  f7_part_1.animate.shift(DOWN*0.1),
                  f7_part_2.animate.shift(UP*0.1),
                  f7_part_3.animate.shift(UP*0.3))
        self.wait(2)
        self.play(f3_part_1.animate.restore(),
                  f3_part_2.animate.restore(),
 
                  f4_part_1.animate.restore(),
                  f4_part_2.animate.restore(),

                  f5_part_1.animate.restore(),
                  f5_part_2.animate.restore(),
                  f5_part_3.animate.restore(),

                  f6_part_1.animate.restore(),
                  f6_part_2.animate.restore(),
                  f6_part_3.animate.restore(),
                  f6_part_4.animate.restore(),
                  f6_part_5.animate.restore(),
                  f6_part_6.animate.restore(),

                  f7_part_1.animate.restore(),
                  f7_part_2.animate.restore(),
                  f7_part_3.animate.restore())
        self.wait(2)




        self.add(f8)
        self.wait(2)
        AUX1 = 5.5
        self.play(self.camera.frame.animate.move_to(f8),
                  f8.animate.scale(1.5),
                  LaggedStart(figures[0].animate.shift(LEFT*AUX1),
                              figures[1].animate.shift(LEFT*AUX1),
                              figures[2].animate.shift(LEFT*AUX1),
                              figures[3].animate.shift(LEFT*AUX1),
                              figures[4].animate.shift(LEFT*AUX1),
                              lag_ratio=0.1),
                  run_time=3)
        self.wait(2)
        f8_parts.scale(1.5)
        self.play(f8.animate.set_fill(opacity=0),
                  FadeIn(f8_parts))
        self.wait(2)
        self.play(FadeOut(f8_parts))
        self.wait(2)


# Área da figura curva
class vid3(MovingCameraScene):
    def construct(self):
        
        # Retomando elementos
        ax1 = Axes(x_range=[-1, 11], x_length=8,
                   y_range=[-0.75, 6], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0).scale(0.6).scale(1.5)
        ax1_x_label = always_redraw(lambda: MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2))
        ax1_y_label = always_redraw(lambda: MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*2.7+RIGHT*0.2))

        def f(x):
            return 0.1*(x-2-0)*(x-2-PI)*(x-2-2*PI) + 2.5

        gr1 = ax1.plot(f, x_range=[-1, 10], stroke_width=4, color=BLUE)
        gr1_aux = ax1.plot(lambda x: 0.1*(x-2-0)*(x-2-PI)*(x-2-2*PI) + 2.5 + 4, x_range=[-1, 10], stroke_width=4, color=BLUE)
        gr1_label = MathTex('y = f(x)', color=BLUE).next_to(gr1, RIGHT).shift(UP*7.78+LEFT*0.3).scale(0.9)
        
        f8 = ax1.get_area(
                gr1,
                x_range=(0+2, 2*PI+2),
                color=WHITE
                ).set_fill(opacity=0).set_stroke(width=2, opacity=1)
        self.add(f8)

        self.camera.frame.move_to(f8)


        
        # Aparecem os eixos e a função
        ax1.shift(DOWN*3+LEFT*4)
        self.wait(2)
        self.add(ax1_x_label, ax1_y_label)
        self.play(ax1.animate.move_to(ORIGIN).shift(DOWN*0), 
                  self.camera.frame.animate.move_to(ORIGIN),
                  run_time=2)
        self.wait(2)
        self.play(LaggedStart(Create(gr1),
                              FadeIn(gr1_label),
                              lag_ratio=0.5),
                              run_time=2)
        self.wait(2)



        # Podemos obter a altura da figura em qualquer ponto
        X1 = ValueTracker(2)
        height_dot = always_redraw(lambda: Dot(color=YELLOW).move_to(ax1.c2p(X1.get_value(), f(X1.get_value()))).set_z_index(2))
        height_line = always_redraw(lambda: Line(ax1.c2p(X1.get_value(),0), height_dot.get_center(), color=YELLOW).set_z_index(2))

        x_label = always_redraw(lambda: MathTex(rf'x', color=YELLOW).scale(0.8).next_to(height_line, DOWN, buff=0.15))
        fx_label = always_redraw(lambda: MathTex(rf'f(x)', color=YELLOW).scale(0.8).next_to(ax1.c2p(0,f(X1.get_value())), LEFT, buff=0.15))
        fx_line = always_redraw(lambda: DashedLine(height_dot.get_center(), ax1.c2p(0,f(X1.get_value())), color=YELLOW, stroke_opacity=0.5))

        self.add(height_dot, height_line, x_label, fx_label, fx_line)
        self.play(X1.animate.set_value(2*PI + 1.999), run_time=4, rate_func=linear)
        self.play(X1.animate.set_value(2), run_time=4, rate_func=linear)
        self.play(X1.animate.set_value(2*PI + 2), run_time=4, rate_func=linear)
        self.remove(height_dot, height_line, x_label, fx_label, fx_line)
        self.wait(2)
        


        # Desenvolvimento da soma de Riemann
        area = ax1.get_area(
                gr1_aux,
                x_range=(0+2, 2*PI+2),
                color=(PURPLE, ORANGE)
                ).set_fill(opacity=0.8).set_stroke(width=0)
        
        area.rotate(180*DEGREES).shift(UP*1.08).set_z_index(-2)
        area_aux1 = area.copy().set_color(BLACK).set_fill(opacity=1).set_stroke(width=3, opacity=1).set_z_index(-1)
        area_aux2 = Rectangle(width=10, height=5, color=BLACK, stroke_width=0, fill_opacity=1).next_to(ax1.c2p(5,0), DOWN, buff=0).set_z_index(-1)
        self.add(area_aux1, area_aux2)
        self.wait(2)

        self.play(area.animate.shift(DOWN*4), run_time=2)
        self.wait(2)
 
        a_label = MathTex('a').set_color(YELLOW).next_to(ax1.c2p(2,0), DOWN, buff=0.15)
        b_label = MathTex('b').set_color(YELLOW).next_to(ax1.c2p(2*PI + 2,0), DOWN, buff=0.15)

        self.play(LaggedStart(AnimationGroup(GrowFromCenter(a_label), Flash(a_label, num_lines=8)),
                              AnimationGroup(GrowFromCenter(b_label), Flash(b_label, num_lines=8)),
                              lag_ratio=0.3))
        self.play(VGroup(a_label, b_label).animate.set_color(WHITE))
        self.wait(2)



        # Subdividindo o intervalo [a,b] em 'n' subintervalos '\Delta x i'        
        n_list = [10, 16, 24, 34, 100]
        tick_groups = []

        for n in n_list:
            ticks = VGroup()
            for i in range(0, n + 1):
                tick = Line(ORIGIN, UP * 0.1, stroke_width=2)
                tick.move_to(ax1.c2p(2 + i * 2 * PI / n, 0))
                tick.set_z_index(2)
                ticks.add(tick)
            tick_groups.append(ticks)
        tick_groups[0].set_color(YELLOW)

        self.play(LaggedStart(*[FadeIn(tick) for tick in tick_groups[0]], lag_ratio=0.1))
        self.wait(2)

        delta_x_braces = []
        for i in range(1, 11):
            delta_x_i_brace = Brace(Line(ax1.c2p(2 + (i-1)*2*PI/10,0), ax1.c2p(2 + i*2*PI/10,0)), DOWN, buff=0.1, color=YELLOW)
            delta_x_braces.append(delta_x_i_brace)

        delta_x_labels = []
        for i in range(1, 11):
            delta_x_i_label = MathTex(rf'\Delta x', color=YELLOW).scale(0.8).next_to(delta_x_braces[i-1], DOWN, buff=0.1)
            delta_x_labels.append(delta_x_i_label)
        delta_x_n_label = MathTex(r'\Delta x_{n}', color=YELLOW).scale(0.6).next_to(delta_x_braces[9], DOWN, buff=0.1)
        delta_x_labels.append(delta_x_n_label)
        
        
        self.play(LaggedStart(FadeIn(delta_x_braces[4], delta_x_labels[4]),
                              lag_ratio=0.1))
        self.wait(2)



        # Retângulos sobre os subintervalos
            # Lista de dxs: mais subdivisões = mais retângulos
        dx_list = [2 * PI / n for n in [10, 16, 24, 34, 200]]

            # Retângulos achatados na base
        flat_rects = ax1.get_riemann_rectangles(
            ax1.plot(lambda x: 0, x_range=[2.629, 2 * PI + 2]),
            x_range=[2.629, 2 * PI + 2],
            dx=dx_list[0],
            input_sample_type="center"
        )
        for rect in flat_rects:
            rect.set_fill(GRAY, opacity=0.3)
            rect.set_stroke(width=0.5)

        # Gera lista de grupos de retângulos
        rect_list = []
        for dx in dx_list:
            rects = ax1.get_riemann_rectangles(gr1, x_range=[2, 2 * PI + 2], dx=dx, input_sample_type="center")
            for i, rect in enumerate(rects):
                rect.set_fill(color=interpolate_color(PURPLE, ORANGE, i / len(rects)), opacity=0.7)
                rect.set_stroke(width=0.5)
            rect_list.append(rects)

        # Primeiro retângulo
        X_HEIGHT_AUX = ValueTracker(2.314)
        rect_aux = always_redraw(lambda:
                           Polygon(ax1.c2p(2,0), ax1.c2p(2.628,0),
                           ax1.c2p(2.628,f(X_HEIGHT_AUX.get_value())), ax1.c2p(2,f(X_HEIGHT_AUX.get_value())),
                           fill_color=rect_list[0][0].get_color(), fill_opacity=0.7,
                           stroke_width=0.5, stroke_color=BLACK
                           ))
        flat_rect = Polygon(ax1.c2p(2,0), ax1.c2p(2.629,0), ax1.c2p(2.629,0), ax1.c2p(2,0)).set_stroke(width=0.5, color=BLACK).set_fill(GRAY, opacity=0.3)
    


        self.play(FadeOut(delta_x_braces[4], delta_x_labels[4]),
                  area.animate.set_opacity(0.3),
                  VGroup(*tick_groups[0]).animate.set_color(WHITE))
        self.play(ReplacementTransform(flat_rects, rect_list[0][1:]), 
                  ReplacementTransform(flat_rect, rect_aux),
                  run_time=1)
        self.wait(2)



        # Variando a altura do primeiro retângulo
        height_rect_dot = always_redraw(lambda: Dot(color=YELLOW).move_to(ax1.c2p(X_HEIGHT_AUX.get_value(), f(X_HEIGHT_AUX.get_value()))).set_z_index(2))
        height_rect_line = always_redraw(lambda: Line(ax1.c2p(X_HEIGHT_AUX.get_value(),0), height_rect_dot.get_center(), color=YELLOW).set_z_index(2))
        
        index = 1
        x_bar_label = always_redraw(lambda: MathTex(rf'\overline{{x}}_{index}', color=YELLOW).scale(0.8).next_to(height_rect_line, DOWN, buff=0.15))
        fx_bar_label = always_redraw(lambda: MathTex(rf'f(\overline{{x}}_{index})', color=YELLOW).scale(0.8).next_to(ax1.c2p(0,f(X_HEIGHT_AUX.get_value())), LEFT, buff=0.15))
        fx_bar_line = always_redraw(lambda: DashedLine(height_rect_dot.get_center(), ax1.c2p(0,f(X_HEIGHT_AUX.get_value())), color=YELLOW, stroke_opacity=0.5))

        self.play(FadeIn(height_rect_dot, height_rect_line),
                  a_label.animate.set_opacity(0.3))
        self.wait(2)
        self.play(FadeIn(x_bar_label, fx_bar_label, fx_bar_line))
        self.wait(2)
        self.wait(2)

        RUN_TIME_1 = 1.2
        self.play(X_HEIGHT_AUX.animate.set_value(2), run_time=RUN_TIME_1)
        self.play(X_HEIGHT_AUX.animate.set_value(2.628), run_time=RUN_TIME_1*1.2)
        self.play(X_HEIGHT_AUX.animate.set_value(2.314), run_time=RUN_TIME_1)
        self.wait(2)



        # Mostra as alturas dos outros retângulos
        self.remove(rect_aux).add(rect_list[0][0])

        self.wait(2)
        a_label.set_opacity(1)
        X_HEIGHT_AUX.set_value(2 + 0.314*3)
        index = 2
        self.play(X_HEIGHT_AUX.animate.set_value(2 + 0.314*3 + 0.0001))
        self.wait(2)

        X_HEIGHT_AUX.set_value(2 + 0.314*5)
        index = 3
        self.play(X_HEIGHT_AUX.animate.set_value(2 + 0.314*5 + 0.0001))
        self.wait(2)

        b_label.set_opacity(0.3)
        X_HEIGHT_AUX.set_value(2 + 0.314*19)
        index = "n"
        self.play(X_HEIGHT_AUX.animate.set_value(2 + 0.314*19 + 0.0001))
        self.wait(2)

        self.play(FadeOut(height_rect_dot, height_rect_line, x_bar_label, fx_bar_label, fx_bar_line),
                  b_label.animate.set_opacity(1))
        self.wait(2)



        # Calculando as áreas de cada retângulo e a área total
        A_text = MathTex(r'A \:\approx\:',
                         r'f(\overline{x}_1) \Delta x',
                         '\:+\:',
                         r'f(\overline{x}_2) \Delta x',
                         '\:+\:',
                         r'f(\overline{x}_3) \Delta x',
                         '\:+\:',
                         '\cdot \cdot \cdot',
                         '\:+\:',
                         r'f(\overline{x}_n) \Delta x'
                         ).scale(0.8).shift(UP*2).set_z_index(3)
        A_text_sr = SurroundingRectangle(A_text, color=BLACK, buff=0.2, fill_opacity=0.8, stroke_width=0).set_z_index(2)
        
        for text, rect in zip(
            [A_text[1], A_text[3], A_text[5], A_text[9]],
            [rect_list[0][0], rect_list[0][1], rect_list[0][2], rect_list[0][9]]
        ):
            text.set_color(rect.get_fill_color())

        A1 = A_text[1].copy().scale(0.9).shift(DOWN)
        A2 = A_text[3].copy().scale(0.9).shift(LEFT*1)
        A3 = A_text[5].copy().scale(0.9).shift(DOWN*0.5+LEFT*1)
        An = A_text[9].copy().scale(0.9).shift(DOWN*2.5+LEFT*0.5)

        Ai_srs = []
        for Ai in [A1, A2, A3, An]:
            Ai_sr = SurroundingRectangle(Ai, color=BLACK, buff=0.2, fill_opacity=0.8, stroke_width=0).set_z_index(2)
            Ai_srs.append(Ai_sr)

        Ai_lines = []
        for Ai, i in zip([A1, A2, A3, An], [0, 1, 2, 9]):
            Ai_line = Line(Ai, Dot(radius=0).move_to(rect_list[0][i].get_top()).shift(DOWN*0.5), buff=0.1).set_opacity(0.5).set_z_index(3)
            Ai_lines.append(Ai_line)

        self.play(FadeIn(A1, A2, A3, An, *Ai_lines, Ai_srs[0]))
        self.wait(2)
        self.play(LaggedStart(Indicate(A1[0:6], scale_factor=1.1),
                              Indicate(A2[0:6], scale_factor=1.1),
                              Indicate(A3[0:6], scale_factor=1.1),
                              Indicate(An[0:6], scale_factor=1.1),
                              lag_ratio=0.2))
        self.wait(2)
        self.play(LaggedStart(Indicate(A1[6:], scale_factor=1.1),
                              Indicate(A2[6:], scale_factor=1.1),
                              Indicate(A3[6:], scale_factor=1.1),
                              Indicate(An[6:], scale_factor=1.1),
                              lag_ratio=0.2))
        self.wait(2)
        self.play(LaggedStart(AnimationGroup(ReplacementTransform(A1, A_text[1]), FadeOut(Ai_lines[0], Ai_srs[0])),
                              AnimationGroup(ReplacementTransform(A2, A_text[3]), FadeOut(Ai_lines[1])),
                              AnimationGroup(ReplacementTransform(A3, A_text[5]), FadeOut(Ai_lines[2])),
                              AnimationGroup(ReplacementTransform(An, A_text[9]), FadeOut(Ai_lines[3])),
                              lag_ratio=0.1),
                  FadeIn(A_text_sr),
                  LaggedStart(FadeIn(A_text[0]), 
                              FadeIn(A_text[2]),
                              FadeIn(A_text[4]),
                              FadeIn(A_text[6]),
                              FadeIn(A_text[7]),
                              FadeIn(A_text[8]),
                              lag_ratio=0.1))
        self.wait(2)



        # Resumindo a soma com o somatório
        self.play(LaggedStart(Indicate(A_text[1][4]),
                              Indicate(A_text[3][4]),
                              Indicate(A_text[5][4]),
                              Indicate(A_text[9][4]),
                              lag_ratio=0.8))
        self.wait(2)

        

        sum_text_2 = MathTex(r'A \:=',
                             r'\lim_{n \to \infty} \:',
                             r'\sum_{i=1}^{n}',
                             r'f(\overline{x}_i) \Delta x'
                             ).scale(0.8).set_z_index(3).move_to(A_text)

        sum_text_1 = MathTex(r'A \:\approx\:',
                             r'\sum_{i=1}^{n}',
                             r'f(\overline{x}_i) \Delta x'
                             ).scale(0.8).set_z_index(3).move_to(sum_text_2, aligned_edge=LEFT)
        sum_text_1[2][4].set_color(YELLOW)

        aux2 = Tex('\it``somatório"', color=GRAY).scale(0.8).next_to(sum_text_1[1][0], UP, buff=0.7).shift(LEFT*1.5).set_z_index(3)
        aux2_line = Line(aux2.get_bottom(), sum_text_1[1][1], buff=0.2, color=GRAY).set_z_index(3)


        aux1 = sum_text_1[2].copy().next_to(A_text, UP, buff=0.7)
        aux1[4].set_color(YELLOW)

        self.play(FadeIn(aux1))
        self.wait(2)
        self.play(Indicate(aux1[4]))
        self.wait(2)
        self.play(ReplacementTransform(A_text[0], sum_text_1[0]),
                  FadeOut(A_text_sr),
                  ReplacementTransform(aux1, sum_text_1[2]),
                  LaggedStart(A_text[1].animate.move_to(sum_text_1[1]).scale(0),
                              A_text[2].animate.move_to(sum_text_1[1]).scale(0),
                              A_text[3].animate.move_to(sum_text_1[1]).scale(0),
                              A_text[4:].animate.move_to(sum_text_1[1]).scale(0),
                              GrowFromCenter(sum_text_1[1]),
                              lag_ratio=0.1))
        self.wait(2)
        self.play(FadeIn(aux2, aux2_line))
        self.wait(2)
        self.play(VGroup(sum_text_1[1][0], sum_text_1[1][2:]).animate.set_color(YELLOW))
        self.wait(2)
        self.play(sum_text_1.animate.set_color(WHITE),
                  FadeOut(aux2, aux2_line))
        self.wait(2)



        # Passando para o limite quando 'n' tende a infinito
        self.play(ReplacementTransform(rect_list[0], rect_list[1]),
                  ReplacementTransform(tick_groups[0], tick_groups[1]))
        self.wait(2)
        self.play(ReplacementTransform(rect_list[1], rect_list[2]),
                  ReplacementTransform(tick_groups[1], tick_groups[2]))
        self.wait(2)
        self.play(ReplacementTransform(rect_list[2], rect_list[3]),
                  ReplacementTransform(tick_groups[2], tick_groups[3]))
        self.wait(2)
        self.play(LaggedStart(FadeOut(rect_list[3]),
                              AnimationGroup(area.animate.set_opacity(0.8),
                                             area_aux1.animate.set_opacity(1),
                                             area_aux2.animate.set_opacity(1)),
                              lag_ratio=0.1),
                  FadeOut(tick_groups[3]))
        self.wait(2)

        self.play(LaggedStart(sum_text_1[0][1].animate.scale(0), 
                              GrowFromCenter(sum_text_2[0][1]),
                              lag_ratio=0.2))
        sum_text_2[1].set_color(YELLOW)
        self.play(LaggedStart(ReplacementTransform(sum_text_1[1:], sum_text_2[2:]),
                              FadeIn(sum_text_2[1]),
                              lag_ratio=0.3))
        self.remove(sum_text_1[0][0]).add(sum_text_2[0][0])
        self.wait(2)
        self.play(sum_text_2[1].animate.set_color(WHITE))
        self.wait(2)



        # Transição para a próxima cena
        black_sq = Square(color=BLACK, fill_opacity=1).scale(20).set_z_index(9)
        sum_text_2[1:].set_z_index(11)
        self.play(LaggedStart(FadeIn(black_sq),
                              sum_text_2[1:].animate.scale(1.25).move_to(ORIGIN).shift(DOWN*0.75),
                              lag_ratio=0.1))
        self.wait(2)



# Definição e notação da integral
class vid4(MovingCameraScene):
    def construct(self):

        # Retomando elemento
        sum_text_2 = MathTex(r'A \:=',
                             r'\lim_{n \to \infty} \:',
                             r'\sum_{i=1}^{n}',
                             r'f(\overline{x}_i) \Delta x'
                             ).scale(0.8).scale(1.25).set_z_index(3)
        sum_text_2[1:].move_to(ORIGIN).shift(DOWN*0.75)

        self.add(sum_text_2[1:])



        def_t1 = Tex('Integral ','definida ', 'de ',r'$f$',r' em ',r'$[a,b]$', color=YELLOW).scale(0.9).next_to(sum_text_2[1:], UP, buff=1).set_z_index(11)
        def_sr1 = SurroundingRectangle(VGroup(sum_text_2[1:], def_t1), color=GRAY, buff=0.4).set_opacity(0.3).set_z_index(-1)
        self.play(LaggedStart(FadeIn(def_t1[0]),
                              FadeIn(def_t1[1]),
                              FadeIn(def_t1[2]),
                              FadeIn(def_t1[3]),
                              FadeIn(def_t1[4]),
                              FadeIn(def_t1[5]),
                              FadeIn(def_sr1),
                              lag_ratio=0.5))
        self.wait(2)

        integral_text = MathTex(r'\int_{a}^{b} f(x) \,dx \:=\:', color=YELLOW).next_to(sum_text_2[1:], LEFT, buff=0.2).shift(RIGHT*1.55).set_z_index(11)
        integral_text[0][9].set_color(WHITE)
        integral_text[0][0:2].shift(RIGHT*0.07)

        def_sr2 = Rectangle(width=def_sr1.get_width()*1.22, height=def_sr1.get_height(), color=GRAY).set_opacity(0.3).set_z_index(-1)

        self.play(ReplacementTransform(def_sr1, def_sr2),
                  LaggedStart(sum_text_2[1:].animate.shift(RIGHT*1.6),
                              FadeIn(integral_text[0][9]),
                              lag_ratio=0.2))
        self.wait(2)

        # O limite do somatório se transforma no 'S' alongado com 'a' e 'b' nas extremidades
        self.play(sum_text_2[1:3].animate.set_color(YELLOW))
        self.wait(2)
        aux1 = sum_text_2[1:3].copy()
        self.play(CounterclockwiseTransform(aux1, integral_text[0][0], path_arc=np.pi/4))
        self.remove(aux1).add(integral_text[0][0])
        self.wait(2)
        self.play(integral_text[0][0].animate.set_color(WHITE),
                  LaggedStart(FadeIn(integral_text[0][2]),
                              FadeIn(integral_text[0][1]),
                              lag_ratio=0.4))
        self.wait(2)
        self.play(VGroup(sum_text_2[1:3], integral_text[0][1:3]).animate.set_color(WHITE))
        self.wait(2)

        # Aparece o nome da função
        self.play(sum_text_2[3][0:6].animate.set_color(YELLOW))
        self.wait(2)
        aux2 = sum_text_2[3][0:6].copy()
        self.play(CounterclockwiseTransform(aux2, integral_text[0][3:7], path_arc=np.pi/4))
        self.remove(aux2).add(integral_text[0][3:7])
        self.wait(2)
        self.play(VGroup(sum_text_2[3][0:6], integral_text[0][3:7]).animate.set_color(WHITE))
        self.wait(2)

        # Os '\Delta x i' se transformam no 'dx'
        self.play(sum_text_2[3][-2:].animate.set_color(YELLOW))
        self.wait(2) 
        aux3 = sum_text_2[3][-2:].copy()
        self.play(CounterclockwiseTransform(aux3, integral_text[0][7:9], path_arc=np.pi/4))
        self.remove(aux3).add(integral_text[0][7:9])
        self.wait(2)
        self.play(VGroup(sum_text_2[3][-2:], integral_text[0][7:9]).animate.set_color(WHITE))
        self.wait(2)

        # Comentário sobre o nome da variável 'x'
        self.play(VGroup(integral_text[0][5], 
                         integral_text[0][8],
                         sum_text_2[3][3],
                         sum_text_2[3][7]).animate.set_color(YELLOW))
        self.wait(2)

        var_1_1 = MathTex('t', color=YELLOW).move_to(integral_text[0][5])
        var_1_2 = MathTex('dt', color=YELLOW).move_to(integral_text[0][7:9], aligned_edge=LEFT)
        var_1_3 = MathTex(r'\overline{t}_i').move_to(sum_text_2[3][2:5])
        var_1_3[0][1].set_color(YELLOW)
        var_1_4 = MathTex(r'\Delta t', color=YELLOW).move_to(sum_text_2[3][6:], aligned_edge=LEFT)

        self.play(Transform(integral_text[0][5], var_1_1),
                  Transform(integral_text[0][8], var_1_2[0][1]),
                  Transform(sum_text_2[3][2:4], var_1_3[0][0:2]),
                  Transform(sum_text_2[3][7], var_1_4[0][1]))
        self.wait(2)


        var_2_1 = MathTex('u', color=YELLOW).move_to(integral_text[0][5])
        var_2_2 = MathTex('du', color=YELLOW).move_to(integral_text[0][7:9], aligned_edge=LEFT)
        var_2_3 = MathTex(r'\overline{u}_i').move_to(sum_text_2[3][2:5])
        var_2_3[0][1].set_color(YELLOW)
        var_2_4 = MathTex(r'\Delta u', color=YELLOW).move_to(sum_text_2[3][6:], aligned_edge=LEFT)

        self.play(Transform(integral_text[0][5], var_2_1),
                  Transform(integral_text[0][8], var_2_2[0][1]),
                  Transform(sum_text_2[3][2:4], var_2_3[0][0:2]),
                  Transform(sum_text_2[3][7], var_2_4[0][1]))
        self.wait(2)


        var_3_1 = MathTex('x').move_to(integral_text[0][5])
        var_3_2 = MathTex('dx').move_to(integral_text[0][7:9], aligned_edge=LEFT)
        var_3_3 = MathTex(r'\overline{x}_i').move_to(sum_text_2[3][2:5])
        var_3_4 = MathTex(r'\Delta x').move_to(sum_text_2[3][6:], aligned_edge=LEFT)

        # Transição para a próxima cena
        t1 = Tex('Teorema Fundamental do Cálculo', color=YELLOW).scale(0.9).to_edge(UP, buff=0.5)
        t1.shift(UP)

        self.play(VGroup(def_t1, integral_text).animate.set_opacity(0.3),
                  Transform(integral_text[0][5], var_3_1.set_opacity(0.3)),
                  Transform(integral_text[0][8], var_3_2[0][1].set_opacity(0.3)),
                  Transform(sum_text_2[3][2:4], var_3_3[0][0:2]),
                  Transform(sum_text_2[3][7], var_3_4[0][1]))
        self.wait(2)
        self.wait(2)
        self.play(LaggedStart(AnimationGroup(VGroup(def_t1, integral_text, sum_text_2[1:]).animate.set_opacity(1).shift(DOWN*6),
                                             def_sr2.animate.shift(DOWN*6)), 
                              t1.animate.shift(DOWN),
                              lag_ratio=0.4),
                              run_time=2.5)
        self.wait(2)


        
# Teorema Fundamental do Cálculo
class vid5(MovingCameraScene):
    def construct(self):

        t1 = Tex('Teorema ','Fundamental do ','Cálculo', color=YELLOW).scale(0.9).to_edge(UP, buff=0.5)
        t1_aux1 = Tex('T.F.C.', color=YELLOW).scale(0.9).to_corner(UL, buff=0.5)
        t1_aux2 = always_redraw(lambda: Tex('T', color=YELLOW).scale(0.9).move_to(t1[0], aligned_edge=LEFT))
        t1_aux3 = always_redraw(lambda: Tex('F', color=YELLOW).scale(0.9).move_to(t1[1], aligned_edge=LEFT))
        t1_aux4 = always_redraw(lambda: Tex('C', color=YELLOW).scale(0.9).move_to(t1[2], aligned_edge=LEFT))

        self.add(t1, t1_aux2, t1_aux3, t1_aux4)
        self.wait(2)

        self.play(LaggedStart(LaggedStart(t1[0].animate.move_to(t1_aux1[0][0], aligned_edge=LEFT).set_opacity(0),
                                          GrowFromCenter(t1_aux1[0][1]),
                                          lag_ratio=0.3),
                              LaggedStart(t1[1].animate.move_to(t1_aux1[0][2], aligned_edge=LEFT).set_opacity(0),
                                          GrowFromCenter(t1_aux1[0][3]),
                                          lag_ratio=0.3),
                              LaggedStart(t1[2].animate.move_to(t1_aux1[0][4], aligned_edge=LEFT).set_opacity(0), 
                                          GrowFromCenter(t1_aux1[0][5]),
                                          lag_ratio=0.3),
                              lag_ratio=0.2))
        self.add(t1_aux1).remove(t1_aux2, t1_aux3, t1_aux4)

        

        # Aparece o gráfico de f
        ax1 = Axes(x_range=[-1, 11], x_length=8,
                   y_range=[-0.75, 6], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0)
        ax1_zero_label = MathTex('0').scale(0.9).set_color(GRAY).next_to(ax1.c2p(0,0), DOWN, buff=0.12).shift(LEFT*0.25)
        ax1_x_label = always_redraw(lambda: MathTex('t').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2))
        ax1_y_label = always_redraw(lambda: MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2))

        def f(x):
            return 0.04*(x-0)*(x-3)*(x-6) + 2.5

        gr1 = ax1.plot(f, x_range=[-3, 9], stroke_width=4, color=BLUE)
        gr1_label = MathTex('y = f(t)', color=BLUE).shift(UP*3.5+RIGHT*3.4).scale(0.9)

        self.play(FadeIn(ax1, ax1_zero_label, ax1_x_label, ax1_y_label, gr1, gr1_label))
        self.wait(2)


        # Criamos uma "função-área" F de 0 a x
        F_text_1 = MathTex(r'F(x)',r'= \int_{0}^{x} f(t) \,dt').scale(0.9).shift(UP*2+LEFT).set_z_index(3)
        F_text_1[1][4:8].set_color(BLUE)
        VGroup(F_text_1[0], F_text_1[1][2]).set_color(YELLOW)
        F_text_1_sr = SurroundingRectangle(F_text_1, color=BLACK, buff=0.2, fill_opacity=0.8, stroke_width=0).set_z_index(2)


        F_text_2 = Tex('\it``Função-área"', color=GRAY).scale(0.8).next_to(F_text_1, LEFT, buff=1).shift(DOWN*0.7).set_z_index(3)
        F_text_2_line = Line(F_text_2, F_text_1, buff=0.1, color=GRAY).set_z_index(3)

        self.play(FadeIn(F_text_1[0], F_text_1[1][0]))
        self.wait(2)
        self.play(FadeIn(F_text_2, F_text_2_line))
        self.wait(2)
        self.play(FadeIn(F_text_1[1][1]))
        self.wait(2)
        self.play(LaggedStart(FadeIn(F_text_1[1][3]),
                              FadeIn(F_text_1[1][2]),
                              lag_ratio=0.5))
        self.wait(2)
        self.play(FadeIn(F_text_1[1][4:]))
        self.wait(2)



        # Comentário sobre a variável de integração 't' em vez de 'x'
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        t2 = Tex(r'Usamos ',r'$t$',r' como a variável de integração para \\não haver conflito com o ',r'$x$',r' que é extremidade \\do intervalo de integração ',r'$[0,x]$', color=GRAY, tex_template=myTemplate, tex_environment="justify").scale(0.65).shift(DOWN*1.5+RIGHT*0.5).set_z_index(3)
        t2[1].set_color(WHITE).set_opacity(0.8)
        t2[3].set_color(YELLOW).set_opacity(0.8)
        t2[5][3].set_color(YELLOW).set_opacity(0.8)
        t2_sr = SurroundingRectangle(t2, color=BLACK, buff=0.2, fill_opacity=0.8, stroke_width=0).set_z_index(2)

        self.play(FadeIn(t2, t2_sr))
        self.wait(2)
        self.wait(2)
        self.play(FadeOut(t2, t2_sr))
        self.wait(2)




        # Mostrando a área calculada pela função F
        X_F_area = ValueTracker(0)
        F_area = always_redraw(lambda: 
                               ax1.get_area(
                               gr1,
                               x_range=(0, X_F_area.get_value()),
                               color=(YELLOW_B, YELLOW_D)
                               ).set_fill(opacity=0.6).set_stroke(width=0).set_z_index(-1))
        
        F_x_label = always_redraw(lambda: MathTex('x', color=YELLOW).next_to(ax1.c2p(X_F_area.get_value(),0), DOWN, buff=0.15))

        self.add(F_area)
        aux1 = MathTex('x', color=YELLOW).next_to(ax1.c2p(4.5,0), DOWN, buff=0.15)
        self.play(X_F_area.animate.set_value(4.5), 
                  GrowFromPoint(aux1, ax1.c2p(0,-0.15)),
                  run_time=2.5)
        self.wait(2)
        self.play(FadeOut(F_text_2, F_text_2_line))
        self.wait(2)



        # Derivada da função-área: F'(x) = f(x)
            # Aumento dx
        aux2 = F_area.copy().set_color(BLACK)
        self.play(X_F_area.animate.set_value(5),
                  aux1.animate.next_to(ax1.c2p(5,0), DOWN, buff=0.15),
                  FadeIn(aux2))
        self.wait(2)

        dx_brace = always_redraw(lambda: Brace(Line(ax1.c2p(4.5,0), ax1.c2p(X_F_area.get_value(),0)), DOWN, buff=0.1, color=YELLOW))
        aux3 = MathTex('dx', color=YELLOW).next_to(dx_brace, DOWN, buff=0.15)
        self.play(FadeIn(dx_brace, aux3),
                  FadeOut(aux1))
        self.wait(2)

            # Aumento dF
        t3 = MathTex(r'dF = f(x)dx').scale(0.9).shift(DOWN*0.5+RIGHT*3)
        VGroup(t3[0][0:2], t3[0][7:]).set_color(YELLOW)
        t3[0][3:7].set_color(BLUE)

        aux4 = always_redraw(lambda: Line(Dot(radius=0).next_to(t3, LEFT, buff=0.17), ax1.c2p((4.5 + X_F_area.get_value())/2, 1.5), buff=0, color=WHITE).set_z_index(3))
        
        aux5 = Brace(Line(ax1.c2p(5, 0), ax1.c2p(5, f(5))), RIGHT, buff=0.1, color=BLUE).scale(0.9)
        aux6 = MathTex('f(x)', color=BLUE).next_to(aux5, RIGHT, buff=0.15)

        self.play(FadeIn(t3[0][0:2], aux4))
        self.wait(2)
        self.play(X_F_area.animate.set_value(4.6))
        self.play(X_F_area.animate.set_value(5))
        self.wait(2)
        self.play(FadeIn(aux5, aux6))
        self.wait(2)
        self.play(LaggedStart(FadeOut(aux2, aux4),
                              FadeIn(t3[0][2], aux1),
                              AnimationGroup(ReplacementTransform(aux6, t3[0][3:7]), FadeOut(aux5)),
                              AnimationGroup(ReplacementTransform(aux3, t3[0][7:]), FadeOut(dx_brace)),
                              lag_ratio=0.1))
        self.wait(2)



        t4 = MathTex(r'\frac{dF}{dx} = f(x)').scale(0.9).move_to(t3, aligned_edge=LEFT).shift(UP*0.035+LEFT*0.07)
        VGroup(t4[0][0:5]).set_color(YELLOW)
        t4[0][6:].set_color(BLUE)

        self.play(LaggedStart(ReplacementTransform(t3[0][0:2], t4[0][0:2]),
                              AnimationGroup(FadeIn(t4[0][2]), ClockwiseTransform(t3[0][7:], t4[0][3:5])),
                              lag_ratio=0.1))
        self.wait(2)



        # 'F' é primitiva de 'f'
        indicative_arrow = Arrow(UP, DOWN*0.5).rotate(-30*DEGREES).next_to(t4, UP).shift(LEFT*0.1)
        self.play(FadeIn(indicative_arrow))
        self.wait(2)
        self.play(indicative_arrow.animate.shift(RIGHT*1+DOWN*0.2))
        self.wait(2)
        self.play(indicative_arrow.animate.shift(LEFT*0.9+UP*0.2))
        self.wait(2)

        t5 = MathTex(r'\frac{d(???)}{dx} = f(x)').scale(0.9).move_to(t4, aligned_edge=LEFT)
        t5[0][0:9].set_color(YELLOW)
        t5[0][10:].set_color(BLUE)
        self.play(ReplacementTransform(t4[0][0:2], t5[0][0:6]),
                  ReplacementTransform(t4[0][2], t5[0][6]),
                  ReplacementTransform(t3[0][7:], t5[0][7:9]),
                  ReplacementTransform(t3[0][2:7], t5[0][9:]))
        self.wait(2)
        self.play(indicative_arrow.animate.shift(RIGHT*1.5+DOWN*0.2))
        self.wait(2)
        self.play(indicative_arrow.animate.shift(LEFT*1.5+UP*0.2))
        
        aux7 = Tex('\it``primitiva"', color=GRAY).scale(0.8).next_to(indicative_arrow, UP).shift(RIGHT*0.3)
        aux8 = Tex('\it``antiderivada"', color=GRAY).scale(0.8).move_to(aux7).shift(RIGHT*0.3)
        self.play(FadeIn(aux7))
        self.wait(2)
        self.play(LaggedStart(FadeOut(aux7),
                              FadeIn(aux8),
                              lag_ratio=0.1))
        self.wait(2)
        self.play(FadeOut(F_text_1, F_area, aux1, t5, indicative_arrow, aux8))
        self.wait(2)
        


        # Área de 'a' até 'b' é igual a 'F(b) - F(a)'
        a_b_area = ax1.get_area(
                   gr1,
                   x_range=(2, 7),
                   color=(BLUE_B, BLUE_D)
                   ).set_fill(opacity=0.7).set_stroke(width=0)
        
        a_line = Line(ax1.c2p(2,0), ax1.c2p(2,f(2)), stroke_width=3).set_opacity(0.5)
        b_line = Line(ax1.c2p(7,0), ax1.c2p(7,f(7)), stroke_width=3).set_opacity(0.5)

        a_label = MathTex('a').next_to(ax1.c2p(2,0), DOWN, buff=0.15)
        b_label = MathTex('b').next_to(ax1.c2p(7,0), DOWN, buff=0.15)

        t3 = MathTex(r'\int_{a}^{b} f(t) \,dt = ',r'F(b) - F(a)').scale(0.9).shift(UP*2+LEFT*0.5).set_z_index(3)
        t3[0][3:7].set_color(BLUE)
        t3[1][0:4].set_color((GREEN_B, GREEN_D))
        t3[1][4:].set_color((RED_D, RED_E))
        t3_sr = SurroundingRectangle(t3[1], color=BLACK, buff=0.2, fill_opacity=0.8, stroke_width=0).set_z_index(2)

        self.play(LaggedStart(FadeIn(a_line, a_label),
                              FadeIn(b_line, b_label),
                              lag_ratio=0.3))
        self.wait(2)
        self.play(FadeIn(t3[0]))
        self.wait(2)

        X_F_area_b = ValueTracker(0)
        F_area_b = always_redraw(lambda: 
                               ax1.get_area(
                               gr1,
                               x_range=(0, X_F_area_b.get_value()),
                               color=(GREEN_B, GREEN_D)
                               ).set_fill(opacity=0.7).set_stroke(width=0).set_z_index(-2))
        self.add(F_area_b)
        self.play(LaggedStart(X_F_area_b.animate.set_value(7),
                              FadeIn(t3[1][0:4]),
                              lag_ratio=0.1),
                              run_time=2.5)
        self.wait(2)


        X_F_area_a = ValueTracker(0)
        F_area_a = always_redraw(lambda: 
                               ax1.get_area(
                               gr1,
                               x_range=(0, X_F_area_a.get_value()),
                               color=(RED_D, RED_E)
                               ).set_fill(opacity=0.7).set_stroke(width=0).set_z_index(0))
        F_area_a_aux = always_redraw(lambda: F_area_a.copy().set_color(BLACK).set_opacity(1).set_z_index(-1))

        self.add(F_area_a, F_area_a_aux)
        self.play(LaggedStart(X_F_area_a.animate.set_value(2),
                              FadeIn(t3[1][4:], t3_sr),
                              lag_ratio=0.1),
                              run_time=1.5)
        aux2 = F_area_a.copy().set_color(BLACK).set_fill(opacity=1)
        self.play(FadeIn(aux2))
        self.wait(2)
        self.wait(2)

        

# Encontrando a primitiva de x^2
class vid6(MovingCameraScene):
    def construct(self):

        t0 = MathTex('f(x) = x^2', color=BLUE)
        self.play(FadeIn(t0))
        self.wait(2)
        
        t1 = MathTex('x^2', color=BLUE).scale(0.9)
        t2 = MathTex('???', color=YELLOW).scale(0.9).next_to(t1, LEFT, buff=2)
        VGroup(t1, t2).move_to(ORIGIN)

        arrow_1 = CurvedArrow(t2.get_top(), t1.get_top(), radius=-1.5, stroke_width=3).shift(UP*0.3)

        t_arrow_1 = MathTex(r'\frac{d}{dx}').scale(0.7).next_to(arrow_1, UP, buff=0.2)

        self.play(t0[0][5:].animate.move_to(t1).scale(0.9),
                  FadeOut(t0[0][0:5]))
        self.add(t1)
        self.play(t0[0][5:].animate.set_opacity(0))
        self.play(FadeIn(t2))
        self.wait(2)
        self.play(LaggedStart(Create(arrow_1),
                              FadeIn(t_arrow_1),
                              lag_ratio=0.1))
        self.wait(2)



        t3 = MathTex('x^3', color=YELLOW).scale(0.9).move_to(t2)
        t3_copy = t3.copy()
        t4 = MathTex('3x^2', color=BLUE).scale(0.9).move_to(t1)

        self.play(t1.animate.shift(RIGHT*2),
                  LaggedStart(FadeOut(t2),
                              FadeIn(t3),
                              lag_ratio=0.2))
        self.wait(2)
        self.play(ClockwiseTransform(t3_copy, t4, path_arc=-np.pi/2))
        self.remove(t3_copy).add(t4)
        self.wait(2)
        self.play(FadeOut(t4))
        self.wait(2)



        t5 = MathTex(r'\frac{x^3}{3}', color=YELLOW).scale(0.9).move_to(t3, aligned_edge=UP)
        t5[0][2:].shift(LEFT*0.1)
        t5_copy = t5.copy()
        t6 = MathTex('x^2', color=BLUE).scale(0.9).move_to(t4)

        self.play(FadeIn(t5[0][2:]))
        self.wait(2)
        self.play(ClockwiseTransform(t5_copy, t6, path_arc=-np.pi/2),
                  t1.animate.move_to(t4))
        self.remove(t1, t5_copy).add(t6)
        self.wait(2)
        self.play(Flash(t5, flash_radius=0.5, num_lines=8))
        self.wait(2)



        t7 = MathTex(r'+ \: 1', color=YELLOW).scale(0.9).next_to(t5, RIGHT, buff=-0.25)
        t8 = MathTex(r'+ \: 2', color=YELLOW).scale(0.9).move_to(t7, aligned_edge=LEFT)
        t9 = MathTex(r'+ \: 3', color=YELLOW).scale(0.9).move_to(t7, aligned_edge=LEFT)
        t10 = MathTex(r'+ \: C', color=YELLOW).scale(0.9).move_to(t7, aligned_edge=LEFT)

        self.remove(t3).add(t5[0][0:2])
        self.play(LaggedStart(t5.animate.shift(LEFT*0.35),
                              FadeIn(t7),
                              lag_ratio=0.1))
        self.wait(2)
        self.play(ReplacementTransform(t7, t8))
        self.wait(2)
        self.play(ReplacementTransform(t8, t9))
        self.wait(2)
        self.play(ReplacementTransform(t9, t10))
        self.wait(2)



        # Influência da constante '+ C' graficamente
        ax1 = Axes(x_range=[-3, 3], x_length=8,
                   y_range=[-0.75, 6], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*7.5)
        ax1_x_label = always_redraw(lambda: MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2))
        ax1_y_label = always_redraw(lambda: MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2))

        def F(x):
            return 0.4*x**3
        
        def f(x):
            return 0.4*3*x**2

        gr1 = ax1.plot(F, x_range=[-2.45, 2.45], stroke_width=4, color=YELLOW)
        
        t11 = MathTex(r'y =',r'\frac{x^3}{3} + C', color=YELLOW).scale(0.9).shift(UP*3+LEFT*5).shift(DOWN*7.5)
        t11_copy = t11[1].copy().move_to(VGroup(t5, t10))
        self.camera.frame.save_state()
        self.add(ax1, ax1_x_label, ax1_y_label, gr1, t11[0])
        self.play(self.camera.frame.animate.move_to(ax1),
                  ReplacementTransform(t11_copy, t11[1]),
                  run_time=2)
        self.wait(2)
        self.play(gr1.animate.shift(UP*3), run_time=1.5)
        self.play(gr1.animate.shift(DOWN*1))
        self.wait(2)



        tangent_line = Line(ORIGIN, RIGHT*5.5, color=BLUE).rotate(np.arctan(f(0.8)*0.75)).move_to(ax1.c2p(0.8,F(0.8))).shift(UP*2)

        self.play(Create(tangent_line))
        self.wait(2)
        self.play(VGroup(gr1, tangent_line).animate.shift(DOWN*2), run_time=1.5)
        self.play(VGroup(gr1, tangent_line).animate.shift(UP*1))
        self.wait(2)



        gr1_copies_up = []
        for i in range(1,9):
            gr1_copy = gr1.copy().shift(UP*i*0.5).set_stroke(opacity=0.3/i)
            gr1_copies_up.append(gr1_copy)
        gr1_copies_down = []

        for i in range(1,7):
            gr1_copy = gr1.copy().shift(DOWN*i*0.5).set_stroke(opacity=0.3/i)
            gr1_copies_down.append(gr1_copy)

        self.play(FadeIn(*gr1_copies_up, *gr1_copies_down))
        self.wait(2)



        # Integral indefinida
        self.play(LaggedStart(self.camera.frame.animate.restore(),
                              FadeOut(ax1, ax1_x_label, ax1_y_label, t11, gr1, tangent_line, *gr1_copies_up, *gr1_copies_down),
                              lag_ratio=0.2),
                              run_time=2)
        self.wait(2)



        t12 = MathTex(r'\int_{a}^{b} x^2 \,dx =',r'\frac{x^3}{3} + C').scale(0.9)
        t13 = MathTex(r'\int x^2 \,dx =',r'\frac{x^3}{3} + C').scale(0.9).move_to(t12, aligned_edge=RIGHT)
        VGroup(t12[0][3:5], t13[0][1:3]).set_color(BLUE)
        VGroup(t12[1], t13[1]).set_color(YELLOW)

        aux1 = Tex('\it``integral indefinida"', color=GRAY).scale(0.8).next_to(t12, LEFT, buff=-0.7).shift(UP*1.5)
        aux2 = Line(aux1.get_bottom(), t13[0][0].get_center(), buff=0.2, stroke_width=3, color=GRAY)

        self.play(LaggedStart(FadeOut(arrow_1, t_arrow_1),
                              MoveAlongPath(t6, ArcBetweenPoints(t6.get_center(), t12[0][3:5].get_center())),
                              MoveAlongPath(VGroup(t5, t10), ArcBetweenPoints(VGroup(t5, t10).get_center(), t12[1].get_center())),
                              FadeIn(t12[0][0:3], t12[0][5:]),
                              lag_ratio=0.1))
        self.wait(2)
        self.play(LaggedStart(AnimationGroup(Flash(t12[0][2], num_lines=8), FadeOut(t12[0][2])),
                              AnimationGroup(Flash(t12[0][1], num_lines=8), FadeOut(t12[0][1])),
                              t12[0][0].animate.move_to(t13[0][0]),
                              lag_ratio=0.2))
        self.wait(2) 
        self.play(FadeIn(aux1, aux2))
        self.wait(2)
        self.wait(2)



# Integral definida de 'x^2' em [1,2]
class vid7(MovingCameraScene):
    def construct(self):

        self.camera.frame.shift(RIGHT*2.5)

        ax1 = Axes(x_range=[-3, 3], x_length=8,
                   y_range=[-0.75, 6], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.5+LEFT*0.4).scale(0.9)
        ax1_zero_label = MathTex('0').scale(0.9).set_color(GRAY).next_to(ax1.c2p(0,0), DOWN, buff=0.12).shift(LEFT*0.25).set_z_index(1)
        ax1_x_label = always_redraw(lambda: MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2))
        ax1_y_label = always_redraw(lambda: MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2))

        def f(x):
            return x**2
        
        def F(x):
            return 0.5*x**3

        gr1 = ax1.plot(f, x_range=[-2.4, 2.4], stroke_width=4, color=BLUE).set_z_index(2)
        gr1_label_1 = MathTex('f(x) = x^2', color=BLUE).scale(0.85).shift(UP*3.3+RIGHT*4.6)
        gr1_label_2 = MathTex(r'F(x) = \frac{x^3}{3} + C', color=YELLOW).scale(0.85).next_to(gr1_label_1, RIGHT, buff=1)

        self.add(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label_1)

        self.play(FadeIn(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label_1, gr1_label_2))
        self.wait(2)



        X_F_area_2 = ValueTracker(2)
        F_area_2 = always_redraw(lambda: 
                               ax1.get_area(
                               gr1,
                               x_range=(0, X_F_area_2.get_value()),
                               color=(GREEN_B, GREEN_E)
                               ).set_fill(opacity=0.6).set_stroke(width=0).set_z_index(-2))
        
        X_F_area_1 = ValueTracker(1)
        F_area_1 = always_redraw(lambda: 
                               ax1.get_area(
                               gr1,
                               x_range=(0, X_F_area_1.get_value()),
                               color=(RED_C, RED_E)
                               ).set_fill(opacity=0.6).set_stroke(width=0).set_z_index(0))
        F_area_1_aux = always_redraw(lambda: F_area_1.copy().set_color(BLACK).set_opacity(1).set_z_index(-1))
        
        a_line = Line(ax1.c2p(1,0), ax1.c2p(1,f(1)), stroke_width=3).set_opacity(0.5).set_z_index(0)
        b_line = Line(ax1.c2p(2,0), ax1.c2p(2,f(2)), stroke_width=3).set_opacity(0.5).set_z_index(0)

        aux1 = MathTex('1', color=WHITE).scale(0.9).next_to(ax1.c2p(1,0), DOWN, buff=0.15).set_z_index(1)
        aux2 = MathTex('2', color=WHITE).scale(0.9).next_to(ax1.c2p(2,0), DOWN, buff=0.15).set_z_index(1)


        t1 = MathTex(r'\int_{1}^{2} x^2 \,dx = ',r' \frac{2^3}{3} + C ',r' - \Big( \frac{1^3}{3} + C \Big)').scale(0.85).shift(RIGHT*6.3).set_z_index(11)
        t1[0][3:5].set_color(BLUE)
        t1[1].set_color(GREEN)
        t1[2].set_color(RED_D)


        self.wait(2)
        self.add(F_area_2, F_area_1_aux, aux1, aux2, a_line, b_line)
        self.wait(2)
        self.play(FadeIn(t1[0]))
        self.wait(2)



        self.play(X_F_area_2.animate.set_value(0),
                  X_F_area_1.animate.set_value(0),
                  run_time=0.001)
        self.wait(2)

        self.play(X_F_area_2.animate.set_value(2), 
                  ReplacementTransform(gr1_label_2[0][5:].copy(), t1[1]),
                  run_time=2)
        self.wait(2)
        self.add(F_area_1)
        self.play(X_F_area_1.animate.set_value(1), 
                  LaggedStart(FadeIn(t1[2][0:2], t1[2][8]),
                              ReplacementTransform(gr1_label_2[0][5:].copy(), t1[2][2:8]),
                              lag_ratio=0.1),
                  run_time=2)
        self.wait(2)
        aux3 = F_area_1.copy().set_color(BLACK).set_fill(opacity=1)
        self.play(FadeIn(aux3))
        self.wait(2)



        # Destaque na constante '+ C'
        black_sq = Square(color=BLACK, fill_opacity=0.7).scale(20).set_z_index(10)
        self.play(FadeIn(black_sq))
        self.wait(2)
        self.play(VGroup(t1[1][4:6], t1[2][6:8]).animate.set_color(YELLOW))
        self.wait(2)

        aux4 = t1[2][0].copy().shift(DOWN)
        self.play(ReplacementTransform(t1[2][0].copy(), aux4),
                  t1[1][4:6].animate.next_to(aux4, LEFT, buff=0.2),
                  t1[2][6:8].animate.next_to(aux4, RIGHT, buff=0.2))
        self.wait(2)
        self.play(FadeOut(t1[1][4:6], t1[2][6:8], aux4))
        self.wait(2)
        self.play(FadeOut(black_sq))
        self.wait(2)
        self.play(LaggedStart(FadeOut(t1[2][1], t1[2][8]),
                              AnimationGroup(t1[2][0].animate.shift(LEFT*0.8), 
                                             t1[2][2:6].animate.shift(LEFT*1)),
                              lag_ratio=0.1))
        self.wait(2)

        t2 = MathTex(r'= \frac{7}{3}').scale(0.85).next_to(t1[2][2:6], RIGHT, buff=0.2, aligned_edge=DOWN)
        self.play(FadeIn(t2))
        self.wait(2)
        self.wait(2)
        self.wait(2)



# Função negativa
class vid8(MovingCameraScene):
    def construct(self):

        ax1 = Axes(x_range=[-1, 11], x_length=8,
                   y_range=[-5, 9], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0).set_z_index(10)
        ax1_zero_label = MathTex('0').scale(0.9).set_color(GRAY).next_to(ax1.c2p(0,0), DOWN, buff=0.12).shift(LEFT*0.25)
        ax1_x_label = always_redraw(lambda: MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2))
        ax1_y_label = always_redraw(lambda: MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2))

        def f(x):
            return -0.04*(x-1.5-0)*(x-1.5-3)*(x-1.5-6) - 3

        gr1 = ax1.plot(f, x_range=[-4, 12], stroke_width=4, color=BLUE).set_z_index(11)
        gr1_label = MathTex('y = f(x)', color=BLUE).shift(DOWN*3.5+RIGHT*4.5).scale(0.9)


        t1 = MathTex(r'\int_{a}^{b} f(x) \,dx')
        t1[0][3:7].set_color(BLUE)
        

        self.play(FadeIn(t1))
        self.wait(2)
        self.play(LaggedStart(t1.animate.shift(UP*2.5),
                              FadeIn(ax1, ax1_x_label, ax1_y_label),
                              Create(gr1),
                              FadeIn(gr1_label),
                              lag_ratio=0.1))
        self.wait(2)



        # As alturas dos retângulos serão negativas
        # Retângulos sobre os subintervalos
            # Lista de dxs: mais subdivisões = mais retângulos
        dx_list = [6 / n for n in [8, 16, 24, 34, 200]]

            # Retângulos achatados na base
        flat_rects = ax1.get_riemann_rectangles(
            ax1.plot(lambda x: 0, x_range=[1, 7]),
            x_range=[1, 7],
            dx=dx_list[0],
            input_sample_type="center"
        )
        for rect in flat_rects:
            rect.set_fill(GRAY, opacity=0.3)
            rect.set_stroke(width=0.5)

        # Gera lista de grupos de retângulos
        rect_list = []
        for dx in dx_list:
            rects = ax1.get_riemann_rectangles(gr1, x_range=[1, 7], dx=dx, input_sample_type="right")
            for i, rect in enumerate(rects):
                rect.set_fill(color=interpolate_color(RED_E, RED_C, i / len(rects)), opacity=0.7)
                if dx < 0.185:
                    rect.set_stroke(width=0)  # só sem borda se estiver bem refinado
                else:
                    rect.set_stroke(width=0.5)
            rect_list.append(rects)
        

        a_line = Line(ax1.c2p(1,0), ax1.c2p(1,f(1)), stroke_width=3).set_opacity(0.5).set_z_index(5)
        b_line = Line(ax1.c2p(7,0), ax1.c2p(7,f(7)), stroke_width=3).set_opacity(0.5).set_z_index(5)

        a_label = MathTex('a').next_to(ax1.c2p(1,0), UP, buff=0.15)
        b_label = MathTex('b').next_to(ax1.c2p(7,0), UP, buff=0.15)


        t3_brace = Brace(rect_list[0][-1], RIGHT, color=RED).scale(0.95)
        t3 = MathTex('f(b) < 0', color=RED).scale(0.9).next_to(t3_brace, RIGHT)


        area = ax1.get_area(gr1,
                            x_range=(1, 7),
                            color=(RED_C, RED_E)
                            ).set_fill(opacity=0).set_stroke(width=0).set_z_index(-2)
        self.add(area)

        self.play(LaggedStart(FadeIn(a_line, b_line, a_label, b_label),
                              ReplacementTransform(flat_rects, rect_list[0]),
                              lag_ratio=0.2))
        self.wait(2)
        self.play(FadeIn(t3_brace, t3))
        self.wait(2)
        self.play(LaggedStart(FadeOut(rect_list[0]), 
                              area.animate.set_opacity(0.6), 
                              lag_ratio=0.05),
                  LaggedStart(t3[0][4:].animate.next_to(t1, RIGHT, buff=0.2),
                              FadeOut(t3_brace, t3[0][0:4]),
                              lag_ratio=0.1))
        self.wait(2)
        self.play(FadeOut(gr1, gr1_label, a_line, b_line, a_label, b_label, area, t3[0][4:]))
        self.wait(2)



# Função com parte positiva e parte negativa
class vid9(MovingCameraScene):
    def construct(self):
        
        # Retomando elementos
        ax1 = Axes(x_range=[-1, 11], x_length=8,
                   y_range=[-5, 9], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0).set_z_index(10)
        ax1_zero_label = MathTex('0').scale(0.9).set_color(GRAY).next_to(ax1.c2p(0,0), DOWN, buff=0.12).shift(LEFT*0.25)
        ax1_x_label = always_redraw(lambda: MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2))
        ax1_y_label = always_redraw(lambda: MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2))

        def f(x):
            return 0.08*(x-0)*(x-5)*(x-10) + x/8

        gr1 = ax1.plot(f, x_range=[-4, 12], stroke_width=4, color=BLUE).set_z_index(11)
        gr1_label = MathTex('y = f(x)', color=BLUE).shift(UP*3.5+RIGHT*5.5).scale(0.9)

        t1 = MathTex(r'\int_{a}^{b} f(x) \,dx')
        t1[0][3:7].set_color(BLUE)
        
        self.add(ax1, ax1_x_label, ax1_y_label, t1.shift(UP*2.5))



        t2 = MathTex(r'\int_{a}^{b} f(x) \,dx =','10','-7','= 3').shift(UP*2.5+RIGHT*0.4)
        t2[0][3:7].set_color(BLUE)
        t2[1].set_color(GREEN)
        t2[2].set_color(RED)

        self.play(LaggedStart(Create(gr1),
                              FadeIn(gr1_label),
                              lag_ratio=0.3),
                              run_time=1.5)
        self.wait(2)



        pos_area = ax1.get_area(gr1,
                            x_range=(0, 5.335),
                            color=(GREEN_C, GREEN_E)
                            ).set_fill(opacity=0).set_stroke(width=0).set_z_index(-2)
        neg_area = ax1.get_area(gr1,
                            x_range=(5.335, 9.65),
                            color=(RED_C, RED_E)
                            ).set_fill(opacity=0).set_stroke(width=0).set_z_index(-2)
        
        t_pos_area = MathTex('10', color=WHITE).move_to(pos_area).shift(LEFT*0.2+DOWN*0.1)
        t_neg_area = MathTex('- \: 7', color=WHITE).move_to(neg_area).shift(RIGHT*0.1+UP*0.05)
        
        self.play(pos_area.animate.set_opacity(0.6),
                  neg_area.animate.set_opacity(0.6),
                  FadeIn(t_pos_area, t_neg_area))
        self.wait(2)
        self.play(LaggedStart(t1.animate.move_to(t2[0][0:9]),
                              FadeIn(t2[0][9]),
                              AnimationGroup(t_pos_area.animate.move_to(t2[1]).set_color(GREEN),
                                             t_neg_area.animate.move_to(t2[2]).set_color(RED)),
                              lag_ratio=0.1))
        self.wait(2)
        self.play(LaggedStart(FadeIn(t2[3][0]),
                              FadeIn(t2[3][1]),
                              lag_ratio=0.1))
        self.wait(2)
        


# Integrando da direita para a esquerda
class vid10(MovingCameraScene):
    def construct(self):        

        ax1 = Axes(x_range=[-1, 11], x_length=8,
                   y_range=[-0.75, 6], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0).set_z_index(-3)
        ax1_zero_label = MathTex('0').scale(0.9).set_color(GRAY).next_to(ax1.c2p(0,0), DOWN, buff=0.12).shift(LEFT*0.25)
        ax1_x_label = always_redraw(lambda: MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2))
        ax1_y_label = always_redraw(lambda: MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2))

        def f(x):
            return 0.02*(x-0)*(x-3)*(x-6) + 2.5

        gr1 = ax1.plot(f, x_range=[-4, 10], stroke_width=4, color=BLUE).set_z_index(-3)
        gr1_label = MathTex('y = f(x)', color=BLUE).shift(UP*3.5+RIGHT*4.05).scale(0.9)

        a_line = Line(ax1.c2p(1.5,0), ax1.c2p(1.5,f(1.5)), stroke_width=3).set_opacity(0.5).set_z_index(-3)
        b_line = Line(ax1.c2p(5.25,0), ax1.c2p(5.25,f(5.25)), stroke_width=3).set_opacity(0.5).set_z_index(-3)
        c_line = Line(ax1.c2p(9,0), ax1.c2p(9,f(9)), stroke_width=3).set_opacity(0.5).set_z_index(-3)

        a_label = MathTex('a').next_to(ax1.c2p(1.5,0), DOWN, buff=0.15)
        b_label = MathTex('b').next_to(ax1.c2p(5.25,0), DOWN, buff=0.15)
        c_label = MathTex('c').next_to(ax1.c2p(9,0), DOWN, buff=0.15)

        self.play(FadeIn(ax1, ax1_zero_label, ax1_x_label, ax1_y_label, gr1, gr1_label, a_line, b_line, a_label, b_label))
        self.wait(2)



        t1 = MathTex(r'\int_{a}^{b} f(x) \,dx',r'> 0').scale(0.9).shift(UP*1.8).set_z_index(3)
        t1[0][3:7].set_color(BLUE)
        t1[1].set_color(GREEN)

        X_F_area_1 = ValueTracker(1.5)
        F_area_1 = always_redraw(lambda: 
                               ax1.get_area(
                               gr1,
                               x_range=(1.5, X_F_area_1.get_value()),
                               color=(GREEN_C, GREEN_E)
                               ).set_fill(opacity=0.6).set_stroke(width=0).set_z_index(-4))
        self.add(F_area_1)
        self.play(LaggedStart(FadeIn(t1),
                              X_F_area_1.animate.set_value(5.25),
                              lag_ratio=0.1),
                  run_time=2)
        self.wait(2)
        self.play(FadeOut(F_area_1))
        self.wait(2)



        X_F_area_2 = ValueTracker(5.25)
        F_area_2 = always_redraw(lambda: 
                               ax1.get_area(
                               gr1,
                               x_range=(X_F_area_2.get_value(), 5.25),
                               color=(RED_C, RED_E)
                               ).set_fill(opacity=0.6).set_stroke(width=0).set_z_index(-4))
        self.add(F_area_2)
        self.play(LaggedStart(AnimationGroup(t1[0][1].animate.move_to(t1[0][2]).shift(LEFT*0.05), 
                                             t1[0][2].animate.move_to(t1[0][1]).shift(RIGHT*0.05),
                                             t1[1][0].animate.rotate(180*DEGREES).set_color(RED)),
                              X_F_area_2.animate.set_value(1.5),
                              lag_ratio=0.1),
                  run_time=2)
        self.wait(2)
        self.play(LaggedStart(FadeOut(t1, F_area_2),
                              FadeIn(c_line, c_label),
                              lag_ratio=0.5))
        self.wait(2)



        # Área em [a,c] é igual a área [a,b] + área em [b,c]
        t2 = MathTex(r'\int_{a}^{c} f(x) \,dx =',r'\int_{a}^{b} f(x) \,dx +',r'\int_{b}^{c} f(x) \,dx', color=GREEN).scale(0.9).shift(UP*1.8).set_z_index(-1)
        VGroup(t2[0][9], t2[1][9]).set_color(WHITE)
        t2_sr_1 = SurroundingRectangle(t2[0], color=BLACK, buff=0.2, fill_opacity=0.8, stroke_width=0).set_z_index(-2)
        t2_sr_2 = SurroundingRectangle(t2[2], color=BLACK, buff=0.2, fill_opacity=0.8, stroke_width=0).set_z_index(-2)
        
        X_F_area_1.set_value(1.5)
        self.add(F_area_1)
        self.play(LaggedStart(FadeIn(t2[0], t2_sr_1),
                              X_F_area_1.animate.set_value(9),
                              lag_ratio=0.1), 
                  run_time=2)
        self.wait(2)



        aux1 = ax1.get_area(gr1, x_range=(1.5, 5.25), color=BLACK).set_fill(opacity=0).set_stroke(width=0).set_z_index(0)
        aux2 = ax1.get_area(gr1, x_range=(5.25, 9), color=BLACK).set_fill(opacity=0).set_stroke(width=0).set_z_index(0)

        self.play(aux2.animate.set_opacity(1),
                  FadeIn(t2[1]))
        self.wait(2)
        self.play(aux2.animate.set_opacity(0), 
                  aux1.animate.set_opacity(1),
                  FadeIn(t2[2], t2_sr_2))
        self.wait(2)
        self.play(aux1.animate.set_opacity(0))
        self.wait(2)



        # Se 'c' for igual ao 'a'
        self.remove(c_line, c_label)

        C_VALUE = ValueTracker(9)
        c_line = always_redraw(lambda: Line(ax1.c2p(C_VALUE.get_value(),0), ax1.c2p(C_VALUE.get_value(),f(C_VALUE.get_value())), stroke_width=3).set_opacity(0.5).set_z_index(-3))
        c_label = always_redraw(lambda: MathTex('c').next_to(ax1.c2p(C_VALUE.get_value(),0), DOWN, buff=0.15))
        
        self.add(c_line, c_label)
        
        t3 = MathTex(r'\int_{a}^{a} f(x) \,dx =',r'\int_{a}^{b} f(x) \,dx +',r'\int_{b}^{a} f(x) \,dx', color=GREEN).scale(0.9).move_to(t2, aligned_edge=LEFT).set_z_index(-1)
        VGroup(t3[0][9], t3[1][9]).set_color(WHITE)
        VGroup(t3[0][1], t3[2][1]).set_color(YELLOW)
        self.play(X_F_area_1.animate.set_value(1.5),
                  C_VALUE.animate.set_value(1.5),
                  run_time=3)
        self.play(FadeOut(c_label))
        self.wait(2)
        self.play(ReplacementTransform(t2[0][1], t3[0][1]),
                  ReplacementTransform(t2[2][1], t3[2][1]),
                  Flash(t2[0][1], num_lines=8, z_index=10),
                  Flash(t2[2][1], num_lines=8, z_index=10))
        self.play(VGroup(t3[0][1], t3[2][1]).animate.set_color(GREEN))
        self.wait(2)



        t4 = MathTex('= 0').scale(0.9).next_to(t2, RIGHT, buff=0.2)

        self.play(VGroup(t2[0][0], t3[0][1], t2[0][2:9]).animate.set_color(YELLOW))
        self.wait(2)
        self.play(VGroup(t2[0][0], t3[0][1], t2[0][2:9]).animate.set_color(GREEN))
        self.play(LaggedStart(AnimationGroup(VGroup(t2[0][0], t3[0][1], t2[0][2:]).animate.shift(LEFT*2).set_opacity(0),
                                             t2[1:].animate.shift(LEFT*2),
                                             FadeOut(t2_sr_1)),
                              FadeIn(t4.shift(LEFT*2)),
                              lag_ratio=0.1),
                              run_time=2)
        self.wait(2)
        self.play(LaggedStart(VGroup(t2[1][9], t2[2], t4).animate.set_opacity(0.3),
                              X_F_area_1.animate.set_value(5.25),
                              lag_ratio=0.5),
                  run_time=2.5)
        self.wait(2)
        X_F_area_2.set_value(5.25)
        self.add(F_area_2)
        self.play(LaggedStart(FadeOut(F_area_1),
                              AnimationGroup(VGroup(t2[1][9], t2[2]).animate.set_opacity(1),
                                             VGroup(t2[1]).animate.set_opacity(0.3)),
                              X_F_area_2.animate.set_value(1.5),
                              lag_ratio=0.5), 
                  run_time=2.5)
        self.wait(2)
        self.play(VGroup(t2[1], t4).animate.set_opacity(1))
        self.wait(2)



        t5 = MathTex(r'- \int_{b}^{a} f(x) \,dx', color=RED).scale(0.9).next_to(t2, RIGHT, buff=0.2, aligned_edge=DOWN).set_z_index(-1).shift(LEFT*2.1)
        
        self.play(MoveAlongPath(t2[2], ArcBetweenPoints(t2[2].get_center(), t5[0][1:].get_center(), radius=-0.5)),
                  FadeOut(t2[1][9], t4[0][1]),
                  FadeIn(t5[0][0]),
                  t4[0][0].animate.shift(LEFT*2.6))
        self.play(t2[2].animate.set_color(RED))
        self.wait(2)



# Semelhanças entre derivada e integral
class vid11(MovingCameraScene):
    def construct(self):  

        t1_1 = Tex('Derivada').scale(1.1)
        t2_1 = Tex('Integral').scale(1.1)
        VGroup(t1_1, t2_1).arrange(RIGHT, buff=3).shift(UP*1.3)

        t1_2 = MathTex(r'\frac{d}{dx} f(x)').scale(1.2).next_to(t1_1, DOWN*3.3)
        t2_2 = MathTex(r'\int_{a}^{b} f(x) \,dx').scale(1.2).next_to(t2_1, DOWN*3.3)
        t2_2[0][1:3].shift(RIGHT*0.15)
        t2_2[0][0].shift(RIGHT*0.1)
        t2_2[0][2:].shift(LEFT*0.1)
        VGroup(t1_2[0][0:4], t2_2[0][0:3], t2_2[0][7:]).set_color(YELLOW)
        VGroup(t1_2[0][4:], t2_2[0][3:7]).set_color(BLUE)

        VGroup(t1_1, t1_2).shift(LEFT*6)
        VGroup(t2_1, t2_2).shift(RIGHT*6)

        self.play(LaggedStart(VGroup(t1_1, t1_2).animate.shift(RIGHT*6),
                              VGroup(t2_1, t2_2).animate.shift(LEFT*6),
                              lag_ratio=0.5),
                              run_time=3)
        self.wait(2)



        # Resumo: derivada
        SCALE_FACTOR = 0.3
        derivative_frame = Rectangle(width=16*SCALE_FACTOR, height=9*SCALE_FACTOR, stroke_width=1.5).next_to(t1_1, DOWN, buff=0.5)

        ax1 = Axes(x_range=[-1, 14], x_length=8,
                   y_range=[-1, 9], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).set_stroke(width=1).shift(DOWN*0.6)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

            # Definindo a função f(x)
        def f(x):
            return (x + 1) / 2 + np.sin(x - 1) + np.sin((x + 1) / 2)

            # Derivada de f(x)
        def f_prime(x):
            return 0.5 + np.cos(x - 1) + 0.5 * np.cos((x + 1) / 2)
        
        gr1 = ax1.plot(f, x_range=[0.4, 13], stroke_width=1.25, color=BLUE).set_z_index(2)
        gr1_label = MathTex('y = f(x)', color=BLUE).next_to(gr1, RIGHT).shift(UP*2+LEFT*0)
        
        t1 = MathTex(r'\frac{\Delta y}{\Delta x}',r'= \frac{f(x+h) - f(x)}{h}').scale(0.9).shift(UP*3+RIGHT)
        t2 = MathTex(r'\frac{dy}{dx}',r'= \lim_{h \to 0}',r'\frac{f(x+h) - f(x)}{h}').scale(0.9).move_to(t1, aligned_edge=LEFT).shift(RIGHT*0.1)
        VGroup(t1[0][0:2], t1[1][1:12], t2[0][0:2], t2[2][0:11]).set_color(PURPLE)
        VGroup(t1[0][3:], t1[1][5], t1[1][13], t2[0][3:], t2[2][4], t2[2][12]).set_color(RED)

        DX_COLOR = RED
        DY_COLOR = PURPLE
        X = ValueTracker(6)
        DX = ValueTracker(4)

        delta_y_line = always_redraw(lambda: Line(ax1.c2p(X.get_value() + DX.get_value(), f(X.get_value()), 0), ax1.c2p(X.get_value() + DX.get_value(), f(X.get_value() + DX.get_value()), 0), color=DY_COLOR, stroke_width=1))
        delta_x_line = always_redraw(lambda: Line(ax1.c2p(X.get_value(), f(X.get_value()), 0), ax1.c2p(X.get_value() + DX.get_value(), f(X.get_value()), 0), color=DX_COLOR, stroke_width=1))

        delta_y_label = always_redraw(lambda: MathTex(r'\Delta y', color=DY_COLOR).scale(DX.get_value()/4).next_to(delta_y_line, RIGHT, buff=0.1))
        delta_x_label = always_redraw(lambda: MathTex(r'\Delta x', color=DX_COLOR).scale(DX.get_value()/4).next_to(delta_x_line, DOWN, buff=0.1))

        VGroup(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label, 
               t1, t2, delta_y_line, delta_x_line, delta_y_label, delta_x_label).move_to(derivative_frame).scale(0.3).shift(DOWN*0.1)


        self.camera.frame.save_state()
        self.play(LaggedStart(FadeOut(t1_2),
                              FadeIn(derivative_frame, 
                                     ax1, ax1_x_label, ax1_y_label, gr1, gr1_label,
                                     delta_y_line, delta_x_line, delta_y_label, delta_x_label, t1),
                              self.camera.frame.animate.move_to(derivative_frame).scale(0.3).shift(DOWN*0.1),
                              lag_ratio=0.3),
                              run_time=3)
        self.wait(2)


        self.remove(delta_y_line, delta_x_line, delta_y_label, delta_x_label)

        delta_y_line = always_redraw(lambda: Line(ax1.c2p(X.get_value() + DX.get_value(), f(X.get_value()), 0), ax1.c2p(X.get_value() + DX.get_value(), f(X.get_value() + DX.get_value()), 0), color=DY_COLOR, stroke_width=1))
        delta_x_line = always_redraw(lambda: Line(ax1.c2p(X.get_value(), f(X.get_value()), 0), ax1.c2p(X.get_value() + DX.get_value(), f(X.get_value()), 0), color=DX_COLOR, stroke_width=1))

        delta_y_label = always_redraw(lambda: MathTex(r'\Delta y', color=DY_COLOR).scale(0.3*DX.get_value()/4).next_to(delta_y_line, RIGHT, buff=0.1*0.3))
        delta_x_label = always_redraw(lambda: MathTex(r'\Delta x', color=DX_COLOR).scale(0.3*DX.get_value()/4).next_to(delta_x_line, DOWN, buff=0.1*0.3))

        self.add(delta_y_line, delta_x_line, delta_y_label, delta_x_label)

        self.play(DX.animate.set_value(0.7),
                  LaggedStart(t1[0][0:2].animate.scale(0),
                              GrowFromCenter(t2[0][0:2]),
                              lag_ratio=0.2),
                  LaggedStart(t1[0][3:].animate.scale(0),
                              GrowFromCenter(t2[0][3:]),
                              lag_ratio=0.2),
                  LaggedStart(ReplacementTransform(t1[1][1:], t2[2]),
                              FadeIn(t2[1][1:]),
                              lag_ratio=0.1),
                  run_time=1.5)

        self.add(delta_y_line.copy(), delta_x_line.copy())
        self.remove(delta_y_line, delta_x_line)

        dy_label = MathTex(r'dy', color=DY_COLOR).scale(0.3).next_to(delta_y_line, RIGHT, buff=0.1*0.3)
        dx_label = MathTex(r'dx', color=DX_COLOR).scale(0.3).next_to(delta_x_line, DOWN, buff=0.1*0.3)

        self.play(FadeOut(delta_y_label, delta_x_label),
                  GrowFromCenter(dy_label),
                  GrowFromCenter(dx_label))
        self.wait(2)
        self.play(self.camera.frame.animate.restore(),
                  run_time=2)
        self.wait(2)



        # Resumo: integral
        integral_frame = derivative_frame.copy().next_to(derivative_frame, RIGHT, buff=0.2)

        ax1 = Axes(x_range=[-1, 11], x_length=8,
                   y_range=[-0.75, 6], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0).scale(0.6).scale(1.5).set_stroke(width=1)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*2.7+RIGHT*0.2)

        def f(x):
            return 0.1*(x-2-0)*(x-2-PI)*(x-2-2*PI) + 2.5

        gr1 = ax1.plot(f, x_range=[0.7, 9.7], stroke_width=1.25, color=BLUE)
        gr1_label = MathTex('y = f(x)', color=BLUE).shift(UP*2.95+RIGHT*3.75).scale(0.9)
        
        dx_list = [2 * PI / n for n in [10, 16, 24, 34, 200]]
        rect_list = []
        for dx in dx_list:
            rects = ax1.get_riemann_rectangles(gr1, x_range=[2, 2 * PI + 2], dx=dx, input_sample_type="center")
            for i, rect in enumerate(rects):
                rect.set_fill(color=interpolate_color(PURPLE, ORANGE, i / len(rects)), opacity=0.7)
                rect.set_stroke(width=0.2)
            rect_list.append(rects)

        t1 = MathTex(r'A \:\approx\:',
                    r'\sum_{i=1}^{n}',
                    r'f(\overline{x}_i) \Delta x'
                    ).scale(0.8).set_z_index(3).shift(UP*2.5+LEFT*0.5)
        t2 = MathTex(r'A \:=',
                    r'\lim_{n \to \infty} \:',
                    r'\sum_{i=1}^{n}',
                    r'f(\overline{x}_i) \Delta x'
                    ).scale(0.8).set_z_index(3).move_to(t1, aligned_edge=LEFT)

        delta_x_brace = Brace(Line(ax1.c2p(2 + 4*2*PI/10,0), ax1.c2p(2 + 5*2*PI/10,0)), DOWN, buff=0.1)
        delta_x_label = MathTex(rf'\Delta x').scale(0.8).next_to(delta_x_brace, DOWN, buff=0.1)
        
        dx_brace = Brace(Line(ax1.c2p(2 + 15*2*PI/34,0), ax1.c2p(2 + 16*2*PI/34,0)), DOWN, buff=0.1)
        dx_label = MathTex(rf'dx').scale(0.8).next_to(dx_brace, DOWN, buff=0.1)
        
        VGroup(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label, 
               *rect_list, t1, t2, delta_x_brace, delta_x_label,
               dx_brace, dx_label).move_to(integral_frame).scale(0.35)
        

        self.play(LaggedStart(FadeOut(t2_2),
                              FadeIn(integral_frame, 
                                     ax1, ax1_x_label, ax1_y_label, gr1, gr1_label,
                                     rect_list[0], delta_x_brace, delta_x_label, t1),
                              self.camera.frame.animate.move_to(integral_frame).scale(0.3),
                              lag_ratio=0.3),
                              run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(rect_list[0], rect_list[3]),
                  LaggedStart(delta_x_label.animate.scale(0),
                              GrowFromCenter(dx_label),
                              lag_ratio=0.2),
                  ReplacementTransform(delta_x_brace, dx_brace),
                  ReplacementTransform(t1[0][1], t2[0][1]),
                  ReplacementTransform(t1[1:], t2[2:]),
                  FadeIn(t2[1]))
        self.wait(2)
        self.play(self.camera.frame.animate.restore(), 
                  run_time=2)
        self.wait(2)



        # Derivada e integral são o resultado de um limite
        t1_3 = MathTex(r'\lim_{h \to 0} \frac{f(x+h) - f(x)}{h}', color=YELLOW).scale(0.9).move_to(derivative_frame).set_z_index(20).shift(UP*0.1)
        t2_3 = MathTex(r'\lim_{n \to \infty} \:\sum_{i=1}^{n} f(\overline{x}_i) \Delta x', color=YELLOW).scale(0.9).move_to(integral_frame).set_z_index(20).shift(UP*0.1)

        black_sq = Square(color=BLACK, fill_opacity=1).scale(20).next_to(t1_1, DOWN, buff=0.3).set_z_index(19)
        self.play(LaggedStart(FadeIn(black_sq),
                              FadeIn(t1_3, t2_3),
                              lag_ratio=0.2))
        self.wait(2)
