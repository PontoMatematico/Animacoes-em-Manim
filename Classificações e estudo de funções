# Classificações e estudo de funções

from manim import *

# Introdução
class vid0(Scene):
    def construct(self):

        # Referência ao vídeo anterior
        t_1 = Tex('O que é função').scale(1.7).to_edge(UP, buff = 1)
        
        axes = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3)
        axes_labels = VGroup(x_label, y_label).set_color(WHITE)
        axes_zero = MathTex('0').scale(0.8).next_to(axes, DL, buff = -0.7)

        graph = axes.plot(lambda x: x * 1/3 + np.sin(x + 4) + 1.3,
                            x_range=[0.5, 4], stroke_width = 4).set_color(BLUE).set_z_index(2)

        t_2 = MathTex('y = f(x)', stroke_width = 0.9).scale(1.4).next_to(graph, RIGHT).set_color(BLUE).shift(UP*0.3)

        g_graph = VGroup(axes, axes_labels, graph).shift(DOWN)


        g_video_1 = VGroup(g_graph, t_1, t_2).scale(0.5).move_to(ORIGIN).shift(RIGHT*0.5)
        g_video_1_rectangle = Rectangle(width=1.6, height=0.9, color=WHITE, stroke_width=1.5).scale(4)


        self.play(FadeIn(g_video_1, g_video_1_rectangle))
        self.wait(2)
        self.play(FadeOut(g_video_1, g_video_1_rectangle))
        self.wait(2)



        # Muitos tipos de funções
        axes_1 = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.7)
        graph_1 = axes_1.plot(lambda x: 1.8,
                            x_range=[-1, 5], stroke_width = 4).set_color(BLUE).set_z_index(2)
        rectangle_1 = SurroundingRectangle(axes_1, buff=0.3, color=GRAY, stroke_width=2)
        g_1 = VGroup(axes_1, graph_1, rectangle_1)



        axes_2 = axes_1.copy()
        graph_2 = axes_2.plot(lambda x: 2 ** (x-3),
                            x_range=[-1, 5], stroke_width = 4).set_color(BLUE).set_z_index(2)
        rectangle_2 = SurroundingRectangle(axes_2, buff=0.3, color=GRAY, stroke_width=2)
        g_2 = VGroup(axes_2, graph_2, rectangle_2)



        axes_3 = axes_1.copy()
        graph_3 = axes_3.plot(lambda x: (x-2.5) ** 2 + 0.5,
                            x_range=[0.5, 4.5], stroke_width = 4).set_color(BLUE).set_z_index(2)
        rectangle_3 = SurroundingRectangle(axes_3, buff=0.3, color=GRAY, stroke_width=2)
        g_3 = VGroup(axes_3, graph_3, rectangle_3)



        axes_5 = Axes(x_range = [-5, 5, 1],
                    y_range = [-4.5, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.7)
        graph_5_a = axes_5.plot(lambda x: 1/x,
                            x_range=[0.3, 4.1], stroke_width = 4).set_color(BLUE).set_z_index(2)
        graph_5_b = axes_5.plot(lambda x: 1/x,
                            x_range=[-5, -0.22], stroke_width = 4).set_color(BLUE).set_z_index(2)
        rectangle_5 = SurroundingRectangle(axes_5, buff=0.3, color=GRAY, stroke_width=2)
        g_5 = VGroup(axes_5, graph_5_a, graph_5_b, rectangle_5)
        
        
        
        axes_4 = axes_5.copy()
        graph_4 = axes_4.plot(lambda x: np.sin(3*x),
                            x_range=[-4.5, 4.5], stroke_width = 4).set_color(BLUE).set_z_index(2)
        rectangle_4 = SurroundingRectangle(axes_4, buff=0.3, color=GRAY, stroke_width=2)
        g_4 = VGroup(axes_4, graph_4, rectangle_4)


        axes_6 = axes_5.copy()
        graph_6 = axes_6.plot(lambda x: 0.2 * x ** 3,
                            x_range=[-2.823, 2.823], stroke_width = 4).set_color(BLUE).set_z_index(2)
        rectangle_6 = SurroundingRectangle(axes_6, buff=0.3, color=GRAY, stroke_width=2)
        g_6 = VGroup(axes_6, graph_6, rectangle_6)


        g = VGroup(g_1, g_2, g_3, g_4, g_6, g_5).arrange_in_grid().scale(0.5)

        self.play(Succession(
            FadeIn(g_1), FadeIn(g_2), FadeIn(g_3),
            FadeIn(g_4), FadeIn(g_6), FadeIn(g_5)
        ))
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)








# Anúncio dos tópicos
class vid1(Scene):
    def construct(self):

        t1 = Tex(r'\scshape Sobrejetora / Injetora / Bijetora').scale(1.2)
        
        self.wait(2)
        self.play(FadeIn(t1))
        self.wait(2)
        self.play(FadeOut(t1))
        self.wait(2)

        t2 = Tex('\scshape Função constante').scale(1.2)
        self.play(FadeIn(t2))
        self.wait(2)
        self.play(FadeOut(t2))
        self.wait(2)

        t8 = Tex('\scshape Zeros da função').scale(1.2)
        self.play(FadeIn(t8))
        self.wait(2)
        self.play(FadeOut(t8))
        self.wait(2)

        t3 = Tex('\scshape Crescente / Decrescente').scale(1.2)
        self.play(FadeIn(t3))
        self.wait(2)
        self.play(FadeOut(t3))
        self.wait(2)

        t4 = Tex('\scshape Máximos / Mínimos').scale(1.2)
        self.play(FadeIn(t4))
        self.wait(2)
        self.play(FadeOut(t4))
        self.wait(2)

        t5 = Tex('\scshape Limitada / Ilimitada').scale(1.2)
        self.play(FadeIn(t5))
        self.wait(2)
        self.play(FadeOut(t5))
        self.wait(2)

        t6 = Tex('\scshape Assíntotas').scale(1.2)
        self.play(FadeIn(t6))
        self.wait(2)
        self.play(FadeOut(t6))
        self.wait(2)

        t7 = Tex('\scshape Par / Ímpar').scale(1.2)
        self.play(FadeIn(t7))
        self.wait(2)
        self.play(FadeOut(t7))
        self.wait(2)



# Sobrejetora
class vid2(Scene):
    def construct(self):

        # Retomando a definição e o diagrama
            # Definição
                                         # 0            1         2         3         4                  5                         6             7      8       9             10                11        12     13      
        function_definition = Tex(r'\it Uma função ',r'$f:\:$',r'$A$',r'$\:\to\:$',r'$B$',r' é uma relação que associa ',r'\\ cada elemento ',r'$x$',r' de ',r'$A$',r' a um único elemento ',r'$f(x)$',r' de ',r'$B$').scale(0.8).shift(UP*2.7)
        function_definition[2].set_color(RED)
        function_definition[4].set_color(BLUE)
        function_definition[7].set_color(RED)
        function_definition[9].set_color(RED)
        function_definition[11].set_color(BLUE)
        function_definition[13].set_color(BLUE)

            # Diagrama
                # Domínio
        domain = Ellipse(width = 3, height = 4, fill_opacity = 0.2).shift(LEFT*2.5)
        domain_label_1 = MathTex('A', color = RED).scale(1.5).next_to(domain, UP, buff = 0.3)
        
        domain_element_1 = Dot(domain.get_center()).shift(UP*1.2)
        domain_element_2 = Dot(domain.get_center()).shift(UP*0.4)
        domain_element_3 = Dot(domain.get_center()).shift(DOWN*0.4)
        domain_element_4 = Dot(domain.get_center()).shift(DOWN*1.2)
        domain_elements = VGroup(domain_element_1, domain_element_2, domain_element_3, domain_element_4)

                # Contradomínio
        codomain = Ellipse(width = 3, height = 4, color = BLUE, fill_opacity = 0.2).shift(RIGHT*2.5)
        codomain_label_1 = MathTex('B', color = BLUE).scale(1.5).next_to(codomain, UP, buff = 0.3)
        
        codomain_element_1 = Dot(codomain.get_center()).shift(UP*1.2)
        codomain_element_2 = Dot(codomain.get_center()).shift(UP*0.4)
        codomain_element_3 = Dot(codomain.get_center()).shift(DOWN*0.4)
        codomain_element_4 = Dot(codomain.get_center()).shift(DOWN*1.2)
        codomain_elements = VGroup(codomain_element_1, codomain_element_2, codomain_element_3, codomain_element_4)
                # Setas
        function = MathTex(r'f').scale(1.2).shift(UP*2.3)

        arrow_1 = CurvedArrow((-2.2, 1.2, 0), (2.2, 1.2, 0), radius = -5, stroke_width = 2.5)
        arrow_2 = CurvedArrow((-2.2, 0.4, 0), (2.2, 0.4, 0), radius = -5, stroke_width = 2.5)
        arrow_3 = CurvedArrow((-2.2, -0.4, 0), (2.2, -0.4, 0), radius = -5, stroke_width = 2.5)
        arrow_4 = CurvedArrow((-2.2, -0.4, 0), (2.2, -1.1, 0), radius = -5, stroke_width = 2.5)
        arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4)

        g_diagram = VGroup(domain, domain_label_1, domain_elements,
                           codomain, codomain_label_1, codomain_elements,
                           function, arrows).scale(0.7).shift(DOWN*1.2)

        self.wait(2)
        self.play(FadeIn(function_definition))
        self.play(FadeIn(g_diagram))
        self.wait(2)



        # Indicando as implicações da definição
            # 1 Não pode sobrar elemento em A
        not_1_1 = Line(UR, DL).scale(0.3)
        not_1_2 = Line(UL, DR).scale(0.3)
        not_1 = VGroup(not_1_1, not_1_2).scale(0.75).set_color(RED).move_to(domain_element_4)

        not_2_1 = Line(UR, DL).scale(0.3)
        not_2_2 = Line(UL, DR).scale(0.3)
        not_2 = VGroup(not_2_1, not_2_2).scale(0.75).set_color(RED).shift(DOWN*1.1)
        
        self.play(domain_element_4.animate.set_color(YELLOW))
        self.wait(2)
        self.play(Create(not_1), domain_element_4.animate.set_color(WHITE))
        self.wait(2)

        self.play(arrow_3.animate.set_color(YELLOW), arrow_4.animate.set_color(YELLOW))
        self.wait(2)
        self.play(Create(not_2), arrow_3.animate.set_color(WHITE), arrow_4.animate.set_color(WHITE))
        self.wait(2)



            # 2 Sobra elemento em B; dois elementos de A compartilham a mesma imagem
        self.play(FadeOut(arrow_4, not_1, not_2))
        arrow_4.rotate(18*DEGREES)
        self.play(FadeIn(arrow_4))

        yes_1_1 = Line(UL, DR).scale(0.11)
        yes_1_2 = Line(DL, UR).scale(0.25).next_to(yes_1_1, RIGHT, aligned_edge=DOWN, buff=-0.02)
        yes_1 = VGroup(yes_1_1, yes_1_2).scale(0.75).set_color(GREEN).move_to(codomain_element_4).shift(RIGHT*0.4)

        yes_2_1 = Line(UL, DR).scale(0.11)
        yes_2_2 = Line(DL, UR).scale(0.25).next_to(yes_2_1, RIGHT, aligned_edge=DOWN, buff=-0.02)
        yes_2 = VGroup(yes_2_1, yes_2_2).scale(0.75).set_color(GREEN).move_to(arrow_4)

        self.play(codomain_element_4.animate.set_color(YELLOW))
        self.play(Succession(Create(yes_1_1, rate_func=rush_into), Create(yes_1_2, rate_func=rush_from)),
                             codomain_element_4.animate.set_color(WHITE), run_time=0.6)
        self.wait(2)


        self.play(domain_element_3.animate.set_color(YELLOW),
                  domain_element_4.animate.set_color(YELLOW))
        self.play(arrow_3.animate.set_color(YELLOW),
                  arrow_4.animate.set_color(YELLOW),
                  codomain_element_3.animate.set_color(YELLOW))
        self.play(Succession(
            Create(yes_2_1, rate_func=rush_into),
            Create(yes_2_2, rate_func=rush_from),
            run_time=0.6))
        self.play(domain_element_3.animate.set_color(WHITE),
                  domain_element_4.animate.set_color(WHITE),
                  codomain_element_3.animate.set_color(WHITE),
                  arrow_3.animate.set_color(WHITE),
                  arrow_4.animate.set_color(WHITE))
        self.wait(2)

        self.play(FadeOut(yes_1, yes_2))
        self.wait(2)



        # Função Sobrejetora

        self.play(FadeOut(function_definition))
        self.wait(2)

        t1 = Tex('Sobrejetora').scale(0.9).to_edge(UP, buff=1.15)
        ul_t1 = Underline(t1)
        ul_t1_aux = Underline(t1[0][0:5], stroke_width=ul_t1.get_stroke_width()).move_to(ul_t1, aligned_edge=LEFT).set_z_index(2)
        self.play(Succession(FadeIn(t1), Create(ul_t1)))
        self.add(ul_t1_aux)
        self.wait(2)



            # Também não sobra elemento em B
        r1_arrow_1 = CurvedArrow((-2.2, 1.2, 0), (2.2, 0.8, 0), radius = -5, stroke_width = 2.5)
        r1_arrow_2 = CurvedArrow((-2.2, 0.4, 0), (2.2, 0, 0), radius = -5, stroke_width = 2.5)
        r1_arrow_3 = CurvedArrow((-2.2, -0.4, 0), (2.2, -0.8, 0), radius = -5, stroke_width = 2.5)
        r1_arrow_4 = CurvedArrow((-2.2, -1.1, 0), (2.2, -0.8, 0), radius = -5, stroke_width = 2.5)
        r1_arrows = VGroup(r1_arrow_1, r1_arrow_2, r1_arrow_3, r1_arrow_4).scale(0.7).shift(DOWN*1.2).set_z_index(3)

        self.play(codomain_elements.animate.shift(DOWN*0.4),
                  FadeOut(codomain_element_4), function.animate.shift(DOWN*0.2),
                  ReplacementTransform(arrow_1, r1_arrow_1),
                  ReplacementTransform(arrow_2, r1_arrow_2),
                  ReplacementTransform(arrow_3, r1_arrow_3),
                  ReplacementTransform(arrow_4, r1_arrow_4))
        self.wait(2)



            # Imagem = Contradomínio
        range = Ellipse(width = 3, height = 4, color = GREEN_D, fill_opacity = 0.3).move_to(codomain).scale(0.62)
        range_label_1 = MathTex(r'= Im', color = range.get_color()).next_to(codomain_label_1, RIGHT, buff=0.25).scale(1.1)
        range_label_1[0][0].set_color(WHITE)

        self.play(FadeIn(range))
        self.play(Write(range_label_1))
        self.wait(2)

            # Comentário sobre o prefixo 'sobre-' de 'sobrejetora'
        self.play(Indicate(t1[0][0:5], scale_factor=1), Indicate(ul_t1_aux, scale_factor=1))
        #self.play(t1[0][0:5].animate.set_color(YELLOW))
        self.wait(2)
        
        t2 = Tex(r'\it ``Sobreposição"', color = GRAY).scale(0.9).next_to(t1, UP).shift(LEFT)
        self.play(FadeIn(t2))
        self.wait(2)

        self.play(Indicate(range, scale_factor=1))
        self.wait(2)
        self.play(Indicate(codomain, scale_factor=1))
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)



