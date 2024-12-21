# Intervalos Reais

from manim import *

# Intervalos abertos e fechados 
class vid1(Scene):
    def construct(self):

        # Reta numérica
        number_line_line_1 = NumberLine(x_range=[-4,4,1], include_ticks=False, include_numbers=False, include_tip=True).scale(0.7).shift(DOWN*1)
        number_line_label_1 = MathTex(r"\mathbb{R}").next_to(number_line_line_1, DR, buff=0.1)
        number_line_1 = VGroup(number_line_line_1, number_line_label_1)
        self.play(Create(number_line_line_1))
        self.play(FadeIn(number_line_label_1))
        self.wait(3)

        # Ponto na reta
        dot_b = Dot((-2,-1,0), radius=0.1, color=YELLOW)

        self.play(GrowFromCenter(dot_b))
        self.play(dot_b.animate.shift(RIGHT*4), run_time=2)
        self.play(dot_b.animate.shift(LEFT*0.5))
        self.wait(3)

        # Intervalo na reta
        dot_a = Dot((-1.5,-1,0), radius=0.1, color=YELLOW)
        self.play(GrowFromCenter(dot_a))
        
        line_1 = Line((-1.5,-1,0), (1.5,-1,0), color=YELLOW, stroke_width=10, stroke_opacity=0.5)
        self.play(Create(line_1))
        self.wait(3)

        # Nomeando os pontos a e b
        a_label = MathTex("a", color=YELLOW).next_to(dot_a, UP)
        b_label = MathTex("b", color=YELLOW).next_to(dot_b, UP)
        self.play(FadeIn(a_label, b_label))

        # Intervalo (a,b)
        interval_1 = MathTex("(","a",",","b",")").shift(UP*1)
        interval_1[0].set_color(YELLOW)
        interval_1[1].set_color(YELLOW)
        interval_1[2].set_color(YELLOW)
        interval_1[3].set_color(YELLOW)
        interval_1[4].set_color(YELLOW)
        self.play(Write(interval_1))
        self.wait(3)

        # Notação de conjunto
        interval_2 = MathTex("(","a",",","b",")",r" \:=\: \{ x \in \mathbb{R} \mid ","a"," < x < ","b"," \}").shift(UP*1)
        interval_2[0].set_color(YELLOW)
        interval_2[1].set_color(YELLOW)
        interval_2[2].set_color(YELLOW)
        interval_2[3].set_color(YELLOW)
        interval_2[4].set_color(YELLOW)
        interval_2[6].set_color(YELLOW)
        interval_2[8].set_color(YELLOW)
        self.play(TransformMatchingShapes(interval_1, interval_2))
        self.wait(3)

        # Intervalo limitado texto
        t_2 = Tex("Intervalo limitado", color=YELLOW).shift(UP*2.5)
        self.play(FadeIn(t_2))
        self.play(FadeOut(t_2))
        self.wait(3)

        # x não pode ser igual ao a ou ao b
        t_1 = MathTex(r"x \neq ","a",r" \:\:\:\:\:\:\: x \neq ","b","", color=RED).scale(0.8).next_to(interval_2, UP).shift(RIGHT*1.8)
        t_1[1].set_color(YELLOW)
        t_1[3].set_color(YELLOW)        
        self.play(FadeIn(t_1))
        self.wait(3)
        self.play(FadeOut(t_1))
        self.wait(3)

        # Reta vai para baixo
        g_1 = VGroup(number_line_1, line_1, dot_a, dot_b, a_label, b_label, interval_2)
        self.play(g_1.animate.shift(DOWN*1))

        # Intervalo aberto título
        intervalo_aberto = Tex("Intervalo aberto").shift(UP*3)
        intervalo_aberto_sr = SurroundingRectangle(intervalo_aberto, buff=0.2, fill_opacity=0.2)
        intervalo_aberto_title = VGroup(intervalo_aberto, intervalo_aberto_sr).set_color(GREEN).shift(DOWN*1)
        self.play(LaggedStart(Write(intervalo_aberto), Create(intervalo_aberto_sr, lag_ratio=0.5)))

        #Destaque nos parênteses e colchetes abertos
        self.play(Indicate(interval_2[0]), Indicate(interval_2[4]))

        interval_3 = MathTex("]","a",",","b","[",r" \:\:\:=\:\: \{ x \in \mathbb{R} \mid ","a"," < x < ","b"," \}").shift(UP*1).shift(DOWN*1)
        interval_3[0].set_color(YELLOW)
        interval_3[1].set_color(YELLOW)
        interval_3[2].set_color(YELLOW)
        interval_3[3].set_color(YELLOW)
        interval_3[4].set_color(YELLOW)
        interval_3[6].set_color(YELLOW)
        interval_3[8].set_color(YELLOW)
        self.play(TransformMatchingShapes(interval_2, interval_3))

        self.play(Indicate(interval_3[0]), Indicate(interval_3[4]))
        self.wait(3)

        # Bolinhas vazadas
        dot_a_2_border = Dot((-1.5,-1,0), radius=0.1, color=YELLOW).set_z_index(1)
        dot_a_2_center = Dot((-1.5,-1,0), radius=0.07, color=BLACK).set_z_index(2)
        dot_a_2 = VGroup(dot_a_2_border, dot_a_2_center).shift(DOWN*1)

        dot_b_2_border = Dot((1.5,-1,0), radius=0.1, color=YELLOW).set_z_index(1)
        dot_b_2_center = Dot((1.5,-1,0), radius=0.07, color=BLACK).set_z_index(2)
        dot_b_2 = VGroup(dot_b_2_border, dot_b_2_center).shift(DOWN*1)

        # Setas nas bolinhas do intervalo fechado preenchidas
        arrow_1 = Arrow((-1.5,-3.5,0), (-1.5,-2,0))
        arrow_2 = Arrow((1.5,-3.5,0), (1.5,-2,0))
        self.play(LaggedStart(FadeIn(arrow_1), FadeIn(arrow_2), lag_ratio=0.3))
        self.wait(3)

        self.play(TransformMatchingShapes(dot_a, dot_a_2),
                  TransformMatchingShapes(dot_b, dot_b_2))
        self.wait(3)
        
        self.play(LaggedStart(FadeOut(arrow_1), FadeOut(arrow_2), lag_ratio=0.3))
        self.wait(3)

        # 3 formas de representação do intervalo
        sr_1_2_ref = MathTex("]a,b[",r" \:\:\:=\:\: ",r"\{ x \in \mathbb{R} \mid a < x < b \}").shift(UP*1).shift(DOWN*1)
        sr_3_ref = VGroup(number_line_1, line_1, dot_a_2, dot_b_2, a_label, b_label)

        sr_1 = SurroundingRectangle(sr_1_2_ref[0], buff=0.2, color=YELLOW)
        sr_2 = SurroundingRectangle(sr_1_2_ref[2], buff=0.2, color=YELLOW)
        sr_3 = SurroundingRectangle(sr_3_ref, buff=0.2, color=YELLOW)

        self.play(FadeIn(sr_1))
        self.wait(3)
        self.play(LaggedStart(FadeOut(sr_1), FadeIn(sr_2), lag_ratio=0.5))
        self.wait(3)
        self.play(LaggedStart(FadeOut(sr_2), FadeIn(sr_3), lag_ratio=0.5))
        self.wait(3)
        self.play(FadeOut(sr_3))
        self.wait(3)
        
        # Intervalo aberto vai para a esquerda
        g_all_1 = VGroup(intervalo_aberto_title, interval_3, number_line_1, line_1, dot_a_2, dot_b_2, a_label, b_label)
        self.play(g_all_1.animate.scale(0.8).shift(LEFT*3.5))
        self.wait(3)


        
        # Intervalo fechado
        intervalo_fechado = Tex("Intervalo fechado").shift(UP*3)
        intervalo_fechado_sr = SurroundingRectangle(intervalo_fechado, buff=0.2, fill_opacity=0.2)
        intervalo_fechado_title = VGroup(intervalo_fechado, intervalo_fechado_sr).set_color(GREEN)

        interval_4 = MathTex("[a,b]",r" \:=\: \{ x \in \mathbb{R} \mid ","a",r" \leq x \leq ","b"," \}").shift(UP*1)
        interval_4[0].set_color(BLUE)
        interval_4[2].set_color(BLUE)
        interval_4[4].set_color(BLUE)

        dot_a_fechado = Dot((-1.5,-1,0), radius=0.1, color=BLUE).set_z_index(1)
        dot_b_fechado = Dot((1.5,-1,0), radius=0.1, color=BLUE).set_z_index(1)
        
        a_label_fechado = MathTex("a", color=BLUE).next_to(dot_a_fechado, UP)
        b_label_fechado = MathTex("b", color=BLUE).next_to(dot_b_fechado, UP)

        number_line_line_2 = NumberLine(x_range=[-4,4,1], include_ticks=False, include_numbers=False, include_tip=True).scale(0.7).shift(DOWN*1)
        number_line_label_2 = MathTex(r"\mathbb{R}").next_to(number_line_line_2, DR, buff=0.1)
        number_line_2 = VGroup(number_line_line_2, number_line_label_2)

        line_2 = Line((-1.5,-1,0), (1.5,-1,0), color=BLUE, stroke_width=10, stroke_opacity=0.7)

        g_all_2 = VGroup(intervalo_fechado_title,
                         interval_4, number_line_2,
                         line_2, dot_a_fechado,
                         dot_b_fechado, a_label_fechado,
                         b_label_fechado).scale(0.8).shift(RIGHT*3.5).shift(DOWN*1)
        
        self.play(LaggedStart(Write(intervalo_fechado), Create(intervalo_fechado_sr), Write(interval_4), lag_ratio=0.5))
        self.wait(3)
        self.play(LaggedStart(Create(number_line_line_2),
                              FadeIn(number_line_label_2),
                              GrowFromCenter(dot_a_fechado),
                              FadeIn(a_label_fechado),
                              Create(line_2),
                              GrowFromCenter(dot_b_fechado),
                              FadeIn(b_label_fechado),
                              lag_ratio=0.2))
        self.wait(3)

        # Setas nas bolinhas do intervalo fechado preenchidas
        arrow_3 = Arrow((2.35,-3.1,0), (2.35,-1.6,0))
        arrow_4 = Arrow((4.75,-3.1,0), (4.75,-1.6,0))
        self.play(LaggedStart(FadeIn(arrow_3), FadeIn(arrow_4), lag_ratio=0.3))
        self.play(LaggedStart(FadeOut(arrow_3), FadeOut(arrow_4), lag_ratio=0.3))
        self.wait(3)

        # FadeOut em tudo
        g_all_3 = VGroup(g_all_1, g_all_2)
        self.play(FadeOut(g_all_3))



