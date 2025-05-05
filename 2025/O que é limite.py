# O que é limite

from manim import *

# Isto é uma função...
class vid0(MovingCameraScene):
    def construct(self):

        t1 = MathTex('f(x) = 2x + 1').shift(DOWN*4.5)
        VGroup(t1[0][2], t1[0][6]).set_color(BLUE)

        self.play(t1.animate.shift(UP*4.5), run_time=2)
        self.wait(2)


        # Calculando o valor da função para vários valores de 'x'
        t2 = MathTex(r'f(1) = 2 \cdot 1 + 1', color=BLUE).move_to(t1, aligned_edge=DL)
        t3 = MathTex('= 3', color=GRAY).next_to(t2, RIGHT, buff=0.2)

        t4 = MathTex(r'f(2) = 2 \cdot 2 + 1', color=BLUE).move_to(t1, aligned_edge=DL)
        t5 = MathTex('= 5', color=GRAY).next_to(t2, RIGHT, buff=0.2)

        t6 = MathTex(r'f(3) = 2 \cdot 3 + 1', color=BLUE).move_to(t1, aligned_edge=DL)
        t7 = MathTex('= 7', color=GRAY).next_to(t2, RIGHT, buff=0.2)
        
        t8 = MathTex(r'f(4) = 2 \cdot 4 + 1', color=BLUE).move_to(t1, aligned_edge=DL)
        t9 = MathTex('= 9', color=GRAY).next_to(t2, RIGHT, buff=0.2)
        
        t10 = MathTex(r'f(5) = 2 \cdot 5 + 1', color=BLUE).move_to(t1, aligned_edge=DL)
        t11 = MathTex('= 11', color=GRAY).next_to(t2, RIGHT, buff=0.2)

        VGroup(t2[0][6], t4[0][6], t6[0][6], t8[0][6], t10[0][6]).set_color(WHITE)

        self.play(FadeOut(t1[0][2], t1[0][6]), 
                  t1[0][7:].animate.move_to(t2, aligned_edge=RIGHT),
                  FadeIn(t2[0][2], shift=UP),
                  FadeIn(t2[0][6]),
                  FadeIn(t2[0][7], shift=UP),
                  FadeIn(t3))

        self.play(FadeOut(t2[0][2], shift=UP),
                  FadeOut(t2[0][6]),
                  FadeOut(t2[0][7], shift=UP),
                  FadeIn(t4[0][2], shift=UP),
                  FadeIn(t4[0][6]),
                  FadeIn(t4[0][7], shift=UP),
                  FadeOut(t3[0][1]), FadeIn(t5[0][1]))

        self.play(FadeOut(t4[0][2], shift=UP),
                  FadeOut(t4[0][6]),
                  FadeOut(t4[0][7], shift=UP),
                  FadeIn(t6[0][2], shift=UP),
                  FadeIn(t6[0][6]),
                  FadeIn(t6[0][7], shift=UP),
                  FadeOut(t5[0][1]), FadeIn(t7[0][1]))

        self.play(FadeOut(t6[0][2], shift=UP),
                  FadeOut(t6[0][6]),
                  FadeOut(t6[0][7], shift=UP),
                  FadeIn(t8[0][2], shift=UP),
                  FadeIn(t8[0][6]),
                  FadeIn(t8[0][7], shift=UP),
                  FadeOut(t7[0][1]), FadeIn(t9[0][1]))

        self.play(FadeOut(t8[0][2], shift=UP),
                  FadeOut(t8[0][6]),
                  FadeOut(t8[0][7], shift=UP),
                  FadeIn(t10[0][2], shift=UP),
                  FadeIn(t10[0][6]),
                  FadeIn(t10[0][7], shift=UP),
                  FadeOut(t9[0][1]), FadeIn(t11[0][1:]))

        self.wait(2)

        self.play(self.camera.frame.animate.shift(DOWN*5), run_time=1.5)

        self.wait(2)



# Algumas funções não aceitam qualquer valor para 'x'
class vid1(MovingCameraScene):
    def construct(self):

        t1 = MathTex(r'f(x) = \frac{1}{x}')
        VGroup(t1[0][2], t1[0][7]).set_color(BLUE)

        self.play(FadeIn(t1))
        self.wait(2)



        t2 = MathTex(r'f(1) = \frac{1}{1}', color=BLUE)
        t2[0][7].set_opacity(0)
        t2[0][2].shift(LEFT*0.015+DOWN*0.01)

        t3 = MathTex('= 1', color=GRAY).next_to(t2, RIGHT, buff=0.3)


        t4 = MathTex(r'f(2) = \frac{1}{2}', color=BLUE)
        t4[0][7].set_opacity(0)
        t4[0][2].shift(LEFT*0.015+DOWN*0.01)

        t5 = MathTex('= 0,5', color=GRAY).move_to(t3, aligned_edge=LEFT)


        t6 = MathTex(r'f(3) = \frac{1}{3}', color=BLUE)
        t6[0][7].set_opacity(0)
        t6[0][2].shift(LEFT*0.015+DOWN*0.01)

        t7 = MathTex('= 0,333...', color=GRAY).move_to(t3, aligned_edge=LEFT)


        t8 = MathTex(r'f(4) = \frac{1}{4}', color=BLUE)
        t8[0][7].set_opacity(0)
        t8[0][2].shift(LEFT*0.015+DOWN*0.01)

        t9 = MathTex('= 0,25', color=GRAY).move_to(t3, aligned_edge=LEFT)


        t10 = MathTex(r'f(0) = \frac{1}{0}', color=RED)
        t10[0][7].set_opacity(0)
        t10[0][2].shift(LEFT*0.015+DOWN*0.01)

        t11 = MathTex(r'= \:\: ?', color=GRAY).move_to(t3, aligned_edge=LEFT)



        arc1 = Arc(angle=PI/2).rotate(PI/2).move_to(t2[0][7], aligned_edge=UR).shift(DOWN*0.2+LEFT*0.08).reverse_points()
        arc2 = arc1.copy().rotate(-PI/2).next_to(arc1, RIGHT, buff=0)

        self.play(FadeOut(t1[0][2], t1[0][7]),
                  FadeIn(t2[0][2], shift=UP),
                  AnimationGroup(t2[0][7].animate.set_opacity(1), MoveAlongPath(t2[0][7], path=arc1)),
                  FadeIn(t3))

        self.play(FadeOut(t2[0][2], shift=UP),
                  AnimationGroup(t2[0][7].animate.set_opacity(0), MoveAlongPath(t2[0][7], path=arc2)),
                  FadeIn(t4[0][2], shift=UP),
                  AnimationGroup(t4[0][7].animate.set_opacity(1), MoveAlongPath(t4[0][7], path=arc1)),
                  FadeOut(t3[0][1]), FadeIn(t5[0][1:]))
        
        self.play(FadeOut(t4[0][2], shift=UP),
                  AnimationGroup(t4[0][7].animate.set_opacity(0), MoveAlongPath(t4[0][7], path=arc2)),
                  FadeIn(t6[0][2], shift=UP),
                  AnimationGroup(t6[0][7].animate.set_opacity(1), MoveAlongPath(t6[0][7], path=arc1)),
                  FadeOut(t5[0][1:]), FadeIn(t7[0][1:]))
        
        self.play(FadeOut(t6[0][2], shift=UP),
                  AnimationGroup(t6[0][7].animate.set_opacity(0), MoveAlongPath(t6[0][7], path=arc2)),
                  FadeIn(t8[0][2], shift=UP),
                  AnimationGroup(t8[0][7].animate.set_opacity(1), MoveAlongPath(t8[0][7], path=arc1)),
                  FadeOut(t7[0][1:]), FadeIn(t9[0][1:]))
        
        self.play(FadeOut(t8[0][2], shift=UP),
                  AnimationGroup(t8[0][7].animate.set_opacity(0), MoveAlongPath(t8[0][7], path=arc2)),
                  FadeIn(t10[0][2], shift=UP),
                  AnimationGroup(t10[0][7].animate.set_opacity(1), MoveAlongPath(t10[0][7], path=arc1)),
                  FadeOut(t9[0][1:]), FadeIn(t11[0][1:]))

        self.wait(2)


        g_all_1 = VGroup(t1[0][0:2], t1[0][3:7], t3[0][0], t10[0][2], t10[0][7], t11[0][1:])
        
        self.play(Wiggle(g_all_1))
        self.wait(2)


        # Essa função não está definida para x = 0
        self.play(FadeOut(t10[0][2], shift=UP),
                  AnimationGroup(t10[0][7].animate.set_opacity(0), MoveAlongPath(t10[0][7], path=arc2)),
                  FadeIn(t1[0][2], t1[0][7]),
                  FadeOut(t3[0][0], t11[0][1:]))


        t12 = Tex(r'não está definida para ','$x = 0$').shift(DOWN*4.5)
        t12[1][0].set_color(BLUE)
        t12[1][2].set_color(RED)

        self.play(t12.animate.shift(UP*3), run_time=2)
        self.wait(2)


        # Transição para a próxima cena
        num_line = NumberLine(x_range=[-3.7, 3.9], include_ticks=True, include_tip=True, include_numbers=True)
        num_line_0 = MathTex('0', color=RED).scale(0.75).shift(DOWN*0.38+LEFT*0.1)

        X_VALUE = ValueTracker(0.1)
        x_tick = always_redraw(lambda: Line(ORIGIN, UP*0.2, color=BLUE).move_to(num_line.number_to_point(X_VALUE.get_value())).set_z_index(2))
        x_tick_dl = always_redraw(lambda: DashedLine(x_tick.get_center(), Dot().move_to(x_tick.get_center()).shift(DOWN*1), color=BLUE).set_opacity(0.5).scale(0.9))
        x_label = always_redraw(lambda: MathTex(r'x','=', f'{X_VALUE.get_value():.1f}').set_color_by_tex('x', BLUE).next_to(x_tick_dl, DOWN, buff=0.1).shift(RIGHT*0.64+UP*0.1))
        group = VGroup(num_line, num_line_0, x_tick, x_tick_dl, x_label).shift(UP*6)
        self.add(group)

        self.play(LaggedStart(t12.animate.shift(DOWN*5),
                              t1.animate.shift(DOWN*6),
                              AnimationGroup(self.camera.frame.animate.shift(UP*6),
                                             X_VALUE.animate.set_value(-0.5)),
                              lag_ratio=0.15),
                              run_time=3)
        self.play(X_VALUE.animate.set_value(3), run_time=1.9)
        self.play(X_VALUE.animate.set_value(1.5), run_time=1.6)
        self.wait(2)



# Calculando a função para números próximos de zero
class vid2(MovingCameraScene):
    def construct(self):

        num_line = NumberLine(x_range=[-3.7, 3.9], include_ticks=True, include_tip=True, include_numbers=True)
        num_line_0 = MathTex('0', color=RED).scale(0.75).shift(DOWN*0.38+LEFT*0.1)
        
        X_VALUE = ValueTracker(1.5)
        x_tick = always_redraw(lambda: Line(ORIGIN, UP*0.2, color=BLUE).move_to(num_line.number_to_point(X_VALUE.get_value())).set_z_index(2))
        x_tick_dl = always_redraw(lambda: DashedLine(x_tick.get_center(), Dot().move_to(x_tick.get_center()).shift(DOWN*1), color=BLUE).set_opacity(0.5).scale(0.9))
        x_label = always_redraw(lambda: MathTex(r'x','=', f'{X_VALUE.get_value():.1f}').set_color_by_tex('x', BLUE).next_to(x_tick_dl, DOWN, buff=0.1).shift(RIGHT*0.64+UP*0.1))

        self.add(num_line, num_line_0, x_tick, x_tick_dl, x_label)


        # Escolhendo números próximos do zero
        self.play(X_VALUE.animate.set_value(0.5),
                  self.camera.frame.animate.scale(0.9), run_time=2)
        self.wait(2)
        self.play(X_VALUE.animate.set_value(0.1),
                  self.camera.frame.animate.scale(0.9), run_time=2)
        self.wait(2)


        t1 = MathTex('00001').next_to(x_label, RIGHT, buff=0).shift(LEFT*0.05)

        self.play(self.camera.frame.animate.scale(0.8),
                  LaggedStart(X_VALUE.animate.set_value(0),
                              FadeIn(t1[0][0]),
                              FadeIn(t1[0][1]),
                              FadeIn(t1[0][2]),
                              FadeIn(t1[0][3]),
                              FadeIn(t1[0][4]),
                              lag_ratio=0.3), 
                              run_time=5)
        self.wait(2)


        t2 = MathTex('f(x)',r'\rightarrow','L',r'\neq f(0)').shift(UP*2)
        t2[0][2].set_color(BLUE)
        t2[2][0].set_color(YELLOW)
        t2[3][4].set_color(RED)

        self.play(FadeIn(t2[0]),
                  self.camera.frame.animate.scale(1.543), run_time=2)
        self.wait()
        self.play(FadeIn(t2[1]))
        self.wait()
        self.play(FadeIn(t2[2]))
        self.wait(2)
        self.play(LaggedStart(FadeIn(t2[3][0]), FadeIn(t2[3][1:]), lag_ratio=0.1))
        self.wait(2)

        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)