# Injetora
class vid3(MovingCameraScene):
    def construct(self):

        # Diagrama
                # Domínio
        domain = Ellipse(width = 3, height = 4, fill_opacity = 0.2).shift(LEFT*2.5)
        domain_label_1 = MathTex('A', color = RED).scale(1.5).next_to(domain, UP, buff = 0.3)
        
        domain_element_1 = Dot(domain.get_center()).shift(UP*1.2)
        domain_element_2 = Dot(domain.get_center()).shift(UP*0.4)
        domain_element_3 = Dot(domain.get_center()).shift(DOWN*0.4)
        domain_element_4 = Dot(domain.get_center()).shift(DOWN*1.2)
        domain_elements = VGroup(domain_element_1, domain_element_2, domain_element_3, domain_element_4)

                # Contradomínio
        codomain = Ellipse(width = 3, height = 4, color = BLUE, fill_opacity = 0.2).shift(RIGHT*2.5)
        codomain_label_1 = MathTex('B', color = BLUE).scale(1.5).next_to(codomain, UP, buff = 0.3)
        
        codomain_element_1 = Dot(codomain.get_center()).shift(UP*1.2)
        codomain_element_2 = Dot(codomain.get_center()).shift(UP*0.4)
        codomain_element_3 = Dot(codomain.get_center()).shift(DOWN*0.4)
        codomain_element_4 = Dot(codomain.get_center()).shift(DOWN*1.2)
        codomain_elements = VGroup(codomain_element_1, codomain_element_2, codomain_element_3, codomain_element_4)
                # Setas
        function = MathTex(r'f').scale(1.2).shift(UP*2.3)

        arrow_1 = CurvedArrow((-2.2, 1.2, 0), (2.2, 1.2, 0), radius = -5, stroke_width = 2.5)
        arrow_2 = CurvedArrow((-2.2, 0.4, 0), (2.2, 0.4, 0), radius = -5, stroke_width = 2.5)
        arrow_3 = CurvedArrow((-2.2, -0.4, 0), (2.2, -0.4, 0), radius = -5, stroke_width = 2.5)
        arrow_4 = CurvedArrow((-2.2, -0.4, 0), (2.2, -1.1, 0), radius = -5, stroke_width = 2.5)
        arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4)

        g_diagram = VGroup(domain, domain_label_1, domain_elements,
                           codomain, codomain_label_1, codomain_elements,
                           function, arrows).scale(0.7).shift(DOWN*1.2)
        
        domain_elements.shift(DOWN*0.4)
        function.shift(DOWN*0.2)

        r2_arrow_1 = CurvedArrow((-2.2, 0.8, 0), (2.2, 1.2, 0), radius = -5, stroke_width = 2.5)
        r2_arrow_2 = CurvedArrow((-2.2, 0, 0), (2.2, 0.4, 0), radius = -5, stroke_width = 2.5)
        r2_arrow_2_copy = CurvedArrow((-2.2, 0, 0), (2.2, 0.4, 0), radius = -5, stroke_width = 2.5)
        r2_arrow_2_aux = CurvedArrow((-2.2, 0, 0), (2.2, 1.2, 0), radius = -5, stroke_width = 2.5)
        r2_arrow_3 = CurvedArrow((-2.2, -0.8, 0), (2.2, -0.4, 0), radius = -5, stroke_width = 2.5)
        r2_arrows = VGroup(r2_arrow_1, r2_arrow_2, r2_arrow_2_copy, r2_arrow_2_aux, r2_arrow_3).scale(0.7).shift(DOWN*1.2)

        self.add(g_diagram, r2_arrows)
        self.remove(arrows, domain_element_4, r2_arrow_2_copy, r2_arrow_2_aux)

        black_sq = Square(color = BLACK, fill_opacity = 1).set_z_index(5).scale(10)
        self.add(black_sq)
        self.play(FadeOut(black_sq))



        # Função Injetora
        t1 = Tex('Injetora').scale(0.9).to_edge(UP, buff=1.15)
        ul_t1 = Underline(t1)
        self.play(Succession(FadeIn(t1), Create(ul_t1)))
        self.wait(2)

        self.play(LaggedStart(
            Flash(domain_element_1, num_lines=8),
            Flash(domain_element_2, num_lines=8),
            Flash(domain_element_3, num_lines=8),
            lag_ratio=0.2))
        
        self.wait(2)

        self.play(LaggedStart(
            Flash(codomain_element_1, num_lines=8),
            Flash(codomain_element_2, num_lines=8),
            Flash(codomain_element_3, num_lines=8),
            lag_ratio=0.2))
        

        
        # a \neq b, f(a) \neq f(b)
        
        t_a = MathTex('a', color = YELLOW).scale(1).next_to(domain, LEFT).shift(UP*1)
        line_t_a = Line(t_a, domain_element_1, color = t_a.get_color(), buff=0.15, stroke_width = 2.5)

        t_b = MathTex('b', color = t_a.get_color()).scale(1).next_to(domain, LEFT).shift(DOWN*0.35)
        line_t_b = Line(t_b, domain_element_2, color = t_a.get_color(), buff=0.15, stroke_width = 2.5)

        self.play(FadeIn(t_a, line_t_a))
        self.play(FadeIn(t_b, line_t_b))
        self.wait(2)

        t_fa = MathTex('f(a)', color = YELLOW).scale(1).next_to(codomain, RIGHT).shift(UP*1.5)
        line_t_fa = Line(t_fa.get_left(), codomain_element_1, color = t_a.get_color(), buff=0.15, stroke_width = 2.5)

        t_fb = MathTex('f(b)', color = YELLOW).scale(1).next_to(codomain, RIGHT)
        line_t_fb = Line(t_fb.get_left(), codomain_element_2, color = t_a.get_color(), buff=0.15, stroke_width = 2.5)
        line_t_fb_copy = Line(t_fb.get_left(), codomain_element_2, color = t_a.get_color(), buff=0.15, stroke_width = 2.5)
        line_t_fb_aux = Line(t_fb.get_left(), codomain_element_1, color = t_a.get_color(), buff=0.15, stroke_width = 2.5)

        self.play(FadeIn(t_fa, line_t_fa))
        self.play(FadeIn(t_fb, line_t_fb))
        self.wait(2)



        # Dois elementos de A não compartilham a mesma imagem
        not_1_1 = Line(UR, DL).scale(0.3)
        not_1_2 = Line(UL, DR).scale(0.3)
        not_1 = VGroup(not_1_1, not_1_2).scale(0.75).set_color(RED).move_to(r2_arrow_2_aux).shift(UP*0.45).set_z_index(3)

        self.play(ReplacementTransform(r2_arrow_2, r2_arrow_2_aux),
                  ReplacementTransform(line_t_fb, line_t_fb_aux))
        self.wait(2)
        self.play(Create(not_1))
        self.wait(2)
        self.play(ReplacementTransform(r2_arrow_2_aux, r2_arrow_2_copy),
                  ReplacementTransform(line_t_fb_aux, line_t_fb_copy),
                  FadeOut(not_1))
        self.wait(2)

        self.play(FadeOut(t_a, t_b, t_fa, t_fb, 
                          line_t_a, line_t_b, line_t_fa, line_t_fb_copy))
        self.wait(2)



            # Comentário sobre a palavra 'injetora'
        t2 = Tex(r'\it ``Injeção"', color = GRAY).scale(0.9).next_to(t1, UP)
        self.play(Indicate(t1, scale_factor=1), Indicate(ul_t1, scale_factor=1))
        self.play(FadeIn(t2))
        self.wait(2)

        self.play(LaggedStart(
            Flash(codomain_element_1, num_lines=8),
            Flash(codomain_element_2, num_lines=8),
            Flash(codomain_element_3, num_lines=8),
            lag_ratio=0.3))
        
        self.play(LaggedStart(
            Indicate(r2_arrow_1, scale_factor = 1.05),
            Indicate(r2_arrow_2_copy, scale_factor = 1.05),
            Indicate(r2_arrow_3, scale_factor = 1.05),
            lag_ratio=0.3))
        
        self.play(FadeIn(black_sq))
        self.wait(2)
        self.remove(t1, ul_t1, t2,
                    domain, domain_label_1, domain_element_1, domain_element_2, domain_element_3,
                    codomain, codomain_label_1, codomain_elements,
                    function, domain, 
                    r2_arrow_1, r2_arrow_2_copy, r2_arrow_3)
        self.remove(black_sq)


        # Teste da Reta Horizontal

        self.camera.frame.shift(UP)

            # Retomando o gráfico
        axes = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3)
        axes_labels = VGroup(x_label, y_label)
        axes_zero = MathTex('0').scale(0.8).next_to(axes, DL, buff = -0.7)

        graph_1 = axes.plot(lambda x: x * 1/3 + np.sin(x + 4) + 1.3,
                            x_range=[0.5, 4], stroke_width = 4).set_color(BLUE).set_z_index(2)

        self.play(FadeIn(axes, axes_labels, axes_zero, graph_1))
        self.wait(2)

        dot_intersection = Dot(graph_1.get_point_from_function(t = 2.5), color = YELLOW).set_z_index(4)
        horizontal_line_1 = Line(LEFT*1.5, RIGHT, color = dot_intersection.get_color(), stroke_opacity = 0.7).scale(2).move_to((0, dot_intersection.get_y(), 0)).set_z_index(3)
        horizontal_line_1.add_updater(lambda m: m.become(Line(LEFT*1.5, RIGHT, color = dot_intersection.get_color(), stroke_opacity = 0.7).scale(2).move_to((0, dot_intersection.get_y(), 0)).set_z_index(3)))
        self.play(Create(horizontal_line_1))
        self.wait(2)
        self.play(GrowFromCenter(dot_intersection))
        self.wait(2)
        
        arrow_x_to_fx = Arrow(dot_intersection.get_center(), axes.coords_to_point(2.5, 0.1, 0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)

        x_dot = Dot(axes.coords_to_point(2.5,0,0)).set_z_index(4)
        y_dot = Dot(axes.coords_to_point(0,2.3485,0)).set_z_index(4)

        self.play(GrowFromCenter(y_dot), Flash(y_dot, num_lines = 8))
        self.wait(2)
        self.play(GrowFromPoint(arrow_x_to_fx, arrow_x_to_fx.get_edge_center(UP)))
        self.wait(2)
        self.play(GrowFromCenter(x_dot), Flash(x_dot, num_lines = 8))
        self.wait(2)
        self.play(FadeOut(x_dot, y_dot, arrow_x_to_fx))
        self.wait(2)

        h_line_test_text = Tex('\it Teste da Reta Horizontal', color = YELLOW).move_to(t1).shift(UP)
        self.play(FadeIn(h_line_test_text))
        self.wait(2)

        self.add(axes, axes_labels, axes_zero, graph_1, horizontal_line_1, h_line_test_text)

        graph_1_aux_1 = axes.plot(lambda x: x * 1/3 + np.sin(x + 4) + 1.3,
                            x_range=[2.5, 4], stroke_width = 4).set_color(BLUE).set_z_index(2)
        self.play(MoveAlongPath(dot_intersection, graph_1_aux_1), run_time = 1.5)
        graph_1.reverse_points()
        self.play(MoveAlongPath(dot_intersection, graph_1), run_time = 4)
        self.wait(2)

        # Mostrando as funções são injetoras ou não
        its_injective_text = Tex('É injetora', color = GREEN).scale(0.8).shift(UP*2.7)
        not_injective_text = Tex('Não é injetora', color = RED).scale(0.8).shift(UP*2.7)
        
            # É injetora
        self.play(FadeIn(its_injective_text))
        self.wait(2)
        self.remove(its_injective_text, graph_1, horizontal_line_1, dot_intersection)
        self.wait(2)

            # Não é injetora
        graph_2 = axes.plot(lambda x: -(x-2) ** 2 + 3.5,
                            x_range=[-0.1, 4.1], stroke_width = 4).set_color(BLUE).set_z_index(2)
        graph_2_aux1 = axes.plot(lambda x: -(x-2) ** 2 + 3.5,
                            x_range=[2, 4], stroke_width = 4).set_color(BLUE).set_z_index(2)
        graph_2_aux2 = axes.plot(lambda x: -(x-2) ** 2 + 3.5,
                            x_range=[0, 2], stroke_width = 4).set_color(BLUE).set_z_index(2)
        graph_2_aux2.reverse_points()
        self.play(FadeIn(graph_2))
        self.wait(2)

        dot_intersection_2 = Dot(graph_2.get_point_from_function(t = 2), color = YELLOW).set_z_index(4)
        dot_intersection_2_copy = Dot(graph_2.get_point_from_function(t = 2), color = YELLOW).set_z_index(4)
        horizontal_line_2 = Line(LEFT*1.5, RIGHT, color = dot_intersection_2.get_color(), stroke_opacity = 0.7).scale(2).move_to((0, dot_intersection_2.get_y(), 0)).set_z_index(3)
        horizontal_line_2.add_updater(lambda m: m.become(Line(LEFT*1.5, RIGHT, color = dot_intersection_2.get_color(), stroke_opacity = 0.7).scale(2).move_to((0, dot_intersection_2.get_y(), 0)).set_z_index(3)))
        
        self.play(Create(horizontal_line_2), GrowFromCenter(dot_intersection_2))
        self.add(dot_intersection_2_copy)
        self.play(MoveAlongPath(dot_intersection_2, graph_2_aux1),
            MoveAlongPath(dot_intersection_2_copy, graph_2_aux2),
            run_time = 3.5)
        self.play(FadeIn(not_injective_text))
        self.wait(2)

        graph_2_aux3 = axes.plot(lambda x: -(x-2) ** 2 + 3.5,
                            x_range=[3, 4], stroke_width = 4).set_color(BLUE).set_z_index(2)
        graph_2_aux3.reverse_points()
        graph_2_aux4 = axes.plot(lambda x: -(x-2) ** 2 + 3.5,
                            x_range=[0, 1], stroke_width = 4).set_color(BLUE).set_z_index(2)
        self.play(MoveAlongPath(dot_intersection_2, graph_2_aux3),
                  MoveAlongPath(dot_intersection_2_copy, graph_2_aux4),
                  run_time = 2)
        self.wait(2)

        arrow_x_to_fx_2 = Arrow(dot_intersection_2.get_center(), axes.coords_to_point(3,0.1,0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)
        arrow_x_to_fx_3 = Arrow(dot_intersection_2_copy.get_center(), axes.coords_to_point(1,0.1,0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)

        x_dot_2 = Dot(axes.coords_to_point(1,0,0)).set_z_index(4)
        x_dot_3 = Dot(axes.coords_to_point(3,0,0)).set_z_index(4)
        y_dot_2 = Dot(axes.coords_to_point(0,2.5,0)).set_z_index(4)

        self.play(GrowFromCenter(y_dot_2), Flash(y_dot_2, num_lines = 8))
        self.wait(2)
        self.play(Create(arrow_x_to_fx_2), 
                  Create(arrow_x_to_fx_3))
        self.wait(2)
        self.play(GrowFromCenter(x_dot_2), Flash(x_dot_2, num_lines = 8),
                  GrowFromCenter(x_dot_3), Flash(x_dot_3, num_lines = 8))
        self.wait(2)
        self.play(FadeIn(black_sq))
        self.wait(2)



# Bijetora
class vid4(Scene):
    def construct(self):

        # Diagrama
                # Domínio
        domain = Ellipse(width = 3, height = 4, fill_opacity = 0.2).shift(LEFT*2.5)
        domain_label_1 = MathTex('A', color = RED).scale(1.5).next_to(domain, UP, buff = 0.3)
        
        domain_element_1 = Dot(domain.get_center()).shift(UP*1.2)
        domain_element_2 = Dot(domain.get_center()).shift(UP*0.4)
        domain_element_3 = Dot(domain.get_center()).shift(DOWN*0.4)
        domain_element_4 = Dot(domain.get_center()).shift(DOWN*1.2)
        domain_elements = VGroup(domain_element_1, domain_element_2, domain_element_3, domain_element_4)

                # Contradomínio
        codomain = Ellipse(width = 3, height = 4, color = BLUE, fill_opacity = 0.2).shift(RIGHT*2.5)
        codomain_label_1 = MathTex('B', color = BLUE).scale(1.5).next_to(codomain, UP, buff = 0.3)
        
        codomain_element_1 = Dot(codomain.get_center()).shift(UP*1.2)
        codomain_element_2 = Dot(codomain.get_center()).shift(UP*0.4)
        codomain_element_3 = Dot(codomain.get_center()).shift(DOWN*0.4)
        codomain_element_4 = Dot(codomain.get_center()).shift(DOWN*1.2)
        codomain_elements = VGroup(codomain_element_1, codomain_element_2, codomain_element_3, codomain_element_4)
        
                # Setas
        function = MathTex(r'f').scale(1.2).shift(UP*2.3)

        arrow_1 = CurvedArrow((-2.2, 1.2, 0), (2.2, 1.2, 0), radius = -5, stroke_width = 2.5)
        arrow_2 = CurvedArrow((-2.2, 0.4, 0), (2.2, 0.4, 0), radius = -5, stroke_width = 2.5)
        arrow_3 = CurvedArrow((-2.2, -0.4, 0), (2.2, -0.4, 0), radius = -5, stroke_width = 2.5)
        arrow_4 = CurvedArrow((-2.2, -1.2, 0), (2.2, -1.2, 0), radius = -5, stroke_width = 2.5)
        arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4).set_z_index(5)

        g_diagram = VGroup(domain, domain_label_1, domain_elements,
                           codomain, codomain_label_1, codomain_elements,
                           function, arrows).scale(0.7).shift(DOWN*1.2)

        self.play(FadeIn(g_diagram))

        t1 = Tex('Bijetora').scale(0.9).to_edge(UP, buff=1.15)
        ul_t1 = Underline(t1)
        self.play(Succession(FadeIn(t1), Create(ul_t1)))
        self.wait(2)

        t2 = Tex('Sobrejetora').scale(0.9)
        t3 = Tex('+').scale(0.9)
        t4 = Tex('Injetora').scale(0.9)
        g1 = VGroup(t2, t3, t4).arrange(DOWN)

        brace1 = Brace(g1, LEFT)

        g2 = VGroup(g1, brace1).next_to(t1, RIGHT)
        self.play(FadeIn(g2))
        self.wait(2)

        range = Ellipse(width = 3, height = 4, color = GREEN_D, fill_opacity = 0.3).move_to(codomain).scale(0.62)
        range_label_1 = MathTex(r'= Im', color = range.get_color()).next_to(codomain_label_1, RIGHT, buff=0.25).scale(1.1)
        range_label_1[0][0].set_color(WHITE)

        self.play(FadeIn(range), t2.animate.set_color(YELLOW))
        self.play(Write(range_label_1))
        self.play(t2.animate.set_color(WHITE))
        self.wait(2)

        t_a = MathTex('a', color = YELLOW).scale(1).next_to(domain, LEFT).shift(UP*0.5)
        line_t_a = Line(t_a, domain_element_2, color = t_a.get_color(), buff=0.15, stroke_width = 2.5)

        t_b = MathTex('b', color = t_a.get_color()).scale(1).next_to(domain, LEFT).shift(DOWN*0.45)
        line_t_b = Line(t_b, domain_element_3, color = t_a.get_color(), buff=0.15, stroke_width = 2.5)

        t_fa = MathTex('f(a)', color = YELLOW).scale(1).next_to(codomain, RIGHT).shift(UP*0.5)
        line_t_fa = Line(t_fa.get_left(), codomain_element_2, color = t_a.get_color(), buff=0.15, stroke_width = 2.5)

        t_fb = MathTex('f(b)', color = YELLOW).scale(1).next_to(codomain, RIGHT).shift(DOWN*0.45)
        line_t_fb = Line(t_fb.get_left(), codomain_element_3, color = t_a.get_color(), buff=0.15, stroke_width = 2.5)

        self.play(t4.animate.set_color(YELLOW))
        self.play(LaggedStart(
            FadeIn(t_a, line_t_a),
            FadeIn(t_b, line_t_b),
            lag_ratio=0.1))
        self.wait(2)
        self.play(LaggedStart(
            FadeIn(t_fa, line_t_fa),
            FadeIn(t_fb, line_t_fb),
            lag_ratio=0.1))
        self.wait(2)
        self.play(FadeOut(t_a, t_b, t_fa, t_fb,
                          line_t_a, line_t_b, line_t_fa, line_t_fb),
                  t4.animate.set_color(WHITE))
        self.wait(2)

        black_sq = Square(color = BLACK, fill_opacity = 1).set_z_index(5).scale(10)
        self.play(FadeIn(black_sq))
        self.wait(2)



# Exemplos de funções sobrejetora / injetora / bijetora
class vid5(MovingCameraScene):
    def construct(self):

        # Diagrama 1

                # Domínio
        domain_i = Ellipse(width = 3, height = 4, fill_opacity = 0.2, stroke_width = 2.5).shift(LEFT*2.5)
        domain_label_1_i = MathTex('C', color = RED).scale(1.5).next_to(domain_i, UP, buff = 0.3)
        
        domain_element_1_i = Dot(domain_i.get_center()).shift(UP*1.2)
        domain_element_2_i = Dot(domain_i.get_center()).shift(UP*0.4)
        domain_element_3_i = Dot(domain_i.get_center()).shift(DOWN*0.4)
        domain_element_4_i = Dot(domain_i.get_center()).shift(DOWN*1.2)
        domain_elements_i = VGroup(domain_element_1_i, domain_element_2_i, domain_element_3_i, domain_element_4_i)
        
                # Contradomínio
        codomain_i = Ellipse(width = 3, height = 4, color = BLUE, fill_opacity = 0.2, stroke_width = 2.5).shift(RIGHT*2.5)
        codomain_label_1_i = MathTex('D', color = BLUE).scale(1.5).next_to(codomain_i, UP, buff = 0.3)
        
        codomain_element_1_i = Dot(codomain_i.get_center()).shift(UP*0.7)
        codomain_element_4_i = Dot(codomain_i.get_center()).shift(DOWN*0.7)
        codomain_elements_i = VGroup(codomain_element_1_i, codomain_element_4_i)

        arrow_1_i = CurvedArrow((-2.2, 1.2, 0), (2.2, 0.7, 0), radius = -5, stroke_width = 2.5)
        arrow_2_i = CurvedArrow((-2.2, 0.4, 0), (2.2, 0.7, 0), radius = -5, stroke_width = 2.5)
        arrow_3_i = CurvedArrow((-2.2, -0.4, 0), (2.2, -0.7, 0), radius = -5, stroke_width = 2.5)
        arrow_4_i = CurvedArrow((-2.2, -1.2, 0), (2.2, -0.7, 0), radius = -5, stroke_width = 2.5)
        arrows_i = VGroup(arrow_1_i, arrow_2_i, arrow_3_i, arrow_4_i)

        range_i = Ellipse(width = 3, height = 4, color = GREEN_D, fill_opacity = 0.3, stroke_width = 2.5).move_to(codomain_i).scale(0.85)
        range_label_1_i = MathTex(r'Im', color = range_i.get_color()).next_to(range_i, UR, buff=-0.7).scale(1.1).set_z_index(4)
        range_label_2_i = MathTex(r'Im', color = BLACK, stroke_width = 4).move_to(range_label_1_i).scale(1.1).set_z_index(3)
        range_label_i = VGroup(range_label_1_i, range_label_2_i)

        rectangle_i_aux = VGroup(domain_i, domain_label_1_i, domain_elements_i,
                           codomain_i, codomain_label_1_i, codomain_elements_i,
                           arrows_i)
        rectangle_i = SurroundingRectangle(rectangle_i_aux, buff = 0.3, color = GRAY, stroke_width = 2)

        g_diagram_i = VGroup(domain_i, domain_label_1_i, domain_elements_i,
                           codomain_i, codomain_label_1_i, codomain_elements_i,
                           arrows_i, rectangle_i, range_i, range_label_i).scale(0.7).shift(DOWN*1.2)
            


        # Diagrama 2

                # Domínio
        domain_ii = Ellipse(width = 3, height = 4, fill_opacity = 0.2, stroke_width = 2.5).shift(LEFT*2.5)
        domain_label_1_ii = MathTex('A', color = RED).scale(1.5).next_to(domain_ii, UP, buff = 0.3)
        
        domain_element_1_ii = Dot(domain_ii.get_center()).shift(UP*1.2)
        domain_element_2_ii = Dot(domain_ii.get_center()).shift(UP*0.4)
        domain_element_3_ii = Dot(domain_ii.get_center()).shift(DOWN*0.4)
        domain_elements_ii = VGroup(domain_element_1_ii, domain_element_2_ii, domain_element_3_ii)
        domain_elements_ii.shift(DOWN*0.4)

                # Contradomínio
        codomain_ii = Ellipse(width = 3, height = 4, color = BLUE, fill_opacity = 0.2, stroke_width = 2.5).shift(RIGHT*2.5)
        codomain_label_1_ii = MathTex('B', color = BLUE).scale(1.5).next_to(codomain_ii, UP, buff = 0.3)
        
        codomain_element_1_ii = Dot(codomain_ii.get_center()).shift(UP*1.2)
        codomain_element_2_ii = Dot(codomain_ii.get_center()).shift(UP*0.4)
        codomain_element_3_ii = Dot(codomain_ii.get_center()).shift(DOWN*0.4)
        codomain_element_4_ii = Dot(codomain_ii.get_center()).shift(DOWN*1.2)
        codomain_elements_ii = VGroup(codomain_element_1_ii, codomain_element_2_ii, codomain_element_3_ii, codomain_element_4_ii)

        arrow_1_ii = CurvedArrow((-2.2, 0.8, 0), (2.2, 1.2, 0), radius = -5, stroke_width = 2.5)
        arrow_2_ii = CurvedArrow((-2.2, 0, 0), (2.2, 0.4, 0), radius = -5, stroke_width = 2.5)
        arrow_3_ii = CurvedArrow((-2.2, -0.8, 0), (2.2, -1.2, 0), radius = -5, stroke_width = 2.5)
        arrows_ii = VGroup(arrow_1_ii, arrow_2_ii, arrow_3_ii)

        rectangle_ii_aux = VGroup(domain_ii, domain_label_1_ii, domain_elements_ii,
                           codomain_ii, codomain_label_1_ii, codomain_elements_ii,
                           arrows_ii)
        rectangle_ii = SurroundingRectangle(rectangle_ii_aux, buff = 0.3, color = GRAY, stroke_width = 2)

        g_diagram_ii = VGroup(domain_ii, domain_label_1_ii, domain_elements_ii,
                           codomain_ii, codomain_label_1_ii, codomain_elements_ii,
                           arrows_ii, rectangle_ii).scale(0.7).shift(DOWN*1.2)
        


        # Diagrama 3

                # Domínio
        domain_iii = Ellipse(width = 3, height = 4, fill_opacity = 0.2, stroke_width = 2.5).shift(LEFT*2.5)
        domain_label_1_iii = MathTex('E', color = RED).scale(1.5).next_to(domain_iii, UP, buff = 0.3)
        
        domain_element_1_iii = Dot(domain_iii.get_center()).shift(UP*1.2)
        domain_element_2_iii = Dot(domain_iii.get_center()).shift(UP*0.4)
        domain_element_3_iii = Dot(domain_iii.get_center()).shift(DOWN*0.4)
        domain_elements_iii = VGroup(domain_element_1_iii, domain_element_2_iii, domain_element_3_iii)
        domain_elements_iii.shift(DOWN*0.4)

                # Contradomínio
        codomain_iii = Ellipse(width = 3, height = 4, color = BLUE, fill_opacity = 0.2, stroke_width = 2.5).shift(RIGHT*2.5)
        codomain_label_1_iii = MathTex('F', color = BLUE).scale(1.5).next_to(codomain_iii, UP, buff = 0.3)
        
        codomain_element_1_iii = Dot(codomain_iii.get_center()).shift(UP*1.2)
        codomain_element_2_iii = Dot(codomain_iii.get_center()).shift(UP*0.4)
        codomain_element_3_iii = Dot(codomain_iii.get_center()).shift(DOWN*0.4)
        codomain_elements_iii = VGroup(codomain_element_1_iii, codomain_element_2_iii, codomain_element_3_iii)
        codomain_elements_iii.shift(DOWN*0.4)

        arrow_1_iii = CurvedArrow((-2.2, 1.2, 0), (2.2, 1.2, 0), radius = -5, stroke_width = 2.5)
        arrow_2_iii = CurvedArrow((-2.2, 0.4, 0), (2.2, 0.4, 0), radius = -5, stroke_width = 2.5)
        arrow_3_iii = CurvedArrow((-2.2, -0.4, 0), (2.2, -0.4, 0), radius = -5, stroke_width = 2.5)
        arrows_iii = VGroup(arrow_1_iii, arrow_2_iii, arrow_3_iii)
        arrows_iii.shift(DOWN*0.4)

        range_iii = Ellipse(width = 3, height = 4, color = GREEN_D, fill_opacity = 0.3, stroke_width = 2.5).move_to(codomain_iii).scale(0.85)
        range_label_1_iii = MathTex(r'Im', color = range_i.get_color()).next_to(range_iii, UR, buff=-0.7).scale(1.1).set_z_index(4)
        range_label_2_iii = MathTex(r'Im', color = BLACK, stroke_width = 4).move_to(range_label_1_iii).scale(1.1).set_z_index(3)
        range_label_iii = VGroup(range_label_1_iii, range_label_2_iii)

        rectangle_iii_aux = VGroup(domain_iii, domain_label_1_iii, domain_elements_iii,
                           codomain_iii, codomain_label_1_iii, codomain_elements_iii,
                           arrows_iii)
        rectangle_iii = SurroundingRectangle(rectangle_iii_aux, buff = 0.3, color = GRAY, stroke_width = 2)

        g_diagram_iii = VGroup(domain_iii, domain_label_1_iii, domain_elements_iii,
                           codomain_iii, codomain_label_1_iii, codomain_elements_iii,
                           arrows_iii, rectangle_iii, range_iii, range_label_iii).scale(0.7).shift(DOWN*1.2)
        


        diagrams = VGroup(g_diagram_ii, g_diagram_i, g_diagram_iii).arrange(RIGHT).scale(0.65).move_to(ORIGIN)

        

        # Checkboxes

            # Checkboxes diagrama 1
        checkbox_1_i = Square(side_length=1, stroke_width = 2.5, color = GRAY).scale(0.4)
        checkbox_text_1_i = Tex('Sobrejetora').next_to(checkbox_1_i, RIGHT)
        g_checkbox_1_i = VGroup(checkbox_1_i, checkbox_text_1_i).scale(0.5)

        checkbox_2_i = Square(side_length=1, stroke_width = 2.5, color = GRAY).scale(0.4)
        checkbox_text_2_i = Tex('Injetora').next_to(checkbox_2_i, RIGHT)
        g_checkbox_2_i = VGroup(checkbox_2_i, checkbox_text_2_i).scale(0.5).next_to(checkbox_1_i, DOWN, aligned_edge=LEFT)

        yes_i = Tex(r'\checkmark').set_color(GREEN).scale(0.9).move_to(checkbox_1_i).shift(UP*0.1+RIGHT*0.07)    
        not_i = Line((-1,0,0), (1,-0,0), stroke_width = 2.5, color = RED).scale(0.7).move_to(g_checkbox_2_i)
        checkboxes_i = VGroup(g_checkbox_1_i, g_checkbox_2_i, yes_i, not_i).next_to(g_diagram_i, UP)



            # Checkboxes diagrama 2
        checkbox_1_ii = Square(side_length=1, stroke_width = 2.5, color = GRAY).scale(0.4)
        checkbox_text_1_ii = Tex('Sobrejetora').next_to(checkbox_1_ii, RIGHT)
        g_checkbox_1_ii = VGroup(checkbox_1_ii, checkbox_text_1_ii).scale(0.5)

        checkbox_2_ii = Square(side_length=1, stroke_width = 2.5, color = GRAY).scale(0.4)
        checkbox_text_2_ii = Tex('Injetora').next_to(checkbox_2_ii, RIGHT)
        g_checkbox_2_ii = VGroup(checkbox_2_ii, checkbox_text_2_ii).scale(0.5).next_to(checkbox_1_ii, DOWN, aligned_edge=LEFT)

        yes_ii = Tex(r'\checkmark').set_color(GREEN).scale(0.9).move_to(checkbox_2_ii).shift(UP*0.1+RIGHT*0.07)    
        not_ii = Line((-1,0,0), (1,-0,0), stroke_width = 2.5, color = RED).scale(0.9).move_to(g_checkbox_1_ii)
        checkboxes_ii = VGroup(g_checkbox_1_ii, g_checkbox_2_ii, yes_ii, not_ii).next_to(g_diagram_ii, UP)



            # Checkboxes diagrama 3
        checkbox_1_iii = Square(side_length=1, stroke_width = 2.5, color = GRAY).scale(0.4)
        checkbox_text_1_iii = Tex('Sobrejetora').next_to(checkbox_1_iii, RIGHT)
        g_checkbox_1_iii = VGroup(checkbox_1_iii, checkbox_text_1_iii).scale(0.5)

        checkbox_2_iii = Square(side_length=1, stroke_width = 2.5, color = GRAY).scale(0.4)
        checkbox_text_2_iii = Tex('Injetora').next_to(checkbox_2_iii, RIGHT)
        g_checkbox_2_iii = VGroup(checkbox_2_iii, checkbox_text_2_iii).scale(0.5).next_to(checkbox_1_iii, DOWN, aligned_edge=LEFT)

        checkbox_3_iii = Square(side_length=1, stroke_width = 2.5, color = GRAY).scale(0.4)
        checkbox_text_3_iii = Tex('Bijetora').next_to(checkbox_3_iii, RIGHT)
        g_checkbox_3_iii = VGroup(checkbox_3_iii, checkbox_text_3_iii).scale(0.5).next_to(g_checkbox_1_iii, DOWN*0.035, aligned_edge=LEFT)


        yes_1_iii = Tex(r'\checkmark').set_color(GREEN).scale(0.9).move_to(checkbox_1_iii).shift(UP*0.1+RIGHT*0.07)    
        yes_2_iii = Tex(r'\checkmark').set_color(GREEN).scale(0.9).move_to(checkbox_2_iii).shift(UP*0.1+RIGHT*0.07)    
        yes_3_iii = Tex(r'\checkmark').set_color(GREEN).scale(0.9).move_to(checkbox_3_iii).shift(UP*0.1+RIGHT*0.07)    
        checkboxes_iii = VGroup(g_checkbox_1_iii, g_checkbox_2_iii, g_checkbox_3_iii, yes_1_iii, yes_2_iii, yes_3_iii).next_to(g_diagram_iii, UP)
        
        
        
        checkboxes = VGroup(checkboxes_i, checkboxes_ii, checkboxes_iii)



        # FadeIn dos 3 diagramas (ii / i / iii)
        self.play(LaggedStart(
            FadeIn(g_diagram_ii),
            FadeIn(domain_i, domain_label_1_i, domain_elements_i,
                   codomain_i, codomain_label_1_i, codomain_elements_i,
                   arrows_i, rectangle_i),
            FadeIn(domain_iii, domain_label_1_iii, domain_elements_iii,
                   codomain_iii, codomain_label_1_iii, codomain_elements_iii,
                   arrows_iii, rectangle_iii),
            lag_ratio=0.3))
        self.wait(2)



        # Zoom no diagrama 1 (ii)
        black_rectangle_1 = Rectangle(width=rectangle_i.get_width(), height=rectangle_i.get_height()*2, color=BLACK, fill_opacity=0.8, stroke_opacity=0.8).scale(1.025).set_z_index(5)
        black_rectangle_2 = black_rectangle_1.copy()
        black_rectangle_3 = black_rectangle_1.copy()

        self.camera.frame.save_state() # salva a posição da câmera

        black_rectangle_1.move_to(rectangle_i)  # No digrama 2
        black_rectangle_2.move_to(rectangle_iii)    # No digrama 3
        black_rectangle_3.move_to(rectangle_ii)    # No digrama 1       
        self.play(self.camera.frame.animate.scale(0.6).move_to(rectangle_ii).shift(UP*0.5),
                  FadeIn(black_rectangle_1, black_rectangle_2))
        self.wait(2)

        # Marcar checkboxes
        self.play(FadeIn(g_checkbox_2_ii))
        self.wait(2)
        self.play(Create(yes_ii))
        self.wait(2)

        self.play(FadeIn(g_checkbox_1_ii))
        self.wait(2)
        self.play(Create(not_ii))
        self.wait(2)



        # Vai para o diagrama 2 (i)
        self.play(FadeOut(black_rectangle_1),
                  FadeIn(black_rectangle_3),
                  self.camera.frame.animate.move_to(rectangle_i).shift(UP*0.5))
        self.wait(2)

        # Marcar checkboxes
        self.play(FadeIn(g_checkbox_1_i))
        self.wait(2)
        self.play(Create(yes_i))
        self.wait(2)

        self.play(FadeIn(g_checkbox_2_i))
        self.wait(2)
        self.play(Create(not_i))
        self.wait(2)

        
        
        # Vai para o diagrama 3 (iii)
        self.play(FadeOut(black_rectangle_2),
                  FadeIn(black_rectangle_1),
                  self.camera.frame.animate.move_to(rectangle_iii).shift(UP*0.5))
        self.wait(2)

        # Marcar checkboxes
        self.play(FadeIn(g_checkbox_1_iii))
        self.wait(2)
        self.play(Create(yes_1_iii))
        self.wait(2)

        self.play(FadeIn(g_checkbox_2_iii))
        self.wait(2)
        self.play(Create(yes_2_iii))
        self.wait(2)

        # Substitui os boxes 'sobrejetora / injetora' por 'bijetora'
        g1_aux = VGroup(g_checkbox_1_iii, yes_1_iii,
                        g_checkbox_2_iii, yes_2_iii)
        g2_aux = VGroup(g_checkbox_3_iii, yes_3_iii).shift(UP*2)
        self.play(Succession(
            g1_aux.animate.shift(UP*2),
            g2_aux.animate.shift(DOWN*2)))
        self.remove(g1_aux)
        self.wait(2)

        # Tira o zoom
        self.play(Restore(self.camera.frame),
                  FadeOut(black_rectangle_1, black_rectangle_3))
        self.wait(2)



# Função constante
class vid6(Scene):
    def construct(self):

        # Título
        t1 = Tex('Função Constante').to_edge(UP, buff=1.2).set_z_index(6)
        ul_t1 = Underline(t1).set_z_index(6)
        ul_t1_aux = Underline(t1[0][8:17], stroke_width=ul_t1.get_stroke_width()).move_to(ul_t1, aligned_edge=RIGHT).set_z_index(7)
        self.play(Succession(FadeIn(t1), Create(ul_t1)))
        self.add(ul_t1_aux)
        self.wait(2)



        # Diagrama

                # Domínio
        domain_i = Ellipse(width = 3, height = 4, fill_opacity = 0.2, stroke_width = 2.5).shift(LEFT*2.5)
        domain_label_1_i = MathTex('A', color = RED).scale(1.5).next_to(domain_i, UP, buff = 0.3)
        
        domain_element_1_i = Dot(domain_i.get_center()).shift(UP*1.2)
        domain_element_2_i = Dot(domain_i.get_center()).shift(UP*0.4)
        domain_element_3_i = Dot(domain_i.get_center()).shift(DOWN*0.4)
        domain_elements_i = VGroup(domain_element_1_i, domain_element_2_i, domain_element_3_i)
        domain_elements_i.shift(DOWN*0.4)

                # Contradomínio
        codomain_i = Ellipse(width = 3, height = 4, color = BLUE, fill_opacity = 0.2, stroke_width = 2.5).shift(RIGHT*2.5)
        codomain_label_1_i = MathTex('B', color = BLUE).scale(1.5).next_to(codomain_i, UP, buff = 0.3)
        
        codomain_element_1_i = Dot(codomain_i.get_center())
        codomain_elements_i = VGroup(codomain_element_1_i)

        arrow_1_i = CurvedArrow((-2.2, 0.8, 0), (2.2, 0, 0), radius = -5, stroke_width = 2.5)
        arrow_2_i = CurvedArrow((-2.2, 0, 0), (2.2, 0, 0), radius = -5, stroke_width = 2.5)
        arrow_3_i = CurvedArrow((-2.2, -0.8, 0), (2.2, 0, 0), radius = -5, stroke_width = 2.5)
        arrows_i = VGroup(arrow_1_i, arrow_2_i, arrow_3_i)

        range_i = Ellipse(width = 3, height = 4, color = GREEN_D, fill_opacity = 0.3, stroke_width = 2.5).move_to(codomain_i).scale(0.85)
        range_label_1_i = MathTex(r'Im', color = range_i.get_color()).next_to(range_i, UR, buff=-0.7).scale(1.1).set_z_index(4)
        range_label_2_i = MathTex(r'Im', color = BLACK, stroke_width = 4).move_to(range_label_1_i).scale(1.1).set_z_index(3)
        range_label_i = VGroup(range_label_1_i, range_label_2_i)

        rectangle_i_aux = VGroup(domain_i, domain_label_1_i, domain_elements_i,
                           codomain_i, codomain_label_1_i, codomain_elements_i,
                           arrows_i)
        rectangle_i = SurroundingRectangle(rectangle_i_aux, buff = 0.3, color = GRAY, stroke_width = 2)

        g_diagram_i = VGroup(domain_i, domain_label_1_i, domain_elements_i,
                           codomain_i, codomain_label_1_i, codomain_elements_i,
                           arrows_i).scale(0.7).shift(DOWN*1.2)
        
        self.play(FadeIn(domain_i, domain_label_1_i, domain_elements_i,
                         codomain_i, codomain_label_1_i, codomain_elements_i))
        self.wait(2)
        self.play(Create(arrows_i), run_time=2)
        self.wait(2)



        # Fórmula algébrica da função e exemplos
        function = MathTex('f(x) = k').scale(0.8).shift(UP*0.7).set_z_index(6)
        self.play(Write(function))
        self.wait(2)

        function_ex_1 = MathTex('f(x) = 2', color = GRAY).scale(0.8).next_to(function, UP).set_z_index(6)
        function_ex_2 = MathTex('f(x) = -1', color = GRAY).scale(0.8).next_to(function, UP).set_z_index(6)
        function_ex_3 = MathTex(r'f(x) = \pi', color = GRAY).scale(0.8).next_to(function, UP).set_z_index(6)
        self.play(FadeIn(function_ex_1))
        self.wait(2)
        self.play(Succession(
            FadeOut(function_ex_1),
            FadeIn(function_ex_2)))
        self.wait(2)
        self.play(Succession(
            FadeOut(function_ex_2),
            FadeIn(function_ex_3)))
        self.wait(2)
        self.play(FadeOut(function_ex_3))
        self.wait(2)



        # Comentário sobre o nome 'constante'
        self.play(Indicate(t1[0][8:17], scale_factor=1),
                  Indicate(ul_t1_aux, scale_factor=1))
        self.wait(2)

        black_sq = Square(color = BLACK, fill_opacity = 1).set_z_index(5).scale(10)
        self.play(FadeIn(black_sq), function.animate.shift(RIGHT+DOWN).set_color(BLUE))
        self.wait(2)



        # Gráfico da função constante
        axes = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3)
        axes_labels = VGroup(x_label, y_label)
        axes_zero = MathTex('0').scale(0.8).next_to(axes, DL, buff = -0.7)

        graph_1 = axes.plot(lambda x: 2,
                            x_range=[-1, 5], stroke_width = 4).set_color(BLUE)
        
        k_label = MathTex('k', color = BLUE).scale(0.9).next_to(axes.coords_to_point(0,2,0), UL*0.5)

        dots = VGroup(*[Dot(axes.coords_to_point(0.3*i - 1, 0, 0), color=YELLOW) for i in range(21)])
        dots_y_dashedlines = VGroup(*[DashedLine(axes.coords_to_point(0.3*i - 1, 0, 0), axes.coords_to_point(0.3*i - 1, 2, 0), color=GRAY).set_opacity(0.5) for i in range(21)])
        
        g_graph = VGroup(axes, axes_labels, axes_zero, graph_1, k_label, dots, dots_y_dashedlines).shift(DOWN).set_z_index(6)
                
        
        
        self.play(FadeIn(axes, axes_labels, axes_zero))
        self.wait(2)
        self.play(Create(graph_1), FadeIn(k_label))
        self.wait(2)
        self.play(Create(dots), Create(dots_y_dashedlines), run_time = 3)
        self.wait(2)
        self.play(FadeOut(dots, dots_y_dashedlines))
        self.wait(2)
        



# Crescente / Decrescente
class vid7(Scene):
    def construct(self):

        # Crescente

            # Título
        t1 = Tex('Crescente').scale(1.1).to_edge(UP)
        ul_t1 = Underline(t1)



            # Gráfico
        axes = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3)
        axes_labels = VGroup(x_label, y_label)
        axes_zero = MathTex('0').scale(0.8).next_to(axes, DL, buff = -0.7)

        graph_1 = axes.plot(lambda x: 1.4 ** x, x_range=[-1, 4.5], stroke_width = 4).set_color(BLUE)
        
        g_graph = VGroup(axes, axes_labels, axes_zero, graph_1).scale(0.9).shift(DOWN*1.7)

        

            # Elementos para a explicação
        dot_1 = Dot(axes.coords_to_point(1,1.4,0), color=YELLOW)
        dot_2 = Dot(axes.coords_to_point(3.5,3.247,0), color=dot_1.get_color())

        
        x_arrow = Arrow(LEFT, RIGHT, color = YELLOW).set_opacity(0.7).scale(1.3).move_to(dot_1, aligned_edge=LEFT).set_z_index(-1)
        y_arrow = Arrow(DOWN, UP, color = x_arrow.get_color()).set_opacity(0.7).scale(0.87).move_to(dot_2, aligned_edge=UP).shift(DOWN*0.15).set_z_index(-1)

        x_arrow_label = MathTex('x', color = x_arrow.get_color()).scale(0.9).next_to(x_arrow, DOWN, buff = 0)
        y_arrow_label = MathTex('y', color = x_arrow.get_color()).scale(0.9).next_to(y_arrow, RIGHT, buff = 0)

        

        a_dashedline = always_redraw(lambda: DashedLine((dot_1.get_x(), dot_1.get_y(), 0), (dot_1.get_x(), axes.get_x_axis().get_y(), 0), color = YELLOW, stroke_opacity=0.7))
        a_label = MathTex('a', color = YELLOW).scale(0.9).next_to(a_dashedline, DOWN, buff = 0.2)

        b_dashedline = always_redraw(lambda: DashedLine((dot_2.get_x(), dot_2.get_y(), 0), (dot_2.get_x(), axes.get_x_axis().get_y(), 0), color = YELLOW, stroke_opacity=0.7))
        b_label = MathTex('b', color = a_label.get_color()).scale(0.9).next_to(b_dashedline, DOWN, buff = 0.2)


        fa_dashedline = always_redraw(lambda: DashedLine((dot_1.get_x(), dot_1.get_y(), 0), (axes.get_y_axis().get_x(), dot_1.get_y(), 0), color = YELLOW, stroke_opacity=0.7))
        fa_label = MathTex('f(a)', color = YELLOW).scale(0.8).next_to(fa_dashedline, LEFT, buff = 0.2)

        fb_dashedline = always_redraw(lambda: DashedLine((dot_2.get_x(), dot_2.get_y(), 0), (axes.get_y_axis().get_x(), dot_2.get_y(), 0), color = YELLOW, stroke_opacity=0.7))
        fb_label = MathTex('f(b)', color = YELLOW).scale(0.8).next_to(fb_dashedline, LEFT, buff = 0.2)

    

            # Definição da função crescente
        def_increasing = MathTex(r'b > a \:\:\Rightarrow\:\: f(b) > f(a)').scale(0.9).next_to(g_graph, UP, buff = 1)
        def_increasing_rectangle = SurroundingRectangle(def_increasing, buff=0.15, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-1)
        
        


        g_increasing_function_aux = VGroup(t1, ul_t1, g_graph, dot_1, dot_2,
                                           x_arrow, y_arrow, x_arrow_label, y_arrow_label,
                                       a_dashedline, a_label,
                                       b_dashedline, b_label,
                                       fa_dashedline, fa_label,
                                       fb_dashedline, fb_label,
                                       def_increasing, def_increasing_rectangle).scale(0.8)
        
        g_increasing_function = VGroup(t1, ul_t1, g_graph, dot_1, dot_2,
                                       a_dashedline, a_label,
                                       b_dashedline, b_label,
                                       fa_dashedline, fa_label,
                                       fb_dashedline, fb_label,
                                       def_increasing, def_increasing_rectangle)
        


        # Animação

            # Gráfico e título
        self.play(LaggedStart(
            Succession(FadeIn(t1), Create(ul_t1)),
            FadeIn(g_graph)))
        self.wait(2)

            #Explicação
        self.play(GrowFromCenter(dot_1))
        self.play(Create(x_arrow), FadeIn(x_arrow_label))
        self.wait(2)

        self.play(Create(y_arrow), FadeIn(y_arrow_label))
        self.play(GrowFromCenter(dot_2))
        self.wait(2)
        
        self.play(FadeOut(x_arrow, y_arrow, x_arrow_label, y_arrow_label))
        self.wait(2)

        self.play(Create(a_dashedline), Create(b_dashedline))
        self.play(GrowFromCenter(a_label), GrowFromCenter(b_label))
        self.wait(2)

        self.play(Create(fa_dashedline), Create(fb_dashedline))
        self.play(GrowFromCenter(fa_label), GrowFromCenter(fb_label))
        self.wait(2)

            # Definição da função crescente
        self.play(Write(def_increasing[0][0:3]))
        self.wait(2)
        self.play(FadeIn(def_increasing[0][3]))
        self.wait(2)
        self.play(Write(def_increasing[0][4:13]))
        self.wait(2)
        self.play(FadeIn(def_increasing_rectangle))
        self.wait(2)

            # Grupo crescente vai à esquerda
        self.play(g_increasing_function.animate.to_edge(LEFT, buff = 1.7))
        self.wait(2)






        # Decrescente

            # Título
        t2 = Tex('Decrescente').scale(1.1).to_edge(UP)
        ul_t2 = Underline(t2)
    


            # Gráfico
        axes_2 = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label_2 = MathTex("x").next_to(axes_2, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label_2 = MathTex("y").next_to(axes_2, UL, buff = -0.5).shift(UP*0.3)
        axes_labels_2 = VGroup(x_label_2, y_label_2)
        axes_zero_2 = MathTex('0').scale(0.8).next_to(axes_2, DL, buff = -0.7)

        graph_2 = axes_2.plot(lambda x: -1.4 ** x + 4.2,
                            x_range=[-1, 4.7], stroke_width = 4).set_color(BLUE)
        
        g_graph_2 = VGroup(axes_2, axes_labels_2, axes_zero_2, graph_2).scale(0.9).shift(DOWN*1.7)



            # Elementos para a explicação
        dot_1_2 = Dot(axes_2.coords_to_point(1,2.8,0), color=YELLOW)
        dot_2_2 = Dot(axes_2.coords_to_point(3.5,0.953,0), color=dot_1_2.get_color())

        
        x_arrow_2 = Arrow(LEFT, RIGHT, color = YELLOW).set_opacity(0.7).scale(1.3).move_to(dot_1_2, aligned_edge=LEFT).set_z_index(-1)
        y_arrow_2 = Arrow(UP, DOWN, color = x_arrow_2.get_color()).set_opacity(0.7).scale(0.87).move_to(dot_2_2, aligned_edge=DOWN).shift(UP*0.15).set_z_index(-1)

        x_arrow_label_2 = MathTex('x', color = x_arrow_2.get_color()).scale(0.9).next_to(x_arrow_2, UP, buff = 0)
        y_arrow_label_2 = MathTex('y', color = x_arrow_2.get_color()).scale(0.9).next_to(y_arrow_2, RIGHT, buff = 0)


        a_dashedline_2 = DashedLine(axes_2.coords_to_point(1,2.8,0), axes_2.coords_to_point(1,0,0), color = YELLOW).set_opacity(0.7).move_to(dot_1_2, aligned_edge=UP)
        a_label_2 = MathTex('a', color = YELLOW).scale(0.9).next_to(a_dashedline_2, DOWN, buff = 0.2)

        b_dashedline_2 = DashedLine(axes_2.coords_to_point(3.5,0.953,0), axes_2.coords_to_point(3.5,0,0), color = a_dashedline_2.get_color()).set_opacity(0.7).move_to(dot_2_2, aligned_edge=UP)
        b_label_2 = MathTex('b', color = a_label_2.get_color()).scale(0.9).next_to(b_dashedline_2, DOWN, buff = 0.2)


        fa_dashedline_2 = DashedLine(axes_2.coords_to_point(1,2.8,0), axes_2.coords_to_point(0,2.8,0), color = YELLOW).set_opacity(0.7).move_to(dot_1_2, aligned_edge=RIGHT)
        fa_label_2 = MathTex('f(a)', color = YELLOW).scale(0.8).next_to(fa_dashedline_2, LEFT, buff = 0.2)

        fb_dashedline_2 = DashedLine(axes_2.coords_to_point(3.5,0.953,0), axes_2.coords_to_point(0,0.953,0), color = YELLOW).set_opacity(0.7).move_to(dot_2_2, aligned_edge=RIGHT)
        fb_label_2 = MathTex('f(b)', color = YELLOW).scale(0.8).next_to(fb_dashedline_2, LEFT, buff = 0.2)



            # Definição da função decrescente
        def_decreasing = MathTex(r'b > a \:\:\Rightarrow\:\: f(b) < f(a)').scale(0.9).next_to(g_graph_2, UP, buff = 1)
        def_decreasing_rectangle = SurroundingRectangle(def_decreasing, buff=0.15, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-1)

        g_decreasing_function = VGroup(t2, ul_t2, g_graph_2, dot_1_2, dot_2_2,
                                       x_arrow_2, y_arrow_2, x_arrow_label_2, y_arrow_label_2,
                                       a_dashedline_2, a_label_2,
                                       b_dashedline_2, b_label_2,
                                       fa_dashedline_2, fa_label_2,
                                       fb_dashedline_2, fb_label_2,
                                       def_decreasing, def_decreasing_rectangle).to_edge(RIGHT, buff = 1.7).scale(0.8)

    
        # Animação

            # Título
        self.play(LaggedStart(
            Succession(FadeIn(t2), Create(ul_t2)),
            FadeIn(g_graph_2)))
        self.wait(2)



            # x cresce, y diminui
        self.play(GrowFromCenter(dot_1_2))
        self.play(Create(x_arrow_2), FadeIn(x_arrow_label_2))
        self.wait(2)

        self.play(Create(y_arrow_2), FadeIn(y_arrow_label_2))
        self.play(GrowFromCenter(dot_2_2))
        self.wait(2)
        
        self.play(FadeOut(x_arrow_2, y_arrow_2, x_arrow_label_2, y_arrow_label_2))
        self.wait(2)



            # b > a  -->  f(b) < f(a)
        self.play(Create(a_dashedline_2), Create(b_dashedline_2))
        self.play(GrowFromCenter(a_label_2), GrowFromCenter(b_label_2))
        self.wait(2)

        self.play(Create(fa_dashedline_2), Create(fb_dashedline_2))
        self.play(GrowFromCenter(fa_label_2), GrowFromCenter(fb_label_2))
        self.wait(2)

            # Definição função decrescente
        self.play(Write(def_decreasing[0][0:3]))
        self.wait(2)
        self.play(FadeIn(def_decreasing[0][3]))
        self.wait(2)
        self.play(Write(def_decreasing[0][4:13]))
        self.wait(2)
        self.play(FadeIn(def_decreasing_rectangle))
        self.wait(2)



        # Comentário deve valer para quaisquer pares de pontos 'a' e 'b'

            # (Crescente) mover os pontos pelo gráfico
        #a_label.add_updater(lambda m: m.become(MathTex('a', color = YELLOW).scale(0.9).next_to(a_dashedline, DOWN, buff = 0.2)))
        #b_label.add_updater(lambda m: m.become(MathTex('b', color = a_label.get_color()).scale(0.9).next_to(b_dashedline, DOWN, buff = 0.2)))
        #fa_label.add_updater(lambda m: m.become(MathTex('f(a)', color = YELLOW).scale(0.8).next_to(fa_dashedline, LEFT, buff = 0.2)))
        #fb_label.add_updater(lambda m: m.become(MathTex('f(b)', color = YELLOW).scale(0.8).next_to(fb_dashedline, LEFT, buff = 0.2)))

        graph_1_aux_a1 = axes.plot(lambda x: 1.4 ** x, x_range=[-1, 1], stroke_width = 4).set_color(BLUE)
        graph_1_aux_a1.reverse_points()
        graph_1_aux_b1 = axes.plot(lambda x: 1.4 ** x, x_range=[-0.5, 3.5], stroke_width = 4).set_color(BLUE)
        graph_1_aux_b1.reverse_points()

        graph_2_aux_a1 = axes_2.plot(lambda x: -1.4 ** x + 4.2, x_range=[-1, 1], stroke_width = 4).set_color(BLUE)
        graph_2_aux_a1.reverse_points()
        graph_2_aux_b1 = axes_2.plot(lambda x: -1.4 ** x + 4.2, x_range=[-0.5, 3.5], stroke_width = 4).set_color(BLUE)
        graph_2_aux_b1.reverse_points()

        #a(1,2.8,0)
        #b(3.5,0.953,0)

        self.play(FadeOut(a_dashedline, b_dashedline, a_label, b_label,
                          fa_dashedline, fb_dashedline, fa_label, fb_label,
                          a_dashedline_2, b_dashedline_2, a_label_2, b_label_2,
                          fa_dashedline_2, fb_dashedline_2, fa_label_2, fb_label_2))
        self.wait(2)
        self.play(MoveAlongPath(dot_1, graph_1_aux_a1),
                  MoveAlongPath(dot_2, graph_1_aux_b1),
                  MoveAlongPath(dot_1_2, graph_2_aux_a1),
                  MoveAlongPath(dot_2_2, graph_2_aux_b1), run_time = 1.5)
        self.wait(2)
        
        graph_1_aux_a2 = axes.plot(lambda x: 1.4 ** x, x_range=[-1, 4.2], stroke_width = 4).set_color(BLUE)
        graph_1_aux_b2 = axes.plot(lambda x: 1.4 ** x, x_range=[-0.5, 4.5], stroke_width = 4).set_color(BLUE)

        graph_2_aux_a2 = axes_2.plot(lambda x: -1.4 ** x + 4.2, x_range=[-1, 4.4], stroke_width = 4).set_color(BLUE)
        graph_2_aux_b2 = axes_2.plot(lambda x: -1.4 ** x + 4.2, x_range=[-0.5, 4.7], stroke_width = 4).set_color(BLUE)
        
        self.play(MoveAlongPath(dot_1, graph_1_aux_a2),
                  MoveAlongPath(dot_2, graph_1_aux_b2),
                  MoveAlongPath(dot_1_2, graph_2_aux_a2),
                  MoveAlongPath(dot_2_2, graph_2_aux_b2), run_time = 2)
        self.wait(2)

        # Função com trecho crescente, trecho decrescente e trecho constante

        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)

        axes_3 = Axes(x_range = [-1, 7, 1],
                    y_range = [-1, 4.5, 1],
                    x_length = 7,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label_3 = MathTex("x").next_to(axes_3, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label_3 = MathTex("y").next_to(axes_3, UL, buff = -0.5).shift(UP*0.3)
        axes_labels_3 = VGroup(x_label_3, y_label_3)

        graph_3_a = axes_3.plot(lambda x: -0.8 * (x - PI/2) ** 2 + 4,
                            x_range=[-0.9, PI/2 + 0.01], stroke_width = 4).set_color(BLUE)
        graph_3_b = axes_3.plot(lambda x: np.sin(x) + 3,
                            x_range=[PI/2, 3*PI/2 + 0.01], stroke_width = 4).set_color(BLUE)
        graph_3_c = axes_3.plot(lambda x: 2,
                            x_range=[3*PI/2, 7], stroke_width = 4).set_color(BLUE)

        graph_3_label = MathTex('f', color = BLUE).next_to(graph_3_c, RIGHT)
        
        g_graph_3 = VGroup(axes_3, axes_labels_3, graph_3_a, graph_3_b, graph_3_c, graph_3_label).scale(0.9).shift(DOWN*0.8)



        self.play(FadeIn(axes_3, axes_labels_3))
        self.wait(2)

        self.play(Create(graph_3_a))
        self.wait(2)
        self.play(Create(graph_3_b))
        self.wait(2)
        self.play(Create(graph_3_c))
        self.wait(2)
        self.play(Create(graph_3_label))
        self.wait(2)

        # Dividir o domínio em intervalos A, B, C

        ab_divider = DashedLine(UP, DOWN*3.5, dash_length=0.1).move_to(axes_3.coords_to_point(PI/2,0,0)).shift(UP*1.5)
        bc_divider = DashedLine(UP, DOWN*3.5, dash_length=0.1).move_to(axes_3.coords_to_point(3*PI/2,0,0)).shift(UP*1.5)

        A_part = Rectangle(height=ab_divider.get_height(), width=2.3, stroke_width=0, fill_opacity=0.2, color=RED).move_to(ab_divider, aligned_edge=RIGHT).set_z_index(-1)
        B_part = Rectangle(height=ab_divider.get_height(), width=2.48, stroke_width=0, fill_opacity=0.2, color=BLUE).move_to(ab_divider, aligned_edge=LEFT).set_z_index(-1)
        C_part = Rectangle(height=ab_divider.get_height(), width=2.3, stroke_width=0, fill_opacity=0.2, color=GREEN).move_to(bc_divider, aligned_edge=LEFT).set_z_index(-1)
        
        A_label = MathTex('A', color = A_part.get_color()).next_to(A_part, UP)
        B_label = MathTex('B', color = B_part.get_color()).next_to(B_part, UP)
        C_label = MathTex('C', color = C_part.get_color()).next_to(C_part, UP)

        A_label_2 = Tex('Crescente', color = GRAY).scale(0.9).next_to(A_label, UP)
        B_label_2 = Tex('Decrescente', color = GRAY).scale(0.9).next_to(B_label, UP)
        C_label_2 = Tex('Constante', color = GRAY).scale(0.9).next_to(C_label, UP)

        self.play(FadeIn(A_part, A_label, A_label_2))
        self.wait(2)
        self.play(FadeOut(A_label_2),
                  FadeIn(B_part, B_label, B_label_2, ab_divider))
        self.wait(2)
        self.play(FadeOut(B_label_2),
                  FadeIn(C_part, C_label, C_label_2, bc_divider))
        self.wait(2)
        self.play(FadeOut(C_label_2))
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)






# Máximos e Mínimos locais
class vid8(MovingCameraScene):
    def construct(self):

        # Máximos e Mínimos locais

            # Título
        t1 = Tex('Máximos/Mínimos locais').scale(0.8).to_edge(UP, buff=1)
        ul_t1 = Underline(t1)



            # Gráfico
        axes = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 4, 1],
                    x_length = 8,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3).shift(RIGHT*0.5)
        axes_labels = VGroup(x_label, y_label)
        axes_zero = MathTex('0').scale(0.8).next_to(axes, DL, buff = -0.7).shift(RIGHT*0.45)

        graph = axes.plot(lambda x: 0.5 * (5*(x-1.5)**2 + 0.6*(x-1.5)**3 - 3.4*(x-1.5)**4 + (x-1.5)**5) + 1,
                            x_range=[0.3, 4.02], stroke_width = 4).set_color(BLUE)
       
        increasing_part_1 = axes.plot(lambda x: 0.5 * (5*(x-1.5)**2 + 0.6*(x-1.5)**3 - 3.4*(x-1.5)**4 + (x-1.5)**5) + 1,
                            x_range=[0.3, 0.787], stroke_width = 8).set_color(YELLOW)
        decreasing_part_1 = axes.plot(lambda x: 0.5 * (5*(x-1.5)**2 + 0.6*(x-1.5)**3 - 3.4*(x-1.5)**4 + (x-1.5)**5) + 1,
                            x_range=[0.787, 1.5], stroke_width = 8).set_color(YELLOW)
        increasing_part_2 = axes.plot(lambda x: 0.5 * (5*(x-1.5)**2 + 0.6*(x-1.5)**3 - 3.4*(x-1.5)**4 + (x-1.5)**5) + 1,
                            x_range=[1.5, 2.84], stroke_width = 8).set_color(YELLOW)
        decreasing_part_2 = axes.plot(lambda x: 0.5 * (5*(x-1.5)**2 + 0.6*(x-1.5)**3 - 3.4*(x-1.5)**4 + (x-1.5)**5) + 1,
                            x_range=[2.84, 3.589], stroke_width = 8).set_color(YELLOW)
        increasing_part_3 = axes.plot(lambda x: 0.5 * (5*(x-1.5)**2 + 0.6*(x-1.5)**3 - 3.4*(x-1.5)**4 + (x-1.5)**5) + 1,
                            x_range=[3.589, 4.02], stroke_width = 8).set_color(YELLOW)

        dot_max_2_interval = axes.plot(lambda x: 0.5 * (5*(x-1.5)**2 + 0.6*(x-1.5)**3 - 3.4*(x-1.5)**4 + (x-1.5)**5) + 1,
                            x_range=[2.84 - 0.6, 2.84 + 0.6], stroke_width = 8, stroke_opacity=0.7).set_color(WHITE)
        dot_min_1_interval = axes.plot(lambda x: 0.5 * (5*(x-1.5)**2 + 0.6*(x-1.5)**3 - 3.4*(x-1.5)**4 + (x-1.5)**5) + 1,
                            x_range=[1.5 - 0.6, 1.5 + 0.6], stroke_width = 8, stroke_opacity=0.7).set_color(WHITE)

        g_graph = VGroup(axes, axes_labels, axes_zero, graph,
                         increasing_part_1, increasing_part_2, increasing_part_3,
                         decreasing_part_1, decreasing_part_2,
                         dot_max_2_interval, dot_min_1_interval).scale(0.9).shift(DOWN*1)
       

        
        self.play(FadeIn(axes, axes_labels, axes_zero))
        self.play(Create(graph))
        self.wait(2)

            # Função oscila entre partes crescentes e decrescentes
        self.play(FadeIn(increasing_part_1, increasing_part_2, increasing_part_3))
        self.wait(2)
        self.play(FadeOut(increasing_part_1, increasing_part_2, increasing_part_3),
                  FadeIn(decreasing_part_1, decreasing_part_2))
        self.wait(2)
        self.play(FadeOut(decreasing_part_1, decreasing_part_2))
        self.wait(2)



            # Pontos máximos e mínimos locais
        dot_max_1 = Dot(graph.get_point_from_function(t=0.787), color=YELLOW).set_z_index(2)
        dot_max_2 = Dot(graph.get_point_from_function(t=2.84), color=YELLOW).set_z_index(2)
        dot_min_1 = Dot(graph.get_point_from_function(t=1.5), color=YELLOW).set_z_index(2)
        dot_min_2 = Dot(graph.get_point_from_function(t=3.589), color=YELLOW).set_z_index(2)

        self.play(LaggedStart(
            GrowFromCenter(dot_max_1),
            GrowFromCenter(dot_max_2),
            lag_ratio=0.4))
        self.wait(2)
        self.play(LaggedStart(
            GrowFromCenter(dot_min_1),
            GrowFromCenter(dot_min_2),
            lag_ratio=0.4))
        self.wait(2)

        self.play(Succession(FadeIn(t1), Create(ul_t1)))
        self.wait(2)



                # Zoom no máximo local
        dot_max_2_aux1 = Dot(graph.get_point_from_function(t=(2.84 - 0.4))).scale(0.7)
        dot_max_2_aux2 = Dot(graph.get_point_from_function(t=(2.84 - 0.28))).scale(0.7)
        dot_max_2_aux3 = Dot(graph.get_point_from_function(t=(2.84 - 0.15))).scale(0.7)
        dot_max_2_aux4 = Dot(graph.get_point_from_function(t=(2.84 + 0.15))).scale(0.7)
        dot_max_2_aux5 = Dot(graph.get_point_from_function(t=(2.84 + 0.28))).scale(0.7)
        dot_max_2_aux6 = Dot(graph.get_point_from_function(t=(2.84 + 0.4))).scale(0.7)
        dot_max_2_aux7 = Dot(graph.get_point_from_function(t=(2.84 + 1.1)), color=YELLOW).scale(0.7)

        dot_max_2_x_dashedline = DashedLine(dot_max_2, axes.coords_to_point(2.84,0,0), color=YELLOW).set_opacity(0.5).set_z_index(-1)
        dot_max_2_y_dashedline = DashedLine(dot_max_2, axes.coords_to_point(0,2.8899,0), color=YELLOW).set_opacity(0.5).set_z_index(-1)

        dot_max_2_x_label = MathTex('m', color=YELLOW).scale(0.8).next_to(dot_max_2_x_dashedline, DOWN, buff=0.1)
        dot_max_2_y_label = MathTex('f(m)', color=YELLOW).scale(0.7).next_to(dot_max_2_y_dashedline, LEFT, buff=0.1)

        t2 = Tex(f'\it Máximo local', color=WHITE).scale(0.7).next_to(dot_max_2, UP)
        t3 = Tex(f'\it Ponto de máximo', color=WHITE).scale(0.7).next_to(dot_max_2_x_label, DOWN, buff=0.1)

        self.camera.frame.save_state() # salva a posição da câmera



        self.play(FadeOut(dot_max_1, dot_min_1, dot_min_2), FadeIn(t2),
                  #self.camera.frame.animate.scale(0.7).move_to(graph),
                  run_time = 1.5)
        self.wait(2)
        self.play(LaggedStart(
            FadeIn(dot_max_2_aux1), FadeIn(dot_max_2_aux2),
            FadeIn(dot_max_2_aux3), FadeIn(dot_max_2_aux4),
            FadeIn(dot_max_2_aux5), FadeIn(dot_max_2_aux6),
            lag_ratio=0.2))
        self.wait(2)
        self.play(FadeOut(dot_max_2_aux1, dot_max_2_aux2,
                         dot_max_2_aux3, dot_max_2_aux4,
                         dot_max_2_aux5, dot_max_2_aux6),
                  FadeIn(dot_max_2_interval))
        self.wait(2)
        self.play(FadeIn(dot_max_2_x_dashedline, dot_max_2_y_dashedline,
                         dot_max_2_x_label, dot_max_2_y_label))
        self.wait(2)
        self.play(t2.animate.next_to(dot_max_2_y_label, DOWN, aligned_edge=RIGHT, buff=0.1))
        self.wait(2)
        self.play(FadeIn(t3))
        self.wait(2)
        self.play(FadeOut(t2, t3, dot_max_2, dot_max_2_interval,
                          dot_max_2_x_dashedline, dot_max_2_y_dashedline,
                          dot_max_2_x_label, dot_max_2_y_label))
        self.wait(2)



                # Zoom no mínimo local
        dot_min_1_x_dashedline = DashedLine(dot_min_1, axes.coords_to_point(1.5,0,0), color=YELLOW).set_opacity(0.5).set_z_index(-1)
        dot_min_1_y_dashedline = DashedLine(dot_min_1, axes.coords_to_point(0,1,0), color=YELLOW).set_opacity(0.5).set_z_index(-1)

        dot_min_1_x_label = MathTex('m', color=YELLOW).scale(0.8).next_to(dot_min_1_x_dashedline, DOWN, buff=0.1)
        dot_min_1_y_label = MathTex('f(m)', color=YELLOW).scale(0.7).next_to(dot_min_1_y_dashedline, LEFT, buff=0.1)

        t4 = Tex(f'\it Mínimo local', color=WHITE).scale(0.7).next_to(dot_min_1, DOWN, buff=0.2)
        t5 = Tex(f'\it Ponto de mínimo', color=WHITE).scale(0.7).next_to(dot_min_1_x_label, DOWN, buff=0.1)

        dot_min_1_aux1 = Dot(graph.get_point_from_function(t=(1.5 - 0.4))).scale(0.7)
        dot_min_1_aux2 = Dot(graph.get_point_from_function(t=(1.5 - 0.28))).scale(0.7)
        dot_min_1_aux3 = Dot(graph.get_point_from_function(t=(1.5 - 0.15))).scale(0.7)
        dot_min_1_aux4 = Dot(graph.get_point_from_function(t=(1.5 + 0.15))).scale(0.7)
        dot_min_1_aux5 = Dot(graph.get_point_from_function(t=(1.5 + 0.28))).scale(0.7)
        dot_min_1_aux6 = Dot(graph.get_point_from_function(t=(1.5 + 0.4))).scale(0.7)

        self.play(FadeIn(t4, dot_min_1),
                  run_time = 1.5)
        self.wait(2)
        self.play(LaggedStart(
            FadeIn(dot_min_1_aux1), FadeIn(dot_min_1_aux2),
            FadeIn(dot_min_1_aux3), FadeIn(dot_min_1_aux4),
            FadeIn(dot_min_1_aux5), FadeIn(dot_min_1_aux6),
            lag_ratio=0.2))
        self.wait(2)
        self.play(FadeOut(dot_min_1_aux1, dot_min_1_aux2,
                         dot_min_1_aux3, dot_min_1_aux4,
                         dot_min_1_aux5, dot_min_1_aux6),
                  FadeIn(dot_min_1_interval))
        self.wait(2)
        self.play(FadeIn(dot_min_1_x_dashedline, dot_min_1_y_dashedline,
                         dot_min_1_x_label, dot_min_1_y_label),
                  t4.animate.next_to(dot_min_1_y_label, DOWN, aligned_edge=RIGHT, buff=0.1))
        self.wait(2)
        self.play(FadeIn(t5))
        self.wait(2)
        self.play(FadeOut(t4, t5, dot_min_1, dot_min_1_interval,
                          dot_min_1_x_dashedline, dot_min_1_y_dashedline,
                          dot_min_1_x_label, dot_min_1_y_label),
                  Restore(self.camera.frame),
                  run_time = 1.5)
        self.wait(2)



                # Comentário sobre o nome "local"
        dot_max_2_interval_area = axes.get_area(graph=dot_max_2_interval, color=WHITE, stroke_width=0).set_opacity(0.5)
        dot_max_2_y_dashedline_aux = DashedLine(dot_max_2_aux7, axes.coords_to_point(0,3.228,0), color=YELLOW).set_opacity(0.5).set_z_index(-1)
        #t2.next_to(dot_max_2, UP)
        self.play(GrowFromCenter(dot_max_2), FadeIn(t2, dot_max_2_y_dashedline, dot_max_2_y_label))
        self.wait(2)
        self.play(FadeIn(dot_max_2_interval))
        self.wait(2)
        self.play(GrowFromCenter(dot_max_2_aux7), FadeIn(dot_max_2_y_dashedline_aux))
        #self.play(dot_max_2_aux7.animate.set_color(WHITE))
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)