# Intervalos semiabertos 
class vid2(Scene):
    def construct(self):

        # Intervalo semiaberto título
        intervalo_semiaberto = Tex("Intervalo semiaberto").shift(UP*2)
        intervalo_semiaberto_sr = SurroundingRectangle(intervalo_semiaberto, buff=0.2, fill_opacity=0.2)
        intervalo_semiaberto_title = VGroup(intervalo_semiaberto, intervalo_semiaberto_sr).set_color(GREEN)

        self.play(LaggedStart(Write(intervalo_semiaberto),
                              Create(intervalo_semiaberto_sr),
                              lag_ratio=0.5))
        self.wait(3)
        
        # Notação de conjunto
        interval_1 = MathTex("(a,b]",r" \:=\: \{ x \in \mathbb{R} \mid ","a",r" < x \leq ","b"," \}")
        interval_1[0].set_color(PINK)
        interval_1[2].set_color(PINK)
        interval_1[4].set_color(PINK)

        self.play(Write(interval_1))
        self.wait(3)

        # Pontos do intervalo
        dot_a_border = Dot((-1.5,-1,0), radius=0.1, color=PINK).set_z_index(1)
        dot_a_center = Dot((-1.5,-1,0), radius=0.07, color=BLACK).set_z_index(2)
        dot_a_semiaberto = VGroup(dot_a_border, dot_a_center).shift(DOWN*1)

        dot_b_semiaberto = Dot((1.5,-1,0), radius=0.1, color=PINK).set_z_index(1).shift(DOWN*1)
        
        a_label_semiaberto = MathTex("a", color=PINK).next_to(dot_a_semiaberto, UP)
        b_label_semiaberto = MathTex("b", color=PINK).next_to(dot_b_semiaberto, UP)

        # Reta numérica
        number_line_line_1 = NumberLine(x_range=[-4,4,1], include_ticks=False, include_numbers=False, include_tip=True).scale(0.7).shift(DOWN*1)
        number_line_label_1 = MathTex(r"\mathbb{R}").next_to(number_line_line_1, DR, buff=0.1)
        number_line_1 = VGroup(number_line_line_1, number_line_label_1).shift(DOWN*1)

        # Linha do intervalo na reta
        line_1 = Line((-1.5,-1,0), (1.5,-1,0), color=PINK, stroke_width=10, stroke_opacity=0.7).shift(DOWN*1)

        g_all_1 = VGroup(intervalo_semiaberto_title, interval_1, number_line_1, line_1, dot_a_semiaberto, dot_b_semiaberto, a_label_semiaberto, b_label_semiaberto)

        self.play(LaggedStart(Create(number_line_1),
                              FadeIn(number_line_label_1),
                              GrowFromCenter(dot_a_semiaberto),
                              FadeIn(a_label_semiaberto),
                              Create(line_1),
                              GrowFromCenter(dot_b_semiaberto),
                              FadeIn(b_label_semiaberto),
                              lag_ratio=0.2))
        self.wait(3)

        
    
