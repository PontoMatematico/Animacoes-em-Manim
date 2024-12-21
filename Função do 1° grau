# Função do 1° grau

from manim import *

# Introdução
class vid1(Scene):
    def construct(self):

        # Título
        t1 = Tex(r'Função do 1\textsuperscript{o} grau').scale(1).to_edge(UP)
        ul_t1 = Underline(t1)
        ul_t1_aux = Underline(t1[0][10:16])
        t2 = Tex(r'Função afim', color=GRAY).scale(1).next_to(ul_t1, DOWN)
        self.play(Succession(FadeIn(t1), Create(ul_t1)))
        self.wait(2)
        self.play(FadeIn(t2))
        self.wait(2)
        self.play(FadeOut(t2))
        self.wait(2)



        # Definição de função do 1o grau
        t3 = MathTex(r'f: \mathbb{R} \to \mathbb{R}',' \:\:\:,\:\:\: f(x) = ax + b').scale(0.9)
        t3_box = SurroundingRectangle(t3, buff=0.15, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-2)
        self.play(Write(t3[0]))
        self.wait(2)
        self.play(Write(t3[1]))
        self.play(FadeIn(t3_box))
        self.wait(2)



        #a,b são reais e 'a' é diferente de zero
        t4 = MathTex(r'a,b \in \mathbb{R}', color=YELLOW).scale(0.8).next_to(t3, DOWN).shift(RIGHT*2.1)
        t5 = MathTex(r'a \neq 0', color=YELLOW).scale(0.8).next_to(t3, DOWN).shift(RIGHT*2.1)
        self.play(t3[1][6].animate.set_color(YELLOW), t3[1][9].animate.set_color(YELLOW), FadeIn(t4))
        self.wait(2)
        self.play(t3[1][9].animate.set_color(WHITE), FadeOut(t4))
        self.play(FadeIn(t5))
        self.wait(2)



        # Se 'a' fosse igual a zero...
        t6 = MathTex('f(x) = 0x + b').scale(0.9).move_to(t3, aligned_edge=RIGHT)
        t6[0][5].set_color(YELLOW)
        t7 = MathTex('f(x) = b').scale(0.9).move_to(t6, aligned_edge=LEFT)
        self.play(TransformMatchingShapes(t3[1][6:10], t6[0][5:9]))
        self.play(LaggedStart(FadeOut(t6[0][5:8]), TransformMatchingShapes(t6[0][8], t7[0][5]), lag_ratio=0.5))
        self.wait(2)
        t3[1][6].set_color(WHITE)
        self.play(Succession(FadeOut(t5, t7[0][5]), FadeIn(t3[1][6:10])))
        self.wait(2)



        # Sobre o nome "1o grau"
        self.play(Indicate(t1[0][10:16], scale_factor=1), Indicate(ul_t1_aux, scale_factor=1))
        self.remove(ul_t1_aux)
        self.wait(2)
        self.play(t3[1][6:10].animate.set_color(YELLOW))
        self.wait(2)



        # 'a' e 'b' assumindo diferentes valores
        t8 = MathTex('f(x) = 2x + 1', color=YELLOW).scale(0.9).move_to(t6, aligned_edge=LEFT)
        t8[0][6:8].set_color(WHITE)
        t9 = MathTex('f(x) = 4x - 3', color=YELLOW).scale(0.9).move_to(t6, aligned_edge=LEFT)
        t9[0][6:8].set_color(WHITE)
        t10 = MathTex(r'f(x) = \pi x + e', color=YELLOW).scale(0.9).move_to(t6, aligned_edge=RIGHT)
        t10[0][6:8].set_color(WHITE)
        self.play(t3[1][7:9].animate.set_color(WHITE))
        self.wait(2)
        self.play(TransformMatchingShapes(t3[1][6:10], t8[0][5:9]))
        #self.wait(0.5)
        self.play(TransformMatchingShapes(t8[0][5:9], t9[0][5:9]))
        #self.wait(0.5)
        self.play(TransformMatchingShapes(t9[0][5:9], t10[0][5:9]))
        #self.wait(0.5)
        self.play(TransformMatchingShapes(t10[0][5:9], t3[1][6:10]))
        self.wait(2)



        # Sobre as letras usadas serem apenas convenções
        self.play(t3[0][0].animate.set_color(BLUE), t3[1][1].animate.set_color(BLUE))
        #self.wait(0.5)
        self.play(t3[1][3].animate.set_color(RED), t3[1][7].animate.set_color(RED))
        #self.wait(0.5)
        self.play(t3[1][6].animate.set_color(YELLOW))
        #self.wait(0.5)
        self.play(t3[1][9].animate.set_color(YELLOW))
        self.wait(2)

        t11 = MathTex(r'g(x) = mx + n', color=GRAY).scale(0.9).next_to(t3[1][1:10], DOWN, buff=0.4, aligned_edge=LEFT)
        t12 = MathTex(r'f(a) = xa + y', color=GRAY).scale(0.9).next_to(t11, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(FadeIn(t11))
        #self.wait(0.5)
        self.play(FadeIn(t12))
        #self.wait(0.5)
        self.play(FadeOut(t11, t12))
        self.wait(2)



        # A função tem duas partes: uma fixa e uma variável
        b_box = SurroundingRectangle(t3[1][9], buff=0.1, stroke_width=0, color = RED).set_opacity(0.5).set_z_index(-1)
        ax_box = SurroundingRectangle(t3[1][6:8], buff=0.1, stroke_width=0, color = BLUE).set_opacity(0.5).set_z_index(-1)
        self.play(t3[0][0].animate.set_color(WHITE),
                  t3[1][1].animate.set_color(WHITE),
                  t3[1][3].animate.set_color(WHITE),
                  t3[1][7].animate.set_color(WHITE),
                  t3[1][6].animate.set_color(WHITE),
                  t3[1][9].animate.set_color(WHITE))
        self.play(DrawBorderThenFill(ax_box))
        self.wait(2)
        self.play(DrawBorderThenFill(b_box))
        self.wait(2)



        # Exemplo do preço da corrida de táxi
        t13 = Tex(r'Preço$(x) = 5 + 3x$').scale(0.9).next_to(t3, DOWN, buff=1)
        t13_box_1 = SurroundingRectangle(t13[0][10], buff=0.1, stroke_width=0, color = RED).set_opacity(0.5).set_z_index(-1)
        t13_box_2 = SurroundingRectangle(t13[0][12:14], buff=0.1, stroke_width=0, color = BLUE).set_opacity(0.5).set_z_index(-1)
        t14_1 = MathTex('x =', color=GRAY).scale(0.8).next_to(t13, DOWN, buff=0.8).shift(RIGHT*2.5)
        t14_2 = Tex(r'distância \\ percorrida', color=GRAY).scale(0.8).next_to(t14_1, RIGHT, buff=0.1)
        t14_line = Arrow(t14_1[0][0], t13[0][13], buff=0.15, color=GRAY)#.shift(DOWN*0.1)
        self.play(Write(t13[0][0:10]))
        self.wait(2)
        self.play(FadeIn(t13[0][10], t13_box_1))
        self.play(FadeOut(t13_box_1))
        self.wait(2)
        self.play(FadeIn(t13[0][11:14], t13_box_2))
        self.play(FadeOut(t13_box_2))
        self.wait(2)
        self.play(FadeIn(t14_line, t14_1, t14_2))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)