# Máximos e Mínimos globais
class vid9(Scene):
    def construct(self):


        # Máximos e Mínimos globais

            # Título
        t1 = Tex('Máximos/Mínimos globais').scale(0.8).to_edge(UP, buff=1)
        ul_t1 = Underline(t1)

        axes = Axes(x_range = [-1, 4.5, 1],
                            y_range = [-1, 4, 1],
                            x_length = 8,
                            y_length = 4.5,
                            axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5+UP*0.2)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3).shift(RIGHT*0.7)
        axes_labels = VGroup(x_label, y_label)
        axes_zero = MathTex('0').scale(0.8).next_to(axes, DL, buff = -0.7).shift(RIGHT*0.6)

        graph = axes.plot(lambda x: (x+0.5) + 0.3*(x+0.5)*((x+0.5)-1)*((x+0.5)-2)*((x+0.5)-3)*((x+0.5)-4)*((x+0.5)-5) - 2.05,
                            x_range=[0.65, 3.7], stroke_width = 4).set_color(BLUE)
        
        dot_max_interval_1 = axes.plot(lambda x: (x+0.5) + 0.3*(x+0.5)*((x+0.5)-1)*((x+0.5)-2)*((x+0.5)-3)*((x+0.5)-4)*((x+0.5)-5) - 2.05,
                            x_range=[3.139 - 0.5, 3.139 + 0.42], stroke_width = 10, stroke_opacity=0.7).set_color(WHITE).set_z_index(-3)
        dot_max_interval_2 = axes.plot(lambda x: (x+0.5) + 0.3*(x+0.5)*((x+0.5)-1)*((x+0.5)-2)*((x+0.5)-3)*((x+0.5)-4)*((x+0.5)-5) - 2.05,
                            x_range=[0.65, 3.7], stroke_width = 10, stroke_opacity=0.7).set_color(WHITE).set_z_index(-3)
        
        graph_start = Dot(axes.coords_to_point(0.65,2.04 - 2.05,0), color=BLUE)
        graph_end = Dot(axes.coords_to_point(3.7,2.497 - 2.05,0), color=BLUE)

        g_graph = VGroup(axes, axes_labels, axes_zero, graph, graph_start, graph_end, dot_max_interval_1, dot_max_interval_2).scale(0.9).shift(DOWN*1)



        dot_max = Dot(graph.get_point_from_function(t=3.139), color=YELLOW).set_z_index(2)
        dot_min = Dot(graph.get_point_from_function(t=1.896), color=YELLOW).set_z_index(2)
        dot_local_max = Dot(graph.get_point_from_function(t=0.999), color=YELLOW).set_z_index(2)

        dot_max_y_dashedline = DashedLine(dot_max, axes.coords_to_point(0,3.07,0), color=YELLOW).set_opacity(0.5).set_z_index(-1)
        dot_min_y_dashedline = DashedLine(dot_min, axes.coords_to_point(0,-0.656,0), color=YELLOW).set_opacity(0.5).set_z_index(-1)
        dot_local_max_y_dashedline = DashedLine(dot_local_max, axes.coords_to_point(0,0.927,0), color=YELLOW).set_opacity(0.5).set_z_index(-1)



        self.play(FadeIn(axes, axes_labels, axes_zero))
        self.wait(2)
        self.play(Succession(LaggedStart(FadeIn(graph_start),
                  Create(graph)),
                  FadeIn(graph_end)))
        self.wait(2)
        self.play(GrowFromCenter(dot_max), FadeIn(dot_max_y_dashedline))
        self.wait(2)
        self.play(FadeIn(dot_max_interval_1))
        self.wait(2)
        self.play(FadeOut(dot_max_interval_1), FadeIn(dot_max_interval_2))
        self.wait(2)
        self.play(FadeOut(dot_max_interval_2))
        self.wait(2)



        t2 = Tex(f'\it Máximo global', color=WHITE).scale(0.7).next_to(dot_max, UP)
        self.play(FadeIn(t2))
        self.wait(2)



        t3 = Tex(f'\it Mínimo global', color=WHITE).scale(0.7).next_to(dot_min, DOWN, buff=0.2)
        self.play(GrowFromCenter(dot_min), FadeIn(dot_min_y_dashedline))
        self.wait(2)
        self.play(FadeIn(t3))
        self.wait(2)



        self.play(Succession(FadeIn(t1), Create(ul_t1)))
        self.wait(2)


        t4 = Tex(f'\it Máximo local', color=WHITE).scale(0.7).next_to(dot_local_max, UP)
        self.play(GrowFromCenter(dot_local_max), FadeIn(dot_local_max_y_dashedline))
        self.wait(2)
        self.play(FadeIn(t4))
        self.wait(2)



        self.play(FadeOut(dot_local_max, dot_min,
                          t3, t4,
                          dot_local_max_y_dashedline, dot_min_y_dashedline))
        self.wait(2)
        self.play(FadeOut(dot_max, t2, dot_max_y_dashedline,
                          axes, axes_zero, axes_labels, graph, graph_start, graph_end))
        self.wait(2)



        # Função pode ter vários pontos de máximo

            # Exemplo função seno
        axes = Axes(x_range = [-1, 100, 1],
                            y_range = [-2, 2, 1],
                            x_length = 83,
                            y_length = 4.5,
                            axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes.get_x_axis(), DR, buff = -0.5).shift(RIGHT*0.4+DOWN*0.6)
        y_label = MathTex("y").next_to(axes.get_y_axis(), UL, buff = -0.5).shift(UP*0.3).shift(LEFT*0.5)
        axes_labels = VGroup(x_label, y_label)

        graph = axes.plot(lambda x: np.sin(x),
                            x_range=[-1, 100], stroke_width = 4).set_color(BLUE)
        
        graph_sin_label = MathTex('y = sen(x)', color=BLUE).next_to(axes.get_y_axis(), RIGHT, buff=2).shift(UP*2)
        
        max_sin_label = MathTex('1', color=YELLOW).scale(0.8).next_to(axes.coords_to_point(0,1,0), LEFT, buff=0.15)
        dot_max_sin_y_dashedline = DashedLine(axes.coords_to_point(100,1,0), axes.coords_to_point(0,1,0), color=YELLOW).scale(1.11).set_opacity(0.5).set_z_index(-1).next_to(axes.coords_to_point(0,1,0), RIGHT, buff=0)
        dots_max_x_dashedlines = VGroup(*[DashedLine(axes.coords_to_point(PI/2 + i*2*PI,1,0), axes.coords_to_point(PI/2 + i*2*PI,0,0), color=GRAY).set_opacity(0.5).set_z_index(-1) for i in range(10)])     
        dots_max = VGroup(*[Dot(graph.get_point_from_function(t=PI/2 + i*2*PI), color=YELLOW).set_z_index(2) for i in range(10)])
        dots_max_label_1 = MathTex(r'\frac{\pi}{2}').scale(0.7).next_to(axes.coords_to_point(PI/2 + 0*PI,0,0), DOWN, buff=0.2)
        dots_max_labels = VGroup(*[MathTex(r'\frac{' + str(4*i + 5) + '\pi}{2}').scale(0.7).next_to(axes.coords_to_point((4*i + 5)*PI/2,0,0), DOWN, buff=0.2) for i in range (10)])
        g_global_maxs = VGroup(max_sin_label, dot_max_sin_y_dashedline, dots_max_x_dashedlines, dots_max, dots_max_label_1, dots_max_labels)

        min_sin_label = MathTex('-1', color=YELLOW).scale(0.8).next_to(axes.coords_to_point(0,-1,0), LEFT, buff=0.15)
        dot_min_sin_y_dashedline = DashedLine(axes.coords_to_point(100,-1,0), axes.coords_to_point(0,-1,0), color=YELLOW).scale(1.11).set_opacity(0.5).set_z_index(-1).next_to(axes.coords_to_point(0,-1,0), RIGHT, buff=0)
        dots_min_x_dashedlines = VGroup(*[DashedLine(axes.coords_to_point(3*PI/2 + i*2*PI,-1,0), axes.coords_to_point(3*PI/2 + i*2*PI,0,0), color=GRAY).set_opacity(0.5).set_z_index(-1) for i in range(10)])
        dots_min = VGroup(*[Dot(graph.get_point_from_function(t=3*PI/2 + i*2*PI), color=YELLOW).set_z_index(2) for i in range(10)])
        dots_min_labels = VGroup(*[MathTex(r'\frac{' + str(4*i + 3) + '\pi}{2}').scale(0.7).next_to(axes.coords_to_point((4*i + 3)*PI/2,0,0), UP, buff=0.2) for i in range (10)])
        g_global_mins = VGroup(min_sin_label, dot_min_sin_y_dashedline, dots_min_x_dashedlines, dots_min, dots_min_labels)
        
        g_graph = VGroup(axes, axes_labels, graph, graph_sin_label, g_global_maxs, g_global_mins)
        g_graph.scale(0.9).shift(DOWN*1+RIGHT*33)

        self.play(FadeIn(axes, axes_labels))
        self.play(Create(graph), FadeIn(graph_sin_label), run_time=2.5)
        self.wait(2)
        self.play(FadeIn(dot_max_sin_y_dashedline), FadeIn(max_sin_label))
        self.wait(2)

            # Infinitos pontos de máximo
        self.play(FadeIn(dots_max), FadeIn(dots_max_x_dashedlines), FadeIn(dots_max_label_1, dots_max_labels))
        g_graph_aux1 = VGroup(axes, axes_labels, graph, graph_sin_label, g_global_maxs)
        self.play(g_graph_aux1.animate.shift(LEFT*30), run_time=10)
        self.wait(2)
        
            # Infinitos pontos de mínimo
        self.play(FadeOut(dots_max, dots_max_x_dashedlines, dots_max_label_1, dots_max_labels))
        g_global_mins.shift(LEFT*30)
        self.play(FadeIn(g_global_mins))
        self.wait(2)
        g_graph_aux2 = VGroup(axes, axes_labels, graph, graph_sin_label, max_sin_label, dot_max_sin_y_dashedline, g_global_mins)
        self.play(g_graph_aux2.animate.shift(RIGHT*30), run_time=5)
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)