# Intervalos ilimitados / infinitos 
class vid3(Scene):
    def construct(self):

        # Intervalo ilimitado texto
        t_2 = Tex("Intervalos ilimitados", color=YELLOW).shift(UP*2.5)
        self.play(FadeIn(t_2))
        self.wait()

        # Intervalo (a, +inf)
        interval_1 = MathTex("(","a",",","+\infty",")", color=YELLOW).set_z_index(1)

        self.play(Write(interval_1))
        self.wait(3)

        # Pontos do intervalo
        dot_a_border = Dot((-1.5,-1,0), radius=0.1, color=YELLOW).set_z_index(1)
        dot_a_center = Dot((-1.5,-1,0), radius=0.07, color=BLACK).set_z_index(2)
        dot_a_semiaberto = VGroup(dot_a_border, dot_a_center).shift(DOWN*1)

        a_label_semiaberto = MathTex("a", color=YELLOW).next_to(dot_a_semiaberto, UP)

        # Reta numérica
        number_line_line_1 = NumberLine(x_range=[-4,4,1], include_ticks=False, include_numbers=False, include_tip=True).scale(0.7).shift(DOWN*1)
        number_line_label_1 = MathTex(r"\mathbb{R}").next_to(number_line_line_1, DR, buff=0.1)
        number_line_1 = VGroup(number_line_line_1, number_line_label_1).shift(DOWN*1)

        # Linha do intervalo na reta
        line_1 = Line((-1.5,-1,0), (2.6,-1,0), color=YELLOW, stroke_width=10, stroke_opacity=0.5).shift(DOWN*1)

        self.play(LaggedStart(Create(number_line_line_1),
                              FadeIn(number_line_label_1),
                              lag_ratio=0.3))
        self.wait(3)
        self.play(LaggedStart(GrowFromCenter(dot_a_semiaberto),
                              FadeIn(a_label_semiaberto),
                              lag_ratio=0.3))
        self.play(Create(line_1))
        self.wait(3)

        # FadeOut 'intervalo ilimitado' e shift(UP) tudo
        g = VGroup(number_line_1, dot_a_semiaberto, a_label_semiaberto, line_1, interval_1)
        self.play(LaggedStart(FadeOut(t_2), g.animate.shift(UP), lag_ratio=0.3))
        self.wait(3)

        # Intervalo (a, +inf) notação de conjunto
        interval_2 = MathTex("(a,+\infty)",r"\:=\: \{ x \in \mathbb{R} \mid x > ","a"," \}").shift(UP)
        interval_2[0].set_color(YELLOW) 
        interval_2[2].set_color(YELLOW)
        self.play(TransformMatchingShapes(interval_1, interval_2))
        self.wait(3)

        g_all_1 = VGroup(interval_2, line_1, dot_a_semiaberto, a_label_semiaberto)
        self.play(FadeOut(g_all_1))

        

        # Intervalo (-inf, b]
        interval_3 = MathTex("(","-\infty",",","b","]", color=BLUE).set_z_index(1).shift(UP)

        self.play(Write(interval_3))
        self.wait(3)

        # Pontos do intervalo
        dot_b_fechado = Dot((1.5,-1,0), radius=0.1, color=BLUE).set_z_index(1)
        b_label_fechado = MathTex("b", color=BLUE).next_to(dot_b_fechado, UP)

        # Linha do intervalo na reta
        line_2 = Line((1.5,-1,0), (-2.8,-1,0), color=BLUE, stroke_width=10, stroke_opacity=0.7)

        self.play(LaggedStart(GrowFromCenter(dot_b_fechado),
                              FadeIn(b_label_fechado),
                              lag_ratio=0.3))
        self.play(Create(line_2))
        self.wait(3)

        # Intervalo (-inf, b] notação de conjunto
        interval_4 = MathTex("(-\infty,b]",r"\:=\: \{ x \in \mathbb{R} \mid x \leq ","b"," \}").shift(UP)
        interval_4[0].set_color(BLUE)
        interval_4[2].set_color(BLUE)
        self.play(TransformMatchingShapes(interval_3, interval_4))
        self.wait(3)

        # FadeOut geral
        g_all_2 = VGroup(interval_4, dot_b_fechado, b_label_fechado, line_2)
        self.play(FadeOut(g_all_2))



        # Intervalo (-inf, +inf)
        interval_5 = MathTex("(","-\infty",",","+\infty",")", color=PINK).set_z_index(1).shift(UP)

        self.play(Write(interval_5))
        self.wait(3)

        # Linha do intervalo na reta
        line_3 = Line((2.6,-1,0), (-2.8,-1,0), color=PINK, stroke_width=10, stroke_opacity=0.7)

        self.play(GrowFromCenter(line_3))
        self.wait(3)

        # Intervalo (-inf, b] notação de conjunto
        interval_6 = MathTex("(-\infty,+\infty)",r"\:=\: \mathbb{R}").shift(UP)
        interval_6[0].set_color(PINK)
        self.play(TransformMatchingShapes(interval_5, interval_6))
        self.wait(3)

        # FadeOut geral
        g_all_3 = VGroup(interval_6, line_3, number_line_1)
        self.play(FadeOut(g_all_3))

        # Intervalo ilimitado é sempre aberto
        t_3 = MathTex("(a,",r"+\infty)", color=YELLOW)
        t_4 = MathTex("(-\infty",r",b]", color=BLUE)
        t_5 = MathTex("(-\infty",r",",r"+\infty)", color=PINK)
        g_t = VGroup(t_3, t_4, t_5).arrange(DOWN, buff=1)
        self.play(FadeIn(g_t))
        self.wait(3)

        d1 = Dot((2.2,1.5,0))
        arrow_1 = Arrow(d1, t_3.get_right())
        arrow_2 = Arrow(d1, t_3.get_right()).move_to(t_4.get_left()).rotate(PI).shift(LEFT*0.6)
        arrow_3 = Arrow(d1, t_3.get_right()).move_to(t_5.get_left()).rotate(PI).shift(LEFT*0.6)
        arrow_4 = Arrow(d1, t_3.get_right()).move_to(t_5.get_right()).shift(RIGHT*0.6)
        g_arrow = VGroup(arrow_1, arrow_2, arrow_3, arrow_4)
        self.play(LaggedStart(FadeIn(arrow_1),
                              FadeIn(arrow_2),
                              FadeIn(arrow_3),
                              FadeIn(arrow_4),
                              lag_ratio=0.4))
        self.wait(3)
        
        # FadeOut geral
        g_all_4 = VGroup(g_t, g_arrow)
        self.play(FadeOut(g_all_4))