# Exemplo de função
class vid2(Scene):
    def construct(self):

        # Exemplo de função afim e tabela de valores x / f(x)
        t15 = MathTex('f(x) = 3x - 2', color=BLUE).scale(0.9).to_edge(UP, buff=1.2).set_z_index(3)
        t15[0][2].set_color(RED)
        t15[0][6].set_color(RED)
        self.play(FadeIn(t15))

            # Tabela
        v_line = Line(UP, DOWN, stroke_width = 2).scale(2.5).shift(DOWN*0.3)
        h_line_1 = Line(LEFT, RIGHT, stroke_width = 2).scale(2)
        h_line_2 = h_line_1.copy()
        h_line_3 = h_line_1.copy()
        h_line_4 = h_line_1.copy()
        h_line_5 = h_line_1.copy()
        h_lines = VGroup(h_line_1, h_line_2, h_line_3, h_line_4, h_line_5).arrange(DOWN, buff = 1).shift(DOWN*0.8)
        
        x_table = MathTex('x', color = RED).scale(1.2).next_to(v_line, LEFT, buff = 0.9).shift(UP*2)
        fx_table = MathTex('f(x)', color = BLUE).scale(1.1).next_to(v_line, RIGHT, buff = 0.5).shift(UP*2)

        x_value_1 = MathTex('1').scale(1).next_to(v_line, LEFT, buff = 0.9).shift(UP*1)
        x_value_2 = MathTex('2').scale(1).next_to(x_value_1, DOWN, buff=0.65)
        x_value_3 = MathTex(r'3').scale(1).next_to(x_value_2, DOWN, buff=0.65)
        x_value_4 = MathTex(r'4').scale(1).next_to(x_value_3, DOWN, buff=0.65)
        x_values = VGroup(x_value_1, x_value_2, x_value_3, x_value_4)

        fx_value_1 = MathTex('1').scale(1).next_to(v_line, RIGHT, buff = 0.9).shift(UP*1)
        fx_value_2 = MathTex('4').scale(1).next_to(fx_value_1, DOWN, buff=0.65)
        fx_value_3 = MathTex(r'7').scale(1).next_to(fx_value_2, DOWN, buff=0.65)
        fx_value_4 = MathTex(r'10').scale(1).next_to(fx_value_3, DOWN, buff=0.65)
        fx_values = VGroup(fx_value_1, fx_value_2, fx_value_3, fx_value_4)

        g_table = VGroup(v_line, h_lines, x_table, fx_table, x_values, fx_values).scale(0.8).shift(DOWN*0.4)

            # Criando tabela
        self.play(LaggedStart(
            Create(v_line),
            Create(h_lines),
            lag_ratio = 0.5))
        self.play(FadeIn(x_table))
        self.play(FadeIn(fx_table))
        self.wait(2)

            # Criando valores x / fx
        t16 = MathTex('f(1) = 3 \cdot 1 - 2 ',' = 1', color=BLUE).scale(0.9).move_to(t15, aligned_edge=LEFT)
        t16[0][2].set_color(RED)
        t16[0][7].set_color(RED)
        t16[1][0:2].set_color(WHITE)
        self.play(FadeIn(x_value_1),
                  TransformMatchingShapes(t15, t16[0]))
        self.wait(2)
        self.play(FadeIn(t16[1]))
        self.play(FadeOut(t16[1][0]),
                  ReplacementTransform(t16[1][1], fx_value_1))
        self.wait(2)

        t17 = MathTex('f(2) = 3 \cdot 2 - 2 ',' = 4', color=BLUE).scale(0.9).move_to(t15, aligned_edge=LEFT)
        t17[0][2].set_color(RED)
        t17[0][7].set_color(RED)
        t17[1][0:2].set_color(WHITE)
        self.play(FadeIn(x_value_2),
                  TransformMatchingShapes(t16[0][2], t17[0][2]),
                  TransformMatchingShapes(t16[0][7], t17[0][7]))
        self.wait(2)
        self.play(FadeIn(t17[1]))
        self.play(FadeOut(t17[1][0]),
                  ReplacementTransform(t17[1][1], fx_value_2))
        self.wait(2)

        t18 = MathTex('f(3) = 3 \cdot 3 - 2 ',' = 7', color=BLUE).scale(0.9).move_to(t15, aligned_edge=LEFT)
        t18[0][2].set_color(RED)
        t18[0][7].set_color(RED)
        t18[1][0:2].set_color(WHITE)
        self.play(FadeIn(x_value_3),
                  TransformMatchingShapes(t17[0][2], t18[0][2]),
                  TransformMatchingShapes(t17[0][7], t18[0][7]))
        self.wait(2)
        self.play(FadeIn(t18[1]))
        self.play(FadeOut(t18[1][0]),
                  ReplacementTransform(t18[1][1], fx_value_3))
        self.wait(2)

        t19 = MathTex('f(4) = 3 \cdot 4 - 2 ',' = 10', color=BLUE).scale(0.9).move_to(t15, aligned_edge=LEFT)
        t19[0][2].set_color(RED)
        t19[0][7].set_color(RED)
        t19[1][0:3].set_color(WHITE)
        self.play(FadeIn(x_value_4),
                  TransformMatchingShapes(t18[0][2], t19[0][2]),
                  TransformMatchingShapes(t18[0][7], t19[0][7]))
        self.wait(2)
        self.play(FadeIn(t19[1]))
        self.play(FadeOut(t19[1][0]),
                  ReplacementTransform(t19[1][1:3], fx_value_4))
        self.wait(2)


        
        black_rec = SurroundingRectangle(t18, color=BLACK, fill_opacity=1).set_z_index(2).shift(UP*3.5)
        self.play(FadeIn(black_rec))
        self.play(FadeIn(t15))
        self.wait(2)