# Máxmimos e mínimos na função constante 
class vid10(Scene):
    def construct(self):

        axes = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3)
        axes_labels = VGroup(x_label, y_label)
        axes_zero = MathTex('0').scale(0.8).next_to(axes, DL, buff = -0.7)

        graph = axes.plot(lambda x: 2,
                            x_range=[-1, 5], stroke_width = 4).set_color(BLUE)
        k_label = MathTex('k', color = BLUE).scale(0.9).next_to(axes.coords_to_point(0,2,0), UL*0.5)
        function = MathTex('f(x) = k', color=BLUE).scale(0.8).shift(RIGHT+UP*0.7)
        range_set = MathTex(r'Im_{f} = \{',' k ','\}').scale(0.8).next_to(function, UP, buff=1).shift(RIGHT*0.1)
        range_set[1].set_color(BLUE)
        
        example_label = MathTex('2', color = YELLOW).scale(0.8).next_to(axes.coords_to_point(0,2,0), UL*0.5)
        example_function = MathTex('f(x) = 2', color=YELLOW).scale(0.8).shift(RIGHT+UP*0.7)
        example_range_set = MathTex(r'Im_{f} = \{',' 2 ','\}').scale(0.8).next_to(example_function, UP, buff=1).shift(RIGHT*0.1)
        example_range_set[1].set_color(YELLOW)
        
        dots = VGroup(*[Dot(graph.get_point_from_function(t=-1 + 0.3*i), color=YELLOW).set_z_index(2) for i in range(21)]).set_z_index(2)
        dots_x_dashedlines = VGroup(*[DashedLine(axes.coords_to_point(-1 + 0.3*i, 2, 0), axes.coords_to_point(-1 + 0.3*i, 0, 0), color=GRAY).set_opacity(0.5).set_z_index(-1) for i in range(21)])
        
        g_graph = VGroup(axes, axes_labels, axes_zero, graph, k_label, function, range_set,
                         example_label, example_function, example_range_set,
                         dots, dots_x_dashedlines).shift(DOWN*0.2)



        t1 = Tex(f'\it Máximo e Mínimo \par globais', color=WHITE).scale(0.7).next_to(k_label, UL, buff=1).shift(DOWN)
        arrow_1 = Arrow(t1, k_label)
        
        t2 = Tex(f'\it Pontos de máximo \par e de mínimo', color=WHITE).scale(0.7).shift(DOWN*3)
        arrow_2 = arrow_1.copy().rotate(160*DEGREES).shift(RIGHT*0.4+DOWN*3)

       

        self.play(FadeIn(axes, axes_labels, axes_zero))
        self.play(Create(graph), FadeIn(k_label))
        self.wait(2)
        self.play(FadeIn(function))
        self.wait(2)
        self.play(FadeIn(range_set))
        self.wait(2)
        self.play(TransformMatchingShapes(function, example_function),
                  TransformMatchingShapes(k_label, example_label))
        self.wait(2)
        self.play(TransformMatchingShapes(range_set, example_range_set))
        #self.play(example_range_set[1].animate.set_color(BLUE))
        self.wait(2)
        self.play(TransformMatchingShapes(example_function, function),
                  TransformMatchingShapes(example_label, k_label),
                  TransformMatchingShapes(example_range_set, range_set))
        self.wait(2)
        self.play(k_label.animate.set_color(YELLOW), 
                  range_set[1].animate.set_color(YELLOW))
        self.wait(2)
        self.play(k_label.animate.set_color(WHITE), 
                  range_set[1].animate.set_color(WHITE),
                  FadeIn(t1, arrow_1))
        self.wait(2)
        self.play(Create(dots), Create(dots_x_dashedlines), run_time = 3)
        self.wait(2)
        self.play(FadeIn(t2, arrow_2))
        self.play(arrow_2.animate.shift(RIGHT*4).rotate(-90*DEGREES), run_time = 3)
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)




    
# Problemas de otimização 1
class vid11(Scene):
    def construct(self):

        def box(ax, t):
            p1 = Dot().scale(0).move_to(ax.c2p(np.cos(t), np.sin(t)))
            p2 = Dot().scale(0).move_to(ax.c2p(-np.cos(t), np.sin(t)))
            p3 = Dot().scale(0).move_to(ax.c2p(-np.cos(t), -np.sin(t)))
            p4 = Dot().scale(0).move_to(ax.c2p(np.cos(t), -np.sin(t)))
            area = Polygon(p1.get_center(), p2.get_center(), p3.get_center(), p4.get_center())\
                .set_fill(ORANGE, opacity=0.5).set_color(ORANGE)
            final = VGroup(p1, p2, p3, p4, area)
            return final
        
        t1 = Tex('\it Problemas de Otimização').to_edge(UP, buff=0.8)

        # Problema 1: retângulo inscrito em círculo      
        axis = Axes(x_range=[-1.1,1.1],
                    y_range=[-1.1,1.1],
                    x_length= 5,
                    y_length= 5,
                    tips = False).scale(0.7)
        graph = DashedVMobject(axis.plot_parametric_curve(lambda t: [np.cos(t), np.sin(t)], t_range=[0,2 * PI]), num_dashes=30).set_opacity(0.5)

        value = ValueTracker(45 * DEGREES)

        area = always_redraw(lambda : box(axis,value.get_value()))
        area_x_label = always_redraw(lambda : MathTex('x', color=ORANGE).next_to(area, RIGHT, buff=0.1).set_z_index(2))
        area_y_label = always_redraw(lambda : MathTex('y', color=ORANGE).next_to(area, DOWN, buff=0.1).set_z_index(2))
        area_A_label = always_redraw(lambda : MathTex('A', color=WHITE).move_to(area).set_z_index(2))
        
        plane = Axes(x_range=[-0.2, 2],
                     y_range=[-0.2, 2],
                     x_length=6,
                     y_length=6,
                     tips=False).to_edge(RIGHT).shift(0.7*LEFT + 0.5*DOWN)

        x_label = plane.get_x_axis_label("s").shift(0.3*DOWN + 0.3*RIGHT)
        y_label = plane.get_y_axis_label("A").shift(0.3*UP + 0.4*LEFT)



        self.play(FadeIn(graph,area))
        self.play(FadeIn(area_x_label, area_y_label, area_A_label))
        self.wait(2)
        self.play(value.animate.set_value(70 * DEGREES), run_time = 2)
        self.play(value.animate.set_value(30 * DEGREES),  run_time = 3)
        self.play(value.animate.set_value(45 * DEGREES), run_time = 2)
        self.wait(2)

        self.remove(graph, area, area_x_label, area_y_label, area_A_label)
        self.wait(2)



            # Função A x x
        axes = Axes(x_range = [-0.5, 1.5, 1],
                    y_range = [-1, 3, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5+UP*0.1)
        y_label = MathTex("A", color=WHITE).next_to(axes, UL, buff = -0.5).shift(UP*0.3+LEFT*0.4)
        axes_labels = VGroup(x_label, y_label)

        graph_1 = axes.plot(lambda x: 2*x * np.sqrt(1 - x**2),
                            x_range=[0, 1], stroke_width = 4).set_color(BLUE)
        graph_2 = axes.plot(lambda x: 2*x * np.sqrt(1 - x**2),
                            x_range=[0.707, 1], stroke_width = 4).set_color(BLUE)
        graph_2.reverse_points()

        dot_1 = always_redraw(lambda: Dot(fill_color=YELLOW).scale(0.8).move_to(graph_1.get_end()).set_z_index(2)).move_to(axes.coords_to_point(0.5,0.55,0))
        dot_2 = Dot(graph_1.get_point_from_function(t=0.707), fill_color=YELLOW)

        g_graph = VGroup(axes, axes_labels, graph_1, graph_2, dot_1, dot_2)#.scale(0.8)

        self.play(FadeIn(axes, axes_labels))
        self.wait(2)
        self.add(dot_1)
        self.play(Create(graph_1), run_time=3)
        self.wait(2)
        self.remove(dot_1).play(MoveAlongPath(dot_2, graph_2), run_time=2)
        self.wait(2)

        

# Problemas de otimização 2
class vid12(ThreeDScene):
    def construct(self):

        # Problema 2: lata de tinta
        self.set_camera_orientation(phi=70*DEGREES, theta=-40*DEGREES)

            # Lata 3d
        r = ValueTracker(1)
        h = ValueTracker(1.7/(r.get_value() ** 2))
        can = always_redraw(lambda: Cylinder(radius=r.get_value(), height=h.get_value(), resolution=24).set_color(ORANGE).set_z_index(2))
        
        can_radius = always_redraw(lambda: Line((0,0,h.get_value()/2), (r.get_value(),0,h.get_value()/2), color=WHITE))
        can_radius_label = always_redraw(lambda: MathTex('r').rotate(90*DEGREES, X_AXIS).next_to(can_radius, UP, buff=0.4))
        
        can_height = always_redraw(lambda: Line((0,0,-h.get_value()/2), (0,0,h.get_value()/2), color=WHITE).next_to(can, DOWN, buff=0))
        can_height_label = always_redraw(lambda: MathTex('h').rotate(90*DEGREES, X_AXIS).next_to(can_height, RIGHT, buff=0.15))
        
        self.play(FadeIn(can))
        self.play(FadeIn(can_radius, can_radius_label, can_height, can_height_label))
        self.wait(2)
        self.play(r.animate.set_value(0.5), run_time = 1)#, rate_func=there_and_back
        self.wait(2)
        self.play(r.animate.set_value(1.5), run_time = 2.5)
        self.wait(2)
        self.play(r.animate.set_value(1), run_time = 1.5)
        self.wait(2)

        self.remove(can, can_height, can_height_label, can_radius, can_radius_label)
        self.wait(2)



            # Funçáo V x r
        axes = Axes(x_range = [-0.5, 6, 1],
                    y_range = [-1, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5+UP*0.1)
        y_label = MathTex("A", color=WHITE).next_to(axes, UL, buff = -0.5).shift(UP*0.3+LEFT*0.4)
        axes_labels = VGroup(x_label, y_label)

        graph_1 = axes.plot(lambda x: 0.1 * (x ** 2 + 1/(x ** 2)) + 0.8,
                            x_range=[0.18, 5], stroke_width = 4).set_color(BLUE)
        graph_2 = axes.plot(lambda x: 0.1 * (x ** 2 + 1/(x ** 2)) + 0.8,
                            x_range=[1, 5], stroke_width = 4).set_color(BLUE)
        graph_2.reverse_points()

        dot_1 = always_redraw(lambda: Dot(fill_color=YELLOW).scale(0.8).move_to(graph_1.get_end()).set_z_index(2)).move_to(axes.coords_to_point(0.5,0.55,0))
        dot_2 = Dot(graph_1.get_point_from_function(t=1), fill_color=YELLOW)

        g_graph = VGroup(axes, axes_labels, graph_1, graph_2, dot_1, dot_2).scale(0.8).shift(DOWN*0.7+RIGHT*2.5)

        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES, frame_center=(1,0,0))
        self.play(FadeIn(axes, axes_labels))
        self.wait(2)
        self.add(dot_1)
        self.play(Create(graph_1), run_time=2.5)
        self.wait(2)
        self.remove(dot_1).play(MoveAlongPath(dot_2, graph_2), run_time=1.5)
        self.wait(2)






# Limitada e Ilimitada
class vid13(Scene):
    def construct(self):

        # Títulos e definições

        t1 = Tex('Limitada').scale(1.1).to_edge(UP, buff=0.2)#.shift(RIGHT*0.3)
        ul_t1 = Underline(t1)

        def_bounded_func = MathTex('-L ',r' \leq ',' f(x) ',r' \leq ',' L').scale(0.9).next_to(t1, DOWN*3.5)
        def_bounded_func_aux = MathTex('-1 ',r' \leq ',' f(x) ',r' \leq ',' 1', color=YELLOW).scale(0.9).next_to(t1, DOWN*3.5)
        def_bounded_func_rectangle = SurroundingRectangle(def_bounded_func, buff=0.15, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-1)



        t3 = Tex('Limitada ',' superiormente').scale(1.1).to_edge(UP, buff=0.2)#.shift(RIGHT*0.3)
        ul_t3 = Underline(t3)

        def_bounded_up_func = MathTex('f(x) ',r' \leq ',' L').scale(0.9).next_to(t3, DOWN*3.5)
        def_bounded_up_func_rectangle = SurroundingRectangle(def_bounded_up_func, buff=0.15, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-1)



        t4 = Tex('Limitada ',' inferiormente', color=YELLOW).scale(1.1).move_to(t3, aligned_edge=LEFT)
        ul_t4 = Underline(t4).move_to(ul_t3, aligned_edge=LEFT)

        def_bounded_down_func = MathTex('f(x) ',r' \geq ',' L').scale(0.9).next_to(t3, DOWN*3.5)
        def_bounded_down_func_rectangle = SurroundingRectangle(def_bounded_down_func, buff=0.15, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-1)



        t5 = Tex('Ilimitada').scale(1.1).move_to(t3)
        ul_t5 = Underline(t5)


        # Gráfico
        axes = Axes(x_range = [-3, 10, 1],
                    y_range = [-2, 2, 1],
                    x_length = 8,
                    y_length = 6,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5+UP*2.3)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3+RIGHT*1.1)
        axes_labels = VGroup(x_label, y_label)


        graph_1 = axes.plot(lambda x: 0.4*(np.sin(x) + np.sin(0.5*x) + np.sin(2*x)),
                            x_range=[-2, 9], stroke_width = 4).set_color(BLUE)
        graph_1_start = Dot(graph_1.get_start(), color=BLUE)
        graph_1_end = Dot(graph_1.get_end(), color=BLUE)

        graph_2 = axes.plot(lambda x: np.sin(x),
                            x_range=[-3, 9.3], stroke_width = 4).set_color(BLUE)
        graph_2_label = MathTex('f(x) = sen(x)', color=BLUE).next_to(graph_2, UP, buff=0.5).shift(RIGHT*3)

        graph_3 = axes.plot(lambda x: -(0.3*x - 1) **2 + 0.8,
                            x_range=[-2, 8.667], stroke_width = 4).set_color(BLUE)
        
        graph_4 = axes.plot(lambda x: (0.3*x - 1) **2 - 0.8,
                            x_range=[-2, 8.667], stroke_width = 4).set_color(BLUE)
        
        graph_5 = axes.plot(lambda x: 0.07 * ((x - 4) ** 3) - 0.5 * x + 2,
                            x_range=[0.17, 7.8], stroke_width = 4).set_color(BLUE)
        

        L_dashedline_up = DashedLine(axes.coords_to_point(-3,1,0), axes.coords_to_point(10,1,0), color=YELLOW).set_opacity(0.5)
        L_dashedline_down = DashedLine(axes.coords_to_point(-3,-1,0), axes.coords_to_point(10,-1,0), color=YELLOW, stroke_opacity=0.7).set_opacity(0.5)

        bound_area = Polygon(L_dashedline_up.get_left(), L_dashedline_up.get_right(),
                             L_dashedline_down.get_right(), L_dashedline_down.get_left(),
                             color=YELLOW, fill_opacity=0.1, stroke_width=0).set_z_index(-3)
        bound_area_aux = bound_area.copy().scale(1.01).set_color(BLACK).set_opacity(1).set_z_index(-2)
        
        L_label_up = MathTex('L', color=YELLOW).scale(0.9).next_to(axes.coords_to_point(0,1,0), UL, buff=0.1)
        L_label_down = MathTex('-L', color=YELLOW).scale(0.9).next_to(axes.coords_to_point(0,-1,0), DL, buff=0.1)
        
        sin_max_label = MathTex('1', color=YELLOW).scale(0.9).next_to(axes.coords_to_point(0,1,0), UL, buff=0.1)
        sin_min_label = MathTex('-1', color=YELLOW).scale(0.9).next_to(axes.coords_to_point(0,-1,0), DL, buff=0.1)
        
        g_graph = VGroup(axes, axes_labels, graph_1, graph_1_start, graph_1_end,
                         graph_2, graph_2_label,
                         graph_3, graph_4, graph_5,
                         L_dashedline_up, L_dashedline_down,
                         bound_area, bound_area_aux,
                         L_label_up, L_label_down,
                         sin_max_label, sin_min_label).scale(0.9).shift(DOWN*1.5)


        
        g_bounded_function = VGroup(g_graph, t1, ul_t1, def_bounded_func, def_bounded_func_aux, def_bounded_func_rectangle,
                                    t3, ul_t3, def_bounded_up_func, def_bounded_up_func_rectangle,
                                    t4, ul_t4, def_bounded_down_func, def_bounded_down_func_rectangle,
                                    t5, ul_t5).scale(0.8)
        


        self.play(FadeIn(axes, axes_labels, graph_1, graph_1_start, graph_1_end))
        self.wait(2)
        self.play(Succession(FadeIn(t1), Create(ul_t1)))
        self.wait(2)
        self.add(bound_area, bound_area_aux)
        self.play(bound_area_aux.animate.shift(RIGHT*6), run_time=3)
        self.wait(2)
        t2 = MathTex('L', color=YELLOW).shift(UP*0.8)
        self.play(FadeIn(t2))
        self.wait(2)
        self.play(FadeIn(def_bounded_func[2]))
        self.play(TransformFromCopy(t2, L_label_up),
                  FadeIn(L_dashedline_up),
                  TransformFromCopy(t2, def_bounded_func[4]),
                  FadeIn(def_bounded_func[3]))
        self.wait(2)
        self.play(TransformFromCopy(t2, L_label_down),
                  FadeIn(L_dashedline_down),
                  TransformFromCopy(t2, def_bounded_func[0]),
                  FadeIn(def_bounded_func[1]))
        self.wait(2)
        self.play(FadeIn(def_bounded_func_rectangle))
        self.wait(2)
        self.play(FadeOut(graph_1, graph_1_start, graph_1_end, bound_area, bound_area_aux, t2))
        


        # Função seno, exemplo de limitada
        self.play(FadeIn(graph_2, graph_2_label))
        self.wait(2)
        self.play(TransformMatchingShapes(L_label_up, sin_max_label),
                  TransformMatchingShapes(def_bounded_func[4], def_bounded_func_aux[4]))
        self.wait(2)
        self.play(TransformMatchingShapes(L_label_down, sin_min_label),
                  TransformMatchingShapes(def_bounded_func[0], def_bounded_func_aux[0]))
        self.wait(2)



        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)



        # Função limitada superiormente
        self.play(FadeIn(axes, axes_labels, graph_3),
                  Succession(FadeIn(t3), Create(ul_t3)))
        self.wait(2)
        self.play(FadeIn(L_dashedline_up, L_label_up))
        self.wait(2)
        self.play(FadeIn(def_bounded_up_func, def_bounded_up_func_rectangle))
        self.wait(2)



        # Função limitada inferiormente
        self.play(FadeOut(graph_3, L_dashedline_up, L_label_up, def_bounded_up_func, def_bounded_up_func_rectangle))
        self.wait(2)
        self.play(FadeOut(t3[1]), ReplacementTransform(ul_t3, ul_t4))
        self.play(FadeIn(t4[1], graph_4))
        self.play(t4[1].animate.set_color(WHITE))
        self.wait(2)

        L_label_up.next_to(axes.coords_to_point(0,-1,0), DL, buff=0.1)
        self.play(FadeIn(L_dashedline_down, L_label_up))
        self.wait(2)
        self.play(FadeIn(def_bounded_down_func, def_bounded_down_func_rectangle))
        self.wait(2)



        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)



        # Função ilimitada
        g_graph.shift(UP*0.5)
        self.play(Succession(FadeIn(t5), Create(ul_t5)))
        self.play(FadeIn(axes, axes_labels, graph_5))
        self.wait(2)

        arrow_1 = Arrow(DOWN, UP, color=YELLOW).scale(0.6, scale_tips=True).rotate(-13*DEGREES).next_to(graph_5, RIGHT, buff=0.1).shift(UP*1.4)
        arrow_2 = arrow_1.copy().rotate(180*DEGREES).next_to(graph_5, LEFT, buff=0.2).shift(DOWN*1.5+RIGHT*0.8)
        self.play(FadeIn(arrow_1))
        self.wait(2)
        self.play(FadeIn(arrow_2))
        self.wait(2)
        self.play(FadeOut(arrow_1, arrow_2))

        L_label_up.next_to(axes.coords_to_point(0,1,0), UL, buff=0.1)
        not_1_1 = Line(UR, DL).scale(0.3)
        not_1_2 = Line(UL, DR).scale(0.3)
        not_1 = VGroup(not_1_1, not_1_2).scale(0.5).set_color(RED).move_to(L_label_up)
        self.play(FadeIn(L_dashedline_up, L_label_up))
        self.play(Create(not_1))
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)



        # Relação entre limitada/ilimitada com máximos/mínimos
        self.play(FadeIn(axes, axes_labels, graph_1, graph_1_start, graph_1_end))
        self.wait(2)



            # Tem máximo e mínimo ---> é limitada
        dot_max = Dot(graph_1.get_point_from_function(t=1.032), color=YELLOW).set_z_index(2)
        dot_min = Dot(graph_1.get_point_from_function(t=-1.032), color=YELLOW).set_z_index(2)
        self.play(GrowFromCenter(dot_max))
        self.play(GrowFromCenter(dot_min))
        self.wait(2)
        self.play(FadeIn(L_dashedline_up, L_dashedline_down))
        self.wait(2)

        self.play(FadeOut(graph_1, graph_1_start, graph_1_end, dot_max, dot_min, L_dashedline_up, L_dashedline_down))
        self.wait(2)



            # É ilimitada ---> não tem máximo e mínimo
        dot_local_max = Dot(graph_5.get_point_from_function(t=2.457), color=YELLOW).set_z_index(2)
        dot_local_min = Dot(graph_5.get_point_from_function(t=5.543), color=YELLOW).set_z_index(2)
        self.play(FadeIn(graph_5))
        self.wait(2)
        self.play(GrowFromCenter(dot_local_max))
        self.play(GrowFromCenter(dot_local_min))
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)