# Operações com intervalos 
class vid4(Scene):
    def construct(self):

        # Nomes das operações
        t1 = Tex("União")
        t2 = Tex("Interseção")
        t3 = Tex("Diferença")
        gt_1 = VGroup(t1, t2, t3).set_color(GREEN).arrange(DOWN, buff=1).shift(LEFT)

        t1_2 = MathTex(r"\cup").scale(1.2)
        t2_2 = MathTex(r"\cap").scale(1.2)
        t3_2 = MathTex(r"\backslash")
        gt_2 = VGroup(t1_2, t2_2, t3_2).set_color(GREEN).arrange(DOWN, buff=1).shift(RIGHT)

        gt_1_e_2 = VGroup(gt_1, gt_2).move_to(ORIGIN)
        
        self.play(LaggedStart(FadeIn(t1),
                              FadeIn(t1_2),
                              FadeIn(t2),
                              FadeIn(t2_2),
                              FadeIn(t3),
                              FadeIn(t3_2),
                              lag_ratio=0.3))
        self.wait(3)
        
        t4_1 = Tex("União", color=GREEN)
        t4_2 = MathTex(r"\cup", color=GREEN).scale(1.2).next_to(t4_1, RIGHT)
        t4 = VGroup(t4_1, t4_2).to_edge(UL)

        g = VGroup(t1, t1_2)
        self.play(ReplacementTransform(g, t4), FadeOut(t2, t3,t2_2, t3_2))
        self.wait()
        
        

