# Função do 2° grau

from manim import *

# Introdução
class vid1(Scene):
    def construct(self):

        # Título
        t1 = Tex(r'Função do 2\textsuperscript{o} grau').scale(1).to_edge(UP)
        ul_t1 = Underline(t1)
        ul_t1_aux = Underline(t1[0][10:16])
        t2 = Tex(r'Função quadrática', color=GRAY).scale(1).next_to(ul_t1, DOWN)
        self.play(Succession(FadeIn(t1), Create(ul_t1)))
        self.wait(2)
        self.play(FadeIn(t2))
        self.wait(2)
        self.play(FadeOut(t2))
        self.wait(2)



        # Definição de função do 1o grau
        t3 = MathTex(r'f: \mathbb{R} \to \mathbb{R}',' \:\:\:,\:\:\: f(x) = ax^2 + bx + c').scale(0.9)
        t3_box = SurroundingRectangle(t3, buff=0.15, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-2)
        self.play(Write(t3[0]))
        self.wait(2)
        self.play(Write(t3[1]))
        self.play(FadeIn(t3_box))
        self.wait(2)



        #a,b,c são reais e 'a' é diferente de zero
        t4 = MathTex(r'a,b,c \in \mathbb{R}', color=YELLOW).scale(0.8).next_to(t3, DOWN).shift(RIGHT*2.1)
        t5 = MathTex(r'a \neq 0', color=YELLOW).scale(0.8).next_to(t3, DOWN).shift(RIGHT*2.1)
        self.play(t3[1][6].animate.set_color(YELLOW),
                  t3[1][10].animate.set_color(YELLOW), 
                  t3[1][13].animate.set_color(YELLOW),
                  FadeIn(t4))
        self.wait(2)
        self.play(t3[1][10].animate.set_color(WHITE), 
                  t3[1][13].animate.set_color(WHITE),
                  FadeOut(t4))
        self.play(FadeIn(t5))
        self.wait(2)



        # Se 'a' fosse igual a zero...
        t6 = MathTex('f(x) = 0x^2 + bx + c').scale(0.9).move_to(t3, aligned_edge=RIGHT)
        t6[0][5].set_color(YELLOW)
        t7 = MathTex('f(x) = bx + c').scale(0.9).move_to(t6, aligned_edge=LEFT)
        self.play(TransformMatchingShapes(t3[1][6:10], t6[0][5:9]))
        #self.remove(t3[1][10:14])
        self.play(LaggedStart(FadeOut(t6[0][5:9]), 
                              TransformMatchingShapes(t3[1][10:14], t7[0][5:9]), 
                              lag_ratio=0.5))
        self.wait(2)
        t3[1][6].set_color(WHITE)
        self.play(Succession(FadeOut(t5, t7[0][5:9]), FadeIn(t3[1][6:14])))
        self.wait(2)



        # Sobre o nome "1o grau"
        self.play(Indicate(t1[0][10:16], scale_factor=1), Indicate(ul_t1_aux, scale_factor=1))
        self.remove(ul_t1_aux)
        self.wait(2)
        self.play(t3[1][6:14].animate.set_color(YELLOW))
        self.wait(2)



        # 'a' e 'b' assumindo diferentes valores
        t8 = MathTex('f(x) = 1x^2 + 3x + 2').scale(0.9).move_to(t6, aligned_edge=LEFT)
        t8[0][5].set_color(YELLOW)
        t8[0][9].set_color(YELLOW)
        t8[0][12].set_color(YELLOW)
        t9 = MathTex('f(x) = 3x^2 + 4x - 1').scale(0.9).move_to(t6, aligned_edge=LEFT)
        t9[0][5].set_color(YELLOW)
        t9[0][9].set_color(YELLOW)
        t9[0][12].set_color(YELLOW)
        t10 = MathTex(r'f(x) = \sqrt{\pi}x^2 + \sqrt{e}').scale(0.9).move_to(t6, aligned_edge=LEFT)
        t10[0][5:8].set_color(YELLOW)
        t10[0][11:14].set_color(YELLOW)
        self.play(t3[1][7:10].animate.set_color(WHITE),
                  t3[1][11:13].animate.set_color(WHITE))
        self.wait(2)
        self.play(ReplacementTransform(t3[1][6:14], t8[0][5:13]))
        #self.wait(0.5)
        self.play(ReplacementTransform(t8[0][5:13], t9[0][5:13]))
        #self.wait(0.5)
        self.play(ReplacementTransform(t9[0][5:13], t10[0][5:17]))
        #self.wait(0.5)

        t11 = MathTex(r'f: \mathbb{R} \to \mathbb{R}',' \:\:\:,\:\:\: f(x) = ax^2 + bx + c').scale(0.9)
        self.play(ReplacementTransform(t10[0][5:17], t11[1][6:14]))
        self.wait(2)