# Assíntotas
class vid14(MovingCameraScene):
    def construct(self):

        # Título
        t1 = Tex('Assíntota').scale(0.9).to_edge(UP)#.shift(RIGHT*0.3)
        ul_t1 = Underline(t1)

        # Funções com assíntotas
        axes_1 = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.7)
        graph_1 = axes_1.plot(lambda x: 0.3 ** x + 1,
                            x_range=[-1, 5], stroke_width = 4).set_color(BLUE).set_z_index(2)
        
        assymptote_1_aux = axes_1.plot(lambda x: 1 - 0.1,
                            x_range=[-1, 5], stroke_width = 0)
        assymptote_1 = DashedLine(axes_1.coords_to_point(-1,1 - 0.1,0), axes_1.coords_to_point(5,1 - 0.1,0), color=YELLOW).set_z_index(3)

        num = ValueTracker(-0.5)
        distance_1_ref_1 = always_redraw(lambda: Dot(graph_1.get_point_from_function(t=num.get_value())).scale(0))
        distance_1_ref_2 = always_redraw(lambda: Dot(assymptote_1_aux.get_point_from_function(t=num.get_value())).scale(0))
        distance_1 = always_redraw(lambda: Line(distance_1_ref_1, distance_1_ref_2, color=WHITE, stroke_width = 5))
        rectangle_1 = SurroundingRectangle(axes_1, buff=0.3, color=GRAY, stroke_width=2)
        
        
        g_1 = VGroup(axes_1, graph_1, rectangle_1, assymptote_1, assymptote_1_aux, 
                     distance_1_ref_1, distance_1_ref_2, distance_1)



        axes_2 = Axes(x_range = [-5, 5, 1],
                    y_range = [-6, 6, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.7)
        graph_2_a = axes_2.plot(lambda x: x + 1/x,
                            x_range=[0.173, 5], stroke_width = 4).set_color(BLUE).set_z_index(2)
        graph_2_b = axes_2.plot(lambda x: x + 1/x,
                            x_range=[-5, -0.173], stroke_width = 4).set_color(BLUE).set_z_index(2)

        assymptote_2_a = DashedLine(axes_2.coords_to_point(-5,-5,0), axes_2.coords_to_point(5,5,0), color=YELLOW).set_z_index(3)
        assymptote_2_b = DashedLine(axes_2.coords_to_point(0,-6,0), axes_2.coords_to_point(0,6,0), color=YELLOW).set_z_index(3)

        rectangle_2 = SurroundingRectangle(axes_2, buff=0.3, color=GRAY, stroke_width=2)
        g_2 = VGroup(axes_2, graph_2_a, graph_2_b, rectangle_2, assymptote_2_a, assymptote_2_b)



        axes_3 = Axes(x_range = [-5, 5, 1],
                    y_range = [-4.5, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False}).set_opacity(0.7)
        graph_3_a = axes_3.plot(lambda x: 0.5 * np.tan(x),
                            x_range=[-1.45, 1.455], stroke_width = 4).set_color(BLUE).set_z_index(2)
        graph_3_b = axes_3.plot(lambda x: 0.5 * np.tan(x),
                            x_range=[-1.45 + PI, 1.45 + PI], stroke_width = 4).set_color(BLUE).set_z_index(2)
        graph_3_c = axes_3.plot(lambda x: 0.5 * np.tan(x),
                            x_range=[-1.45 - PI, 1.45 - PI], stroke_width = 4).set_color(BLUE).set_z_index(2)
        
        assymptote_3_a = DashedLine(axes_3.coords_to_point(PI/2,-4.5,0), axes_3.coords_to_point(PI/2,4.5,0), color=YELLOW).set_z_index(3)
        assymptote_3_b = DashedLine(axes_3.coords_to_point(-PI/2,-4.5,0), axes_3.coords_to_point(-PI/2,4.5,0), color=YELLOW).set_z_index(3)
        assymptote_3_c = DashedLine(axes_3.coords_to_point(3*PI/2,-4.5,0), axes_3.coords_to_point(3*PI/2,4.5,0), color=YELLOW).set_z_index(3)
        assymptote_3_d = DashedLine(axes_3.coords_to_point(-3*PI/2,-4.5,0), axes_3.coords_to_point(-3*PI/2,4.5,0), color=YELLOW).set_z_index(3)

        rectangle_3 = SurroundingRectangle(axes_3, buff=0.3, color=GRAY, stroke_width=2)
        g_3 = VGroup(axes_3, graph_3_a, graph_3_b, graph_3_c, rectangle_3, assymptote_3_a, assymptote_3_b, assymptote_3_c, assymptote_3_d)


        g = VGroup(g_1, g_2, g_3).arrange(RIGHT).scale(0.7).shift(DOWN*0.5)


        label_1 = MathTex(r'y = 0.5^x + 1', color=BLUE).scale(0.8).next_to(g_1, UP)
        label_2 = MathTex(r'y = x + {1 \over x}', color=BLUE).scale(0.8).next_to(g_2, UP)
        label_3 = Tex(r'$y =$ tg$(x)$', color=BLUE).scale(0.8).next_to(g_3, UP)



        self.play(LaggedStart(
            FadeIn(axes_1, graph_1, rectangle_1, label_1),
            FadeIn(axes_2, graph_2_a, graph_2_b, rectangle_2, label_2),
            FadeIn(axes_3, graph_3_a, graph_3_b, graph_3_c, rectangle_3, label_3),
            lag_ratio=0.5))
        self.wait(2)

        self.play(LaggedStart(
            FadeIn(assymptote_1),
            FadeIn(assymptote_2_a, assymptote_2_b),
            FadeIn(assymptote_3_a, assymptote_3_b, assymptote_3_c, assymptote_3_d),
            lag_ratio=0.5))
        self.wait(2)

        self.play(Succession(FadeIn(t1), Create(ul_t1)))
        self.wait(2)

        self.camera.frame.save_state() # Salva a posição da câmera
        self.play(self.camera.frame.animate.scale(0.6).move_to(g_1))
        self.wait(2)

        self.play(Create(distance_1))
        self.add(distance_1_ref_1, distance_1_ref_2)
        self.wait(2)
        arrow_1 = MathTex(r'\rightarrow').next_to(graph_1, UP, buff=-1.5).shift(RIGHT*1.5)
        self.play(num.animate.set_value(4.9),
                  self.camera.frame.animate.scale(0.5).shift(RIGHT*0.5), # Zoom no gráfico 1
                  run_time=6)
        self.wait(2)

        self.play(Restore(self.camera.frame)) # Tira o zoom
        self.wait(2)



        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)



        # Função que parece ter assíntota, mas não tem
        axes = Axes(x_range = [-3, 3, 1],
                    y_range = [-1, 6, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3).shift(RIGHT*1.65)
        axes_labels = VGroup(x_label, y_label)
        axes_zero = MathTex('0').scale(0.8).next_to(axes, DL, buff = -0.7).shift(RIGHT*1.65+DOWN*0.2)

        graph_1 = axes.plot(lambda x: x ** 2, x_range=[-5, 5], stroke_width = 4).set_color(BLUE)
        graph_2 = axes.plot(lambda x: x ** 2, x_range=[3.5, 5], stroke_width = 20, stroke_opacity=0.4).set_color(WHITE)

        graph_1_label = MathTex('f(x) = x^2', color=BLUE).move_to(axes.coords_to_point(-3.5,3,0))

        assymptote_1 = DashedLine(axes.coords_to_point(4,10,0), axes.coords_to_point(6,32,0), color=YELLOW, dash_length=0.1).shift(LEFT*0.7+DOWN*4.5).rotate(0*DEGREES).set_z_index(3)

        g_graph = VGroup(axes, axes_labels, axes_zero, graph_1, graph_1_label, assymptote_1, graph_2).scale(0.9).shift(DOWN*1.2+RIGHT*0.28)
        

        black_rectangle = Rectangle(width=10, height=5, color=BLACK, fill_opacity=1).next_to(axes, UP, buff=0.2).set_z_index(2)

        self.add(black_rectangle)
        self.play(FadeIn(axes, axes_labels, axes_zero, graph_1, graph_1_label))
        self.play(self.camera.frame.animate.scale(2).shift(UP*5),
                  black_rectangle.animate.shift(UP*15))
        self.wait(2)
        self.play(FadeIn(assymptote_1))
        self.wait(2)     
        self.play(FadeIn(graph_2))
        self.wait(2)
        self.play(self.camera.frame.animate.scale(0.4).move_to(assymptote_1).shift(UP*3.5))
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)
        