# Exemplo de união 
class vid5(Scene):
    def construct(self):

        # Título no canto 
        t1_1 = Tex("União", color=GREEN)
        t1_2 = MathTex(r"\cup", color=GREEN).scale(1.2).next_to(t1_1, RIGHT)
        t1 = VGroup(t1_1, t1_2).to_edge(UL)
        self.add(t1)
        self.wait()


        # Inequação-exemplo
        t2_1 = MathTex(r"x^2 - 1 > 0", color = WHITE).shift(UP*2)
        self.play(Write(t2_1))
        self.wait(3)

        # Gráfico de x^2 - 1

        axes = Axes(x_range = [-3,3,1],
                    y_range = [-1.5,3,1],
                    x_length = 5,
                    y_length = 5,
                    x_axis_config = {'include_ticks' : False, 'include_tip' : False},
                    y_axis_config = {'include_ticks' : False, 'include_tip' : True}).scale(0.6).shift(DOWN)
        
        x_label = MathTex('x').scale(0.8).next_to(axes, RIGHT, buff = 0).shift(DOWN*0.8)
        y_label = MathTex('y').scale(0.8).next_to(axes, UP, buff = -0.1).shift(LEFT*0.3)
        labels = VGroup(x_label, y_label)

        plane = NumberPlane(x_range = [-3,3,1],
                    y_range = [-1.5,3,1],
                    x_length = 7,
                    y_length = 5).scale(0.6).shift(DOWN).set_opacity(0.3)
        
        graph = axes.plot(lambda x : 0.5*x**2 - 1, color = BLUE, stroke_width = 5)

        number_line = NumberLine(x_range = [-3,3,1], length = 8,
                                 include_ticks=False, include_numbers=False, include_tip=True).scale(0.6).shift(DOWN*1.5)

        self.play(FadeIn(axes, number_line, plane))
        self.play(Create(graph))
        self.wait(3)



        graph_2 = axes.plot(lambda x : 0.5*x**2 - 1, x_range = [1.414,3,1], color = YELLOW, stroke_width = 15, stroke_opacity = 0.5)
        graph_3 = axes.plot(lambda x : 0.5*x**2 - 1, x_range = [-3, -1.414,1], color = YELLOW, stroke_width = 15, stroke_opacity = 0.5)

        dot_1_negative_border = Dot(axes.coords_to_point(-1.414, 0), radius=0.1, color = YELLOW)
        dot_1_negative_center = Dot(axes.coords_to_point(-1.414, 0), radius=0.07, color=BLACK).set_z_index(2)
        dot_1_negative = VGroup(dot_1_negative_border, dot_1_negative_center)

        dot_1_positive_border = Dot(axes.coords_to_point(1.414, 0), radius=0.1, color = YELLOW)
        dot_1_positive_center = Dot(axes.coords_to_point(1.414, 0), radius=0.07, color=BLACK).set_z_index(2)
        dot_1_positive = VGroup(dot_1_positive_border, dot_1_positive_center)
        
        dots = VGroup(dot_1_negative, dot_1_negative_center, dot_1_positive, dot_1_positive_center)

        dot_1_negative_label = MathTex('-1').scale(0.8).next_to(dot_1_negative, DL, buff = 0.1)
        dot_1_positive_label = MathTex('1').scale(0.8).next_to(dot_1_positive, DR, buff = 0.1)
        dot_labels = VGroup(dot_1_negative_label, dot_1_positive_label).set_color(YELLOW)

        self.play(FadeIn(graph_2, graph_3))
        self.play(GrowFromCenter(dot_1_negative), GrowFromCenter(dot_1_positive), FadeIn(dot_labels))
        self.wait(3)



        interval_negative_part = Line(number_line.number_to_point(-3), dot_1_negative, color = YELLOW, stroke_width=10, stroke_opacity = 0.5)
        interval_positive_part = Line(dot_1_positive, number_line.number_to_point(2.735), color = YELLOW, stroke_width=10, stroke_opacity = 0.5)
        interval_line = VGroup(interval_negative_part, interval_positive_part)

        g = VGroup(number_line, interval_line, dot_labels, dots)

        self.play(FadeIn(number_line),
                  ReplacementTransform(graph_3, interval_negative_part),
                  ReplacementTransform(graph_2, interval_positive_part),
                  FadeOut(axes, graph, plane))
        self.play(g.animate.shift(UP*0.5))
        self.wait(3)

        interval_label_1 = MathTex(r'(-\infty, -1)').scale(0.8).next_to(interval_negative_part, UP, buff = 0.5)
        interval_label_2 = MathTex(r'(1, +\infty)').scale(0.8).next_to(interval_positive_part, UP, buff = 0.5)
        interval_labels = VGroup(interval_label_1, interval_label_2).set_color(YELLOW)
        self.play(FadeIn(interval_label_1))
        self.wait(3)
        self.play(FadeIn(interval_label_2))
        self.wait(3)

        solution = MathTex(r'S = x \in',r'(-\infty, -1) \cup (1, +\infty)').scale(0.8).next_to(number_line, UP, buff = 1)
        solution[1].set_color(YELLOW)
        self.play(TransformMatchingShapes(interval_labels, solution))
        self.wait(3)

        # FadeOut geral
        fadeout = Square(color = BLACK).scale(10)
        self.play(FadeIn(fadeout))