# Começar com y = x^2
class vid2(Scene):
    def construct(self):

        # Retomando elementos
        t1 = Tex(r'Função do 2\textsuperscript{o} grau').scale(1).to_edge(UP)
        ul_t1 = Underline(t1)
        t3 = MathTex(r'f: \mathbb{R} \to \mathbb{R}',' \:\:\:,\:\:\: f(x) = ax^2 + bx + c').scale(0.9)
        t3_box = SurroundingRectangle(t3, buff=0.15, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-2)
        g_aux1 = VGroup(t1, ul_t1, t3, t3_box)
        self.add(g_aux1)
        self.play(g_aux1.animate.shift(UP*3))
        self.wait(2)



        # Função y = x^2
        t4_0 = MathTex(r'f(x) = x^2').scale(0.9)
        t4 = MathTex(r'y = x^2').scale(0.9).shift(UP*3)
        t5 = MathTex('a &= 1',
                     r'\\ b &= 0',
                     r'\\ c &= 0', color=YELLOW).scale(0.9).next_to(t4_0, RIGHT, buff=0.8)
        indicative_arrow_0 = Arrow(DOWN, UP*0.5).rotate(30*DEGREES).shift(DOWN*0.6+LEFT*0.1)
        self.play(FadeIn(t4_0))
        self.wait(2)
        self.play(FadeIn(t5[0]))
        self.wait(2)
        self.play(FadeIn(t5[1:3]))
        self.wait(2)
        self.play(FadeIn(indicative_arrow_0))
        self.wait(2)
        self.play(indicative_arrow_0.animate.shift(RIGHT*1.1))
        self.wait(2)
        self.play(FadeOut(t5[0], t5[1:3], g_aux1, indicative_arrow_0))
        
        black_sq_1 = Square(color=BLACK, fill_opacity=1).scale(2).next_to(t4, UP, buff=0.1).set_z_index(2)
        black_sq_2 = Square(color=BLACK, fill_opacity=1).next_to(t4, DOWN, buff=0.1).set_z_index(2)
        t4[0][0].shift(DOWN)
        self.play(t4_0.animate.move_to(t4[0][1:4], aligned_edge=UR))
        self.add(black_sq_1, black_sq_2, t4[0][0])
        self.play(t4_0[0][0:4].animate.shift(UP),
                  t4[0][0].animate.shift(UP))
        self.wait(2)
        
        

        # Gráfico
        axes = Axes(x_range = [-6, 6, 1],
                    y_range = [-2, 11, 1],
                    x_length = 5,
                    y_length = 5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        x_label = MathTex("x").next_to(axes.get_x_axis(), DR, buff = 0)
        y_label = MathTex("y").next_to(axes.get_y_axis(), UL, buff = 0).shift(DOWN*0.1)
        axes_labels = VGroup(x_label, y_label).set_color(WHITE).set_opacity(0.6)
        axes_zero = MathTex('0').set_opacity(0.6).scale(0.8).next_to(axes.coords_to_point(0,0,0), DL, buff = 0.13)
        
        graph = axes.plot(lambda x: x ** 2,
                            x_range=[-3, 3], stroke_width = 4).set_color(BLUE)
        graph_pos = axes.plot(lambda x: x ** 2,
                            x_range=[0, 3], stroke_width = 4).set_color(BLUE)
        graph_neg = graph_pos.copy()

        dot_neg1 = Dot(axes.coords_to_point(-1,1,0))
        dot_neg2 = Dot(axes.coords_to_point(-2,4,0))
        dot_neg3 = Dot(axes.coords_to_point(-3,9,0))
        dot_0 = Dot(axes.coords_to_point(0,0,0))
        dot_pos1 = Dot(axes.coords_to_point(1,1,0))
        dot_pos2 = Dot(axes.coords_to_point(2,4,0))
        dot_pos3 = Dot(axes.coords_to_point(3,9,0))
        dots = VGroup(dot_neg1, 
                      dot_neg2, 
                      dot_neg3, 
                      dot_0, 
                      dot_pos1, 
                      dot_pos2, 
                      dot_pos3).set_color(YELLOW)

        dot_x_line_pos1 = DashedLine(dot_pos1, axes.coords_to_point(1,0,0))
        dot_x_line_pos2 = DashedLine(dot_pos2, axes.coords_to_point(2,0,0))
        dot_x_line_pos3 = DashedLine(dot_pos3, axes.coords_to_point(3,0,0))
        dot_x_line_neg1 = dot_x_line_pos1.copy().next_to(axes.coords_to_point(-1,0,0), UP, buff=0)
        dot_x_line_neg2 = dot_x_line_pos2.copy().next_to(axes.coords_to_point(-2,0,0), UP, buff=0)
        dot_x_line_neg3 = dot_x_line_pos3.copy().next_to(axes.coords_to_point(-3,0,0), UP, buff=0)
        dots_x_lines = VGroup(dot_x_line_pos1,
                              dot_x_line_pos2,
                              dot_x_line_pos3,
                              dot_x_line_neg1,
                              dot_x_line_neg2,
                              dot_x_line_neg3).set_color(GRAY).set_z_index(-1)

        dot_y_line_pos1 = DashedLine(dot_pos1, axes.coords_to_point(0,1,0))
        dot_y_line_pos2 = DashedLine(dot_pos2, axes.coords_to_point(0,4,0))
        dot_y_line_pos3 = DashedLine(dot_pos3, axes.coords_to_point(0,9,0))
        dot_y_line_neg1 = dot_y_line_pos1.copy().next_to(axes.coords_to_point(0,1,0), LEFT, buff=0)
        dot_y_line_neg2 = dot_y_line_pos2.copy().next_to(axes.coords_to_point(0,4,0), LEFT, buff=0)
        dot_y_line_neg3 = dot_y_line_pos3.copy().next_to(axes.coords_to_point(0,9,0), LEFT, buff=0)
        dots_y_lines = VGroup(dot_y_line_pos1,
                              dot_y_line_pos2,
                              dot_y_line_pos3,
                              dot_y_line_neg1,
                              dot_y_line_neg2, 
                              dot_y_line_neg3).set_color(GRAY).set_z_index(-1)

        dot_0_label = MathTex('(0,0)').scale(0.8).next_to(dot_0, DR, buff = 0.13)
        dot_pos1_label = MathTex('(1,1)').scale(0.8).next_to(dot_pos1, RIGHT, buff = 0.13)
        dot_pos2_label = MathTex('(2,4)').scale(0.8).next_to(dot_pos2, RIGHT, buff = 0.13)
        dot_pos3_label = MathTex('(3,9)').scale(0.8).next_to(dot_pos3, RIGHT, buff = 0.13)
        dot_neg1_label = MathTex('(-1,1)').scale(0.8).next_to(dot_neg1, LEFT, buff = 0.13)
        dot_neg2_label = MathTex('(-2,4)').scale(0.8).next_to(dot_neg2, LEFT, buff = 0.13)
        dot_neg3_label = MathTex('(-3,9)').scale(0.8).next_to(dot_neg3, LEFT, buff = 0.13)
        dots_labels = VGroup(dot_0_label,
                             dot_pos1_label,
                             dot_pos2_label,
                             dot_pos3_label,
                             dot_neg1_label,
                             dot_neg2_label,
                             dot_neg3_label).set_color(YELLOW)

        g_graph = VGroup(axes, axes_labels, axes_zero, graph, graph_pos, graph_neg, 
                         dots, dots_x_lines, dots_y_lines, dots_labels).move_to(ORIGIN).shift(DOWN*0.7)

        

        # Todos os pontos do gráfico são da forma (x,x^2)
        t6 = MathTex('(x,x^2)').scale(0.9).shift(RIGHT*3)
        self.play(FadeIn(t6, axes, axes_labels, axes_zero))
        self.wait()

        indicative_arrow_1 = Arrow(DOWN, UP*0.5).rotate(30*DEGREES).shift(DOWN*0.5+RIGHT*3.4)
        self.play(FadeIn(indicative_arrow_1))
        self.wait()
        self.play((indicative_arrow_1.animate.shift(LEFT*0.4)))
        self.wait()
        self.play(FadeOut(indicative_arrow_1, t6))
        self.wait()

        

        # Alguns pontos que pertencem ao gráfico
        self.play(GrowFromCenter(dot_0), FadeIn(dot_0_label))
        self.wait()
        self.play(dot_0.animate.set_color(BLUE), FadeOut(dot_0_label),
                  GrowFromCenter(dot_pos1), FadeIn(dot_pos1_label, dot_x_line_pos1, dot_y_line_pos1))
        self.wait()
        self.play(dot_pos1.animate.set_color(BLUE), FadeOut(dot_pos1_label),
                  GrowFromCenter(dot_pos2), FadeIn(dot_pos2_label, dot_x_line_pos2, dot_y_line_pos2))
        self.wait()
        self.play(dot_pos2.animate.set_color(BLUE), FadeOut(dot_pos2_label),
                  GrowFromCenter(dot_pos3), FadeIn(dot_pos3_label, dot_x_line_pos3, dot_y_line_pos3))
        self.play(dot_pos3.animate.set_color(BLUE), FadeOut(dot_pos3_label))
        self.wait()



        # Adicionando mais pontos para formar a curva (apenas da parte positva)
        extra_dot_1 = Dot(graph.get_point_from_function(t=0.6))
        extra_dot_2 = Dot(graph.get_point_from_function(t=1.35))
        extra_dot_3 = Dot(graph.get_point_from_function(t=1.7))
        extra_dot_4 = Dot(graph.get_point_from_function(t=2.25))
        extra_dot_5 = Dot(graph.get_point_from_function(t=2.5))
        extra_dot_6 = Dot(graph.get_point_from_function(t=2.75))
        extra_dots = VGroup(extra_dot_1, 
                            extra_dot_2, 
                            extra_dot_3,
                            extra_dot_4,
                            extra_dot_5,
                            extra_dot_6).set_color(BLUE)
        self.play(Create(extra_dots), run_time=2)
        self.wait()
        self.play(FadeOut(extra_dots), FadeIn(graph_pos))
        self.wait()



        # Pontos para valores negativos de 'x'
        t7 = MathTex(r'(-a)^2 &= a^2',
                     r'\\(-2)^2 &= 2^2 = 4').scale(0.9).shift(LEFT*3.5)
        self.play(FadeIn(t7[0][0:5]))
        self.wait()
        self.play(FadeIn(t7[0][5:8]))
        self.wait()
        self.play(FadeIn(t7[1][0:5]))
        self.wait()
        self.play(FadeIn(t7[1][5:8]))
        self.wait()
        self.play(FadeIn(t7[1][8:10]))
        self.wait()
        self.play(FadeOut(t7))
        self.wait()



        # Pontos da função à esquerda da origem
        self.play(GrowFromCenter(dot_neg1), FadeIn(dot_neg1_label, dot_x_line_neg1, dot_y_line_neg1))
        self.wait()
        self.play(dot_neg1.animate.set_color(BLUE), FadeOut(dot_neg1_label),
                  GrowFromCenter(dot_neg2), FadeIn(dot_neg2_label, dot_x_line_neg2, dot_y_line_neg2))
        self.wait()
        self.play(dot_neg2.animate.set_color(BLUE), FadeOut(dot_neg2_label),
                  GrowFromCenter(dot_neg3), FadeIn(dot_neg3_label, dot_x_line_neg3, dot_y_line_neg3))
        self.play(dot_neg3.animate.set_color(BLUE), FadeOut(dot_neg3_label))
        self.wait()



        # O gráfico é simétrico em relação ao eixo 'y'
        self.play(Rotate(graph_neg, 180*DEGREES, axis=Y_AXIS, about_point=axes.coords_to_point(0,0,0)),
                  run_time=2)
        self.wait()
        self.play(FadeOut(dots, dots_x_lines, dots_y_lines))
        self.wait()



        # y = x^2 é função par
        t8 = Tex('é função par').scale(0.9).next_to(t4, RIGHT, buff=0.3)
        self.play(Write(t8))
        self.wait()
        self.play(FadeOut(t8))
        self.wait()



# Sobre o formato do gráfico: parábola
class vid3(Scene):
    def construct(self):

        # Função y = x^2
        t4 = MathTex(r'y = x^2').scale(0.9).shift(UP*3)
        self.add(t4)

        

        # Gráfico
        axes = Axes(x_range = [-6, 6, 1],
                    y_range = [-2, 11, 1],
                    x_length = 5,
                    y_length = 5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        x_label = MathTex("x").next_to(axes.get_x_axis(), DR, buff = 0)
        y_label = MathTex("y").next_to(axes.get_y_axis(), UL, buff = 0).shift(DOWN*0.1)
        axes_labels = VGroup(x_label, y_label).set_color(WHITE).set_opacity(0.6)
        axes_zero = MathTex('0').set_opacity(0.6).scale(0.8).next_to(axes.coords_to_point(0,0,0), DL, buff = 0.13)
        
        graph = axes.plot(lambda x: x ** 2,
                            x_range=[-3, 3], stroke_width = 4).set_color(BLUE).set_z_index(3)
        graph_2 = axes.plot(lambda x: x ** 2,
                            x_range=[-3, 3], stroke_width = 4).set_color(YELLOW).set_z_index(3)
        graph_3 = axes.plot(lambda x: x ** 2,
                            x_range=[-3, 3], stroke_width = 4).set_color(BLUE).set_z_index(3)

        g_graph = VGroup(axes, axes_labels, axes_zero, graph, graph_2, graph_3).move_to(ORIGIN).shift(DOWN*0.7)
        self.add(g_graph).remove(graph_2, graph_3)



        # Destaque na forma do gráfico
        self.play(LaggedStart(Create(graph_2),
                              Create(graph_3),
                              lag_ratio=0.2))
        self.wait()
        self.play(FadeOut(axes, axes_labels, axes_zero, t4))
        self.wait()

        t5 = Tex('Parábola', color=BLUE).scale(0.9).next_to(graph, UP, buff=1.5)
        axis_of_symmetry = DashedVMobject(Line(UP, DOWN, color=YELLOW).scale(2.8)).set_z_index(3).move_to(axes.get_y_axis())
        self.play(FadeIn(t5))
        self.wait()
        self.play(FadeIn(axis_of_symmetry))
        self.wait()

        self.play(t5.animate.shift(UP*1.8))
        self.play(FadeIn(axes, axes_labels, axes_zero, t4))
        self.wait()
        self.play(Indicate(axis_of_symmetry, scale_factor=1.1))
        self.wait()
        g_y_axis = VGroup(axes.get_y_axis(), y_label)
        self.play(Indicate(g_y_axis, scale_factor=1.1))
        self.wait()



        # A parábola se move no plano
        g_aux1 = VGroup(graph, axis_of_symmetry)
        self.remove(graph_2, graph_3)
        self.play(FadeOut(t4), g_aux1.animate.shift(LEFT*1), run_time=1.5)
        self.wait()
        self.play(g_aux1.animate.shift(RIGHT*2.5+UP*1), run_time=2)
        self.wait()
        self.play(g_aux1.animate.shift(LEFT*1+DOWN*1.5), run_time=2)
        self.wait()

     

# Todas as funções têm forma de parábola / concavidade / vértice
class vid4(Scene):
    def construct(self):

        axes = Axes(x_range = [-6, 6, 1],
                    y_range = [-2, 11, 1],
                    x_length = 5,
                    y_length = 5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.5)

        axes_1 = axes.copy()
        graph_1 = axes.plot(lambda x: x**2 + 4*x + 3,
                         x_range=[-5.2, 1.2], stroke_width = 4).set_color(RED).set_z_index(2)
        vertex_1 = Dot(graph_1.get_point_from_function(t=-2)).scale(1.3).set_color(YELLOW)
        g_1 = VGroup(axes_1, graph_1, vertex_1)


        axes_2 = axes.copy()
        graph_2 = axes.plot(lambda x: -x**2 + 5*x,
                         x_range=[-0.3, 5.3], stroke_width = 4).set_color(GREEN).set_z_index(2)
        vertex_2 = Dot(graph_2.get_point_from_function(t=2.5)).scale(1.3).set_color(YELLOW)
        g_2 = VGroup(axes_2, graph_2, vertex_2)


        axes_3 = axes.copy()
        graph_3 = axes.plot(lambda x: 0.3*x**2 + 2,
                         x_range=[-5, 5], stroke_width = 4).set_color(BLUE).set_z_index(2)
        vertex_3 = Dot(graph_3.get_point_from_function(t=0)).scale(1.3).set_color(YELLOW)
        g_3 = VGroup(axes_3, graph_3, vertex_3)


        g_0 = VGroup(g_1, g_2, g_3).arrange(RIGHT, buff=1).scale(0.7).shift(DOWN*0.3).set_z_index(6)


        box_1 = SurroundingRectangle(g_1, buff=0.3, color=GRAY, stroke_width=2)
        box_2 = SurroundingRectangle(g_2, buff=0.3, color=GRAY, stroke_width=2)
        box_3 = SurroundingRectangle(g_3, buff=0.3, color=GRAY, stroke_width=2)
        boxes = VGroup(box_1, box_2, box_3).set_z_index(6)


        label_1 = MathTex('y = x^2 + 4x + 3').scale(0.8).next_to(g_1, UP, buff=0.5).set_color(RED)
        label_2 = MathTex('y = -x^2 + 5x').scale(0.8).next_to(g_2, UP, buff=0.5).set_color(GREEN)
        label_3 = MathTex('y = 0.3x^2 + 2').scale(0.8).next_to(g_3, UP, buff=0.5).set_color(BLUE)
        labels = VGroup(label_1, label_2, label_3).set_z_index(6)
        

        self.play(FadeIn(axes_1, graph_1, box_1, label_1))
        self.wait(2)
        self.play(FadeIn(axes_2, graph_2, box_2, label_2))
        self.wait(2)
        self.play(FadeIn(axes_3, graph_3, box_3, label_3))
        self.wait(2)



        # Concavidade
        t1 = Tex('Concavidade', color=YELLOW).scale(0.9).shift(UP*3.2)
        indicative_arrow_1 = Arrow(UP, DOWN*0.5, color=YELLOW).next_to(graph_1, UP, buff=-1.8)
        indicative_arrow_2 = indicative_arrow_1.copy().rotate(180*DEGREES).next_to(graph_2, DOWN, buff=-1.2)
        indicative_arrow_3 = indicative_arrow_1.copy().next_to(graph_3, UP, buff=-1.2)
        indicative_arrows1 = VGroup(indicative_arrow_1, indicative_arrow_2, indicative_arrow_3)
        
        self.play(LaggedStart(FadeIn(indicative_arrow_1),
                              FadeIn(indicative_arrow_2),
                              FadeIn(indicative_arrow_3)))
        self.wait(2)
        self.play(FadeIn(t1))
        self.wait(2)
        self.play(FadeOut(t1, indicative_arrows1))
        self.wait(2)


        # Concavidade para cima / para baixo
        black_sq_1 = Rectangle(height=2, width=1, color=BLACK, fill_opacity=0.8, stroke_width=0).scale(4.2).set_z_index(7).move_to(box_1)
        black_sq_2 = Rectangle(height=2, width=1, color=BLACK, fill_opacity=0.8, stroke_width=0).scale(4.2).set_z_index(7).move_to(box_2)
        black_sq_3 = Rectangle(height=2, width=1, color=BLACK, fill_opacity=0.8, stroke_width=0).scale(4.2).set_z_index(7).move_to(box_3)

        self.play(FadeIn(black_sq_2))
        self.wait(2)
        self.play(LaggedStart(FadeOut(black_sq_2),
                              FadeIn(black_sq_1, black_sq_3),
                              lag_ratio=0.2))
        self.wait(2)
        self.play(FadeOut(black_sq_1, black_sq_3))
        self.wait(2)


        self.add(boxes, labels, g_0)

        # Vértice: o ponto da parábola por onde passa a linha de simetria
        t2 = Tex('Vértice', color=YELLOW).scale(0.9).shift(UP*3.2).set_z_index(3)
        indicative_arrow_4 = Arrow(UP, DOWN*0.5, color=YELLOW).rotate(135*DEGREES).next_to(vertex_1, DL, buff=0.1)
        indicative_arrow_5 = Arrow(UP, DOWN*0.5, color=YELLOW).rotate(-45*DEGREES).next_to(vertex_2, UR, buff=0.1)
        indicative_arrow_6 = Arrow(UP, DOWN*0.5, color=YELLOW).rotate(225*DEGREES).next_to(vertex_3, DR, buff=0.1)
        indicative_arrows2 = VGroup(indicative_arrow_4, indicative_arrow_5, indicative_arrow_6)

        self.play(GrowFromCenter(vertex_1),
                  GrowFromCenter(vertex_2),
                  GrowFromCenter(vertex_3))
        self.play(FadeIn(t2, 
                         indicative_arrow_4, 
                         indicative_arrow_5, 
                         indicative_arrow_6))
        self.wait(2)
        self.play(FadeOut(indicative_arrows2))
        self.wait(2)



        axis_of_symmetry_1 = DashedVMobject(Line(UP, DOWN, color=YELLOW).scale(1.75)).set_z_index(3).move_to(axes_1.coords_to_point(-2, 4.5, 0))
        axis_of_symmetry_2 = DashedVMobject(Line(UP, DOWN, color=YELLOW).scale(1.75)).set_z_index(3).move_to(axes_2.coords_to_point(2.5, 4.5, 0))
        axis_of_symmetry_3 = DashedVMobject(Line(UP, DOWN, color=YELLOW).scale(1.75)).set_z_index(3).move_to(axes_3.coords_to_point(0, 4.5, 0))
        axes_of_symmetry = VGroup(axis_of_symmetry_1, axis_of_symmetry_2, axis_of_symmetry_3)  
        
        self.play(FadeIn(axes_of_symmetry))
        self.wait(2)



        # O vértice é ora o máximo ora o mínimo das funções
        vertex_1_y_line = DashedLine(LEFT, RIGHT).scale(1.6).move_to(axes_1.coords_to_point(0,-1,0))
        vertex_2_y_line = vertex_1_y_line.copy().move_to(axes_2.coords_to_point(0,6.25,0))
        vertex_3_y_line = vertex_1_y_line.copy().move_to(axes_3.coords_to_point(0,2,0))
        vertices_y_lines = VGroup(vertex_1_y_line, vertex_2_y_line, vertex_3_y_line).set_color(GRAY).set_z_index(-1)

        min_label_1 = Tex('\it mín.', color=GRAY).scale(0.7).next_to(vertex_1_y_line, DOWN, buff=0.1, aligned_edge=RIGHT)
        max_label_2 = Tex('\it máx.', color=GRAY).scale(0.7).next_to(vertex_2_y_line, UP, buff=0.1, aligned_edge=LEFT)
        min_label_3 = min_label_1.copy().next_to(vertex_3_y_line, DOWN, buff=0.1, aligned_edge=RIGHT)
        max_min_labels = VGroup(min_label_1, max_label_2, min_label_3)

        self.play(FadeIn(black_sq_2), FadeOut(axes_of_symmetry))
        self.wait(2)
        self.play(FadeIn(vertex_1_y_line, vertex_3_y_line))
        self.wait(2)
        self.play(LaggedStart(FadeOut(black_sq_2),
                              FadeIn(black_sq_1, black_sq_3),
                              lag_ratio=0.2))
        self.wait(2)
        self.play(FadeIn(vertex_2_y_line))
        self.wait(2)
        self.play(FadeOut(black_sq_1, black_sq_3))
        self.wait(2)
        self.play(LaggedStart(FadeIn(min_label_1),
                              FadeIn(max_label_2),
                              FadeIn(min_label_3),
                              lag_ratio=0.5))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)
     


# Raízes
class vid5(MovingCameraScene):
    def construct(self):

        axes = Axes(x_range = [-1, 7, 1],
                    y_range = [-1, 9, 1],
                    x_length = 5,
                    y_length = 5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
    

        axes_1 = axes.copy()
        graph_1 = axes.plot(lambda x: (x - 3)**2 - 1,
                         x_range=[0.5, 5.5], stroke_width = 5).set_color(RED).set_z_index(2)
        root_1a = Dot(graph_1.get_point_from_function(t=2)).scale(1).set_color(YELLOW)
        root_1b = Dot(graph_1.get_point_from_function(t=4)).scale(1).set_color(YELLOW)
        root_1a_label = MathTex('2').scale(0.8).next_to(axes_1.coords_to_point(2,0,0), DL, buff = 0.13).set_opacity(0.6)
        root_1b_label = MathTex('4').scale(0.8).next_to(axes_1.coords_to_point(4,0,0), DR, buff = 0.13).set_opacity(0.6)
        g_1 = VGroup(axes_1, graph_1, root_1a, root_1b, root_1a_label, root_1b_label)


        axes_2 = axes.copy()
        graph_2 = axes.plot(lambda x: (x - 3)**2,
                         x_range=[0.5, 5.5], stroke_width = 5).set_color(GREEN).set_z_index(2)
        root_2 = Dot(graph_2.get_point_from_function(t=3)).scale(1).set_color(YELLOW)
        root_2_label = MathTex('3').scale(0.8).next_to(axes_2.coords_to_point(3,0,0), DOWN, buff = 0.17).set_opacity(0.6)
        g_2 = VGroup(axes_2, graph_2, root_2, root_2_label)


        axes_3 = axes.copy()
        graph_3 = axes.plot(lambda x: (x - 3)**2 + 1,
                         x_range=[0.5, 5.5], stroke_width = 5).set_color(BLUE).set_z_index(2)
        g_3 = VGroup(axes_3, graph_3)


        g_0 = VGroup(g_1, g_2, g_3).arrange(RIGHT, buff=1).scale(0.9).shift(DOWN*0.3).set_z_index(6)



        box_1 = SurroundingRectangle(g_1, buff=0.3, color=GRAY, stroke_width=2)
        box_2 = SurroundingRectangle(g_2, buff=0.3, color=GRAY, stroke_width=2)
        box_3 = SurroundingRectangle(g_3, buff=0.3, color=GRAY, stroke_width=2)
        boxes = VGroup(box_1, box_2, box_3).set_z_index(6)



        self.camera.frame.save_state()
        self.camera.frame.move_to(g_1).shift(UP*0)

        t1 = Tex('Raízes', color=YELLOW).scale(0.9).next_to(g_1, UP, buff=0.85).set_z_index(8)
        label_1 = MathTex('y = x^2 - 6x + 8','=0', color=RED).scale(0.9).next_to(box_1, DOWN, buff=0.1).shift(RIGHT*0.5).set_z_index(3)
        label_2 = MathTex('y = x^2 - 6x + 9','=0', color=GREEN).scale(0.9).next_to(box_2, DOWN, buff=0.1).shift(RIGHT*0.5).set_z_index(3)
        label_3 = MathTex('y = x^2 - 6x + 10','=0', color=BLUE).scale(0.9).next_to(box_3, DOWN, buff=0.1).shift(RIGHT*0.5).set_z_index(3)

        self.play(FadeIn(t1, axes_1, graph_1, label_1[0], box_1))
        self.wait()
        self.play(LaggedStart(GrowFromCenter(root_1a), 
                              GrowFromCenter(root_1b),
                              lag_ratio=0.2))
        self.wait()



        # Há 3 situações possíveis: 2 raízes, 1 raiz, 0 raízes
        black_sq_1 = Rectangle(height=2, width=1, color=BLACK, fill_opacity=0.8, stroke_width=0).scale(5.2).set_z_index(7).move_to(g_1)
        black_sq_2 = black_sq_1.copy().move_to(g_2)
        black_sq_3 = black_sq_1.copy().move_to(g_3)

        self.play(LaggedStart(Flash(root_1a, num_lines=8),     # primeira   
                              Flash(root_1b, num_lines=8),
                              lag_ratio=0.2))
        self.wait()



        self.play(self.camera.frame.animate.move_to(g_2).shift(UP*0),     # segunda
                  t1.animate.next_to(g_2, UP, buff=0.85),
                  FadeIn(black_sq_1),
                  FadeIn(axes_2, graph_2, root_2, label_2[0], box_2),
                  run_time=2)
        self.wait()
        self.play(Flash(root_2, num_lines=8))
        self.wait()



        self.play(self.camera.frame.animate.move_to(g_3).shift(UP*0),     # terceira
                  t1.animate.next_to(g_3, UP, buff=0.85),
                  FadeIn(black_sq_2),
                  FadeIn(g_3, label_3[0], box_3),
                  run_time=2)
        self.wait()



        # A câmera se afasta para mostrar as 3 funções
        self.play(FadeOut(black_sq_1, black_sq_2),
                  self.camera.frame.animate.move_to(g_2).shift(UP*0).scale(1.2),
                  t1.animate.next_to(g_2, UP, buff=1.5).scale(1.2),
                  run_time=2)
        self.wait()
        label_1[1].shift(LEFT*0.5)
        label_2[1].shift(LEFT*0.5)
        label_3[1].shift(LEFT*0.5)



        # Igualando as expressões a zero para encontrar o valor das raízes
        self.play(self.camera.frame.animate.shift(DOWN*7),
                  label_1[0].animate.shift(LEFT*0.5),
                  label_2[0].animate.shift(LEFT*0.5),
                  label_3[0].animate.shift(LEFT*0.5),
                  run_time=2)
        self.camera.frame.save_state()
        self.play(LaggedStart(Write(label_1[1]),
                              Write(label_2[1]),
                              Write(label_3[1]),
                              lag_ratio=0.2))
        self.wait()
        '''self.play(FadeOut(g_1, box_1,
                          g_2, box_2,
                          g_3, box_3))'''
    

        
        arrow_1 = MathTex(r'\Rightarrow', color=RED).scale(0.9).rotate(-90*DEGREES).next_to(label_1, DOWN, buff=0.2)
        arrow_2 = MathTex(r'\Rightarrow', color=GREEN).scale(0.9).rotate(-90*DEGREES).next_to(label_2, DOWN, buff=0.2)
        arrow_3 = MathTex(r'\Rightarrow', color=BLUE).scale(0.9).rotate(-90*DEGREES).next_to(label_3, DOWN, buff=0.2)

        result_1a = MathTex(r'x_{1} = 4', color=RED).scale(0.9).next_to(arrow_1, DOWN, buff=0.2)
        result_1b = MathTex(r'x_{2} = 2', color=RED).scale(0.9).next_to(result_1a, DOWN, buff=0.2)
        result_2 = MathTex('x = 3', color=GREEN).scale(0.9).next_to(arrow_2, DOWN, buff=0.2)
        result_3 = Tex('sem solução', color=BLUE).scale(0.9).next_to(arrow_3, DOWN, buff=0.2)
        
        self.play(LaggedStart(FadeIn(arrow_1, result_1a, result_1b),
                              FadeIn(arrow_2, result_2),
                              FadeIn(arrow_3, result_3),
                              lag_ratio=0.5))
        self.wait()



        # De forma geral, a eq. do 2o grau é resolvida pela fórmula resolutiva
        t2 = MathTex('ax^2 + bx + c = 0',
                     r'\:\:\:\:\Rightarrow\:\:\:\:',
                     r'x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}').scale(1.1).shift(DOWN*8.5)
        t3 = Tex('Fórmula ','Resolutiva', color=GRAY).next_to(t2[2], DOWN, buff=0.5)
        t4 = Tex('de Bhaskara', color=GRAY).move_to(t3[1], aligned_edge=LEFT)
        
        self.play(FadeIn(t2[0]))
        self.wait()
        self.play(LaggedStart(FadeIn(t2[1]),
                              FadeIn(t2[2], t3),
                              lag_ratio=0.5))
        self.wait()
        black_sq_aux = Square(color=BLACK, fill_opacity=1).scale(2).next_to(t3[1], DOWN, buff=0.1).set_z_index(2)
        self.add(black_sq_aux)
        self.play(LaggedStart(t3[1].animate.shift(DOWN*2), 
                              FadeIn(t4)))
        self.remove(t3[1], black_sq_aux)
        self.wait()
        self.play(FadeOut(t3[0], t4))
        self.wait()



        # A fórmula fornece dois valores para 'x'
        t5 = MathTex(r'x_{1} =',r'\frac{-b + \sqrt{b^2 - 4ac}}{2a}')
        t6 = MathTex(r'x_{2} =',r'\frac{-b - \sqrt{b^2 - 4ac}}{2a}')
        t5[1][2].set_color(YELLOW)
        t6[1][2].set_color(YELLOW)
        g_aux1 = VGroup(t5, t6).arrange(DOWN, buff=1).move_to(t2[2]).shift(DOWN*0.1)
        g_aux1_brace = Brace(g_aux1, LEFT, buff=0.1)
        self.play(LaggedStart(FadeOut(t2[2]),
                              FadeIn(t5[0], t6[0], g_aux1_brace),
                              lag_ratio=0.5))
        self.wait()
        self.play(FadeIn(t5[1]))
        self.wait()
        self.play(FadeIn(t6[1]))
        self.wait()
        self.play(t5[1][2].animate.set_color(WHITE),
                  t6[1][2].animate.set_color(WHITE))
        self.wait()



        # Discriminante (Delta)
        t5_2 = MathTex(r'x_{1} =',r'\frac{-b + \sqrt{\Delta}}{2a}').move_to(t5).shift(LEFT*0.1)
        t6_2 = MathTex(r'x_{2} =',r'\frac{-b - \sqrt{\Delta}}{2a}').move_to(t6).shift(LEFT*0.1)
        t5_2_copy = t5_2.copy().move_to(t5, aligned_edge=LEFT).set_z_index(3)
        t6_2_copy = t6_2.copy().move_to(t6, aligned_edge=LEFT)
        t5_2[1][5:6].set_color(YELLOW)
        t6_2[1][5:6].set_color(YELLOW)

        self.play(t5[1][5:11].animate.set_color(YELLOW),
                  t6[1][5:11].animate.set_color(YELLOW))
        self.wait()
        self.play(ReplacementTransform(t5[1][5:11], t5_2[1][5:6]),      # 'b^2 - 4ac' vira delta (t5)
                  ReplacementTransform(t6[1][5:11], t6_2[1][5:6]))      # O mesmo para o t6
        self.wait()
        self.play(ReplacementTransform(t5_2[1][5:6], t5_2_copy[1][5:6]),    # O delta vai para a esquerda (t5)
                  ReplacementTransform(t5[1][3:5], t5_2_copy[1][3:5]),      # Ajuste no símbolo da raiz (t5)
                  ReplacementTransform(t5[1][11:14], t5_2_copy[1][6:9]),    # Ajuste no denominador da fração (t5)
                  ReplacementTransform(t6_2[1][5:6], t6_2_copy[1][5:6]),    # O mesmo de cima para o t6
                  ReplacementTransform(t6[1][3:5], t6_2_copy[1][3:5]),      # " " " "
                  ReplacementTransform(t6[1][11:14], t6_2_copy[1][6:9]))    # " " " "
        self.wait()



        t7 = Tex('\it Discriminante', color=GRAY).scale(0.95).next_to(g_aux1, RIGHT, buff=0.5).shift(UP*0.5)
        arrow_t7 = Arrow(t7, t5_2_copy[1][5:6].get_right(), color=GRAY)
        self.play(FadeIn(t7, arrow_t7))
        self.wait()
        self.play(self.camera.frame.animate.shift(UP*7))
        self.play(FadeOut(t7, arrow_t7, t2[0:2]))
        self.wait()

        black_sq_aux2 = black_sq_aux.copy().scale(10).move_to(g_aux1_brace, aligned_edge=UP)

        g_aux2 = VGroup(t5[0], t5[1][0:3], t5_2_copy[1][3:9],   # grupo com a chave e as fórmulas das duas raízes x_1 e x_2
                        t6[0], t6[1][0:3], t6_2_copy[1][3:9],
                        g_aux1_brace)
        #self.add(Line(UP, DOWN).scale(10))
        self.play(g_aux2.animate.shift(LEFT*2))
        self.play(self.camera.frame.animate.shift(DOWN*7))
        self.wait()



        # Arrumando as coisas: substitui o grupo auxiliar 'g_aux2' por algo mais organizado
        root_x1 = MathTex(r'x_{1} = \frac{-b + \sqrt{\Delta}}{2a}')
        root_x2 = MathTex(r'x_{2} = \frac{-b - \sqrt{\Delta}}{2a}')
        roots_x1_x2 = VGroup(root_x1, root_x2).arrange(DOWN, buff=1)
        roots_brace = Brace(roots_x1_x2, LEFT, buff=0.1)
        g_roots = VGroup(roots_x1_x2, roots_brace).move_to(g_aux2)
        self.remove(g_aux2).add(g_roots)
        self.wait()

        # Cópias para auxiliar nas próximas transformações
        root_x1_copy1 = root_x1.copy()
        root_x2_copy1 = root_x2.copy()

        root_x1_copy2 = root_x1.copy()
        root_x2_copy2 = root_x2.copy()

        root_x1_copy3 = root_x1.copy()
        root_x2_copy3 = root_x2.copy()



        # Delta > 0
        t8 = MathTex(r'\Delta > 0', color=YELLOW).next_to(g_roots, LEFT, buff=1)
        self.play(FadeIn(t8))
        self.wait()
        g_aux3 = VGroup(roots_brace,                            # grupo que não inclui a raiz de delta para diminuir a opacidade
                        root_x1[0][0:6], root_x1[0][9:13],
                        root_x2[0][0:6], root_x2[0][9:13])
        self.play(g_aux3.animate.set_opacity(0.3))
        self.wait()
        self.play(g_aux3.animate.set_opacity(1))
        self.wait()



        # Calculando com os coeficientes da primeira função (vermelha)
        red_root_x1 = MathTex(r'x_{1} \:\:= \frac{6 + \sqrt{4}}{2}','\:\:\:= 4').move_to(root_x1, aligned_edge=LEFT)
        red_root_x2 = MathTex(r'x_{2} \:\:= \frac{6 - \sqrt{4}}{2}','\:\:\:= 2').move_to(root_x2, aligned_edge=LEFT)
        VGroup(red_root_x1[0][3], red_root_x1[0][7], red_root_x1[0][9], red_root_x1[1][1]).set_color(RED)
        VGroup(red_root_x2[0][3], red_root_x2[0][7], red_root_x2[0][9], red_root_x2[1][1]).set_color(RED)

        black_sq_1.move_to(result_1b, aligned_edge=DOWN)
        black_sq_2.move_to(result_2, aligned_edge=DOWN)
        black_sq_3.move_to(result_3, aligned_edge=DOWN)

        self.play(FadeIn(black_sq_2, black_sq_3))
        self.wait()
        self.play(ReplacementTransform(root_x1[0][3:9], red_root_x1[0][3:8]),
                  ReplacementTransform(root_x1[0][10:12], red_root_x1[0][9]),
                  ReplacementTransform(root_x2[0][3:9], red_root_x2[0][3:8]),
                  ReplacementTransform(root_x2[0][10:12], red_root_x2[0][9]))
        self.wait()
        self.play(LaggedStart(FadeIn(red_root_x1[1]),
                              FadeIn(red_root_x2[1]),
                              lag_ratio=0.5),
                  FadeIn(root_1a_label, root_1b_label))
        self.wait()
        



        # Então delta > 0 é o primeiro caso
        self.play(t8.animate.next_to(g_1, UP, buff=-1),
                  self.camera.frame.animate.shift(UP*5.5), run_time=2)
        self.wait()
        self.play(ReplacementTransform(red_root_x1[0][3:8], root_x1_copy1[0][3:9]),
                  ReplacementTransform(red_root_x1[0][9], root_x1_copy1[0][10:12]),
                  ReplacementTransform(red_root_x2[0][3:8], root_x2_copy1[0][3:9]),
                  ReplacementTransform(red_root_x2[0][9], root_x2_copy1[0][10:12]),
                  FadeOut(red_root_x1[1], red_root_x2[1]))
        self.wait()
        self.play(FadeOut(black_sq_2, black_sq_3),
                  Restore(self.camera.frame),
                  run_time=2) 
        self.wait()



        # Delta = 0
        t9 = MathTex(r'\Delta = 0', color=YELLOW).next_to(g_roots, LEFT, buff=1)
        self.play(FadeIn(t9))
        self.wait()
        


        # Calculando com os coeficientes da segunda função (verde)
        green_root_x1 = MathTex(r'x_{1} \:\:= \frac{6 + \sqrt{0}}{2}','\:\:\:= 3').move_to(root_x1, aligned_edge=LEFT)
        green_root_x2 = MathTex(r'x_{2} \:\:= \frac{6 - \sqrt{0}}{2}','\:\:\:= 3').move_to(root_x2, aligned_edge=LEFT)
        VGroup(green_root_x1[0][3], green_root_x1[0][7], green_root_x1[0][9], green_root_x1[1][1]).set_color(GREEN)
        VGroup(green_root_x2[0][3], green_root_x2[0][7], green_root_x2[0][9], green_root_x2[1][1]).set_color(GREEN)

        green_root_x1_aux = MathTex(r'x_{1} \:\:\:\:= \frac{6 + 0}{2}','\:\:\:= 3').move_to(root_x1, aligned_edge=LEFT).shift(DOWN*0.05)
        green_root_x2_aux = MathTex(r'x_{2} \:\:\:\:= \frac{6 - 0}{2}','\:\:\:= 3').move_to(root_x2, aligned_edge=LEFT).shift(DOWN*0.05)
        VGroup(green_root_x1_aux[0][3], green_root_x1_aux[0][5], green_root_x1_aux[0][7], green_root_x1_aux[1][1]).set_color(GREEN)
        VGroup(green_root_x2_aux[0][3], green_root_x2_aux[0][5], green_root_x2_aux[0][7], green_root_x2_aux[1][1]).set_color(GREEN)
        
        self.play(FadeIn(black_sq_1, black_sq_3))
        self.wait()
        self.play(ReplacementTransform(root_x1_copy1[0][3:9], green_root_x1[0][3:8]),
                  ReplacementTransform(root_x1_copy1[0][10:12], green_root_x1[0][9]),
                  ReplacementTransform(root_x2_copy1[0][3:9], green_root_x2[0][3:8]),
                  ReplacementTransform(root_x2_copy1[0][10:12], green_root_x2[0][9]))
        self.wait()
        self.play(ReplacementTransform(green_root_x1[0][3:8], green_root_x1_aux[0][3:6]),
                  ReplacementTransform(green_root_x2[0][3:8], green_root_x2_aux[0][3:6]))
        self.wait()
        self.play(FadeIn(green_root_x1[1]), 
                  FadeIn(green_root_x2[1]),
                  FadeIn(root_2_label))
        self.wait()



        # Então delta = 0 é o segundo caso
        self.play(t9.animate.next_to(g_2, UP, buff=-1),
                  self.camera.frame.animate.shift(UP*5.5), run_time=2)
        self.wait()
        self.play(ReplacementTransform(green_root_x1_aux[0][3:6], root_x1_copy2[0][3:9]),
                  ReplacementTransform(green_root_x1[0][9], root_x1_copy2[0][10:12]),
                  ReplacementTransform(green_root_x2_aux[0][3:6], root_x2_copy2[0][3:9]),
                  ReplacementTransform(green_root_x2[0][9], root_x2_copy2[0][10:12]),
                  FadeOut(green_root_x1[1], green_root_x2[1]))
        self.wait()
        self.play(FadeOut(black_sq_1, black_sq_3),
                  Restore(self.camera.frame),
                  run_time=2) 
        self.wait()



        # Delta < 0
        t10 = MathTex(r'\Delta < 0', color=YELLOW).next_to(g_roots, LEFT, buff=1).set_z_index(8)
        self.play(FadeIn(t10))
        self.wait()



        # Calculando com os coeficientes da terceira função (azul)
        blue_root_x1 = MathTex(r'x_{1} \:\:= \frac{6 + \sqrt{-4}}{2}','\:\:\:= 3').move_to(root_x1, aligned_edge=LEFT)
        blue_root_x2 = MathTex(r'x_{2} \:\:= \frac{6 - \sqrt{-4}}{2}','\:\:\:= 3').move_to(root_x2, aligned_edge=LEFT)
        VGroup(blue_root_x1[0][3], blue_root_x1[0][7:9], blue_root_x1[0][10], blue_root_x1[1][1]).set_color(BLUE)
        VGroup(blue_root_x2[0][3], blue_root_x2[0][7:9], blue_root_x2[0][10], blue_root_x2[1][1]).set_color(BLUE)

        self.play(FadeIn(black_sq_1, black_sq_2))
        self.wait()
        self.play(ReplacementTransform(root_x1_copy2[0][3:9], blue_root_x1[0][3:9]),
                  ReplacementTransform(root_x1_copy2[0][10:12], blue_root_x1[0][10]),
                  ReplacementTransform(root_x2_copy2[0][3:9], blue_root_x2[0][3:9]),
                  ReplacementTransform(root_x2_copy2[0][10:12], blue_root_x2[0][10]))
        self.wait()



        # Então delta < 0 é o terceiro caso
        self.play(t10.animate.next_to(g_3, UP, buff=-1),
                  self.camera.frame.animate.shift(UP*5.5), run_time=2)
        self.wait()     
        self.play(ReplacementTransform(blue_root_x1[0][3:9], root_x1_copy3[0][3:9]),
                  ReplacementTransform(blue_root_x1[0][10], root_x1_copy3[0][10:12]),
                  ReplacementTransform(blue_root_x2[0][3:9], root_x2_copy3[0][3:9]),
                  ReplacementTransform(blue_root_x2[0][10], root_x2_copy3[0][10:12]),
                  FadeOut(blue_root_x1[1], blue_root_x2[1]))
        self.play(FadeOut(black_sq_1, black_sq_2,
                          arrow_1, arrow_2, arrow_3,
                          result_1a, result_1b, result_2, result_3),
                  self.camera.frame.animate.shift(UP*1.5), 
                  run_time=1.5) 
        self.wait()



        # Zoom na primeira função
        label_1_aux = MathTex('y = x^2 - 6x + 8', color=RED).scale(0.9).next_to(box_1, UP, buff=0.1).set_z_index(3)
        self.play(self.camera.frame.animate.move_to(g_1).scale(0.84),
                  t1.animate.next_to(g_1, UP, buff=0.85).scale(0.84),
                  FadeOut(t1, g_2, g_3, 
                          box_1, box_2, box_3, 
                          t8, t9, t10, 
                          label_1[1], label_2, label_3),
                  TransformMatchingShapes(label_1[0], label_1_aux),
                  run_time=1.5)
        self.wait()



# Simetria das raízes / Coordenadas do vértice
class vid6(MovingCameraScene):
    def construct(self):

        # Retomando elementos
        axes = Axes(x_range = [-1, 7, 1],
                    y_range = [-1, 9, 1],
                    x_length = 5,
                    y_length = 5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
    

        axes_1 = axes.copy()
        graph_1 = axes.plot(lambda x: (x - 3)**2 - 1,
                         x_range=[0.5, 5.5], stroke_width = 5).set_color(RED).set_z_index(2)
        root_1a = Dot(graph_1.get_point_from_function(t=2)).scale(1).set_color(YELLOW).set_z_index(3)
        root_1b = Dot(graph_1.get_point_from_function(t=4)).scale(1).set_color(YELLOW).set_z_index(3)
        root_1a_label = MathTex('2').scale(0.8).next_to(axes_1.coords_to_point(2,0,0), DL, buff = 0.13).set_opacity(0.6)
        root_1b_label = MathTex('4').scale(0.8).next_to(axes_1.coords_to_point(4,0,0), DR, buff = 0.13).set_opacity(0.6)
        vertex_1 = Dot(graph_1.get_point_from_function(t=3)).set_color(YELLOW).set_z_index(3)
        g_1 = VGroup(axes_1, graph_1, root_1a, root_1b, root_1a_label, root_1b_label, vertex_1)


        axes_2 = axes.copy()
        graph_2 = axes.plot(lambda x: (x - 3)**2,
                         x_range=[0.5, 5.5], stroke_width = 5).set_color(GREEN).set_z_index(2)
        root_2 = Dot(graph_2.get_point_from_function(t=3)).scale(1).set_color(YELLOW)
        g_2 = VGroup(axes_2, graph_2, root_2)


        axes_3 = axes.copy()
        graph_3 = axes.plot(lambda x: (x - 3)**2 + 1,
                         x_range=[0.5, 5.5], stroke_width = 5).set_color(BLUE).set_z_index(2)
        g_3 = VGroup(axes_3, graph_3)


        g_0 = VGroup(g_1, g_2, g_3).arrange(RIGHT, buff=1).scale(0.9).shift(DOWN*0.3).set_z_index(6)


        box_1 = SurroundingRectangle(g_1, buff=0.3, color=GRAY, stroke_width=2)
       
        self.camera.frame.move_to(g_1).shift(UP*0)

        t1 = Tex('Raízes', color=YELLOW).scale(0.9).next_to(g_1, UP, buff=0.85).set_z_index(8)
        
        label_1 = MathTex('y = x^2 - 6x + 8', color=RED).scale(0.9).next_to(box_1, UP, buff=0.1).set_z_index(3)
        label_1_copy = label_1.copy()
        self.add(axes_1, graph_1, root_1a, root_1b, root_1a_label, root_1b_label, label_1)



        # As raízes estão à mesma distância da linha de simetria
        axis_of_symmetry = DashedVMobject(Line(UP, DOWN, color=GRAY).scale(2.8), num_dashes=16).set_z_index(3).move_to(axes_1.coords_to_point(3,4,0)).shift(DOWN*0.5)
        self.play(FadeIn(axis_of_symmetry))
        self.wait()

        distance_1 = Line(axes_1.coords_to_point(2,0,0), axes_1.coords_to_point(3,0,0), stroke_width=6, color=YELLOW).set_opacity(0.5)
        distance_2 = Line(axes_1.coords_to_point(4,0,0), axes_1.coords_to_point(3,0,0), stroke_width=6, color=YELLOW).set_opacity(0.5)
        self.play(Create(distance_1),
                  Create(distance_2),
                  run_time=1.5)
        self.wait()

        t2 = Tex('Vértice', color=YELLOW).scale(0.9).next_to(g_1, DOWN, buff=0.5).shift(RIGHT*2)
        arrow_t2 = Arrow(t2, vertex_1, color=YELLOW)
        self.play(FadeIn(t2, arrow_t2),
                  FadeOut(distance_1, distance_2),
                  root_1a.animate.set_color(WHITE),
                  root_1b.animate.set_color(WHITE))
        self.wait()

        vertex_1_coord = MathTex('(',r'x_v',',',r'y_v',')', color=YELLOW).scale(0.9).move_to(t2, aligned_edge=LEFT).shift(UP*0.05)
        self.play(LaggedStart(FadeOut(t2, axis_of_symmetry),
                              FadeIn(vertex_1_coord),
                              lag_ratio=0.3))
        self.wait()



        # 'x' do vértice
        t3 = MathTex(r'x_v ',' = {',r'x_1',' + ',r'x_2',' \over 2}').scale(0.9).next_to(g_1, RIGHT, buff=0.5)
        t3[0].set_color(YELLOW)
        self.play(TransformFromCopy(vertex_1_coord[1], t3[0]))
        self.wait()
        self.play(FadeIn(t3[1:6]))
        self.wait()

        t4 = MathTex(r'x_v ',' = {','2',' + ','4',' \over 2}',r'= 3').scale(0.9).move_to(t3)
        t4[0].set_color(YELLOW)
        t4[2].set_opacity(0.6).move_to(t3[2]).shift(UP*0.1+RIGHT*0.1)
        t4[4].set_opacity(0.6).move_to(t3[4]).shift(UP*0.1+LEFT*0.05)
        t4[6].next_to(t3, RIGHT, buff=0.2)
        t4[6][1].set_color(YELLOW)
        self.play(FadeOut(t3[2], t3[4]),
                  TransformFromCopy(root_1a_label, t4[2]),
                  TransformFromCopy(root_1b_label, t4[4]))
        self.wait()
        self.play(FadeIn(t4[6]))
        self.wait()
        self.play(FadeOut(vertex_1_coord[1], t3[0:2], t3[3], t3[5], t4[2], t4[4], t4[6][0]), 
                  t4[6][1].animate.move_to(vertex_1_coord[1]).shift(UP*0.05))
        self.wait()



        # 'y' do vértice
        t5_aux = MathTex(r'y ',' = ',r'x','^2 - 6','x',' + 8', color=RED).scale(0.9).next_to(g_1, RIGHT, buff=-0.5)
        t5 = MathTex(r'y_v ',' = ',r'{x_v}','^2 - 6','x_v',' + 8', color=RED).scale(0.9).next_to(g_1, RIGHT, buff=-0.5)
        t5[0].set_color(YELLOW)
        #t5[2].set_color(YELLOW)
        #t5[4].set_color(YELLOW)
        self.add(label_1_copy)
        self.play(label_1.animate.move_to(t5_aux, aligned_edge=LEFT))
        self.remove(label_1).add(t5_aux)
        self.wait()
        self.play(TransformMatchingShapes(t5_aux, t5))
        self.wait()
        
        t6 = MathTex(r'y_v ',' = ',r'3','^2 - 6',r'\cdot 3',' + 8','= -1', color=RED).scale(0.9).next_to(g_1, RIGHT, buff=-0.5)
        t6[0].set_color(YELLOW)
        #t6[2].set_color(YELLOW)
        #t6[4].set_color(YELLOW)
        t6[6][1:3].set_color(YELLOW)
        self.play(ReplacementTransform(t5[2:6], t6[2:6]))
        self.wait()
        self.play(FadeIn(t6[6]))
        self.wait()
        self.play(FadeOut(vertex_1_coord[3], t5[0:2], t6[2:6], t6[6][0]),
                  t6[6][1:3].animate.move_to(vertex_1_coord[3]).shift(UP*0.05+LEFT*0.06),
                  t4[6][1].animate.shift(LEFT*0.07),
                  vertex_1_coord[2].animate.shift(LEFT*0.12))
        self.wait()



        # Comentário sobre o resultado fornecido por bhaskara para essa função
        red_root_x1 = MathTex(r'x_{1} = \frac{6 + \sqrt{4}}{2}','= 4').scale(0.8)
        red_root_x2 = MathTex(r'x_{2} = \frac{6 - \sqrt{4}}{2}','= 2').scale(0.8)
        VGroup(red_root_x1[0][3], red_root_x1[0][7], red_root_x1[0][9], red_root_x1[1][1]).set_color(RED)
        VGroup(red_root_x2[0][3], red_root_x2[0][7], red_root_x2[0][9], red_root_x2[1][1]).set_color(RED)
        roots = VGroup(red_root_x1, red_root_x2).arrange(DOWN, buff=1)
        roots_brace = Brace(roots, LEFT, buff=0.1)
        g_roots = VGroup(roots, roots_brace).next_to(g_1, RIGHT).shift(RIGHT*4.6)

        self.add(g_roots)
        self.play(self.camera.frame.animate.shift(RIGHT*2.8),
                  g_roots.animate.shift(LEFT*2.5),
                  vertex_1.animate.set_color(WHITE),
                  arrow_t2.animate.set_color(WHITE),
                  vertex_1_coord[0].animate.set_color(WHITE),
                  vertex_1_coord[2].animate.set_color(WHITE),
                  vertex_1_coord[4].animate.set_color(WHITE),
                  t4[6][1].animate.set_color(WHITE),
                  t6[6][1:3].animate.set_color(WHITE),
                  run_time=2)
        self.wait()



        # Separando as frações
        red_root_x1_2 = MathTex(r'x_{1} = \frac{6}{2} + \frac{\sqrt{4}}{2}','= 4').scale(0.8).move_to(red_root_x1, aligned_edge=LEFT)
        red_root_x2_2 = MathTex(r'x_{2} = \frac{6}{2} - \frac{\sqrt{4}}{2}','= 2').scale(0.8).move_to(red_root_x2, aligned_edge=LEFT)
        VGroup(red_root_x1_2[0][3], red_root_x1_2[0][7], red_root_x1_2[0][9], red_root_x1_2[1][1]).set_color(RED)
        VGroup(red_root_x2_2[0][3], red_root_x2_2[0][7], red_root_x2_2[0][9], red_root_x2_2[1][1]).set_color(RED)

        self.play(FadeTransform(red_root_x1, red_root_x1_2),
                  FadeTransform(red_root_x2, red_root_x2_2))
        self.wait()



        # As raízes partem de um mesmo número...
        box1_root1 = SurroundingRectangle(red_root_x1_2[0][3:6], stroke_width=2)
        box1_root2 = SurroundingRectangle(red_root_x2_2[0][3:6], stroke_width=2)

        box2_root1 = SurroundingRectangle(red_root_x1_2[0][7:12], stroke_width=2)
        box2_root2 = SurroundingRectangle(red_root_x2_2[0][7:12], stroke_width=2)


        self.play(FadeIn(box1_root1, box1_root2))
        self.wait()
        self.play(FadeIn(box2_root1))
        self.wait()
        self.play(FadeIn(box2_root2))
        self.wait()
        self.play(FadeOut(box1_root1, box1_root2, box2_root1, box2_root2))
        self.wait()



        # A primeira parcela é o 'x' do vértice
        xv_x_line = DashedLine(vertex_1, axes_1.coords_to_point(3,0,0), color=GRAY)
        t7 = MathTex('3', color=YELLOW).scale(0.8).move_to(red_root_x1_2[0][3:6])
        t8 = t7.copy().move_to(red_root_x2_2[0][3:6])

        self.play(t4[6][1].animate.set_color(YELLOW),
                  FadeIn(xv_x_line),
                  LaggedStart(FadeOut(red_root_x1_2[0][3:6], red_root_x2_2[0][3:6]),
                              FadeIn(t7, t8),
                              lag_ratio=0.3))
        self.wait()



        # A primeira parcela é a distância das raízes ao 'x' do vértice
        arrow_1 = CurvedArrow(axes_1.coords_to_point(3,0,0), axes_1.coords_to_point(2,0.2,0), color=YELLOW, tip_length=0.2, radius=0.4)
        arrow_2 = CurvedArrow(axes_1.coords_to_point(3,0,0), axes_1.coords_to_point(4,0.2,0), color=YELLOW, tip_length=0.2, radius=-0.4)

        self.play(t4[6][1].animate.set_color(WHITE),
                  t7.animate.set_color(WHITE),
                  t8.animate.set_color(WHITE),
                  red_root_x1_2[0][7:12].animate.set_color(YELLOW),
                  red_root_x2_2[0][7:12].animate.set_color(YELLOW))
        self.play(GrowFromEdge(arrow_2, DL))
        self.play(GrowFromEdge(arrow_1, DR))
        self.wait()



        # Mudando para as formas literais da função e das raízes
        label_2 = MathTex('y = a ',' x ',' ^2 ',' + b ',' x ',' + c', color=BLUE).scale(0.9).move_to(label_1_copy)
        label_2_copy = label_2.copy()
        graph_2 = axes_1.plot(lambda x: (x - 3)**2 - 1,
                         x_range=[0.2, 5.8], stroke_width = 5).set_color(BLUE)
        root_1a_label_2 = MathTex(r'x_2').scale(0.8).next_to(axes_1.coords_to_point(2,0,0), DL, buff = 0.13).set_opacity(0.6)
        root_1b_label_2 = MathTex(r'x_1').scale(0.8).next_to(axes_1.coords_to_point(4,0,0), DR, buff = 0.13).set_opacity(0.6)
        vertex_1_coord_2 = MathTex(r'(','x_v',',','y_v',')').move_to(vertex_1_coord, aligned_edge=LEFT)
        
        roots_brace.shift(DOWN*0.5+RIGHT*0.5)
        root1_formula1 = MathTex(r'x_{1} = \frac{-b + \sqrt{\Delta}}{2a}').scale(0.8).move_to(red_root_x1, aligned_edge=LEFT).shift(DOWN*0.5+RIGHT*0.5)
        root2_formula1 = MathTex(r'x_{2} = \frac{-b - \sqrt{\Delta}}{2a}').scale(0.8).move_to(red_root_x2, aligned_edge=LEFT).shift(DOWN*0.5+RIGHT*0.5)
        VGroup(root1_formula1[0][4], root1_formula1[0][8], root1_formula1[0][11]).set_color(BLUE)
        VGroup(root2_formula1[0][4], root2_formula1[0][8], root2_formula1[0][11]).set_color(BLUE)

        self.play(LaggedStart(FadeOut(label_1_copy, graph_1, 
                                      root_1a_label, root_1b_label, 
                                      xv_x_line, arrow_1, arrow_2,
                                      vertex_1_coord[0], t4[6][1], vertex_1_coord[2], t6[6][1:3], vertex_1_coord[4],
                                      red_root_x1_2[0][0:3], t7, red_root_x1_2[0][6:16], red_root_x1_2[1], red_root_x2_2[0][0:3], t8, red_root_x2_2[0][6:16], red_root_x2_2[1]),
                              FadeIn(label_2, graph_2, vertex_1_coord_2,
                                     root_1a_label_2, root_1b_label_2,
                                     root1_formula1, root2_formula1),
                              lag_ratio=1))
        self.wait()


        # Fazendo a média das duas raízes
        mean_1 = MathTex(r'x_{v} = \frac{1}{2} \left( ',r' \frac{-b + \sqrt{\Delta}}{2a} ','+',r' \frac{-b - \sqrt{\Delta}}{2a} ',r'\right)').scale(0.8).next_to(root1_formula1, UP, buff=0.7).shift(LEFT*0.6)
        mean_1[0][0:2].set_color(YELLOW)
        VGroup(mean_1[1][1], mean_1[1][5], mean_1[1][8],
               mean_1[3][1], mean_1[3][5], mean_1[3][8]).set_color(BLUE)

        self.play(FadeIn(mean_1[0][0:2]))
        self.play(FadeIn(mean_1[0][2:7], mean_1[2], mean_1[4]))
        self.play(ReplacementTransform(root1_formula1[0][3:12], mean_1[1]),
                  ReplacementTransform(root2_formula1[0][3:12], mean_1[3]))
        self.wait()
        self.play(LaggedStart(FadeOut(root1_formula1[0][0:3], root2_formula1[0][0:3], roots_brace),
                              mean_1.animate.shift(DOWN*2.5),
                              lag_ratio=0.5))
        self.wait(2)
        


        mean_2 = MathTex(r'x_{v} = \frac{1}{2} \left( ',r' \frac{-b + \sqrt{\Delta} -b - \sqrt{\Delta}}{2a} ',r'\right)').scale(0.8).move_to(mean_1, aligned_edge=LEFT)
        mean_2[0][0:2].set_color(YELLOW)
        VGroup(mean_2[1][1], mean_2[1][5], mean_2[1][7], mean_2[1][11], mean_2[1][14]).set_color(BLUE)
        self.play(TransformMatchingTex(mean_1, mean_2))
        self.wait(2)

        red_line1 = Line(UP*0.2, DOWN*0.2, color=RED, stroke_width=4).scale(2).rotate(50*DEGREES).move_to(mean_2[1][3:6])
        red_line2 = red_line1.copy().move_to(mean_2[1][9:12])
        self.play(Create(red_line1), Create(red_line2))
        self.wait(2)

        mean_3 = MathTex(r'x_{v} = \frac{1}{2} \left( ',r' \frac{-b -b}{2a} ',r'\right)').scale(0.8).move_to(mean_1, aligned_edge=LEFT)
        mean_3[0][0:2].set_color(YELLOW)
        VGroup(mean_3[1][1], mean_3[1][3], mean_3[1][6]).set_color(BLUE)
        self.play(FadeOut(red_line1, red_line2),
                  TransformMatchingTex(mean_2, mean_3))
        self.wait(2)
        
        mean_4 = MathTex(r'x_{v} = \frac{1}{2} \left( ',r' \frac{-2b}{2a} ',r'\right)').scale(0.8).move_to(mean_1, aligned_edge=LEFT)
        mean_4[0][0:2].set_color(YELLOW)
        VGroup(mean_4[1][2], mean_4[1][5]).set_color(BLUE)
        self.play(TransformMatchingTex(mean_3, mean_4))
        self.wait(2)

        mean_5 = MathTex(r'x_{v} = \frac{1}{2} \left( ',r' \frac{-b}{a} ',r'\right)').scale(0.8).move_to(mean_1, aligned_edge=LEFT)
        mean_5[0][0:2].set_color(YELLOW)
        VGroup(mean_5[1][1], mean_5[1][3]).set_color(BLUE)
        self.play(TransformMatchingTex(mean_4, mean_5))
        self.wait(2)

        mean_6 = MathTex(r'x_{v} =',r' \frac{-b}{2a}').scale(0.8).move_to(mean_1, aligned_edge=LEFT)
        mean_6[0][0:2].set_color(YELLOW)
        VGroup(mean_6[1][1], mean_6[1][4]).set_color(BLUE)
        self.play(TransformMatchingTex(mean_5, mean_6))
        self.wait(2)



        # Então 'x' do vértice = -b/2a
        xv_coord = MathTex(r'\left(',r' \frac{-b}{2a} ',',',r' \frac{-\Delta}{4a} ',r'\right)').scale(0.8).move_to(vertex_1_coord_2[1], aligned_edge=LEFT).shift(LEFT*0.15)
        xv_coord[4].shift(RIGHT*0.1)

        self.play(ReplacementTransform(mean_6[1], xv_coord[1]),
                  FadeOut(vertex_1_coord_2[0:2], mean_6[0]), 
                  FadeIn(xv_coord[0]),
                  vertex_1_coord_2[2:5].animate.shift(RIGHT*0.2))
        self.wait()

                  




        '''# Separando as frações em duas
        root1_formula2 = MathTex(r'x_{1} = \frac{-b}{2a} + \frac{\sqrt{b^2 - 4ac}}{2a}').scale(0.8).move_to(red_root_x1, aligned_edge=LEFT)
        root2_formula2 = MathTex(r'x_{2} = \frac{-b}{2a} - \frac{\sqrt{b^2 - 4ac}}{2a}').scale(0.8).move_to(red_root_x2, aligned_edge=LEFT)
        VGroup(root1_formula2[0][4], root1_formula2[0][7], root1_formula2[0][11], root1_formula2[0][15:17], root1_formula2[0][19]).set_color(BLUE)
        VGroup(root2_formula2[0][4], root2_formula2[0][7], root2_formula2[0][11], root2_formula2[0][15:17], root2_formula2[0][19]).set_color(BLUE)

        self.play(FadeTransform(root1_formula1, root1_formula2),
                  FadeTransform(root2_formula1, root2_formula2))
        self.wait()



        # Coordenada 'x' do vértice = -b/2a
        xv_coord = MathTex(r'\left(',r' \frac{-b}{2a} ',',',r' \frac{-\Delta}{4a} ',r'\right)').scale(0.8).move_to(vertex_1_coord_2[1], aligned_edge=LEFT).shift(LEFT*0.15)
        xv_coord[1].set_color(YELLOW)
        xv_coord[3].set_color(YELLOW)
        xv_coord[4].shift(RIGHT*0.1)

        g_aux1 = VGroup(root1_formula2[0][3:8], root2_formula2[0][3:8])
        g_aux1_copy = g_aux1.copy()

        self.play(g_aux1.animate.set_color(YELLOW))
        self.wait()
        #self.add(g_aux1_copy)
        self.play(FadeOut(vertex_1_coord_2[0:2]),
                  FadeIn(xv_coord[0]),
                  vertex_1_coord_2[2:5].animate.shift(RIGHT*0.2),
                  ReplacementTransform(g_aux1_copy, xv_coord[1]))
        self.wait()'''



        # Coordenada 'y' do vértice = -delta/4a
        t9 = MathTex('y_v ',' = a ',r' {x_v} ',' ^2 ','+ b ',r' {x_v} ','+ c').scale(0.9).move_to(g_roots).shift(LEFT*1.2)
        t9[0].set_color(YELLOW)
        VGroup(t9[1], t9[4], t9[6]).set_color(BLUE)

        t10 = MathTex(r'y_v ',' = a ',r' {\left( \frac{-b}{2a} \right)} ^2 ',' + b ',r' \left( \frac{-b}{2a} \right) ',' + c', color=BLUE).move_to(t9, aligned_edge=LEFT)
        t10[0].set_color(YELLOW)
        t10[2].set_color(WHITE)
        t10[4].set_color(WHITE)
        
        #self.play(FadeOut(roots_brace, root1_formula2, root2_formula2),
        #          xv_coord[1].animate.set_color(WHITE))
        
        self.add(label_2_copy)
        self.play(label_2_copy.animate.move_to(t9, aligned_edge=LEFT))
        self.wait()
        self.play(TransformMatchingShapes(label_2_copy, t9))
        self.wait()
        self.play(ReplacementTransform(t9, t10))
        self.wait()



        t11 = MathTex(r'y_v ',' = a ',r' \frac{(-b)^2}{(2a)^2} ',' + b ',r' \left( \frac{-b}{2a} \right) ',' + c', color=BLUE).move_to(t9, aligned_edge=LEFT)
        t11[0].set_color(YELLOW)
        t11[2].set_color(WHITE)
        t11[4].set_color(WHITE)
        self.play(TransformMatchingTex(t10, t11))
        self.wait()



        t12 = MathTex(r'y_v ',' = a ',r' \frac{b^2}{(2a)^2} ',' + b ',r' \left( \frac{-b}{2a} \right) ',' + c', color=BLUE).move_to(t9, aligned_edge=LEFT)
        t12[0].set_color(YELLOW)
        t12[2].set_color(WHITE)
        t12[4].set_color(WHITE)
        self.play(TransformMatchingTex(t11, t12))
        self.wait()



        t13 = MathTex(r'y_v ',' = a ',r' \frac{b^2}{4a^2} ',' + b ',r' \left( \frac{-b}{2a} \right) ',' + c', color=BLUE).move_to(t9, aligned_edge=LEFT)
        t13[0].set_color(YELLOW)
        t13[2].set_color(WHITE)
        t13[4].set_color(WHITE)
        self.play(TransformMatchingTex(t12, t13))
        self.wait()



        t14 = MathTex(r'y_v ',' = ',r' \frac{ab^2}{4a^2} ',' + b ',r' \left( \frac{-b}{2a} \right) ',' + c', color=BLUE).move_to(t9, aligned_edge=LEFT)
        t14[0].set_color(YELLOW)
        t14[2][1:7].set_color(WHITE)
        t14[4].set_color(WHITE)
        self.play(TransformMatchingTex(t13, t14))
        self.wait()

        red_line1 = Line(UP*0.2, DOWN*0.2, color=RED, stroke_width=4).rotate(30*DEGREES).move_to(t14[2][0])
        red_line2 = red_line1.copy().move_to(t14[2][6])
        self.play(Create(red_line1), Create(red_line2))
        self.wait()



        t15 = MathTex(r'y_v ',' = ',r' \frac{b^2}{4a} ',' + b ',r' \left( \frac{-b}{2a} \right) ',' + c', color=BLUE).move_to(t9, aligned_edge=LEFT)
        t15[0].set_color(YELLOW)
        t15[2].set_color(WHITE)
        t15[4].set_color(WHITE)
        self.play(TransformMatchingTex(t14, t15),
                  FadeOut(red_line1, red_line2))
        self.wait()



        t16 = MathTex(r'y_v ',' = ',r' \frac{b^2}{4a} ',' + ',r' \frac{b(-b)}{2a} ',' + c', color=BLUE).move_to(t9, aligned_edge=LEFT)
        t16[0].set_color(YELLOW)
        t16[2].set_color(WHITE)
        t16[4][1:8].set_color(WHITE)
        self.play(TransformMatchingTex(t15, t16))
        self.wait()



        t17 = MathTex(r'y_v ',' = ',r' \frac{b^2}{4a} ',' + ',r' \frac{-b^2}{2a} ',' + c', color=BLUE).move_to(t9, aligned_edge=LEFT)
        t17[0].set_color(YELLOW)
        t17[2].set_color(WHITE)
        t17[4].set_color(WHITE)
        self.play(TransformMatchingTex(t16, t17))
        self.wait()



        t18 = MathTex(r'y_v ',' = ',r' \frac{b^2}{4a} ',' + ',r' \frac{-b^2}{2a} ',r' \cdot \frac{2}{2} ',' + c', color=BLUE).move_to(t9, aligned_edge=LEFT)
        t18[0].set_color(YELLOW)
        t18[2].set_color(WHITE)
        t18[4].set_color(WHITE)
        t18[5].set_color(GRAY)
        self.play(TransformMatchingTex(t17, t18))
        self.wait()



        t19 = MathTex(r'y_v ',' = ',r' \frac{b^2}{4a} ',' + ',r' \frac{-2b^2}{4a} ',' + c', color=BLUE).move_to(t9, aligned_edge=LEFT)
        t19[0].set_color(YELLOW)
        t19[2].set_color(WHITE)
        t19[4].set_color(WHITE)
        self.play(TransformMatchingTex(t18, t19))
        self.wait()



        t20 = MathTex(r'y_v ',' = ',r' \frac{b^2}{4a} ',' + ',r' \frac{-2b^2}{4a} ',' + c ',r' \cdot \frac{4a}{4a}', color=BLUE).move_to(t9, aligned_edge=LEFT)
        t20[0].set_color(YELLOW)
        t20[2].set_color(WHITE)
        t20[4].set_color(WHITE)
        t20[6].set_color(GRAY)
        self.play(FadeIn(t20[6]))
        self.remove(t19, t20[6]).add(t20)
        self.wait()



        t21 = MathTex(r'y_v ',' = ',r' \frac{b^2}{4a} ',' +',r' \frac{-2b^2}{4a} ',r' + \frac{4ac}{4a} ', color=BLUE).move_to(t9, aligned_edge=LEFT)
        t21[0].set_color(YELLOW)
        t21[2].set_color(WHITE)
        t21[4].set_color(WHITE)
        self.play(TransformMatchingTex(t20, t21))
        self.wait()



        t22 = MathTex(r'y_v ',' = ',r' \frac{b^2 - 2b^2 + 4ac}{4a}').move_to(t9, aligned_edge=LEFT)
        t22[0].set_color(YELLOW)
        self.play(FadeTransform(t21, t22))
        self.wait()



        t23 = MathTex(r'y_v ',' = ',r' \frac{-b^2 + 4ac}{4a}').move_to(t9, aligned_edge=LEFT)
        t23[0].set_color(YELLOW)
        self.play(FadeTransform(t22, t23))
        self.wait()



        t24 = MathTex(r'y_v ',' = ',r' \frac{-(b^2 - 4ac)}{4a}').move_to(t9, aligned_edge=LEFT)
        t24[0].set_color(YELLOW)
        self.play(FadeTransform(t23, t24))
        self.wait()



        t25 = MathTex(r'y_v ',' = ',r' \frac{-\Delta}{4a}').move_to(t24)
        t25[0].set_color(YELLOW)
        self.play(ReplacementTransform(t24[0:2], t25[0:2]),
                  ReplacementTransform(t24[2][0:9], t25[2][0:2]),
                  ReplacementTransform(t24[2][9:13], t25[2][2:5]))
        self.remove(t24[0:2], t25[0:2], t25[2][0:2], t25[2][2:5]).add(t25)
        self.wait()



        # Então 'y' do vértice = -delta/4a
        self.play(self.camera.frame.animate.shift(LEFT*2.8),
                  FadeOut(vertex_1_coord_2[3:5], t25[0:2]),
                  FadeIn(xv_coord[4]),
                  t25[2].animate.move_to(xv_coord[3]).shift(RIGHT*0.1).scale(0.8))
        self.wait()
  


# Forma geral: Gráfico mudando o valor dos coeficientes a,b,c
class vid7(MovingCameraScene):
    def construct(self):

        t1 = MathTex('y ','=',' ax^2 ','+',' bx ','+',' c ').scale(0.9).to_edge(UP, buff=1.2)
        t1[2][0].set_color(BLUE)
        t1[4][0].set_color(RED)
        t1[6][0].set_color(GREEN)



        # ValueTrackers dos coeficientes 'a' e 'b'
        a = ValueTracker(1)
        b = ValueTracker(0)
        c = ValueTracker(0)



        # Mostrador do valor de 'a'
        a_label = MathTex('a', color=t1[2][0].get_color())
        a_numberline = NumberLine(x_range=[-5,5], length=2, tick_size=0,
                                  stroke_width=5, color=GRAY).rotate(90*DEGREES).next_to(a_label, DOWN, buff=0.2)
        a_numberline_dot = always_redraw(lambda: Dot(a_numberline.number_to_point(a.get_value()), color=a_label.get_color()))
        a_value_label = always_redraw(lambda: MathTex(f'{a.get_value():.1f}', color=a_label.get_color()).scale(0.7).next_to(a_numberline, DOWN, buff=0.1))

        g_a_display = VGroup(a_label, a_numberline, a_numberline_dot, a_value_label).shift(UP*3+RIGHT*4)



        # Mostrador do valor de 'b'
        b_label = MathTex('b', color=t1[4][0].get_color())
        b_numberline = NumberLine(x_range=[-5,5], length=2, tick_size=0,
                                  stroke_width=5, color=GRAY).rotate(90*DEGREES).next_to(b_label, DOWN, buff=0.2)
        b_numberline_dot = always_redraw(lambda: Dot(b_numberline.number_to_point(b.get_value()), color=b_label.get_color()))
        b_value_label = always_redraw(lambda: MathTex(f'{b.get_value():.1f}', color=b_label.get_color()).scale(0.7).next_to(b_numberline, DOWN, buff=0.1))
        
        g_b_display = VGroup(b_label, b_numberline, b_numberline_dot, b_value_label).next_to(g_a_display, RIGHT, buff=0.5, aligned_edge=DOWN)



        # Mostrador do valor de 'b'
        c_label = MathTex('c', color=t1[6][0].get_color())
        c_numberline = NumberLine(x_range=[-5,5], length=2, tick_size=0,
                                  stroke_width=5, color=GRAY).rotate(90*DEGREES).next_to(c_label, DOWN, buff=0.2)
        c_numberline_dot = always_redraw(lambda: Dot(c_numberline.number_to_point(c.get_value()), color=c_label.get_color()))
        c_value_label = always_redraw(lambda: MathTex(f'{c.get_value():.1f}', color=c_label.get_color()).scale(0.7).next_to(c_numberline, DOWN, buff=0.1))
        
        g_c_display = VGroup(c_label, c_numberline, c_numberline_dot, c_value_label).next_to(g_b_display, RIGHT, buff=0.5, aligned_edge=DOWN)

        g_displays = VGroup(g_a_display, g_b_display, g_c_display)

        # Gráfico
        axes = Axes(x_range = [-5, 5, 1],
                    y_range = [-5, 5, 1],
                    x_length = 9,
                    y_length = 9,
                    axis_config = {"include_ticks" : False}).scale(0.5).set_opacity(0.6).move_to(ORIGIN).shift(DOWN)
        x_label = MathTex("x").scale(0.8).next_to(axes.get_x_axis(), DR, buff = 0)
        y_label = MathTex("y").scale(0.8).next_to(axes.get_y_axis(), UL, buff = 0).shift(DOWN*0.1)
        axes_labels = VGroup(x_label, y_label).set_color(WHITE).set_opacity(0.6)
        axes_zero = MathTex('0').scale(0.64).next_to(axes.coords_to_point(0,0,0), DL, buff = 0.13).set_opacity(0.6)

        graph_1 = always_redraw(lambda: axes.plot(lambda x: (a.get_value())*x**2 + (b.get_value())*x + (c.get_value()),
                         x_range=[-7,7], stroke_width = 6).set_color(GREEN).set_z_index(-2))
        
        

        # Borda para o gráfico não escapar dos eixos
        external_border = Square(fill_opacity=1, color=YELLOW).scale(10)
        RADIUS = ValueTracker(2.5)
        internal_border = always_redraw(lambda: Circle(radius=RADIUS.get_value(), fill_opacity=1, color=BLUE))
        border = always_redraw(lambda: Difference(external_border, internal_border, fill_opacity=1, color=BLACK).set_z_index(-1).move_to(axes.coords_to_point(-(b.get_value())/2*(a.get_value()), -((b.get_value())**2 - 4*(a.get_value())*(c.get_value()))/4*(a.get_value()), 0)))

        # Animação
        self.add(border)
        self.play(FadeIn(axes, axes_labels, axes_zero, t1))
        self.play(Create(graph_1),
                  run_time=1.5)
        self.wait(2)
        self.play(FadeIn(g_a_display),
                  FadeOut(t1[3:7]),
                  t1[0:3].animate.shift(RIGHT*0.9))
        self.wait(2)
        
        

        # a > 1
        self.play(a.animate.set_value(3), run_time=3)
        self.wait(2)

        arrow1 = Arrow(DOWN, UP, tip_length=0.2).scale(0.7).rotate(90*DEGREES).move_to((1.5,0,0))
        arrow2 = arrow1.copy().rotate(180*DEGREES).move_to((-1.5,0,0))  
        self.play(FadeIn(arrow1, shift=LEFT),
                  FadeIn(arrow2, shift=RIGHT))
        self.play(FadeOut(arrow1, arrow2))
        self.wait(2)



        # 0 < a < 1
        self.play(a.animate.set_value(0.2),
                  RADIUS.animate.set_value(5.5), 
                  run_time=3)
        self.wait(2)
        arrow1.rotate(180*DEGREES).shift(RIGHT)
        arrow2.rotate(180*DEGREES).shift(LEFT)
        self.play(FadeIn(arrow1, shift=RIGHT),
                  FadeIn(arrow2, shift=LEFT))
        self.play(FadeOut(arrow1, arrow2))
        self.wait(2)



        # Comparar 3 funções
        graph_a = axes.plot(lambda x: 5*x**2,
                         x_range=[-1,1], stroke_width = 4).set_color(RED).set_z_index(2)
        graph_a_neg = axes.plot(lambda x: 5*x**2,
                         x_range=[-1,0], stroke_width = graph_a.get_stroke_width()).set_color(RED).set_z_index(2)
        graph_a_pos_1 = axes.plot(lambda x: 5*x**2,
                         x_range=[0,0.89], stroke_width = graph_a.get_stroke_width()).set_color(RED).set_z_index(2)
        graph_a_pos_2 = axes.plot(lambda x: 5*x**2,
                         x_range=[0.89,1], stroke_width = graph_a.get_stroke_width()).set_color(RED).set_z_index(2)
        
        graph_b = axes.plot(lambda x: 0.8*x**2,
                         x_range=[-2.48,2.48], stroke_width = graph_a.get_stroke_width()).set_color(BLUE).set_z_index(2)
        graph_b_neg = axes.plot(lambda x: 0.8*x**2,
                         x_range=[-2.48,0], stroke_width = graph_a.get_stroke_width()).set_color(BLUE).set_z_index(2)
        graph_b_pos_1 = axes.plot(lambda x: 0.8*x**2,
                         x_range=[0,0.89], stroke_width = graph_a.get_stroke_width()).set_color(BLUE).set_z_index(2)
        graph_b_pos_2 = axes.plot(lambda x: 0.8*x**2,
                         x_range=[0.89,2.24], stroke_width = graph_a.get_stroke_width()).set_color(BLUE).set_z_index(2)
        graph_b_pos_3 = axes.plot(lambda x: 0.8*x**2,
                         x_range=[2.24,2.48], stroke_width = graph_a.get_stroke_width()).set_color(BLUE).set_z_index(2)
        
        graph_c = axes.plot(lambda x: 0.3*x**2,
                         x_range=[-4.05,4.05], stroke_width = graph_a.get_stroke_width()).set_color(GREEN).set_z_index(2)
        graph_c_neg = axes.plot(lambda x: 0.3*x**2,
                         x_range=[-4.05,0], stroke_width = graph_a.get_stroke_width()).set_color(GREEN).set_z_index(2)
        graph_c_pos_1 = axes.plot(lambda x: 0.3*x**2,
                         x_range=[0,0.89], stroke_width = graph_a.get_stroke_width()).set_color(GREEN).set_z_index(2)
        graph_c_pos_2 = axes.plot(lambda x: 0.3*x**2,
                         x_range=[0.89,2.24], stroke_width = graph_a.get_stroke_width()).set_color(GREEN).set_z_index(2)
        graph_c_pos_3 = axes.plot(lambda x: 0.3*x**2,
                         x_range=[2.24,3.65], stroke_width = graph_a.get_stroke_width()).set_color(GREEN).set_z_index(2)
        graph_c_pos_4 = axes.plot(lambda x: 0.3*x**2,
                         x_range=[3.65,4.05], stroke_width = graph_a.get_stroke_width()).set_color(GREEN).set_z_index(2)
        
        graph_a_label = MathTex('y = 2x^2', color=graph_a.get_color()).scale(0.6).rotate(35*DEGREES).next_to(graph_a, UR, buff=0.1).shift(LEFT*0.1)
        graph_b_label = MathTex('y = x^2', color=graph_b.get_color()).scale(0.6).rotate(35*DEGREES).next_to(graph_b, UR, buff=0.1).shift(LEFT*0.1)
        graph_c_label = MathTex('y = 0.5x^2', color=graph_c.get_color()).scale(0.6).rotate(35*DEGREES).next_to(graph_c, UR, buff=0.1).shift(LEFT*0.1)

        y_line = DashedLine(axes.coords_to_point(-5,4,0), axes.coords_to_point(5,4,0), dash_length=0.05, color=YELLOW).set_opacity(0.7).set_z_index(3)
        y_line_label = MathTex('y = 2', color=YELLOW).scale(0.64).set_opacity(0.7).next_to(y_line, LEFT, buff=0.1)

        x_time_label = MathTex("t").scale(0.8).next_to(axes.get_x_axis(), DR, buff = 0).set_opacity(0.6)
        x_time_tick = Line(UP*0.1, DOWN*0.1).move_to(axes.coords_to_point(0,0,0))
        X_TIME = ValueTracker(0)
        x_time_tick_label = always_redraw(lambda : MathTex(f'{X_TIME.get_value():.1f}').scale(0.64).next_to(x_time_tick, DOWN, buff=0.1))

        black_sq1 = Rectangle(height=2, width=1, color=BLACK, fill_opacity=1, stroke_width=0).scale(4.2).next_to(axes.coords_to_point(0,-1,0), DOWN, buff=0).set_z_index(2)

        self.play(FadeOut(t1[0:3], g_a_display, graph_1, axes_labels, axes_zero),
                  self.camera.frame.animate.scale(0.7),
                  FadeIn(black_sq1),
                  run_time=1.5)
        self.wait(2)
        self.play(LaggedStart(Create(graph_b), FadeIn(graph_b_label), lag_ratio=0.2))
        self.wait(2)
        self.play(LaggedStart(Create(graph_a), FadeIn(graph_a_label), lag_ratio=0.2))
        self.wait(2)
        self.play(LaggedStart(Create(graph_c), FadeIn(graph_c_label), lag_ratio=0.2))
        self.wait(2)



        # Destaque em cada função de uma vez
        self.play(graph_b.animate.set_stroke(opacity=0.3),
                  graph_c.animate.set_stroke(opacity=0.3),
                  graph_b_label.animate.set_opacity(0.3),
                  graph_c_label.animate.set_opacity(0.3))
        self.wait(2)
        self.play(graph_a.animate.set_stroke(opacity=0.3),
                  graph_b.animate.set_stroke(opacity=1),
                  graph_a_label.animate.set_opacity(0.3),
                  graph_b_label.animate.set_opacity(1))
        self.wait(2)
        self.play(graph_b.animate.set_stroke(opacity=0.3),
                  graph_c.animate.set_stroke(opacity=1),
                  graph_b_label.animate.set_opacity(0.3),
                  graph_c_label.animate.set_opacity(1))
        self.wait(2)
        self.play(graph_a.animate.set_stroke(opacity=1),
                  graph_b.animate.set_stroke(opacity=1),
                  graph_a_label.animate.set_opacity(1),
                  graph_b_label.animate.set_opacity(1))
        self.wait(2)



        # Se as funções disputarem uma corrida...
        self.play(FadeIn(y_line, y_line_label))
        self.wait(2)
        self.play(FadeIn(x_time_label))
        self.wait(2)

        self.add(graph_a_neg, graph_b_neg, graph_c_neg)
        self.play(graph_a.animate.set_stroke(opacity=0.3),
                  graph_b.animate.set_stroke(opacity=0.3),
                  graph_c.animate.set_stroke(opacity=0.3),
                  graph_a_label.animate.set_opacity(0.3),
                  graph_b_label.animate.set_opacity(0.3),
                  graph_c_label.animate.set_opacity(0.3),
                  FadeIn(x_time_tick, x_time_tick_label))
        self.wait(2)
        self.play(Create(graph_a_pos_1), 
                  Create(graph_b_pos_1),
                  Create(graph_c_pos_1),
                  x_time_tick.animate.move_to(axes.coords_to_point(0.89,0,0)),
                  X_TIME.animate.set_value(1),
                  graph_a_label.animate.set_opacity(1),
                  run_time = 2)
        self.wait(2)
        self.play(Create(graph_a_pos_2),
                  Create(graph_b_pos_2),
                  Create(graph_c_pos_2),
                  x_time_tick.animate.move_to(axes.coords_to_point(2.24,0,0)),
                  X_TIME.animate.set_value(2**(1/2)),
                  graph_b_label.animate.set_opacity(1),
                  run_time = 2)
        self.wait(2)
        self.play(Create(graph_b_pos_3),
                  Create(graph_c_pos_3),
                  x_time_tick.animate.move_to(axes.coords_to_point(3.65,0,0)),
                  X_TIME.animate.set_value(2),
                  graph_c_label.animate.set_opacity(1),
                  run_time = 2)
        self.wait(2)
        self.play(Create(graph_c_pos_4),
                  FadeOut(x_time_tick, x_time_tick_label),
                  run_time = 2)
        self.wait(2)



        self.remove(graph_a, graph_b, graph_c)
        a.set_value(1)
        self.play(FadeIn(t1[0:3], g_a_display, axes_labels, axes_zero),
                  self.camera.frame.animate.scale(1.4286),
                  FadeOut(graph_a_neg, graph_b_neg, graph_c_neg,
                          graph_a_pos_1, graph_b_pos_1, graph_c_pos_1,
                          graph_a_pos_2, graph_b_pos_2, graph_c_pos_2,
                          graph_b_pos_3, graph_c_pos_3,
                          graph_c_pos_4,
                          graph_a_label, graph_b_label, graph_c_label,
                          black_sq1, x_time_label, y_line, y_line_label),
                  run_time=1.5)
        self.wait()
        self.play(FadeIn(graph_1))
        self.wait(2)
        self.play(a.animate.set_value(-1), run_time=3)
        self.wait(2)
        self.play(a.animate.set_value(-5), run_time=2)
        self.wait(2)
        self.play(a.animate.set_value(-0.2), run_time=2)
        self.wait(2)




        # Adiciona os outros termos: + bx + c
        self.play(a.animate.set_value(1), run_time=2)
        self.play(FadeIn(t1[3:7], g_b_display, g_c_display), t1[0:3].animate.shift(LEFT*0.9))
        self.wait(2)



        # Coeficiente 'c'
        black_sq1.scale(0.5).next_to(g_c_display, LEFT, buff=0.5).set_opacity(0.8)
        self.play(FadeIn(black_sq1))
        self.wait(2)


        t2 = MathTex('x = 0', color=GRAY).scale(0.8).next_to(t1, UP)

        t1_2 = MathTex('y ','=',' a0^2 ','+',' b0 ','+',' c ').scale(0.9).to_edge(UP, buff=1.2)
        t1_2[2][0].set_color(BLUE)
        t1_2[4][0].set_color(RED)
        t1_2[6][0].set_color(GREEN)

        red_line1 = Line(UP*0.2, DOWN*0.2, color=RED, stroke_width=4).scale(1.3).rotate(60*DEGREES).move_to(t1_2[2])
        red_line2 = red_line1.copy().move_to(t1_2[4])

        self.play(FadeIn(t2))
        self.wait(2)
        self.play(TransformMatchingShapes(t1, t1_2))
        self.wait(2)
        self.play(Create(red_line1), Create(red_line2))
        self.wait(2)
        self.play(FadeOut(red_line1, red_line2, t1_2[2:6], t2))
        self.play(t1_2[0:2].animate.shift(RIGHT*1.09),
                  t1_2[6].animate.shift(LEFT*1.09))
        self.wait(2)


        c_tick = always_redraw(lambda : Line(LEFT*0.15, RIGHT*0.15).move_to(axes.coords_to_point(0,c.get_value(),0)).set_z_index(3))
        c_tick_label = always_redraw(lambda : c_value_label.copy().set_color(WHITE).scale(0.9).next_to(axes.coords_to_point(0,c.get_value(),0), DL, buff=0.13))

        self.play(FadeIn(c_tick), FadeOut(t1_2[0:2], t1_2[6]),
                  TransformFromCopy(c_value_label, c_tick_label))
        self.play(FadeIn(t1))
        self.wait(2)
        self.play(c.animate.set_value(1), run_time=1)
        self.wait(2)
        self.play(c.animate.set_value(3), run_time=2)
        self.wait(2)
        self.play(c.animate.set_value(-3), run_time=3)
        self.wait(2)
        self.play(c.animate.set_value(1), run_time=2)
        self.wait(2)
        self.play(FadeOut(c_tick, c_tick_label, black_sq1))
        self.wait(2)



        # Coeficiente 'b'
        black_sq1.next_to(g_b_display, RIGHT, buff=0.3)
        black_sq2 = black_sq1.copy().next_to(g_b_display, LEFT, buff=0.3)

        self.play(FadeIn(black_sq1, black_sq2))
        self.wait(2)
        self.play(b.animate.set_value(3), run_time=2)
        self.wait(2)
        self.play(b.animate.set_value(-3), run_time=3)
        self.wait(2)
        self.play(b.animate.set_value(1), run_time=2)
        self.wait(2)

        b_dot = Dot(axes.coords_to_point(0,1,0))
        b_dot_tex = Tex('inclinação aqui').scale(0.8).next_to(axes.get_x_axis(), RIGHT, buff=-0.7).shift(DOWN*0.7)
        b_dot_arrow = always_redraw(lambda : Arrow(b_dot_tex, b_dot))

        tangent_line = always_redraw(lambda: axes.plot(lambda x: (b.get_value())*x + 1,
                         x_range=[-5,5], stroke_width = 6).set_color(GRAY).set_z_index(-2))
        
        tangent_line_label = MathTex('y = bx + c').scale(0.8).next_to(axes.get_x_axis(), RIGHT, buff=1.5)
        tangent_line_label[0][2].set_color(RED)
        tangent_line_label[0][4].set_color(GREEN)

        tangent_line_label2 = always_redraw(lambda : MathTex(f'y =',f'{b.get_value():.1f}','x +',f'{c.get_value():.1f}').scale(0.8).move_to(tangent_line_label, aligned_edge=LEFT))
        tangent_line_label2[1].set_color(RED)
        tangent_line_label2[3].set_color(GREEN)
        always_redraw(lambda : tangent_line_label2[1].set_color(RED))
        always_redraw(lambda : tangent_line_label2[3].set_color(GREEN))
        
        self.play(GrowFromCenter(b_dot), FadeIn(b_dot_tex, b_dot_arrow))
        self.wait(2)
        self.play(Create(tangent_line), run_time=2)
        self.wait(2)
        self.play(FadeOut(b_dot_tex, b_dot_arrow), 
                  FadeIn(tangent_line_label))
        self.wait(2)
        self.play(TransformMatchingShapes(tangent_line_label, tangent_line_label2),
                  TransformFromCopy(b_value_label, tangent_line_label2[1]),
                  TransformFromCopy(c_value_label, tangent_line_label2[3]))
        
        self.remove(tangent_line_label2[0], tangent_line_label2[1], tangent_line_label2[2], tangent_line_label2[3]).add(tangent_line_label2)

        self.wait(2)
        self.play(Indicate(tangent_line_label2[1]))
        self.wait(2)
        self.play(b.animate.set_value(0), run_time=2)
        self.wait(2)
        self.play(b.animate.set_value(-2), run_time=3)
        self.wait(2)

        self.play(FadeOut(tangent_line, tangent_line_label2, b_dot, black_sq1, black_sq2))
        self.wait(2)



        # Mudando os coeficientes
        self.play(a.animate.set_value(2), run_time=2, func_rate=rush_into)
        self.play(a.animate.set_value(0.3), run_time=1)
        self.play(a.animate.set_value(1), run_time=2, func_rate=rush_from)
        self.wait()
        self.play(b.animate.set_value(3), run_time=2, func_rate=rush_into)
        self.play(b.animate.set_value(0), run_time=1)
        self.play(b.animate.set_value(-3), run_time=2, func_rate=rush_from)
        self.wait()
        self.play(c.animate.set_value(3), run_time=2, func_rate=rush_into)
        self.play(c.animate.set_value(-2), run_time=1)
        self.play(c.animate.set_value(1), run_time=2, func_rate=rush_from)
        self.wait(2)



# Sobre a variação da função
class vid8(Scene):
    def construct(self):

        # Função y = x^2
        t4 = MathTex(r'y = x^2').scale(0.9).shift(UP*3)
        


        # Diferente da função do 1o grau... (insert do vídeo anterior)
        insert_border = Rectangle(width=16, height=9, color=WHITE, stroke_width=2).scale(0.65)
        insert_label = Tex(r'Função do 1\textsuperscript{o} grau').scale(0.9).next_to(insert_border, UP, buff=0.1).shift(RIGHT*0.3)
        yt_logo = ImageMobject("youtube_logo.png").scale(0.15).next_to(insert_label, LEFT, buff=0.2).shift(UP*0.05)
        insert_tex = Tex('INSERIR VÍDEO AQUI', color=YELLOW)

        self.play(FadeIn(insert_border, yt_logo, insert_label, insert_tex))
        self.wait(2)
        self.play(FadeOut(insert_border, yt_logo, insert_label, insert_tex))
        self.wait(2)



            # Tabela
        v_line = Line(UP, DOWN, stroke_width = 2).scale(3).shift(DOWN*0.3)
        h_line_1 = Line(LEFT, RIGHT, stroke_width = 2).scale(2)
        h_line_2 = h_line_1.copy()
        h_line_3 = h_line_1.copy()
        h_line_4 = h_line_1.copy()
        h_line_5 = h_line_1.copy()
        h_line_6 = h_line_1.copy()
        h_lines = VGroup(h_line_1, h_line_2, h_line_3, h_line_4, h_line_5, h_line_6).arrange(DOWN, buff = 1).shift(DOWN*0.8)
        
        x_table = MathTex('x', color = RED).scale(1.2).next_to(v_line, LEFT, buff = 0.9).shift(UP*2.5)
        fx_table = MathTex('y', color = BLUE).scale(1.2).next_to(v_line, RIGHT, buff = 0.9).shift(UP*2.5)

        x_value_1 = MathTex('1').scale(1).next_to(v_line, LEFT, buff = 0.9).shift(UP*1.5)
        x_value_2 = MathTex('2').scale(1).next_to(x_value_1, DOWN, buff=0.65)
        x_value_3 = MathTex(r'3').scale(1).next_to(x_value_2, DOWN, buff=0.65)
        x_value_4 = MathTex(r'4').scale(1).next_to(x_value_3, DOWN, buff=0.65)
        x_value_5 = MathTex(r'5').scale(1).next_to(x_value_4, DOWN, buff=0.65)
        x_values = VGroup(x_value_1, x_value_2, x_value_3, x_value_4, x_value_5)

        fx_value_1 = MathTex('1').scale(1).next_to(v_line, RIGHT, buff = 0.9).shift(UP*1.5)
        fx_value_2 = MathTex('4').scale(1).next_to(fx_value_1, DOWN, buff=0.65)
        fx_value_3 = MathTex(r'9').scale(1).next_to(fx_value_2, DOWN, buff=0.65)
        fx_value_4 = MathTex(r'16').scale(1).next_to(fx_value_3, DOWN, buff=0.65)
        fx_value_5 = MathTex(r'25').scale(1).next_to(fx_value_4, DOWN, buff=0.65)
        fx_values = VGroup(fx_value_1, fx_value_2, fx_value_3, fx_value_4, fx_value_5)

        g_table = VGroup(v_line, h_lines, x_table, fx_table, x_values, fx_values).scale(0.8).shift(DOWN*0.4)



        # Setas nos valores de x
        x_arrow_1 = CurvedArrow(UP*0.7, DOWN*0.5, radius=0.7).scale(0.5).next_to(h_line_2, LEFT, buff=0.1).shift(UP*0.1)
        x_arrow_2 = x_arrow_1.copy().next_to(h_line_3, LEFT, buff=0.1)
        x_arrow_3 = x_arrow_1.copy().next_to(h_line_4, LEFT, buff=0.1).shift(DOWN*0.1)
        x_arrow_4 = x_arrow_1.copy().next_to(h_line_5, LEFT, buff=0.1).shift(DOWN*0.2)
        x_arrows = VGroup(x_arrow_1, x_arrow_2, x_arrow_3, x_arrow_4).set_color(GRAY)

        x_arrow_1_label = MathTex('+1').scale(0.8).next_to(x_arrow_1, LEFT, buff=0.15)
        x_arrow_2_label = x_arrow_1_label.copy().next_to(x_arrow_2, LEFT, buff=0.15)
        x_arrow_3_label = x_arrow_1_label.copy().next_to(x_arrow_3, LEFT, buff=0.15)
        x_arrow_4_label = x_arrow_1_label.copy().next_to(x_arrow_4, LEFT, buff=0.15)
        x_arrows_labels = VGroup(x_arrow_1_label, x_arrow_2_label, x_arrow_3_label, x_arrow_4_label).set_color(GRAY)


        fx_arrow_1 = CurvedArrow(UP*0.7, DOWN*0.5, radius=-0.7).scale(0.5).next_to(h_line_2, RIGHT, buff=0.1).shift(UP*0.1)
        fx_arrow_2 = fx_arrow_1.copy().next_to(h_line_3, RIGHT, buff=0.1)
        fx_arrow_3 = fx_arrow_1.copy().next_to(h_line_4, RIGHT, buff=0.1).shift(DOWN*0.1)
        fx_arrow_4 = fx_arrow_1.copy().next_to(h_line_5, RIGHT, buff=0.1).shift(DOWN*0.2)
        fx_arrows = VGroup(fx_arrow_1, fx_arrow_2, fx_arrow_3, fx_arrow_4).set_color(GRAY)

        fx_arrow_1_label = MathTex('+3').scale(0.8).next_to(fx_arrow_1, RIGHT, buff=0.15)
        fx_arrow_2_label = MathTex('+5').scale(0.8).next_to(fx_arrow_2, RIGHT, buff=0.15)
        fx_arrow_3_label = MathTex('+7').scale(0.8).next_to(fx_arrow_3, RIGHT, buff=0.15)
        fx_arrow_4_label = MathTex('+9').scale(0.8).next_to(fx_arrow_4, RIGHT, buff=0.15)
        fx_arrows_labels = VGroup(fx_arrow_1_label, fx_arrow_2_label, fx_arrow_3_label, fx_arrow_4_label).set_color(GRAY)


    
            # Criando tabela
        self.play(FadeIn(v_line, h_lines, x_table, fx_table, t4))
        self.wait(2)
        self.play(FadeIn(x_value_1), run_time=0.7)
        self.play(FadeIn(x_value_2, x_arrow_1), GrowFromCenter(x_arrow_1_label), run_time=0.7)
        self.play(FadeIn(x_value_3, x_arrow_2), GrowFromCenter(x_arrow_2_label), run_time=0.7)
        self.play(FadeIn(x_value_4, x_arrow_3), GrowFromCenter(x_arrow_3_label), run_time=0.7)
        self.play(FadeIn(x_value_5, x_arrow_4), GrowFromCenter(x_arrow_4_label), run_time=0.7)
        self.wait(2)
        self.play(LaggedStart(FadeIn(fx_value_1),
                              FadeIn(fx_value_2),
                              FadeIn(fx_value_3),
                              FadeIn(fx_value_4),
                              FadeIn(fx_value_5),
                              lag_ratio=0.5))
        self.wait(2)
        self.play(FadeIn(fx_arrow_1, fx_arrow_1_label))
        self.play(FadeIn(fx_arrow_2, fx_arrow_2_label))
        self.play(FadeIn(fx_arrow_3, fx_arrow_3_label))
        self.play(FadeIn(fx_arrow_4, fx_arrow_4_label))
        self.wait(2)



        # Diferença das diferenças
        fx_arrow_2_1 = CurvedArrow(UP*0.7, DOWN*0.5, radius=-0.7).scale(0.5).next_to(fx_arrow_1_label, RIGHT, buff=0.2).shift(DOWN*0.5)
        fx_arrow_2_2 = fx_arrow_2_1.copy().next_to(fx_arrow_2_label, RIGHT, buff=0.2).shift(DOWN*0.5)
        fx_arrow_2_3 = fx_arrow_2_1.copy().next_to(fx_arrow_3_label, RIGHT, buff=0.2).shift(DOWN*0.5)
        fx_arrows_2 = VGroup(fx_arrow_2_1, fx_arrow_2_2, fx_arrow_2_3).set_color(GRAY)

        fx_arrow_1_label_2 = MathTex('+2').scale(0.8).next_to(fx_arrow_2_1, RIGHT, buff=0.15)
        fx_arrow_2_label_2 = fx_arrow_1_label_2.copy().next_to(fx_arrow_2_2, RIGHT, buff=0.15)
        fx_arrow_3_label_2 = fx_arrow_1_label_2.copy().next_to(fx_arrow_2_3, RIGHT, buff=0.15)
        fx_arrows_labels_2 = VGroup(fx_arrow_1_label_2, fx_arrow_2_label_2, fx_arrow_3_label_2).set_color(GRAY)

        self.play(fx_arrows_labels.animate.set_color(YELLOW))
        self.wait(2)
        self.play(FadeIn(fx_arrow_2_1, fx_arrow_1_label_2))
        self.play(FadeIn(fx_arrow_2_2, fx_arrow_2_label_2))
        self.play(FadeIn(fx_arrow_2_3, fx_arrow_3_label_2))
        self.wait(2)
        self.play(fx_arrows_labels.animate.set_color(GRAY))
        self.wait(2)



        rectangle_1 = SurroundingRectangle(fx_values, buff=0.15, color=YELLOW, stroke_opacity=0.7)
        rectangle_2 = SurroundingRectangle(fx_arrows_labels, buff=0.12, color=YELLOW, stroke_opacity=0.7)
        self.play(FadeIn(rectangle_1))
        self.wait(2)
        self.play(ReplacementTransform(rectangle_1, rectangle_2))
        self.wait(2)



        # Faça o mesmo com f(x) = x^3
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        t6 = Tex(r'Faça o mesmo experimento \\ com a função $y = x^3$ e veja \\ se existe algum padrão', color=GRAY, tex_template=myTemplate, tex_environment="justify").scale(0.7).to_edge(UL)
        self.play(FadeIn(t6))
        self.wait(2)
      


# Comparando a velocidade das funções afim e quadrática
class vid9(MovingCameraScene):
    def construct(self):

        axes = Axes(x_range = [-5, 5, 1],
                    y_range = [-2, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        x_label = MathTex("x").next_to(axes.get_x_axis(), DR, buff = 0)
        y_label = MathTex("y").next_to(axes.get_y_axis(), UL, buff = 0).shift(DOWN*0.1)
        axes_labels = VGroup(x_label, y_label).set_color(WHITE).set_opacity(0.6)
        axes_zero = MathTex('0').scale(0.8).next_to(axes.coords_to_point(0,0,0), DL, buff = 0.13).set_opacity(0.6)
        


        # Gráfico da função afim
        axes_1 = axes.copy()
        axes_labels_1 = axes_labels.copy()
        graph_1 = axes_1.plot(lambda x: 0.7*x + 1,
                            x_range=[-4, 4], stroke_width = 4).set_color(RED).set_z_index(2)

        g_graph_1_aux = VGroup(axes_1, axes_labels_1, graph_1).move_to(ORIGIN)
        g_graph_1_box = SurroundingRectangle(g_graph_1_aux, buff=0.3, color=GRAY, stroke_width=2)
        g_graph_1_label = MathTex('y = ax + b', color=graph_1.get_color()).scale(0.9).next_to(g_graph_1_box, UP, buff=0.1)

        g_graph_1 = VGroup(g_graph_1_aux, g_graph_1_box, g_graph_1_label)



        # Gráfico da função quadrática
        axes_2 = axes.copy()
        axes_labels_2 = axes_labels.copy()
        graph_2 = axes_2.plot(lambda x: 0.25*x**2,
                            x_range=[-4, 4], stroke_width = 4).set_color(BLUE).set_z_index(2)

        g_graph_2_aux = VGroup(axes_2, axes_labels_2, graph_2).move_to(ORIGIN)
        g_graph_2_box = SurroundingRectangle(g_graph_2_aux, buff=0.3, color=GRAY, stroke_width=2)
        g_graph_2_label = MathTex('y = ax^2 + bx + c', color=graph_2.get_color()).scale(0.9).next_to(g_graph_2_box, UP, buff=0.1)

        g_graph_2 = VGroup(g_graph_2_aux, g_graph_2_box, g_graph_2_label)


        g_graphs = VGroup(g_graph_1, g_graph_2).arrange(RIGHT, buff=0.5, aligned_edge=DOWN).shift(UP*0.2)
        
        

        # Velocidade da função afim
        X_VALUE_1 = ValueTracker(-4)

        reference_dot_1 = always_redraw(lambda : Dot(graph_1.get_point_from_function(t=X_VALUE_1.get_value()), radius=0))
        delta_x_line_1 = always_redraw(lambda : DashedLine((0,0,0), (0.5,0,0)).next_to(reference_dot_1, RIGHT, buff=0))
        speed_arrow_1 = Arrow((0,0,0), (0,1,0), max_stroke_width_to_length_ratio=10, max_tip_length_to_length_ratio=0.4, color=YELLOW).move_to(delta_x_line_1.get_edge_center(RIGHT), aligned_edge=DOWN).set_z_index(3)
        speed_arrow_1_label = always_redraw(lambda : MathTex('v', color=YELLOW).scale(0.9).next_to(speed_arrow_1, RIGHT, buff=0.1).set_z_index(3))
          
    

        # Velocidade da função quadrática
        X_VALUE_2 = ValueTracker(-4)

        reference_dot_2a = always_redraw(lambda : Dot(graph_2.get_point_from_function(t=X_VALUE_2.get_value()), radius=0))
        reference_dot_2b = always_redraw(lambda : Dot(graph_2.get_point_from_function(t=X_VALUE_2.get_value()), radius=0).shift(RIGHT*0.5))
        reference_dot_2c = always_redraw(lambda : Dot(graph_2.get_point_from_function(t=X_VALUE_2.get_value() + 1), radius=0))
        

        delta_x_line_2 = always_redraw(lambda : DashedLine((0,0,0), (0.5,0,0)).next_to(reference_dot_2a, RIGHT, buff=0))
        speed_arrow_2 = always_redraw(lambda : Arrow(reference_dot_2b, reference_dot_2c, buff=0, max_stroke_width_to_length_ratio=7, max_tip_length_to_length_ratio=0.3, color=YELLOW).set_z_index(3))
        speed_arrow_2_label = always_redraw(lambda : MathTex('v', color=YELLOW).scale(0.9).next_to(speed_arrow_2, RIGHT, buff=0.1).set_z_index(3))
        
        



        # Animação das velocidades
        self.play(FadeIn(g_graphs))
        self.wait(2)

        self.play(FadeIn(reference_dot_1, delta_x_line_1, speed_arrow_1, speed_arrow_1_label))
        speed_arrow_1.add_updater(lambda m: m.become(Arrow((0,0,0), (0,1,0), max_stroke_width_to_length_ratio=10, max_tip_length_to_length_ratio=0.4, color=YELLOW).move_to(delta_x_line_1.get_edge_center(RIGHT), aligned_edge=DOWN).set_z_index(3)))
        self.wait(2)
        self.play(X_VALUE_1.animate.set_value(3), run_time=5)
        self.wait(2)


        self.play(FadeIn(reference_dot_2a, reference_dot_2b, reference_dot_2c, delta_x_line_2, speed_arrow_2, speed_arrow_2_label))
        self.wait(2)
        self.play(X_VALUE_2.animate.set_value(-1), run_time=5)
        self.wait(2)
        self.play(X_VALUE_2.animate.set_value(3), run_time=5)
        self.wait(2)



        # Funções afim e quadrática descrevem MRU e MRUV
        black_sq1 = Rectangle(height=2, width=1, color=BLACK, fill_opacity=0.8, stroke_width=0).scale(4.2).set_z_index(7).move_to(g_graph_2_label, aligned_edge=DL)
        self.play(FadeOut(g_graph_1_aux, g_graph_1_box, g_graph_2_aux, g_graph_2_box,
                          reference_dot_1, delta_x_line_1, speed_arrow_1, speed_arrow_1_label,
                          reference_dot_2a, reference_dot_2b, reference_dot_2c, delta_x_line_2, speed_arrow_2, speed_arrow_2_label),
                  FadeIn(black_sq1))
        self.wait(2)
        self.add(g_graph_1_label, g_graph_2_label)

        car_1 = ImageMobject("car_inverted_to_white_transparent.png").scale(0.5).shift(DOWN*2.5+LEFT*8.2)
        car_2 = car_1.copy()

        foot = ImageMobject("swapped_colors_image_1.png").scale(0.3).shift(UP).set_z_index(2)
        pedal = ImageMobject("swapped_colors_image_2.png").scale(0.3).shift(UP*0.6+RIGHT*0.7)
        black_sq2 = Rectangle(height=2, width=1, color=BLACK, fill_opacity=1, stroke_width=0).set_z_index(7).next_to(pedal, DOWN, buff=0)
        
            # Função afim : MRU      
        self.add(car_1, car_2, black_sq2)

        self.play(FadeIn(foot, pedal))
        self.play(foot.animate.rotate(-0.17, about_point=ORIGIN),
                  pedal.animate.rotate(-0.17, about_point=ORIGIN), run_time=2)
        self.play(car_1.animate.shift(RIGHT*17),
                  run_time=7, rate_func=linear)
        self.play(FadeOut(foot, pedal, black_sq1))
        self.wait(2)



            # Função quadrática : MRUV
        foot.rotate(0.26, about_point=ORIGIN)
        pedal.rotate(0.26, about_point=ORIGIN)
        black_sq1.move_to(g_graph_1_label, aligned_edge=DR)

        self.play(FadeIn(foot, pedal, black_sq1))
        self.play(foot.animate.rotate(-0.44, about_point=ORIGIN),
                  pedal.animate.rotate(-0.44, about_point=ORIGIN), run_time=5)
        self.play(car_2.animate.shift(RIGHT*17), run_time=5, rate_func=rush_into)
        self.play(FadeOut(foot, pedal, black_sq1))
        self.remove(black_sq2)
        self.wait(2)



        # As funções de posição de MRU e MRUV são da fato uma afim e uma quadrática
        car_1.shift(LEFT*17).shift(UP*2.5)
        car_2.shift(LEFT*17).shift(UP*1)

        t1 = Tex('Movimento Retilíneo Uniforme', color=RED).scale(0.8)
        t2 = Tex('Movimento Retilíneo Uniformemente Variado', color=BLUE).scale(0.8).shift(DOWN*1.5)

        self.play(car_1.animate.shift(RIGHT*17), run_time=7, rate_func=linear)
        self.play(FadeIn(t1, shift=RIGHT))
        self.wait(2)
        self.play(car_2.animate.shift(RIGHT*17), run_time=5, rate_func=rush_into)
        self.play(FadeIn(t2, shift=RIGHT))
        self.wait(2)

        t3 = MathTex('S(t) = S_0 + vt', color=RED).move_to(t1)
        t4 = MathTex(r'S(t) = S_0 + v_0t + \frac{1}{2}at^2', color=BLUE).move_to(t2)
        self.play(ReplacementTransform(t1, t3),
                  Indicate(g_graph_1_label))
        self.wait(2)
        self.play(ReplacementTransform(t2, t4),
                  Indicate(g_graph_2_label))
        self.wait(2)



# (v1) (p/ Instagram) Gráfico mudando o valor dos coeficientes a,b,c
class vid10(MovingCameraScene):
    def construct(self):

        t1 = MathTex('y ','=',' ax^2 ','+',' bx ','+',' c ').scale(0.8).to_edge(UP, buff=1)
        t1[2][0].set_color(BLUE)
        t1[4][0].set_color(RED)
        t1[6][0].set_color(GREEN)



        # ValueTrackers dos coeficientes 'a' e 'b'
        a = ValueTracker(1)
        b = ValueTracker(0)
        c = ValueTracker(0)



        # Mostrador do valor de 'b'
        b_label = MathTex('b', color=t1[4][0].get_color()).scale(0.7)
        b_numberline = NumberLine(x_range=[-5,5], length=2, tick_size=0,
                                  stroke_width=5, color=GRAY).scale(0.55).rotate(90*DEGREES).next_to(b_label, DOWN, buff=0.2)
        b_numberline_dot = always_redraw(lambda: Dot(b_numberline.number_to_point(b.get_value()), color=b_label.get_color()).scale(0.8))
        b_value_label = always_redraw(lambda: MathTex(f'{b.get_value():.1f}', color=b_label.get_color()).scale(0.6).next_to(b_numberline, DOWN, buff=0.1))
        
        g_b_display = VGroup(b_label, b_numberline, b_numberline_dot, b_value_label).shift(UP*2)



        # Mostrador do valor de 'a'
        a_label = MathTex('a', color=t1[2][0].get_color()).scale(0.7)
        a_numberline = NumberLine(x_range=[-5,5], length=2, tick_size=0,
                                  stroke_width=5, color=GRAY).scale(0.55).rotate(90*DEGREES).next_to(a_label, DOWN, buff=0.2)
        a_numberline_dot = always_redraw(lambda: Dot(a_numberline.number_to_point(a.get_value()), color=a_label.get_color()).scale(0.8))
        a_value_label = always_redraw(lambda: MathTex(f'{a.get_value():.1f}', color=a_label.get_color()).scale(0.6).next_to(a_numberline, DOWN, buff=0.1))

        g_a_display = VGroup(a_label, a_numberline, a_numberline_dot, a_value_label).next_to(g_b_display, LEFT, buff=0.5, aligned_edge=DOWN)

      

        # Mostrador do valor de 'b'
        c_label = MathTex('c', color=t1[6][0].get_color()).scale(0.7)
        c_numberline = NumberLine(x_range=[-5,5], length=2, tick_size=0,
                                  stroke_width=5, color=GRAY).scale(0.55).rotate(90*DEGREES).next_to(c_label, DOWN, buff=0.2)
        c_numberline_dot = always_redraw(lambda: Dot(c_numberline.number_to_point(c.get_value()), color=c_label.get_color()).scale(0.8))
        c_value_label = always_redraw(lambda: MathTex(f'{c.get_value():.1f}', color=c_label.get_color()).scale(0.6).next_to(c_numberline, DOWN, buff=0.1))
        
        g_c_display = VGroup(c_label, c_numberline, c_numberline_dot, c_value_label).next_to(g_b_display, RIGHT, buff=0.5, aligned_edge=DOWN)



        g_displays = VGroup(g_a_display, g_b_display, g_c_display)



        # Box de fundo dos mostradores
        black_sq = Square(color=BLACK, side_length=1).scale(3.2).set_opacity(0.7).set_z_index(-1).move_to(g_a_display, aligned_edge=DL).shift(LEFT*0.2+DOWN*0.2)



        # Gráfico
        axes = Axes(x_range = [-5, 5, 1],
                    y_range = [-5, 5, 1],
                    x_length = 9,
                    y_length = 9,
                    axis_config = {"include_ticks" : False}).scale(0.5).set_opacity(1).move_to(ORIGIN).shift(DOWN*2)
        x_label = MathTex("x").scale(0.8).next_to(axes.get_x_axis(), DR, buff = 0)
        y_label = MathTex("y").scale(0.8).next_to(axes.get_y_axis(), UL, buff = 0).shift(DOWN*0.1)
        axes_labels = VGroup(x_label, y_label).set_color(WHITE).set_opacity(0.6)
        axes_zero = MathTex('0').scale(0.64).next_to(axes.coords_to_point(0,0,0), DL, buff = 0.13).set_opacity(0.6)

        graph_1 = always_redraw(lambda: axes.plot(lambda x: (a.get_value())*x**2 + (b.get_value())*x + (c.get_value()),
                         x_range=[-7,7], stroke_width = 6).set_color(GREEN).set_z_index(-2))
        
        tangent_line = axes.plot(lambda x: 2*x,
                         x_range=[-5,5], stroke_width = 6).set_color(GRAY).set_z_index(-2)
        
        

        # Borda para o gráfico não escapar dos eixos
        external_border = Square(fill_opacity=1, color=YELLOW).scale(10)
        internal_border = always_redraw(lambda: Circle(radius=1.7, fill_opacity=1, color=BLUE))
        border = always_redraw(lambda: Difference(external_border, internal_border, fill_opacity=1, color=BLACK).set_z_index(-1).move_to(axes.coords_to_point(-(b.get_value())/2*(a.get_value()), -((b.get_value())**2 - 4*(a.get_value())*(c.get_value()))/4*(a.get_value()), 0)))

        g_graph = VGroup(axes, axes_labels, axes_zero, graph_1, border).scale(0.7).shift(DOWN*1.8)

        reel_border_ref = Rectangle(width=9, height=16).scale(0.5)



        # Animação
        t1[0:3].shift(RIGHT*0.9)

        self.add(border, black_sq)
        self.play(FadeIn(axes, axes_labels, axes_zero, t1[0:3], g_a_display))
        self.play(Create(graph_1), run_time=2.5)
          
        self.play(a.animate.set_value(3), run_time=2)
        self.play(a.animate.set_value(0.3), run_time=3)
        self.play(a.animate.set_value(-1), run_time=2)
        self.play(a.animate.set_value(-3), run_time=2)
        self.play(a.animate.set_value(-0.3), run_time=3)
        self.play(a.animate.set_value(1), run_time=2)


        # Adiciona 'b'
        t1[3:5].shift(RIGHT*0.35)

        self.play(t1[0:3].animate.shift(LEFT*0.55), 
                  FadeIn(t1[3:5], g_b_display))

        self.play(b.animate.set_value(-2), run_time=2)
        self.play(b.animate.set_value(2), run_time=2)

        self.play(Create(tangent_line))
        tangent_line = always_redraw(lambda: axes.plot(lambda x: (b.get_value())*x,
                         x_range=[-5,5], stroke_width = 6).set_color(GRAY).set_z_index(-2))
        

        self.play(b.animate.set_value(-1), run_time=2)
        self.play(b.animate.set_value(-3), run_time=2)
        self.play(b.animate.set_value(1), run_time=2)
        self.play(b.animate.set_value(3), run_time=2)
        self.play(b.animate.set_value(0), run_time=2)
        self.play(FadeOut(tangent_line))



        # Adiciona 'c'
        self.play(t1[0:3].animate.shift(LEFT*0.35), 
                  t1[3:5].animate.shift(LEFT*0.35), 
                  FadeIn(t1[5:8], g_c_display))

        self.play(c.animate.set_value(1), run_time=2)
        self.play(c.animate.set_value(3), run_time=2)
        self.play(c.animate.set_value(-1), run_time=3)
        self.play(c.animate.set_value(-3), run_time=2)
        self.play(c.animate.set_value(0), run_time=3)



# (v2) (p/ Instagram) Gráfico mudando o valor dos coeficientes a,b,c
class vid11(MovingCameraScene):
    def construct(self):

        t1 = MathTex('y ','=',' ax^2 ','+',' bx ','+',' c ').scale(0.8).to_edge(UP, buff=0.8)
        t1[2][0].set_color(BLUE)
        t1[4][0].set_color(RED)
        t1[6][0].set_color(GREEN)



        # ValueTrackers dos coeficientes 'a' e 'b'
        a = ValueTracker(1)
        b = ValueTracker(0)
        c = ValueTracker(0)




        # Mostrador do valor de 'a'
        a_numberline = NumberLine(x_range=[-5,5], length=2, tick_size=0,
                                  stroke_width=5, color=GRAY).scale(0.55).next_to(t1, DOWN, buff=0.8)
        a_label = MathTex('a', color=t1[2][0].get_color()).scale(0.7).next_to(a_numberline, LEFT, buff=0.2)
        a_numberline_dot = always_redraw(lambda: Dot(a_numberline.number_to_point(a.get_value()), color=a_label.get_color()).scale(0.8))
        a_value_label = always_redraw(lambda: MathTex(f'{a.get_value():.1f}', color=a_label.get_color()).scale(0.6).next_to(a_numberline, RIGHT, buff=0.1))

        g_a_display = VGroup(a_label, a_numberline, a_numberline_dot, a_value_label)
      


        # Mostrador do valor de 'b'
        b_numberline = NumberLine(x_range=[-5,5], length=2, tick_size=0,
                                  stroke_width=5, color=GRAY).scale(0.55).next_to(a_numberline, DOWN, buff=0.5, aligned_edge=LEFT)
        b_label = MathTex('b', color=t1[4][0].get_color()).scale(0.7).next_to(b_numberline, LEFT, buff=0.2)
        b_numberline_dot = always_redraw(lambda: Dot(b_numberline.number_to_point(b.get_value()), color=b_label.get_color()).scale(0.8))
        b_value_label = always_redraw(lambda: MathTex(f'{b.get_value():.1f}', color=b_label.get_color()).scale(0.6).next_to(b_numberline, RIGHT, buff=0.1))
        
        g_b_display = VGroup(b_label, b_numberline, b_numberline_dot, b_value_label)#.next_to(g_a_display, DOWN, buff=0.5, aligned_edge=LEFT)



        # Mostrador do valor de 'b'
        c_numberline = NumberLine(x_range=[-5,5], length=2, tick_size=0,
                                  stroke_width=5, color=GRAY).scale(0.55).next_to(b_numberline, DOWN, buff=0.5, aligned_edge=LEFT)
        c_label = MathTex('c', color=t1[6][0].get_color()).scale(0.7).next_to(c_numberline, LEFT, buff=0.2)
        c_numberline_dot = always_redraw(lambda: Dot(c_numberline.number_to_point(c.get_value()), color=c_label.get_color()).scale(0.8))
        c_value_label = always_redraw(lambda: MathTex(f'{c.get_value():.1f}', color=c_label.get_color()).scale(0.6).next_to(c_numberline, RIGHT, buff=0.1))
        
        g_c_display = VGroup(c_label, c_numberline, c_numberline_dot, c_value_label)#.next_to(g_b_display, DOWN, buff=0.5, aligned_edge=LEFT)



        g_displays = VGroup(g_a_display, g_b_display, g_c_display)



        # Box de fundo dos mostradores
        black_sq = Square(color=BLACK, side_length=1).scale(3.2).set_opacity(0.7).set_z_index(-1).move_to(g_c_display, aligned_edge=DOWN).shift(DOWN*0.2)



        # Gráfico
        axes = Axes(x_range = [-5, 5, 1],
                    y_range = [-5, 5, 1],
                    x_length = 9,
                    y_length = 9,
                    axis_config = {"include_ticks" : False}).scale(0.5).set_opacity(1).move_to(ORIGIN).shift(DOWN*1.6)
        x_label = MathTex("x").scale(0.8).next_to(axes.get_x_axis(), DR, buff = 0)
        y_label = MathTex("y").scale(0.8).next_to(axes.get_y_axis(), UL, buff = 0).shift(DOWN*0.1)
        axes_labels = VGroup(x_label, y_label).set_color(WHITE).set_opacity(1)
        axes_zero = MathTex('0').scale(0.64).next_to(axes.coords_to_point(0,0,0), DL, buff = 0.13).set_opacity(0.6)

        graph_1 = always_redraw(lambda: axes.plot(lambda x: (a.get_value())*x**2 + (b.get_value())*x + (c.get_value()),
                         x_range=[-7,7], stroke_width = 6).set_color(GREEN).set_z_index(-2))
        
        tangent_line = axes.plot(lambda x: 2*x,
                         x_range=[-5,5], stroke_width = 4).set_color(GRAY).set_z_index(-2)
        
        

        # Borda para o gráfico não escapar dos eixos
        external_border = Square(fill_opacity=1, color=YELLOW).scale(10)
        internal_border = always_redraw(lambda: Circle(radius=1.7, fill_opacity=1, color=BLUE))
        border = always_redraw(lambda: Difference(external_border, internal_border, fill_opacity=1, color=BLACK).set_z_index(-1).move_to(axes.coords_to_point(-(b.get_value())/2*(a.get_value()), -((b.get_value())**2 - 4*(a.get_value())*(c.get_value()))/4*(a.get_value()), 0)))

        g_graph = VGroup(axes, axes_labels, axes_zero, graph_1, border).scale(0.7).shift(DOWN*1.8)

        reel_border_ref = Rectangle(width=9, height=16).scale(0.5)



        # Animação
        t1[0:3].shift(RIGHT*0.9)

        self.add(border, black_sq)
        self.play(FadeIn(axes, axes_labels, axes_zero, t1[0:3], g_a_display))
        self.play(Create(graph_1), run_time=2.5)
          
        self.play(a.animate.set_value(3), run_time=2)
        self.play(a.animate.set_value(0.3), run_time=3)
        self.play(a.animate.set_value(-3), run_time=3)
        self.play(a.animate.set_value(1), run_time=3)


        # Adiciona 'b'
        t1[3:5].shift(RIGHT*0.35)

        self.play(t1[0:3].animate.shift(LEFT*0.55), 
                  FadeIn(t1[3:5], g_b_display))

        self.play(b.animate.set_value(-2), run_time=2)
        self.play(b.animate.set_value(2), run_time=2)

        self.play(Create(tangent_line))
        tangent_line.add_updater(lambda m: m.become(axes.plot(lambda x: (b.get_value())*x,
                         x_range=[-5,5], stroke_width = 4).set_color(GRAY).set_z_index(-2)))
        

        self.play(b.animate.set_value(-3), run_time=3)
        self.play(b.animate.set_value(3), run_time=3)
        self.play(b.animate.set_value(0), run_time=2)
        self.wait(2)
        self.play(FadeOut(tangent_line))
        self.wait(2)



        # Adiciona 'c'
        self.play(t1[0:3].animate.shift(LEFT*0.35), 
                  t1[3:5].animate.shift(LEFT*0.35), 
                  FadeIn(t1[5:8], g_c_display))

        self.play(c.animate.set_value(1), run_time=2)
        self.play(c.animate.set_value(3), run_time=2)
        self.play(c.animate.set_value(-3), run_time=3)
        self.play(c.animate.set_value(0), run_time=2)