# A função tem variação constante
class vid3(Scene):
    def construct(self):

        # Retomando elementos
            # Função
        t15 = MathTex('f(x) = 3x - 2', color=WHITE).scale(0.9).to_edge(UP, buff=1.2).set_z_index(3)
        t15[0][2].set_color(RED)
        t15[0][6].set_color(RED)

        t16 = MathTex('f(x) = ',' 3x ',' - 2').scale(0.9).to_edge(UP, buff=1.2).set_z_index(3)

            # Tabela
        v_line = Line(UP, DOWN, stroke_width = 2).scale(2.5).shift(DOWN*0.3)
        h_line_1 = Line(LEFT, RIGHT, stroke_width = 2).scale(2)
        h_line_2 = h_line_1.copy()
        h_line_3 = h_line_1.copy()
        h_line_4 = h_line_1.copy()
        h_line_5 = h_line_1.copy()
        h_lines = VGroup(h_line_1, h_line_2, h_line_3, h_line_4, h_line_5).arrange(DOWN, buff = 1).shift(DOWN*0.8)
        
        x_table = MathTex('x', color = RED).scale(1.2).next_to(v_line, LEFT, buff = 0.9).shift(UP*2)
        fx_table = MathTex('f(x)', color = BLUE).scale(1.1).next_to(v_line, RIGHT, buff = 0.5).shift(UP*2)

        x_value_1 = MathTex('1').scale(1).next_to(v_line, LEFT, buff = 0.9).shift(UP*1)
        x_value_2 = MathTex('2').scale(1).next_to(x_value_1, DOWN, buff=0.65)
        x_value_3 = MathTex(r'3').scale(1).next_to(x_value_2, DOWN, buff=0.65)
        x_value_4 = MathTex(r'4').scale(1).next_to(x_value_3, DOWN, buff=0.65)
        x_values = VGroup(x_value_1, x_value_2, x_value_3, x_value_4)

        fx_value_1 = MathTex('1').scale(1).next_to(v_line, RIGHT, buff = 0.9).shift(UP*1)
        fx_value_2 = MathTex('4').scale(1).next_to(fx_value_1, DOWN, buff=0.65)
        fx_value_3 = MathTex(r'7').scale(1).next_to(fx_value_2, DOWN, buff=0.65)
        fx_value_4 = MathTex(r'10').scale(1).next_to(fx_value_3, DOWN, buff=0.65)
        fx_values = VGroup(fx_value_1, fx_value_2, fx_value_3, fx_value_4)

        g_table = VGroup(v_line, h_lines, x_table, fx_table, x_values, fx_values).scale(0.8).shift(DOWN*0.4)

        self.add(t15, g_table)
        self.wait(2)



        # Setas nos valores de x
        x_arrow_1 = CurvedArrow(UP*0.7, DOWN*0.5, radius=0.7).scale(0.5).next_to(h_line_2, LEFT, buff=0.1).shift(UP*0.1)
        x_arrow_2 = CurvedArrow(UP*0.7, DOWN*0.5, radius=0.7).scale(0.5).next_to(h_line_3, LEFT, buff=0.1)
        x_arrow_3 = CurvedArrow(UP*0.7, DOWN*0.5, radius=0.7).scale(0.5).next_to(h_line_4, LEFT, buff=0.1).shift(DOWN*0.1)
        x_arrows = VGroup(x_arrow_1, x_arrow_2, x_arrow_3).set_color(GRAY)

        x_arrow_1_label = MathTex('+1').scale(0.8).next_to(x_arrow_1, LEFT, buff=0.15)
        x_arrow_2_label = MathTex('+1').scale(0.8).next_to(x_arrow_2, LEFT, buff=0.15)
        x_arrow_3_label = MathTex('+1').scale(0.8).next_to(x_arrow_3, LEFT, buff=0.15)
        x_arrows_labels = VGroup(x_arrow_1_label, x_arrow_2_label, x_arrow_3_label).set_color(GRAY)


        fx_arrow_1 = CurvedArrow(UP*0.7, DOWN*0.5, radius=-0.7).scale(0.5).next_to(h_line_2, RIGHT, buff=0.1).shift(UP*0.1)
        fx_arrow_2 = CurvedArrow(UP*0.7, DOWN*0.5, radius=-0.7).scale(0.5).next_to(h_line_3, RIGHT, buff=0.1)
        fx_arrow_3 = CurvedArrow(UP*0.7, DOWN*0.5, radius=-0.7).scale(0.5).next_to(h_line_4, RIGHT, buff=0.1).shift(DOWN*0.1)
        fx_arrows = VGroup(fx_arrow_1, fx_arrow_2, fx_arrow_3).set_color(GRAY)

        fx_arrow_1_label = MathTex('+3').scale(0.8).next_to(fx_arrow_1, RIGHT, buff=0.15)
        fx_arrow_2_label = MathTex('+3').scale(0.8).next_to(fx_arrow_2, RIGHT, buff=0.15)
        fx_arrow_3_label = MathTex('+3').scale(0.8).next_to(fx_arrow_3, RIGHT, buff=0.15)
        fx_arrows_labels = VGroup(fx_arrow_1_label, fx_arrow_2_label, fx_arrow_3_label).set_color(GRAY)


        self.play(FadeIn(x_arrow_1), FadeIn(x_arrow_1_label))
        self.play(FadeIn(x_arrow_2), FadeIn(x_arrow_2_label))
        self.play(FadeIn(x_arrow_3), FadeIn(x_arrow_3_label))
        self.wait(2)

        self.play(FadeIn(fx_arrow_1), FadeIn(fx_arrow_1_label))
        self.play(FadeIn(fx_arrow_2), FadeIn(fx_arrow_2_label))
        self.play(FadeIn(fx_arrow_3), FadeIn(fx_arrow_3_label))
        self.wait(2)



        # Destaque na parte variável da função
        self.play(TransformMatchingShapes(t15, t16))
        sr_1 = SurroundingRectangle(t16[1], buff=0.1, stroke_width=0, color = RED).set_opacity(0.5).set_z_index(-1)
        self.play(FadeIn(sr_1))
        self.wait(2)
        self.play(FadeOut(sr_1))
        self.wait(2)



        # Setas para variação de 2 e 3 unidades
        x_arrow_4 = CurvedArrow(UP*1, DOWN*2.3, radius=2).scale(0.5).next_to(h_line_2, LEFT, buff=0.1).shift(DOWN*0.4)
        x_arrow_5 = CurvedArrow(UP*1, DOWN*4, radius=3).scale(0.5).next_to(h_line_3, LEFT, buff=0.1)
        x_arrows_2 = VGroup(x_arrow_4, x_arrow_5).set_color(GRAY)

        x_arrow_4_label = MathTex('+2').scale(0.8).next_to(x_arrow_4, LEFT, buff=0.15)
        x_arrow_5_label = MathTex('+3').scale(0.8).next_to(x_arrow_5, LEFT, buff=0.15)
        x_arrows_labels_2 = VGroup(x_arrow_4_label, x_arrow_5_label).set_color(GRAY)


        fx_arrow_4 = CurvedArrow(UP*1, DOWN*2.3, radius=-2).scale(0.5).next_to(h_line_2, RIGHT, buff=0.1).shift(DOWN*0.4)
        fx_arrow_5 = CurvedArrow(UP*1, DOWN*4, radius=-3).scale(0.5).next_to(h_line_3, RIGHT, buff=0.1)
        fx_arrows_2 = VGroup(fx_arrow_4, fx_arrow_5).set_color(GRAY)

        fx_arrow_4_label = MathTex('+6').scale(0.8).next_to(fx_arrow_4, RIGHT, buff=0.15)
        fx_arrow_5_label = MathTex('+9').scale(0.8).next_to(fx_arrow_5, RIGHT, buff=0.15)
        fx_arrows_labels_2 = VGroup(fx_arrow_4_label, fx_arrow_5_label).set_color(GRAY)


        self.play(FadeOut(x_arrow_2, x_arrow_3, 
                          x_arrow_2_label, x_arrow_3_label,
                          fx_arrow_2, fx_arrow_3, 
                          fx_arrow_2_label, fx_arrow_3_label))
        self.wait(2)
        self.play(ReplacementTransform(x_arrow_1, x_arrow_4),
                  FadeOut(x_arrow_1_label),
                  FadeIn(x_arrow_4_label)) # Aumento de 2 unidades
        self.wait(2)
        self.play(ReplacementTransform(fx_arrow_1, fx_arrow_4),
                  FadeOut(fx_arrow_1_label),
                  FadeIn(fx_arrow_4_label)) 
        self.wait(2)


        self.play(ReplacementTransform(x_arrow_4, x_arrow_5),
                  FadeOut(x_arrow_4_label),
                  FadeIn(x_arrow_5_label)) # Aumento de 3 unidades
        self.wait(2)
        self.play(ReplacementTransform(fx_arrow_4, fx_arrow_5),
                  FadeOut(fx_arrow_4_label),
                  FadeIn(fx_arrow_5_label))
        self.wait(2)