# Exemplo de interseção 
class vid6(Scene):
    def construct(self):

        # Título no canto 
        t1_1 = Tex("Interseção", color=GREEN)
        t1_2 = MathTex(r"\cap", color=GREEN).scale(1.2).next_to(t1_1, RIGHT)
        t1 = VGroup(t1_1, t1_2)
        self.play(FadeIn(t1))
        self.play(t1.animate.to_edge(UL))
        self.wait()



        # Exemplo sistema de inequações
        system_ineq = MathTex(r"\begin{cases} 3x - 2 > 1 \\ 2x + 1 \leq 5 \end{cases}")
        self.play(Write(system_ineq), run_time=1.5)
        self.wait(3)

        # Primeira inequação do exemplo
        line_1_1 = system_ineq[0][1:7].copy().set_color(BLUE)
        self.play(system_ineq.animate.shift(LEFT*3.5+UP*0.5), line_1_1.animate.move_to([4,0.5,0], aligned_edge=RIGHT))
        
        line_1_2 = MathTex("3x - 2 > 1").move_to(line_1_1.get_center())
        line_1_3 = MathTex("3x > 3").next_to(line_1_2, DOWN)
        line_1_4 = MathTex("x > 1").next_to(line_1_3, DOWN)
        g_line_1 = VGroup(line_1_2, line_1_3, line_1_4).set_color(BLUE)

        self.add(line_1_2).remove(line_1_1)
        self.play(TransformFromCopy(line_1_2, line_1_3))
        self.play(TransformFromCopy(line_1_3, line_1_4))
        self.wait(3)

        # Intervalo 1a inequação
        number_line_1 = NumberLine(x_range=[-3,3,1], include_ticks=False, include_numbers=False, include_tip=True)
        number_line_1.next_to(g_line_1, UP, buff=1).scale(0.7).shift(RIGHT*0.5)

        interval_1 = MathTex(r"(1 , +\infty)", color=BLUE).scale(0.8).next_to(number_line_1, LEFT)

        dot_1_border = Dot((-1.5,1,0), radius=0.1, color=BLUE).set_z_index(1)
        dot_1_center = Dot((-1.5,1,0), radius=0.07, color=BLACK).set_z_index(2)
        dot_1_aberto = VGroup(dot_1_border, dot_1_center)
        dot_1_aberto.move_to(number_line_1).shift(LEFT)
        dot_1_label = MathTex("1", color=BLUE).scale(0.8).next_to(dot_1_border, UP)

        dot_ref1_line_1 = Dot(dot_1_aberto.get_center())
        dot_ref2_line_1 = Dot(dot_1_aberto.get_center()).shift(RIGHT*2.93)
        line_1 = Line(dot_ref1_line_1, dot_ref2_line_1, color=BLUE, stroke_width=10, stroke_opacity=0.7)

        self.play(LaggedStart(FadeIn(interval_1),
                              Create(number_line_1),
                              GrowFromCenter(dot_1_aberto),
                              FadeIn(dot_1_label),
                              Create(line_1),
                              lag_ratio=0.5))
        self.wait(3)

        self.play(FadeOut(g_line_1))





        # Segunda inequação do exemplo
        line_2_1 = system_ineq[0][7:13].copy().set_color(RED)
        self.play(line_2_1.animate.move_to([4,-0.5,0], aligned_edge=RIGHT))
        
        line_2_2 = MathTex(r"2x + 1 \leq 5").move_to(line_2_1.get_center())
        line_2_3 = MathTex(r"2x \leq 4").next_to(line_2_2, DOWN)
        line_2_4 = MathTex(r"x \leq 2").next_to(line_2_3, DOWN)
        g_line_2 = VGroup(line_2_2, line_2_3, line_2_4).set_color(RED)

        self.add(line_2_2).remove(line_2_1)
        self.play(TransformFromCopy(line_2_2, line_2_3))
        self.play(TransformFromCopy(line_2_3, line_2_4))
        self.wait(3)

        # Intervalo 2a inequação
        number_line_2 = NumberLine(x_range=[-3,3,1], include_ticks=False, include_numbers=False, include_tip=True)
        number_line_2.next_to(number_line_1, DOWN, buff=1).scale(0.7)

        interval_2 = MathTex(r"(-\infty , 2]", color=RED).scale(0.8).next_to(number_line_2, LEFT)

        dot_2_fechado = Dot((-1.5,1,0), radius=0.1, color=RED).set_z_index(1)
        dot_2_fechado.move_to(number_line_2).shift(RIGHT)
        dot_2_label = MathTex("2", color=RED).scale(0.8).next_to(dot_2_fechado, UP)

        dot_ref1_line_2 = Dot(dot_2_fechado.get_center())
        dot_ref2_line_2 = Dot(dot_2_fechado.get_center()).shift(LEFT*3.18)
        line_2 = Line(dot_ref1_line_2, dot_ref2_line_2, color=RED, stroke_width=10, stroke_opacity=0.7)

        self.play(LaggedStart(FadeIn(interval_2),
                              Create(number_line_2),
                              GrowFromCenter(dot_2_fechado),
                              FadeIn(dot_2_label),
                              Create(line_2),
                              lag_ratio=0.5))
        self.wait(3)
        
        self.play(FadeOut(g_line_2))





        # Intervalo resultante interseção
        number_line_3 = NumberLine(x_range=[-3,3,1], include_ticks=False, include_numbers=False, include_tip=True)
        number_line_3.next_to(number_line_2, DOWN, buff=1).scale(0.7)

        interval_3_1 = MathTex(r"S = (1 , +\infty) \cap (-\infty , 2]", color=PURPLE).scale(0.8).move_to(number_line_3)
        interval_3_2 = MathTex(r"S = (1 , 2]", color=PURPLE).scale(0.8).next_to(number_line_3, LEFT)

        dot_3_border = Dot((-1.5,1,0), radius=0.1, color=PURPLE).set_z_index(1)
        dot_3_center = Dot((-1.5,1,0), radius=0.07, color=BLACK).set_z_index(2)
        dot_3_aberto = VGroup(dot_3_border, dot_3_center)
        dot_3_aberto.move_to(number_line_3).shift(LEFT)
        dot_3_aberto_label = MathTex("1", color=PURPLE).scale(0.8).next_to(dot_3_border, DOWN)

        dot_3_fechado = Dot((-1.5,1,0), radius=0.1, color=PURPLE).set_z_index(1)
        dot_3_fechado.move_to(number_line_3).shift(RIGHT)
        dot_3_fechado_label = MathTex("2", color=PURPLE).scale(0.8).next_to(dot_3_fechado, DOWN)

        dot_ref1_line_3 = Dot(dot_3_aberto.get_center())
        dot_ref2_line_3 = Dot(dot_3_fechado.get_center())
        line_3 = Line(dot_ref1_line_3, dot_ref2_line_3, color=PURPLE, stroke_width=10, stroke_opacity=0.7)

        dashed_line_1 = DashedLine(dot_1_aberto, dot_3_aberto, color = YELLOW)
        dashed_line_2 = DashedLine(dot_2_fechado, dot_3_fechado, color = YELLOW)
        dashed_lines = VGroup(dashed_line_1, dashed_line_2).set_color(YELLOW).set_opacity(0.5).set_z_index(-1)

        self.play(Write(interval_3_1))
        self.wait(3)
        self.play(interval_3_1.animate.shift(LEFT*4.4))
        self.wait(3)

        self.play(Create(number_line_3))
        self.play(Create(dashed_line_1), Create(dashed_line_2), rate_func = smooth)

        self.play(GrowFromCenter(dot_3_aberto), GrowFromCenter(dot_3_fechado),
                  FadeIn(dot_3_aberto_label), FadeIn(dot_3_fechado_label))

        self.play(Create(line_3))
        self.wait(3)
                
        self.play(TransformMatchingShapes(interval_3_1, interval_3_2))
        self.wait(3)



        g_all = VGroup(t1, system_ineq,
                       number_line_1, interval_1, dot_1_aberto, dot_1_label, line_1,
                       number_line_2, interval_2, dot_2_fechado, dot_2_label, line_2,
                       number_line_3, interval_3_2, dot_3_aberto, dot_3_aberto_label, dot_3_fechado, dot_3_fechado_label, line_3)
        self.play(FadeOut(g_all))