# Par
class vid15(MovingCameraScene):
    def construct(self):

        #l = Line(UP*3, DOWN*3).move_to(ORIGIN)
        #self.add(l)

        # Par

            # Título
        t1 = Tex('Par').scale(1.1).to_edge(UP).shift(RIGHT*0.3)
        ul_t1 = Underline(t1)



            # Definição da função par
        def_even = MathTex(r'f(x) = f(-x)').scale(0.9).next_to(t1, DOWN*4.5)
        def_even_rectangle = SurroundingRectangle(def_even, buff=0.15, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-1)



            # Gráfico
        axes = Axes(x_range = [-3, 3, 1],
                    y_range = [-1, 6, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3).shift(RIGHT*1.65)
        axes_labels = VGroup(x_label, y_label)
        axes_zero = MathTex('0').scale(0.8).next_to(axes, DL, buff = -0.7).shift(RIGHT*1.65+DOWN*0.2)

        graph_1 = axes.plot(lambda x: x ** 2, x_range=[-2.3, 2.3], stroke_width = 4).set_color(BLUE)
        graph_2 = axes.plot(lambda x: x ** 2, x_range=[0, 2.3], stroke_width = 4).set_color(BLUE)
        graph_3 = axes.plot(lambda x: x ** 2, x_range=[0, 2.3], stroke_width = 4).set_color(BLUE)
        graph_4 = axes.plot(lambda x: x ** 2, x_range=[0.5,1.5], stroke_width = 4).set_color(BLUE)
        graph_4.reverse_points()
        graph_5 = axes.plot(lambda x: x ** 2, x_range=[0.5, 2.2], stroke_width = 4).set_color(BLUE)

        g_graph = VGroup(axes, axes_labels, axes_zero, graph_1, graph_2, graph_3, graph_4, graph_5).scale(0.9).shift(DOWN*1.2+RIGHT*0.28)



        graph_1_label = MathTex('f(x) = x^2', color = BLUE).scale(0.9).next_to(graph_1, LEFT).shift(UP)
        


            # Exemplos de pontos simétricos
        graph_1_label_a = MathTex('f(1) = f(-1) = 1', color = GRAY).scale(0.9).next_to(graph_1_label, DOWN, aligned_edge=RIGHT)
        graph_1_label_b = MathTex('f(2) = f(-2) = 4', color = GRAY).scale(0.9).next_to(graph_1_label, DOWN, aligned_edge=RIGHT)

        even_dot_a1 = Dot(axes.coords_to_point(1,1,0), color=BLUE)
        even_dot_a1_dashedline1 = DashedLine(even_dot_a1, (even_dot_a1.get_x(), axes.get_x_axis().get_y(), 0), color = GRAY)
        even_dot_a1_dashedline2 = DashedLine(even_dot_a1, (axes.get_y_axis().get_x(), even_dot_a1.get_y(), 0), color = GRAY)

        even_dot_a2 = Dot(axes.coords_to_point(-1,1,0), color=BLUE)
        even_dot_a2_dashedline1 = DashedLine(even_dot_a2, (even_dot_a2.get_x(), axes.get_x_axis().get_y(), 0), color = GRAY)
        even_dot_a2_dashedline2 = DashedLine(even_dot_a2, (axes.get_y_axis().get_x(), even_dot_a2.get_y(), 0), color = GRAY)

        even_dot_b1 = Dot(axes.coords_to_point(2,4,0), color=BLUE)
        even_dot_b1_dashedline1 = DashedLine(even_dot_b1, (even_dot_b1.get_x(), axes.get_x_axis().get_y(), 0), color = GRAY)
        even_dot_b1_dashedline2 = DashedLine(even_dot_b1, (axes.get_y_axis().get_x(), even_dot_b1.get_y(), 0), color = GRAY)

        even_dot_b2 = Dot(axes.coords_to_point(-2,4,0), color=BLUE)
        even_dot_b2_dashedline1 = DashedLine(even_dot_b2, (even_dot_b2.get_x(), axes.get_x_axis().get_y(), 0), color = GRAY)
        even_dot_b2_dashedline2 = DashedLine(even_dot_b2, (axes.get_y_axis().get_x(), even_dot_b2.get_y(), 0), color = GRAY)

        even_dots = VGroup(even_dot_a1, even_dot_a1_dashedline1, even_dot_a1_dashedline2,
                           even_dot_b1, even_dot_a2_dashedline1, even_dot_a2_dashedline2,
                           even_dot_a2, even_dot_b1_dashedline1, even_dot_b1_dashedline2,
                           even_dot_b2, even_dot_b2_dashedline1, even_dot_b2_dashedline2)

        x_label_a1 = MathTex('1').scale(0.72).next_to(axes.coords_to_point(1,0,0), DOWN, buff=0.1)
        x_label_a2 = MathTex('-1').scale(0.72).next_to(axes.coords_to_point(-1,0,0), DOWN, buff=0.1).shift(LEFT*0.1)
        x_label_b1 = MathTex('2').scale(0.72).next_to(axes.coords_to_point(2,0,0), DOWN, buff=0.1)
        x_label_b2 = MathTex('-2').scale(0.72).next_to(axes.coords_to_point(-2,0,0), DOWN, buff=0.1).shift(LEFT*0.15)
        y_label_fa = MathTex('1').scale(0.72).next_to(axes.coords_to_point(0,1,0), UL, buff=0.1)
        y_label_fb = MathTex('4').scale(0.72).next_to(axes.coords_to_point(0,4,0), UL, buff=0.1)
        dots_labels = VGroup(x_label_a1, x_label_a2, x_label_b1, x_label_b2,
                             y_label_fa, y_label_fb)
        


            # Mais pontos
        extra_dot_1 = Dot(axes.coords_to_point(0.5,0.25,0), color=BLUE)
        extra_dot_2 = Dot(axes.coords_to_point(-0.5,0.25,0), color=BLUE)
        extra_dot_3 = Dot(axes.coords_to_point(1.38,1.38**2,0), color=BLUE)
        extra_dot_4 = Dot(axes.coords_to_point(-1.38,1.38**2,0), color=BLUE)
        extra_dot_5 = Dot(axes.coords_to_point(1.7,1.7**2,0), color=BLUE)
        extra_dot_6 = Dot(axes.coords_to_point(-1.7,1.7**2,0), color=BLUE)
        extra_dot_7 = Dot(axes.coords_to_point(2.3,2.3**2,0), color=BLUE)
        extra_dot_8 = Dot(axes.coords_to_point(-2.3,2.3**2,0), color=BLUE)
        more_dots = VGroup(extra_dot_1, extra_dot_2,
                             extra_dot_3, extra_dot_4,
                             extra_dot_5, extra_dot_6,
                             extra_dot_7, extra_dot_8)

        g_even_function = VGroup(t1, ul_t1, def_even, def_even_rectangle, g_graph,
                                 graph_1_label, graph_1_label_a, graph_1_label_b,
                                 even_dots, dots_labels, more_dots).scale(0.8)
        


            # Diagrama para mostrar que x e -x têm mesma imagem
                # Domínio
        domain = Ellipse(width = 3, height = 4, fill_opacity = 0.2).shift(LEFT*2.5)
        domain_element_2 = (MathTex('x').scale(1.3).move_to(domain.get_center())).shift(UP*0.6)
        domain_element_3 = (MathTex('-x').scale(1.3).move_to(domain.get_center())).shift(DOWN*0.6+LEFT*0.25)
        domain_elements = VGroup(domain_element_2, domain_element_3)

                # Contradomínio
        codomain = Ellipse(width = 3, height = 4, color = BLUE, fill_opacity = 0.2).shift(RIGHT*2.5)
        codomain_element = Dot(codomain.get_center())

        arrow_1 = CurvedArrow((-2.2, 0.6, 0), (2.2, 0, 0), radius = -5, stroke_width = 2.5)
        arrow_2 = CurvedArrow((-2.2, -0.6, 0), (2.2, 0, 0), radius = -5, stroke_width = 2.5)
        arrows = VGroup(arrow_1, arrow_2)



        g_diagram = VGroup(domain, domain_elements,
                           codomain, codomain_element,
                           arrows).scale(0.6).shift(DOWN*1.2).set_z_index(3)
        
        
        
        
        # Animação

            # Título
        self.play(Succession(FadeIn(t1), Create(ul_t1)))
        self.wait(2)



            # Trocar sinal do argumento
        t2 = MathTex('f(+x)').scale(0.9).shift(UP*1)
        t3 = MathTex('f(-x)').scale(0.9)
        black_rectangle_aux_1 = Rectangle(height=0.95, color=BLACK, fill_opacity=1).next_to(t2, UP, buff=0.1).set_z_index(2)
        black_rectangle_aux_2 = Rectangle(height=0.95, color=BLACK, fill_opacity=1).next_to(t2, DOWN, buff=0.1).set_z_index(2)

        self.play(FadeIn(t2))
        self.add(t3[0][2:4], black_rectangle_aux_1, black_rectangle_aux_2)
        self.play(t2[0][2:4].animate.shift(UP),
                   t3[0][2:4].animate.shift(UP))
        self.wait(2)
        self.play(FadeOut(t2[0][0:2], t2[0][4:5], t2[0][2:4], t3[0][2:4]))
        self.remove(black_rectangle_aux_1, black_rectangle_aux_2)
        self.wait(2)



            # Diagrama x e -x têm mesma imagem
        def_even_aux = MathTex(r'f(x) = f(-x)').scale(0.78).next_to(codomain_element, RIGHT, buff=-0.1, aligned_edge=LEFT).set_z_index(5)        
        self.play(FadeIn(g_diagram))
        self.play(FadeOut(codomain_element),
                  FadeIn(def_even_aux))
        self.wait(2)



            # Definição de função par
        self.play(ReplacementTransform(def_even_aux, def_even),
                  FadeOut(domain, domain_elements, codomain, arrows))
        self.play(FadeIn(def_even_rectangle))
        self.wait(2)



            # Gráfico da função par, exemplo f(x) = x^2
        self.play(FadeIn(graph_1_label, axes, axes_labels, axes_zero))
        self.wait(2)
        self.play(FadeIn(graph_1_label_a, x_label_a1, x_label_a2, y_label_fa,
                         even_dot_a1, even_dot_a1_dashedline1, even_dot_a1_dashedline2,
                         even_dot_a2, even_dot_a2_dashedline1, even_dot_a2_dashedline2))
        self.wait(2)
        self.play(FadeOut(graph_1_label_a))
        self.play(FadeIn(graph_1_label_b, x_label_b1, x_label_b2, y_label_fb,
                         even_dot_b1, even_dot_b1_dashedline1, even_dot_b1_dashedline2,
                         even_dot_b2, even_dot_b2_dashedline1, even_dot_b2_dashedline2))
        self.wait(2)
        self.play(FadeOut(graph_1_label_b))
        self.play(LaggedStart(
            FadeIn(extra_dot_1, extra_dot_2),
            FadeIn(extra_dot_3, extra_dot_4),
            FadeIn(extra_dot_5, extra_dot_6),
            FadeIn(extra_dot_7, extra_dot_8),
            lag_ratio=0.4))
        self.wait(2)



            # Os pontos se transformam no gráfico da função f(x) = x^2
        g_dots = VGroup(even_dot_a1, even_dot_a2,
                        even_dot_b1, even_dot_b2,
                        more_dots)
        self.play(TransformMatchingShapes(g_dots, graph_1),
                  FadeOut(even_dot_a1_dashedline1, even_dot_a1_dashedline2,
                          even_dot_a2_dashedline1, even_dot_a2_dashedline2,
                          even_dot_b1_dashedline1, even_dot_b1_dashedline2,
                          even_dot_b2_dashedline1, even_dot_b2_dashedline2,
                          x_label_a1, x_label_a2, y_label_fa,
                          x_label_b1, x_label_b2, y_label_fb),
                          run_time = 2)
        self.wait(2)



            # Simetria em relação ao eixo y
        self.play(axes.get_y_axis().animate.set_color(YELLOW),
                  y_label.animate.set_color(YELLOW))
        self.wait(2)
        self.add(graph_2, graph_3)
        self.play(FadeOut(graph_1, graph_1_label))
        self.play(Rotate(graph_3, -180*DEGREES, axis=Y_AXIS, about_point=axes.coords_to_point(0,0,0)), run_time = 2)
        self.play(axes.get_y_axis().animate.set_color(WHITE),
                  y_label.animate.set_color(WHITE))
        self.wait(2)



                # Significado geométrico da simetria 
        line_aux1 = Line(UP*3, DOWN*3).move_to(axes.coords_to_point(0,2.25,0)) # linha auxiliar para os ângulos retos

        dot_p = Dot(axes.coords_to_point(1.5,2.25,0), color=YELLOW)
        distance_p_Oy = always_redraw(lambda: Line(dot_p, (0,dot_p.get_y(),0), color=YELLOW).set_opacity(0.7))
        angle_distance_p_Oy = always_redraw(lambda: RightAngle(distance_p_Oy, line_aux1, length=0.15, quadrant=(-1,1)))

        dot_p_symmetrical = always_redraw(lambda: Dot(((-1 * dot_p.get_x()),dot_p.get_y(),0), color=YELLOW))
        distance_p_symmetrical_Oy = always_redraw(lambda: Line((0,dot_p_symmetrical.get_y(),0), dot_p_symmetrical, color=YELLOW).set_opacity(0.7))
        angle_distance_p_symmetrical_Oy = always_redraw(lambda: RightAngle(distance_p_Oy, line_aux1, length=0.15, quadrant=(1,1)))

        self.play(GrowFromCenter(dot_p))
        self.wait(2)
        self.play(Succession(Create(distance_p_Oy), FadeIn(angle_distance_p_Oy)))
        self.wait(2)
        self.play(Create(distance_p_symmetrical_Oy), FadeIn(angle_distance_p_symmetrical_Oy))
        self.play(GrowFromCenter(dot_p_symmetrical))
        self.wait(2)

        self.play(FadeOut(angle_distance_p_Oy, angle_distance_p_symmetrical_Oy))
        self.play(MoveAlongPath(dot_p, graph_4), run_time = 3)
        self.play(MoveAlongPath(dot_p, graph_5), run_time = 3)
        self.wait(2)

        self.remove(dot_p, dot_p_symmetrical, distance_p_Oy, distance_p_symmetrical_Oy)
        self.wait(2)



                # Coordenadas dos pontos simétricos
        dot_p.move_to(axes.coords_to_point(1.5,2.25,0))
        dot_p_symmetrical.move_to(axes.coords_to_point(-1.5,2.25,0))
        
        dot_p_label = MathTex('(x,y)').scale(0.8).next_to(dot_p, UR, buff=0).shift(RIGHT*0.2)
        dot_p_symmetrical_label = MathTex('(-x,y)').scale(0.8).next_to(dot_p_symmetrical, UL, buff=0).shift(LEFT*0.2)

        '''line_aux2 = Line(axes.coords_to_point(1.5, 2.25, 0), axes.coords_to_point(1.5, 0, 0))
        brace_1 = Brace(line_aux2, RIGHT, color = YELLOW)

        line_aux3 = Line(axes.coords_to_point(-1.5, 2.25, 0), axes.coords_to_point(-1.5, 0, 0))
        brace_2 = Brace(line_aux3, LEFT, color = YELLOW)'''

        self.play(GrowFromCenter(dot_p))
        self.wait(2)
        self.play(FadeIn(dot_p_label))
        self.wait(2)
        self.play(GrowFromCenter(dot_p_symmetrical))
        self.wait(2)
        self.play(FadeIn(dot_p_symmetrical_label))
        self.wait(2)
        
                    # Destaque nas coordenada 'y'
        self.play(dot_p_label[0][3].animate.set_color(YELLOW),
                  dot_p_symmetrical_label[0][4].animate.set_color(YELLOW))
        self.wait(2)
        self.play(dot_p_label[0][3].animate.set_color(WHITE),
                  dot_p_symmetrical_label[0][4].animate.set_color(WHITE))
        self.wait(2)
        
                    # Destaque nas coordenadas 'x'
        self.play(dot_p_label[0][1].animate.set_color(YELLOW),
                  dot_p_symmetrical_label[0][1:3].animate.set_color(YELLOW))
        self.wait(2)
        self.play(dot_p_label[0][1].animate.set_color(WHITE),
                  dot_p_symmetrical_label[0][1:3].animate.set_color(WHITE))
        self.wait(2)





        
# Ímpar
class vid16(MovingCameraScene):
    def construct(self):

        #l = Line(UP*3, DOWN*3).move_to(ORIGIN)
        #self.add(l)

        # Ímpar

            # Título
        t1 = Tex('Ímpar').scale(1.1).to_edge(UP).shift(RIGHT*0.3+UP)
        ul_t1 = Underline(t1).set_z_index(3)



            # Definição da função ímpar
        def_odd = MathTex(r'f(-x) = -f(x)').scale(0.9).next_to(t1, DOWN*4.5)
        def_odd_rectangle = SurroundingRectangle(def_odd, buff=0.18, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-1)



            # Gráfico
        axes = Axes(x_range = [-3.5, 3.5, 1],
                    y_range = [-8.5, 9.5, 1],
                    x_length = 5,
                    y_length = 7,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes.get_x_axis(), DR, buff = -0.5).shift(RIGHT*0.5+DOWN*0.5)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3).shift(RIGHT*1.65)
        axes_labels = VGroup(x_label, y_label)

        graph_1 = axes.plot(lambda x: x ** 3, x_range=[-2.05, 2.05], stroke_width = 4).set_color(BLUE)
        graph_2 = axes.plot(lambda x: x ** 3, x_range=[1, 1.6], stroke_width = 4).set_color(BLUE)
        graph_2.reverse_points()
        graph_3 = axes.plot(lambda x: x ** 3, x_range=[-1.6, -1], stroke_width = 4).set_color(BLUE)
        graph_4 = axes.plot(lambda x: x ** 3, x_range=[1, 2], stroke_width = 4).set_color(BLUE)
        graph_5 = axes.plot(lambda x: x ** 3, x_range=[-2, -1], stroke_width = 4).set_color(BLUE)
        graph_5.reverse_points()
        graph_6 = axes.plot(lambda x: x ** 3, x_range=[0, 2.05], stroke_width = 4).set_color(BLUE)
        graph_7 = axes.plot(lambda x: x ** 3, x_range=[0, 2.05], stroke_width = 4).set_color(BLUE)
        graph_8 = axes.plot(lambda x: x ** 3, x_range=[0, 2.05], stroke_width = 4).set_color(BLUE)

        g_graph = VGroup(axes, axes_labels, graph_1, graph_2, graph_3, graph_4, graph_5, graph_6, graph_7, graph_8).scale(0.8).shift(DOWN*1.7+RIGHT*0.28)



        graph_1_label = MathTex('f(x) = x^3', color = BLUE).scale(0.9).next_to(graph_1, LEFT).shift(UP*2.5)
        


            # Exemplos de pontos simétricos
        graph_1_label_a1 = MathTex('f(1) = 1', color = GRAY).scale(0.9).next_to(graph_1_label, DOWN, aligned_edge=LEFT)
        graph_1_label_a2 = MathTex('f(-1)= -1', color = GRAY).scale(0.9).next_to(graph_1_label_a1, DOWN)
        
        graph_1_label_b1 = MathTex('f(2) = 8', color = GRAY).scale(0.9).next_to(graph_1_label, DOWN, aligned_edge=LEFT)
        graph_1_label_b2 = MathTex('f(-2)= -8', color = GRAY).scale(0.9).next_to(graph_1_label_b1, DOWN)

        odd_dot_a1 = Dot(axes.coords_to_point(1,1,0), color=BLUE)
        odd_dot_a1_dashedline1 = DashedLine(odd_dot_a1, (odd_dot_a1.get_x(), axes.get_x_axis().get_y(), 0), color = GRAY)
        odd_dot_a1_dashedline2 = DashedLine(odd_dot_a1, (axes.get_y_axis().get_x(), odd_dot_a1.get_y(), 0), color = GRAY)

        odd_dot_a2 = Dot(axes.coords_to_point(-1,-1,0), color=BLUE)
        odd_dot_a2_dashedline1 = DashedLine(odd_dot_a2, (odd_dot_a2.get_x(), axes.get_x_axis().get_y(), 0), color = GRAY)
        odd_dot_a2_dashedline2 = DashedLine(odd_dot_a2, (axes.get_y_axis().get_x(), odd_dot_a2.get_y(), 0), color = GRAY)

        odd_dot_b1 = Dot(axes.coords_to_point(2,8,0), color=BLUE)
        odd_dot_b1_dashedline1 = DashedLine(odd_dot_b1, (odd_dot_b1.get_x(), axes.get_x_axis().get_y(), 0), color = GRAY)
        odd_dot_b1_dashedline2 = DashedLine(odd_dot_b1, (axes.get_y_axis().get_x(), odd_dot_b1.get_y(), 0), color = GRAY)

        odd_dot_b2 = Dot(axes.coords_to_point(-2,-8,0), color=BLUE)
        odd_dot_b2_dashedline1 = DashedLine(odd_dot_b2, (odd_dot_b2.get_x(), axes.get_x_axis().get_y(), 0), color = GRAY)
        odd_dot_b2_dashedline2 = DashedLine(odd_dot_b2, (axes.get_y_axis().get_x(), odd_dot_b2.get_y(), 0), color = GRAY)

        odd_dots = VGroup(odd_dot_a1, odd_dot_a1_dashedline1, odd_dot_a1_dashedline2,
                           odd_dot_b1, odd_dot_a2_dashedline1, odd_dot_a2_dashedline2,
                           odd_dot_a2, odd_dot_b1_dashedline1, odd_dot_b1_dashedline2,
                           odd_dot_b2, odd_dot_b2_dashedline1, odd_dot_b2_dashedline2)

        x_label_a1 = MathTex('1').scale(0.72).next_to(axes.coords_to_point(1,0,0), DOWN, buff=0.1)
        x_label_a2 = MathTex('-1').scale(0.72).next_to(axes.coords_to_point(-1,0,0), UP, buff=0.1).shift(LEFT*0.1)
        x_label_b1 = MathTex('2').scale(0.72).next_to(axes.coords_to_point(2,0,0), DOWN, buff=0.1)
        x_label_b2 = MathTex('-2').scale(0.72).next_to(axes.coords_to_point(-2,0,0), UP, buff=0.1).shift(LEFT*0.15)
        y_label_fa1 = MathTex('1').scale(0.72).next_to(axes.coords_to_point(0,1,0), UL, buff=0.1)
        y_label_fa2 = MathTex('-1').scale(0.72).next_to(axes.coords_to_point(0,-1,0), DL, buff=0.1)
        y_label_fb1 = MathTex('8').scale(0.72).next_to(axes.coords_to_point(0,8,0), DL, buff=0.1)
        y_label_fb2 = MathTex('-8').scale(0.72).next_to(axes.coords_to_point(0,-8,0), UL, buff=0.1)
        dots_labels = VGroup(x_label_a1, x_label_a2, x_label_b1, x_label_b2,
                             y_label_fa1, y_label_fa2, y_label_fb1, y_label_fb2)
        


            # Mais pontos
        extra_dot_1 = Dot(graph_1.get_point_from_function(t=0.5), color=BLUE)
        extra_dot_2 = Dot(graph_1.get_point_from_function(t=-0.5), color=BLUE)
        extra_dot_3 = Dot(graph_1.get_point_from_function(t=1.35), color=BLUE)
        extra_dot_4 = Dot(graph_1.get_point_from_function(t=-1.35), color=BLUE)
        extra_dot_5 = Dot(graph_1.get_point_from_function(t=1.6), color=BLUE)
        extra_dot_6 = Dot(graph_1.get_point_from_function(t=-1.6), color=BLUE)
        extra_dot_7 = Dot(graph_1.get_point_from_function(t=1.8), color=BLUE)
        extra_dot_8 = Dot(graph_1.get_point_from_function(t=-1.8), color=BLUE)
        
        more_dots = VGroup(extra_dot_1, extra_dot_2,
                             extra_dot_3, extra_dot_4,
                             extra_dot_5, extra_dot_6,
                             extra_dot_7, extra_dot_8)

        g_odd_function = VGroup(t1, ul_t1, def_odd, def_odd_rectangle, g_graph,
                                 graph_1_label,
                                 graph_1_label_a1, graph_1_label_a2,
                                 graph_1_label_b1, graph_1_label_b2,
                                 odd_dots, dots_labels, more_dots).scale(0.8)
        


            # Diagrama para mostrar que x e -x têm imagens opostas
                # Domínio
        domain = Ellipse(width = 3, height = 4, fill_opacity = 0.2).shift(LEFT*2.5)
        domain_element_2 = MathTex('x').scale(1.3).move_to(domain.get_center()).shift(UP*0.6)
        domain_element_3 = MathTex('-x').scale(1.3).move_to(domain.get_center()).shift(DOWN*0.6+LEFT*0.25)
        domain_elements = VGroup(domain_element_2, domain_element_3)

                # Contradomínio
        codomain = Ellipse(width = 3, height = 4, color = BLUE, fill_opacity = 0.2).shift(RIGHT*2.5)
        codomain_element_1 = MathTex('y').scale(1.3).move_to(codomain.get_center()).shift(UP*0.6)
        codomain_element_2 = MathTex('-y').scale(1.3).move_to(codomain.get_center()).shift(DOWN*0.6+RIGHT*0.3)
        codomain_elements = VGroup(codomain_element_1, codomain_element_2)

        arrow_1 = CurvedArrow((-2.2, 0.6, 0), (2.2, 0.6, 0), radius = -5, stroke_width = 2.5)
        arrow_2 = CurvedArrow((-2.2, -0.6, 0), (2.2, -0.6, 0), radius = -5, stroke_width = 2.5)
        arrows = VGroup(arrow_1, arrow_2)



        g_diagram = VGroup(domain, domain_elements,
                           codomain, codomain_elements,
                           arrows).scale(0.6).shift(DOWN*1.2).set_z_index(3)
        
        
        
        
        # Animação

            # Título
        self.play(Succession(FadeIn(t1), Create(ul_t1)))
        self.wait(2)



            # Trocar sinal do argumento
        t2 = MathTex('f(+x)').scale(0.9).shift(UP*1)
        t3 = MathTex('f(-x)').scale(0.9)
        t4 = MathTex('-').scale(0.9).next_to(t2, LEFT, buff=0.1)
        black_rectangle_aux_1 = Rectangle(height=0.95, color=BLACK, fill_opacity=1).next_to(t2, UP, buff=0.1).set_z_index(2)
        black_rectangle_aux_2 = Rectangle(height=0.95, color=BLACK, fill_opacity=1).next_to(t2, DOWN, buff=0.1).set_z_index(2)

        self.play(FadeIn(t2))
        self.add(t3[0][2:4], black_rectangle_aux_1, black_rectangle_aux_2)
        self.play(t2[0][2:4].animate.shift(UP),
                   t3[0][2:4].animate.shift(UP))
        self.wait(2)
        self.play(FadeIn(t4))
        self.wait(2)
        self.play(FadeOut(t2[0][0:2], t2[0][4:5], t2[0][2:4], t3[0][2:4], t4))
        self.remove(black_rectangle_aux_1, black_rectangle_aux_2)
        self.wait(2)



            # Diagrama x e -x têm imagens opostas
        def_odd_aux = MathTex(r'f(-x)','=','-f(x)', color=YELLOW).scale(0.78).next_to(codomain, RIGHT, buff=0.3).set_z_index(5)        
        def_odd_aux[1].set_color(WHITE)

        self.play(FadeIn(g_diagram))
        self.wait(2)
        self.play(FadeIn(def_odd_aux[0]),
                  codomain_element_2.animate.set_color(YELLOW))
        self.wait(2)
        self.play(FadeIn(def_odd_aux[1]),
                  codomain_element_2.animate.set_color(WHITE),
                  def_odd_aux[0].animate.set_color(WHITE))
        self.wait(2)
        self.play(FadeIn(def_odd_aux[2]),
                  codomain_element_1.animate.set_color(YELLOW))
        self.wait(2)
        self.play(codomain_element_1.animate.set_color(WHITE),
                  def_odd_aux[2].animate.set_color(WHITE))



            # Definição de função ímpar   
        self.play(def_odd_aux.animate.move_to(def_odd).scale(0.9))
        self.play(FadeIn(def_odd_rectangle))
        self.wait(2)
        self.play(FadeOut(domain, domain_elements, codomain, codomain_elements, arrows))
        self.wait(2)



            # Gráfico da função ímpar, exemplo f(x) = x^3
        self.play(FadeIn(graph_1_label, axes, axes_labels))
        self.wait(2)
        self.play(FadeIn(graph_1_label_a1, x_label_a1, y_label_fa1,
                         odd_dot_a1, odd_dot_a1_dashedline1, odd_dot_a1_dashedline2))
        self.wait(2)
        self.play(FadeIn(graph_1_label_a2, x_label_a2, y_label_fa2,
                         odd_dot_a2, odd_dot_a2_dashedline1, odd_dot_a2_dashedline2))
        self.wait(2)
        self.play(FadeOut(graph_1_label_a1, graph_1_label_a2))
        self.wait(2)

        self.play(FadeIn(graph_1_label_b1, x_label_b1, y_label_fb1,
                         odd_dot_b1, odd_dot_b1_dashedline1, odd_dot_b1_dashedline2))
        self.wait(2)
        self.play(FadeIn(graph_1_label_b2, x_label_b2, y_label_fb2,
                         odd_dot_b2, odd_dot_b2_dashedline1, odd_dot_b2_dashedline2))
        self.wait(2)
        self.play(FadeOut(graph_1_label_b1, graph_1_label_b2))
        self.wait(2)

        self.play(LaggedStart(
            FadeIn(extra_dot_1, extra_dot_2),
            FadeIn(extra_dot_3, extra_dot_4),
            FadeIn(extra_dot_5, extra_dot_6),
            FadeIn(extra_dot_7, extra_dot_8),
            lag_ratio=0.4))
        self.wait(2)



            # Os pontos se transformam no gráfico da função f(x) = x^3
        g_dots = VGroup(odd_dot_a1, odd_dot_a2,
                        odd_dot_b1, odd_dot_b2,
                        more_dots)
        self.play(TransformMatchingShapes(g_dots, graph_1),
                  FadeOut(odd_dot_a1_dashedline1, odd_dot_a1_dashedline2,
                          odd_dot_a2_dashedline1, odd_dot_a2_dashedline2,
                          odd_dot_b1_dashedline1, odd_dot_b1_dashedline2,
                          odd_dot_b2_dashedline1, odd_dot_b2_dashedline2,
                          x_label_a1, x_label_a2, y_label_fa1, y_label_fa2,
                          x_label_b1, x_label_b2, y_label_fb1, y_label_fb2),
                          run_time = 2)
        self.wait(2)



        # Simetria em relação à origem

        dot_origin = Dot(axes.coords_to_point(0,0,0), color=YELLOW)
        self.play(FadeOut(graph_1_label))
        self.wait(2)
        self.play(GrowFromCenter(dot_origin))
        self.play(dot_origin.animate.set_color(WHITE))
        self.wait(2)

        dot_p = Dot(axes.coords_to_point(1.6,4.096,0), color=YELLOW)
        dot_p_symmetrical = Dot(axes.coords_to_point(-1.6,-4.096,0), color=YELLOW)
        #dot_p_symmetrical = always_redraw(lambda: Dot(axes.coords_to_point(-1 * dot_p.get_x(),-1 * dot_p.get_y(),0), color=YELLOW))

        distance_1 = always_redraw(lambda: Line(dot_p, axes.coords_to_point(0,0,0), color=YELLOW).set_opacity(0.7))
        distance_2 = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), dot_p_symmetrical, color=YELLOW).set_opacity(0.7))

        support_line = DashedLine(dot_p, dot_p_symmetrical, color=GRAY).scale(2).set_z_index(-1)

        self.play(GrowFromCenter(dot_p))
        self.wait(2)
        self.play(Create(distance_1))
        self.wait(2)
        self.play(Create(distance_2))
        self.wait(2)
        self.play(GrowFromCenter(dot_p_symmetrical))
        self.wait(2)
        self.play(FadeIn(support_line))
        self.wait(2)
        self.play(FadeOut(support_line))
        self.wait(2)
        self.play(MoveAlongPath(dot_p, graph_2),
                  MoveAlongPath(dot_p_symmetrical, graph_3), run_time = 3)
        self.wait(2)
        self.play(MoveAlongPath(dot_p, graph_4),
                  MoveAlongPath(dot_p_symmetrical, graph_5), run_time = 3)
        self.wait(2)
        self.play(FadeOut(dot_origin, dot_p, dot_p_symmetrical, distance_1, distance_2))
        self.wait(2)



        # Coordenadas da função ímpar
        dot_p.move_to(axes.coords_to_point(1.6,4.096,0))
        dot_p_symmetrical.move_to(axes.coords_to_point(-1.6,-4.096,0))

        dot_p_label = MathTex('(x,y)').scale(0.8).next_to(dot_p, DR, buff=0).shift(RIGHT*0.1)
        dot_p_symmetrical_label = MathTex('(-x,-y)').scale(0.8).next_to(dot_p_symmetrical, UL, buff=0).shift(LEFT*0.1)

        self.play(GrowFromCenter(dot_p))
        self.wait(2)
        self.play(FadeIn(dot_p_label))
        self.wait(2)
        self.play(GrowFromCenter(dot_p_symmetrical))
        self.wait(2)
        self.play(FadeIn(dot_p_symmetrical_label))
        self.wait(2)

            # Destaque nas coordenadas 'x'
        self.play(dot_p_label[0][1].animate.set_color(YELLOW),
                  dot_p_symmetrical_label[0][1:3].animate.set_color(YELLOW))
        self.wait(2)
        self.play(dot_p_label[0][1].animate.set_color(WHITE),
                  dot_p_symmetrical_label[0][1:3].animate.set_color(WHITE))
        self.wait(2)

            # Destaque nas coordenadas 'x'
        self.play(dot_p_label[0][3].animate.set_color(YELLOW),
                  dot_p_symmetrical_label[0][4:6].animate.set_color(YELLOW))
        self.wait(2)
        self.play(dot_p_label[0][3].animate.set_color(WHITE),
                  dot_p_symmetrical_label[0][4:6].animate.set_color(WHITE))
        self.wait(2)



            # Simetria em relação aos dois eixos ao mesmo tempo
        
        dot_aux = Dot(axes.coords_to_point(-1.6,4.096,0), color=GRAY)
        line_y_symmetry = DashedLine(dot_p, dot_aux, color=GRAY).set_z_index(-2)
        line_x_symmetry = DashedLine(dot_aux, dot_p_symmetrical, color=GRAY).set_z_index(-2)

                # Trocar 'x' por '-x' = simetria em relação ao eixo y
        self.play(Indicate(dot_p_label[0][1], scale_factor=1.2))
        self.wait(2)
        self.play(Indicate(dot_p_symmetrical_label[0][1:3], scale_factor=1.2))
        self.wait(2)
        self.play(Indicate(axes.get_y_axis(), scale_factor=1.05),
                  Create(line_y_symmetry))
        self.play(GrowFromCenter(dot_aux))
        self.wait(2)

                # Trocar 'y' por '-y' = simetria em relação ao eixo x
        self.play(Indicate(dot_p_label[0][3], scale_factor=1.2))
        self.wait(2)
        self.play(Indicate(dot_p_symmetrical_label[0][4:6], scale_factor=1.2))
        self.wait(2)
        self.play(Indicate(axes.get_x_axis(), scale_factor=1.05),
                  Create(line_x_symmetry))
        self.wait(2)



                # Duas reflexões seguidas

                    # Reflete 'y' depois 'x'
        self.add(graph_6, graph_7)
        self.play(FadeOut(graph_1,
                          dot_p, dot_p_symmetrical,
                          dot_p_label, dot_p_symmetrical_label,
                          line_y_symmetry, line_x_symmetry, dot_aux))
        self.wait(2)
        self.play(Rotate(graph_7, -180*DEGREES, axis=Y_AXIS, about_point=axes.coords_to_point(0,0,0)), run_time = 2)
        self.wait(2)
        self.play(Rotate(graph_7, -180*DEGREES, axis=X_AXIS, about_point=axes.coords_to_point(0,0,0)), run_time = 2)
        self.wait(2)
        
                    # Reflete 'x' depois 'y'
        self.play(FadeOut(graph_7))
        self.add(graph_8)

        self.wait(2)
        self.play(Rotate(graph_8, -180*DEGREES, axis=X_AXIS, about_point=axes.coords_to_point(0,0,0)), run_time = 2)
        self.wait(2)
        self.play(Rotate(graph_8, -180*DEGREES, axis=Y_AXIS, about_point=axes.coords_to_point(0,0,0)), run_time = 2)
        self.wait(2)
        