# Gráfico da função afim
class vid4(MovingCameraScene):
    def construct(self):

        t1 = MathTex('f(x)',' = 3x ',' - 2').scale(0.9).to_edge(UP, buff=1.2)
        t2 = MathTex('y',' = 3x ',' - 2').scale(0.9).move_to(t1, aligned_edge=RIGHT).shift(DOWN)
        black_sq_1 = Square(color=BLACK, fill_opacity=1).scale(2).next_to(t1, UP, buff=0.1).set_z_index(2)
        black_sq_2 = Square(color=BLACK, fill_opacity=1).next_to(t1, DOWN, buff=0.1).set_z_index(2)

        self.add(t1, black_sq_1, black_sq_2)
        self.play(t1[0].animate.shift(UP),
                  t2[0].animate.shift(UP))
        self.wait(2)


        # Gráfico da função
        axes = Axes(x_range = [-0.8, 5, 1],
                    y_range = [-1, 8, 1],
                    x_length = 4.5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        x_label = MathTex("x").next_to(axes.get_x_axis(), DR, buff = 0)
        y_label = MathTex("y").next_to(axes.get_y_axis(), UL, buff = 0).shift(DOWN*0.1)
        axes_labels = VGroup(x_label, y_label).set_color(WHITE).set_opacity(0.6)
        axes_zero = MathTex('0').scale(0.8).next_to(axes.coords_to_point(0,0,0), DL, buff = 0.13).set_opacity(0.6)

        graph = axes.plot(lambda x: 3*x - 2,
                         x_range=[0.33, 3.4], stroke_width = 4).set_color(BLUE).set_z_index(2)
        
        g_graph = VGroup(axes, axes_labels, axes_zero, graph).move_to(ORIGIN).shift(DOWN)

        self.play(FadeIn(axes, axes_labels, axes_zero))
        self.play(Create(graph))
        self.wait(2)



        # Variações em 'x' e em 'y'
        delta_x_1 = DashedLine(axes.coords_to_point(1,1,0), axes.coords_to_point(2,1,0), color=RED)
        delta_y_1 = DashedLine(axes.coords_to_point(2,0.97,0), axes.coords_to_point(2,4,0), color=PURPLE).set_z_index(4)

        delta_x_2 = DashedLine(axes.coords_to_point(1,1,0), axes.coords_to_point(3,1,0), color=RED)
        delta_y_2 = DashedLine(axes.coords_to_point(3,0.97,0), axes.coords_to_point(3,7,0), color=PURPLE).set_z_index(4)

        g_deltas = VGroup(delta_x_1, delta_y_1,
                          delta_x_2, delta_y_2)



        # Labels 'delta x' e 'delta y'
        delta_x_1_label = MathTex(r'\Delta x', color=RED).scale(0.6).next_to(delta_x_1, DOWN, buff=0.1)    
        delta_y_1_label = MathTex(r'\Delta y', color=PURPLE).scale(0.6).next_to(delta_y_1, RIGHT, buff=0.1)

        delta_x_2_label = MathTex(r'\Delta x', color=RED).scale(0.6).next_to(delta_x_2, DOWN, buff=0.1)
        delta_y_2_label = MathTex(r'\Delta y', color=PURPLE).scale(0.6).next_to(delta_y_2, RIGHT, buff=0.1)

        g_deltas_labels = VGroup(delta_x_1_label, delta_y_1_label,
                                 delta_x_2_label, delta_y_2_label)



        # Labels 'Delta x' e 'delta y' com valores
        delta_x_1_label_1 = MathTex(r'1', color=RED).scale(0.7).next_to(delta_x_1, DOWN, buff=0.1)    
        delta_y_1_label_1 = MathTex(r'3', color=PURPLE).scale(0.7).next_to(delta_y_1, RIGHT, buff=0.1)

        delta_x_2_label_1 = MathTex(r'2', color=RED).scale(0.7).next_to(delta_x_2, DOWN, buff=0.1)
        delta_y_2_label_1 = MathTex(r'6', color=PURPLE).scale(0.7).next_to(delta_y_2, RIGHT, buff=0.1)

        g_deltas_labels_1 = VGroup(delta_x_1_label_1, delta_y_1_label_1,
                                 delta_x_2_label_1, delta_y_2_label_1)

        


        self.play(LaggedStart(Create(delta_x_1)))
        self.wait(2)
        self.play(FadeIn(delta_x_1_label))
        self.wait(2)
        self.play(LaggedStart(Create(delta_y_1)))
        self.play(FadeIn(delta_y_1_label))
        self.wait(2)



        # 'Delta x' e 'delta y' são proporcionais
        t3 = MathTex(r'\Delta y ',' = 3 \cdot ',r' \Delta x').next_to(g_graph, RIGHT)
        t3[0].set_color(PURPLE)
        t3[2].set_color(RED)

        self.play(Indicate(t1[1][1]))
        self.wait(2)
        self.play(TransformMatchingShapes(delta_y_1_label.copy(), t3[0]))
        self.wait(2)
        self.play(FadeIn(t3[1][0]),
                  TransformMatchingShapes(t1[1][1].copy(), t3[1][1]))
        self.wait(2)
        self.play(FadeIn(t3[1][2]),
                  TransformMatchingShapes(delta_x_1_label.copy(), t3[2]))
        self.wait(2)



        # Colocando valores nos 'delta x' e 'delta y'
        t4 = MathTex(r'3 ',' = 3 \cdot ',r' 1').move_to(t3)
        t4[0].set_color(PURPLE)
        t4[2].set_color(RED)

        self.play(ReplacementTransform(t3[2], t4[2]),
                  ReplacementTransform(delta_x_1_label, delta_x_1_label_1))
        self.wait(2)
        self.play(ReplacementTransform(t3[0], t4[0]),
                  ReplacementTransform(delta_y_1_label, delta_y_1_label_1))
        self.wait(2)


        t5 = MathTex(r'6 ',' = 3 \cdot ',r' 2').move_to(t3)
        t5[0].set_color(PURPLE)
        t5[2].set_color(RED)

        self.play(ReplacementTransform(t4[2], t5[2]),
                  ReplacementTransform(delta_x_1_label_1, delta_x_2_label_1),
                  FadeOut(delta_y_1_label_1),
                  ReplacementTransform(delta_x_1, delta_x_2),
                  ReplacementTransform(delta_y_1, delta_y_2))
        self.wait(2)
        self.play(ReplacementTransform(t4[0], t5[0]),
                  FadeIn(delta_y_2_label_1))
        self.wait(2)


        
        # Nome do coeficiente 'taxa de variação' ou 'velocidade'
        t6 = Tex('\it ``Taxa de variação"', color=GRAY).scale(0.8).next_to(t1, DOWN).shift(RIGHT*2.7+DOWN*0.3).set_z_index(3)
        arrow_1 = Arrow(t6, t1[1][1].get_edge_center(DOWN), buff=0.2, color=GRAY).scale(1.1).set_z_index(3)
        self.play(Indicate(t1[1][1]))
        self.wait(2)
        self.play(FadeIn(t6, arrow_1))
        self.wait(2)



        # Usando a forma geral da função e coeficiente 'a' 
        black_sq_3 = SurroundingRectangle(t1, color=BLACK, fill_opacity=1).scale(2).set_z_index(2)
        t8 = MathTex('y',' = ax ',' + b').scale(0.9).move_to(t1, aligned_edge=RIGHT).shift(DOWN*0.55).set_z_index(3)
        self.play(FadeIn(black_sq_3))
        self.play(FadeIn(t8))
        self.wait(2)
        self.play(Indicate(t8[1][1]))
        self.wait(2)
        self.play(FadeOut(t6, arrow_1))
        self.wait(2)


        t3_2 = MathTex(r'\Delta y ',' = a \cdot ',r' \Delta x').next_to(g_graph, RIGHT)
        t3_2[0].set_color(PURPLE)
        t3_2[2].set_color(RED)

        self.play(ReplacementTransform(t5[0], t3_2[0]),
                  ReplacementTransform(t3[1], t3_2[1]),
                  ReplacementTransform(t5[2], t3_2[2]),
                  ReplacementTransform(delta_x_2_label_1, delta_x_2_label),
                  ReplacementTransform(delta_y_2_label_1, delta_y_2_label))
        self.wait(2)



        t9 = MathTex(r'\Delta y ',' = a \cdot ',r' \Delta x').next_to(g_graph, RIGHT)
        t9[0].set_color(PURPLE)
        t9[2].set_color(RED)
        self.remove(t3_2[0], t3_2[1], t3_2[2]).add(t9)

        t10 = MathTex(r'\frac{\Delta y}{\Delta x}',' = a').move_to(t9, aligned_edge=LEFT)
        t10[0][0:2].set_color(PURPLE)
        t10[0][3:5].set_color(RED)

        triangle_1 = Polygon(axes.coords_to_point(1,1,0),
                             axes.coords_to_point(3,7,0),
                             axes.coords_to_point(3,1,0),
                             color=YELLOW, stroke_opacity=1, fill_opacity=0.2).set_z_index(3)
        angle_1 = Polygon(axes.coords_to_point(3,1,0), axes.coords_to_point(2.7,1,0),
                          axes.coords_to_point(2.7,1.5,0), axes.coords_to_point(3,1.5,0)).set_z_index(-2)
        
        self.play(ReplacementTransform(t9[2], t10[0][3:5]),
                  ReplacementTransform(t9[0], t10[0][0:2]),
                  FadeIn(t10[0][2]),
                  FadeOut(t9[1][2]),
                  t9[1][0:2].animate.shift(RIGHT*0.1))
        self.wait(2)
        self.play(DrawBorderThenFill(triangle_1),
                  FadeIn(angle_1))
        self.play(FadeOut(triangle_1, angle_1))
        self.wait(2)



        # Cateto oposto/cateto adjacente = tangente do ângulo
        t11 = Tex(r'$=$ tg $\theta$').next_to(t10, RIGHT, buff=0.15)
        angle_2 = Angle(Line(axes.coords_to_point(0,-2,0), axes.coords_to_point(3,7,0)), 
                        Line(axes.coords_to_point(0,1,0), axes.coords_to_point(3,1,0)), 
                        quadrant=(1,1), other_angle=True, radius=0.5).set_z_index(4)
        angle_2_label = always_redraw(lambda : Tex(r'$\theta$').scale(0.8).next_to(angle_2, UR, buff=0).shift(DOWN*0.15+RIGHT*0.05).set_z_index(4))

        self.play(FadeIn(angle_2, angle_2_label))
        self.wait(2)
        self.play(Indicate(delta_y_2_label), Indicate(t10[0][0:2]))
        self.wait(2)
        self.play(Indicate(delta_x_2_label), Indicate(t10[0][3:5]))
        self.wait(2)
        self.play(Write(t11))
        self.wait(2)
        self.play(angle_2.animate.move_to(axes.coords_to_point(0.95,0,0), aligned_edge=DL))
        self.wait(2)



        # Nome 'coeficiente angular'
        t12 = Tex('\it ``Coeficiente angular"', color=GRAY).scale(0.8).next_to(t1, DOWN).shift(RIGHT*2.7+DOWN*0.3).set_z_index(3)
        arrow_2 = Arrow(t12, t1[1][1].get_edge_center(DOWN), buff=0.2, color=GRAY).set_z_index(3).scale(1.1)
        
        self.play(t8[1][1].animate.set_color(YELLOW))
        self.wait(2)
        self.play(FadeIn(t12, arrow_2))
        self.wait(2)
        black_sq_4 = Square(color=BLACK, fill_opacity=1).scale(5).next_to(t1, DOWN, buff=0.1).shift(RIGHT).set_z_index(5)
        self.play(FadeOut(t12, arrow_2), FadeIn(black_sq_4))
        self.wait(2)



        # Mostrando a inclinação do gráfico de acordo com o valor de 'a'
        axes_1 = axes.copy()
        graph_1 = axes.plot(lambda x: 0.5*x,
                         x_range=[-1, 5], stroke_width = 4).set_color(BLUE).set_z_index(2)
        ang_1 = Angle(Line(axes_1.coords_to_point(0,0,0), axes_1.coords_to_point(1,0.5,0)),
                      axes_1.get_x_axis(),
                      other_angle=True, radius=1.3)
        ang_1_label = MathTex(r'\theta').scale(0.8).next_to(ang_1, RIGHT, buff=0.1).shift(UP*0.05)
        g_1 = VGroup(axes_1, graph_1, ang_1, ang_1_label)


        axes_2 = axes.copy()
        graph_2 = axes.plot(lambda x: 3*x - 3,
                         x_range=[0.7, 3.6], stroke_width = 4).set_color(BLUE).set_z_index(2)
        ang_2 = Angle(Line(axes_2.coords_to_point(1,0,0), axes_2.coords_to_point(2,3,0)),
                      axes_2.get_x_axis(),
                      other_angle=True)
        ang_2_label = MathTex(r'\theta').scale(0.8).next_to(ang_2, RIGHT, buff=0).shift(UP*0.15+RIGHT*0.08)
        g_2 = VGroup(axes_2, graph_2, ang_2, ang_2_label)


        axes_3 = axes.copy()
        graph_3 = axes.plot(lambda x: -1.5*x + 4.5,
                         x_range=[-0.7, 3.5], stroke_width = 4).set_color(BLUE).set_z_index(2)
        ang_3 = Angle(Line(axes_3.coords_to_point(3,0,0), axes_3.coords_to_point(2,1.5,0)),
                      axes_3.get_x_axis(),
                      other_angle=True)
        ang_3_label = MathTex(r'\theta').scale(0.8).next_to(ang_3, UP, buff=0.1).shift(RIGHT*0.2)
        g_3 = VGroup(axes_3, graph_3, ang_3, ang_3_label)


        g_0 = VGroup(g_1, g_2, g_3).arrange(RIGHT, buff=1).scale(0.7).shift(DOWN).set_z_index(6)


        box_1 = SurroundingRectangle(g_1, buff=0.3, color=GRAY, stroke_width=2)
        box_2 = SurroundingRectangle(g_2, buff=0.3, color=GRAY, stroke_width=2)
        box_3 = SurroundingRectangle(g_3, buff=0.3, color=GRAY, stroke_width=2)
        boxes = VGroup(box_1, box_2, box_3).set_z_index(6)


        label_1 = MathTex('a = 0.5').scale(0.8).next_to(g_1, UP, buff=0.5)
        label_2 = MathTex('a = 3').scale(0.8).next_to(g_2, UP, buff=0.5)
        label_3 = MathTex('a = -1.5').scale(0.8).next_to(g_3, UP, buff=0.5)
        labels = VGroup(label_1, label_2, label_3).set_color(YELLOW).set_z_index(6)
        

        self.play(FadeIn(g_1, box_1, label_1))
        self.wait(2)
        self.play(FadeIn(g_2, box_2, label_2))
        self.wait(2)
        self.play(FadeIn(g_3, box_3, label_3))
        self.wait(2)



        # Sobre o coeficiente 'b'
        self.play(t8[1][1].animate.set_color(WHITE),
                  FadeOut(g_0, boxes, labels))
        self.wait(2)
        
        t13 = Tex('\it ``Coeficiente linear"', color=GRAY).scale(0.8).next_to(t1, DOWN).shift(RIGHT*3.7+DOWN*0.3).set_z_index(6)
        arrow_3 = Arrow(t13, t1[2][1], buff=0.2, color=GRAY).set_z_index(6).scale(1.1)
        self.play(t8[2][1].animate.set_color(YELLOW))
        self.wait(2)
        self.play(FadeIn(t13, arrow_3))
        self.wait(2)
        self.play(FadeOut(t13, arrow_3))
        self.wait(2)
        
        t14 = MathTex('y',' = a0 ',' + b').scale(0.9).move_to(t8).set_z_index(3)
        redline_1 = Line(DOWN*0.5, UP*0.5, color=RED).rotate(-60*DEGREES).move_to(t14[1][1:3]).scale(0.8).set_z_index(7)
        self.play(TransformMatchingShapes(t8[1][2], t14[1][2]))
        self.wait(2)
        self.play(Create(redline_1))
        self.wait(2)



        # 'b' é o valor em que o gráfico cruza o eixo 'y'
        axes = Axes(x_range = [-0.8, 5, 1],
                    y_range = [-1, 8, 1],
                    x_length = 4.5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        x_label = MathTex("x").next_to(axes.get_x_axis(), DR, buff = 0)
        y_label = MathTex("y").next_to(axes.get_y_axis(), UL, buff = 0).shift(DOWN*0.1)
        axes_labels = VGroup(x_label, y_label).set_color(WHITE).set_opacity(0.6)
        axes_zero = MathTex('0').scale(0.8).next_to(axes.coords_to_point(0,0,0), DL, buff = 0.13).set_opacity(0.6)
        b_label = MathTex('b', color=YELLOW).scale(0.9).next_to(axes.coords_to_point(0,2,0), LEFT, buff=0.15).shift(UP*0.15)
        b_tick = Line(LEFT*0.1, RIGHT*0.1, color=YELLOW).move_to(axes.coords_to_point(0,2,0))

        graph = axes.plot(lambda x: x + 2,
                         x_range=[-0.5, 5], stroke_width = 4).set_color(BLUE).set_z_index(2)
        
        g_graph = VGroup(axes, axes_labels, axes_zero, graph, b_label, b_tick).move_to(ORIGIN).shift(DOWN).set_z_index(6)

        self.play(FadeIn(axes, axes_labels, axes_zero))
        self.wait(2)
        self.play(Create(graph))
        self.wait(2)
        self.play(FadeIn(b_label, b_tick))
        self.wait(2)



# Caso especial: função linear e função identidade
class vid5(Scene):
    def construct(self):

        t0 = MathTex('f(x)',' = 3x ',' - 2').scale(0.9).to_edge(UP, buff=1.2) # Referência para t1
        t1 = MathTex('y',' = ax ',' + b').scale(0.9).move_to(t0, aligned_edge=RIGHT)
        t2 = MathTex('y',' = ax ',' + 0').scale(0.9).move_to(t1, aligned_edge=LEFT)
        t6 = Tex('\it ``Função linear"', color=GRAY).scale(0.8).next_to(t2[0:2], UP, buff=0.3)
        self.add(t1)
        self.wait(2)
        self.play(TransformMatchingShapes(t1,t2))
        self.wait(2)
        self.play(FadeOut(t2[2]))
        self.wait(2)
        self.play(FadeIn(t6))
        self.wait(2)


        
        axes = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 5, 1],
                    x_length = 4.5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        x_label = MathTex("x").next_to(axes.get_x_axis(), DR, buff = 0)
        y_label = MathTex("y").next_to(axes.get_y_axis(), UL, buff = 0).shift(DOWN*0.1)
        axes_labels = VGroup(x_label, y_label).set_color(WHITE).set_opacity(0.6)
        axes_zero = MathTex('0').scale(0.8).next_to(axes.coords_to_point(0,0,0), DL, buff = 0.13).set_opacity(0.6)
        
        graph_1 = axes.plot(lambda x: 0.5*x,
                         x_range=[-1, 5], stroke_width = 4).set_color(BLUE)
        graph_2 = axes.plot(lambda x: x,
                         x_range=[-1, 5], stroke_width = 6).set_color(BLUE)
        
        g_graph = VGroup(axes, axes_labels, axes_zero, graph_1, graph_2).move_to(ORIGIN).shift(DOWN)

        self.play(FadeIn(axes, axes_labels, axes_zero))
        self.play(Create(graph_1))
        self.wait(2)



        dot_origin = Dot(axes.coords_to_point(0,0,0), color=YELLOW)
        dot_origin_label = MathTex('(0,0)', color=YELLOW).scale(0.7).next_to(dot_origin, UL, buff=0.1)
        self.play(GrowFromCenter(dot_origin))
        self.play(FadeIn(dot_origin_label))
        self.wait(2)
        self.play(FadeOut(dot_origin, dot_origin_label, graph_1, t6))
        self.wait(2)


        # Função identidade
        t3 = MathTex('y',' = 1x ',' + 0').scale(0.9).move_to(t1, aligned_edge=LEFT)
        t4 = MathTex('y',' = x ',' + 0').scale(0.9).move_to(t1, aligned_edge=LEFT)
        t7 = Tex('\it ``Função identidade"', color=GRAY).scale(0.8).next_to(t4[0:2], UP, buff=0.3)
        self.play(FadeIn(t7))
        self.wait(2)
        self.play(TransformMatchingShapes(t2[1], t3[1]))
        self.wait(2)
        self.play(ReplacementTransform(t3[1], t4[1]))
        self.wait(2)

        t5 = MathTex(r'x \longmapsto x', color=YELLOW).scale(0.9).next_to(t4[0:2], DOWN, buff=0.4)
        self.play(FadeIn(t5[0][0]))
        self.play(GrowFromEdge(t5[0][1:4], LEFT))
        self.play(FadeIn(t5[0][4]))
        self.wait(2)



            # Pontos do gráfico da função identidade
        dot_1 = Dot(axes.coords_to_point(1,1,0))
        dot_2 = Dot(axes.coords_to_point(2,2,0))
        dot_3 = Dot(axes.coords_to_point(3,3,0))
        dot_4 = Dot(axes.coords_to_point(4,4,0))
        g_dots = VGroup(dot_1, dot_2, dot_3, dot_4).set_color(BLUE)



            # Linhas das coordenadas dos pontos
        dot_1_x_line = DashedLine(axes.coords_to_point(1,1,0), axes.coords_to_point(1,0,0))
        dot_1_y_line = DashedLine(axes.coords_to_point(1,1,0), axes.coords_to_point(0,1,0))
        
        dot_2_x_line = DashedLine(axes.coords_to_point(2,2,0), axes.coords_to_point(2,0,0))
        dot_2_y_line = DashedLine(axes.coords_to_point(2,2,0), axes.coords_to_point(0,2,0))
        
        dot_3_x_line = DashedLine(axes.coords_to_point(3,3,0), axes.coords_to_point(3,0,0))
        dot_3_y_line = DashedLine(axes.coords_to_point(3,3,0), axes.coords_to_point(0,3,0))
        
        dot_4_x_line = DashedLine(axes.coords_to_point(4,4,0), axes.coords_to_point(4,0,0))
        dot_4_y_line = DashedLine(axes.coords_to_point(4,4,0), axes.coords_to_point(0,4,0))
        
        g_x_y_lines = VGroup(dot_1_x_line, dot_1_y_line,
                             dot_2_x_line, dot_2_y_line,
                             dot_3_x_line, dot_3_y_line,
                             dot_4_x_line, dot_4_y_line).set_color(GRAY)
            


            # Labels das coordenadas dos pontos
        dot_1_x_label = MathTex('1').scale(0.8).next_to(axes.coords_to_point(1,0,0), DOWN, buff=0.1)
        dot_1_y_label = MathTex('1').scale(0.8).next_to(axes.coords_to_point(0,1,0), LEFT, buff=0.1)

        dot_2_x_label = MathTex('2').scale(0.8).next_to(axes.coords_to_point(2,0,0), DOWN, buff=0.1)
        dot_2_y_label = MathTex('2').scale(0.8).next_to(axes.coords_to_point(0,2,0), LEFT, buff=0.1)

        dot_3_x_label = MathTex('3').scale(0.8).next_to(axes.coords_to_point(3,0,0), DOWN, buff=0.1)
        dot_3_y_label = MathTex('3').scale(0.8).next_to(axes.coords_to_point(0,3,0), LEFT, buff=0.1)

        dot_4_x_label = MathTex('4').scale(0.8).next_to(axes.coords_to_point(4,0,0), DOWN, buff=0.1)
        dot_4_y_label = MathTex('4').scale(0.8).next_to(axes.coords_to_point(0,4,0), LEFT, buff=0.1)

        g_x_y_labels = VGroup(dot_1_x_label, dot_1_y_label,
                              dot_2_x_label, dot_2_y_label,
                              dot_3_x_label, dot_3_y_label,
                              dot_4_x_label, dot_4_y_label).set_opacity(0.6)



        # Aparecem alguns pontos do gráfico
        self.play(GrowFromCenter(dot_1),
                  FadeIn(dot_1_x_line, dot_1_y_line,
                         dot_1_x_label, dot_1_y_label))
        self.wait(2)
        self.play(GrowFromCenter(dot_2),
                  FadeIn(dot_2_x_line, dot_2_y_line,
                         dot_2_x_label, dot_2_y_label))
        self.wait(2)
        self.play((GrowFromCenter(dot_3),
                   FadeIn(dot_3_x_line, dot_3_y_line,
                         dot_3_x_label, dot_3_y_label)))
        self.play((GrowFromCenter(dot_4),
                   FadeIn(dot_4_x_line, dot_4_y_line,
                         dot_4_x_label, dot_4_y_label)))
        self.wait(2)        



        # Os pontos se transformam no gráfico completo
        self.play(FadeOut(g_dots), FadeIn(graph_2))
        self.wait(2)



        # O gráfico divide o 1o quadrante ao meio
        square_1 = Polygon(axes.coords_to_point(0,0,0),
                           axes.coords_to_point(0,5,0),
                           axes.coords_to_point(5,5,0),
                           axes.coords_to_point(5,0,0),
                           fill_opacity=0.1, stroke_width=0, color=WHITE)

        triangle_1 = Polygon(axes.coords_to_point(0,0,0),
                             axes.coords_to_point(0,5,0),
                             axes.coords_to_point(5,5,0),
                             fill_opacity=0.2, stroke_width=0, color=YELLOW)
        
        triangle_2 = Polygon(axes.coords_to_point(0,0,0),
                             axes.coords_to_point(5,0,0),
                             axes.coords_to_point(5,5,0),
                             fill_opacity=0.2, stroke_width=0, color=YELLOW)
        
        self.play(FadeIn(square_1))
        self.wait(2)
        self.play(FadeIn(triangle_1))
        self.play(FadeOut(triangle_1), FadeIn(triangle_2))
        self.play(FadeOut(triangle_2))
        self.wait(2)

        black_sq = Square(fill_opacity=1, color=BLACK).scale(5)
        self.play(FadeIn(black_sq))
        self.wait(2)



# Gráfico mudando o valor dos coeficientes
class vid6(Scene):
    def construct(self):

        t1 = MathTex('y',' = ax ',' + b').scale(0.9).to_edge(UP, buff=1.2)
        t1[1][1].set_color(BLUE)
        t1[2][1].set_color(RED)
        t1[0:2].shift(RIGHT*0.4)



        # ValueTrackers dos coeficientes 'a' e 'b'
        a = ValueTracker(1)
        b = ValueTracker(0)



        # Mostrador do valor de 'a'
        a_label = MathTex('a', color=t1[1][1].get_color())
        a_numberline = NumberLine(x_range=[-5,5], length=2, tick_size=0,
                                  stroke_width=5, color=GRAY).rotate(90*DEGREES).next_to(a_label, DOWN, buff=0.2)
        a_numberline_dot = always_redraw(lambda: Dot(a_numberline.number_to_point(a.get_value()), color=a_label.get_color()))
        a_value_label = always_redraw(lambda: MathTex(f'{a.get_value():.1f}', color=a_label.get_color()).scale(0.7).next_to(a_numberline_dot, LEFT, buff=0.1))

        g_a_display = VGroup(a_label, a_numberline, a_numberline_dot, a_value_label).shift(UP*3+RIGHT*4)



        # Mostrador do valor de 'b'
        b_label = MathTex('b', color=t1[2][1].get_color())
        b_numberline = NumberLine(x_range=[-5,5], length=2, tick_size=0,
                                  stroke_width=5, color=GRAY).rotate(90*DEGREES).next_to(b_label, DOWN, buff=0.2)
        b_numberline_dot = always_redraw(lambda: Dot(b_numberline.number_to_point(b.get_value()), color=b_label.get_color()))
        b_value_label = always_redraw(lambda: MathTex(f'{b.get_value():.1f}', color=b_label.get_color()).scale(0.7).next_to(b_numberline_dot, RIGHT, buff=0.1))
        
        g_b_display = VGroup(b_label, b_numberline, b_numberline_dot, b_value_label).shift(UP*3+RIGHT*5)



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

        plane = NumberPlane(x_range = [-4, 4, 1], 
                              y_range = [-4, 4, 1], 
                              x_length = 9, 
                              y_length = 9, 
                              color=GRAY).set_opacity(0.3).scale(0.5).set_z_index(-1).move_to(axes)
         
        graph_1 = always_redraw(lambda: axes.plot(lambda x: (a.get_value())*x + 1.25*(b.get_value()),
                         x_range=[-5,5], stroke_width = 6).set_color(GREEN).set_z_index(-2))
        graph_1_aux_1 = always_redraw(lambda: axes.plot(lambda x: (a.get_value())*x + 1.25*(b.get_value()),
                         x_range=[-1.5,1.5], stroke_width = 6).set_color(GREEN).set_z_index(1))
        graph_1_aux_2 = always_redraw(lambda: axes.plot(lambda x: (a.get_value())*x + 1.25*(b.get_value()),
                         x_range=[-4.4,4.4], stroke_width = 6).set_color(GREEN).set_z_index(1))
        graph_1_aux_3 = always_redraw(lambda: axes.plot(lambda x: (a.get_value())*x + 1.25*(b.get_value()),
                         x_range=[-3.5,3.5], stroke_width = 6).set_color(GREEN).set_z_index(1))
        


        # Borda para o gráfico não escapar dos eixos
        external_border = Square(fill_opacity=1, color=YELLOW).scale(10)
        internal_border = always_redraw(lambda: Circle(radius=2.25, fill_opacity=1, color=BLUE))
        border = always_redraw(lambda: Difference(external_border, internal_border, fill_opacity=1, color=BLACK).set_z_index(-1).move_to(axes.coords_to_point(0,b.get_value(),0)))



        # Animação
        self.play(FadeIn(axes, axes_labels, axes_zero))
        self.add(border)
        self.wait(2)
        self.play(Create(graph_1),
                  Create(graph_1_aux_3),
                  run_time=1.5)
        self.add(graph_1_aux_1).remove(graph_1_aux_3)
        self.wait(2)
        self.play(FadeIn(t1[0:2], g_a_display))
        self.wait(2)
        '''self.play(a.animate.set_value(3), run_time=3)
        self.wait(2)
        self.play(a.animate.set_value(0.1), run_time=3)
        self.wait(2)
        self.play(a.animate.set_value(-0.5), run_time=2)
        self.wait(2)
        self.play(a.animate.set_value(-2), run_time=2)
        self.wait(2)'''
        self.play(a.animate.set_value(1), run_time=2)
        self.wait(2)



        # Adiciona o coeficiente 'b'
        self.play(t1[0:2].animate.shift(LEFT*0.4),
                  FadeIn(t1[2], g_b_display))
        self.wait(2)
        self.add(graph_1_aux_1)
        '''self.play(b.animate.set_value(2), run_time=2)
        self.wait(2)'''
        self.play(b.animate.set_value(-1), run_time=4)
        self.wait(2)
        self.remove(graph_1_aux_1)



        # Comentário sobre 'a' nunca ser zero, a função é ou crescente ou decrescente
        self.play(a.animate.set_value(0), b.animate.set_value(1), run_time=2)
        self.wait(2)
        redline_1 = Line(UP*0.5, DOWN*0.5, color=RED).rotate(-60*DEGREES).scale(0.8)
        redline_2 = Line(UP*0.5, DOWN*0.5, color=RED).rotate(60*DEGREES).scale(0.8)
        red_x = VGroup(redline_1, redline_2).move_to(a_value_label)
        self.play(Create(red_x))
        self.wait(2)
        self.play(FadeOut(red_x), a.animate.set_value(0.5), run_time=2)
        self.wait(2)
        self.play(a.animate.set_value(-0.5), run_time=3)
        self.wait(2)



        '''# Comentário sobre o gráfico nunca ser vertical
        vertical_graph = Line(axes.coords_to_point(2,-5,0), 
                              axes.coords_to_point(2,5,0),
                              stroke_width=6, color=GREEN)
        right_angle = RightAngle(vertical_graph, axes.get_x_axis(), length=0.2)

        self.remove(graph_1_aux_1)
        self.play(FadeOut(g_a_display, g_b_display, graph_1, graph_1_aux_1))
        self.play(FadeIn(vertical_graph))
        self.wait(2)
        self.play(FadeIn(right_angle))
        self.wait(2)
        self.play(FadeOut(vertical_graph, right_angle))
        self.wait(2)

        # Para ser vertical o coeficiente 'a' deveria ser infinito
        a_aux = ValueTracker(1)
        a_label_aux = MathTex('a', color=t1[1][1].get_color())
        a_numberline_aux = NumberLine(x_range=[0,100], length=2, tick_size=0,
                                  stroke_width=5, color=GRAY).rotate(90*DEGREES).next_to(a_label_aux, DOWN, buff=0.2)
        a_numberline_dot_aux = always_redraw(lambda: Dot(a_numberline_aux.number_to_point(a_aux.get_value()), color=a_label.get_color()))
        a_value_label_aux = always_redraw(lambda: MathTex(f'{a_aux.get_value():.1f}', color=a_label.get_color()).scale(0.7).next_to(a_numberline_dot_aux, LEFT, buff=0.1))
        g_a_display_aux = VGroup(a_label_aux, a_numberline_aux, a_numberline_dot_aux, a_value_label_aux).shift(UP*3+RIGHT*4)

        a.set_value(1)
        b.set_value(0)
        self.play(FadeIn(g_a_display_aux, g_b_display, graph_1))
        self.wait()
        self.play(a.animate.set_value(100), 
                  a_aux.animate.set_value(100), 
                  run_time=5)

        t2 = MathTex(r'\infty').scale(0.7).move_to(a_value_label_aux)
        self.play(FadeOut(a_value_label_aux))
        self.wait(2)
        self.play(FadeIn(t2))
        self.wait(2)

        red_x.scale(0.9).move_to(t2)
        self.play(Create(red_x))
        self.wait()'''



# Mostrando o jeito de pensar nos gráficos de funções afim
class vid7(Scene):
    def construct(self):


        axes = Axes(x_range = [-3, 3, 1],
                    y_range = [-3, 3, 1],
                    x_length = 7,
                    y_length = 7,
                    axis_config = {"include_ticks" : False}).scale(0.7).set_opacity(0.6).move_to(ORIGIN).shift(DOWN)
        
        axes_1 = axes.copy()
        plane_1 = NumberPlane(x_range = [-3, 3, 1], 
                              y_range = [-3, 3, 1], 
                              x_length = 7, 
                              y_length = 7, 
                              color=GRAY).set_opacity(0.3).scale(0.7).move_to(axes_1).set_z_index(-1)
        graph_1 = axes.plot(lambda x: x,
                         x_range=[-2, 2], stroke_width = 4).set_color(BLUE).set_z_index(2)
        slope_1 = DashedVMobject(Polygon(axes_1.coords_to_point(0,0,0),
                                         axes_1.coords_to_point(1,0,0),
                                         axes_1.coords_to_point(1,1,0),
                                         color=YELLOW), num_dashes=18)
        slope_1_x_label = MathTex('1', color=YELLOW).scale(0.9).next_to(slope_1, DOWN, buff=0.2)
        slope_1_y_label = MathTex('1', color=YELLOW).scale(0.9).next_to(slope_1, RIGHT, buff=0.2)
        b_value_label_1 = MathTex(r'1', color=YELLOW).scale(0.8).next_to(axes_1.coords_to_point(0,1,0), LEFT, buff=0.2)
        b_value_tick_1 = Line(LEFT*0.1, RIGHT*0.1, color=YELLOW).move_to(axes_1.coords_to_point(0,1,0))
        g_1 = VGroup(axes_1, plane_1, graph_1, slope_1, slope_1_x_label, slope_1_y_label, b_value_label_1, b_value_tick_1)


        axes_2 = axes.copy()
        plane_2 = NumberPlane(x_range = [-3, 3, 1], 
                              y_range = [-3, 3, 1], 
                              x_length = 7, 
                              y_length = 7, 
                              color=GRAY).set_opacity(0.3).scale(0.7).move_to(axes_2).set_z_index(-1)
        graph_2 = axes.plot(lambda x: 2*x,
                         x_range=[-1, 1.5], stroke_width = 4).set_color(BLUE).set_z_index(2)
        graph_2_2 = axes.plot(lambda x: 2*x - 2,
                         x_range=[-0.5, 1.5], stroke_width = 4).set_color(BLUE).set_z_index(2)
        slope_2 = DashedVMobject(Polygon(axes_2.coords_to_point(0,0,0),
                                         axes_2.coords_to_point(1,0,0),
                                         axes_2.coords_to_point(1,2,0),
                                         color=YELLOW), num_dashes=23)
        slope_2_x_label = MathTex('1', color=YELLOW).scale(0.9).next_to(slope_2, DOWN, buff=0.2)
        slope_2_y_label = MathTex('2', color=YELLOW).scale(0.9).next_to(slope_2, RIGHT, buff=0.2)
        b_value_label_2 = MathTex(r'-2', color=YELLOW).scale(0.8).next_to(axes_2.coords_to_point(0,-2,0), LEFT, buff=0.2)
        b_value_tick_2 = Line(LEFT*0.1, RIGHT*0.1, color=YELLOW).move_to(axes_2.coords_to_point(0,-2,0))
        g_2 = VGroup(axes_2, plane_2, graph_2, graph_2_2, slope_2, slope_2_x_label, slope_2_y_label, b_value_label_2, b_value_tick_2)


        axes_3 = axes.copy()
        plane_3 = NumberPlane(x_range = [-3, 3, 1], 
                              y_range = [-3, 3, 1], 
                              x_length = 7, 
                              y_length = 7, 
                              color=GRAY).set_opacity(0.3).scale(0.7).move_to(axes_3).set_z_index(-1)
        graph_3 = axes.plot(lambda x: -0.5*x,
                         x_range=[-2.5, 2.5], stroke_width = 4).set_color(BLUE).set_z_index(2)
        slope_3 = DashedVMobject(Polygon(axes_3.coords_to_point(0,0,0),
                                         axes_3.coords_to_point(1,0,0),
                                         axes_3.coords_to_point(1,-0.5,0),
                                         color=YELLOW), num_dashes=14)
        slope_3_x_label = MathTex('1', color=YELLOW).scale(0.9).next_to(slope_3, UP, buff=0.2)
        slope_3_y_label = MathTex('0.5', color=YELLOW).scale(0.9).next_to(slope_3, RIGHT, buff=0.2)
        b_value_label_3 = MathTex(r'\sqrt{2}', color=YELLOW).scale(0.8).next_to(axes_3.coords_to_point(0,1.41,0), LEFT, buff=0.2)
        b_value_tick_3 = Line(LEFT*0.1, RIGHT*0.1, color=YELLOW).move_to(axes_3.coords_to_point(0,1.41,0))
        g_3 = VGroup(axes_3, plane_3, graph_3, slope_3, slope_3_x_label, slope_3_y_label, b_value_label_3, b_value_tick_3)


        g_0 = VGroup(g_1, g_2, g_3).arrange(RIGHT, buff=1).scale(0.7)



        box_1 = SurroundingRectangle(axes_1, buff=0.3, color=GRAY, stroke_width=2)
        box_2 = SurroundingRectangle(axes_2, buff=0.3, color=GRAY, stroke_width=2)
        box_3 = SurroundingRectangle(axes_3, buff=0.3, color=GRAY, stroke_width=2)
        boxes = VGroup(box_1, box_2, box_3)



        label_1 = MathTex('y = x + 1').scale(0.8).next_to(g_1, UP, buff=0.5)
        label_2 = MathTex('y = 2x - 2').scale(0.8).next_to(g_2, UP, buff=0.5)
        label_3 = MathTex(r'y = -0.5x + \sqrt{2}').scale(0.8).next_to(g_3, UP, buff=0.5)
        labels = VGroup(label_1, label_2, label_3)



        self.play(LaggedStart(FadeIn(label_1, box_1, axes_1, plane_1),
                              FadeIn(label_2, box_2, axes_2, plane_2),
                              FadeIn(label_3, box_3, axes_3, plane_3),
                              lag_ratio=0.5))
        self.wait(2)
        


        # Observando o coeficiente 'a' e a inclinação
        self.play(label_2[0][2].animate.set_color(YELLOW),
                  label_3[0][2:6].animate.set_color(YELLOW))
        self.wait(2)

        self.play(LaggedStart(FadeIn(slope_1, slope_1_x_label, slope_1_y_label, graph_1),
                              FadeIn(slope_2, slope_2_x_label, slope_2_y_label, graph_2),
                              FadeIn(slope_3, slope_3_x_label, slope_3_y_label, graph_3),
                              lag_ratio=0.5))
        self.wait(2)

        self.play(label_2[0][2].animate.set_color(WHITE),
                  label_3[0][2:6].animate.set_color(WHITE),
                  FadeOut(slope_1_x_label, slope_1_y_label,
                          slope_2_x_label, slope_2_y_label,
                          slope_3_x_label, slope_3_y_label,
                          slope_1, slope_2, slope_3))
        
        

        # Observando o coeficiente 'b' e a translação vertical
        self.play(label_1[0][3:5].animate.set_color(YELLOW),
                  label_2[0][4:6].animate.set_color(YELLOW),
                  label_3[0][7:11].animate.set_color(YELLOW))
        self.wait(2)

        self.play(FadeIn(b_value_label_1, b_value_tick_1),
                  graph_1.animate.shift(UP*0.5717))
        
        self.play(FadeIn(b_value_label_2, b_value_tick_2),
                  ReplacementTransform(graph_2, graph_2_2))
        
        self.play(FadeIn(b_value_label_3, b_value_tick_3), 
                  graph_3.animate.shift(UP*(0.5717*1.41)))
        self.wait(2)

        self.play(label_1[0][3:5].animate.set_color(WHITE),
                  label_2[0][4:6].animate.set_color(WHITE),
                  label_3[0][7:11].animate.set_color(WHITE))
        self.wait(2)

        self.play(FadeOut(b_value_label_1, b_value_tick_1,
                          b_value_label_2, b_value_tick_2,
                          b_value_label_3, b_value_tick_3))
        self.wait(2)
        
        


# Raiz da função
class vid8(Scene):
    def construct(self):

        t1 = Tex('Raiz').scale(0.8).to_edge(UP, buff=1.2)
        ul_t1 = Underline(t1)
        t2 = MathTex('y = f(x)',' = 0').scale(0.9).next_to(t1, DOWN, buff=0.7)
        self.play(Write(t1), Create(ul_t1), FadeIn(t2[0]))
        self.wait(2)
        self.play(Write(t2[1]))
        self.wait(2)

        axes = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 5, 1],
                    x_length = 4.5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        x_label = MathTex("x").next_to(axes.get_x_axis(), DR, buff = 0)
        y_label = MathTex("y").next_to(axes.get_y_axis(), UL, buff = 0).shift(DOWN*0.1)
        axes_labels = VGroup(x_label, y_label).set_color(WHITE).set_opacity(0.6)
        axes_zero = MathTex('0').scale(0.8).next_to(axes.coords_to_point(0,0,0), DL, buff = 0.13).set_opacity(0.6)
        
        graph_1 = axes.plot(lambda x: 2*x - 4,
                         x_range=[1.5, 4.5], stroke_width = 4).set_color(BLUE)
        root_dot = Dot(axes.coords_to_point(2,0,0), color=YELLOW).set_z_index(2)
        g_graph = VGroup(axes, axes_labels, axes_zero, graph_1, root_dot).scale(0.9).move_to(ORIGIN).shift(DOWN*1.1)

        self.play(FadeIn(axes, axes_labels, axes_zero, graph_1))
        self.wait(2)
        self.play(GrowFromCenter(root_dot))
        self.wait(2)


        t3 = MathTex('y = 3x - 2',' &= 0',
                     r'\\ 3x &= 2',
                     r'\\ x &= 2/3', color=BLUE).shift(LEFT*1)
        
        t4 = MathTex('y = ax + b',' &= 0',
                     r'\\ ax &= -b',
                     r'\\ x &= -b/a', color=GREEN).next_to(t3, RIGHT*2, aligned_edge=UP)
        
        g_1 = VGroup(t3, t4).arrange(RIGHT, buff=2)

        root_box_1 = SurroundingRectangle(t3[3], buff=0.15, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-1)
        root_box_2 = SurroundingRectangle(t4[3], buff=0.15, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-1)

        # Raiz da função exemplo
        self.play(FadeOut(t2, g_graph, root_dot))
        self.play(FadeIn(t3[0]))
        self.wait(2)
        self.play(Write(t3[1]))
        self.wait(2)
        self.play(FadeIn(t3[2]))
        self.wait(2)
        self.play(FadeIn(t3[3]))
        self.play(FadeIn(root_box_1))
        self.wait(2)



        # Raiz de qualquer função afim
        self.play(FadeIn(t4[0]))
        self.wait(2)
        self.play(Write(t4[1]))
        self.wait(2)
        self.play(FadeIn(t4[2]))
        self.wait(2)
        self.play(FadeIn(t4[3]))
        self.play(FadeIn(root_box_2))
        self.wait(2)

        self.play(FadeOut(t3, t4, root_box_1, root_box_2))
        self.wait(2)



        # As funções têm uma única raiz
        g_graph.shift(UP*0.5)
        t5 = Tex('\it Uma única raiz').scale(0.8).shift(RIGHT*2.5+DOWN*1)
        t5_arrow = Arrow(t5, root_dot, color=GRAY, buff=0.1).scale(0.9)
        self.play(FadeIn(axes, axes_labels, axes_zero, graph_1))
        self.wait(2)
        self.play(GrowFromCenter(root_dot))
        self.wait(2)
        self.play(Indicate(graph_1, scale_factor=1.1))
        self.play(Indicate(axes.get_x_axis(), scale_factor=1.1))
        self.wait(2)

        line_1 = DashedLine(LEFT, RIGHT*6, color=GRAY, stroke_width=6, dash_length=0.1).move_to(axes.get_x_axis())
        line_2 = line_1.copy().rotate(63.435*DEGREES).move_to(graph_1)
        self.play(FadeIn(line_1, line_2))
        self.wait(2)
        self.play(Flash(root_dot, num_lines=8))
        self.wait(2)