# Exemplo de diferença 
class vid7(Scene):
    def construct(self):

        # Título no canto 
        t1_1 = Tex("Diferença", color=GREEN)
        t1_2 = MathTex(r'\backslash', color=GREEN).next_to(t1_1, RIGHT)
        t1 = VGroup(t1_1, t1_2)
        self.play(FadeIn(t1))
        self.play(t1.animate.to_edge(UL))

        t2 = MathTex(r'f(x) = {1 \over x}', color = BLUE)
        self.play(Write(t2))
        self.wait(2) 
        self.play(t2.animate.shift(LEFT*3.4))

        t3 = Tex('definida para').next_to(t2, RIGHT, buff = 0.5)
        t4 = MathTex(r'x \in (-\infty, +\infty)', color = BLUE).next_to(t3, RIGHT, buff = 0.4)
        g = VGroup(t2, t3, t4).move_to(ORIGIN)
        self.play(Write(t3))
        self.play(Write(t4))
        self.wait(2)

        t2_2 = MathTex(r'f(x) = {1 \over x}', color = BLUE).shift(LEFT*3.4)
        t3_2 = Tex('definida para').next_to(t2_2, RIGHT, buff = 0.5)
        t5 = MathTex(r'x \in (-\infty, +\infty) \:\backslash\: \{ 0 \}', color = BLUE).next_to(t3_2, RIGHT, buff = 0.4)
        g2 = VGroup(t2_2, t3_2, t5).move_to(ORIGIN)
        self.play(TransformMatchingShapes(g, g2))
        self.wait(2)



# Observação uso do x é uma convenção 
class vid8(Scene):
    def construct(self):

        t1 = MathTex(r"\{ x \in \mathbb{R} \mid ","a"," < x < ","b"," \}")
        self.add(t1)
        self.wait(3)

        t2 = MathTex(r"\{ ",r" x ",r" \in \mathbb{R} \mid ","a"," < ",r"x",r" < ","b"," \}")
        t2[1].set_color(YELLOW)
        t2[5].set_color(YELLOW)
        self.play(TransformMatchingShapes(t1, t2))
        self.wait(3)

        t3 = MathTex(r"\{ ",r" y ",r" \in \mathbb{R} \mid ","a"," < ",r"y",r" < ","b"," \}")
        t3[1].set_color(YELLOW)
        t3[5].set_color(YELLOW)
        self.play(TransformMatchingShapes(t2, t3))
        self.wait(3)

        t4 = MathTex(r"\{ ",r" \heartsuit ",r" \in \mathbb{R} \mid ","a"," < ",r"\heartsuit",r" < ","b"," \}")
        t4[1].set_color(YELLOW)
        t4[5].set_color(YELLOW)
        self.play(TransformMatchingShapes(t3, t4))
        self.wait(3)

        t5 = MathTex('x')
        t6 = MathTex('y')
        t7 = MathTex('\heartsuit')
        g = VGroup(t5, t6, t7).arrange(RIGHT, buff = 1).shift(UP*1.5).set_color(YELLOW)

        arrow = Arrow(UP*2.5, UP*1).shift(LEFT*0.8+UP*0.6).rotate(-45*DEGREES)

        self.play(LaggedStart(
            TransformMatchingShapes(t4, t1),
            FadeIn(g),
            lag_ratio = 0.5))
        self.play(FadeIn(arrow))
        self.play(arrow.animate.shift(RIGHT*2.5), run_time = 1.8)
        self.wait(3)
        self.play(FadeOut(arrow))
        self.wait(3)