# Explicação da ideia intuitiva de limite
class vid3(MovingCameraScene):
    def construct(self):

        ax1 = Axes(x_range=[-1, 8], x_length=9,
                   y_range=[-1, 5], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        gr1 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[0.4, 8], stroke_width=5, color=BLUE)
        gr1_label = MathTex('y = f(x)', color=BLUE).next_to(gr1, RIGHT).shift(UP*1.8+LEFT*0.1)
        

        # Criando o gráfico
        self.play(LaggedStart(FadeIn(ax1), FadeIn(ax1_x_label, ax1_y_label), Create(gr1), FadeIn(gr1_label), lag_ratio=0.2))
        self.wait(2)


        # Limite para x -> a
        A_COLOR = YELLOW
        L_COLOR = YELLOW

        dot_a_l = Dot(ax1.coords_to_point(3.5,2.38,0), color=A_COLOR)
        dot_a_l_black = dot_a_l.copy().set_color(BLACK).scale(0.6).set_z_index(4)

        a_tick = Line(ORIGIN, UP*0.2, color=A_COLOR).move_to(ax1.coords_to_point(3.5,0,0)).set_z_index(2)
        a_label = MathTex('a', color=A_COLOR).next_to(a_tick, DOWN, buff=0.2).set_z_index(2)
        a_line = DashedLine(a_tick, ax1.coords_to_point(3.5,2.38,0), color=A_COLOR).set_opacity(0.5).set_z_index(-1).set_z_index(2)
        
        l_tick = a_tick.copy().rotate(90*DEGREES).set_color(L_COLOR).move_to(ax1.coords_to_point(0,2.38,0)).set_z_index(2)
        l_label = MathTex('L', color=L_COLOR).next_to(l_tick, LEFT, buff=0.2).set_z_index(2)
        l_line = DashedLine(ax1.coords_to_point(3.5,2.38,0), l_tick, color=A_COLOR).set_opacity(0.5).set_z_index(-1).set_z_index(2)

        t1 = MathTex('?', color=A_COLOR).move_to(l_label)



            # Não conseguimos calcular 'f(a)'
        self.play(LaggedStart(FadeIn(a_tick, a_label, a_line),
                              AnimationGroup(GrowFromCenter(dot_a_l), GrowFromCenter(dot_a_l_black)),
                              FadeIn(l_tick, t1, l_line),
                              lag_ratio=0.05))
        self.wait(2)



        X_VALUE = ValueTracker(4.4)
        DOT_REF = always_redraw(lambda: Dot(gr1.get_point_from_function(t = X_VALUE.get_value()), color=BLUE).set_z_index(5))

        x_tick = always_redraw(lambda: Line(ORIGIN, UP*0.2).set_color(BLUE).move_to(ax1.coords_to_point(X_VALUE.get_value(),0,0)).set_z_index(2))
        x_line = always_redraw(lambda: DashedLine(DOT_REF, ax1.coords_to_point(X_VALUE.get_value(),-0.7,0), color=BLUE).set_opacity(0.5).set_z_index(-3))
        x_label = always_redraw(lambda: MathTex('x', color=BLUE).next_to(x_line, DOWN, buff=0.15).set_z_index(2))

        fx_tick = always_redraw(lambda: Line(ORIGIN, UP*0.2).rotate(90*DEGREES).set_color(BLUE).move_to(ax1.get_y_axis().number_to_point(DOT_REF.get_y() + 2.2)).set_z_index(2))
        fx_line = always_redraw(lambda: DashedLine(DOT_REF, Dot().move_to(fx_tick).shift(LEFT*0.8), color=BLUE).set_opacity(0.5).set_z_index(-3))
        fx_label = always_redraw(lambda: MathTex('f(x)', color=BLUE).next_to(fx_line, LEFT, buff=0.15).set_z_index(2))



        # A função varia pouco para 'x' próximo de 'a'
        HIGHLIGHT_COLOR = YELLOW

        X_LEFT_1 = 2.6
        X_RIGHT_1 = 4.4

        Y_LEFT_1 = 2.78
        Y_RIGHT_1 = 2.06

        x_highlight1 = Line(ax1.coords_to_point(X_LEFT_1,0,0), ax1.coords_to_point(X_RIGHT_1,0,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        y_highlight1 = Line(ax1.coords_to_point(0,Y_LEFT_1,0), ax1.coords_to_point(0,Y_RIGHT_1,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        graph_highlight1 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[X_LEFT_1, X_RIGHT_1], stroke_width=5, color=HIGHLIGHT_COLOR)
        a_bar1 = ax1.get_area(graph=gr1, x_range=(X_LEFT_1, X_RIGHT_1), 
                             color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        l_bar1 = Polygon(ax1.coords_to_point(0,Y_LEFT_1,0), 
                        ax1.coords_to_point(0,Y_RIGHT_1,0),
                        ax1.coords_to_point(X_RIGHT_1,Y_RIGHT_1,0), 
                        ax1.coords_to_point(X_LEFT_1,Y_LEFT_1,0),
                        color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)

        self.add(DOT_REF,
                 x_label, x_line, x_tick,
                 x_highlight1, graph_highlight1,
                 a_bar1)
        self.play(X_VALUE.animate.set_value(2.6), rate_func=linear)
        self.play(X_VALUE.animate.set_value(4.4),  rate_func=linear)
        self.play(X_VALUE.animate.set_value(2.6), rate_func=linear)
        self.play(X_VALUE.animate.set_value(4.4),  rate_func=linear)

        self.remove(t1)
        self.add(fx_tick, fx_label, fx_line, y_highlight1, l_bar1)
        self.play(X_VALUE.animate.set_value(2.6), rate_func=linear)
        self.play(X_VALUE.animate.set_value(4.4),  rate_func=linear)
        self.play(X_VALUE.animate.set_value(2.6), rate_func=linear)
        self.play(X_VALUE.animate.set_value(4.4),  rate_func=linear)



            # O intervalo ao redor de 'a' vai diminuindo
        X_LEFT_2 = 2.7
        X_RIGHT_2 = 4.3

        Y_LEFT_2 = 2.75
        Y_RIGHT_2 = 2.07

        x_highlight2 = Line(ax1.coords_to_point(X_LEFT_2,0,0), ax1.coords_to_point(X_RIGHT_2,0,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        y_highlight2 = Line(ax1.coords_to_point(0,Y_LEFT_2,0), ax1.coords_to_point(0,Y_RIGHT_2,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        graph_highlight2 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[X_LEFT_2, X_RIGHT_2], stroke_width=5, color=HIGHLIGHT_COLOR)
        a_bar2 = ax1.get_area(graph=gr1, x_range=(X_LEFT_2, X_RIGHT_2), 
                             color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        l_bar2 = Polygon(ax1.coords_to_point(0,Y_LEFT_2,0), 
                        ax1.coords_to_point(0,Y_RIGHT_2,0),
                        ax1.coords_to_point(X_RIGHT_2,Y_RIGHT_2,0), 
                        ax1.coords_to_point(X_LEFT_2,Y_LEFT_2,0),
                        color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        
        self.play(ReplacementTransform(x_highlight1, x_highlight2),
                  ReplacementTransform(y_highlight1, y_highlight2),
                  ReplacementTransform(graph_highlight1, graph_highlight2),
                  ReplacementTransform(a_bar1, a_bar2),
                  ReplacementTransform(l_bar1, l_bar2),
                  X_VALUE.animate.set_value(2.7),
                  rate_func=linear)
        

        X_LEFT_3 = 2.8
        X_RIGHT_3 = 4.2

        Y_LEFT_3 = 2.72
        Y_RIGHT_3 = 2.09

        x_highlight3 = Line(ax1.coords_to_point(X_LEFT_3,0,0), ax1.coords_to_point(X_RIGHT_3,0,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        y_highlight3 = Line(ax1.coords_to_point(0,Y_LEFT_3,0), ax1.coords_to_point(0,Y_RIGHT_3,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        graph_highlight3 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[X_LEFT_3, X_RIGHT_3], stroke_width=5, color=HIGHLIGHT_COLOR)
        a_bar3 = ax1.get_area(graph=gr1, x_range=(X_LEFT_3, X_RIGHT_3), 
                             color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        l_bar3 = Polygon(ax1.coords_to_point(0,Y_LEFT_3,0), 
                        ax1.coords_to_point(0,Y_RIGHT_3,0),
                        ax1.coords_to_point(X_RIGHT_3,Y_RIGHT_3,0), 
                        ax1.coords_to_point(X_LEFT_3,Y_LEFT_3,0),
                        color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        
        self.play(ReplacementTransform(x_highlight2, x_highlight3),
                  ReplacementTransform(y_highlight2, y_highlight3),
                  ReplacementTransform(graph_highlight2, graph_highlight3),
                  ReplacementTransform(a_bar2, a_bar3),
                  ReplacementTransform(l_bar2, l_bar3),
                  X_VALUE.animate.set_value(4.2),
                  rate_func=linear)


        X_LEFT_4 = 2.9
        X_RIGHT_4 = 4.1

        Y_LEFT_4 = 2.68
        Y_RIGHT_4 = 2.12

        x_highlight4 = Line(ax1.coords_to_point(X_LEFT_4,0,0), ax1.coords_to_point(X_RIGHT_4,0,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        y_highlight4 = Line(ax1.coords_to_point(0,Y_LEFT_4,0), ax1.coords_to_point(0,Y_RIGHT_4,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        graph_highlight4 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[X_LEFT_4, X_RIGHT_4], stroke_width=5, color=HIGHLIGHT_COLOR)
        a_bar4 = ax1.get_area(graph=gr1, x_range=(X_LEFT_4, X_RIGHT_4), 
                             color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        l_bar4 = Polygon(ax1.coords_to_point(0,Y_LEFT_4,0), 
                        ax1.coords_to_point(0,Y_RIGHT_4,0),
                        ax1.coords_to_point(X_RIGHT_4,Y_RIGHT_4,0), 
                        ax1.coords_to_point(X_LEFT_4,Y_LEFT_4,0),
                        color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        
        self.play(ReplacementTransform(x_highlight3, x_highlight4),
                  ReplacementTransform(y_highlight3, y_highlight4),
                  ReplacementTransform(graph_highlight3, graph_highlight4),
                  ReplacementTransform(a_bar3, a_bar4),
                  ReplacementTransform(l_bar3, l_bar4),
                  X_VALUE.animate.set_value(2.9),
                  rate_func=linear)
        

        X_LEFT_5 = 3
        X_RIGHT_5 = 4

        Y_LEFT_5 = 2.64
        Y_RIGHT_5 = 2.15
        
        x_highlight5 = Line(ax1.coords_to_point(X_LEFT_5,0,0), ax1.coords_to_point(X_RIGHT_5,0,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        y_highlight5 = Line(ax1.coords_to_point(0,Y_LEFT_5,0), ax1.coords_to_point(0,Y_RIGHT_5,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        graph_highlight5 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[X_LEFT_5, X_RIGHT_5], stroke_width=5, color=HIGHLIGHT_COLOR)
        a_bar5 = ax1.get_area(graph=gr1, x_range=(X_LEFT_5, X_RIGHT_5), 
                             color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        l_bar5 = Polygon(ax1.coords_to_point(0,Y_LEFT_5,0), 
                        ax1.coords_to_point(0,Y_RIGHT_5,0),
                        ax1.coords_to_point(X_RIGHT_5,Y_RIGHT_5,0), 
                        ax1.coords_to_point(X_LEFT_5,Y_LEFT_5,0),
                        color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        
        self.play(ReplacementTransform(x_highlight4, x_highlight5),
                  ReplacementTransform(y_highlight4, y_highlight5),
                  ReplacementTransform(graph_highlight4, graph_highlight5),
                  ReplacementTransform(a_bar4, a_bar5),
                  ReplacementTransform(l_bar4, l_bar5),
                  X_VALUE.animate.set_value(4),
                  rate_func=linear)


        X_LEFT_6 = 3.1
        X_RIGHT_6 = 3.9

        Y_LEFT_6 = 2.59
        Y_RIGHT_6 = 2.19
        
        x_highlight6 = Line(ax1.coords_to_point(X_LEFT_6,0,0), ax1.coords_to_point(X_RIGHT_6,0,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        y_highlight6 = Line(ax1.coords_to_point(0,Y_LEFT_6,0), ax1.coords_to_point(0,Y_RIGHT_6,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        graph_highlight6 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[X_LEFT_6, X_RIGHT_6], stroke_width=5, color=HIGHLIGHT_COLOR)
        a_bar6 = ax1.get_area(graph=gr1, x_range=(X_LEFT_6, X_RIGHT_6), 
                             color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        l_bar6 = Polygon(ax1.coords_to_point(0,Y_LEFT_6,0), 
                        ax1.coords_to_point(0,Y_RIGHT_6,0),
                        ax1.coords_to_point(X_RIGHT_6,Y_RIGHT_6,0), 
                        ax1.coords_to_point(X_LEFT_6,Y_LEFT_6,0),
                        color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        
        self.play(ReplacementTransform(x_highlight5, x_highlight6),
                  ReplacementTransform(y_highlight5, y_highlight6),
                  ReplacementTransform(graph_highlight5, graph_highlight6),
                  ReplacementTransform(a_bar5, a_bar6),
                  ReplacementTransform(l_bar5, l_bar6),
                  X_VALUE.animate.set_value(3.1),
                  rate_func=linear)

        
        X_LEFT_7 = 3.2
        X_RIGHT_7 = 3.8

        Y_LEFT_7 = 2.54
        Y_RIGHT_7 = 2.23

        x_highlight7 = Line(ax1.coords_to_point(X_LEFT_7,0,0), ax1.coords_to_point(X_RIGHT_7,0,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        y_highlight7 = Line(ax1.coords_to_point(0,Y_LEFT_7,0), ax1.coords_to_point(0,Y_RIGHT_7,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        graph_highlight7 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[X_LEFT_7, X_RIGHT_7], stroke_width=5, color=HIGHLIGHT_COLOR)
        a_bar7 = ax1.get_area(graph=gr1, x_range=(X_LEFT_7, X_RIGHT_7), 
                             color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        l_bar7 = Polygon(ax1.coords_to_point(0,Y_LEFT_7,0), 
                        ax1.coords_to_point(0,Y_RIGHT_7,0),
                        ax1.coords_to_point(X_RIGHT_7,Y_RIGHT_7,0), 
                        ax1.coords_to_point(X_LEFT_7,Y_LEFT_7,0),
                        color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        
        self.play(ReplacementTransform(x_highlight6, x_highlight7),
                  ReplacementTransform(y_highlight6, y_highlight7),
                  ReplacementTransform(graph_highlight6, graph_highlight7),
                  ReplacementTransform(a_bar6, a_bar7),
                  ReplacementTransform(l_bar6, l_bar7),
                  X_VALUE.animate.set_value(3.8),
                  rate_func=linear)
        

        X_LEFT_8 = 3.3
        X_RIGHT_8 = 3.7

        Y_LEFT_8 = 2.49
        Y_RIGHT_8 = 2.28

        x_highlight8 = Line(ax1.coords_to_point(X_LEFT_8,0,0), ax1.coords_to_point(X_RIGHT_8,0,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        y_highlight8 = Line(ax1.coords_to_point(0,Y_LEFT_8,0), ax1.coords_to_point(0,Y_RIGHT_8,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        graph_highlight8 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[X_LEFT_8, X_RIGHT_8], stroke_width=5, color=HIGHLIGHT_COLOR)
        a_bar8 = ax1.get_area(graph=gr1, x_range=(X_LEFT_8, X_RIGHT_8), 
                             color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        l_bar8 = Polygon(ax1.coords_to_point(0,Y_LEFT_8,0), 
                        ax1.coords_to_point(0,Y_RIGHT_8,0),
                        ax1.coords_to_point(X_RIGHT_8,Y_RIGHT_8,0), 
                        ax1.coords_to_point(X_LEFT_8,Y_LEFT_8,0),
                        color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        
        self.play(ReplacementTransform(x_highlight7, x_highlight8),
                  ReplacementTransform(y_highlight7, y_highlight8),
                  ReplacementTransform(graph_highlight7, graph_highlight8),
                  ReplacementTransform(a_bar7, a_bar8),
                  ReplacementTransform(l_bar7, l_bar8),
                  X_VALUE.animate.set_value(3.3),
                  rate_func=linear)
        
        
        X_LEFT_9 = 3.4
        X_RIGHT_9 = 3.6

        Y_LEFT_9 = 2.44
        Y_RIGHT_9 = 2.33

        x_highlight9 = Line(ax1.coords_to_point(X_LEFT_9,0,0), ax1.coords_to_point(X_RIGHT_9,0,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        y_highlight9 = Line(ax1.coords_to_point(0,Y_LEFT_9,0), ax1.coords_to_point(0,Y_RIGHT_9,0), stroke_width=4, color=HIGHLIGHT_COLOR)
        graph_highlight9 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[X_LEFT_9, X_RIGHT_9], stroke_width=5, color=HIGHLIGHT_COLOR)
        a_bar9 = ax1.get_area(graph=gr1, x_range=(X_LEFT_9, X_RIGHT_9), 
                             color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        l_bar9 = Polygon(ax1.coords_to_point(0,Y_LEFT_9,0), 
                        ax1.coords_to_point(0,Y_RIGHT_9,0),
                        ax1.coords_to_point(X_RIGHT_9,Y_RIGHT_9,0), 
                        ax1.coords_to_point(X_LEFT_9,Y_LEFT_9,0),
                        color=YELLOW, stroke_width=0).set_opacity(0.1).set_z_index(-5)
        
        self.play(ReplacementTransform(x_highlight8, x_highlight9),
                  ReplacementTransform(y_highlight8, y_highlight9),
                  ReplacementTransform(graph_highlight8, graph_highlight9),
                  ReplacementTransform(a_bar8, a_bar9),
                  ReplacementTransform(l_bar8, l_bar9),
                  X_VALUE.animate.set_value(3.6),
                  rate_func=linear)


        self.play(FadeIn(l_label, l_tick), 
                  X_VALUE.animate.set_value(3.4),
                  rate_func=linear)
        self.play(X_VALUE.animate.set_value(3.6),
                  rate_func=linear)
        self.play(X_VALUE.animate.set_value(3.4),
                  rate_func=linear)
        self.play(X_VALUE.animate.set_value(3.6),
                  rate_func=linear)
        self.play(X_VALUE.animate.set_value(3.4),
                  rate_func=linear)
        self.play(X_VALUE.animate.set_value(3.6),
                  rate_func=linear)
        self.play(X_VALUE.animate.set_value(3.4),
                  rate_func=linear)
        self.play(X_VALUE.animate.set_value(3.6),
                  rate_func=linear)
        self.play(X_VALUE.animate.set_value(3.4),
                  rate_func=linear)
        self.play(X_VALUE.animate.set_value(3.6),
                  rate_func=linear)
        self.play(X_VALUE.animate.set_value(3.4),
                  rate_func=linear)
        self.play(X_VALUE.animate.set_value(3.6),
                  rate_func=linear)


        # O nome dessa aproximação é "limite"
        t2 = Tex('Limite').shift(UP*4.5)
        self.play(t2.animate.shift(DOWN*1.5), run_time=1.5)
        self.wait(2)


        # lim de f(x) para x -> a = L
        t3 = MathTex(r'\lim_{x\to a} f(x) = L ').shift(UP*2)
        VGroup(t3[0][3], t3[0][6:10]).set_color(BLUE)
        t3[0][5].set_color(A_COLOR)
        t3[0][11].set_color(L_COLOR)
        self.play(t2.animate.shift(UP*1.5))
        self.play(LaggedStart(FadeIn(t3[0][0:3]), FadeIn(t3[0][6:10]), lag_ratio=0.5))
        self.wait(2)
        self.play(LaggedStart(FadeIn(t3[0][3]), FadeIn(t3[0][4]), FadeIn(t3[0][5]), lag_ratio=0.1))
        self.wait(2)
        self.play(LaggedStart(FadeIn(t3[0][10]), TransformFromCopy(l_label, t3[0][11]), lag_ratio=0.1))
        self.wait(2)




# Exemplo de limite na função 2x - 1
class vid4(MovingCameraScene):
    def construct(self):

        self.camera.frame.scale(1.2)

        ax1 = Axes(x_range=[-1.5, 4.9], x_length=6.4,
                   y_range=[-1.5, 6.9], y_length=8.4,
                   axis_config={"include_ticks" : True, "include_numbers" : True}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.1+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*4.1+RIGHT*0.6)

        gr1 = ax1.plot(lambda x: 2*x - 1, x_range=[-0.2, 4], stroke_width=5, color=BLUE)
        gr1_label = MathTex('y = 2x - 1', color=BLUE).next_to(gr1, RIGHT).shift(UP*4+RIGHT*0.3)
        

        # Criando o gráfico
        self.play(LaggedStart(FadeIn(ax1), FadeIn(ax1_x_label, ax1_y_label), Create(gr1), FadeIn(gr1_label), lag_ratio=0.2))
        self.wait(2)


        A_COLOR = YELLOW
        L_COLOR = YELLOW

        a_tick = Line(ORIGIN, UP*0.2, stroke_width=2, color=A_COLOR).move_to(ax1.coords_to_point(3,0,0)).set_z_index(2)
        a_label = MathTex('3', color=A_COLOR).scale(0.7).next_to(a_tick, DOWN, buff=0.15).set_z_index(2)
        a_line = DashedLine(a_tick, ax1.coords_to_point(3,5,0), color=A_COLOR).set_opacity(0.5).set_z_index(-1).set_z_index(2)

        a_dot = Dot().set_color(A_COLOR).move_to(ax1.coords_to_point(3,5,0))
        a_dot_black = a_dot.copy().set_color(BLACK).scale(0.6).set_z_index(4)

        l_tick = a_tick.copy().rotate(90*DEGREES).set_color(L_COLOR).move_to(ax1.coords_to_point(0,5,0)).set_z_index(2)
        l_label = MathTex('5', color=L_COLOR).scale(0.7).next_to(l_tick, LEFT, buff=0.15).set_z_index(2)
        l_line = DashedLine(ax1.coords_to_point(3,5,0), l_tick, color=A_COLOR).set_opacity(0.5).set_z_index(-1).set_z_index(2)

        X_VALUE = ValueTracker(3.5)
        DOT_REF = always_redraw(lambda: Dot(gr1.get_point_from_function(t = X_VALUE.get_value()), color=BLUE).set_z_index(5))
        DOT_REF_hightlight1 = always_redraw(lambda: ax1.plot(lambda x: 2*x - 1, x_range=[3, X_VALUE.get_value()], stroke_width=5, color=YELLOW).set_z_index(3))
        DOT_REF_hightlight2 = always_redraw(lambda: ax1.plot(lambda x: 2*x - 1, x_range=[X_VALUE.get_value(), 3], stroke_width=5, color=YELLOW).set_z_index(3))

        self.add(DOT_REF, DOT_REF_hightlight1)

        x_tick = always_redraw(lambda: a_tick.copy().set_color(BLUE).move_to(ax1.coords_to_point(X_VALUE.get_value(),0,0)).set_z_index(2))
        x_line = always_redraw(lambda: DashedLine(DOT_REF, ax1.coords_to_point(X_VALUE.get_value(),-0.7,0), color=BLUE).set_opacity(0.5).set_z_index(-3))
        x_label = always_redraw(lambda: MathTex('x', color=BLUE).next_to(x_line, DOWN, buff=0.15).set_z_index(2))

        fx_tick = always_redraw(lambda: a_tick.copy().rotate(90*DEGREES).set_color(BLUE).move_to(ax1.get_y_axis().number_to_point(DOT_REF.get_y() + 2.9)).set_z_index(2))
        fx_line = always_redraw(lambda: DashedLine(DOT_REF, Dot().move_to(fx_tick).shift(LEFT*0.8), color=BLUE).set_opacity(0.5).set_z_index(-3))
        fx_label = always_redraw(lambda: MathTex('f(x)', color=BLUE).next_to(fx_line, LEFT, buff=0.15).set_z_index(2))

        x_highlight = always_redraw(lambda: Line(ax1.coords_to_point(X_VALUE.get_value(),0,0), ax1.coords_to_point(3,0,0), stroke_width=4, color=A_COLOR))
        fx_highlight = always_redraw(lambda: Line(fx_tick.get_center(), ax1.coords_to_point(0,5,0), stroke_width=4, color=A_COLOR))

        x_bar = always_redraw(lambda: ax1.get_area(graph=gr1, x_range=(3, X_VALUE.get_value()), 
                             color=YELLOW, stroke_width=0).set_opacity(0.15).set_z_index(-5))
        fx_bar = always_redraw(lambda: Polygon(ax1.coords_to_point(0,5,0), 
                        fx_tick.get_center(), 
                        ax1.coords_to_point(X_VALUE.get_value(),2*X_VALUE.get_value() - 1,0),
                        ax1.coords_to_point(3,5,0),
                        color=YELLOW, stroke_width=0).set_opacity(0.15).set_z_index(-5))
        
 

        # Quando x -> 3, f(x) -> 5
        self.add(x_tick, x_line, x_label, x_highlight, x_bar,
                 a_label, a_tick, a_line, a_dot, a_dot_black)
        self.play(X_VALUE.animate.set_value(3.02), rate_func=linear, run_time=2)
        X_VALUE.set_value(2.5)
        self.remove(DOT_REF_hightlight1).add(DOT_REF_hightlight2)
        self.play(X_VALUE.animate.set_value(2.98), rate_func=linear, run_time=2)
        
        self.add(fx_tick, fx_line, fx_label, fx_highlight, fx_bar)
        X_VALUE.set_value(3.5)
        self.remove(DOT_REF_hightlight2).add(DOT_REF_hightlight1)
        self.play(X_VALUE.animate.set_value(3.02), FadeIn(l_label, l_tick, l_line), rate_func=linear, run_time=2)
        X_VALUE.set_value(2.5)
        self.remove(DOT_REF_hightlight1).add(DOT_REF_hightlight2)
        self.play(X_VALUE.animate.set_value(2.98), rate_func=linear, run_time=2.0001)


        # lim de 2x - 1 para x -> 3 = 5
        t3 = MathTex(r'\lim_{x \to 3} 2x - 1 = 5 ').shift(RIGHT*5+UP*3.5)
        VGroup(t3[0][3], t3[0][6:10]).set_color(BLUE)
        t3[0][5].set_color(A_COLOR)
        t3[0][11].set_color(L_COLOR)
        self.play(LaggedStart(FadeOut(gr1_label[0][0:2]),
                              ReplacementTransform(gr1_label[0][2:], t3[0][6:10]),
                              FadeIn(t3[0][0:3]),
                              lag_ratio=0.2))
        self.wait(2)
        self.play(LaggedStart(FadeIn(t3[0][3]), FadeIn(t3[0][4]), FadeIn(t3[0][5]), lag_ratio=0.1))
        self.wait(2)
        self.play(LaggedStart(FadeIn(t3[0][10]), TransformFromCopy(l_label, t3[0][11]), lag_ratio=0.1))
        self.wait(2)

        

# O limite é para onde a função vai à medida que ‘x’ se aproxima de ‘a’
class vid5(MovingCameraScene):
    def construct(self):

        # Retomando elementos
        ax1 = Axes(x_range=[-1, 8], x_length=9,
                   y_range=[-1, 5], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        gr1 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[0.4, 8], stroke_width=5, color=BLUE)
        gr1_label = MathTex('y = f(x)', color=BLUE).next_to(gr1, RIGHT).shift(UP*1.8+LEFT*0.1).set_z_index(7)
        

        A_COLOR = YELLOW
        L_COLOR = YELLOW

        dot_a_l = Dot(ax1.coords_to_point(3.5,2.38,0), color=A_COLOR).set_z_index(3)
        dot_a_l_black = dot_a_l.copy().set_color(BLACK).scale(0.6).set_z_index(4)

        a_tick = Line(ORIGIN, UP*0.2, color=A_COLOR).move_to(ax1.coords_to_point(3.5,0,0)).set_z_index(2)
        a_label = MathTex('a', color=A_COLOR).next_to(a_tick, DOWN, buff=0.2).set_z_index(2)
        a_line = DashedLine(a_tick, ax1.coords_to_point(3.5,2.38,0), color=A_COLOR).set_opacity(0.5).set_z_index(-1).set_z_index(2)
        
        l_tick = a_tick.copy().rotate(90*DEGREES).set_color(L_COLOR).move_to(ax1.coords_to_point(0,2.38,0)).set_z_index(2)
        l_label = MathTex('L', color=L_COLOR).next_to(l_tick, LEFT, buff=0.2).set_z_index(2)
        l_line = DashedLine(ax1.coords_to_point(3.5,2.38,0), l_tick, color=A_COLOR).set_opacity(0.5).set_z_index(-1).set_z_index(2)


        X_VALUE = ValueTracker(4.5)
        DOT_REF = always_redraw(lambda: Dot(gr1.get_point_from_function(t = X_VALUE.get_value()), color=BLUE).set_z_index(5))
        self.add(DOT_REF)

        x_tick = always_redraw(lambda: a_tick.copy().set_color(BLUE).move_to(ax1.coords_to_point(X_VALUE.get_value(),0,0)).set_z_index(2))
        x_line = always_redraw(lambda: DashedLine(DOT_REF, ax1.coords_to_point(X_VALUE.get_value(),-0.7,0), color=BLUE).set_opacity(0.5).set_z_index(-3))
        x_label = always_redraw(lambda: MathTex('x', color=BLUE).next_to(x_line, DOWN, buff=0.15).set_z_index(2))

        fx_tick = always_redraw(lambda: a_tick.copy().rotate(90*DEGREES).set_color(BLUE).move_to(ax1.get_y_axis().number_to_point(DOT_REF.get_y() + 2.2)).set_z_index(2))
        fx_line = always_redraw(lambda: DashedLine(DOT_REF, Dot().move_to(fx_tick).shift(LEFT*0.8), color=BLUE).set_opacity(0.5).set_z_index(-3))
        fx_label = always_redraw(lambda: MathTex('f(x)', color=BLUE).next_to(fx_line, LEFT, buff=0.15).set_z_index(2))

        x_bar = always_redraw(lambda: ax1.get_area(graph=gr1, x_range=(3.5, X_VALUE.get_value()), 
                             color=YELLOW, stroke_width=0).set_opacity(0.15).set_z_index(-5))
        fx_bar = always_redraw(lambda: Polygon(ax1.coords_to_point(0,2.38,0), 
                        fx_tick.get_center(), 
                        DOT_REF.get_center(),
                        ax1.coords_to_point(3.5,2.38,0),
                        color=YELLOW, stroke_width=0).set_opacity(0.15).set_z_index(-5))

        x_highlight = always_redraw(lambda: Line(ax1.coords_to_point(3.5,0,0), ax1.coords_to_point(X_VALUE.get_value(),0,0), color=YELLOW))
        y_highlight = always_redraw(lambda: Line(ax1.coords_to_point(0,2.38,0), fx_tick.get_center(), color=YELLOW))
        
        graph_highlight_r = always_redraw(lambda: ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[3.5, X_VALUE.get_value()], stroke_width=5, color=YELLOW))
        graph_highlight_l = always_redraw(lambda: ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[X_VALUE.get_value(), 3.5], stroke_width=5, color=YELLOW))


        t3 = MathTex(r'\lim_{x\to a} f(x) = L ').shift(UP*2).set_z_index(11)
        VGroup(t3[0][3], t3[0][6:10]).set_color(BLUE)
        t3[0][5].set_color(A_COLOR)
        t3[0][11].set_color(L_COLOR)

        self.add(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label,
                 a_tick, a_label, a_line, dot_a_l, dot_a_l_black, l_label, l_tick, l_line,
                 t3,
                 x_tick, x_line, x_label, x_bar,
                 fx_tick, fx_line, fx_label, fx_bar,
                 x_highlight, y_highlight, graph_highlight_r)
        self.wait(2)

        self.play(X_VALUE.animate.set_value(3.55), rate_func=linear, run_time=1.7)

        self.remove(graph_highlight_r).add(graph_highlight_l)
        X_VALUE.set_value(2.5)
        self.play(X_VALUE.animate.set_value(3.45), rate_func=linear, run_time=1.7)

        self.remove(graph_highlight_l).add(graph_highlight_r)
        X_VALUE.set_value(4.5)
        self.play(X_VALUE.animate.set_value(3.55), rate_func=linear, run_time=1.7)

        self.remove(graph_highlight_r).add(graph_highlight_l)
        X_VALUE.set_value(2.5)
        self.play(X_VALUE.animate.set_value(3.45), rate_func=linear, run_time=1.7)
        self.wait(2)



         # Diferença entre 'lim f(x) para x -> a' e 'f(a)'
        self.remove(DOT_REF,
                    x_tick, x_line, x_label, x_bar,
                    fx_tick, fx_line, fx_label, fx_bar)
        self.wait(2)
        
        dot1 = dot_a_l.copy().scale(1).set_color(BLUE).set_z_index(4)
        dot1_x_line = always_redraw(lambda: DashedLine(dot1, a_tick.get_center(), color=BLUE).set_opacity(0.5).set_z_index(-1).set_z_index(2))
        dot1_y_line = always_redraw(lambda: DashedLine(dot1, Dot().scale(0).move_to(dot1.get_center()).shift(LEFT*4.2), color=BLUE).set_opacity(0.5).set_z_index(-1).set_z_index(2))
        
        fa_tick = always_redraw(lambda: l_tick.copy().set_color(BLUE).move_to(Dot().move_to(dot1_y_line.get_left()).shift(RIGHT*0.7)))
        
        fa_label = always_redraw(lambda: MathTex(r'f(a)', color=BLUE).next_to(dot1_y_line, LEFT, buff=0.15).set_z_index(11))
        fa_label_copy1 = always_redraw(lambda: MathTex(r'f(a)', color=BLUE).next_to(dot1_y_line, LEFT, buff=0.15).set_z_index(11))
        

        fa_label_aux = always_redraw(lambda: fa_label[0][2].copy().set_color(YELLOW))
        fa_label_aux_copy = always_redraw(lambda: fa_label_copy1[0][2].copy().set_color(YELLOW))
        

        self.play(FadeIn(VGroup(dot1, dot1_x_line, dot1_y_line, fa_tick, fa_label, fa_label_aux), shift=UP))
        self.play(LaggedStart(X_VALUE.animate.set_value(3.5), 
                              ReplacementTransform(fx_label, fa_label),
                              FadeIn(fa_label_aux),
                              FadeOut(x_tick, x_line, x_label, x_bar),
                              lag_ratio=0.1))
        self.remove(DOT_REF, fa_label, fa_label_aux,
                    fx_tick, fx_line, fx_label, fx_bar)
        self.add(dot1, dot1_x_line, dot1_y_line, fa_tick, fa_label_copy1, fa_label_aux_copy)
        self.wait(2)
        self.play(dot1.animate.shift(UP*1.25), run_time=1.5)
        self.play(dot1.animate.shift(DOWN*2), run_time=1.5)
        self.wait(2)
        self.play(dot1.animate.shift(UP*0.75), run_time=2)
        self.wait(2)



            # Destaque no gráfico contínuo
        AUX_VALUE = ValueTracker(-1)
        
        gr1_hightlight = always_redraw(lambda: ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[AUX_VALUE.get_value(), AUX_VALUE.get_value()+1], stroke_width=5, color=YELLOW).set_z_index(5))
        
        gr1_hightlight_black_aux1 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[-1, 0.4], stroke_width=6, color=BLACK).set_z_index(6)
        gr1_hightlight_black_aux2 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[8, 10], stroke_width=6, color=BLACK).set_z_index(6)
        
        gr1_hightlight_axis_aux1 = Line(ax1.coords_to_point(0,-1,0), ax1.coords_to_point(0,1,0), stroke_width=2, color=GRAY).set_z_index(7)
        gr1_hightlight_axis_aux2 = Line(ax1.coords_to_point(-1,0,0), ax1.coords_to_point(1,0,0), stroke_width=2, color=GRAY).set_z_index(7)

        self.add(gr1_hightlight, 
                 gr1_hightlight_black_aux1, gr1_hightlight_black_aux2, 
                 gr1_hightlight_axis_aux1, gr1_hightlight_axis_aux2)
        self.remove(dot_a_l, dot_a_l_black)
        self.play(LaggedStart(dot1.animate.scale(0), AUX_VALUE.animate.set_value(9), lag_ratio=0.1), run_time=4)
        self.wait(2)
        


            # Destacando o 'lim = L' e o 'f(a) = L'
        fa_label_copy = MathTex(r'f(a)', color=BLUE).move_to(fa_label_copy1).set_z_index(11)
        fa_label_copy[0][2].set_color(YELLOW)
        self.remove(fa_label_copy1, fa_label_aux_copy).add(fa_label_copy)
        self.wait(2)


        black_sq1 = Square(color=BLACK).scale(10).set_opacity(1).set_z_index(10)


        fa = MathTex('f(a) = L').next_to(t3, LEFT, buff=4).set_z_index(11)
        fa[0][0:2].set_color(BLUE)
        fa[0][3].set_color(BLUE)
        fa[0][2].set_color(YELLOW)
        fa[0][5].set_color(YELLOW)

        self.remove(y_highlight)
        self.play(LaggedStart(FadeOut(ax1, ax1_y_label, ax1_x_label, 
                              gr1, gr1_label, 
                              gr1_hightlight_axis_aux1, gr1_hightlight_axis_aux2,
                              l_tick, l_line, 
                              a_tick, a_line,a_label, 
                              dot1_x_line, dot1_y_line, 
                              fa_tick),
                          fa_label_copy.animate.move_to(fa[0][0:4]),
                          fa_label_copy.animate.move_to(fa[0][0:4]),
                          self.camera.frame.animate.move_to(t3.get_center()).shift(LEFT*3.25+DOWN*2),
                          l_label.animate.move_to(fa[0][5]),
                          FadeIn(fa[0][4])))
        self.remove(fa_label_copy, l_label).add(fa[0][0:4], fa[0][5])
        self.wait(2)



                # Explicação de 'f(a) = L'
        fa_t1 = Tex('$x$',' é ','igual',' ao ','$a$').next_to(fa, DOWN, buff=1).set_z_index(11)
        fa_t1[0].set_color(BLUE)
        fa_t1[4].set_color(YELLOW)

        fa_t2 = MathTex(r'\Rightarrow').rotate(-90*DEGREES).next_to(fa_t1, DOWN, buff=0.5).set_z_index(11)

        fa_t3 = Tex('$f(x)$',' é ','igual',' a ','$L$').next_to(fa_t2, DOWN, buff=0.5).set_z_index(11)
        fa_t3[0].set_color(BLUE)
        fa_t3[4].set_color(YELLOW)

        fa_brace = Brace(fa_t1, UP, color=GRAY).set_z_index(11)

        self.play(FadeIn(fa_brace))
        self.play(LaggedStart(FadeIn(fa_t1[0]),
                              FadeIn(fa_t1[1]), 
                              FadeIn(fa_t1[2]), 
                              FadeIn(fa_t1[3]),
                              FadeIn(fa_t1[4]),
                              lag_ratio=0.3))
        self.wait(2)
        self.play(LaggedStart(FadeIn(fa_t2),
                              FadeIn(fa_t3[0]),
                              FadeIn(fa_t3[1]), 
                              FadeIn(fa_t3[2]), 
                              FadeIn(fa_t3[3]),
                              FadeIn(fa_t3[4]),
                              lag_ratio=0.3))
        self.wait(2)



                # Explicação de 'lim = L'
        lim_t1 = Tex('$x$',' chega ','perto',' de ','$a$').next_to(t3, DOWN, buff=0.9).set_z_index(11)
        lim_t1[0].set_color(BLUE)
        lim_t1[4].set_color(YELLOW)

        lim_t2 = MathTex(r'\Rightarrow').rotate(-90*DEGREES).next_to(lim_t1, DOWN, buff=0.5).set_z_index(11)

        lim_t3 = Tex('$f(x)$',' chega ','perto',' de ','$L$').next_to(lim_t2, DOWN, buff=0.5).set_z_index(11)
        lim_t3[0].set_color(BLUE)
        lim_t3[4].set_color(YELLOW)


        lim_brace = Brace(lim_t1, UP, color=GRAY).set_z_index(11)


        self.play(FadeIn(lim_brace))
        self.wait()
        self.play(LaggedStart(FadeIn(lim_t1[0]),
                              FadeIn(lim_t1[1]), 
                              FadeIn(lim_t1[2]), 
                              FadeIn(lim_t1[3]),
                              FadeIn(lim_t1[4]),
                              lag_ratio=0.3))
        self.wait(2)

        self.play(LaggedStart(FadeIn(lim_t2),
                              FadeIn(lim_t3[0]),
                              FadeIn(lim_t3[1]), 
                              FadeIn(lim_t3[2]), 
                              FadeIn(lim_t3[3]),
                              FadeIn(lim_t3[4]),
                              lag_ratio=0.4))
        self.wait(2)



                # Para o limite, não importa 'f(a)', mas apenas o entorno
        red_line1 = Line(UP*0.5, DOWN*0.6, color=RED, stroke_width=4).scale(2).rotate(70*DEGREES).move_to(fa)
        red_line2 = red_line1.copy().rotate(40*DEGREES).move_to(red_line1).reverse_points()
        self.play(LaggedStart(Create(red_line2), 
                              Create(red_line1), 
                              lag_ratio=0.4))
        self.wait(2)



        # Transição para a próxima cena
        t5 = MathTex(r'f(x) = \frac{1}{x}', color=BLUE).shift(UP*7+RIGHT*10)
        self.add(t5)
        self.play(self.camera.frame.animate.move_to(t5), run_time=3)
        self.wait(2)



# Limite de 1/x para x -> 0
class vid6(MovingCameraScene):
    def construct(self):

        t1 = MathTex(r'f(x) = \frac{1}{x}', color=BLUE)
        VGroup(t1[0][2], t1[0][7]).set_color(BLUE)

        t2= MathTex(r'f(0) = \frac{1}{0}', color=BLUE)
        VGroup(t2[0][2], t2[0][7]).set_color(RED)
        t2[0][7].set_opacity(0)
        t2[0][2].shift(LEFT*0.015+DOWN*0.015)
        t2[0][7].shift(LEFT*0.015+DOWN*0.01)

        arc1 = Arc(angle=PI/2).rotate(PI/2).move_to(t2[0][7], aligned_edge=UR).shift(DOWN*0.2+LEFT*0.08).reverse_points()
        arc2 = arc1.copy().rotate(-PI/2).next_to(arc1, RIGHT, buff=0)

        t3 = MathTex(r'\lim_{x \to 0^{+}}').move_to(t1)
        t3[0][3].set_color(BLUE)
        t3[0][5].set_color(RED)
        t3[0][0:3].shift(DOWN*0.1)
        t3[0][3:6].shift(RIGHT*0.15)

        self.add(t1)
        self.wait(2)
        self.play(FadeOut(t1[0][2], t1[0][7]),
                  FadeIn(t2[0][2], shift=UP),
                  AnimationGroup(t2[0][7].animate.set_opacity(1), MoveAlongPath(t2[0][7], path=arc1)))
        self.wait(2)
        self.play(FadeIn(t1[0][7]),
                  FadeOut(t2[0][2]),
                  AnimationGroup(t2[0][7].animate.set_opacity(0), MoveAlongPath(t2[0][7], path=arc2)),
                  LaggedStart(FadeOut(t1[0][0:2], t1[0][3:5]),
                              FadeIn(t3[0][0]),
                              FadeIn(t3[0][1]),
                              FadeIn(t3[0][2]),
                              lag_ratio=0.1))
        self.wait()
        self.play(LaggedStart(t3[0][0:3].animate.shift(UP*0.1),
                              FadeIn(t3[0][3]), 
                              FadeIn(t3[0][4]), 
                              FadeIn(t3[0][5]), 
                              lag_ratio=0.1))
        self.wait(2)



        # Construindo o gráfico y = 1/x
        ax1 = Axes(x_range=[-4.9, 5], x_length=9.9,
                   y_range=[-4.9, 5], y_length=9.9,
                   axis_config={"include_ticks" : True,
                                "include_numbers" : True}).set_color(GRAY).shift(DOWN*4.5+LEFT*2.5)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.12+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*5+RIGHT*0.75)
        ax1_0_label = MathTex('0').set_color(RED).scale(0.8).next_to(ax1.coords_to_point(0,0,0), DOWN, buff=0.25).shift(LEFT*0.3)

        ax1_black_sq_aux1 = Square(color=BLACK).scale(3).set_opacity(1).next_to(ax1.coords_to_point(0,0,0), LEFT, buff=0.8).set_z_index(4)
        ax1_black_sq_aux2 = Square(color=BLACK).scale(3).set_opacity(1).next_to(ax1.coords_to_point(0,0,0), DOWN, buff=0.8).set_z_index(4)
        self.add(ax1_black_sq_aux1, ax1_black_sq_aux2)


        gr1 = ax1.plot(lambda x: 1/x, x_range=[0.25, 4], stroke_width=5, color=BLUE)
        

        self.play(self.camera.frame.animate.shift(DOWN*2+LEFT*0),
                  LaggedStart(FadeIn(ax1, ax1_0_label), 
                              FadeIn(ax1_x_label, ax1_y_label), 
                              lag_ratio=0.2),
                  run_time=2)
        self.wait(2)



        X_VALUE = ValueTracker(4)

        DOT_REF = always_redraw(lambda: Dot(color=BLUE).move_to(gr1.get_point_from_function(t=X_VALUE.get_value())).set_z_index(5))
        DOT_REF_path = always_redraw(lambda: ax1.plot(lambda x: 1/x, x_range=[X_VALUE.get_value(), 4], stroke_width=5, color=BLUE).set_z_index(5))

        x_tick = always_redraw(lambda: Line(ORIGIN, UP*0.2).set_color(BLUE).move_to(ax1.coords_to_point(X_VALUE.get_value(),0,0)).set_z_index(5))
        x_line = always_redraw(lambda: DashedLine(DOT_REF, ax1.coords_to_point(X_VALUE.get_value(),-0.7,0), color=BLUE).set_opacity(0.5).set_z_index(5))
        x_label1 = always_redraw(lambda: MathTex(f'{X_VALUE.get_value():.0f}', color=BLUE).scale(0.8).next_to(x_line, DOWN, buff=0.15).set_z_index(5))

        fx_tick = always_redraw(lambda: x_tick.copy().rotate(90*DEGREES).move_to(ax1.get_y_axis().number_to_point(1/X_VALUE.get_value())).set_z_index(5))
        fx_line = always_redraw(lambda: DashedLine(DOT_REF, Dot().move_to(fx_tick).shift(LEFT*0.8), color=BLUE).set_opacity(0.5).set_z_index(5))
        fx_label1 = always_redraw(lambda: MathTex(r'\frac{1}{',f'{X_VALUE.get_value():.0f}',r'}=',f'{1/X_VALUE.get_value():.2f}', color=BLUE).scale(0.8).next_to(fx_line, LEFT, buff=0.15).set_z_index(5))


        self.add(DOT_REF, DOT_REF_path,
                 x_tick, x_line, x_label1,
                 fx_tick, fx_line, fx_label1)
        self.wait(3)
        self.play(X_VALUE.animate.set_value(3), run_time=2)
        self.wait(2)
        self.play(X_VALUE.animate.set_value(2), run_time=2)

        fx_label2 = always_redraw(lambda: MathTex(r'\frac{1}{',f'{X_VALUE.get_value():.0f}',r'}=',f'{1/X_VALUE.get_value():.1f}', color=BLUE).scale(0.8).set_z_index(5).next_to(fx_line, LEFT, buff=0.15))
        self.remove(fx_label1)
        self.add(fx_label2)

        self.wait(2)
        self.play(X_VALUE.animate.set_value(1), run_time=2)
        self.wait(2)

        x_label2 = always_redraw(lambda: MathTex(f'{X_VALUE.get_value():.1f}', color=BLUE).scale(0.8).next_to(x_line, DOWN, buff=0.15).set_z_index(4))
        fx_label3 = always_redraw(lambda: MathTex(r'\frac{1}{',f'{X_VALUE.get_value():.1f}',r'}=',f'{1/X_VALUE.get_value():.1f}', color=BLUE).scale(0.8).set_z_index(5).next_to(fx_line, LEFT, buff=0.15))
        self.remove(x_label1, fx_label2)
        self.add(x_label2, fx_label3)

        self.play(X_VALUE.animate.set_value(0.5), run_time=2)
        self.wait(2)

        x_label3 = always_redraw(lambda: MathTex(f'{X_VALUE.get_value():.2f}', color=BLUE).scale(0.8).next_to(x_line, DOWN, buff=0.15).set_z_index(4))
        fx_label4 = always_redraw(lambda: MathTex(r'\frac{1}{',f'{X_VALUE.get_value():.2f}',r'}=',f'{1/X_VALUE.get_value():.1f}', color=BLUE).scale(0.8).set_z_index(5).next_to(fx_line, LEFT, buff=0.15))
        self.remove(x_label2, fx_label3)
        self.add(x_label3, fx_label4)

        self.play(X_VALUE.animate.set_value(0.25), run_time=2)
        self.wait(2)

        self.remove(x_label3, fx_label4)
        self.add(x_label2, fx_label3)


        ax2 = Axes(x_range=[-10.9, 11], x_length=21.9,
                   y_range=[-10.9, 11], y_length=21.9,
                   axis_config={"include_ticks" : True,
                                "include_numbers" : True}).set_color(GRAY).move_to(ax1).set_z_index(3)
        ax2_y_label = MathTex('y').set_color(GRAY).next_to(ax2.get_y_axis(), LEFT).shift(UP*11+RIGHT*0.8)
        ax2_black_sq_aux1 = Square(color=BLACK).scale(0.7).set_opacity(1).rotate(25*DEGREES).move_to(ax1.coords_to_point(-0.757,5,0)).set_z_index(2)
        
        self.camera.frame.save_state()
        self.play(FadeIn(ax2_black_sq_aux1, ax2.get_y_axis(), ax2_y_label),
                  X_VALUE.animate.set_value(0.1),
                  self.camera.frame.animate.scale(1.6).shift(UP*2.6),
                  run_time=2)
        self.wait(2)



        # O resultado do limite é + infinito
        t4 = MathTex(r'= + \infty').next_to(t1, RIGHT, buff=0.25)
        t4[0][1:].set_color(YELLOW)

        self.play(self.camera.frame.animate.scale(0.625).move_to(VGroup(t3, t4)), run_time=2)
        self.wait(2)
        self.play(LaggedStart(FadeIn(t4[0][0]),
                              FadeIn(t4[0][1:]),
                              lag_ratio=0.1))
        self.wait(2)



        # A aproximação foi feita pela direita
        self.play(FadeOut(ax2_black_sq_aux1, 
                          ax2.get_y_axis(), 
                          ax2_y_label,
                          DOT_REF, DOT_REF_path,
                          x_tick, x_line, x_label2,
                          fx_tick, fx_line, fx_label3),
                  FadeIn(gr1),
                  self.camera.frame.animate.restore(),
                  run_time=2)
        self.wait(2)

        X_VALUE.set_value(4)
        self.add(DOT_REF, 
                 x_tick, x_line, x_label3, 
                 fx_tick, fx_line, fx_label4)
        self.wait(2)

        self.play(X_VALUE.animate.set_value(0.25), run_time=4)
        self.wait(2)



        # Fazendo a aproximação pela esquerda
        x_tick_2 = always_redraw(lambda: Line(ORIGIN, UP*0.2).set_color(BLUE).move_to(ax1.coords_to_point(X_VALUE.get_value(),0,0)).set_z_index(5))
        x_line_2 = always_redraw(lambda: DashedLine(DOT_REF, ax1.coords_to_point(X_VALUE.get_value(),0,0), color=BLUE).set_opacity(0.5).set_z_index(5))
        x_label_2 = always_redraw(lambda: MathTex(f'{X_VALUE.get_value():.2f}', color=BLUE).scale(0.8).next_to(x_line_2, UP, buff=0.2).set_z_index(5))

        fx_tick_2 = always_redraw(lambda: x_tick.copy().rotate(90*DEGREES).move_to(ax1.get_y_axis().number_to_point(1/X_VALUE.get_value())).set_z_index(5))
        fx_line_2 = always_redraw(lambda: DashedLine(DOT_REF, Dot().move_to(fx_tick_2), color=BLUE).set_opacity(0.5).set_z_index(5))
        fx_label_2 = always_redraw(lambda: MathTex(f'{1/X_VALUE.get_value():.1f}',r'= \frac{1}{',f'{X_VALUE.get_value():.2f}', color=BLUE).scale(0.8).next_to(fx_line_2, RIGHT, buff=0.25).shift(UP*0.04).set_z_index(5))

        self.play(self.camera.frame.animate.scale(1.4).move_to(ax1.coords_to_point(0,0.3,0)),
                  ax1_black_sq_aux1.animate.shift(LEFT*5),
                  ax1_black_sq_aux2.animate.shift(DOWN*5),
                  run_time=2)
        self.remove(DOT_REF, 
                    x_tick, x_line, x_label3, 
                    fx_tick, fx_line, fx_label4)
        self.wait(2)

        X_VALUE.set_value(-4)
        DOT_REF_path_2 = always_redraw(lambda: ax1.plot(lambda x: 1/x, x_range=[-4, X_VALUE.get_value()], stroke_width=5, color=BLUE).set_z_index(5))
        self.add(DOT_REF, DOT_REF_path_2,
                 x_tick_2, x_line_2, x_label_2, 
                 fx_tick_2, fx_line_2, fx_label_2)
        self.wait(2)
        self.play(X_VALUE.animate.set_value(-0.25), run_time=6)
        self.wait(2)



        # O limite deveria ser também igual a - infinito
        t5 = MathTex(r'\lim_{x \to 0^{-}} \frac{1}{x} = - \infty').move_to(ax1.coords_to_point(-3.7,-4,0))
        t5[0][3].set_color(BLUE)
        t5[0][5].set_color(RED)
        t5[0][9].set_color(BLUE)
        t5[0][11:].set_color(YELLOW)
        t5[0][3:6].shift(RIGHT*0.15)
        t5[0][0:7].shift(UP*0.1)

        self.play(LaggedStart(FadeIn(t5[0][0:6], t5[0][7:10]),
                              FadeIn(t5[0][10]),
                              FadeIn(t5[0][11:]),
                              lag_ratio=0.5))
        self.wait(2)
        self.play(Circumscribe(VGroup(t1, t3, t4)))
        self.wait()
        self.play(Circumscribe(VGroup(t5)))
        self.wait(2)



        # Limites laterais
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.7).move_to(VGroup(t1, t3, t4)), run_time=2)
        self.play(t3[0][3:6].animate.shift(LEFT*0.15),
                  GrowFromCenter(t3[0][6]))
        self.wait(2)

        gr2 = ax1.plot(lambda x: 1/x, x_range=[-4, -0.25], stroke_width=5, color=BLUE)
        self.remove(DOT_REF, DOT_REF_path_2,
                    x_tick_2, x_line_2, x_label_2, 
                    fx_tick_2, fx_line_2, fx_label_2)
        self.add(gr2)

        self.play(self.camera.frame.animate.move_to(t5), run_time=2)
        self.play(t5[0][3:6].animate.shift(LEFT*0.15),
                  GrowFromCenter(t5[0][6]))
        self.wait(2)

        self.play(self.camera.frame.animate.restore(), run_time=1.5)
        self.wait(2)



# O limite só existe se dois limites laterais coincidirem
class vid7(MovingCameraScene):
    def construct(self):

        # Retomando elementos
        ax1 = Axes(x_range=[-1, 8], x_length=9,
                   y_range=[-1, 5], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        gr1 = ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[0.4, 8], stroke_width=5, color=BLUE)
        gr1_label = MathTex('y = f(x)', color=BLUE).next_to(gr1, RIGHT).shift(UP*1.8+LEFT*0.1).set_z_index(7)
        

        A_COLOR = YELLOW
        L_COLOR = YELLOW

        dot_a_l = Dot(ax1.coords_to_point(3.5,2.38,0), color=A_COLOR).set_z_index(3)
        dot_a_l_black = dot_a_l.copy().set_color(BLACK).scale(0.6).set_z_index(4)

        a_tick = Line(ORIGIN, UP*0.2, color=A_COLOR).move_to(ax1.coords_to_point(3.5,0,0)).set_z_index(2)
        a_label = MathTex('a', color=A_COLOR).next_to(a_tick, DOWN, buff=0.2).set_z_index(2)
        a_line = DashedLine(a_tick, ax1.coords_to_point(3.5,2.38,0), color=A_COLOR).set_opacity(0.5).set_z_index(-1).set_z_index(2)
        
        l_tick = a_tick.copy().rotate(90*DEGREES).set_color(L_COLOR).move_to(ax1.coords_to_point(0,2.38,0)).set_z_index(2)
        l_label = MathTex('L', color=L_COLOR).next_to(l_tick, LEFT, buff=0.2).set_z_index(2)
        l_line = DashedLine(ax1.coords_to_point(3.5,2.38,0), l_tick, color=A_COLOR).set_opacity(0.5).set_z_index(-1).set_z_index(2)


        X_VALUE = ValueTracker(4.5)
        DOT_REF = always_redraw(lambda: Dot(gr1.get_point_from_function(t = X_VALUE.get_value()), color=BLUE).set_z_index(5))
        self.add(DOT_REF)

        x_tick = always_redraw(lambda: a_tick.copy().set_color(BLUE).move_to(ax1.coords_to_point(X_VALUE.get_value(),0,0)).set_z_index(2))
        x_line = always_redraw(lambda: DashedLine(DOT_REF, ax1.coords_to_point(X_VALUE.get_value(),-0.7,0), color=BLUE).set_opacity(0.5).set_z_index(-3))
        x_label = always_redraw(lambda: MathTex('x', color=BLUE).next_to(x_line, DOWN, buff=0.15).set_z_index(2))

        fx_tick = always_redraw(lambda: a_tick.copy().rotate(90*DEGREES).set_color(BLUE).move_to(ax1.get_y_axis().number_to_point(DOT_REF.get_y() + 2.2)).set_z_index(2))
        fx_line = always_redraw(lambda: DashedLine(DOT_REF, Dot().move_to(fx_tick).shift(LEFT*0.8), color=BLUE).set_opacity(0.5).set_z_index(-3))
        fx_label = always_redraw(lambda: MathTex('f(x)', color=BLUE).next_to(fx_line, LEFT, buff=0.15).set_z_index(2))

        x_bar = always_redraw(lambda: ax1.get_area(graph=gr1, x_range=(3.5, X_VALUE.get_value()), 
                             color=YELLOW, stroke_width=0).set_opacity(0.15).set_z_index(-5))
        fx_bar = always_redraw(lambda: Polygon(ax1.coords_to_point(0,2.38,0), 
                        fx_tick.get_center(), 
                        DOT_REF.get_center(),
                        ax1.coords_to_point(3.5,2.38,0),
                        color=YELLOW, stroke_width=0).set_opacity(0.15).set_z_index(-5))

        x_highlight = always_redraw(lambda: Line(ax1.coords_to_point(3.5,0,0), ax1.coords_to_point(X_VALUE.get_value(),0,0), color=YELLOW))
        y_highlight = always_redraw(lambda: Line(ax1.coords_to_point(0,2.38,0), fx_tick.get_center(), color=YELLOW))
        graph_highlight_r = always_redraw(lambda: ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[3.5, X_VALUE.get_value()], stroke_width=5, color=YELLOW))
        graph_highlight_l = always_redraw(lambda: ax1.plot(lambda x: x/2 + np.sin(x) + np.sin(x/2), x_range=[X_VALUE.get_value(), 3.5], stroke_width=5, color=YELLOW))


        lim_t = MathTex(r'\lim_{x\to a} f(x) = L ').shift(UP*2).set_z_index(13)
        VGroup(lim_t[0][3], lim_t[0][6:10]).set_color(BLUE)
        lim_t[0][5].set_color(A_COLOR)
        lim_t[0][11].set_color(L_COLOR)

        self.add(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label,
                 a_tick, a_label, a_line, dot_a_l, dot_a_l_black, l_label, l_tick, l_line,
                 lim_t,
                 x_tick, x_line, x_label, x_bar,
                 fx_tick, fx_line, fx_label, fx_bar,
                 x_highlight, y_highlight, graph_highlight_r)
        
        

        # Escrevendo os limites laterais
        lim_r = MathTex(r'\lim_{x\to a^{+}} f(x) = L ').scale(1).shift(RIGHT*4+UP*3).set_z_index(13)
        VGroup(lim_r[0][3], lim_r[0][7:11]).set_color(BLUE)
        lim_r[0][5].set_color(A_COLOR)
        lim_r[0][12].set_color(L_COLOR)

        lim_l = MathTex(r'\lim_{x\to a^{-}} f(x) = L ').scale(1).shift(RIGHT*4+UP*1.5).set_z_index(13)
        VGroup(lim_l[0][3], lim_l[0][7:11]).set_color(BLUE)
        lim_l[0][5].set_color(A_COLOR)
        lim_l[0][12].set_color(L_COLOR)

        g_lim_lat = VGroup(lim_r, lim_l).shift(DOWN*0.15)
        g_lim_lat_brace = Brace(g_lim_lat, LEFT, buff=0.3, color=GRAY).scale(1.1).set_z_index(13)
        
        g_lim_lat_sr = Square(color=BLACK).scale(3).move_to(g_lim_lat).shift(UP*1.5+RIGHT).set_stroke(width=0).set_opacity(0.8).set_z_index(8)
        
        self.play(ApplyWave(lim_t, amplitude=0.1))
        self.wait()
        self.play(LaggedStart(GrowFromEdge(g_lim_lat_brace, LEFT),
                              FadeIn(g_lim_lat_sr),
                              FadeIn(lim_r),
                              FadeIn(lim_l),
                              lag_ratio=0.5))
        self.wait(2)

        self.play(X_VALUE.animate.set_value(3.55), rate_func=linear, run_time=2)
        X_VALUE.set_value(4.5)
        
        self.remove(graph_highlight_r).add(graph_highlight_l)
        X_VALUE.set_value(2.5)
        self.play(X_VALUE.animate.set_value(3.45), rate_func=linear, run_time=2)

        self.remove(graph_highlight_l).add(graph_highlight_r)
        X_VALUE.set_value(4.5)
        self.play(X_VALUE.animate.set_value(3.55), rate_func=linear, run_time=2.0001)
        
        self.remove(graph_highlight_r).add(graph_highlight_l)
        X_VALUE.set_value(2.5)
        self.play(X_VALUE.animate.set_value(3.45), rate_func=linear, run_time=2)



        # Comentário sobre os sinais + e -
        big_black_square = Polygon(ax1.coords_to_point(-2,6,0),
                                   ax1.coords_to_point(10,6,0),
                                   ax1.coords_to_point(10,-2,0),
                                   ax1.coords_to_point(-2,-2,0)).set_stroke(width=0).set_color(BLACK).set_opacity(0.8).set_z_index(12)

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.8).move_to(g_lim_lat).shift(LEFT*1.6),
                  FadeIn(big_black_square),
                  FadeOut(g_lim_lat_sr),
                  run_time=2)
        self.wait()

        indicative_arrow1 = Arrow(DOWN*0.5, UP*0.8, color=WHITE).set_z_index(15).rotate(45*DEGREES).move_to(lim_r).shift(DOWN*0.6+LEFT*0.1)
        self.play(FadeIn(indicative_arrow1))
        self.play(indicative_arrow1.animate.shift(DOWN*1.5))
        self.play(FadeOut(indicative_arrow1))
        self.wait(2)


        
        lim_r_highlight_aux = SurroundingRectangle(lim_r)
        lim_r_highlight = Difference(big_black_square, lim_r_highlight_aux).set_stroke(width=0).set_color(BLACK).set_opacity(0.8).set_z_index(13)

        lim_l_highlight_aux1 = SurroundingRectangle(lim_l)
        lim_l_highlight_aux2 = lim_l_highlight_aux1.copy().set_stroke(width=0).set_color(BLACK).set_opacity(0.8).set_z_index(12)
        lim_l_highlight = Difference(big_black_square, lim_l_highlight_aux1).set_stroke(width=0).set_color(BLACK).set_opacity(0.8).set_z_index(13)

        self.play(LaggedStart(FadeIn(lim_r_highlight), 
                              FadeOut(big_black_square),
                              lag_ratio=0.15))
        self.wait(2)
        self.play(LaggedStart(FadeIn(lim_l_highlight, lim_l_highlight_aux2), 
                              FadeOut(lim_r_highlight),
                              lag_ratio=0.2))
        self.wait(2)
        self.play(LaggedStart(FadeIn(big_black_square), 
                              FadeOut(lim_l_highlight, lim_l_highlight_aux2),
                              lag_ratio=0.1))
        self.wait(2)



        # No caso da função '1/x', o limite não existe
        lim_1_over_x_t = MathTex(r'\lim_{x\to 0} \frac{1}{x} = L ').move_to(lim_t).shift(UP*0.125+RIGHT*0.3).set_z_index(13)
        VGroup(lim_1_over_x_t[0][3], lim_1_over_x_t[0][6:9]).set_color(BLUE)
        lim_1_over_x_t[0][5].set_color(RED)
        lim_1_over_x_t[0][10].set_color(L_COLOR)

        lim_1_over_x_r = MathTex(r'\lim_{x\to 0^{+}} \frac{1}{x} = + \infty').scale(1).move_to(lim_r).shift(UP*0.15+LEFT*0.02).set_z_index(13)
        VGroup(lim_1_over_x_r[0][3], lim_1_over_x_r[0][7:10]).set_color(BLUE)
        lim_1_over_x_r[0][5].set_color(RED)
        lim_1_over_x_r[0][11:].set_color(L_COLOR)

        lim_1_over_x_l = MathTex(r'\lim_{x\to 0^{-}} \frac{1}{x} = - \infty').scale(1).move_to(lim_l).shift(UP*0.15+LEFT*0.02).set_z_index(13)
        VGroup(lim_1_over_x_l[0][3], lim_1_over_x_l[0][7:10]).set_color(BLUE)
        lim_1_over_x_l[0][5].set_color(RED)
        lim_1_over_x_l[0][11:].set_color(L_COLOR)

        self.play(LaggedStart(FadeOut(lim_t[0][6:10]),
                              FadeIn(lim_1_over_x_t[0][6:10]),
                              lim_t[0][0:6].animate.shift(RIGHT*0.59),
                              lag_ratio=0.2),
                  LaggedStart(FadeOut(lim_r[0][7:11]),
                              FadeIn(lim_1_over_x_r[0][7:10]),
                              lim_r[0][11:].animate.shift(LEFT*0.57),
                              lag_ratio=0.2),
                  LaggedStart(FadeOut(lim_l[0][7:11]),
                              FadeIn(lim_1_over_x_l[0][7:10]),
                              lim_l[0][11:].animate.shift(LEFT*0.57),
                              lag_ratio=0.2))
        #self.wait()
        self.play(LaggedStart(FadeOut(lim_t[0][5]),
                              FadeIn(lim_1_over_x_t[0][5]),
                              lag_ratio=0.2),
                  LaggedStart(FadeOut(lim_r[0][5]),
                              FadeIn(lim_1_over_x_r[0][5]),
                              lag_ratio=0.2),
                  LaggedStart(FadeOut(lim_l[0][5]),
                              FadeIn(lim_1_over_x_l[0][5]),
                              lag_ratio=0.2))
        self.wait()
        self.play(LaggedStart(FadeOut(lim_r[0][12]),
                              FadeIn(lim_1_over_x_r[0][11:]),
                              FadeOut(lim_l[0][12]),
                              FadeIn(lim_1_over_x_l[0][11:]),
                              lag_ratio=0.2))
        self.wait()
        red_line1 = Line(UP*0.5, DOWN*0.6, color=RED, stroke_width=3).scale(2.5).rotate(70*DEGREES).move_to(lim_t).set_z_index(15)
        red_line2 = red_line1.copy().rotate(40*DEGREES).move_to(red_line1).reverse_points().set_z_index(15)
        self.play(LaggedStart(Create(red_line2), 
                              Create(red_line1), 
                              lag_ratio=0.4))
        self.wait()



# Definição intuitiva de limite
class vid8(MovingCameraScene):
    def construct(self):

        A_COLOR = L_COLOR = YELLOW
        
        lim_t = MathTex(r'\lim_{x\to a} f(x) = L ').shift(UP*1.3).set_z_index(13)
        VGroup(lim_t[0][3], lim_t[0][6:10]).set_color(BLUE)
        lim_t[0][5].set_color(A_COLOR)
        lim_t[0][11].set_color(L_COLOR)

        self.play(FadeIn(lim_t))
        self.wait(2)



        # Destacando cada parte da sentença lim_(x -> a) f(x) = L
        self.play(lim_t[0][3:].animate.set_opacity(0.3))
        self.wait()
        self.play(lim_t[0][0:6].animate.set_opacity(0.3),
                  lim_t[0][6:10].animate.set_opacity(1))
        self.wait()
        self.play(lim_t[0][6:10].animate.set_opacity(0.3),
                  lim_t[0][3:6].animate.set_opacity(1))
        self.wait()
        self.play(lim_t[0][3:6].animate.set_opacity(0.3),
                  lim_t[0][10:].animate.set_opacity(1))
        self.wait()
        self.play(lim_t[0][0:10].animate.set_opacity(1))
        self.wait(2)



        # Definição intuitiva
        lim_def1 = Tex(r'quando ','$x$',' está',' próximo ','de',' $a$',r',\\$f(x)$ ','está',' próximo ','de',' $L$').scale(0.9).next_to(lim_t, DOWN, buff=1)
        VGroup(lim_def1[1], lim_def1[6]).set_color(BLUE)
        VGroup(lim_def1[5], lim_def1[10]).set_color(YELLOW)

        lim_def_box1 = SurroundingRectangle(VGroup(lim_t, lim_def1), color=GRAY, buff=0.2).set_opacity(0.3).set_z_index(-1)

        self.play(LaggedStart(FadeIn(lim_def1[0]), FadeIn(lim_def1[1]),
                              FadeIn(lim_def1[2]), FadeIn(lim_def1[3]),
                              FadeIn(lim_def1[4]), FadeIn(lim_def1[5]), 
                              lag_ratio=0.35))
        self.wait(2)
        self.play(LaggedStart(FadeIn(lim_def1[6]), FadeIn(lim_def1[7]),
                              FadeIn(lim_def1[8]), FadeIn(lim_def1[9]),
                              FadeIn(lim_def1[10]),
                              lag_ratio=0.4))
        self.wait()
        self.play(Create(lim_def_box1), run_time=1.5)
        self.wait(2)
        self.play(lim_def1[0:3].animate.set_opacity(0.3),
                  lim_def1[4:8].animate.set_opacity(0.3),
                  lim_def1[9:11].animate.set_opacity(0.3))
        self.wait(4)



# Construindo a definição precisa de limite
class vid9(MovingCameraScene):
    def construct(self):
        
        # Retomando elementos (vid4)
        self.camera.frame.scale(1.2)

        ax1 = Axes(x_range=[-1.5, 4.9], x_length=6.4,
                   y_range=[-1.5, 6.9], y_length=8.4,
                   axis_config={"include_ticks" : True, "include_numbers" : True}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.1+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*4.1+RIGHT*0.6)

        gr1 = ax1.plot(lambda x: 2*x - 1, x_range=[-0.2, 4], stroke_width=5, color=BLUE)
        gr1_label = MathTex('y = 2x - 1', color=BLUE).next_to(gr1, RIGHT).shift(UP*4+RIGHT*0.3)
        
        self.add(ax1, ax1_x_label, ax1_y_label, gr1)

        A_COLOR = YELLOW
        L_COLOR = YELLOW

        a_tick = Line(ORIGIN, UP*0.2, stroke_width=2, color=A_COLOR).move_to(ax1.coords_to_point(3,0,0)).set_z_index(2)
        a_label = MathTex('3', color=A_COLOR).scale(0.7).next_to(a_tick, DOWN, buff=0.15).set_z_index(2)
        a_line = DashedLine(a_tick, ax1.coords_to_point(3,5,0), color=A_COLOR).set_opacity(0.5).set_z_index(-1).set_z_index(2)

        a_dot = Dot().set_color(A_COLOR).move_to(ax1.coords_to_point(3,5,0))
        a_dot_black = a_dot.copy().set_color(BLACK).scale(0.6).set_z_index(4)

        l_tick = a_tick.copy().rotate(90*DEGREES).set_color(L_COLOR).move_to(ax1.coords_to_point(0,5,0)).set_z_index(2)
        l_label = MathTex('5', color=L_COLOR).scale(0.7).next_to(l_tick, LEFT, buff=0.15).set_z_index(2)
        l_line = DashedLine(ax1.coords_to_point(3,5,0), l_tick, color=A_COLOR).set_opacity(0.5).set_z_index(-1).set_z_index(2)

        X_VALUE = ValueTracker(2.98)
        DOT_REF = always_redraw(lambda: Dot(gr1.get_point_from_function(t = X_VALUE.get_value()), color=BLUE).set_z_index(5))
        DOT_REF_hightlight1 = always_redraw(lambda: ax1.plot(lambda x: 2*x - 1, x_range=[3, X_VALUE.get_value()], stroke_width=5, color=YELLOW).set_z_index(3))
        DOT_REF_hightlight2 = always_redraw(lambda: ax1.plot(lambda x: 2*x - 1, x_range=[X_VALUE.get_value(), 3], stroke_width=5, color=YELLOW).set_z_index(3))

        self.add(DOT_REF, DOT_REF_hightlight1)

        x_tick = always_redraw(lambda: a_tick.copy().set_color(BLUE).move_to(ax1.coords_to_point(X_VALUE.get_value(),0,0)).set_z_index(2))
        x_line = always_redraw(lambda: DashedLine(DOT_REF, ax1.coords_to_point(X_VALUE.get_value(),-0.7,0), color=BLUE).set_opacity(0.5).set_z_index(-3))
        x_label = always_redraw(lambda: MathTex('x', color=BLUE).next_to(x_line, DOWN, buff=0.15).set_z_index(2))

        fx_tick = always_redraw(lambda: a_tick.copy().rotate(90*DEGREES).set_color(BLUE).move_to(ax1.get_y_axis().number_to_point(DOT_REF.get_y() + 2.9)).set_z_index(2))
        fx_line = always_redraw(lambda: DashedLine(DOT_REF, Dot().move_to(fx_tick).shift(LEFT*0.8), color=BLUE).set_opacity(0.5).set_z_index(-3))
        fx_label = always_redraw(lambda: MathTex('f(x)', color=BLUE).next_to(fx_line, LEFT, buff=0.15).set_z_index(2))

        x_highlight = always_redraw(lambda: Line(ax1.coords_to_point(X_VALUE.get_value(),0,0), ax1.coords_to_point(3,0,0), stroke_width=4, color=A_COLOR))
        fx_highlight = always_redraw(lambda: Line(fx_tick.get_center(), ax1.coords_to_point(0,5,0), stroke_width=4, color=A_COLOR))

        x_bar = always_redraw(lambda: ax1.get_area(graph=gr1, x_range=(3, X_VALUE.get_value()), 
                             color=YELLOW, stroke_width=0).set_opacity(0.15).set_z_index(-5))
        fx_bar = always_redraw(lambda: Polygon(ax1.coords_to_point(0,5,0), 
                        fx_tick.get_center(), 
                        ax1.coords_to_point(X_VALUE.get_value(),2*X_VALUE.get_value() - 1,0),
                        ax1.coords_to_point(3,5,0),
                        color=YELLOW, stroke_width=0).set_opacity(0.15).set_z_index(-5))
        

        t3 = MathTex(r'\lim_{x \to 3} 2x - 1 = 5 ').shift(RIGHT*5+UP*3.5)
        VGroup(t3[0][3], t3[0][6:10]).set_color(BLUE)
        t3[0][5].set_color(A_COLOR)
        t3[0][11].set_color(L_COLOR)

        self.add(x_tick, x_line, x_label, x_highlight, x_bar,
                 fx_tick, fx_line, fx_label, fx_highlight, fx_bar,
                 a_label, a_tick, a_line, a_dot, a_dot_black,
                 l_label, l_tick, l_line,
                 t3)
        


        # Quão próximo de 3 deverá estar o 'x'...
        X_REF_L = ValueTracker(2.98)
        X_REF_R = ValueTracker(3.02)

        x_hl = always_redraw(lambda: Line(ax1.coords_to_point(X_REF_L.get_value(),0,0), ax1.coords_to_point(X_REF_R.get_value(),0,0), stroke_width=4, color=A_COLOR))
        x_hl_bar = always_redraw(lambda: ax1.get_area(graph=gr1, x_range=(X_REF_L.get_value(), X_REF_R.get_value()), 
                             color=YELLOW, stroke_width=0).set_opacity(0.15).set_z_index(-5))

        x_hl_left_par = always_redraw(lambda: Tex('(', color=YELLOW).scale(0.6).next_to(x_hl, LEFT, buff=-0.07))
        x_hl_right_par = always_redraw(lambda: Tex(')', color=YELLOW).scale(0.6).next_to(x_hl, RIGHT, buff=-0.07))

        self.remove(fx_tick, fx_line, fx_label, fx_highlight, fx_bar, x_highlight, x_bar)
        self.add(x_hl, x_hl_bar, x_hl_left_par, x_hl_right_par)
        self.play(X_REF_L.animate.set_value(2.98 - 0.48),
                  X_REF_R.animate.set_value(3.02 + 0.48))
        self.play(X_VALUE.animate.set_value(3.5), rate_func=linear)
        self.play(X_VALUE.animate.set_value(3.0001), rate_func=linear)
        self.remove(DOT_REF_hightlight1).add(DOT_REF_hightlight2)
        self.play(X_VALUE.animate.set_value(2.5), rate_func=linear)
        self.wait(2)



        # ...para que 'f(x)' difira de 5 por menos que 0,5
        FX_REF_D = ValueTracker(4.98)
        FX_REF_U = ValueTracker(5.02)
        fx_hl = always_redraw(lambda: Line(ax1.coords_to_point(0,FX_REF_D.get_value(),0), ax1.coords_to_point(0,FX_REF_U.get_value(),0), stroke_width=4, color=A_COLOR))
        fx_hl_bar = always_redraw(lambda: Polygon(ax1.coords_to_point(0,FX_REF_D.get_value(),0), 
                                                  ax1.coords_to_point((FX_REF_D.get_value() + 1)/2,FX_REF_D.get_value(),0),
                                                  ax1.coords_to_point((FX_REF_U.get_value() + 1)/2,FX_REF_U.get_value(),0),
                                                  ax1.coords_to_point(0,FX_REF_U.get_value(),0),
                                                  color=YELLOW, stroke_width=0).set_opacity(0.15).set_z_index(-5))

        x_hl_down_par = always_redraw(lambda: Tex('(', color=YELLOW).scale(0.6).rotate(90*DEGREES).next_to(fx_hl, DOWN, buff=-0.07))
        x_hl_up_par = always_redraw(lambda: Tex(')', color=YELLOW).scale(0.6).rotate(90*DEGREES).next_to(fx_hl, UP, buff=-0.07))

        self.add(fx_tick, fx_line, fx_label, fx_hl, fx_hl_bar, x_hl_down_par, x_hl_up_par)
        self.play(FX_REF_D.animate.set_value(2*2.5 - 1),
                  FX_REF_U.animate.set_value(2*3.5 - 1))
        self.play(X_VALUE.animate.set_value((5 + 1)/2), rate_func=linear)
        self.remove(DOT_REF_hightlight2).add(DOT_REF_hightlight1)
        self.play(X_VALUE.animate.set_value((6 + 1)/2), rate_func=linear)
        self.play(X_VALUE.animate.set_value((5 + 1)/2), rate_func=linear)
        self.remove(DOT_REF_hightlight1).add(DOT_REF_hightlight2)
        

        brace_aux = Brace(Line(ax1.coords_to_point(0,5,0), ax1.coords_to_point(0,4.5,0)),
                                 direction=RIGHT, color=GRAY).set_z_index(3)
        brace_aux_label = MathTex('0,5').scale(0.7).next_to(brace_aux, RIGHT, buff=0.1).set_z_index(3)
        brace_aux_label_sr = SurroundingRectangle(brace_aux_label, color=BLACK).set_stroke(width=0).set_opacity(0.7).set_z_index(2)

        self.play(X_REF_L.animate.set_value(3 - 0.25), X_REF_R.animate.set_value(3 + 0.25),
                  FX_REF_D.animate.set_value(4.5), FX_REF_U.animate.set_value(5.5),
                  FadeIn(brace_aux, brace_aux_label, brace_aux_label_sr))
        self.wait(2)



        # Distância entre 'x' e 3 = |x - 3|
        self.remove(DOT_REF_hightlight2)
        self.add(DOT_REF_hightlight1)
        self.play(X_VALUE.animate.set_value(3.4),
                  X_REF_L.animate.set_value(3 - 0.5), X_REF_R.animate.set_value(3 + 0.5),
                  FX_REF_D.animate.set_value(4), FX_REF_U.animate.set_value(6),
                  self.camera.frame.animate.scale(0.7).move_to(a_tick).shift(UP),
                  FadeOut(brace_aux, brace_aux_label, brace_aux_label_sr),
                  run_time=1.5)
        self.wait(2)


        '''dist_x_3_brace = always_redraw(lambda: Brace(Line(ax1.coords_to_point(3,0,0),
                                                          ax1.coords_to_point(X_VALUE.get_value(),0,0)),
                                                     direction=UP,
                                                     color=GRAY))
        self.play(FadeIn(dist_x_3_brace))
        self.wait(2)


        dist_x_3 = MathTex(r'\vert x - 3 \vert').scale(0.8).next_to(dist_x_3_brace, UP, buff=0.1).set_z_index(3)
        dist_x_3[0][1].set_color(BLUE)
        dist_x_3[0][3].set_color(YELLOW)
        dist_x_3_sr = SurroundingRectangle(dist_x_3, color=BLACK).set_stroke(width=0).set_opacity(0.7).set_z_index(2)

        self.play(LaggedStart(FadeIn(dist_x_3_sr),
                              FadeIn(dist_x_3[0][1]),
                              FadeIn(dist_x_3[0][2]),
                              FadeIn(dist_x_3[0][3]),
                              lag_ratio=0.3))
        self.wait(2)
        self.remove(DOT_REF_hightlight1).add(DOT_REF_hightlight2)
        self.play(X_VALUE.animate.set_value(2.6),
                  dist_x_3[0][1:4].animate.shift(LEFT*0.4),
                  dist_x_3_sr.animate.shift(LEFT*0.4))
        self.wait(2)
        dist_x_3[0][0].shift(LEFT*0.4)
        dist_x_3[0][4].shift(LEFT*0.4)
        self.play(FadeIn(dist_x_3[0][0], dist_x_3[0][4]))
        self.wait(2)



        # Distância entre 'f(x)' e 5 = |f(x) - 5|
        self.play(self.camera.frame.animate.move_to(l_tick).shift(RIGHT), run_time=1.5)
        self.wait(2)


        dist_fx_5_brace = always_redraw(lambda: Brace(Line(ax1.coords_to_point(0,5,0),
                                                          ax1.coords_to_point(0,2*X_VALUE.get_value() - 1,0)),
                                                     direction=RIGHT,
                                                     color=GRAY))
        self.play(FadeIn(dist_fx_5_brace))
        self.wait(2)


        dist_fx_5 = MathTex(r'\vert f(x) - 5 \vert').scale(0.8).next_to(dist_fx_5_brace, RIGHT, buff=0.1).set_z_index(3)
        dist_fx_5[0][1:5].set_color(BLUE)
        dist_fx_5[0][6].set_color(YELLOW)
        dist_fx_5_sr = SurroundingRectangle(dist_fx_5, color=BLACK).set_stroke(width=0).set_opacity(0.7).set_z_index(2)

        self.play(LaggedStart(FadeIn(dist_fx_5_sr),
                              FadeIn(dist_fx_5[0][0], dist_fx_5[0][7]),
                              FadeIn(dist_fx_5[0][1:7]),
                              lag_ratio=0.4))
        self.wait(2)



        # Escrevendo a implicação da definição formal
        self.play(self.camera.frame.animate.scale(1.4286).move_to(ORIGIN).shift(RIGHT*4),
                  t3.animate.shift(RIGHT), 
                  run_time=2)
        self.wait(2)

        
        t4 = MathTex(r'\vert x - 3 \vert < \delta',r'\:\:\:\Rightarrow\:\:\:',r'\vert f(x) - 5 \vert < 0,5').scale(0.8).next_to(t3, DOWN, buff=1, aligned_edge=LEFT).set_z_index(3)
        t4[0][1].set_color(BLUE)
        t4[0][3].set_color(YELLOW)
        t4[2][1:5].set_color(BLUE)
        t4[2][6].set_color(YELLOW)
        t4[0][6].scale(1.2)

        self.play(GrowFromCenter(t4[0][6]))
        self.wait()
        self.play(dist_x_3.animate.move_to(t4[0][0:5]),
                  FadeOut(dist_x_3_sr, dist_x_3_brace),
                  t4[0][6].animate.scale(1/(1.2)))
        self.wait()
        self.play(LaggedStart(FadeIn(t4[0][5])))
        self.wait()
        self.play(LaggedStart(FadeIn(t4[1])))
        self.wait()
        self.play(dist_fx_5.animate.move_to(t4[2][0:8]),
                  FadeOut(dist_fx_5_sr, dist_fx_5_brace))
        self.wait()
        self.play(LaggedStart(FadeIn(t4[2][8]),
                              FadeIn(t4[2][9:]),
                              lag_ratio=0.5))
        self.wait(2)



        # Arrumando as coisas
        self.remove(dist_x_3, dist_fx_5)
        self.add(t4[0][0:5], t4[2][0:8])



        # Fazendo a conta para encontrar o delta
        t5 = MathTex(r'\vert x - 3 \vert < \delta',r'\:\:\:\Rightarrow\:\:\:',r'\vert 2x - 1 - 5 \vert < 0,5').scale(0.8).next_to(t4, DOWN, buff=0.5, aligned_edge=LEFT)
        t5[0][1].set_color(BLUE)
        t5[0][3].set_color(YELLOW)
        t5[2][1:5].set_color(BLUE)
        t5[2][6].set_color(YELLOW)

        self.play(TransformFromCopy(VGroup(t4[1], t4[2][0], t4[2][5:]),
                                    VGroup(t5[1], t5[2][0], t5[2][5:])))
        self.play(TransformFromCopy(t4[2][1:5], t5[2][1:5]))  
        self.wait(2)


        t6 = MathTex(r'\vert x - 3 \vert < \delta',r'\:\:\:\Rightarrow\:\:\:',r'\vert 2x - 6 \vert < 0,5').scale(0.8).next_to(t5, DOWN, buff=0.5, aligned_edge=LEFT)
        t6[0][1].set_color(BLUE)
        t6[0][3].set_color(YELLOW)
        t6[2][1:3].set_color(BLUE)
        t6[2][4].set_color(YELLOW)

        self.play(TransformFromCopy(VGroup(t5[1], t5[2][0:3], t5[2][7:]),
                                    VGroup(t6[1], t6[2][0:3], t6[2][5:])))
        self.play(TransformFromCopy(t5[2][3:7], t6[2][3:5]))
        self.wait(2)


        t7 = MathTex(r'\vert x - 3 \vert < \delta',r'\:\:\:\Rightarrow\:\:\:',r'2 \vert x - 3 \vert < 0,5').scale(0.8).next_to(t6, DOWN, buff=0.5, aligned_edge=LEFT)
        t7[0][1].set_color(BLUE)
        t7[0][3].set_color(YELLOW)
        t7[2][2].set_color(BLUE)
        t7[2][4].set_color(YELLOW)

        self.play(TransformFromCopy(VGroup(t6[1], t6[2][0:]),
                                    VGroup(t7[1], t7[2][0:])))
        self.wait(2)


        t8 = MathTex(r'\vert x - 3 \vert < \delta',r'\:\:\:\Rightarrow\:\:\:',r'\vert x - 3 \vert < 0,25').scale(0.8).next_to(t7, DOWN, buff=0.5, aligned_edge=LEFT)
        t8[0][1].set_color(BLUE)
        t8[0][3].set_color(YELLOW)
        t8[2][1].set_color(BLUE)
        t8[2][3].set_color(YELLOW)

        t_aux1 = t7[2][1:7].copy()
        self.play(t_aux1.animate.move_to(t8[2][0:6]),
                  TransformFromCopy(t7[2][7:], t8[2][6:]),
                  TransformFromCopy(t7[1], t8[1]))
        self.wait(2)



        # Arrumando as coisas
        self.remove(t_aux1)
        self.add(t8[2][0:6])



        # Cada linha implica a próxima
        self.play(t5[1:].animate.set_opacity(0.3),
                  t6[1:].animate.set_opacity(0.3),
                  t7[1:].animate.set_opacity(0.3),
                  t8[1:].animate.set_opacity(0.3))
        self.play(t4[0:].animate.set_opacity(0.3),
                  t5[1:].animate.set_opacity(1))
        self.play(t5[1:].animate.set_opacity(0.3),
                  t6[1:].animate.set_opacity(1))
        self.play(t6[1:].animate.set_opacity(0.3),
                  t7[1:].animate.set_opacity(1))
        self.play(t7[1:].animate.set_opacity(0.3),
                  t8[1:].animate.set_opacity(1))
        self.wait(2)



        # delta = 0,25
        sr_025 = SurroundingRectangle(t8[2][6:], color=GRAY)
        sr_delta = SurroundingRectangle(t4[0][6], color=GRAY)

        self.play(Create(sr_025))
        self.play(t4[0:].animate.set_opacity(1))
        self.play(Create(sr_delta))
        self.wait(2)


        x_025_brace = Brace(Line(ax1.coords_to_point(2.75,0,0), ax1.coords_to_point(3,0,0)),
                                 direction=UP, color=GRAY).set_z_index(3)
        x_025_label = MathTex('0,25').scale(0.7).next_to(x_025_brace, UP, buff=0.1).set_z_index(3)
        x_025_label_sr = SurroundingRectangle(x_025_label, color=BLACK).set_stroke(width=0).set_opacity(0.7).set_z_index(2)

        fx_025_brace = Brace(Line(ax1.coords_to_point(0,4.5,0), ax1.coords_to_point(0,5,0)),
                                 direction=RIGHT, color=GRAY).set_z_index(3)
        fx_025_label = MathTex('0,5').scale(0.7).next_to(fx_025_brace, RIGHT, buff=0.1).set_z_index(3)
        fx_025_label_sr = SurroundingRectangle(fx_025_label, color=BLACK).set_stroke(width=0).set_opacity(0.7).set_z_index(2)

        self.play(VGroup(t8[2][6:], sr_025).animate.move_to(t4[0][6], aligned_edge=LEFT).shift(DOWN*0.05),
                  FadeOut(t4[0][6], sr_delta,
                          t5[1:],
                          t6[1:],
                          t7[1:],
                          t8[1], t8[2][0:6]),
                  t4[1:].animate.shift(RIGHT*0.7))
        self.play(FadeOut(sr_025))
        self.wait(2)
        self.play(X_VALUE.animate.set_value(2.85), 
                  X_REF_L.animate.set_value(2.75),
                  X_REF_R.animate.set_value(3.25),
                  FX_REF_D.animate.set_value(2*2.75 - 1),
                  FX_REF_U.animate.set_value(2*3.25 - 1),
                  FadeIn(x_025_brace, x_025_label, x_025_label_sr), run_time=1.5)
        self.wait(2)
        self.play(FadeIn(fx_025_brace, fx_025_label, fx_025_label_sr))
        self.wait(2)



        # Se quisermos uma tolerância de 0,1
        sr_aux1 = SurroundingRectangle(t4[2][9:], color=GRAY).set_z_index(5)
        self.play(Create(sr_aux1))
        self.wait()

        t9 = MathTex('0,5').scale(0.8).move_to(t4[2][9:], aligned_edge=LEFT).set_z_index(5)
        t9_aux = SurroundingRectangle(t9, color=BLACK).set_opacity(1).set_z_index(4)
        self.add(t9, t9_aux)
        self.play(t4[0][0:6].animate.set_opacity(0.3),
                  t8[2][6:].animate.set_opacity(0.3),
                  t4[1].animate.set_opacity(0.3),
                  FadeOut(x_025_brace, x_025_label, x_025_label_sr,
                          fx_025_brace, fx_025_label, fx_025_label_sr))

        t10 = MathTex('0,4').scale(0.8).move_to(t4[2][9:], aligned_edge=LEFT).set_z_index(5)
        self.remove(t9).add(t10)
        self.wait(0.5)

        t11 = MathTex('0,3').scale(0.8).move_to(t4[2][9:], aligned_edge=LEFT).set_z_index(5)
        self.remove(t10).add(t11)
        self.wait(0.5)

        t12 = MathTex('0,2').scale(0.8).move_to(t4[2][9:], aligned_edge=LEFT).set_z_index(5)
        self.remove(t11).add(t12)
        self.wait(0.5)

        t13 = MathTex('0,1').scale(0.8).move_to(t4[2][9:], aligned_edge=LEFT).set_z_index(5)
        self.remove(t12).add(t13)
        self.wait(2)



            # Fazendo a mesma conta de antes
        self.play(ReplacementTransform(t8[2][6:], t4[0][6]),
                  t4[0][0:6].animate.set_opacity(1),
                  t4[1].animate.set_opacity(1).shift(LEFT*0.35),
                  FadeOut(sr_aux1))
        self.wait(2)


        t14 = MathTex(r'\:\:\:\Rightarrow\:\:\:',r'\vert 2x - 1 - 5 \vert < 0,1').scale(0.8).next_to(t4[1:], DOWN, buff=0.5, aligned_edge=LEFT)
        t15 = MathTex(r'\:\:\:\Rightarrow\:\:\:',r'\vert 2x - 6 \vert < 0,1').scale(0.8).next_to(t14, DOWN, buff=0.5, aligned_edge=LEFT)
        t16 = MathTex(r'\:\:\:\Rightarrow\:\:\:',r'2 \vert x - 3 \vert < 0,1').scale(0.8).next_to(t15, DOWN, buff=0.5, aligned_edge=LEFT)
        t17 = MathTex(r'\:\:\:\Rightarrow\:\:\:',r'\vert x - 3 \vert < 0,05').scale(0.8).next_to(t16, DOWN, buff=0.5, aligned_edge=LEFT)    
        VGroup(t14[1][1:5],
               t15[1][1:3],
               t16[1][2],
               t17[1][1]).set_color(BLUE)
        VGroup(t14[1][6],
               t15[1][4],
               t16[1][4],
               t17[1][3]).set_color(YELLOW)
        self.play(LaggedStart(FadeIn(t14),
                              FadeIn(t15),
                              FadeIn(t16),
                              FadeIn(t17),
                              lag_ratio=0.5))
        self.wait()


        sr_005 = SurroundingRectangle(t17[1][6:], color=GRAY)
        self.play(Create(sr_005))
        self.wait(2)


        self.play(FadeOut(t14, t15, t16, t17, sr_005),
                  t4[0][0:7].animate.set_opacity(0.3),
                  t4[1].animate.set_opacity(0.3))
        


        # Se quisermos uma tolerância de 0,01
        t18 = MathTex('0,01').scale(0.8).move_to(t13, aligned_edge=LEFT).set_z_index(5)
        self.play(TransformMatchingShapes(t13, t18))
        self.wait(2)



            # Fazendo a mesma conta de antes
        self.play(t4[0][0:7].animate.set_opacity(1),
                  t4[1].animate.set_opacity(1))
        self.wait()


        t19 = MathTex(r'\:\:\:\Rightarrow\:\:\:',r'\vert 2x - 1 - 5 \vert < 0,01').scale(0.8).next_to(t4[1:], DOWN, buff=0.5, aligned_edge=LEFT)
        t20 = MathTex(r'\:\:\:\Rightarrow\:\:\:',r'\vert 2x - 6 \vert < 0,01').scale(0.8).next_to(t14, DOWN, buff=0.5, aligned_edge=LEFT)
        t21 = MathTex(r'\:\:\:\Rightarrow\:\:\:',r'2 \vert x - 3 \vert < 0,01').scale(0.8).next_to(t15, DOWN, buff=0.5, aligned_edge=LEFT)
        t22 = MathTex(r'\:\:\:\Rightarrow\:\:\:',r'\vert x - 3 \vert < 0,005').scale(0.8).next_to(t16, DOWN, buff=0.5, aligned_edge=LEFT)
        VGroup(t19[1][1:5],
               t20[1][1:3],
               t21[1][2],
               t22[1][1]).set_color(BLUE)
        VGroup(t19[1][6],
               t20[1][4],
               t21[1][4],
               t22[1][3]).set_color(YELLOW)
        self.play(LaggedStart(FadeIn(t19),
                              FadeIn(t20),
                              FadeIn(t21),
                              FadeIn(t22),
                              lag_ratio=0.3))
        self.wait()


        sr_0005 = SurroundingRectangle(t22[1][6:], color=GRAY)
        self.play(Create(sr_0005))
        self.wait(2)

        sr_aux2 = SurroundingRectangle(t18, color=GRAY).set_z_index(5)
        self.play(Create(sr_aux2))
        self.wait(2)


        self.play(FadeOut(t19, t20, t21, t22, sr_0005, sr_aux2),
                  t4[0][0:7].animate.set_opacity(0.3),
                  t4[1].animate.set_opacity(0.3))
        self.wait(2)



        # Para uma tolerância qualquer epsilon
        t23 = MathTex(r'\varepsilon').scale(0.8).move_to(t18, aligned_edge=LEFT).set_z_index(5)
        self.play(FadeTransform(t18, t23, stretch=False))
        self.wait(2)


            # Fazendo a mesma conta de antes
        self.play(t4[0][0:7].animate.set_opacity(1),
                  t4[1].animate.set_opacity(1))
        self.wait()


        t24 = MathTex(r'\:\:\:\Rightarrow\:\:\:',r'\vert 2x - 1 - 5 \vert < \varepsilon').scale(0.8).next_to(t4[1:], DOWN, buff=0.5, aligned_edge=LEFT)
        t24[1][9].scale(0.8/0.7)
        t25 = MathTex(r'\:\:\:\Rightarrow\:\:\:',r'\vert 2x - 6 \vert < \varepsilon').scale(0.8).next_to(t14, DOWN, buff=0.5, aligned_edge=LEFT)
        t25[1][7].scale(0.8/0.7)
        t26 = MathTex(r'\:\:\:\Rightarrow\:\:\:',r'2 \vert x - 3 \vert < \varepsilon').scale(0.8).next_to(t15, DOWN, buff=0.5, aligned_edge=LEFT)
        t26[1][7].scale(0.8/0.7)
        t27 = MathTex(r'\:\:\:\Rightarrow\:\:\:',r'\vert x - 3 \vert < \varepsilon/2').scale(0.8).next_to(t16, DOWN, buff=0.5, aligned_edge=LEFT)
        t27[1][6].scale(0.8/0.7)
        VGroup(t24[1][1:5],
               t25[1][1:3],
               t26[1][2],
               t27[1][1]).set_color(BLUE)
        VGroup(t24[1][6],
               t25[1][4],
               t26[1][4],
               t27[1][3]).set_color(YELLOW)
        self.play(LaggedStart(FadeIn(t24),
                              FadeIn(t25),
                              FadeIn(t26),
                              FadeIn(t27),
                              lag_ratio=0.3))
        self.wait()


        sr_epsilon_over_2 = SurroundingRectangle(t27[1][6:], color=GRAY)
        self.play(Create(sr_epsilon_over_2))
        self.wait(2)



        # Mostrando no gráfico que |x - 3| < epsilon/2   ->   |f(x) - 5| < epsilon
        x_epsilon_over_2_brace = Brace(Line(ax1.coords_to_point(2.75,0,0), ax1.coords_to_point(3,0,0)), direction=UP, color=GRAY).set_z_index(3)
        x_epsilon_over_2_label = MathTex(r'\varepsilon/2').scale(0.7).next_to(x_epsilon_over_2_brace, UP, buff=0.1).set_z_index(3)
        x_epsilon_over_2_label[0][0].scale(0.8/0.7)
        x_epsilon_over_2_label_sr = SurroundingRectangle(x_epsilon_over_2_label, color=BLACK).set_stroke(width=0).set_opacity(0.7).set_z_index(2)

        fx_epsilon_over_2_brace = Brace(Line(ax1.coords_to_point(0,4.5,0), ax1.coords_to_point(0,5,0)), direction=RIGHT, color=GRAY).set_z_index(3)
        fx_epsilon_over_2_label = MathTex(r'\varepsilon').scale(0.8).next_to(fx_epsilon_over_2_brace, RIGHT, buff=0.1).set_z_index(3)
        fx_epsilon_over_2_label_sr = SurroundingRectangle(fx_epsilon_over_2_label, color=BLACK).set_stroke(width=0).set_opacity(0.7).set_z_index(2)

        self.camera.frame.save_state()

        self.play(self.camera.frame.animate.scale(0.7).move_to(a_tick).shift(UP), run_time=2)
        self.play(FadeIn(x_epsilon_over_2_brace, x_epsilon_over_2_label, x_epsilon_over_2_label_sr))
        self.wait(2)

        self.play(self.camera.frame.animate.move_to(l_tick).shift(RIGHT), run_time=2)
        self.play(FadeIn(fx_epsilon_over_2_brace, fx_epsilon_over_2_label, fx_epsilon_over_2_label_sr))
        self.wait(2)

        self.play(self.camera.frame.animate.restore())
        self.wait(2)



        # Adicionando updaters às distâncias epsilon e epsilon/2
        x_epsilon_over_2_brace.add_updater(lambda m: m.become(Brace(Line(ax1.coords_to_point(X_REF_L.get_value(),0,0), ax1.coords_to_point(3,0,0)), direction=UP, color=GRAY).set_z_index(3)))
        x_epsilon_over_2_label.add_updater(lambda m: m.become(MathTex(r'\varepsilon/2').scale(0.7).next_to(x_epsilon_over_2_brace, UP, buff=0.1).set_z_index(3)))
        x_epsilon_over_2_label_sr.add_updater(lambda m: m.become(SurroundingRectangle(x_epsilon_over_2_label, color=BLACK).set_stroke(width=0).set_opacity(0.7).set_z_index(2)))

        fx_epsilon_over_2_brace.add_updater(lambda m: m.become(Brace(Line(ax1.coords_to_point(0,FX_REF_D.get_value(),0), ax1.coords_to_point(0,5,0)), direction=RIGHT, color=GRAY).set_z_index(3)))
        fx_epsilon_over_2_label.add_updater(lambda m: m.become(MathTex(r'\varepsilon').scale(0.8).next_to(fx_epsilon_over_2_brace, RIGHT, buff=0.1).set_z_index(3)))
        fx_epsilon_over_2_label_sr.add_updater(lambda m: m.become(SurroundingRectangle(fx_epsilon_over_2_label, color=BLACK).set_stroke(width=0).set_opacity(0.7).set_z_index(2)))



        # Epsilon pode ser qualquer número positivo
        self.play(LaggedStart(FadeOut(t4[0][0:7], t4[1], t4[2][0:9], t23,
                                      t24, t25, t26, t27, sr_epsilon_over_2),
                              t3.animate.shift(DOWN*3+RIGHT*1),
                              lag_ratio=0.5),
                              run_time=2)
        self.wait(2)


            # Zoom em 'f(x)'
        self.play(LaggedStart(self.camera.frame.animate.scale(0.6).move_to(l_tick).shift(RIGHT),
                              AnimationGroup(X_REF_L.animate.set_value(2.95), X_REF_R.animate.set_value(3.05),
                                             FX_REF_D.animate.set_value(2*2.95 - 1), FX_REF_U.animate.set_value(2*3.05 - 1),
                                             X_VALUE.animate.set_value(2.98)), lag_ratio=0.25), run_time=6)
        self.wait(2)


            # Zoom em 'x'
        self.play(self.camera.frame.animate.move_to(a_tick).shift(UP),
                  X_REF_L.animate.set_value(2.75), X_REF_R.animate.set_value(3.25),
                  FX_REF_D.animate.set_value(2*2.75 - 1), FX_REF_U.animate.set_value(2*3.25 - 1),
                  X_VALUE.animate.set_value(2.85), run_time=1.5)
        self.play(X_REF_L.animate.set_value(2.9), X_REF_R.animate.set_value(3.1),
                  FX_REF_D.animate.set_value(2*2.9 - 1), FX_REF_U.animate.set_value(2*3.1 - 1),
                  X_VALUE.animate.set_value(2.95), run_time=6)
        self.wait(2)


            # Afastando a câmera
        self.play(self.camera.frame.animate.restore(), run_time=2)
        self.wait(2)



        # O valor do limite não poderia ser diferente de 5
        t28 = MathTex(r'\lim_{x \to 3} 2x - 1 = 4').move_to(t3, aligned_edge=LEFT)
        VGroup(t28[0][3], t28[0][6:10]).set_color(BLUE)
        t28[0][5].set_color(A_COLOR)
        t28[0][11].set_color(L_COLOR)

        l_label2 = MathTex('4', color=L_COLOR).scale(0.7).next_to(Dot().scale(1.55).move_to(l_tick).shift(DOWN*1), LEFT, buff=0.15).set_z_index(2)
        l_line2 = DashedLine(ax1.coords_to_point((4 + 1)/2,4,0), Dot().scale(0).move_to(l_tick).shift(DOWN*1), color=A_COLOR).set_opacity(0.5).set_z_index(-1).set_z_index(2)

        self.play(l_tick.animate.shift(DOWN*1), ReplacementTransform(l_line, l_line2),
                  FadeOut(t3[0][11], shift=UP), FadeOut(l_label),
                  FadeIn(t28[0][11], shift=UP), FadeIn(l_label2))
        self.wait(2)
        self.play(X_REF_L.animate.set_value((3.5 + 1)/2), X_REF_R.animate.set_value((6.5 + 1)/2),
                  FX_REF_D.animate.set_value(3.5), FX_REF_U.animate.set_value(6.5),
                  X_VALUE.animate.set_value((3.7 + 1)/2),
                  run_time=2)
        self.wait(2)
        self.play(X_REF_L.animate.set_value((4.3 + 1)/2), X_REF_R.animate.set_value((5.7 + 1)/2),
                  FX_REF_D.animate.set_value(4.3), FX_REF_U.animate.set_value(5.7),
                  X_VALUE.animate.set_value((4.4 + 1)/2),
                  run_time=5)
        self.wait(2)


        red_line1 = Line(UP*0.5, DOWN*0.6, color=RED, stroke_width=4).scale(0.8).rotate(55*DEGREES).move_to(t28[0][11])
        red_line2 = red_line1.copy().rotate(70*DEGREES).move_to(red_line1).reverse_points()
        self.play(LaggedStart(Create(red_line2), 
                              Create(red_line1), 
                              lag_ratio=0.4))
        self.wait(2)'''



# Escrevendo a definição precisa de limite
class vid10(MovingCameraScene):
    def construct(self):
        
        A_COLOR = L_COLOR = YELLOW

        lim_t = MathTex(r'\lim_{x\to a} f(x) = L ').shift(UP*1.3)
        VGroup(lim_t[0][3], lim_t[0][6:10]).set_color(BLUE)
        lim_t[0][5].set_color(A_COLOR)
        lim_t[0][11].set_color(L_COLOR)

        self.play(FadeIn(lim_t))
        self.wait(2)



        # Destacando cada parte da sentença lim_(x -> a) f(x) = L
        self.play(lim_t[0][3:].animate.set_opacity(0.3))
        self.wait()
        self.play(lim_t[0][0:6].animate.set_opacity(0.3),
                  lim_t[0][6:10].animate.set_opacity(1))
        self.wait()
        self.play(lim_t[0][6:10].animate.set_opacity(0.3),
                  lim_t[0][3:6].animate.set_opacity(1))
        self.wait()
        self.play(lim_t[0][3:6].animate.set_opacity(0.3),
                  lim_t[0][10:].animate.set_opacity(1))
        self.wait()
        self.play(lim_t[0][0:10].animate.set_opacity(1))
        self.wait(2)



        # Escrevendo a definição precisa
        lim_def1 = Tex('para ','qualquer ',r'$\varepsilon > 0$',' houver ','um ',r'$\delta > 0$',' tal ','que').scale(0.9).next_to(lim_t, DOWN, buff=1)
        lim_def2 = Tex(r'$\vert x - a \vert$',' $<$ ',r'$\delta$',r' \:\:\:$\Rightarrow$\:\:\: ',r'$\vert f(x) - L \vert$',' $<$ ',r'$\varepsilon$').scale(0.9).next_to(lim_def1, DOWN, buff=0.3)
        VGroup(lim_def2[0][1], lim_def2[4][1:5]).set_color(BLUE)
        VGroup(lim_def2[0][3], lim_def2[4][6]).set_color(YELLOW)

        lim_def_box1 = SurroundingRectangle(VGroup(lim_t, lim_def1, lim_def2), color=GRAY, buff=0.2).set_opacity(0.3).set_z_index(-1)

        self.play(LaggedStart(FadeIn(lim_def1[0]), FadeIn(lim_def1[1]), FadeIn(lim_def1[2]),
                              lag_ratio=0.5))
        self.play(LaggedStart(FadeIn(lim_def1[3]), FadeIn(lim_def1[4]), FadeIn(lim_def1[5]),
                              lag_ratio=0.5))
        self.play(LaggedStart(FadeIn(lim_def1[6]), FadeIn(lim_def1[7]),
                              lag_ratio=0.5))
        self.play(LaggedStart(FadeIn(lim_def2[0]), FadeIn(lim_def2[1]), FadeIn(lim_def2[2]),
                              lag_ratio=0.5))
        self.play(FadeIn(lim_def2[3]))
        self.play(LaggedStart(FadeIn(lim_def2[4]), FadeIn(lim_def2[5]),
                              FadeIn(lim_def2[6]),
                              lag_ratio=0.5))
        self.wait()
        self.play(Create(lim_def_box1), run_time=1.5)
        self.wait(2)



        # Comparando a definição precisa com a intuitiva
        lim_t_copy = lim_t.copy().shift(UP*1.5)
        lim_def3 = Tex(r'quando ','$x$',' está',' próximo ','de',' $a$',r',\\$f(x)$ ','está',' próximo ','de',' $L$').scale(0.9).next_to(lim_t_copy, DOWN, buff=0.7)
        VGroup(lim_def3[1], lim_def3[6]).set_color(BLUE)
        VGroup(lim_def3[5], lim_def3[10]).set_color(YELLOW)

        lim_def_box2 = SurroundingRectangle(VGroup(lim_t_copy, lim_def3), color=GRAY, buff=0.2).set_opacity(0.3).set_z_index(-1)

        self.add(lim_t_copy, lim_def3, lim_def_box2)
        VGroup(lim_t_copy, lim_def3, lim_def_box2).shift(UP*3.5)

        black_sq1 = lim_def_box1.copy().shift(DOWN*2).scale(1.45).set_opacity(0.6).set_color(BLACK).set_stroke(width=0).set_z_index(3)

        self.play(self.camera.frame.animate.scale(1.1),
                  LaggedStart(AnimationGroup(lim_t.animate.shift(DOWN*2.2),
                                             VGroup(lim_def1, lim_def2).animate.shift(DOWN*1.9),
                                             lim_def_box1.animate.shift(DOWN*2).set_height(lim_def_box1.get_height()*0.95).set_width(lim_def_box1.get_width()*1)),
                              AnimationGroup(VGroup(lim_t_copy, lim_def3, lim_def_box2).animate.shift(DOWN*3.5),
                                             FadeIn(black_sq1)),
                              lag_ratio=0.2),
                              run_time=2)
        self.wait(2)
        self.play(FadeOut(black_sq1))
        self.wait(2)
        self.play(LaggedStart(VGroup(lim_t, lim_def1, lim_def2, lim_def_box1).animate.shift(DOWN*5),
                              VGroup(lim_t_copy, lim_def3, lim_def_box2).animate.move_to(ORIGIN),
                              lag_ratio=0.2),
                              run_time=2)
        self.wait(2)
        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)



# Limite para x -> infinito
class vid11(MovingCameraScene):
    def construct(self):

        A_COLOR = L_COLOR = YELLOW

        lim_t1 = MathTex(r'\lim_{x\to \infty}').scale(1.5)
        lim_t1[0][3].set_color(BLUE)
        lim_t1[0][5].set_color(YELLOW)

        lim_t2 = MathTex(r'\lim_{x\to \pm\infty}').scale(1.5)
        lim_t2[0][3].set_color(BLUE)
        lim_t2[0][5:].set_color(YELLOW)


        self.play(FadeIn(lim_t1[0][0:3]))
        self.wait()
        self.play(LaggedStart(FadeIn(lim_t1[0][3]),
                              FadeIn(lim_t1[0][4]),
                              FadeIn(lim_t1[0][5]),
                              lag_ratio=0.2))
        self.wait()
        self.play(TransformMatchingShapes(lim_t1[0][3:], lim_t2[0][3:]))
        self.wait(2)
        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)



# Exemplo y = 1/x
class vid12(MovingCameraScene):
    def construct(self):

        ax1 = Axes(x_range=[-1, 8], x_length=9,
                   y_range=[-1.3, 8], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        gr1 = ax1.plot(lambda x: 1/x, x_range=[0.14, 7.4], stroke_width=5, color=BLUE)
        gr1_label = MathTex(r'y = \frac{1}{x}', color=BLUE).shift(UP*2)
        
        X_VALUE = ValueTracker(0.14)
        DOT_REF = always_redraw(lambda: Dot(gr1.get_point_from_function(t = X_VALUE.get_value()), color=BLUE).set_z_index(5))
        DOT_REF_path = always_redraw(lambda: ax1.plot(lambda x: 1/x, x_range=[0.14, X_VALUE.get_value()], stroke_width=5, color=BLUE).set_z_index(5))

        a_tick = Line(ORIGIN, UP*0.2, color=YELLOW).move_to(ax1.coords_to_point(3.5,0,0)).set_z_index(2)
        
        x_tick = always_redraw(lambda: a_tick.copy().set_color(BLUE).move_to(ax1.coords_to_point(X_VALUE.get_value(),0,0)).set_z_index(2))
        x_line = always_redraw(lambda: DashedLine(DOT_REF, ax1.coords_to_point(X_VALUE.get_value(),-0.7,0), color=BLUE).set_opacity(0.5).set_z_index(-3))
        x_label = always_redraw(lambda: MathTex('x', color=BLUE).next_to(x_line, DOWN, buff=0.15).set_z_index(2))

        fx_tick = always_redraw(lambda: a_tick.copy().rotate(90*DEGREES).set_color(BLUE).move_to(ax1.get_y_axis().number_to_point(1/X_VALUE.get_value())).set_z_index(2))
        fx_line = always_redraw(lambda: DashedLine(DOT_REF, Dot().move_to(fx_tick).shift(LEFT*0.8), color=BLUE).set_opacity(0.5).set_z_index(-3))
        fx_label = always_redraw(lambda: MathTex(r'\frac{1}{x}', color=BLUE).next_to(fx_line, LEFT, buff=0.15).set_z_index(2))

        self.add(ax1, ax1_x_label, ax1_y_label,
                 gr1_label)
        self.wait(2)
        self.add(DOT_REF, DOT_REF_path,
                 x_tick, x_line, x_label, 
                 fx_tick, fx_line, fx_label)
        self.wait(2)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.75).move_to(ax1.coords_to_point(3.5,2,0)),
                  X_VALUE.animate.set_value(7.4), run_time=10)
        self.wait()


        # Escrevendo o limite
        lim_t = MathTex(r'\lim_{x\to +\infty} \frac{1}{x} = 0').move_to(gr1_label).shift(RIGHT*0.24)
        VGroup(lim_t[0][3], lim_t[0][7:10]).set_color(BLUE)
        lim_t[0][5:7].set_color(YELLOW)
        lim_t[0][11].set_color(YELLOW)

        self.play(self.camera.frame.animate.restore(), run_time=1.5)
        self.play(FadeIn(lim_t[0][0:3]),
                  FadeOut(gr1_label[0][0:2]))
        self.wait()
        self.play(FadeIn(lim_t[0][3:7]))
        self.wait()
        self.play(FadeIn(lim_t[0][10:]))
        self.wait(2)
        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)



# Exemplo y = xˆ3
class vid13(MovingCameraScene):
    def construct(self):

        ax1 = Axes(x_range=[-3, 3], x_length=6,
                   y_range=[-5, 5], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        gr1 = ax1.plot(lambda x: x**3, x_range=[0, 1.7], stroke_width=5, color=BLUE)
        gr1_label = MathTex(r'y = x^3', color=BLUE).shift(UP*2+RIGHT*3.2)
        
        X_VALUE = ValueTracker(0)
        DOT_REF = always_redraw(lambda: Dot(gr1.get_point_from_function(t = X_VALUE.get_value()), color=BLUE).set_z_index(5))
        DOT_REF_path1 = always_redraw(lambda: ax1.plot(lambda x: x**3, x_range=[0, X_VALUE.get_value()], stroke_width=5, color=BLUE).set_z_index(5))
        DOT_REF_path2 = always_redraw(lambda: ax1.plot(lambda x: x**3, x_range=[X_VALUE.get_value(), 0], stroke_width=5, color=BLUE).set_z_index(5))

        a_tick = Line(ORIGIN, UP*0.2, color=YELLOW).move_to(ax1.coords_to_point(3.5,0,0)).set_z_index(2)
        
        x_tick1 = always_redraw(lambda: a_tick.copy().set_color(BLUE).move_to(ax1.coords_to_point(X_VALUE.get_value(),0,0)).set_z_index(2))
        x_line1 = always_redraw(lambda: DashedLine(DOT_REF, ax1.coords_to_point(X_VALUE.get_value(),0,0), color=BLUE).set_opacity(0.5).set_z_index(-3))
        x_label1 = always_redraw(lambda: MathTex('x', color=BLUE).next_to(x_line1, DOWN, buff=0.3).set_z_index(2))

        fx_tick1 = always_redraw(lambda: a_tick.copy().rotate(90*DEGREES).set_color(BLUE).move_to(ax1.get_y_axis().number_to_point(X_VALUE.get_value()**3)).set_z_index(2))
        fx_line1 = always_redraw(lambda: DashedLine(DOT_REF, Dot().move_to(fx_tick1).shift(LEFT*0.8), color=BLUE).set_opacity(0.5).set_z_index(-3))
        fx_label1 = always_redraw(lambda: MathTex(r'x^3', color=BLUE).next_to(fx_line1, LEFT, buff=0.15).set_z_index(2))

        self.add(ax1, ax1_x_label, ax1_y_label,
                 gr1_label)
        self.wait(2)
        self.add(DOT_REF, DOT_REF_path1,
                 x_tick1, x_line1, x_label1, 
                 fx_tick1, fx_line1, fx_label1)
        self.wait(2)
        self.play(X_VALUE.animate.set_value(1.7), run_time=5)
        self.wait(2)


        x_tick2 = always_redraw(lambda: a_tick.copy().set_color(BLUE).move_to(ax1.coords_to_point(X_VALUE.get_value(),0,0)).set_z_index(2))
        x_line2 = always_redraw(lambda: DashedLine(DOT_REF, ax1.coords_to_point(X_VALUE.get_value(),0,0), color=BLUE).set_opacity(0.5).set_z_index(-3))
        x_label2 = always_redraw(lambda: MathTex('x', color=BLUE).next_to(x_line2, UP, buff=0.3).set_z_index(2))

        fx_tick2 = always_redraw(lambda: a_tick.copy().rotate(90*DEGREES).set_color(BLUE).move_to(ax1.get_y_axis().number_to_point(X_VALUE.get_value()**3)).set_z_index(2))
        fx_line2 = always_redraw(lambda: DashedLine(DOT_REF, Dot().move_to(fx_tick2), color=BLUE).set_opacity(0.5).set_z_index(-3))
        fx_label2 = always_redraw(lambda: MathTex(r'x^3', color=BLUE).next_to(fx_line2, RIGHT, buff=0.3).shift(UP*0.1).set_z_index(2))

        self.remove(DOT_REF_path1,
                    x_tick1, x_line1, x_label1, 
                    fx_tick1, fx_line1, fx_label1)
        self.add(gr1, DOT_REF_path2,
                 x_tick2, x_line2, x_label2, 
                 fx_tick2, fx_line2, fx_label2)
        X_VALUE.set_value(0)
        self.wait(2)
        self.play(X_VALUE.animate.set_value(-1.7), run_time=5)
        self.wait(2)




        # Escrevendo o limite
        lim_t1 = MathTex(r'\lim_{x\to +\infty} x^3 = +\infty').move_to(gr1_label).shift(RIGHT*0.54+DOWN*0.12)
        VGroup(lim_t1[0][3], lim_t1[0][7:9]).set_color(BLUE)
        lim_t1[0][5:7].set_color(YELLOW)
        lim_t1[0][10:].set_color(YELLOW)

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.8).shift(UP+RIGHT),
                  FadeOut(gr1_label[0][0:2]),
                  FadeIn(lim_t1[0][0:3]),
                  run_time=2)
        self.wait()
        self.play(FadeIn(lim_t1[0][3:7]))
        self.wait()
        self.play(FadeIn(lim_t1[0][9:]))
        self.wait(2)


        lim_t2 = MathTex(r'\lim_{x\to -\infty} x^3 = -\infty').shift(LEFT*3.7+DOWN*2.5)
        VGroup(lim_t2[0][3], lim_t2[0][7:9]).set_color(BLUE)
        lim_t2[0][5:7].set_color(YELLOW)
        lim_t2[0][10:].set_color(YELLOW)

        self.play(self.camera.frame.animate.shift(DOWN*2+LEFT*2), 
                  FadeOut(DOT_REF,
                          x_tick2, x_line2, x_label2, 
                          fx_tick2, fx_line2, fx_label2),
                  run_time=2)
        self.play(FadeIn(lim_t2[0][0:3], lim_t2[0][7:9]))
        self.wait()
        self.play(FadeIn(lim_t2[0][3:7]))
        self.wait()
        self.play(FadeIn(lim_t2[0][9:]))
        self.play(self.camera.frame.animate.restore(), run_time=1.5)
        self.wait(2)



# Exemplo y = sen(x)
class vid14(MovingCameraScene):
    def construct(self):

        ax1 = Axes(x_range=[-2, 21], x_length=9,
                   y_range=[-2, 5], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        gr1 = ax1.plot(lambda x: 0.9*np.sin(x), x_range=[-1.5, 20.3], stroke_width=5, color=BLUE)
        gr1_label = MathTex(r'y = \text{sen}(x)', color=BLUE).shift(UP*2)
        
        X_VALUE = ValueTracker(-1.5)
        DOT_REF = always_redraw(lambda: Dot(gr1.get_point_from_function(t = X_VALUE.get_value()), color=BLUE).set_z_index(5))
        DOT_REF_path = always_redraw(lambda: ax1.plot(lambda x: 0.9*np.sin(x), x_range=[-1.5, X_VALUE.get_value()], stroke_width=5, color=BLUE).set_z_index(5))

        a_tick = Line(ORIGIN, UP*0.2, color=YELLOW).move_to(ax1.coords_to_point(3.5,0,0)).set_z_index(2)
        
        x_tick = always_redraw(lambda: a_tick.copy().set_color(BLUE).move_to(ax1.coords_to_point(X_VALUE.get_value(),0,0)).set_z_index(2))
        x_line = always_redraw(lambda: DashedLine(DOT_REF, ax1.coords_to_point(X_VALUE.get_value(),-0.9,0), color=BLUE).set_opacity(0.5).set_z_index(-3))
        x_label = always_redraw(lambda: MathTex('x', color=BLUE).next_to(x_line, DOWN, buff=0.15).set_z_index(2))

        fx_tick = always_redraw(lambda: a_tick.copy().rotate(90*DEGREES).set_color(BLUE).move_to(ax1.get_y_axis().number_to_point(0.9*np.sin(X_VALUE.get_value()))).set_z_index(2))
        fx_line = always_redraw(lambda: DashedLine(DOT_REF, Dot().move_to(fx_tick).shift(LEFT*0.8), color=BLUE).set_opacity(0.5).set_z_index(-3))
        fx_label = always_redraw(lambda: MathTex(r'\text{sen}(x)', color=BLUE).next_to(fx_line, LEFT, buff=0.15).set_z_index(2))

        self.add(ax1, ax1_x_label, ax1_y_label,
                 gr1_label)
        self.wait(2)
        self.add(DOT_REF, DOT_REF_path,
                 x_tick, x_line, x_label, 
                 fx_tick, fx_line, fx_label)
        self.wait(2)


        pos_1_tick = fx_tick.copy().set_color(GRAY).move_to(ax1.coords_to_point(0,0.9,0))
        pos_1_label = MathTex('1', color=GRAY).scale(0.8).next_to(pos_1_tick, UL, buff=0.15).shift(RIGHT*0.1)

        neg_1_tick = fx_tick.copy().set_color(GRAY).move_to(ax1.coords_to_point(0,-0.9,0))
        neg_1_label = MathTex('-1', color=GRAY).scale(0.8).next_to(neg_1_tick, DL, buff=0.15).shift(RIGHT*0.1)

        self.play(LaggedStart(X_VALUE.animate.set_value(20.3),
                              FadeIn(pos_1_tick, pos_1_label, neg_1_tick, neg_1_label),
                              lag_ratio=0.2), run_time=10)
        self.wait(2)



        # Escrevendo o limite
        lim_t1 = MathTex(r'\lim_{x\to +\infty} \text{sen}(x)').move_to(gr1_label).shift(LEFT*0.24+DOWN*0.11)
        VGroup(lim_t1[0][3], lim_t1[0][7:10]).set_color(BLUE)
        lim_t1[0][5:7].set_color(YELLOW)
        lim_t1[0][11].set_color(YELLOW)

        lim_t2 = Tex('não',' existe').next_to(lim_t1, RIGHT, buff=0.25).shift(UP*0.14)

        self.play(FadeIn(lim_t1[0][0:3]),
                  FadeOut(gr1_label[0][0:2]))
        self.wait()
        self.play(FadeIn(lim_t1[0][3:7]))
        self.wait()
        self.play(LaggedStart(FadeIn(lim_t2[0]),
                              FadeIn(lim_t2[1]),
                              lag_ratio=0.2))
        self.wait(2)
        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)



# Comentário sobre a definição
class vid15(MovingCameraScene):
    def construct(self):
        
        A_COLOR = L_COLOR = YELLOW

        lim_t = MathTex(r'\lim_{x\to a} f(x) = L ').shift(UP*1.3)
        VGroup(lim_t[0][3], lim_t[0][6:10]).set_color(BLUE)
        lim_t[0][5].set_color(A_COLOR)
        lim_t[0][11].set_color(L_COLOR)

        lim_def1 = Tex('para ','qualquer ',r'$\varepsilon > 0$',' houver ','um ',r'$\delta > 0$',' tal ','que').scale(0.9).next_to(lim_t, DOWN, buff=1)
        lim_def2 = Tex(r'$\vert x - a \vert$',' $<$ ',r'$\delta$',r' \:\:\:$\Rightarrow$\:\:\: ',r'$\vert f(x) - L \vert$',' $<$ ',r'$\varepsilon$').scale(0.9).next_to(lim_def1, DOWN, buff=0.3)
        VGroup(lim_def2[0][1], lim_def2[4][1:5]).set_color(BLUE)
        VGroup(lim_def2[0][3], lim_def2[4][6]).set_color(YELLOW)

        lim_def_box1 = SurroundingRectangle(VGroup(lim_t, lim_def1, lim_def2), color=GRAY, buff=0.2).set_opacity(0.3).set_z_index(-1)

        self.play(FadeIn(lim_t, lim_def1, lim_def2, lim_def_box1))
        self.wait(4)



        # Para os casos em que o limite envolve infinito...
        lim_t2 = MathTex(r'\lim_{x\to \pm\infty} f(x) = \pm\infty ').shift(UP*1.3)
        VGroup(lim_t2[0][3], lim_t2[0][7:11]).set_color(BLUE)
        lim_t2[0][5:7].set_color(A_COLOR)
        lim_t2[0][12:].set_color(L_COLOR)
        
        self.play(lim_def1.animate.set_opacity(0.3),
                  lim_def2.animate.set_opacity(0.3),
                  LaggedStart(AnimationGroup(lim_t[0][0:3].animate.move_to(lim_t2[0][0:3]), 
                                             TransformMatchingShapes(lim_t[0][3:6], lim_t2[0][3:7])),
                              TransformMatchingShapes(lim_t[0][11], lim_t2[0][12:]),
                              lag_ratio=0.6))
        self.wait(2)
