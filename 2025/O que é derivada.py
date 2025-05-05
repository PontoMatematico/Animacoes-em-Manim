# O que é derivada

from manim import *

# Introdução
class vid1(Scene):
    def construct(self):
        
        # Este é o gráfico de uma função de 'x'...
        ax1 = Axes(x_range=[-1, 14], x_length=8,
                   y_range=[-1, 9], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

            # Definindo a função f(x)
        def f(x):
            return (x + 1) / 2 + np.sin(x - 1) + np.sin((x + 1) / 2)

            # Derivada de f(x)
        def f_prime(x):
            return 0.5 + np.cos(x - 1) + 0.5 * np.cos((x + 1) / 2)
        
        gr1 = ax1.plot(f, x_range=[0.4, 13], stroke_width=4, color=BLUE)
        gr1_label = MathTex('y = f(x)', color=BLUE).next_to(gr1, RIGHT).shift(UP*2+LEFT*0)
        
            # Criando o gráfico
        self.play(LaggedStart(FadeIn(ax1), FadeIn(ax1_x_label, ax1_y_label), Create(gr1), FadeIn(gr1_label), lag_ratio=0.2))
        self.wait(2)



        





        # A função cresce aqui, decresce ali...
            # Destaquenas regiões em que a função cresce ou decresce
        HL_COLOR = YELLOW
        HL_STROKE_WIDTH = 8

        hl_increasing_1 = ax1.plot(f, x_range=[0.4, 2.89], stroke_width=HL_STROKE_WIDTH, color=HL_COLOR)
        hl_increasing_2 = ax1.plot(f, x_range=[5.7, 9.82], stroke_width=HL_STROKE_WIDTH, color=HL_COLOR)
        hl_increasing_3 = ax1.plot(f, x_range=[10.72, 13], stroke_width=HL_STROKE_WIDTH, color=HL_COLOR)
        
        hl_decreasing_1 = ax1.plot(f, x_range=[2.89, 5.70], stroke_width=HL_STROKE_WIDTH, color=HL_COLOR)

        hl_low_variation_1 = ax1.plot(f, x_range=[9.5, 11.2], stroke_width=HL_STROKE_WIDTH, color=HL_COLOR)

        self.play(LaggedStart(Create(hl_increasing_1, time_width=0.8),
                              Create(hl_increasing_2, time_width=0.8),
                              Create(hl_increasing_3, time_width=0.8),
                              lag_ratio=0.7))
        self.wait(2)
        self.play(FadeOut(hl_increasing_1, hl_increasing_2, hl_increasing_3))                       

        self.play(Create(hl_decreasing_1, time_width=0.8))
        self.wait(2)
        self.play(FadeOut(hl_decreasing_1))                       

        self.play(Create(hl_low_variation_1, time_width=0.8))
        self.wait(2)
        self.play(FadeOut(hl_low_variation_1))                       
        self.wait(2)



        # Se a função cresce, quão rápido ela cresce?
        self.play(LaggedStart(FadeIn(hl_increasing_1),
                              FadeIn(hl_increasing_2),
                              FadeIn(hl_increasing_3),
                              lag_ratio=0.3))
        self.wait(2)

        hl_arrow = Arrow(max_tip_length_to_length_ratio=0.15, max_stroke_width_to_length_ratio=6).set_color(HL_COLOR).scale(0.6)
        hl_arrow_1 = hl_arrow.copy().rotate(62*DEGREES).move_to(hl_increasing_1).shift(LEFT*0.4+UP*0.3)
        hl_arrow_2 = hl_arrow.copy().rotate(55*DEGREES).move_to(hl_increasing_2).shift(LEFT*0.4+UP*0.12)
        hl_arrow_3 = hl_arrow.copy().rotate(55*DEGREES).move_to(hl_increasing_3).shift(LEFT*0+UP*0.25)

        self.play(LaggedStart(FadeIn(hl_arrow_1),
                              FadeIn(hl_arrow_2),
                              FadeIn(hl_arrow_3),
                              lag_ratio=0.3))
        self.wait(2)
        self.play(FadeOut(hl_increasing_1, hl_increasing_2, hl_increasing_3,
                          hl_arrow_1, hl_arrow_2, hl_arrow_3))
        self.wait(2)


        # Quais são os pontos exatos em que ela troca entre crescente e decrescente?
        max_dot_1 = Dot().move_to(ax1.c2p(2.893, 3.825, 0))
        max_dot_2 = Dot().move_to(ax1.c2p(9.816, 5.212, 0))

        min_dot_1 = Dot().move_to(ax1.c2p(5.7, 2.143, 0))
        min_dot_2 = Dot().move_to(ax1.c2p(10.722, 5.158, 0))

        self.play(GrowFromCenter(max_dot_1))
        self.play(GrowFromCenter(min_dot_1))
        self.wait(2)
        hl_aux_1 = ax1.plot(f, x_range=[5.7, 13], stroke_width=HL_STROKE_WIDTH, color=HL_COLOR)
        self.play(Succession(ShowPassingFlash(hl_increasing_1, time_width=0.7),
                             ShowPassingFlash(hl_decreasing_1, time_width=0.7),
                             ShowPassingFlash(hl_aux_1, time_width=0.7, time=2)))
        self.play(FadeOut(max_dot_1, min_dot_1))
        self.wait(2)



        # O objetivo é encontrar uma forma de quantificar a variação
        X = ValueTracker(0.4)

        moving_point = always_redraw(lambda: Dot(color=WHITE).move_to(ax1.c2p(X.get_value(), f(X.get_value()))))
        derivative_tex = always_redraw(lambda: MathTex(str(round(f_prime(X.get_value()), 2))).scale(0.8).next_to(moving_point, UP, buff=0.2))
        
        self.add(moving_point, derivative_tex)
        self.play(X.animate.set_value(13), run_time=10, rate_func=linear)
        self.wait(2)



# Sobre a variação na função do 1o grau
class vid2(Scene):
    def construct(self):
        
        # Criando o gráfico
        ax1 = Axes(x_range=[-1, 14], x_length=8,
                   y_range=[-1, 9 ], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        def f(x):
            return 0.5*x + 2

        gr1 = ax1.plot(f, x_range=[-1, 13], stroke_width=4, color=GREEN)
        gr1_label = MathTex('y = ax + b', color=GREEN).to_edge(UP, buff=1)

        self.play((FadeIn(gr1_label)))        
        self.play(LaggedStart(FadeIn(ax1), FadeIn(ax1_x_label, ax1_y_label), Create(gr1), lag_ratio=0.2))
        self.wait(2)



        # "Variação" é sinônimo de "inclinação"
        black_sq_1 = Square(color=BLACK).set_opacity(0.8).scale(10).set_z_index(2)
        t1 = Tex('variação',' = ','inclinação').set_z_index(3)

        self.play(FadeIn(black_sq_1, t1[0]))
        self.wait(2)
        self.play(FadeIn(t1[1]))
        self.play(FadeIn(t1[2]))
        self.wait(2)
        
       
        
        # O parâmetro 'a' tem dois nomes: taxa de variação e coeficiente angular
        t_aux_1 = gr1_label.copy().set_z_index(3)
        t_aux_1[0][2].set_color(YELLOW)
        self.play(FadeIn(t_aux_1))
        self.wait(2)


        t2 = Tex(r'\it ``taxa de variação"', color=YELLOW).set_z_index(4).shift(UP*1.4+LEFT*2.7)
        t3 = Tex(r'\it ``coeficiente angular"', color=YELLOW).set_z_index(4).shift(UP*1.4+RIGHT*2.7)
        self.play(FadeIn(t2))
        self.wait(2)
        self.play(FadeIn(t3))
        self.wait(2)

        arrow_t2 = CurvedArrow(Dot(t_aux_1[0][2].get_edge_center(DOWN)).shift(DOWN*0.2).get_center(), Dot(t1[0].get_edge_center(UP)).shift(UP*0.2).get_center(), radius=4).shift(LEFT*0.1).set_z_index(3).set_color(GRAY_C)
        arrow_t3 = CurvedArrow(Dot(t_aux_1[0][2].get_edge_center(DOWN)).shift(DOWN*0.2).get_center(), Dot(t1[2].get_edge_center(UP)).shift(UP*0.2).get_center(), radius=-4).shift(RIGHT*0.1).set_z_index(3).set_color(GRAY_C)
        self.play(FadeIn(arrow_t2))
        self.wait(2)
        self.play(FadeIn(arrow_t3))
        self.wait(2)

        gr1_label[0][2].set_color(YELLOW)
        self.play(FadeOut(t1, t_aux_1, t2, t3, arrow_t2, arrow_t3, black_sq_1))
        self.wait(2)



# Calculando o valor do coeficiente 'a'
class vid3(Scene):
    def construct(self):
        
        # Retomando elementos
        ax1 = Axes(x_range=[-1, 14], x_length=8,
                   y_range=[-1, 9 ], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        def f(x):
            return 0.5*x + 2

        gr1 = ax1.plot(f, x_range=[-1, 13], stroke_width=4, color=GREEN)
        gr1_label = MathTex('y = ax + b', color=GREEN).to_edge(UP, buff=1)
        gr1_label[0][2].set_color(YELLOW)

        self.add(gr1_label,ax1, ax1_x_label, ax1_y_label, gr1)
        self.wait(2)



        # Escolhemos dois pontos e fazemos 'Delta y/Delta x'
        X = ValueTracker(5.5)
        DX = ValueTracker(2)

        DX_COLOR = RED
        DY_COLOR = PURPLE


        dot_1 = Dot().move_to(ax1.c2p(X.get_value(),f(X.get_value()),0)).set_z_index(2)
        dot_2 = Dot().move_to(ax1.c2p(X.get_value() + DX.get_value(),f(X.get_value() + DX.get_value()),0)).set_z_index(2)


        x1_line = DashedLine(dot_1, ax1.c2p(X.get_value(),0,0)).set_color(GRAY)      
        y1_line = DashedLine(dot_1, ax1.c2p(0,f(X.get_value()),0)).set_color(GRAY)
        
        x2_line = DashedLine(dot_2, ax1.c2p(X.get_value() + DX.get_value(),0,0)).set_color(GRAY)      
        y2_line = DashedLine(dot_2, ax1.c2p(0,f(X.get_value() + DX.get_value()),0)).set_color(GRAY)      

        x1_label = MathTex(r'x_1').scale(0.8).next_to(x1_line, DOWN, buff=0.1).set_color(GRAY)  
        y1_label = MathTex(r'y_1').scale(0.8).next_to(y1_line, LEFT, buff=0.1).set_color(GRAY)  

        x2_label = MathTex(r'x_2').scale(0.8).next_to(x2_line, DOWN, buff=0.1).set_color(GRAY)  
        y2_label = MathTex(r'y_2').scale(0.8).next_to(y2_line, LEFT, buff=0.1).set_color(GRAY)  


        delta_y_line = Line(ax1.c2p(X.get_value() + DX.get_value(),f(X.get_value()),0), dot_2).set_color(DY_COLOR).scale(1.07)
        delta_x_line = Line(dot_1, ax1.c2p(X.get_value() + DX.get_value(),f(X.get_value()),0)).set_color(DX_COLOR)

        delta_y_brace = Brace(delta_y_line, RIGHT, buff=0.1)
        delta_x_brace = Brace(delta_x_line, DOWN, buff=0.1)

        delta_y_label_1 = MathTex(r'y_2 - y_1').scale(0.8).next_to(delta_y_line, RIGHT, buff=0.15).set_color(DY_COLOR)
        delta_y_label_2 = MathTex(r'\Delta y').scale(0.8).next_to(delta_y_line, RIGHT, buff=0.1).set_color(DY_COLOR)
        delta_x_label_1 = MathTex(r'x_2 - x_1').scale(0.8).next_to(delta_x_line, DOWN, buff=0.2).set_color(DX_COLOR).set_z_index(3)
        delta_x_label_1_sr = SurroundingRectangle(delta_x_label_1).set_color(BLACK).set_stroke(width=0).set_opacity(0.8).set_z_index(2)
        delta_x_label_2 = MathTex(r'\Delta x').scale(0.8).next_to(delta_x_line, DOWN, buff=0.1).set_color(DX_COLOR)


        t1 = MathTex(r'a = \frac{y_2 - y_1}{x_2 - x_1}').move_to(gr1_label).shift(DOWN*0.05)
        t1[0][0].set_color(YELLOW)
        t1[0][2:7].set_color(DY_COLOR)
        t1[0][8:13].set_color(DX_COLOR)

        t2 = MathTex(r'a = \frac{\Delta y}{\Delta x}').move_to(t1).shift(UP*0.1)
        t2[0][0].set_color(YELLOW)
        t2[0][2:4].set_color(DY_COLOR)
        t2[0][5:7].set_color(DX_COLOR)


        self.play(ReplacementTransform(gr1_label[0][2], t1[0][0]),
                  FadeOut(gr1_label[0][0:2], gr1_label[0][3:]),
                  FadeIn(t1[0][1]))
        self.wait(2)
        self.play(LaggedStart(AnimationGroup(GrowFromCenter(dot_1), FadeIn(x1_line, x1_label, y1_line, y1_label)),
                              AnimationGroup(GrowFromCenter(dot_2), FadeIn(x2_line, x2_label, y2_line, y2_label)),
                              lag_ratio=0.4))
        self.wait(2)
        self.play(FadeIn(t1[0][2:8], delta_y_label_1),
                  Create(delta_y_line))
        self.wait(2)
        self.play(FadeIn(t1[0][8:13], delta_x_label_1, delta_x_label_1_sr),
                  Create(delta_x_line))
        self.wait(2)
        self.play(LaggedStart(FadeOut(t1[0][2:7], delta_y_label_1),     # Troca 'y2 - y1' por 'delta y'
                              FadeIn(t2[0][2:4], delta_y_label_2),
                              FadeOut(t1[0][8:13], delta_x_label_1, delta_x_label_1_sr),    # Troca 'x2 - x1' por 'delta x'
                              AnimationGroup(FadeIn(t2[0][5:7],delta_x_label_2), 
                                             ReplacementTransform(t1[0][7], t2[0][4]),
                                             ReplacementTransform(t1[0][0:2], t2[0][0:2])),
                              lag_ratio=0.3))
        self.wait(2)
        self.play(FadeOut(x1_line, y1_line, x1_label, y1_label,
                          x2_line, y2_line, x2_label, y2_label))
        self.wait(2)



# Sobre o sinal e o módulo do coeficiente 'a'
class vid4(Scene):
    def construct(self):
        
        # Retomando elementos
        ax1 = Axes(x_range=[-1, 14], x_length=8,
                   y_range=[-1, 9 ], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        
        A = ValueTracker(0.5)

        def f(x):
            return A.get_value()*(x - 6.5) + 5.25

        gr1 = always_redraw(lambda: ax1.plot(f, x_range=[-1, 13], stroke_width=4, color=GREEN).set_z_index(-2))
        
        aux_1 = Square().scale(10)
        aux_2 = Ellipse(width=2.1, height=1.7).scale(4.5).move_to(ax1.c2p(6.5, 4.25, 0))
        gr1_black_circ = Difference(aux_1, aux_2).set_color(BLACK).set_opacity(1).set_z_index(-1)

        gr1_label = MathTex('y = ax + b', color=BLUE).to_edge(UP, buff=1)
        gr1_label[0][2].set_color(YELLOW)

        self.add(ax1, ax1_x_label, ax1_y_label, gr1, gr1_black_circ)



        X = ValueTracker(5.5)
        DX = ValueTracker(2)

        DX_COLOR = RED
        DY_COLOR = PURPLE


        dot_1 = always_redraw(lambda: Dot().move_to(ax1.c2p(X.get_value(),f(X.get_value()),0)).set_z_index(2))
        dot_2 = always_redraw(lambda: Dot().move_to(ax1.c2p(X.get_value() + DX.get_value(),f(X.get_value() + DX.get_value()),0)).set_z_index(2))


        delta_y_line = always_redraw(lambda: Line(ax1.c2p(X.get_value() + DX.get_value(),f(X.get_value()),0), dot_2).set_color(DY_COLOR))
        delta_x_line = always_redraw(lambda: Line(dot_1, ax1.c2p(X.get_value() + DX.get_value(),f(X.get_value()),0)).set_color(DX_COLOR))

        delta_y_label_2 = always_redraw(lambda: MathTex(r'\Delta y').scale(0.8).next_to(delta_y_line, RIGHT, buff=0.1).set_color(DY_COLOR))
        delta_x_label_2 = always_redraw(lambda: MathTex(r'\Delta x').scale(0.8).next_to(delta_x_line, DOWN, buff=0.1).set_color(DX_COLOR))


        t1 = MathTex(r'a = \frac{y_2 - y_1}{x_2 - x_1}').move_to(gr1_label).shift(DOWN*0.05)
        t2 = MathTex(r'a = \frac{\Delta y}{\Delta x}').move_to(t1).shift(UP*0.1).set_z_index(3)
        t2[0][0].set_color(YELLOW)
        t2[0][2:4].set_color(DY_COLOR)
        t2[0][5:7].set_color(DX_COLOR)

        t3_1 = MathTex(r'=').next_to(t2, RIGHT, buff=0.25).set_z_index(3)
        t3_2 = always_redraw(lambda: MathTex(f'{A.get_value():.1f}').scale(0.9).next_to(t3_1, RIGHT, buff=0.2).set_z_index(3))
        t_sr = SurroundingRectangle(VGroup(t2, t3_2)).set_color(BLACK).set_stroke(width=0).set_opacity(0.8).set_z_index(2)


        self.add(dot_1, dot_2,
                 delta_y_line, delta_x_line,
                 delta_y_label_2, delta_x_label_2,
                 t2, t_sr)
        
        self.play(FadeIn(t3_1, t3_2))
        self.wait(2)
        
        
        self.play(A.animate.set_value(2),
                  DX.animate.set_value(1.5),
                  run_time=5)
        self.wait(2)
        self.play(A.animate.set_value(0.2),
                  DX.animate.set_value(2.5),
                  run_time=5)
        self.wait(2)
        self.play(A.animate.set_value(0),
                  DX.animate.set_value(2.5),
                  run_time=5)
        self.wait(2)
        self.play(A.animate.set_value(-1.5),
                  X.animate.set_value(6),
                  DX.animate.set_value(2),
                  run_time=5)
        self.wait(2)



        # [cena para usar no vid5]
        # Na função do 1o grau a inclinação é a mesma em todo o gráfico
        A.set_value(0.5)
        X.set_value(-1)
        self.wait(2)
        self.play(X.animate.set_value(11), run_time=7)
        self.wait(2)



# Na função x^2 a inclinação é diferente em cada ponto
class vid5(Scene):
    def construct(self):

        ax1 = Axes(x_range=[-5, 5], x_length=8,
                   y_range=[-1, 9], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        def f(x):
            return 0.5*x**2

        gr1 = ax1.plot(f, x_range=[-4.1, 4.1], stroke_width=4, color=BLUE)
        gr1_label = MathTex('y = x^2', color=BLUE).to_edge(UP, buff=1.2).shift(LEFT*4.2)

        # Criando o gráfico
        self.play(LaggedStart(FadeIn(ax1), 
                              FadeIn(ax1_x_label, ax1_y_label), 
                              Create(gr1), 
                              FadeIn(gr1_label), 
                              lag_ratio=0.2))
        self.wait(2)



        # Animação
        X = ValueTracker(-4.1)
        DX = ValueTracker(0.6)

        DX_COLOR = RED
        DY_COLOR = PURPLE


        dot_1 = always_redraw(lambda: Dot().move_to(ax1.c2p(X.get_value(),f(X.get_value()),0)))
        dot_2 = always_redraw(lambda: Dot().move_to(ax1.c2p(X.get_value() + DX.get_value(),f(X.get_value() + DX.get_value()),0)))


        delta_y_line = always_redraw(lambda: Line(ax1.c2p(X.get_value() + DX.get_value(), f(X.get_value()), 0), dot_2).set_color(DY_COLOR) if X.get_value() > 0
                                        else Line(dot_1, ax1.c2p(X.get_value(), f(X.get_value() + DX.get_value()), 0)).set_color(DY_COLOR))
        
        delta_x_line = always_redraw(lambda: Line(dot_1, ax1.c2p(X.get_value() + DX.get_value(),f(X.get_value()),0)).set_color(DX_COLOR) if X.get_value() > 0
                                        else Line(ax1.c2p(X.get_value(),f(X.get_value() + DX.get_value()),0), dot_2).set_color(DX_COLOR))

        delta_y_label_2 = always_redraw(lambda: MathTex(r'\Delta y').scale(0.8).next_to(delta_y_line, RIGHT, buff=0.1).set_color(DY_COLOR) if X.get_value() > 0
                                        else MathTex(r'\Delta y').scale(0.8).next_to(delta_y_line, LEFT, buff=0.1).set_color(DY_COLOR))
        delta_x_label_2 = always_redraw(lambda: MathTex(r'\Delta x').scale(0.8).next_to(delta_x_line, DOWN, buff=0.1).set_color(DX_COLOR))

        self.add(dot_1, dot_2, delta_y_line, delta_x_line, delta_y_label_2, delta_x_label_2)
        self.play(X.animate.set_value(4.1 - 0.6), run_time=7)
        self.wait(2)
        self.play(FadeOut(dot_1, dot_2, delta_y_line, delta_x_line, delta_y_label_2, delta_x_label_2))
        self.wait(2)



# Reta tangente no ponto (2,2^2) da função y = x^2
class vid6(MovingCameraScene):
    def construct(self):
        
        # Retomando elementos
        ax1 = Axes(x_range=[-5, 5], x_length=8,
                   y_range=[-1, 9], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        def f(x):
            return 0.5*x**2

        gr1 = ax1.plot(f, x_range=[-4.1, 4.1], stroke_width=4, color=BLUE)
        gr1_label = MathTex('y = x^2', color=BLUE).to_edge(UP, buff=1.2).shift(LEFT*4.2)

        self.add(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label)



        # Escolhemos o ponto (2,2^2)
        DOT_1_COLOR = WHITE

        dot_1 = Dot(ax1.c2p(2,f(2),0)).set_color(DOT_1_COLOR).set_z_index(5)
        dot_1_label_aux = MathTex(r'(x,x^2)').set_color(DOT_1_COLOR).scale(0.8).next_to(dot_1, UL, buff=0.05)
        dot_1_label = MathTex(r'(2,2^2)').set_color(DOT_1_COLOR).scale(0.8).move_to(dot_1_label_aux)

        self.play(GrowFromCenter(dot_1))
        self.wait(2)
        self.play(FadeIn(dot_1_label_aux))
        self.wait(2)
        self.play(ReplacementTransform(dot_1_label_aux, dot_1_label))
        self.wait(2)



        # Aparece a reta tangente
        tangent_line = ax1.plot(lambda x: 0.5*4*(x-2) + f(2), 
                                x_range=[0.1, 3.9], stroke_width=4, color=GREEN)
        tangent_line_label = MathTex('y = ax + b', color=GREEN).next_to(tangent_line, RIGHT, buff=0.2).shift(UP*2.35)

        indicative_arrow_1 = Arrow(ORIGIN, UP*1.5).set_color(GRAY).rotate(30*DEGREES).next_to(tangent_line_label, DOWN, buff=0.1).shift(RIGHT*0.15)

        self.play(FadeIn(VGroup(tangent_line, tangent_line_label), shift=UL), run_time=1.5)
        self.wait(2)
        self.play(FadeIn(indicative_arrow_1),
                  tangent_line_label[0][2].animate.set_color(YELLOW))
        self.wait(2)
        self.play(FadeOut(indicative_arrow_1),
                  tangent_line_label[0][2].animate.set_color(GREEN))
        self.wait(2)



        # Retas que não são a tangente
        not_tangent_line_1 = Line(stroke_width=2, color=WHITE).scale(2.7).set_opacity(0.5).move_to(ax1.c2p(2,f(2),0)).rotate((48.5 + 8 + 7.5)*DEGREES)
        not_tangent_line_2 = not_tangent_line_1.copy().rotate(15*DEGREES)
        not_tangent_line_3 = not_tangent_line_2.copy().rotate(15*DEGREES)
        not_tangent_line_4 = not_tangent_line_3.copy().rotate(15*DEGREES)
        not_tangent_line_5 = not_tangent_line_4.copy().rotate(15*DEGREES)
        not_tangent_line_6 = not_tangent_line_5.copy().rotate(15*DEGREES)
        not_tangent_line_7 = not_tangent_line_6.copy().rotate(15*DEGREES)
        not_tangent_line_8 = not_tangent_line_7.copy().rotate(15*DEGREES)
        not_tangent_line_9 = not_tangent_line_8.copy().rotate(15*DEGREES)
        not_tangent_line_10 = not_tangent_line_9.copy().rotate(15*DEGREES)
        not_tangent_line_11 = not_tangent_line_10.copy().rotate(15*DEGREES)
        not_tangent_line_12 = not_tangent_line_11.copy().rotate(15*DEGREES)

        self.play(LaggedStart(GrowFromCenter(not_tangent_line_1),
                              GrowFromCenter(not_tangent_line_2),
                              GrowFromCenter(not_tangent_line_3),
                              GrowFromCenter(not_tangent_line_4),
                              GrowFromCenter(not_tangent_line_5),
                              GrowFromCenter(not_tangent_line_6),
                              GrowFromCenter(not_tangent_line_7),
                              GrowFromCenter(not_tangent_line_8),
                              GrowFromCenter(not_tangent_line_9),
                              GrowFromCenter(not_tangent_line_10),
                              GrowFromCenter(not_tangent_line_11),
                              GrowFromCenter(not_tangent_line_12),
                              lag_ratio=0.05))
        self.wait(2)
        self.play(FadeOut(not_tangent_line_1, not_tangent_line_2, 
                          not_tangent_line_3, not_tangent_line_4,
                          not_tangent_line_5, not_tangent_line_6, 
                          not_tangent_line_7, not_tangent_line_8,
                          not_tangent_line_9, not_tangent_line_10,
                          not_tangent_line_11, not_tangent_line_12))
        self.wait(2)


        t1 = Tex(r'\it ``reta tangente"', color=GREEN).move_to(tangent_line_label).shift(DOWN*1.5)
        t2 = Tex(r'\it ``tocar"', color=GRAY).scale(0.9).next_to(t1[0][4:], DOWN, buff=0.2)
        sq_aux_1 = Rectangle(width=4, height=3, stroke_width=2).scale(0.5).move_to(ax1.c2p(2,f(2),0)).set_stroke(opacity=0.5)
        self.play(FadeIn(t1))
        self.wait(2)
        self.play(Create(sq_aux_1))
        self.wait(2)

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.2).move_to(ax1.c2p(2,f(2),0)),
                  gr1.animate.set_stroke(width=2),
                  tangent_line.animate.set_stroke(width=2).shift(DR*0.01),
                  sq_aux_1.animate.scale(0.5),
                  run_time=10)
        self.wait(2)
        self.remove(tangent_line_label)
        self.play(self.camera.frame.animate.restore(),
                  gr1.animate.set_stroke(width=5),
                  tangent_line.animate.set_stroke(width=5).shift(UL*0.01),
                  run_time=2)
        self.wait(2)
        self.play(FadeIn(t2))
        self.wait(2)
        self.play(FadeOut(tangent_line))
        tangent_line.rotate(45*DEGREES)
        self.play(Create(tangent_line))
        self.play(FadeOut(tangent_line))
        tangent_line.rotate(-45*DEGREES)
        self.play(FadeIn(tangent_line, shift=UL), run_time=1.5)
        self.wait(2)
        self.play(Uncreate(sq_aux_1))
        self.wait(2)



# Calculando a inclinação da reta tangente no ponto (2,2^2) da função y = x^2
class vid7(MovingCameraScene):
    def construct(self):
        
        # Retomando elementos
        ax1 = Axes(x_range=[-5, 5], x_length=8,
                   y_range=[-1, 9], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        def f(x):
            return 0.5*x**2

        gr1 = ax1.plot(f, x_range=[-4.1, 4.1], stroke_width=4, color=BLUE)
        gr1_label = MathTex('y = x^2', color=BLUE).to_edge(UP, buff=1.2).shift(LEFT*4.2)

        self.add(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label)



        DOT_1_COLOR = WHITE
        DOT_2_COLOR = GRAY

        dot_1 = Dot(ax1.c2p(2,f(2),0)).set_color(DOT_1_COLOR).set_z_index(6)
        dot_1_label_aux = MathTex(r'(x,x^2)').set_color(DOT_1_COLOR).scale(0.8).next_to(dot_1, UL, buff=0.05)
        dot_1_label = MathTex(r'(2,2^2)').set_color(DOT_1_COLOR).scale(0.8).move_to(dot_1_label_aux).set_z_index(3)
        dot_1_label_sr = SurroundingRectangle(dot_1_label, color=BLACK, stroke_width=0, fill_opacity=0.8).set_z_index(2)

        tangent_line = ax1.plot(lambda x: 0.5*4*(x-2) + f(2), 
                                x_range=[0.1, 3.9], stroke_width=4, color=GREEN).set_z_index(2)
        tangent_line_label = MathTex('y = ax + b', color=GREEN).next_to(tangent_line, RIGHT, buff=0.2).shift(UP*2.2)

        self.add(dot_1, dot_1_label, dot_1_label_sr, tangent_line)



        # Se fizermos 'delta y/delta x' vamos ter '0/0'
        DX_COLOR = RED
        DY_COLOR = PURPLE

        t1 = MathTex(r'\frac{\Delta y}{\Delta x} = \frac{0}{0}').shift(RIGHT*5+DOWN*1)
        VGroup(t1[0][0:2], t1[0][6]).set_color(DY_COLOR)
        VGroup(t1[0][3:5], t1[0][8]).set_color(DX_COLOR)

        self.play(FadeIn(t1[0][0:5]))
        self.wait(2)
        self.play(LaggedStart(FadeIn(t1[0][5]), 
                              FadeIn(t1[0][6:]),
                              lag_ratio=0.3))
        self.wait(2)
        self.play(FadeOut(t1))
        self.wait(2)



        # Vamos aproximar a tangente por uma secante
        X = ValueTracker(2)
        DX = ValueTracker(2)
        
        dot_2 = always_redraw(lambda: Dot(ax1.c2p(X.get_value() + DX.get_value(),f(X.get_value() + DX.get_value()),0)).set_color(DOT_2_COLOR).set_z_index(5))
        
        SECANT_LINE_LENGTH = 6.5
        secant_line = always_redraw(lambda: ax1.plot(lambda x: ((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())*(x-X.get_value()) + f(X.get_value()), 
                                                     x_range=[X.get_value() + 0.5*DX.get_value() - (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5, X.get_value()  + 0.5*DX.get_value() + (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5], 
                                                     stroke_width=4, 
                                                     color=GRAY))
        
        self.play(Create(secant_line), 
                  GrowFromCenter(dot_2),
                  tangent_line.animate.set_opacity(0.3))
        self.wait(2)
        self.play(LaggedStart(Flash(dot_1, num_lines=8),
                              Flash(dot_2, num_lines=8),
                              lag_ratio=0.2))
        self.wait(2)



        # Coordenadas do segundo ponto
        dot_2_label = always_redraw(lambda: MathTex(r'(2 + h,(2 + h)^2)').set_color(DOT_2_COLOR).scale(0.7).next_to(dot_2, UL, buff=0.05).shift(UP*0.05))

            # Coordenada x: 2 + h
        x1_line = DashedLine(ax1.c2p(X.get_value(),f(X.get_value()),0), ax1.c2p(X.get_value(),0,0), color=GRAY)
        
        X2_DX = ValueTracker(0)
        x2_line = always_redraw(lambda: DashedLine(ax1.c2p(X.get_value() + X2_DX.get_value(),f(X.get_value() + X2_DX.get_value()),0), ax1.c2p(X.get_value() + X2_DX.get_value(),0,0), color=GRAY))
        x1_label = MathTex('2', color=GRAY).scale(0.8).next_to(ax1.c2p(X.get_value(),0,0), DOWN, buff=0.15)
        x2_label = MathTex('2 + h', color=GRAY).scale(0.8).next_to(ax1.c2p(X.get_value() + DX.get_value(),0,0), DOWN, buff=0.15)

        h_brace = always_redraw(lambda: Brace(Line(ax1.c2p(X.get_value(),0,0), ax1.c2p(X.get_value() + DX.get_value(),0,0)), UP, buff=0, color=GRAY))
        h_label = always_redraw(lambda: MathTex('h', color=GRAY).scale(0.8).next_to(h_brace, UP, buff=0.1)).set_z_index(3)
        h_label_sr = always_redraw(lambda: SurroundingRectangle(h_label, color=BLACK, stroke_width=0, fill_opacity=0.8).set_z_index(2))

        self.play(FadeIn(dot_2_label[0][0], dot_2_label[0][4], dot_2_label[0][11]))
        self.wait(2)
        self.play(LaggedStart(FadeIn(x1_line),
                              FadeIn(x1_label),
                              lag_ratio=0.2))
        self.wait(2)
        self.add(x2_line)
        self.play(X2_DX.animate.set_value(DX.get_value()), 
                  GrowFromPoint(x2_label[0][1:3], x1_label.get_right()),
                  TransformMatchingShapes(x1_label.copy(), x2_label[0][0]),
                  GrowFromPoint(VGroup(h_brace, h_label), h_brace.get_left()),
                  FadeIn(dot_2_label[0][1:4]),
                  run_time=2)
        self.add(h_label_sr)
        self.wait(2)

                # Corrigindo o objeto x2_line
        x2_line = always_redraw(lambda: DashedLine(ax1.c2p(X.get_value() + DX.get_value(),f(X.get_value() + X2_DX.get_value()),0), ax1.c2p(X.get_value() + DX.get_value(),0,0), color=GRAY))
        


            # Coordenada y: (2 + h)^2
        y2_line = always_redraw(lambda: DashedLine(ax1.c2p(X.get_value() + DX.get_value(),f(X.get_value() + X2_DX.get_value()),0), ax1.c2p(0,f(X.get_value() + DX.get_value()),0), color=GRAY))
        y2_label = MathTex('(2 + h)^2', color=GRAY).scale(0.75).next_to(ax1.c2p(0,f(X.get_value() + DX.get_value()),0), LEFT, buff=0.15)
      
        self.play(LaggedStart(FadeIn(y2_line),
                              FadeIn(y2_label, dot_2_label[0][5:11]),
                              lag_ratio=0.2))
        self.wait(2)



        # O nome dessa reta é secante
        t2 = Tex(r'\it ``reta secante"', color=GRAY).shift(UP*1.8+RIGHT*5)
        t3 = Tex(r'\it ``cortar"', color=GRAY).set_opacity(0.7).scale(0.9).next_to(t2[0][4:], DOWN, buff=0.3)
        
        self.play(FadeIn(t2))
        self.wait(2)
        self.play(FadeIn(t3))
        self.wait(2)
        self.play(FadeOut(t2, t3))
        self.wait(2)



        # Calculando a inclinação da reta secante
        t4 = MathTex(r'\lim_{h \to 0}',r'\frac{\Delta y}{\Delta x}','=',r'\frac{(2 + h)^2 - 2^2}{h}').shift(RIGHT*7+UP*1)
        t4[0].shift(UP*0.15)
        VGroup(t4[1][0:2], t4[3][0:9]).set_color(DY_COLOR)
        VGroup(t4[0][3], t4[1][3:5], t4[3][3], t4[3][10]).set_color(DX_COLOR)

        delta_y_line = always_redraw(lambda: Line(ax1.c2p(X.get_value() + DX.get_value(), f(X.get_value()), 0), ax1.c2p(X.get_value() + DX.get_value(), f(X.get_value() + DX.get_value()), 0), color=DY_COLOR))
        delta_x_line = always_redraw(lambda: Line(ax1.c2p(X.get_value(), f(X.get_value()), 0), ax1.c2p(X.get_value() + DX.get_value(), f(X.get_value()), 0), color=DX_COLOR))

        delta_y_label = always_redraw(lambda: MathTex(r'\Delta y', color=DY_COLOR).scale(DX.get_value()/2).next_to(delta_y_line, RIGHT, buff=0.1))
        delta_x_label = always_redraw(lambda: MathTex(r'\Delta x', color=DX_COLOR).scale(DX.get_value()/2).next_to(delta_x_line, UP, buff=0.1))

        self.play(self.camera.frame.animate.shift(RIGHT*4),
                  FadeOut(x2_label, y2_line, y2_label),
                  FadeIn(t4[1:3], delta_y_line, delta_y_label, delta_x_line, delta_x_label),
                  run_time=2)
        self.wait(2)
        self.play(FadeIn(t4[3][0:6], t4[3][9]))
        self.wait(2)
        self.play(FadeIn(t4[3][6:9]))
        self.wait(2)
        self.play(FadeIn(t4[3][10]))
        self.wait(2)



        t5 = MathTex(r'\lim_{h \to 0}',r'\frac{\Delta y}{\Delta x}','=',r'\frac{2^2 + 4h + h^2 - 2^2}{h}').move_to(t4, aligned_edge=DL)
        t5[0].shift(UP*0.15)
        VGroup(t5[1][0:2], t5[3][0:11]).set_color(DY_COLOR)
        VGroup(t5[0][3], t5[1][3:5], t5[3][4], t5[3][6:8], t5[3][12]).set_color(DX_COLOR)

        self.play(LaggedStart(FadeOut(t4[3][0:6]),
                              ReplacementTransform(t4[3][6:11], t5[3][8:13]),
                              FadeIn(t5[3][0:8]),
                              lag_ratio=0.3))
        self.wait(2)



        t6 = MathTex(r'\lim_{h \to 0}',r'\frac{\Delta y}{\Delta x}','=',r'\frac{4h + h^2}{h}').move_to(t4, aligned_edge=DL)
        t6[0].shift(UP*0.15)
        VGroup(t6[1][0:2], t6[3][0:5]).set_color(DY_COLOR)
        VGroup(t6[0][3], t6[1][3:5], t6[3][1], t6[3][3:5], t6[3][6]).set_color(DX_COLOR)

        
        t7 = MathTex(r'\lim_{h \to 0}',r'\frac{\Delta y}{\Delta x}','=',r'\frac{h(4 + h)}{h}').move_to(t4, aligned_edge=DL)
        t7[0].shift(UP*0.15)
        VGroup(t7[1][0:2], t7[3][0:6]).set_color(DY_COLOR)
        VGroup(t7[0][3], t7[1][3:5], t7[3][0], t7[3][4], t7[3][7]).set_color(DX_COLOR)

        red_line1 = Line(UP*0.2, DOWN*0.2, color=RED, stroke_width=4).scale(2).rotate(-50*DEGREES).move_to(t5[3][0:2])
        red_line2 = red_line1.copy().move_to(t5[3][9:11])
        self.play(Create(red_line1), Create(red_line2))
        self.play(LaggedStart(FadeOut(t5[3][0:3], t5[3][8:11], red_line1, red_line2),
                              AnimationGroup(TransformMatchingShapes(t5[3][3:8], t6[3][0:5]),
                                             ReplacementTransform(VGroup(t5[3][11], t5[3][12]), t7[3][6:])),
                              lag_ratio=0.5))
        self.wait(2)
        self.play(LaggedStart(FadeOut(t6[3][0:5]),
                              FadeIn(t7[3][0:6]),
                              lag_ratio=0.5))
        self.wait(2)



        t8 = MathTex(r'\lim_{h \to 0}',r'\frac{\Delta y}{\Delta x}','=',r'\lim_{h \to 0} 4 + h','= 4').move_to(t4, aligned_edge=DL)
        VGroup(t8[0], t8[3][0:6]).shift(UP*0.15)
        VGroup(t8[1][0:2], t8[3][6:8]).set_color(DY_COLOR)
        VGroup(t8[0][3], t8[1][3:5], t8[3][3], t8[3][8]).set_color(DX_COLOR)
        t8[3][6:].shift(LEFT*0.94)
        t8[4].shift(RIGHT*0.1)
        

        red_line3 = red_line1.copy().scale(0.9).move_to(t7[3][0])
        red_line4 = red_line1.copy().scale(0.9).move_to(t7[3][7])
        self.play(Create(red_line3), Create(red_line4))
        self.play(LaggedStart(FadeOut(t7[3][0:2], t7[3][5:8], red_line3, red_line4),
                              ReplacementTransform(t7[3][2:5], t8[3][6:]),
                              lag_ratio=0.5))
        self.wait(2)



        # Quanto menor for o 'h', melhor será a aproximação
        self.play(Wiggle(secant_line, n_wiggles=4))
        self.wait(2)
        self.play(tangent_line.animate.set_opacity(1),
                  Wiggle(tangent_line, n_wiggles=4))
        self.wait(2)



            # Diminuindo 'h'
        self.play(DX.animate.set_value(1), X2_DX.animate.set_value(1), run_time=2)
        self.wait(2)
        self.play(DX.animate.set_value(0.5), X2_DX.animate.set_value(0.5), run_time=2)
        self.wait(2)
        self.play(DX.animate.set_value(0.05), X2_DX.animate.set_value(0.05), run_time=2)
        self.wait(2)
        DX.set_value(2)
        self.play(DX.animate.set_value(0.005), X2_DX.animate.set_value(0.005), run_time=5)
        self.wait(2)
        self.remove(delta_y_label, delta_x_label)

            # Calculando o limite para 'h' -> 0
        self.play(LaggedStart(t8[3][6:].animate.shift(RIGHT*0.97),
                              FadeIn(t4[0][0:3], t8[3][0:3]),
                              lag_ratio=0.4),
                              run_time=1.5)
        self.wait(2)
        self.play(LaggedStart(FadeIn(t4[0][3], t8[3][3]),
                              FadeIn(t4[0][4], t8[3][4]),
                              FadeIn(t4[0][5], t8[3][5]),
                              lag_ratio=0.1))
        self.wait(2)
        self.play(FadeIn(t8[4]))
        self.wait(2)

        # Essa é a inclinação/taxa de variação instantânea da função em (2,2^2)
        self.remove(secant_line)
        self.play(Wiggle(tangent_line, n_wiggles=4))
        self.wait(2)


        t9 = Tex(r'taxa de variação \par instantânea em $(2,2^2)$', color=GRAY).scale(0.8).next_to(t8, DOWN, buff=1).shift(RIGHT*1+UP*0.5)
        self.play(FadeIn(t9))
        self.wait(2)


        dx_line = Line(ax1.c2p(2,2**2 - 2,0), ax1.c2p(2 + 0.2,2**2 - 2,0), color=YELLOW).set_stroke(width=3)
        dx_line_label = MathTex(r'dx', color=YELLOW).scale(0.25).next_to(dx_line, DOWN, buff=0.05)

        dy_line = Line(ax1.c2p(2 + 0.2,2**2 - 2,0), ax1.c2p(2 + 0.2,(2 + 0.2)**2 - 2,0), color=PURPLE).set_stroke(width=3).shift(DOWN*0.01+LEFT*0).scale(1.01)
        dy_line_label = MathTex(r'dy', color=PURPLE).scale(0.25).next_to(dy_line, RIGHT, buff=0.05)

        dy_aux_1 = dx_line.copy().scale(0.88).rotate(90*DEGREES).move_to(dy_line, aligned_edge=DOWN)
        dy_aux_2 = dy_aux_1.copy().scale(0.88).next_to(dy_aux_1, UP, buff=0)
        dy_aux_3 = dy_aux_1.copy().scale(0.88).next_to(dy_aux_2, UP, buff=0)
        dy_aux_4 = dy_aux_1.copy().scale(0.88).next_to(dy_aux_3, UP, buff=0)

        gr1_aux_1 = ax1.plot(lambda x: x**2 - 2, x_range=[-4.1, 4.1], stroke_width=3, color=BLUE)
        gr1_aux_2 = gr1.copy()

        dot_1.save_state()
        self.camera.frame.save_state()
        self.play(LaggedStart(FadeOut(dot_2, secant_line, tangent_line, h_label, h_label_sr),
                              AnimationGroup(self.camera.frame.animate.scale(0.25).move_to(ax1.c2p(2,f(2.1),0)),
                                             dot_1.animate.scale(0.5)),
                  ReplacementTransform(gr1, gr1_aux_1),
                  lag_ratio=0.25),
                  run_time=5)
        self.wait(2)
        self.play(Create(dx_line), 
                  FadeIn(dx_line_label))
        self.play(VGroup(dx_line, dx_line_label).animate.set_color(DX_COLOR))
        self.wait(2)
        self.play(Create(dy_line),
                  FadeIn(dy_line_label))
        self.wait(2)
        self.add(dy_aux_1)
        self.wait(2)
        self.add(dy_aux_2).remove(dy_aux_1)
        self.wait(2)
        self.add(dy_aux_3).remove(dy_aux_2)
        self.wait(2)
        self.add(dy_aux_4).remove(dy_aux_3)
        self.wait(2)
        self.remove(dy_aux_4)
        self.wait(2)
        self.remove(t9)
        self.play(LaggedStart(FadeOut(dx_line, dx_line_label, 
                                      dy_line, dy_line_label),
                              ReplacementTransform(gr1_aux_1, gr1_aux_2),
                              AnimationGroup(self.camera.frame.animate.restore(),
                                             dot_1.animate.restore()),
                              FadeIn(tangent_line, h_label, h_label_sr),
                              lag_ratio=0.3),
                  run_time=5)
        self.wait(2)
        self.add(secant_line)
        self.wait(2)
        DX.set_value(2)
        self.play(DX.animate.set_value(0.005), run_time=5)
        self.wait(2)









        # Sobre a notação dy/dx
        t10 = MathTex(r'\frac{dy}{dx}').move_to(t8[1]).scale(1).shift(DOWN*1.8+RIGHT*1.5)
        t10[0][0:2].set_color(DY_COLOR)
        t10[0][3:5].set_color(DX_COLOR)

        t10_brace = Brace(t8[0:2], DOWN, color=GRAY)

        self.play(GrowFromCenter(t10))
        self.wait(2)
        self.play(FadeIn(t10_brace),
                  t10.animate.shift(LEFT*2), 
                  run_time=1.5)
        self.wait(2)
        self.play(t10[0][0].animate.set_color(YELLOW),
                  t10[0][3].animate.set_color(YELLOW))
        self.wait(2)
        self.play(t8[1][0].animate.set_color(YELLOW),
                  t8[1][3].animate.set_color(YELLOW))
        self.wait(2)
        self.play(t10[0][0].animate.set_color(DY_COLOR),
                  t10[0][3].animate.set_color(DX_COLOR),
                  t8[1][0].animate.set_color(DY_COLOR),
                  t8[1][3].animate.set_color(DX_COLOR))
        self.wait(2)
        self.play(Indicate(t8[1][0]),
                  Indicate(t8[1][3]))
        self.wait(2)
        self.play(Indicate(t10[0][0]),
                  Indicate(t10[0][3]))
        self.wait(2)
        self.play(self.camera.frame.animate.shift(LEFT*4), run_time=2)
        self.wait(2)



# A derivada de de 'x^2' é '2x'
class vid8(MovingCameraScene):
    def construct(self):
        
        # Retomando elementos
        ax1 = Axes(x_range=[-5, 5], x_length=8,
                   y_range=[-1, 9], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        def f(x):
            return 0.5*x**2
        
        def f_prime(x):
            return 0.5*2*x
        
        X = ValueTracker(2)

        gr1 = ax1.plot(f, x_range=[-4.1, 4.1], stroke_width=4, color=BLUE)
        gr1_label = MathTex('y = x^2', color=BLUE).to_edge(UP, buff=1.2).shift(LEFT*4.2)

        self.add(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label)



        DOT_1_COLOR = WHITE
        DOT_2_COLOR = GRAY

        dot_1 = always_redraw(lambda: Dot(ax1.c2p(X.get_value(),f(X.get_value()),0)).set_color(DOT_1_COLOR).set_z_index(6))
        
        TANGENT_LINE_LENGTH = 6.5
        DX = ValueTracker(0.01)
        tangent_line = always_redraw(lambda: ax1.plot(lambda x: f_prime(X.get_value())*(x - X.get_value()) + f(X.get_value()), 
                                x_range=[X.get_value() + 0.5*DX.get_value() - (TANGENT_LINE_LENGTH**2/(4 + 4*abs((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5, X.get_value()  + 0.5*DX.get_value() + (TANGENT_LINE_LENGTH**2/(4 + 4*abs((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5], 
                                stroke_width=4, 
                                color=GREEN).set_z_index(2))

        self.add(dot_1, tangent_line)



        x1_line = always_redraw(lambda: DashedLine(ax1.c2p(X.get_value(),f(X.get_value()),0), ax1.c2p(X.get_value(),0,0), color=GRAY))
        x1_label = always_redraw(lambda: MathTex(f'{X.get_value():.1f}', color=GRAY).scale(0.8).next_to(ax1.c2p(X.get_value(),0,0), DOWN, buff=0.15))
        
        self.add(x1_line, x1_label)



        self.camera.frame.shift(RIGHT*4)



        # f'(2) = 4
        DX_COLOR = RED
        DY_COLOR = PURPLE
        
        t_dy_dx = always_redraw(lambda: MathTex(r'\frac{dy}{dx}(',f'{X.get_value():.1f}',') =',f'{2*f_prime(X.get_value()):.1f}').scale(0.9).next_to(dot_1, DR, buff=0.2).shift(UP*0.2).set_z_index(11))
        t_dy_dx_aux1 = always_redraw(lambda: MathTex('dy', color=DY_COLOR).scale(0.9).move_to(t_dy_dx[0][0:2]))
        t_dy_dx_aux2 = always_redraw(lambda: MathTex('dx', color=DX_COLOR).scale(0.9).move_to(t_dy_dx[0][3:5]))
        
        self.add(t_dy_dx, t_dy_dx_aux1, t_dy_dx_aux2)

        self.play(self.camera.frame.animate.shift(LEFT*4), run_time=2)
        self.wait(2)
        

        # f'(3) = 6
        self.play(X.animate.set_value(3), run_time=1.5)
        self.wait(2)


        # f'(4) = 8
        self.play(X.animate.set_value(4), run_time=1.5)
        self.wait(2)



        # Calculando a derivada num ponto genérico
        self.play(FadeOut(t_dy_dx, t_dy_dx_aux1, t_dy_dx_aux2, 
                          x1_line, x1_label))
        self.wait(2)



        X.set_value(2)
        DX_2 = ValueTracker(2)

        x1_label_2 = MathTex(f'x', color=GRAY).scale(0.9).next_to(ax1.c2p(X.get_value(),0,0), DOWN, buff=0.15)
        
        x2_line = always_redraw(lambda: DashedLine(ax1.c2p(X.get_value() + DX_2.get_value(),f(X.get_value() + DX_2.get_value()),0), ax1.c2p(X.get_value() + DX_2.get_value(),0,0), color=GRAY))
        x2_label = always_redraw(lambda: MathTex(f'x + h', color=GRAY).scale(0.9).next_to(ax1.c2p(X.get_value() + DX_2.get_value(),0,0), DOWN, buff=0.15))
        
        dot_1_label = always_redraw(lambda: MathTex(r'(x,x^2)').set_color(DOT_1_COLOR).scale(0.8).next_to(dot_1, UL, buff=0.05).set_z_index(3))
        dot_1_label_sr = SurroundingRectangle(dot_1_label, color=BLACK, stroke_width=0, fill_opacity=0.8).set_z_index(2)
        
        dot_2 = always_redraw(lambda: Dot(ax1.c2p(X.get_value() + DX_2.get_value(),f(X.get_value() + DX_2.get_value()),0)).set_color(DOT_2_COLOR).set_z_index(5))
        dot_2_label = always_redraw(lambda: MathTex(r'(x + h,(x + h)^2)').set_color(DOT_2_COLOR).scale(0.7).next_to(dot_2, UL, buff=0.05).shift(UP*0.05))

        SECANT_LINE_LENGTH = 6.5
        secant_line = always_redraw(lambda: ax1.plot(lambda x: ((f(X.get_value() + DX_2.get_value()) - f(X.get_value()))/DX_2.get_value())*(x-X.get_value()) + f(X.get_value()), 
                                                     x_range=[X.get_value() + 0.5*DX_2.get_value() - (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX_2.get_value()) - f(X.get_value()))/DX_2.get_value())))**0.5, X.get_value()  + 0.5*DX_2.get_value() + (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX_2.get_value()) - f(X.get_value()))/DX_2.get_value())))**0.5], 
                                                     stroke_width=4, 
                                                     color=GRAY))
        
        self.wait(2)
        self.play(X.animate.set_value(2),
                  tangent_line.animate.set_opacity(0.3),
                  FadeIn(dot_1),
                  FadeIn(x1_line, x1_label_2, dot_1_label))
        self.wait(2)
        self.play(FadeIn(dot_2, x2_line, x2_label, dot_2_label),
                  Create(secant_line))
        self.wait(2)



        # Fazendo a conta
        t4 = MathTex(r'\lim_{h \to 0}',r'\frac{\Delta y}{\Delta x}',r'= \lim_{h \to 0}',r'\frac{(x + h)^2 - x^2}{h}').shift(RIGHT*7+UP*1)
        VGroup(t4[0], t4[2][0:7]).shift(UP*0.15)
        VGroup(t4[1][0:2], t4[3][0:9]).set_color(DY_COLOR)
        VGroup(t4[0][3], t4[1][3:5], t4[2][4], t4[3][3], t4[3][10]).set_color(DX_COLOR)
        
        t5 = MathTex(r'\lim_{h \to 0}',r'\frac{\Delta y}{\Delta x}',r'= \lim_{h \to 0}',r'\frac{x^2 + 2xh + h^2 - x^2}{h}').move_to(t4, aligned_edge=DL)
        VGroup(t5[0], t5[2][0:7]).shift(UP*0.15)
        VGroup(t5[1][0:2], t5[3][0:12]).set_color(DY_COLOR)
        VGroup(t5[0][3], t5[1][3:5], t5[3][5], t5[3][7:9], t5[3][13]).set_color(DX_COLOR)

        t6 = MathTex(r'\lim_{h \to 0}',r'\frac{\Delta y}{\Delta x}',r'= \lim_{h \to 0}',r'\frac{2xh + h^2}{h}').move_to(t4, aligned_edge=DL)
        VGroup(t6[0], t6[2][0:7]).shift(UP*0.15)
        VGroup(t6[1][0:2], t6[3][0:5]).set_color(DY_COLOR)
        VGroup(t6[0][3], t6[1][3:5], t6[3][2], t6[3][4:6], t6[3][7]).set_color(DX_COLOR)
  
        t7 = MathTex(r'\lim_{h \to 0}',r'\frac{\Delta y}{\Delta x}',r'= \lim_{h \to 0}',r'\frac{h(2x + h)}{h}').move_to(t4, aligned_edge=DL)
        VGroup(t7[0], t7[2][0:7]).shift(UP*0.15)
        VGroup(t7[1][0:2], t7[3][0:7]).set_color(DY_COLOR)
        VGroup(t7[0][3], t7[1][3:5], t7[3][0], t7[3][5], t7[3][8]).set_color(DX_COLOR)

        t8 = MathTex(r'\lim_{h \to 0}',r'\frac{\Delta y}{\Delta x}',r'= \lim_{h \to 0}',r'2x + h','= 2x').move_to(t4, aligned_edge=DL)
        VGroup(t8[0], t8[2][0:7]).shift(UP*0.15)
        VGroup(t8[1][0:2], t8[3][6:8]).set_color(DY_COLOR)
        VGroup(t8[0][3], t8[1][3:5], t8[3][3]).set_color(DX_COLOR)
        t8[3:].shift(RIGHT*0.1)
        
        self.play(self.camera.frame.animate.shift(RIGHT*5), run_time=2)
        self.play(FadeIn(t4))
        self.wait(0)
        self.play(t4[3].animate.shift(UP*1.5), 
                  FadeIn(t5[3], shift=UP*1.5))
        self.wait(0)
        self.play(t5[3].animate.shift(UP*1.5),
                  FadeOut(t4[3], shift=UP*1.5), 
                  FadeIn(t6[3], shift=UP*1.5))
        self.wait(0)
        self.play(t6[3].animate.shift(UP*1.5),
                  FadeOut(t5[3], shift=UP*1.5), 
                  FadeIn(t7[3], shift=UP*1.5))
        self.wait(0)
        self.play(t7[3].animate.shift(UP*1.5),
                  FadeOut(t6[3], shift=UP*1.5), 
                  FadeIn(t8[3], shift=UP*1.5))
        self.wait(0)
        self.play(FadeOut(t7[3]))
        self.wait(0)
        self.play(FadeIn(t8[4]))
        self.wait(2)
        self.play(FadeOut(t4[0:3], t8[3:]))
        self.wait(2)


        # Transição para a próxima cena
        self.remove(gr1_label)
        gr1_label_2 = gr1_label.copy().next_to(ax1, UP, buff=1)
        self.play(FadeOut(secant_line, tangent_line,
                          x1_line, x1_label_2, 
                          dot_1, dot_1_label,
                          dot_2, x2_line, x2_label, dot_2_label),
                  FadeIn(gr1_label_2),
                  self.camera.frame.animate.scale(1.3).shift(LEFT*0.5+UP*0.5))
        self.wait(2)


        X = ValueTracker(-4.1)

        tangent_line = always_redraw(lambda: Line((0,0,0), (5,0,0), stroke_width=4, color=GREEN).rotate(np.arctan(f_prime(X.get_value()) * 0.75)).move_to(dot_1))

        self.add(dot_1, tangent_line, 
                 t_dy_dx, t_dy_dx_aux1, t_dy_dx_aux2)
        self.wait(2)
        self.play(X.animate.set_value(4), run_time=5)
        self.wait(2)



        # Aparece o gráfico da função derivada
        ax2 = Axes(x_range=[-5, 5], x_length=8,
                   y_range=[-5, 5], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).next_to(ax1, RIGHT, buff=1)
        ax2_x_label = MathTex('x').set_color(GRAY).next_to(ax2.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax2_y_label = MathTex('y').set_color(GRAY).next_to(ax2.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        gr2 = ax2.plot(f_prime, x_range=[-4.1, 4.1], stroke_width=4, color=BLUE)
        gr2_label = MathTex(r'\frac{dy}{dx} = 2x', color=BLUE).next_to(ax2, UP, buff=1)

        dot_gr2 = always_redraw(lambda: Dot(ax2.c2p(X.get_value(),f_prime(X.get_value()),0)).set_color(DOT_1_COLOR).set_z_index(6))
        
        x_line_gr2 = always_redraw(lambda: DashedLine(ax2.c2p(X.get_value(), f_prime(X.get_value()), 0), ax2.c2p(X.get_value(), 0, 0), color=GRAY))
        x_line_gr2_label = always_redraw(lambda: MathTex(f'{X.get_value():.1f}', color=GRAY).scale(0.9).next_to(ax2.c2p(X.get_value(), 0, 0), DOWN, buff=0.15))
        
        y_line_gr2 = always_redraw(lambda: DashedLine(ax2.c2p(X.get_value(), f_prime(X.get_value()), 0), ax2.c2p(0, f_prime(X.get_value()), 0), color=GRAY))
        y_line_gr2_label = always_redraw(lambda: MathTex(f'{f_prime(X.get_value()*2):.1f}', color=GRAY).scale(0.9).next_to(ax2.c2p(0, f_prime(X.get_value()), 0), LEFT, buff=0.15))
        
        t9 = Tex('Derivada', color=YELLOW).scale(1.2).move_to(ax2).shift(UP).set_z_index(3)
        t9_sr = SurroundingRectangle(t9, color=BLACK, stroke_width=0, fill_opacity=0.8).set_z_index(2)

        X.set_value(-4.1)
        self.add(ax2, ax2_x_label, ax2_y_label,
                 gr2, gr2_label, 
                 dot_gr2, 
                 x_line_gr2, x_line_gr2_label,
                 y_line_gr2, y_line_gr2_label)
        self.play(X.animate.set_value(4), run_time=5)
        self.wait(2)
        self.play(FadeIn(t9, t9_sr))
        self.wait(2)
        self.play(FadeOut(t9, t9_sr))
        self.wait(2)


        black_sq_1 = Square(color=BLACK, stroke_width=0, fill_opacity=0.8).scale(10).set_z_index(10).next_to(ax1_x_label, RIGHT, buff=0.1)
        black_sq_2 = black_sq_1.copy().next_to(ax2, LEFT, buff=0.1)

        t_dy_dx_copy = t_dy_dx.copy()
        t_dy_dx_aux1_copy = t_dy_dx_aux1.copy()
        t_dy_dx_aux2_copy = t_dy_dx_aux2.copy()

        self.remove(t_dy_dx, t_dy_dx_aux1, t_dy_dx_aux2)
        self.add(t_dy_dx_copy, t_dy_dx_aux1_copy, t_dy_dx_aux2_copy)

        self.play(FadeIn(black_sq_1),
                  VGroup(t_dy_dx_copy, t_dy_dx_aux1_copy, t_dy_dx_aux2_copy).animate.set_opacity(0.2))
        self.wait(2)
        self.play(LaggedStart(FadeOut(black_sq_1),
                              FadeIn(black_sq_2),
                              lag_ratio=0.5))
        self.wait(2)
        self.play(FadeOut(black_sq_2),
                  VGroup(t_dy_dx_copy, t_dy_dx_aux1_copy, t_dy_dx_aux2_copy).animate.set_opacity(1))
        self.wait(2)
        


# Calculando a derivada em uma função genérica
class vid9(MovingCameraScene):
    def construct(self):
        
        # Retomando elementos
        ax1 = Axes(x_range=[-1, 14], x_length=8,
                   y_range=[-1, 9], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.6)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

            # Definindo a função f(x)
        def f(x):
            return (x + 1) / 2 + np.sin(x - 1) + np.sin((x + 1) / 2)

            # Derivada de f(x)
        def f_prime(x):
            return 0.5 + np.cos(x - 1) + 0.5 * np.cos((x + 1) / 2)
        
        gr1 = ax1.plot(f, x_range=[0.4, 13], stroke_width=4, color=BLUE)
        gr1_label = MathTex('y = f(x)', color=BLUE).next_to(gr1, RIGHT).shift(UP*2+LEFT*0)
        
        self.add(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label)
        self.wait(2)


        DOT_1_COLOR = WHITE
        DOT_2_COLOR = GRAY

        X = ValueTracker(6)

        dot_1 = Dot(ax1.c2p(X.get_value(), f(X.get_value()))).set_color(DOT_1_COLOR).set_z_index(6)
        dot_1_label = MathTex(r'(x,f(x))').set_color(DOT_1_COLOR).scale(0.8).next_to(dot_1, DR, buff=0.05)
        dot_1_label_sr = SurroundingRectangle(dot_1_label, color=BLACK, stroke_width=0, fill_opacity=0.8).set_z_index(2)


        TANGENT_LINE_LENGTH = 7.5
        DX_TG = ValueTracker(0.01)
        tangent_line = ax1.plot(lambda x: f_prime(X.get_value())*(x-X.get_value()) + f(X.get_value()), 
                                x_range=[X.get_value() + 0.5*DX_TG.get_value() - (TANGENT_LINE_LENGTH**2/(4 + 4*abs((f(X.get_value() + DX_TG.get_value()) - f(X.get_value()))/DX_TG.get_value())))**0.5, X.get_value()  + 0.5*DX_TG.get_value() + (TANGENT_LINE_LENGTH**2/(4 + 4*abs((f(X.get_value() + DX_TG.get_value()) - f(X.get_value()))/DX_TG.get_value())))**0.5], 
                                stroke_width=4, color=GREEN).set_z_index(2)

        self.play(FadeIn(dot_1, tangent_line))
        self.wait(2)
        self.play(FadeIn(dot_1_label))
        self.wait(2)



        # Traçando a reta secante 
        DX = ValueTracker(4)
        
        dot_2 = always_redraw(lambda: Dot(ax1.c2p(X.get_value() + DX.get_value(),f(X.get_value() + DX.get_value()),0)).set_color(DOT_2_COLOR).set_z_index(5))
        dot_2_label = always_redraw(lambda: MathTex(r'(x + h,f(x + h))').set_color(GRAY).scale(0.8).next_to(dot_2, UL, buff=0.05))
  
        SECANT_LINE_LENGTH = 7.5
        secant_line = always_redraw(lambda: ax1.plot(lambda x: ((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())*(x-X.get_value()) + f(X.get_value()), 
                                                     x_range=[X.get_value() + 0.5*DX.get_value() - (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5, X.get_value()  + 0.5*DX.get_value() + (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5], 
                                                     stroke_width=4, 
                                                     color=GRAY))
        
        dot_2_aux_1 = dot_2.copy()
        dot_2_label_aux_1 = dot_2_label.copy()
        secant_line_aux_1 = secant_line.copy()

        self.play(LaggedStart(Create(secant_line_aux_1),
                              GrowFromCenter(dot_2_aux_1),
                              tangent_line.animate.set_opacity(0.3),
                              lag_ratio=0.3))
        self.remove(secant_line_aux_1, dot_2_aux_1).add(secant_line, dot_2)
        self.wait(2)
        self.play(Flash(dot_1, num_lines=8))
        self.wait(2)
        self.play(Flash(dot_2, num_lines=8),
                  FadeIn(dot_2_label_aux_1))
        self.remove(dot_2_label_aux_1).add(dot_2_label)
        self.wait(2)



        # Calculando a inclinação da reta secante
        DX_COLOR = RED
        DY_COLOR = PURPLE
        
        delta_y_line = always_redraw(lambda: Line(ax1.c2p(X.get_value() + DX.get_value(), f(X.get_value()), 0), ax1.c2p(X.get_value() + DX.get_value(), f(X.get_value() + DX.get_value()), 0), color=DY_COLOR))
        delta_x_line = always_redraw(lambda: Line(ax1.c2p(X.get_value(), f(X.get_value()), 0), ax1.c2p(X.get_value() + DX.get_value(), f(X.get_value()), 0), color=DX_COLOR))

        delta_y_label = always_redraw(lambda: MathTex(r'\Delta y', color=DY_COLOR).scale(DX.get_value()/4).next_to(delta_y_line, RIGHT, buff=0.1))
        delta_x_label = always_redraw(lambda: MathTex(r'\Delta x', color=DX_COLOR).scale(DX.get_value()/4).next_to(delta_x_line, UP, buff=0.1))

        t4 = MathTex(r'\lim_{h \to 0}',r'\frac{\Delta y}{\Delta x}',r'= \lim_{h \to 0}',r'\frac{f(x+h) - f(x)}{h}').scale(0.9).shift(UP*3)
        t4[2][1:].set_z_index(15)
        t4[3].set_z_index(15)
        t4[0].shift(UP*0.15)
        t4[2][1:].shift(UP*0.15)
        t4[3].shift(LEFT*0.8)
        VGroup(t4[1][0:2], t4[3][0:11]).set_color(DY_COLOR)
        VGroup(t4[0][3], t4[1][3:5], t4[2][4], t4[3][4], t4[3][12]).set_color(DX_COLOR)

        self.play(FadeIn(t4[1][0:3]),
                  Create(delta_y_line), FadeIn(delta_y_label))
        self.wait(2)
        self.play(FadeIn(t4[2][0], t4[3][0:12]))
        self.wait(2)
        self.play(FadeIn(t4[1][3:]),
                  Create(delta_x_line), FadeIn(delta_x_label))
        self.wait(2)
        self.play(FadeIn(t4[3][12]))
        self.wait(2)



        # Fazemos o 'h' tender a zero
        self.play(DX.animate.set_value(0.01),
                  tangent_line.animate.set_opacity(1),
                  run_time=5)
        self.wait(2)
        self.play(LaggedStart(t4[3].animate.shift(RIGHT*0.8),
                              FadeIn(t4[0][0:3], t4[2][1:4]),
                              lag_ratio=0.3))
        self.wait(2)
        self.play(FadeIn(t4[0][3:], t4[2][4:]))
        self.wait(2)
        self.remove(secant_line)
        self.play(Wiggle(tangent_line, n_wiggles=4))
        self.wait(2)



        # Destaque na definição da derivada
        black_sq_1 = Square(color=BLACK, fill_opacity=1).scale(20).set_z_index(13)
        t5 = MathTex(r'\lim_{h \to 0}',r'\frac{f(x+h) - f(x)}{h}').scale(1.1).set_z_index(15)
        t5[0].shift(UP*0.15)

        t6 = Tex('Derivada ','de ',r'$f$',' calculada ','em ',r'$x$', color=YELLOW).scale(0.9).next_to(t5, UP, buff=1).set_z_index(15)

        VGroup(t5, t6).move_to(ORIGIN)

        def_sr1 = SurroundingRectangle(VGroup(t5, t6), color=GRAY, buff=0.4).set_opacity(0.3).set_z_index(14)

        self.play(FadeIn(black_sq_1),
                  ReplacementTransform(VGroup(t4[2][1:], t4[3]), t5),
                  run_Time=3)
        self.wait(2)
        self.play(LaggedStart(FadeIn(t6[0]),
                              FadeIn(t6[1]),
                              FadeIn(t6[2]),
                              FadeIn(t6[3]),
                              FadeIn(t6[4]),
                              FadeIn(t6[5]),
                              FadeIn(def_sr1),
                              lag_ratio=0.5))
        self.wait(2)



        # Mudando a notação para dy/dx ou df/dx
        t7 = MathTex(r'\frac{dy}{dx}(x) =').scale(1.1).next_to(t5, LEFT, buff=0.2).set_z_index(15).set_opacity(0)
        t7.shift(RIGHT*1.1)
        self.add(t7)

        t5_aux = t5.copy().shift(RIGHT*1.1)
        def_sr2 = SurroundingRectangle(VGroup(t6, t5_aux, t7), color=GRAY, buff=0.4).set_opacity(0.3).set_z_index(14)

        self.play(LaggedStart(AnimationGroup(t5.animate.shift(RIGHT*1.1), ReplacementTransform(def_sr1, def_sr2)),
                              t7.animate.set_opacity(1),
                              lag_ratio=0.5))
        self.wait(2)



        t8 = MathTex(r'\frac{df}{dx}(x) =').scale(1.1).move_to(t7, aligned_edge=RIGHT).set_z_index(15)
        self.play(TransformMatchingShapes(t7[0][0:5], t8[0][0:5]))
        self.wait(2)



        # Mudando a notação para y'(x) ou f'(x)
        t9 = MathTex(r'y^\prime(x) =').scale(1.1).move_to(t7, aligned_edge=RIGHT).set_z_index(15)
        t9[0][0:2].shift(RIGHT*0.05)
        self.play(LaggedStart(FadeOut(t8[0][0:5]),
                              FadeIn(t9[0][0:2]),
                              lag_ratio=0.7))
        self.wait(2)


        t10 = MathTex(r'f^\prime(x) =').scale(1.1).move_to(t7, aligned_edge=RIGHT).set_z_index(15)
        t10[0][0:2].shift(RIGHT*0.05)
        self.play(LaggedStart(FadeOut(t9[0][0:2]),
                              FadeIn(t10[0][0:2]),
                              lag_ratio=0.7))
        self.wait(2)



        # Volta para o gráfico
        self.add(t4),
        self.remove(t4,
                    dot_1, dot_1_label,
                    dot_2, dot_2_label,
                    tangent_line)
        self.wait()
        self.play(LaggedStart(FadeOut(def_sr2, t6, t5, t7[0][5:], t10[0][0:2]),
                              FadeOut(black_sq_1),
                              lag_ratio=0.5))
        self.wait(2)



        # Ponto percorrendo o gráfico com o valor da derivada em cima
        dot_1 = always_redraw(lambda: Dot(ax1.c2p(X.get_value(), f(X.get_value()))).set_color(DOT_1_COLOR).set_z_index(6))

        derivative_tex = always_redraw(lambda: MathTex(str(round(f_prime(X.get_value()), 2))).scale(0.8).next_to(dot_1, UP, buff=0.2))

        tangent_line = always_redraw(lambda: Line((0,0,0), (5,0,0), stroke_width=4, color=GREEN).rotate(np.arctan(f_prime(X.get_value())*0.888)).move_to(dot_1))

        self.add(dot_1, derivative_tex, tangent_line)

        X.set_value(0.4)
        self.play(X.animate.set_value(13), run_time=10, rate_func=linear)
        self.wait(2)



# A derivada tem o mesmo papel do coeficiente angular
class vid10(MovingCameraScene):
    def construct(self):
        
        # Retomando elementos
        ax1 = Axes(x_range=[-1, 14], x_length=8,
                   y_range=[-1, 9], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.6)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

            # Definindo a função f(x)
        def f(x):
            return (x + 1) / 2 + np.sin(x - 1) + np.sin((x + 1) / 2)

            # Derivada de f(x)
        def f_prime(x):
            return 0.5 + np.cos(x - 1) + 0.5 * np.cos((x + 1) / 2)
        
        gr1 = ax1.plot(f, x_range=[0.4, 13], stroke_width=4, color=BLUE)
        gr1_label = MathTex('y = f(x)', color=BLUE).next_to(gr1, RIGHT).shift(UP*2+LEFT*0)


        X = ValueTracker(0.4)

        
        TANGENT_LINE_LENGTH = 7.5
        DX_TG = ValueTracker(0.01)
        tangent_line = always_redraw(lambda: Line((0,0,0), (5,0,0), stroke_width=4, color=GREEN).rotate(np.arctan(f_prime(X.get_value())*0.888)).move_to(ax1.c2p(X.get_value(), f(X.get_value()), 0)))

        self.add(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label)
        self.wait(2)



        # A derivada é positiva quando a função é crescente
        DOT_1_COLOR = WHITE

        dot_1 = always_redraw(lambda: Dot(ax1.c2p(X.get_value(), f(X.get_value()))).set_color(DOT_1_COLOR).set_z_index(6))
        derivative_tex = always_redraw(lambda: MathTex(str(round(f_prime(X.get_value()), 2))).scale(0.8).next_to(dot_1, UP, buff=0.2))


        HL_COLOR = YELLOW
        HL_STROKE_WIDTH = 8

        hl_increasing_1 = ax1.plot(f, x_range=[0.4, 2.89], stroke_width=HL_STROKE_WIDTH, color=HL_COLOR)
        hl_increasing_2 = ax1.plot(f, x_range=[5.7, 9.82], stroke_width=HL_STROKE_WIDTH, color=HL_COLOR)
        hl_increasing_3 = ax1.plot(f, x_range=[10.72, 13], stroke_width=HL_STROKE_WIDTH, color=HL_COLOR)
        
        self.add(hl_increasing_1, dot_1, derivative_tex, tangent_line)
        self.play(X.animate.set_value(2.8), run_time=3, rate_func=linear)
        self.wait(2)

        X.set_value(5.8)
        self.add(hl_increasing_2).remove(hl_increasing_1)
        self.play(X.animate.set_value(9.7), run_time=3, rate_func=linear)
        self.wait(2)

        X.set_value(10.6)
        self.add(hl_increasing_3).remove(hl_increasing_2)
        self.play(X.animate.set_value(13), run_time=3, rate_func=linear)
        self.wait(2)

        self.remove(hl_increasing_3, dot_1, derivative_tex, tangent_line)
        self.wait(2)



        # A derivada é negativa quando a função é decrescente
        hl_decreasing_1 = ax1.plot(f, x_range=[2.89, 5.70], stroke_width=HL_STROKE_WIDTH, color=HL_COLOR)

        X.set_value(2.8)
        self.add(hl_decreasing_1, dot_1, derivative_tex, tangent_line)
        self.play(X.animate.set_value(5.6), run_time=3, rate_func=linear)
        self.wait(2)

        self.remove(hl_decreasing_1, dot_1, derivative_tex, tangent_line)
        self.wait(2)



        # A derivada é zero nos pontos em que a função muda de crescente para decrescente
        max_dot_1 = Dot().move_to(ax1.c2p(2.893, 3.825, 0))
        max_dot_2 = Dot().move_to(ax1.c2p(9.816, 5.212, 0))

        min_dot_1 = Dot().move_to(ax1.c2p(5.7, 2.143, 0))
        min_dot_2 = Dot().move_to(ax1.c2p(10.722, 5.158, 0))

        X.set_value(2.891)
        self.add(dot_1, derivative_tex, tangent_line)
        self.play(X.animate.set_value(2.892))
        self.wait(2)

        X.set_value(5.705)
        self.play(X.animate.set_value(5.706))
        self.wait(2)

        X.set_value(9.815)
        self.play(X.animate.set_value(9.816))
        self.wait(2)

        X.set_value(10.723)
        self.play(X.animate.set_value(10.724))
        self.wait(2)



        # A derivada é zero quando a função é constante
        ax2 = Axes(x_range=[-1, 14], x_length=8,
                   y_range=[-1, 9], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.6)
        ax2_x_label = MathTex('x').set_color(GRAY).next_to(ax2.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax2_y_label = MathTex('y').set_color(GRAY).next_to(ax2.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

            # Definindo a função f(x)
        def f(x):
            return 4

            # Derivada de f(x)
        def f_prime(x):
            return 0.0
        
        gr2 = ax2.plot(f, x_range=[-1, 13], stroke_width=4, color=BLUE)
        gr2_label = MathTex('y = f(x)', color=BLUE).next_to(gr2, RIGHT)


        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)
        self.play(FadeIn(ax2, ax2_x_label, ax2_y_label, gr2, gr2_label))
        self.wait(2)

        X.set_value(-1)
        self.add(dot_1, derivative_tex, tangent_line)
        self.play(X.animate.set_value(13), run_time=5, rate_func=linear)
        self.wait(2)
        


# O limite tem que ser igual pelos dois lados
class vid11(MovingCameraScene):
    def construct(self):
        
        # Retomando elementos
        ax1 = Axes(x_range=[-1, 14], x_length=8,
                   y_range=[-1, 9], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.6)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

            # Definindo a função f(x)
        def f(x):
            return (x + 1) / 2 + np.sin(x - 1) + np.sin((x + 1) / 2)

            # Derivada de f(x)
        def f_prime(x):
            return 0.5 + np.cos(x - 1) + 0.5 * np.cos((x + 1) / 2)
        
        gr1 = ax1.plot(f, x_range=[0.4, 13], stroke_width=4, color=BLUE)
        gr1_label = MathTex('y = f(x)', color=BLUE).next_to(gr1, RIGHT).shift(UP*2+LEFT*0)

        self.add(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label)


        DOT_1_COLOR = WHITE
        DOT_2_COLOR = GRAY

        X = ValueTracker(6)

        dot_1 = Dot(ax1.c2p(X.get_value(), f(X.get_value()))).set_color(DOT_1_COLOR).set_z_index(6)
        dot_1_label = MathTex(r'(x,f(x))').set_color(DOT_1_COLOR).scale(0.8).next_to(dot_1, DR, buff=0.05)
        dot_1_label_sr = SurroundingRectangle(dot_1_label, color=BLACK, stroke_width=0, fill_opacity=0.8).set_z_index(2)



        TANGENT_LINE_LENGTH = 7.5
        DX_TG = ValueTracker(0.01)
        tangent_line = ax1.plot(lambda x: f_prime(X.get_value())*(x-X.get_value()) + f(X.get_value()), 
                                x_range=[X.get_value() + 0.5*DX_TG.get_value() - (TANGENT_LINE_LENGTH**2/(4 + 4*abs((f(X.get_value() + DX_TG.get_value()) - f(X.get_value()))/DX_TG.get_value())))**0.5, X.get_value()  + 0.5*DX_TG.get_value() + (TANGENT_LINE_LENGTH**2/(4 + 4*abs((f(X.get_value() + DX_TG.get_value()) - f(X.get_value()))/DX_TG.get_value())))**0.5], 
                                stroke_width=4, color=GREEN).set_z_index(2)

        self.add(dot_1, tangent_line)



        # Traçando a reta secante
        DX = ValueTracker(4)
        
        dot_2 = always_redraw(lambda: Dot(ax1.c2p(X.get_value() + DX.get_value(),f(X.get_value() + DX.get_value()),0)).set_color(DOT_2_COLOR).set_z_index(5))

        x2_line = always_redraw(lambda: DashedLine(dot_2, ax1.c2p(X.get_value() + DX.get_value(),0,0), color=GRAY))
        x2_line_aux_1 = x2_line.copy()

        SECANT_LINE_LENGTH = 7.5
        secant_line = always_redraw(lambda: ax1.plot(lambda x: ((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())*(x-X.get_value()) + f(X.get_value()), 
                                                     x_range=[X.get_value() + 0.5*DX.get_value() - (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5, X.get_value()  + 0.5*DX.get_value() + (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5], 
                                                     stroke_width=4, 
                                                     color=GRAY))
        
        dot_2_aux_1 = dot_2.copy()
        secant_line_aux_1 = secant_line.copy()

        self.play(LaggedStart(Create(secant_line_aux_1),
                              AnimationGroup(GrowFromCenter(dot_2_aux_1), FadeIn(x2_line_aux_1)),
                              tangent_line.animate.set_opacity(1),
                              lag_ratio=0.3))
        self.remove(secant_line_aux_1, dot_2_aux_1, x2_line_aux_1).add(secant_line, dot_2, x2_line)
        self.wait(2)



        # Aproximando a tangente pela secante
        self.play(DX.animate.set_value(0.01), run_time=3)
        self.wait(2)

        DX.set_value(-4)
        self.play(DX.animate.set_value(-0.01), run_time=3)
        self.wait(2)

        DX.set_value(4)
        self.play(DX.animate.set_value(0.01), run_time=3)
        self.wait(2)

        DX.set_value(-4)
        self.play(DX.animate.set_value(-0.01), run_time=3)
        self.wait(2)

        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)
        self.add(ax1, ax1_x_label, ax1_y_label)
        self.wait(2)
        


        # Exemplo: função não contínua
        def f1(x):
            return x*1/2 + np.sin(x + 4) + 0.3

        def f2(x):
            return x*1/2 + np.sin(x + 2) + 1  

        def f1_prime(x):
            return 0.5 + np.cos(x + 4)

        def f2_prime(x):
            return 0.5 + np.cos(x + 2)
        

        gr2_1 = ax1.plot(f1, x_range=[0.4, 7], stroke_width=4, color=BLUE)
        gr2_2 = ax1.plot(f2, x_range=[7, 13], stroke_width=4, color=BLUE)
        gr2_label = MathTex(r'y = f(x)', color=BLUE).next_to(gr1, RIGHT).shift(UP*2.5+LEFT*0)


        a_line = DashedLine(ax1.c2p(7,f2(7),0), ax1.c2p(7,0,0), color=YELLOW).set_opacity(0.5)
        a_label = MathTex('a', color=YELLOW).scale(0.9).next_to(ax1.c2p(7,0,0), DOWN, buff=0.2)


        X.set_value(7)
        DX.set_value(-4)
        dot_2_gr1 = always_redraw(lambda: Dot(ax1.c2p(X.get_value() + DX.get_value(),f1(X.get_value() + DX.get_value()),0)).set_color(DOT_2_COLOR).set_z_index(5))
        dot_2_gr2 = always_redraw(lambda: Dot(ax1.c2p(X.get_value() + DX.get_value(),f2(X.get_value() + DX.get_value()),0)).set_color(DOT_2_COLOR).set_z_index(5))


        x2_line_gr1 = always_redraw(lambda: DashedLine(dot_2_gr1, ax1.c2p(X.get_value() + DX.get_value(),0,0), color=GRAY))
        x2_line_gr2 = always_redraw(lambda: DashedLine(dot_2_gr2, ax1.c2p(X.get_value() + DX.get_value(),0,0), color=GRAY))


        dot_aux_1 = Dot(color=BLUE).move_to(ax1.c2p(7,f1(7))).set_z_index(2)
        dot_aux_2 = Dot(color=BLUE).move_to(ax1.c2p(7,f2(7))).set_z_index(2)
        dot_aux_3 = Dot(color=BLACK).move_to(ax1.c2p(7,f2(7))).scale(0.7).set_z_index(3)


        SECANT_LINE_LENGTH = 8.5
        secant_line1 = always_redraw(lambda: ax1.plot(lambda x: ((f1(X.get_value() + DX.get_value()) - f1(X.get_value()))/DX.get_value())*(x-X.get_value()) + f1(X.get_value()), 
                                                     x_range=[X.get_value() + 0.5*DX.get_value() - (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5, X.get_value()  + 0.5*DX.get_value() + (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5], 
                                                     stroke_width=4, 
                                                     color=GRAY))
        secant_line2 = always_redraw(lambda: ax1.plot(lambda x: ((f2(X.get_value() + DX.get_value()) - f2(X.get_value()))/DX.get_value())*(x-X.get_value()) + f2(X.get_value()), 
                                                     x_range=[X.get_value() + 0.5*DX.get_value() - (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5, X.get_value()  + 0.5*DX.get_value() + (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5], 
                                                     stroke_width=4, 
                                                     color=GRAY))
        

        X.set_value(7)
        DX.set_value(-4)
        self.play(FadeIn(gr2_1, gr2_2, gr2_label, a_line, a_label, dot_aux_1, dot_aux_2, dot_aux_3))
        self.add(x2_line_gr1, dot_2_gr1, secant_line1)
        self.wait(2)
        self.play(DX.animate.set_value(-0.01), run_time=3)  # Aproximando pela esquerda
        self.wait(2)



        DX.set_value(4)
        self.remove(x2_line_gr1, dot_2_gr1, secant_line1).add(secant_line2, dot_2_gr2, x2_line_gr2)
        self.wait(2)
        self.play(DX.animate.set_value(0.01), run_time=3)   # Aproximando pela direita
        self.wait(2)


        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)



        # Exemplo: função y = |x^2 - 1|
        ax3 = Axes(x_range=[-4, 4], x_length=8,
                   y_range=[-1, 7], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY)
        ax3_x_label = MathTex('x').set_color(GRAY).next_to(ax3.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax3_y_label = MathTex('y').set_color(GRAY).next_to(ax3.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)


        def f3(x):
                return x**2 - 1

        def f4(x):
                return -x**2 + 1

        def f5(x):
                return x**2 - 1

        gr3_1 = ax3.plot(f3, x_range=[-2.8, -1], stroke_width=4, color=BLUE)
        gr3_2 = ax3.plot(f4, x_range=[-1, 1], stroke_width=4, color=BLUE)
        gr3_3 = ax3.plot(f5, x_range=[1, 2.8], stroke_width=4, color=BLUE)
        gr3_label = MathTex(r'y = \vert x^2 - 1 \vert', color=BLUE).next_to(gr3_3, RIGHT).shift(UP*2+LEFT*0)

        self.add(ax3, ax3_x_label, ax3_y_label, gr3_1, gr3_2, gr3_3, gr3_label)
        self.wait(2)



        dot_1 = Dot(ax3.c2p(1,0,0)).set_z_index(6)

        self.play(GrowFromCenter(dot_1), 
        Flash(dot_1, num_lines=8))



            # Aproximando pela direita
        X.set_value(1)
        DX.set_value(1.5)
        
        dot_2_f3 = always_redraw(lambda: Dot(ax3.c2p(X.get_value() + DX.get_value(),f3(X.get_value() + DX.get_value()),0)).set_color(DOT_2_COLOR).set_z_index(5))
        dot_2_f4 = always_redraw(lambda: Dot(ax3.c2p(X.get_value() + DX.get_value(),f4(X.get_value() + DX.get_value()),0)).set_color(DOT_2_COLOR).set_z_index(5))

        SECANT_LINE_LENGTH = 6.5
        secant_line1 = always_redraw(lambda: ax3.plot(lambda x: ((f3(X.get_value() + DX.get_value()) - f3(X.get_value()))/DX.get_value())*(x-X.get_value()) + f3(X.get_value()), 
                                                     x_range=[X.get_value() + 0.5*DX.get_value() - (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5, X.get_value()  + 0.5*DX.get_value() + (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5], 
                                                     stroke_width=4, 
                                                     color=GRAY))

        self.add(dot_2_f3, secant_line1)
        self.wait(2)
        self.play(DX.animate.set_value(0.01), run_time=3)
        self.wait(2)

        self.remove(dot_2_f3, secant_line1).add(dot_2_f3.copy(), secant_line1.copy())
        self.wait(2)



            # Aproximando pela esquerda
        DX.set_value(-1.9)
        secant_line2 = always_redraw(lambda: ax3.plot(lambda x: ((f4(X.get_value() + DX.get_value()) - f4(X.get_value()))/DX.get_value())*(x-X.get_value()) + f4(X.get_value()), 
                                                     x_range=[X.get_value() + 0.5*DX.get_value() - (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5, X.get_value()  + 0.5*DX.get_value() + (SECANT_LINE_LENGTH**2/(4 + 4*((f(X.get_value() + DX.get_value()) - f(X.get_value()))/DX.get_value())))**0.5], 
                                                     stroke_width=4, 
                                                     color=GRAY))

        self.add(dot_2_f4, secant_line2)
        self.wait(2)
        self.play(DX.animate.set_value(-0.01), run_time=3)
        self.wait(2)

        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)



# Uma função é derivável nos pontos onde o limite existe
class vid12(MovingCameraScene):
    def construct(self):

        t2 = MathTex(r'\lim_{h \to 0}',r'\frac{f(a + h) - f(a)}{h}')
        t1 = Tex(r'Uma',' função ','$f(x)$',' é ','derivável',' em ','$x = a$',' se').set_color(YELLOW).scale(0.9).next_to(t2, UP, buff=0.7)
        t3 = Tex(r'existe').set_color(YELLOW).scale(0.9).next_to(t2, RIGHT, buff=0.7)

        VGroup(t2, t3).move_to(ORIGIN)

        VGroup(t1, t2, t3).move_to(ORIGIN)

        def_sr = SurroundingRectangle(VGroup(t1, t2, t3), color=GRAY, buff=0.4).set_opacity(0.3).set_z_index(14)

        self.play(LaggedStart(FadeIn(t1[0]),
                              FadeIn(t1[1]),
                              FadeIn(t1[2]),
                              FadeIn(t1[3]),
                              FadeIn(t1[4]),
                              FadeIn(t1[5]),
                              FadeIn(t1[6]),
                              FadeIn(t1[7]),
                              FadeIn(t2),
                              FadeIn(t3),
                              FadeIn(def_sr),
                              lag_ratio=0.5))
        self.wait(2)
        self.play(FadeOut(t1, t2, t3, def_sr))
        self.wait(2)



        # O gráfico deve ser contínuo e suave
        ax1 = Axes(x_range=[-1, 14], x_length=8,
                   y_range=[-1, 9 ], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

            # Definindo a função f(x)
        def f(x):
            return (x + 1) / 2 + np.sin(2*x - 1) + np.sin(x + 1) + 1
            
        gr1 = ax1.plot(f, x_range=[0.4, 13], stroke_width=4, color=BLUE)
        gr1_label = MathTex('y = f(x)', color=BLUE).next_to(gr1, RIGHT).shift(UP*2.5+LEFT*0)

        hl_1 = ax1.plot(f, x_range=[1.2 - 0.5, 1.2 + 0.5], stroke_width=8, color=YELLOW)
        hl_2 = ax1.plot(f, x_range=[2.9 - 0.5, 2.9 + 0.5], stroke_width=8, color=YELLOW)
        hl_3 = ax1.plot(f, x_range=[4.7 - 0.5, 5.5 + 0.5], stroke_width=8, color=YELLOW)
        hl_4 = ax1.plot(f, x_range=[7.5 - 0.5, 7.5 + 0.5], stroke_width=8, color=YELLOW)
        hl_5 = ax1.plot(f, x_range=[9.2 - 0.5, 9.2 + 0.5], stroke_width=8, color=YELLOW)
        hl_6 = ax1.plot(f, x_range=[11 - 0.5, 11.9 + 0.5], stroke_width=8, color=YELLOW)

        self.play(FadeIn(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label))
        self.wait(2)
        self.play(ShowPassingFlash(gr1.copy().set_color(YELLOW).set_stroke(width=8), time_width=0.3), run_time=2.5)
        self.wait(2)
        self.play(FadeIn(hl_1, hl_2, hl_3, hl_4, hl_5, hl_6))
        self.wait(2)



# Trabalhando com derivadas na prática
class vid13(MovingCameraScene):
    def construct(self):

        t = MathTex(r'\lim_{h \to 0}',r'\frac{f(x + h) - f(x)}{h}').scale(1.1)

        self.play(FadeIn(t))
        self.wait(2)
        self.add(t)



        # Derivadas de algumas funções
        h_line_1 = Line(LEFT, RIGHT, stroke_width = 2).scale(2.3)
        h_line_2 = h_line_1.copy()
        h_line_3 = h_line_1.copy()
        h_line_4 = h_line_1.copy()
        h_line_5 = h_line_1.copy()
        h_lines = VGroup(h_line_1, h_line_2, h_line_3, h_line_4, h_line_5).arrange(DOWN, buff = 1).shift(DOWN*0)
        
        v_line = Line(UP, DOWN, stroke_width = 2).scale(2.5).move_to(h_lines, aligned_edge=DOWN)
        
        x_table = MathTex('f(x)', color = BLUE).scale(1.1).next_to(h_line_1, UP, buff = 0.2).shift(LEFT*1.15)
        y_table = MathTex(r'f^\prime(x)', color = BLUE).scale(1.1).next_to(h_line_1, UP, buff = 0.2).shift(RIGHT*1.15)
        
        x_value_1 = MathTex(r'x^n').scale(1).next_to(h_line_2, UP, buff = 0.3).shift(LEFT*1.15)
        x_value_2 = MathTex(r'\ln(x)').scale(1).next_to(h_line_3, UP, buff = 0.2).shift(LEFT*1.15)
        x_value_3 = MathTex(r'e^x').scale(1).next_to(h_line_4, UP, buff = 0.3).shift(LEFT*1.15)
        x_value_4 = MathTex(r'\text{sen}(x)').scale(1).next_to(h_line_5, UP, buff = 0.2).shift(LEFT*1.15)
        x_values = VGroup(x_value_1, x_value_2, x_value_3, x_value_4)

        y_value_1 = MathTex(r'nx^{n-1}').scale(1).next_to(h_line_2, UP, buff = 0.3).shift(RIGHT*1.15)
        y_value_2 = MathTex(r'1/x').scale(1).next_to(h_line_3, UP, buff = 0.2).shift(RIGHT*1.15)
        y_value_3 = MathTex(r'e^x').scale(1).next_to(h_line_4, UP, buff = 0.3).shift(RIGHT*1.15)
        y_value_4 = MathTex(r'\text{cos}(x)').scale(1).next_to(h_line_5, UP, buff = 0.2).shift(RIGHT*1.15)
        y_values = VGroup(y_value_1, y_value_2, y_value_3, y_value_4)

        etc1 = MathTex('...').scale(1.2).next_to(h_line_5, DOWN, buff = 0.6).shift(LEFT*1.15).rotate(-90*DEGREES)
        etc2 = MathTex('...').scale(1.2).next_to(h_line_5, DOWN, buff = 0.6).shift(RIGHT*1.15).rotate(-90*DEGREES)

        table = VGroup(v_line, h_lines, x_table, y_table, x_values, y_values, etc1, etc2)
        table.shift(DOWN*8)


        self.add(table)
        self.play(self.camera.frame.animate.shift(DOWN*8), run_time=2)
        self.wait(2)



        # Regras de derivação
        sum_rule = MathTex(r'\bigl( f(x) + g(x) \bigr) ^\prime \:=\: f^\prime(x) \:+\: g^\prime(x)')
        product_rule = MathTex(r'\bigl( f(x) \cdot g(x) \bigr) ^\prime \:=\: f^\prime(x) \cdot g(x) \:+\: f(x) \cdot g^\prime(x)')
        chain_rule = MathTex(r'\bigl( f(g(x)) \bigr)^\prime \:=\: f^\prime(g(x)) \cdot g^\prime(x)')

        VGroup(sum_rule[0][1:5], sum_rule[0][13:18],
               product_rule[0][1:5], sum_rule[0][13:18], product_rule[0][24:28],
               chain_rule[0][1:3], chain_rule[0][7], chain_rule[0][11:14], chain_rule[0][18],
               ).set_color(BLUE)
        
        VGroup(sum_rule[0][6:10], sum_rule[0][19:24],
               product_rule[0][6:10], product_rule[0][19:23], product_rule[0][29:34],
               chain_rule[0][3:7], chain_rule[0][14:18], chain_rule[0][20:25]).set_color(RED)

        rules = VGroup(sum_rule, product_rule, chain_rule).arrange(DOWN, buff=1, aligned_edge=LEFT).scale(0.9)
        rules.shift(DOWN*16)


        sr_sum_rule = SurroundingRectangle(sum_rule, color=YELLOW, buff=0.3, fill_opacity=0).set_z_index(-1)
        sr_product_rule = SurroundingRectangle(product_rule, color=YELLOW, buff=0.3, fill_opacity=0).set_z_index(-1)
        sr_chain_rule = SurroundingRectangle(chain_rule, color=YELLOW, buff=0.3, fill_opacity=0).set_z_index(-1)



        self.add(rules)
        self.play(self.camera.frame.animate.shift(DOWN*8), run_time=2)
        self.wait(2)
        ############self.play(FadeIn(sr_sum_rule))
        self.play(sum_rule.animate.set_opacity(1),
                  product_rule.animate.set_opacity(0.2),
                  chain_rule.animate.set_opacity(0.2))
        self.wait(2)
        ###########3self.play(FadeOut(sr_sum_rule),
        ############          FadeIn(sr_product_rule))
        self.play(sum_rule.animate.set_opacity(0.2),
                  product_rule.animate.set_opacity(1),
                  chain_rule.animate.set_opacity(0.2))
        self.wait(2)
        ###########self.play(FadeOut(sr_product_rule),
        #########3          FadeIn(sr_chain_rule))
        self.play(sum_rule.animate.set_opacity(0.2),
                  product_rule.animate.set_opacity(0.2),
                  chain_rule.animate.set_opacity(1))
        self.wait(2)
        ###########self.play(FadeOut(sr_chain_rule))
        self.wait(2)



        # Derivando uma função
        t1 = MathTex(r'\bigl( (x + 1) \cdot e^{x^2} \bigr) ^\prime =',r'e^{x^2} + (x + 1) \cdot 2x \cdot e^{x^2}')
        t1.set_color(BLUE)
        VGroup(t1[0][0], t1[0][10:]).set_color(WHITE)
        t1.shift(DOWN*24)

        self.add(t1[0])
        self.play(self.camera.frame.animate.shift(DOWN*8), run_time=2)
        self.wait(2)
        self.play(LaggedStart(FadeIn(t1[1][0:3]),
                              FadeIn(t1[1][3:9]),
                              FadeIn(t1[1][9:]),
                              lag_ratio=0.7))
        self.wait(2)

        

        t2 = MathTex(r'x^4 + 2x^3 - 3x^2 + 4x - 5', color=BLUE)
        t2.shift(DOWN*32)
        self.add(t2)

        self.play(self.camera.frame.animate.shift(DOWN*8), run_time=2)
        self.wait(2)
        self.play(FadeOut(t2))
        self.wait(2)



# Derivada de polinômio
class vid14(MovingCameraScene):
    def construct(self):
        
        # Derivada de x^1
        t1 = MathTex(r'(x^1)^\prime = 1')
        t1[0][1:3].set_color(BLUE)

        self.play(FadeIn(t1[0][0:6]))
        self.wait(2)
        self.play(FadeIn(t1[0][6]))
        self.wait(2)



        ax1 = Axes(x_range=[-1, 5], x_length=6,
                   y_range=[-1, 5], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        def f(x):
            return x

        gr1 = ax1.plot(f, x_range=[-1, 5], stroke_width=4, color=BLUE)
        gr1_label = MathTex('y = x', color=BLUE).next_to(gr1, RIGHT).shift(UP*3+LEFT*0)

        VGroup(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label).scale(0.9)

        self.play(LaggedStart(t1.animate.scale(0.9).to_corner(UL, buff=1),
                              FadeIn(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label),
                              lag_ratio=0.5))
        self.wait(2)
        self.play(FadeOut(ax1, ax1_x_label, ax1_y_label, gr1, gr1_label))
        self.wait(2)



        # Derivada de x^2
        t2 = MathTex(r'(x^2)^\prime = 2x')
        t2[0][1:3].set_color(GREEN)

        self.play(FadeIn(t2[0][0:6]))
        self.wait(2)
        self.play(FadeIn(t2[0][6:]))
        self.wait(2)
        self.play(t2.animate.scale(0.9).next_to(t1, DOWN, buff=0.8, aligned_edge=LEFT))
        self.wait(2)



        # Outras derivadas de x^n
        t3 = MathTex(r'(x^3)^\prime = 3x^2').scale(0.9).next_to(t2, DOWN, buff=0.8, aligned_edge=LEFT)
        t3[0][1:3].set_color(ORANGE)

        t4 = MathTex(r'(x^4)^\prime = 4x^3').scale(0.9).next_to(t3, DOWN, buff=0.8, aligned_edge=LEFT)
        t4[0][1:3].set_color(RED)

        t5 = MathTex(r'(x^5)^\prime = 5x^4').scale(0.9).next_to(t4, DOWN, buff=0.8, aligned_edge=LEFT)
        t5[0][1:3].set_color(PURPLE)

        self.play(LaggedStart(FadeIn(t3),
                              FadeIn(t4),
                              FadeIn(t5),
                              lag_ratio=0.3))
        self.wait(2)



        # Fórmula geral para a derivada de x^n
        t6 = MathTex(r'(x^n)^\prime = nx^{n-1}')
        t6_sr = SurroundingRectangle(t6, color=GRAY, buff=0.2).set_opacity(0).set_z_index(-1)

        l1 = Line(t1.get_edge_center(RIGHT), t6.get_edge_center(LEFT), buff=0.3, color=BLUE)
        l2 = Line(t2.get_edge_center(RIGHT), t6.get_edge_center(LEFT), buff=0.3, color=GREEN)
        l3 = Line(t3.get_edge_center(RIGHT), t6.get_edge_center(LEFT), buff=0.3, color=ORANGE)
        l4 = Line(t4.get_edge_center(RIGHT), t6.get_edge_center(LEFT), buff=0.3, color=RED)
        l5 = Line(t5.get_edge_center(RIGHT), t6.get_edge_center(LEFT), buff=0.3, color=PURPLE)

        self.play(LaggedStart(Create(l1),
                              Create(l2),
                              Create(l3),
                              Create(l4),
                              Create(l5),
                              GrowFromCenter(t6[0][0:6]),
                              lag_ratio=0.1))
        self.wait(2)
        self.play(LaggedStart(FadeIn(t6[0][6]),
                              FadeIn(t6[0][7]),
                              FadeIn(t6[0][8:]),
                              lag_ratio=0.5))
        self.wait(2)
        self.add(t6_sr)
        self.play(LaggedStart(FadeOut(t1, t2, t3, t4, t5,
                                      l1, l2, l3, l4, l5),
                              AnimationGroup(t6.animate.shift(UP*2.5),
                                             t6_sr.animate.shift(UP*2.5).set_opacity(0.3)),
                              lag_ratio=0.4))
        self.wait(2)



        # Derivada de uma constante vezes uma função
        t3 = MathTex(r'(af(x))^\prime = a \cdot f^\prime(x)').next_to(t6, DOWN, buff=1)
        VGroup(t3[0][2:6], t3[0][11:]).set_color(BLUE)
        VGroup(t3[0][1], t3[0][9]).set_color(YELLOW)

        t3_sr = SurroundingRectangle(t3, color=GRAY, buff=0.2).set_opacity(0.3).set_z_index(-1)

        self.play(FadeIn(t3[0][0:7]))
        self.wait(2)
        self.play(FadeIn(t3[0][7:]))
        self.play(FadeIn(t3_sr))
        self.wait(2)



        t4 = MathTex(r'(2x^3)^\prime = 2 \cdot 3x^2').scale(0.9).next_to(t3, DOWN, buff=0.7)
        VGroup(t4[0][2:6], t4[0][9:]).set_color(BLUE)
        VGroup(t4[0][1], t4[0][7]).set_color(YELLOW)

        t4_aux = MathTex(r'6x^2', color=BLUE).scale(0.9).move_to(t4[0][7:], aligned_edge=LEFT)
        t4_aux[0][0].set_color(GREEN)

        self.play(FadeIn(t4[0][0:7]))
        self.wait(2)
        self.play(FadeIn(t4[0][7:]))
        self.wait(2)
        self.play(TransformMatchingShapes(t4[0][7:], t4_aux))
        self.wait(2)
        self.play(FadeOut(t4[0][0:7], t4_aux))
        self.wait(2)



        # Derivada da soma
        t5 = MathTex(r'\bigl( f(x) + g(x) \bigr) ^\prime \:=\: f^\prime(x) \:+\: g^\prime(x)').next_to(t3, DOWN, buff=1)
        VGroup(t5[0][1:5], t5[0][13:18]).set_color(BLUE)
        VGroup(t5[0][6:10], t5[0][19:24]).set_color(RED)

        t5_sr = SurroundingRectangle(t5, color=GRAY, buff=0.2).set_opacity(0.3)

        self.play(FadeIn(t5[0][0:13]))
        self.wait(2)
        self.play(FadeIn(t5[0][13:]))
        self.play(FadeIn(t5_sr))
        self.wait(2)



        t6 = MathTex(r'(3x^5 + 4x^3)^\prime = 15x^4 + 12x^2').scale(0.9).next_to(t5, DOWN, buff=0.7)
        VGroup(t6[0][1:4], t6[0][11:15]).set_color(BLUE)
        VGroup(t6[0][5:8], t6[0][16:]).set_color(RED)

        self.play(FadeIn(t6[0][0:11]))
        self.wait(2)
        self.play(FadeIn(t6[0][11:]))
        self.wait(2)
        self.play(FadeOut(t6))
        self.wait(2)
        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)



        # Derivando um polinômio
        t7 = MathTex(r'f(x) =','x^4','+ 2x^3','- 3x^2','+ 4x','- 5', color=BLUE).scale(0.9).shift(UP*0.5)
        t8 = MathTex(r'f^\prime(x) =','4x^3','+ 6x^2','- 6x','+ 4','- 0', color=BLUE).scale(0.9).shift(DOWN*0.5+LEFT*0.17)
        VGroup(t7[0][4], t8[0][5]).set_color(WHITE)

        t8_aux_1 = MathTex('x^4', color=BLUE).scale(0.9).move_to(t8[1], aligned_edge=RIGHT)

        self.play(FadeIn(t7))
        self.wait(2)
        self.play(FadeIn(t8[0][0:6]))
        self.wait(2)
        self.play(TransformFromCopy(t7[1], t8[1]))
        self.wait(2)
        self.play(FadeIn(t8[2][0]),
                  TransformFromCopy(t7[2][1:], t8[2][1:]))
        self.wait(2)
        self.play(FadeIn(t8[3][0]),
                  TransformFromCopy(t7[3][1:], t8[3][1:]))
        self.wait(2)
        self.play(FadeIn(t8[4][0]),
                  TransformFromCopy(t7[4][1:], t8[4][1:]))
        self.wait(2)
        self.play(FadeIn(t8[5][0]),
                  TransformFromCopy(t7[5][1:], t8[5][1:]))
        self.wait(2)
        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)



        self.play(ReplacementTransform(t7[1].copy(), t8_aux_1))
        self.wait(2)
        self.play(LaggedStart(AnimationGroup(Succession(t8_aux_1[0][1].animate.shift(DOWN*0.1).rotate(5*DEGREES),
                                                        CounterclockwiseTransform(t8_aux_1[0][1], t8[1][0]))),
                              FadeIn(t8[1][2]),
                              lag_ratio=0.8))
        self.wait()


        self.add(t1)



# Derivadas de ordens maiores
class vid15(MovingCameraScene):
    def construct(self):

        self.camera.frame.save_state()

        X = ValueTracker(-0.3)
        
        # Função
        ax1 = Axes(x_range=[-1, 5], x_length=6,
                   y_range=[-1, 5], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        g_ax1 = VGroup(ax1, ax1_x_label, ax1_y_label)

        def f(x):
            return np.sin(1.3*x) + x/1.3

        gr1 = ax1.plot(f, x_range=[-0.3, 5], stroke_width=4, color=BLUE)
        gr1_label = MathTex('y = f(x)', color=BLUE).next_to(g_ax1, UP, buff=0)

                

        # 1a derivada
        ax2 = ax1.copy()
        ax2_x_label = ax1_x_label.copy()
        ax2_y_label = ax1_y_label.copy()

        g_ax2 = VGroup(ax2, ax2_x_label, ax2_y_label).next_to(g_ax1, RIGHT, buff=1)

        def f_prime1(x):
            return 1.3 * np.cos(1.3*x) + 1/1.3
        
        gr2 = always_redraw(lambda: ax2.plot(f_prime1, x_range=[-0.3, X.get_value()], stroke_width=4, color=GREEN))
        gr2_label = MathTex(r'y = f^\prime(x)', color=GREEN).next_to(g_ax2, UP, buff=0)
        


        # 2a derivada
        ax3 = ax1.copy()
        ax3_x_label = ax1_x_label.copy()
        ax3_y_label = ax1_y_label.copy()

        g_ax3 = VGroup(ax3, ax3_x_label, ax3_y_label).next_to(g_ax2, RIGHT, buff=1)

        def f_prime2(x):
            return -1.69 * np.sin(1.3*x)
        
        gr3 = always_redraw(lambda: ax3.plot(f_prime2, x_range=[-0.3, X.get_value()], stroke_width=4, color=ORANGE))
        gr3_label = MathTex(r'y = f^{\prime\prime}(x)', color=ORANGE).next_to(g_ax3, UP, buff=0)
        


        # 3a derivada
        ax4 = ax1.copy()
        ax4_x_label = ax1_x_label.copy()
        ax4_y_label = ax1_y_label.copy()

        g_ax4 = VGroup(ax4, ax4_x_label, ax4_y_label).next_to(g_ax3, RIGHT, buff=1)

        def f_prime3(x):
            return -2.197 * np.cos(1.3*x)
        
        gr4 = ax4.plot(f_prime3, x_range=[-0.3, 5], stroke_width=4, color=LIGHT_BROWN)
        gr4_label = MathTex(r'y = f^{\prime\prime\prime}(x)', color=LIGHT_BROWN).next_to(g_ax4, UP, buff=0)
        


        # 4a derivada
        ax5 = ax1.copy()
        ax5_x_label = ax1_x_label.copy()
        ax5_y_label = ax1_y_label.copy()

        g_ax5 = VGroup(ax5, ax5_x_label, ax5_y_label).next_to(g_ax4, RIGHT, buff=1)

        def f_prime4(x):
            return 2.8561 * np.sin(1.3*x)
        
        gr5 = ax5.plot(f_prime4, x_range=[-0.3, 5], stroke_width=4, color=RED)
        gr5_label = MathTex(r'y = f^{(4)}(x)', color=RED).next_to(g_ax5, UP, buff=0)
        


        # 5a derivada
        ax6 = ax1.copy()
        ax6_x_label = ax1_x_label.copy()
        ax6_y_label = ax1_y_label.copy()

        g_ax6 = VGroup(ax6, ax6_x_label, ax6_y_label).next_to(g_ax5, RIGHT, buff=1)

        def f_prime5(x):
            return 3.71293 * np.cos(1.3*x)
        
        gr6 = always_redraw(lambda: ax6.plot(f_prime5, x_range=[-0.3, 5], stroke_width=4, color=PURPLE))
        gr6_label = MathTex(r'y = f^{(5)}(x)', color=PURPLE).next_to(g_ax6, UP, buff=0)
        


        dot_1 = always_redraw(lambda: Dot(ax1.c2p(X.get_value(),f(X.get_value()),0), color=YELLOW).set_z_index(3))
        tg_line_1 = always_redraw(lambda: Line((0,0,0), (5,0,0), stroke_width=3, color=YELLOW).rotate(np.arctan(f_prime1(X.get_value()))).move_to(ax1.c2p(X.get_value(), f(X.get_value()), 0)).set_z_index(2))

        dot_2 = always_redraw(lambda: Dot(ax2.c2p(X.get_value(),f_prime1(X.get_value()),0), color=YELLOW).set_z_index(3))
        tg_line_2 = always_redraw(lambda: Line((0,0,0), (5,0,0), stroke_width=3, color=YELLOW).rotate(np.arctan(f_prime2(X.get_value()))).move_to(ax2.c2p(X.get_value(), f_prime1(X.get_value()), 0)).set_z_index(2))



        self.play(FadeIn(g_ax1, gr1, gr1_label))
        self.wait(2)
        self.add(g_ax2, gr2, gr2_label, dot_1, tg_line_1)
        self.play(LaggedStart(self.camera.frame.animate.scale(1.1).move_to((VGroup(g_ax1, g_ax2).get_x(),0,0)),
                              X.animate.set_value(5),
                              lag_ratio=0.3),
                              run_time=5)
        self.wait(2)
        self.remove(dot_1, tg_line_1, gr2)
        self.wait(2)
        self.add(g_ax3, gr3, gr3_label, dot_2, tg_line_2, gr2.copy())
        self.wait(2)
        X.set_value(-0.3)
        self.play(LaggedStart(self.camera.frame.animate.move_to((VGroup(g_ax2, g_ax3).get_x(),0,0)),
                              X.animate.set_value(5),
                              lag_ratio=0.3),
                              run_time=5)
        self.wait(2)
        self.remove(dot_2, tg_line_2)
        self.wait(2)
        self.play(LaggedStart(self.camera.frame.animate.scale(1.1).move_to((VGroup(g_ax3, g_ax4).get_x(),0,0)),
                              FadeIn(g_ax4, gr4, gr4_label, scale=1.2),
                              lag_ratio=0.1),
                              rate_func=linear,
                              run_time=3)
        self.wait(2)
        self.play(LaggedStart(self.camera.frame.animate.move_to((VGroup(g_ax4, g_ax5).get_x(),0,0)),
                              FadeIn(g_ax5, gr5, gr5_label, scale=1.2),
                              lag_ratio=0.1),
                              rate_func=linear,
                              run_time=3)
        self.wait(2)
        self.play(LaggedStart(self.camera.frame.animate.move_to((VGroup(g_ax5, g_ax6).get_x(),0,0)),
                              FadeIn(g_ax6, gr6, gr6_label, scale=1.2),
                              lag_ratio=0.1),
                              rate_func=linear,
                              run_time=3)           
        self.wait(2)
        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)



# Comentário sobre as derivadas de ordens maiores de um polinômio
class vid16(MovingCameraScene):
    def construct(self):

        t1 = MathTex(r'(x^n)^\prime = nx^{n-1}')

        self.play(FadeIn(t1))
        self.wait(2)
        self.play(Indicate(t1[0][2]))
        self.wait(2)
        self.play(Indicate(t1[0][8:11]))
        self.wait(2)
        self.play(FadeOut(t1))
        self.wait(2)



        # Função
        ax1 = Axes(x_range=[-4, 4], x_length=6,
                   y_range=[-3, 5], y_length=6,
                   axis_config={"include_ticks" : False}).set_color(GRAY).shift(DOWN*0.2)
        ax1_x_label = MathTex('x').set_color(GRAY).next_to(ax1.get_x_axis(), RIGHT).shift(DOWN*0.3+LEFT*0.2)
        ax1_y_label = MathTex('y').set_color(GRAY).next_to(ax1.get_y_axis(), LEFT).shift(UP*3+RIGHT*0.2)

        g_ax1 = VGroup(ax1, ax1_x_label, ax1_y_label)

        def f(x):
            return 0.1*x**4 - x**2 + 0.9

        gr1 = ax1.plot(f, x_range=[-3.5, 3.5], stroke_width=4, color=BLUE)
        gr1_label = MathTex('f(x) = x^4 - x^2 + 1', color=BLUE).next_to(g_ax1, UP, buff=0.5)

                

        # 1a derivada
        ax2 = ax1.copy()
        ax2_x_label = ax1_x_label.copy()
        ax2_y_label = ax1_y_label.copy()

        g_ax2 = VGroup(ax2, ax2_x_label, ax2_y_label).next_to(g_ax1, RIGHT, buff=1)

        def f_prime1(x):
            return 0.4*x**3 - 2*x
        
        gr2 = always_redraw(lambda: ax2.plot(f_prime1, x_range=[-2.8, 2.8], stroke_width=4, color=GREEN))
        gr2_label = MathTex(r'f^\prime(x) = 4x^3 - 2x', color=GREEN).next_to(g_ax2, UP, buff=0.5)
        


        # 2a derivada
        ax3 = ax1.copy()
        ax3_x_label = ax1_x_label.copy()
        ax3_y_label = ax1_y_label.copy()

        g_ax3 = VGroup(ax3, ax3_x_label, ax3_y_label).next_to(g_ax2, RIGHT, buff=1)

        def f_prime2(x):
            return 1.2*x**2 - 2
        
        gr3 = always_redraw(lambda: ax3.plot(f_prime2, x_range=[-2.1, 2.1], stroke_width=4, color=ORANGE))
        gr3_label = MathTex(r'f^{\prime\prime}(x) = 12x^2 - 2', color=ORANGE).next_to(g_ax3, UP, buff=0.5)
        


        # 3a derivada
        ax4 = ax1.copy()
        ax4_x_label = ax1_x_label.copy()
        ax4_y_label = ax1_y_label.copy()

        g_ax4 = VGroup(ax4, ax4_x_label, ax4_y_label).next_to(g_ax3, RIGHT, buff=1)

        def f_prime3(x):
            return 2.4*x
        
        gr4 = ax4.plot(f_prime3, x_range=[-1.25, 2], stroke_width=4, color=LIGHT_BROWN)
        gr4_label = MathTex(r'f^{\prime\prime\prime}(x) = 24x', color=LIGHT_BROWN).next_to(g_ax4, UP, buff=0.5)
        


        # 4a derivada
        ax5 = ax1.copy()
        ax5_x_label = ax1_x_label.copy()
        ax5_y_label = ax1_y_label.copy()

        g_ax5 = VGroup(ax5, ax5_x_label, ax5_y_label).next_to(g_ax4, RIGHT, buff=1)

        def f_prime4(x):
            return 2.4
        
        gr5 = ax5.plot(f_prime4, x_range=[-4, 4], stroke_width=4, color=RED)
        gr5_label = MathTex(r'f^{(4)}(x) = 24', color=RED).next_to(g_ax5, UP, buff=0.5)
        


        # 5a derivada
        ax6 = ax1.copy()
        ax6_x_label = ax1_x_label.copy()
        ax6_y_label = ax1_y_label.copy()

        g_ax6 = VGroup(ax6, ax6_x_label, ax6_y_label).next_to(g_ax5, RIGHT, buff=1)

        def f_prime5(x):
            return 0
        
        gr6 = always_redraw(lambda: ax6.plot(f_prime5, x_range=[-4, 4], stroke_width=4, color=PURPLE))
        gr6_label = MathTex(r'f^{(5)}(x) = 0', color=PURPLE).next_to(g_ax6, UP, buff=0.5)
        

        self.camera.frame.scale(1.1).shift(UP*0.5)
        self.play(FadeIn(g_ax1, gr1, gr1_label))
        self.wait(2)
        self.play(FadeIn(g_ax2, g_ax3, g_ax4, g_ax5, g_ax6,
                         gr2, gr3, gr4, gr5, gr6,
                         gr2_label, gr3_label, gr4_label, gr5_label, gr6_label))
        self.wait(2)
        self.play(self.camera.frame.animate.move_to((VGroup(g_ax5, g_ax6).get_x(),0.5,0)), 
                  run_time=15)
        self.wait(2)
        self.play(FadeOut(mob) for mob in self.mobjects)
        self.wait(2)