# Comentário sobre os nomes "par" e "ímpar"
class vid17(Scene):
    def construct(self):

        #l = Line(UP*3, DOWN*3).move_to(ORIGIN)
        #self.add(l)

        t = MathTex('f(x) = x^n').scale(0.8).to_edge(UP, buff=0.9)
        t_box = SurroundingRectangle(t, color=GRAY, stroke_width=2)

        # Par
        t2 = Tex('Par').scale(1.1).to_edge(UP).shift(RIGHT*0.3+DOWN*0.2)
        ul_t2 = Underline(t2)
        g_even = VGroup(t2, ul_t2).scale(0.8).to_edge(LEFT, buff=3.5)



        # Ímpar
        t1 = Tex('Ímpar').scale(1.1).to_edge(UP).shift(RIGHT*0.3+UP*0.02)
        ul_t1 = Underline(t1).set_z_index(3)
        g_odd = VGroup(t1, ul_t1).scale(0.8).to_edge(RIGHT, buff=3.25)
        


        # Funções pares x^n

        square_aux_1 = Square().scale(2.5).next_to(g_even, DOWN, buff=0.8)
        square_aux_2 = Square().scale(2.5).next_to(g_odd, DOWN, buff=0.8)



        axes_1 = Axes(x_range = [-3, 3, 1],
                    y_range = [-1, 6, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label_1 = MathTex("x").next_to(axes_1, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label_1 = MathTex("y").next_to(axes_1, UL, buff = -0.5).shift(UP*0.3).shift(RIGHT*1.65)
        axes_1_labels = VGroup(x_label_1, y_label_1)
        graph_1 = axes_1.plot(lambda x: x ** 2, x_range=[-2.3, 2.3], stroke_width = 4).set_color(BLUE)
        graph_1_label = MathTex('y = x^2', color=BLUE).scale(1.5).next_to(axes_1, UP, buff=0.5)
        g_graph_even_1 = VGroup(axes_1, graph_1, graph_1_label).scale(0.45).move_to(square_aux_1, aligned_edge=UL)



        axes_2 = Axes(x_range = [-3, 3, 1],
                    y_range = [-1, 6, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label_2 = MathTex("x").next_to(axes_2, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label_2 = MathTex("y").next_to(axes_2, UL, buff = -0.5).shift(UP*0.3).shift(RIGHT*1.65)
        axes_2_labels = VGroup(x_label_2, y_label_2)
        graph_2 = axes_2.plot(lambda x: x ** 4, x_range=[-1.516, 1.516], stroke_width = 4).set_color(BLUE)
        graph_2_label = MathTex('y = x^4', color=BLUE).scale(1.5).next_to(axes_2, UP, buff=0.5)
        g_graph_even_2 = VGroup(axes_2, graph_2, graph_2_label).scale(0.45).move_to(square_aux_1, aligned_edge=UR)



        axes_3 = Axes(x_range = [-6, 6, 1],
                    y_range = [-2, 2, 1],
                    x_length = 11.1,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label_3 = MathTex("x").next_to(axes_3, DR, buff = -0.5).shift(RIGHT*0.5+UP*1.6)
        y_label_3 = MathTex("y").next_to(axes_3, UL, buff = -0.5).shift(UP*0.3).shift(RIGHT*4.6)
        axes_3_labels = VGroup(x_label_3, y_label_3)
        graph_3 = axes_3.plot(lambda x: np.cos(x), x_range=[-6, 6], stroke_width = 4).set_color(BLUE)
        graph_3_label = MathTex('y = cos(x)', color=BLUE).scale(1.5).next_to(graph_3, UP).shift(RIGHT*3.7+UP*0.1)
        g_graph_even_3 = VGroup(axes_3, graph_3, graph_3_label).scale(0.45).move_to(square_aux_1, aligned_edge=DOWN).shift(DOWN*0.17)



        border_1 = SurroundingRectangle(g_graph_even_1, color=GRAY, stroke_width=2)
        border_2 = SurroundingRectangle(g_graph_even_2, color=GRAY, stroke_width=2)
        border_3 = SurroundingRectangle(g_graph_even_3, color=GRAY, stroke_width=2)        



        # Funções ímpares x^n

        axes_4 = Axes(x_range = [-3, 3, 1],
                    y_range = [-2.5, 2.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label_4 = MathTex("x").next_to(axes_4, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label_4 = MathTex("y").next_to(axes_4, UL, buff = -0.5).shift(UP*0.3).shift(RIGHT*1.65)
        axes_4_labels = VGroup(x_label_4, y_label_4)
        graph_4 = axes_4.plot(lambda x: x , x_range=[-2.3, 2.3], stroke_width = 4).set_color(BLUE)
        graph_4_label = MathTex('y = x','^1', color=BLUE).scale(1.5).next_to(axes_4, UP, buff=0.5).shift(RIGHT*0.1)
        graph_4_label[1].set_color(BLACK)
        g_graph_odd_4 = VGroup(axes_4, graph_4, graph_4_label).scale(0.45).move_to(square_aux_2, aligned_edge=UL)
        #.next_to(g_graph_even_2, RIGHT, buff=0.1)
        #.move_to(square_aux_2, aligned_edge=UL)



        axes_5 = Axes(x_range = [-3, 3, 1],
                    y_range = [-2.5, 2.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label_5 = MathTex("x").next_to(axes_5, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label_5 = MathTex("y").next_to(axes_5, UL, buff = -0.5).shift(UP*0.3).shift(RIGHT*1.65)
        axes_5_labels = VGroup(x_label_5, y_label_5)
        graph_5 = axes_5.plot(lambda x: 0.8 * x ** 3, x_range=[-1.46, 1.46], stroke_width = 4).set_color(BLUE)
        graph_5_label = MathTex('y = x^3', color=BLUE).scale(1.5).next_to(axes_5, UP,  buff=0.5)
        g_graph_odd_5 = VGroup(axes_5, graph_5, graph_5_label).scale(0.45).move_to(square_aux_2, aligned_edge=UR)



        axes_6 = Axes(x_range = [-6, 6, 1],
                    y_range = [-2, 2, 1],
                    x_length = 11.1,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label_6 = MathTex("x").next_to(axes_6, DR, buff = -0.5).shift(RIGHT*0.5+UP*1.6)
        y_label_6 = MathTex("y").next_to(axes_6, UL, buff = -0.5).shift(UP*0.3).shift(RIGHT*4.6)
        axes_6_labels = VGroup(x_label_6, y_label_6)
        graph_6 = axes_6.plot(lambda x: np.sin(x), x_range=[-6, 6], stroke_width = 4).set_color(BLUE)
        graph_6_label = MathTex('y = sen(x)', color=BLUE).scale(1.5).next_to(graph_6, UP).shift(RIGHT*3.7+UP*0.1)
        g_graph_odd_6 = VGroup(axes_6, graph_6, graph_6_label).scale(0.45).move_to(square_aux_2, aligned_edge=DOWN).shift(DOWN*0.17)



        border_4 = SurroundingRectangle(g_graph_odd_4, color=GRAY, stroke_width=2)
        border_5 = SurroundingRectangle(g_graph_odd_5, color=GRAY, stroke_width=2)
        border_6 = SurroundingRectangle(g_graph_odd_6, color=GRAY, stroke_width=2)        



        # Animação

        self.play(FadeIn(g_even, g_odd))
        self.wait(2)
        self.play(FadeIn(t, t_box))
        self.wait(2)

        self.play(FadeIn(g_graph_even_1, border_1)) # y = x^2
        self.wait(2)
        self.play(FadeIn(g_graph_even_2, border_2)) # y = x^4
        self.wait(2)

        self.play(FadeIn(g_graph_odd_4, border_4)) # y = x^1
        self.wait(2)
        self.play(FadeIn(g_graph_odd_5, border_5)) # y = x^3
        self.wait(2)

        self.play(FadeOut(t, t_box))
        self.wait(2)
        self.play(FadeIn(g_graph_even_3, border_3)) # y = cos(x)
        self.wait(2)
        self.play(FadeIn(g_graph_odd_6, border_6)) # y = sen(x)
        self.wait(2)


        self.add(g_odd, g_even, t, t_box, #square_aux_1, square_aux_2,
                 g_graph_even_1, g_graph_even_2, g_graph_even_3,
                 g_graph_odd_4, g_graph_odd_5, g_graph_odd_6,
                 border_1, border_2, border_3,
                 border_4, border_5, border_6,
                 graph_1_label, graph_2_label, graph_3_label)
        





# Zeros da função
class vid18(Scene):
    def construct(self):

        axes = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3)
        axes_labels = VGroup(x_label, y_label)
        axes_zero = MathTex('0', color=YELLOW).scale(0.8).next_to(axes.coords_to_point(0,0,0), LEFT, buff = 0.2)
        axes_zero_back = Square(color=BLACK, stroke_width = 0).set_opacity(0.7).next_to(axes.coords_to_point(0,0,0), LEFT, buff = 0.03).set_z_index(7)

        graph_1 = axes.plot(lambda x: 2*x - 3,
                            x_range=[1, 3.5], stroke_width = 4).set_color(BLUE).set_z_index(2)     
        graph_2 = axes.plot(lambda x: (x-2.5)**2 + 0.7,
                            x_range=[0.683, 4.317], stroke_width = 4).set_color(BLUE).set_z_index(2)     
        graph_3 = axes.plot(lambda x: -1.5*(x-2)**2 + 3.5,
                            x_range=[0.268, 3.732], stroke_width = 4).set_color(BLUE).set_z_index(2)     
        
        
        
        root_1 = Dot(graph_1.get_point_from_function(t=3/2), color=YELLOW)
        fx_dashedline = DashedLine(root_1, axes.coords_to_point(0,0,0), color=YELLOW, stroke_opacity=0.7, stroke_width = 6)

        root_3_a = Dot(graph_3.get_point_from_function(t=0.472), color=YELLOW)
        root_3_b = Dot(graph_3.get_point_from_function(t=3.528), color=YELLOW)

        g_graph = VGroup(axes, axes_labels, axes_zero, graph_1, graph_2, graph_3,
                         root_1, fx_dashedline, root_3_a, root_3_b).shift(DOWN*0.5).set_z_index(6)
        axes_zero.set_z_index(8)

        t1 = Tex(f'\it Zero ',' da função', color=WHITE).scale(0.7).next_to(root_1, DR, buff=0.1)
        t2 = Tex(f'\it (ou raiz)', color=GRAY).scale(0.7).next_to(t1, DOWN, buff=0.1).shift(LEFT*0.8)



        # Função com 1 zero
        self.play(FadeIn(axes, axes_labels))
        self.play(Create(graph_1))
        self.wait(2)
        self.play(GrowFromCenter(root_1))
        self.wait(2)
        self.play(Create(fx_dashedline))
        self.play(FadeIn(axes_zero, axes_zero_back))
        self.wait(2)
        self.play(Write(t1[0]))
        self.wait(2)
        self.play(FadeIn(t2))
        self.wait(2)
        self.play(Write(t1[1]))
        self.wait(2)

        self.play(FadeOut(graph_1, fx_dashedline, root_1, t1, t2),
                  axes_zero.animate.next_to(axes, DL, buff = -0.7).set_color(WHITE),
                  FadeOut(axes_zero_back))



        # Função sem zeros
        self.play(Create(graph_2))
        self.wait(2)

        self.play(FadeOut(graph_2))



        # Função com mais de 1 zero
        self.play(Create(graph_3))
        self.wait(2)
        self.play(LaggedStart(
            GrowFromCenter(root_3_a),
            GrowFromCenter(root_3_b),
            lag_ratio=0.2))
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)



        # Encontar os zeros de uma função
        t3 = MathTex(r'f(x) = 2x - 2',
                     r'&= 0',
                     r'\\ 2x &= 2',
                     r'\\ x &= 1', color=WHITE).scale(0.8)
        t3[0].set_color(BLUE)
        t3[1].set_color(WHITE)

        t4 = MathTex('g(x) = \ln(x^2 + 1) - \ln(2)',
                     r'&= 0',
                     r'\\ \ln(x^2 + 1) &= \ln(2)',
                     r'\\ e^{\ln(x^2 + 1)} &= e^{\ln(2)}',
                     r'\\ x^2 + 1 &= 2',
                     r'\\ x^2 &= 1',
                     r'\\ x &= \pm 1', color=WHITE).scale(0.8)
        t4[0].set_color(RED)
        t4[1].set_color(WHITE)

        g_1 = VGroup(t3, t4).arrange(RIGHT, aligned_edge=UP, buff = 2.5)

        t3_box = SurroundingRectangle(t3[3], buff=0.15, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-1)
        t4_box = SurroundingRectangle(t4[6], buff=0.15, stroke_width=0, color = GRAY).set_opacity(0.3).set_z_index(-1)

        self.play(LaggedStart(
            FadeIn(t3[0]),
            FadeIn(t4[0]),
            lag_ratio=0.3))
        self.wait(2)
        self.play(Write(t3[1]),
                  Write(t4[1]))
        self.wait(2)
        self.play(Succession(
            FadeIn(t3[2]),
            FadeIn(t3[3]),
            FadeIn(t3_box)))
        self.wait(2)
        self.play(Succession(
            FadeIn(t4[2]),
            FadeIn(t4[3]),
            FadeIn(t4[4]),
            FadeIn(t4[5]),
            FadeIn(t4[6]),
            FadeIn(t4_box)))
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects]) # FadeOut de toda a cena
        self.wait(2)