# Apêndice cenas faltando
class vid9(Scene):
    def construct(self):

        # Intervalo fechado
        intervalo_fechado = Tex("Intervalo fechado").shift(UP*3)
        intervalo_fechado_sr = SurroundingRectangle(intervalo_fechado, buff=0.2, fill_opacity=0.2)
        intervalo_fechado_title = VGroup(intervalo_fechado, intervalo_fechado_sr).set_color(GREEN)

        interval_4 = MathTex("[",r" a,b ",r"]",r" \:=\: \{ x \in \mathbb{R} \mid ","a",r" \leq x \leq ","b"," \}").shift(UP*1)
        interval_4[0].set_color(BLUE)
        interval_4[1].set_color(BLUE)
        interval_4[2].set_color(BLUE)
        interval_4[4].set_color(BLUE)

        dot_a_fechado = Dot((-1.5,-1,0), radius=0.1, color=BLUE).set_z_index(1)
        dot_b_fechado = Dot((1.5,-1,0), radius=0.1, color=BLUE).set_z_index(1)
        
        a_label_fechado = MathTex("a", color=BLUE).next_to(dot_a_fechado, UP)
        b_label_fechado = MathTex("b", color=BLUE).next_to(dot_b_fechado, UP)

        number_line_line_2 = NumberLine(x_range=[-4,4,1], include_ticks=False, include_numbers=False, include_tip=True).scale(0.7).shift(DOWN*1)
        number_line_label_2 = MathTex(r"\mathbb{R}").next_to(number_line_line_2, DR, buff=0.1)
        number_line_2 = VGroup(number_line_line_2, number_line_label_2)

        line_2 = Line((-1.5,-1,0), (1.5,-1,0), color=BLUE, stroke_width=10, stroke_opacity=0.7)

        g_all_2 = VGroup(intervalo_fechado_title,
                         interval_4, number_line_2,
                         line_2, dot_a_fechado,
                         dot_b_fechado, a_label_fechado,
                         b_label_fechado).scale(0.8).shift(RIGHT*3.5).shift(DOWN*1)

        #self.add(g_all_2)
        #self.wait()
        #self.play(Indicate(interval_4[0]), Indicate(interval_4[2]), color = BLUE)
        #self.wait()

        #####################

        t = MathTex("(a,b]", color = PINK)

        interval_1 = MathTex("(a,b]",r" \:=\: \{ x \in \mathbb{R} \mid ","a",r" < x \leq ","b"," \}")
        interval_1[0].set_color(PINK)
        interval_1[2].set_color(PINK)
        interval_1[4].set_color(PINK)
        #self.play(Write(t))
        #self.wait(2)
        #self.play(TransformMatchingShapes(t, interval_1))
        #self.wait()

        #####################

        t2 = Tex('Inequação*', color = RED)
        #self.play(FadeOut(t2, shift=DOWN))

        #####################

        number_line = NumberLine(x_range = [-3,3,1], length = 8,
                                 include_ticks=False, include_numbers=False, include_tip=True).scale(0.6).shift(DOWN*1.5)
        interval_negative_part = Line(number_line.number_to_point(-3), number_line.number_to_point(-1.414), color = YELLOW, stroke_width=10, stroke_opacity = 0.5)
        interval_positive_part = Line(number_line.number_to_point(1.414), number_line.number_to_point(2.735), color = YELLOW, stroke_width=10, stroke_opacity = 0.5)
        interval_line = VGroup(interval_negative_part, interval_positive_part)

        interval_label_1 = MathTex(r'(-\infty, -1)').scale(0.8).next_to(interval_negative_part, UP, buff = 0.5)
        interval_label_2 = MathTex(r'(1, +\infty)').scale(0.8).next_to(interval_positive_part, UP, buff = 0.5)
        interval_labels = VGroup(interval_label_1, interval_label_2).set_color(YELLOW)

        g = VGroup(number_line, interval_line, interval_labels).shift(UP*0.5)

        solution = MathTex(r'S = x \in',r'(-\infty, -1) \cup (1, +\infty)').scale(0.8).next_to(number_line, UP, buff = 1)
        solution[1].set_color(YELLOW)

        #self.play(FadeIn(interval_label_1))
        #self.wait(2)
        #self.play(FadeIn(interval_label_2))
        #self.wait(2)
        #self.play(TransformMatchingShapes(interval_labels, solution))
        #self.wait(2)

        #####################

        # Reta numérica
        number_line_line_1 = NumberLine(x_range=[-4,4,1], include_ticks=False, include_numbers=False, include_tip=True).scale(0.7).shift(DOWN*1)
        number_line_label_1 = MathTex(r"\mathbb{R}").next_to(number_line_line_1, DR, buff=0.1)
        number_line_1 = VGroup(number_line_line_1, number_line_label_1)
        self.add(number_line_1)

        # Intervalo (-inf, +inf)
        interval_5 = MathTex("(","-\infty",",","+\infty",")", color=PINK).set_z_index(1).shift(UP)

        self.play(Write(interval_5))
        self.wait(3)

        # Linha do intervalo na reta
        line_3 = Line((2.55,-1,0), (-2.8,-1,0), color=PINK, stroke_width=10, stroke_opacity=0.7)

        self.play(GrowFromCenter(line_3))
        self.wait(3)

        # Intervalo (-inf, b] notação de conjunto
        interval_6 = MathTex("(-\infty,+\infty)",r"\:=\: \mathbb{R}").shift(UP)
        interval_6[0].set_color(PINK)
        self.play(TransformMatchingShapes(interval_5, interval_6))
        self.wait(3)

        # FadeOut geral
        g_all_3 = VGroup(interval_6, line_3, number_line_1)
        self.play(FadeOut(g_all_3))
