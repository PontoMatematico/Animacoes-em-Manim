# Trigonometria

from manim import *

import numpy as np

# Triângulo retângulo
class vid1(MovingCameraScene):
    
    def angle_between(self, v1, v2):    # Calcula o ângulo entre dois vetores em graus
        cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.degrees(np.arccos(cos_theta))

    def construct(self):
        
        # Criando pontos e linhas iniciais do triângulo
        dot_A = Dot([-1.99, 0.2, 0]).scale(0)
        dot_B = Dot([1.34, 1.31, 0]).scale(0)  
        dot_C = Dot([0.63, -2.12, 0]).scale(0) 

        line_AB = Line(dot_A, dot_B, color=WHITE)
        line_BC = Line(dot_B, dot_C, color=WHITE)
        line_CA = Line(dot_C, dot_A, color=WHITE)

        # Funções de atualização para os ângulos e linhas
        def update_triangle(mob):
            # Calculando os vetores atualizados
            AB = dot_B.get_center() - dot_A.get_center()
            BC = dot_C.get_center() - dot_B.get_center()
            CA = dot_A.get_center() - dot_C.get_center()

            # Calculando os ângulos internos
            angle_A = self.angle_between(AB, -CA)
            angle_B = self.angle_between(BC, -AB)
            angle_C = self.angle_between(CA, -BC)

            # Atualizando textos dos ângulos
            angle_A_text.become(MathTex(f"{angle_A:.0f}^\\circ").scale(0.7).move_to(Angle.from_three_points(dot_B, dot_A, dot_C, radius=0.9, other_angle=True)))
            angle_B_text.become(MathTex(f"{angle_B:.0f}^\\circ").scale(0.7).move_to(Angle.from_three_points(dot_A, dot_B, dot_C, radius=0.8)))
            angle_C_text.become(MathTex(f"{angle_C:.0f}^\\circ").scale(0.7).move_to(Angle.from_three_points(dot_B, dot_C, dot_A, radius=0.9)))

            # Atualizando as linhas do triângulo
            line_AB.put_start_and_end_on(dot_A.get_center(), dot_B.get_center())
            line_BC.put_start_and_end_on(dot_B.get_center(), dot_C.get_center())
            line_CA.put_start_and_end_on(dot_C.get_center(), dot_A.get_center())

        # Criando ângulos como textos para serem atualizados
        COLOR_ANGLE_1 = PURPLE
        COLOR_ANGLE_2 = GREEN
        COLOR_ANGLE_3 = RED

        angle_A = always_redraw(lambda: Angle.from_three_points(dot_B.get_center(), dot_A.get_center(), dot_C.get_center(), radius=0.2, stroke_width=40, color=COLOR_ANGLE_1, other_angle=True).set_z_index(-1))        
        angle_B = always_redraw(lambda: Angle.from_three_points(dot_A.get_center(), dot_B.get_center(), dot_C.get_center(), radius=0.2, stroke_width=40, color=COLOR_ANGLE_2).set_z_index(-1))       
        angle_C = always_redraw(lambda: Angle.from_three_points(dot_B.get_center(), dot_C.get_center(), dot_A.get_center(), radius=0.2, stroke_width=40, color=COLOR_ANGLE_3).set_z_index(-1))
        
        angle_A_text = MathTex("0^\\circ")
        angle_B_text = MathTex("0^\\circ")
        angle_C_text = MathTex("0^\\circ")

        for mob in [line_AB, line_BC, line_CA, angle_A_text, angle_B_text, angle_C_text]:
            mob.add_updater(update_triangle)
        



        # Animação

        # Desenhando o triângulo
        dot_1 = Dot((-1.99, 0.2, 0), color=BLUE_E).scale(0.7).set_z_index(3)

        path = VMobject(color=BLUE)
        path.set_points_as_corners([dot_1.get_center(), dot_1.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot_1.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.2).move_to(dot_1))
        def update_curve(mob):
            mob.move_to(dot_1.get_center())
        self.camera.frame.add_updater(update_curve)

        self.add(path)
        self.play(GrowFromCenter(dot_1))
        self.play(dot_1.animate.move_to(dot_B))
        self.play(dot_1.animate.move_to(dot_C))
        self.play(dot_1.animate.move_to(dot_A))
        self.camera.frame.remove_updater(update_curve)

        triangle_1 = always_redraw(lambda: Polygon(dot_A.get_center(), dot_B.get_center(), dot_C.get_center(), color=BLUE, fill_opacity=0).set_z_index(2))
        self.add(triangle_1, dot_A, dot_B, dot_C, line_AB, line_BC, line_CA).remove(path, dot_1)
        self.play(dot_1.animate.scale(0),
                  Restore(self.camera.frame),
                  #self.camera.frame.animate.scale(5).move_to((0,2,0)), 
                  run_time=2)
        self.wait(2)

    

        # A soma dos ângulos é sempre 180°
        self.play(FadeIn(angle_A, angle_B, angle_C,
                         angle_A_text, angle_B_text, angle_C_text,
                         line_AB, line_BC, line_CA))
        self.wait(2)

        sum_of_angles_text = MathTex(r'OO + OO + 90^{\circ} = 180^{\circ}').scale(0.9).to_corner(UL, buff=1)
        sum_of_angles_text[0][9:14].shift(LEFT*0.2)

        angle_A_copy = always_redraw(lambda: angle_A.copy().move_to(sum_of_angles_text[0][0:2]).shift(DOWN*0.05))
        angle_B_copy = always_redraw(lambda: angle_B.copy().move_to(sum_of_angles_text[0][3:5]).shift(UP*0.05))
        angle_C_copy = always_redraw(lambda: angle_C.copy().move_to(sum_of_angles_text[0][6:9]).shift(DOWN*0.05))

        self.play(LaggedStart(ReplacementTransform(angle_A.copy(), angle_A_copy),
                              FadeIn(sum_of_angles_text[0][2]),
                              ReplacementTransform(angle_B.copy(), angle_B_copy),
                              FadeIn(sum_of_angles_text[0][5]),
                              TransformFromCopy(angle_C, angle_C_copy),
                              FadeIn(sum_of_angles_text[0][9:14]),
                              lag_ratio=0.2))
        self.wait(2)



        # Mudando o formato do triângulo
        self.play(dot_A.animate.move_to([-2.5, -1, 0]),
                  dot_B.animate.move_to([0, 1, 0]),
                  dot_C.animate.move_to([2, -0.5, 0]))
        
        self.play(dot_A.animate.move_to([-3, -1, 0]),
                  dot_B.animate.move_to([1, 2, 0]),
                  dot_C.animate.move_to([1, -1.5, 0]))
        
        self.play(dot_A.animate.move_to([-0.5, -2, 0]),
                  dot_B.animate.move_to([0.5, 1.5, 0]),
                  dot_C.animate.move_to([2.5, -1, 0]))
        
        self.wait(2)



        # Triângulo retângulo: um dos ângulos é 90°
        t2 = Tex('Triângulo retângulo', color=WHITE).shift(DOWN*2.2)
        t2_arrow = Arrow(UR, DL).scale(0.5).next_to(t2, DOWN, buff=0.5).shift(LEFT*0.8)

        self.play(dot_A.animate.move_to([-2, -1.5, 0]),
                  dot_B.animate.move_to([2, 1.2, 0]),
                  dot_C.animate.move_to([2, -1.5, 0]))
                
        angle_90 = RightAngle(Line(dot_A, dot_C), Line(dot_C, dot_B), stroke_width=3, quadrant=(-1,1), length=0.3, color=COLOR_ANGLE_3)
        angle_90_dot = Dot(color=COLOR_ANGLE_3).scale(0.5).move_to(angle_90)

        self.add(angle_90, angle_90_dot).remove(angle_C)
        self.play(FadeIn(t2),
                  FadeTransform(angle_C_copy, sum_of_angles_text[0][6:9]),
                  sum_of_angles_text[0][5].animate.shift(LEFT*0.1),
                  sum_of_angles_text[0][9:14].animate.shift(RIGHT*0.2))
        self.wait(2)

        self.play(Flash(angle_90, num_lines=8, line_length=0.35, flash_radius=0.2))
        self.wait(2)



        # Ângulos complementares
        t3 = MathTex(r'x + y = 90^{\circ}').to_corner(UR, buff=1)
        t3[0][4:6].scale(0.9)
        t4 = Tex('\it Complementares', color=GRAY).scale(0.9).next_to(t3, DOWN)
        t4_arrow_1 = Arrow(t4, t3[0][0], color=GRAY)
        t4_arrow_2 = Arrow(t4, t3[0][2], color=GRAY)

        self.play(FadeIn(t3, t4))
        self.wait(2)

        brace_1 = Brace(sum_of_angles_text[0][0:9], DOWN, color=GRAY)
        brace_2 = Brace(sum_of_angles_text[0][0:5], DOWN, color=GRAY)
        brace_2_label = MathTex(r'90^{\circ}', color=GRAY).scale(0.9).next_to(brace_2, DOWN)

        self.play(FadeIn(brace_1))
        self.wait(2)
        self.play(ReplacementTransform(brace_1, brace_2))
        self.play(FadeIn(brace_2_label))
        self.wait(2)

        angle_A_text_aux = angle_A_text.copy()
        angle_B_text_aux = angle_B_text.copy()
        angle_C_text_aux = angle_C_text.copy()

        self.remove(angle_A_text, 
                    angle_B_text, 
                    angle_C_text).add(angle_A_text_aux, 
                                      angle_B_text_aux, 
                                      angle_C_text_aux)
        
        angle_A_aux1 = angle_A.copy()
        angle_A_aux2 = Angle.from_three_points(dot_B.get_center(), dot_A.get_center(), dot_C.get_center(), radius=0.3, stroke_width=55, color=COLOR_ANGLE_1, other_angle=True).set_z_index(-1)
        self.remove(angle_A).add(angle_A_aux1)
        self.play(FadeOut(angle_A_text_aux, angle_B_text_aux, angle_C_text_aux),
                  ReplacementTransform(angle_A_aux1, angle_A_aux2))
        self.play(LaggedStart(t3[0][0].animate.move_to(angle_A_text_aux),
                              t3[0][2].animate.move_to(angle_B_text_aux),
                              FadeOut(t3[0][1], t3[0][3:7], t4),
                              lag_ratio=0.2))
        self.wait(2)
        self.play(FadeOut(t2, brace_2, brace_2_label, angle_A_copy, angle_B_copy,
                          sum_of_angles_text[0][2], sum_of_angles_text[0][5:14]))
        self.wait(2)


        
# Triângulos semelhantes
class vid2(MovingCameraScene):
    def construct(self):
        
        # Retomando o triângulo
        dot_A = Dot([-2, -1.5, 0]).scale(0)
        dot_B = Dot([2, 1.2, 0]).scale(0)
        dot_C = Dot([2, -1.5, 0]).scale(0)

        COLOR_ANGLE_1 = PURPLE
        COLOR_ANGLE_2 = GREEN
        COLOR_ANGLE_3 = RED

        angle_A = always_redraw(lambda: Angle.from_three_points(dot_B.get_center(), dot_A.get_center(), dot_C.get_center(), radius=0.3, stroke_width=55, color=COLOR_ANGLE_1, other_angle=True).set_z_index(-1))        
        angle_B = always_redraw(lambda: Angle.from_three_points(dot_A.get_center(), dot_B.get_center(), dot_C.get_center(), radius=0.2, stroke_width=40, color=COLOR_ANGLE_2).set_z_index(-1))       
        angle_90 = always_redraw(lambda: RightAngle(Line(dot_A, dot_C), Line(dot_C, dot_B), stroke_width=3, quadrant=(-1,1), length=0.3, color=COLOR_ANGLE_3))
        angle_90_dot = always_redraw(lambda: Dot(color=COLOR_ANGLE_3).scale(0.5).move_to(angle_90))
        
        angle_A_label = always_redraw(lambda: MathTex('x').scale(0.9).move_to(Angle.from_three_points(dot_B, dot_A, dot_C, radius=0.9, other_angle=True)).set_z_index(5))
        angle_B_label = always_redraw(lambda: MathTex('y').scale(0.9).move_to(Angle.from_three_points(dot_A, dot_B, dot_C, radius=0.8)).set_z_index(5))

        triangle_1 = always_redraw(lambda: Polygon(dot_A.get_center(), dot_B.get_center(), dot_C.get_center(), color=BLUE, fill_opacity=0).set_z_index(2))
        triangle_1_fill = always_redraw(lambda: triangle_1.copy().set_color(BLACK).set_opacity(1).move_to(triangle_1, aligned_edge=DL).set_z_index(-3))
        
        self.add(triangle_1, triangle_1_fill, angle_A, angle_B, angle_90, angle_90_dot, angle_A_label, angle_B_label)



        # Mudando a escala do triângulo
        triangle_2 = triangle_1.copy().scale(1.45).move_to(triangle_1, aligned_edge=DL).set_z_index(-4)
        triangle_3 = triangle_1.copy().scale(1.25).move_to(triangle_1, aligned_edge=DL).set_z_index(-4)
        triangle_4 = triangle_1.copy().scale(1.3).move_to(triangle_1, aligned_edge=DL).set_z_index(-4)

        self.play(TransformFromCopy(triangle_1, triangle_2), run_time=2)
        self.play(ReplacementTransform(triangle_2, triangle_3))
        self.play(ReplacementTransform(triangle_3, triangle_4))
        self.wait(2)

        self.play(dot_A.animate.shift(LEFT*3.3),
                  dot_B.animate.shift(LEFT*3.3),
                  dot_C.animate.shift(LEFT*3.3),
                  triangle_4.animate.shift(RIGHT*2),
                  run_time=2.5)
        self.wait(2)

        

        # Os ângulos se mantêm iguais
        angle_A_4 = angle_A.copy().move_to(triangle_4, aligned_edge=DL).shift(RIGHT*0.25)
        angle_A_4_label = angle_A_label.copy().next_to(angle_A_4, RIGHT, buff=0.3, aligned_edge=DOWN).shift(UP*0.15+RIGHT*0.1)

        angle_B_4 = angle_B.copy().move_to(triangle_4, aligned_edge=UR).shift(DOWN*0.1)
        angle_B_4_label = angle_B_label.copy().next_to(angle_B_4, DOWN, buff=0.3, aligned_edge=LEFT).shift(LEFT*0.27)

        angle_90_4 = angle_90.copy().move_to(triangle_4, aligned_edge=DR)
        angle_90_dot_4 = angle_90_dot.copy().move_to(angle_90_4)

        g_angle_A = VGroup(angle_A, angle_A_label)
        g_angle_B = VGroup(angle_B, angle_B_label)
        g_angle_90 = VGroup(angle_90, angle_90_dot)
        
        g_angle_A_4 = VGroup(angle_A_4, angle_A_4_label)
        g_angle_B_4 = VGroup(angle_B_4, angle_B_4_label)
        g_angle_90_4 = VGroup(angle_90_4, angle_90_dot_4)

        g_angle_A_copy = g_angle_A.copy()
        g_angle_B_copy = g_angle_B.copy()
        g_angle_90_copy = g_angle_90.copy()

        self.play(LaggedStart(ClockwiseTransform(g_angle_90_copy, g_angle_90_4, path_arc=-np.pi/2),
                              ClockwiseTransform(g_angle_B_copy, g_angle_B_4, path_arc=-np.pi/2),
                              ClockwiseTransform(g_angle_A_copy, g_angle_A_4, path_arc=-np.pi/2),
                              lag_ratio=0.2))
        self.remove(g_angle_90_copy, g_angle_A_copy, g_angle_B_copy)
        self.add(g_angle_90_4, g_angle_B_4, g_angle_A_4)
        self.wait(2)



        # Os tamanhos dos lados são alterados
        side_a_label = MathTex('3', color=WHITE).next_to(triangle_1, RIGHT, buff=0.2)
        side_b_label = MathTex('4', color=WHITE).next_to(triangle_1, DOWN, buff=0.2)
        side_c_label = MathTex('5', color=WHITE).next_to(triangle_1, UL, buff=-1.5).shift(UP*0.3+RIGHT*0.35)

        self.play(FadeIn(side_a_label, side_b_label, side_c_label))
        self.wait(2)

        side_ka_label = MathTex(r'k \cdot 3', color=WHITE).next_to(triangle_4, RIGHT, buff=0.2)
        side_kb_label = MathTex(r'k \cdot 4', color=WHITE).next_to(triangle_4, DOWN, buff=0.2)
        side_kc_label= MathTex(r'k \cdot 5', color=WHITE).next_to(triangle_4, UL, buff=-2).shift(UP*0.3+RIGHT*0.4)
       
        side_2a_label = MathTex(r'2 \cdot 3', color=WHITE).next_to(triangle_4, RIGHT, buff=0.2)
        side_2b_label = MathTex(r'2 \cdot 4', color=WHITE).next_to(triangle_4, DOWN, buff=0.2)
        side_2c_label= MathTex(r'2 \cdot 5', color=WHITE).next_to(triangle_4, UL, buff=-2).shift(UP*0.3+RIGHT*0.4)
        
        g1 = VGroup(side_2a_label[0][0], side_2b_label[0][0], side_2c_label[0][0]).set_color(YELLOW)

        side_a_label_copy = side_a_label.copy()
        side_b_label_copy = side_b_label.copy()
        side_c_label_copy = side_c_label.copy()

        self.play(LaggedStart(ClockwiseTransform(side_a_label_copy, side_ka_label, path_arc=-np.pi/2),
                              ClockwiseTransform(side_b_label_copy, side_kb_label, path_arc=-np.pi/2),
                              ClockwiseTransform(side_c_label_copy, side_kc_label, path_arc=-np.pi/2),
                              lag_ratio=0.2))
        self.remove(side_a_label_copy, side_b_label_copy, side_c_label_copy)
        self.add(side_ka_label, side_kb_label, side_kc_label)
        self.wait(2)
        self.play(side_ka_label[0][0].animate.set_color(YELLOW),
                  side_kb_label[0][0].animate.set_color(YELLOW),
                  side_kc_label[0][0].animate.set_color(YELLOW))
        self.remove(side_a_label_copy, side_b_label_copy, side_c_label_copy)
        self.wait(2)
        self.play(ReplacementTransform(side_ka_label, side_2a_label),
                  ReplacementTransform(side_kb_label, side_2b_label),
                  ReplacementTransform(side_kc_label, side_2c_label))
        self.wait(2)



        # As razões entre os lados são iguais
        black_sq_1 = Square(color=BLACK).scale(5).set_opacity(0.7).move_to(triangle_1, aligned_edge=UR).shift(UP*0.1+RIGHT*0.5).set_z_index(6)
        black_sq_2 = black_sq_1.copy().move_to(triangle_4, aligned_edge=UL).shift(UP*0.1+LEFT*0.1)
        
        black_sq_1_down = black_sq_1.copy().next_to(triangle_1, DOWN, aligned_edge=RIGHT, buff=0).shift(UP*0.008+RIGHT*0.1).set_z_index(3)
        black_sq_2_down = black_sq_1.copy().next_to(triangle_4, DOWN, aligned_edge=LEFT, buff=0).shift(UP*0.008+LEFT*0.1).set_z_index(3)

        self.play(self.camera.frame.animate.shift(UP), FadeIn(black_sq_2, black_sq_1_down))
        
        ratio_1 = MathTex(r'\frac{3}{5}',r'\hspace{1cm} = \hspace{1cm}',r'\frac{2 \cdot 3}{2 \cdot 5}').to_edge(UP, buff=0.3)
        ratio_2 = MathTex(r'\frac{3}{5}').move_to(ratio_1[2])
        ratio_3 = MathTex(r'\frac{3}{5}').to_edge(UP, buff=0.3).shift(LEFT*1.5)



            # Razão do primeiro triângulo
        self.play(LaggedStart(TransformFromCopy(side_a_label, ratio_1[0][0]),
                              FadeIn(ratio_1[0][1]),
                              TransformFromCopy(side_c_label, ratio_1[0][2]),
                              lag_ratio=0.2))
        self.wait(2)

            # Razão do segundo triângulo
        self.play(FadeOut(black_sq_2, black_sq_1_down), FadeIn(black_sq_1, black_sq_2_down))
        self.play(LaggedStart(TransformFromCopy(side_2a_label, ratio_1[2][0:3]),
                              FadeIn(ratio_1[2][3]),
                              TransformFromCopy(side_2c_label, ratio_1[2][4:7]),
                              lag_ratio=0.2))
        self.wait(2)

            # As razões são iguais
        red_line1 = Line(UP*0.2, DOWN*0.2, color=RED, stroke_width=4).scale(2).rotate(50*DEGREES).move_to(ratio_1[2][0])
        red_line2 = red_line1.copy().move_to(ratio_1[2][4])
        
        self.play(Create(red_line1), Create(red_line2))
        self.play(FadeOut(red_line1, red_line2, black_sq_1, black_sq_2_down),
                  FadeTransform(ratio_1[2], ratio_2, stretch=False))
        self.wait(2)
        self.play(ratio_1[0].animate.set_color(YELLOW),
                  ratio_2.animate.set_color(YELLOW))
        self.wait(2)



        # Essa razão pertence à família de triângulos semelhantes      
        self.wait(2)
        g2 = VGroup(ratio_1[0], ratio_2)
        self.play(dot_A.animate.shift(RIGHT*2),
                  dot_B.animate.shift(RIGHT*2),
                  dot_C.animate.shift(RIGHT*2),
                  ReplacementTransform(g2, ratio_3),
                  FadeOut(triangle_4, g_angle_90_4, g_angle_B_4, g_angle_A_4,
                          side_a_label, side_b_label, side_c_label,
                          side_2a_label, side_2b_label, side_2c_label))
        self.wait(2)

        COLOR_1 = YELLOW
        triangle_5 = always_redraw(lambda: triangle_1.copy().set_color(COLOR_1).set_stroke(opacity=0.3).set_fill(opacity=0).scale(0.4).move_to(triangle_1, aligned_edge=DL).set_z_index(4))
        triangle_6 = always_redraw(lambda: triangle_1.copy().set_color(COLOR_1).set_stroke(opacity=0.3).set_fill(opacity=0).scale(0.6).move_to(triangle_1, aligned_edge=DL).set_z_index(4))
        triangle_7 = always_redraw(lambda: triangle_1.copy().set_color(COLOR_1).set_stroke(opacity=0.3).set_fill(opacity=0).scale(0.8).move_to(triangle_1, aligned_edge=DL).set_z_index(4))
        triangle_8 = always_redraw(lambda: triangle_1.copy().set_color(COLOR_1).set_stroke(opacity=0.3).set_fill(opacity=0).scale(1.2).move_to(triangle_1, aligned_edge=DL).set_z_index(-4))
        triangle_9 = always_redraw(lambda: triangle_1.copy().set_color(COLOR_1).set_stroke(opacity=0.3).set_fill(opacity=0).scale(1.4).move_to(triangle_1, aligned_edge=DL).set_z_index(-4))
        triangle_10 = always_redraw(lambda: triangle_1.copy().set_color(COLOR_1).set_stroke(opacity=0.3).set_fill(opacity=0).scale(1.6).move_to(triangle_1, aligned_edge=DL).set_z_index(-4))
        triangle_11 = always_redraw(lambda: triangle_1.copy().set_color(COLOR_1).set_stroke(opacity=0.3).set_fill(opacity=0).scale(1.8).move_to(triangle_1, aligned_edge=DL).set_z_index(-4))

        self.play(LaggedStart(TransformFromCopy(triangle_1, triangle_5),
                              TransformFromCopy(triangle_1, triangle_6),
                              TransformFromCopy(triangle_1, triangle_7),
                              lag_ratio=0.1),
                  LaggedStart(TransformFromCopy(triangle_1, triangle_8),
                              TransformFromCopy(triangle_1, triangle_9),
                              TransformFromCopy(triangle_1, triangle_10),
                              TransformFromCopy(triangle_1, triangle_11),
                              lag_ratio=0.1))
        self.wait(2)



        # A razão pertence aos ângulos 'x' e 'y'
        self.play(dot_B.animate.shift(UP*0.5+LEFT*0.8),
                  dot_C.animate.shift(LEFT*0.8))

        self.play(dot_B.animate.shift(DOWN*1+RIGHT*2),
                  dot_C.animate.shift(RIGHT*2))
        
        self.play(dot_B.animate.shift(UP*0.5+LEFT*1.2),
                  dot_C.animate.shift(LEFT*1.2))
        
        self.wait(2)

        ratio_3_ref = Dot(ratio_3.get_center()).shift(DOWN*0.65)
        g_angle_A_ref = Dot(g_angle_A.get_center()).shift(UP*0.4+LEFT*0.1)
        g_angle_B_ref = Dot(g_angle_B.get_center()).shift(UP*0.5)

        arrow_1 = CurvedArrow(ratio_3_ref.get_center(), g_angle_A_ref.get_center(), radius=5)
        arrow_2 = CurvedArrow(ratio_3_ref.get_center(), g_angle_B_ref.get_center(), radius=3)

        self.play(FadeIn(arrow_1, arrow_2))
        self.wait(2)



# Nomes dos lados e das razões
class vid3(MovingCameraScene):
    def construct(self):
        
        # Retomando o triângulo
        dot_A = Dot([-2, -1.5, 0]).scale(0)
        dot_B = Dot([2, 1.2, 0]).scale(0)
        dot_C = Dot([2, -1.5, 0]).scale(0)

        COLOR_ANGLE_1 = PURPLE
        COLOR_ANGLE_2 = GREEN
        COLOR_ANGLE_3 = RED

        angle_A = Angle.from_three_points(dot_B.get_center(), dot_A.get_center(), dot_C.get_center(), radius=0.3, stroke_width=55, color=COLOR_ANGLE_1, other_angle=True).set_z_index(-1)
        angle_B = Angle.from_three_points(dot_A.get_center(), dot_B.get_center(), dot_C.get_center(), radius=0.2, stroke_width=40, color=COLOR_ANGLE_2).set_z_index(-1)     
        angle_90 = always_redraw(lambda: RightAngle(Line(dot_A, dot_C), Line(dot_C, dot_B), stroke_width=3, quadrant=(-1,1), length=0.3, color=COLOR_ANGLE_3))
        angle_90_dot = always_redraw(lambda: Dot(color=COLOR_ANGLE_3).scale(0.5).move_to(angle_90))
        
        angle_A_label = MathTex('x').scale(0.9).move_to(Angle.from_three_points(dot_B, dot_A, dot_C, radius=0.9, other_angle=True)).set_z_index(5)
        angle_B_label = MathTex('y').scale(0.9).move_to(Angle.from_three_points(dot_A, dot_B, dot_C, radius=0.8)).set_z_index(5)

        triangle_1 =  Polygon(dot_A.get_center(), dot_B.get_center(), dot_C.get_center(), color=WHITE, fill_opacity=0).set_z_index(2)
        
        side_a = Line(dot_B, dot_C, color=YELLOW).scale(1.01).set_z_index(3)
        side_b = Line(dot_A, dot_C, color=YELLOW).scale(1.01).set_z_index(3)
        side_c = Line(dot_A, dot_B, color=YELLOW).scale(1.01).set_z_index(3)

        side_a_label = Tex(r'Cateto',r'\par oposto', color=YELLOW).scale(0.9).next_to(side_b, DOWN, buff=0.2)
        side_b_label = Tex(r'Cateto',r'\par adjacente', color=YELLOW).scale(0.9).next_to(side_a, RIGHT, buff=0.2)
        side_b_label[0].shift(LEFT*0.2)
        side_c_label = Tex('Hipotenusa', color=YELLOW).rotate(34*DEGREES).scale(0.9).next_to(side_a, UL, buff=-0.5).shift(DOWN*1.2+LEFT*1.7)

        #self.add(triangle_1, side_a, side_b, side_c, side_a_label, side_b_label, side_c_label, angle_A, angle_B, angle_90, angle_90_dot, angle_A_label, angle_B_label)



        self.play(DrawBorderThenFill(triangle_1))
        self.wait(2)
        self.play(Create(side_c))       # Hipotenusa
        self.play(FadeIn(side_c_label)) 
        self.play(side_c.animate.set_color(COLOR_ANGLE_3),
                  side_c_label.animate.set_color(COLOR_ANGLE_3))
        self.wait(2)
        self.play(Create(side_a), Create(side_b))       # Catetos
        self.play(LaggedStart(FadeIn(side_a_label[0]),
                              FadeIn(side_b_label[0]),
                              lag_ratio=0.2))
        self.play(side_a.animate.set_color(COLOR_ANGLE_1),
                  side_a_label[0].animate.set_color(COLOR_ANGLE_2),
                  side_b.animate.set_color(COLOR_ANGLE_2),
                  side_b_label[0].animate.set_color(COLOR_ANGLE_1))
        self.wait(2)
        self.play(FadeIn(angle_B, angle_B_label))
        self.wait(2)

        side_a_label[1].set_color(COLOR_ANGLE_2)    # Catetos oposto e adjacente
        side_b_label[1].set_color(COLOR_ANGLE_1)
        self.play(FadeIn(side_a_label[1]))
        self.wait(2)
        self.play(FadeIn(side_b_label[1]))
        self.wait(2)

        self.play(FadeOut(angle_B, angle_B_label),  # Se escolher o outro ângulo como ref, os papéis de cat. oposto e adjacente são trocados
                  FadeIn(angle_A, angle_A_label))
        self.wait(2)
        
        side_a_label_aux = side_a_label.copy().set_color(COLOR_ANGLE_1).move_to(side_b_label).shift(LEFT*0.2)
        side_b_label_aux = side_b_label.copy().set_color(COLOR_ANGLE_2).move_to(side_a_label)
        side_b_label_aux[0].shift(RIGHT*0.2)
        self.play(CounterclockwiseTransform(side_a_label, side_a_label_aux),
                  ClockwiseTransform(side_b_label, side_b_label_aux))
        self.remove(side_a_label, side_b_label).add(side_a_label_aux, side_b_label_aux)
        self.wait(2)



        # Razões entre os lados
        SCALE_FACTOR = 0.6

        t1 = MathTex(r'{\text{Cat. oposto}',r'\over \text{Hipotenusa}}').scale(SCALE_FACTOR)
        t2 = MathTex(r'{\text{Cat. adjacente}',r'\over \text{Hipotenusa}}').scale(SCALE_FACTOR)
        t3 = MathTex(r'{\text{Cat. oposto}',r'\over \text{Cat. adjacente}}').scale(SCALE_FACTOR)
        t4 = MathTex(r'{\text{Hipotenusa}',r'\over \text{Cat. oposto}}').scale(SCALE_FACTOR)
        t5 = MathTex(r'{\text{Hipotenusa}',r'\over \text{Cat. adjacente}}').scale(SCALE_FACTOR)
        t6 = MathTex(r'{\text{Cat. adjacente}',r'\over \text{Cat. oposto}}').scale(SCALE_FACTOR)
        
        t1 = MathTex(r'{{a}',r'\over {c}}')#.scale(SCALE_FACTOR)
        t2 = MathTex(r'{{b}',r'\over {c}}')#.scale(SCALE_FACTOR)
        t3 = MathTex(r'{{a}',r'\over {b}}')#.scale(SCALE_FACTOR)
        t4 = MathTex(r'{{c}',r'\over {a}}')#.scale(SCALE_FACTOR)
        t5 = MathTex(r'{{c}',r'\over {b}}')#.scale(SCALE_FACTOR)
        t6 = MathTex(r'{{b}',r'\over {a}}')#.scale(SCALE_FACTOR)
        
        g_ratios_color_1 = VGroup(t1[0], t3[0], t4[1][1:], t6[1][1:]).set_color(COLOR_ANGLE_1)
        g_ratios_color_2 = VGroup(t2[0], t3[1][1:], t5[1][1:], t6[0]).set_color(COLOR_ANGLE_2)
        g_ratios_color_3 = VGroup(t1[1][1:], t2[1][1:], t4[0], t5[0]).set_color(COLOR_ANGLE_3)

        g_ratio_1 = VGroup(t1, t2, t3).arrange(DOWN, buff=0.7)
        g_ratio_2 = VGroup(t4, t5, t6).arrange(DOWN, buff=0.7)
        g_ratios = VGroup(g_ratio_1, g_ratio_2).arrange(RIGHT, buff=0.8).to_corner(UL, buff=1.5).shift(DOWN*0.5)

        side_a_label_2 = MathTex('a', color=COLOR_ANGLE_1).move_to(side_a_label_aux, aligned_edge=LEFT)
        side_b_label_2 = MathTex('b', color=COLOR_ANGLE_2).move_to(side_b_label_aux, aligned_edge=UP)
        side_c_label_2 = MathTex('c', color=COLOR_ANGLE_3).move_to(side_c_label)

        self.play(LaggedStart(ReplacementTransform(side_a_label_aux, side_a_label_2),
                              ReplacementTransform(side_b_label_aux, side_b_label_2),
                              ReplacementTransform(side_c_label, side_c_label_2),
                              lag_ratio=0.2))
        self.wait(2)







        side_a_label_2.save_state()
        side_a.save_state()
        side_b_label_2.save_state()
        side_b.save_state()
        side_c_label_2.save_state()
        side_c.save_state()

        self.play(side_a_label_2.animate.set_color(YELLOW),
                  side_c_label_2.animate.set_color(YELLOW),
                  side_a.animate.set_color(YELLOW),
                  side_c.animate.set_color(YELLOW))
        self.wait(2)

        self.play(LaggedStart(TransformFromCopy(side_a_label_2, t1[0]),     # 1a razão
                              TransformFromCopy(side_c_label_2, t1[1][1:]),
                              FadeIn(t1[1][0]),
                              lag_ratio=0.1))
        self.play(LaggedStart(TransformFromCopy(side_c_label_2, t4[0]),     # 4a razão
                              TransformFromCopy(side_a_label_2, t4[1][1:]),
                              FadeIn(t4[1][0]),
                              lag_ratio=0.1))
        self.wait(2)
        


        self.play(side_b_label_2.animate.set_color(YELLOW),
                  side_c_label_2.animate.set_color(YELLOW),
                  side_b.animate.set_color(YELLOW),
                  side_c.animate.set_color(YELLOW),
                  Restore(side_a_label_2),
                  Restore(side_a))
        self.wait(2)

        self.play(TransformFromCopy(side_b_label_2, t2[0]),     # 2a razão
                  FadeIn(t2[1][0]),
                  TransformFromCopy(side_c_label_2, t2[1][1:]))
        self.play(TransformFromCopy(side_c_label_2, t5[0]),     # 5a razão
                  FadeIn(t5[1][0]),
                  TransformFromCopy(side_b_label_2, t5[1][1:]))
        self.wait(2)
        


        self.play(side_a_label_2.animate.set_color(YELLOW),
                  side_b_label_2.animate.set_color(YELLOW),
                  side_a.animate.set_color(YELLOW),
                  side_b.animate.set_color(YELLOW),
                  Restore(side_c_label_2),
                  Restore(side_c))
        self.wait(2)

        self.play(TransformFromCopy(side_a_label_2, t3[0]),     # 3a razão
                  FadeIn(t3[1][0]),
                  TransformFromCopy(side_b_label_2, t3[1][1:]))
        self.play(TransformFromCopy(side_b_label_2, t6[0]),     # 6a razão
                  FadeIn(t6[1][0]),
                  TransformFromCopy(side_a_label_2, t6[1][1:]))
        self.wait(2)

        self.play(Restore(side_a_label_2), Restore(side_a),
                  Restore(side_b_label_2), Restore(side_b))
        self.wait(2)



        self.play(LaggedStart(
            TransformFromCopy(side_a_label_aux, t1[0]),     # 1a razão
            FadeIn(t1[1][0]),
            TransformFromCopy(side_c_label, t1[1][1:]),

            TransformFromCopy(side_b_label_aux, t2[0]),     # 2a razão
            FadeIn(t2[1][0]),
            TransformFromCopy(side_c_label, t2[1][1:]),

            TransformFromCopy(side_a_label_aux, t3[0]),     # 3a razão
            FadeIn(t3[1][0]),
            TransformFromCopy(side_b_label_aux, t3[1][1:]),

            TransformFromCopy(side_c_label, t4[0]),     # 4a razão
            FadeIn(t4[1][0]),
            TransformFromCopy(side_a_label_aux, t4[1][1:]),
            
            TransformFromCopy(side_c_label, t5[0]),     # 5a razão
            FadeIn(t5[1][0]),
            TransformFromCopy(side_b_label_aux, t5[1][1:]),

            TransformFromCopy(side_b_label_aux, t6[0]),     # 6a razão
            FadeIn(t6[1][0]),
            TransformFromCopy(side_a_label_aux, t6[1][1:]),
                              lag_ratio=0.1))
        
        self.wait(5)



        g_triangle = VGroup(triangle_1, angle_A, angle_A_label, 
                            side_a, side_b, side_c,
                            side_a_label_2, side_b_label_2, side_c_label_2)

        self.play(FadeOut(g_ratios), 
                  g_triangle.animate.shift(RIGHT*3))
        g_aux_0 = VGroup(angle_B, angle_B_label).shift(RIGHT*3)

        # Seno
        sine_1 = MathTex(r'\text{sen}(x) = ',r' {a \over c}').scale(0.9).to_edge(LEFT, buff=0.7).shift(UP*2)
        sine_1[1][0].set_color(COLOR_ANGLE_1)
        sine_1[1][2].set_color(COLOR_ANGLE_3)

        sine_text_1 = Tex('Seno', color=GRAY).scale(0.8).next_to(sine_1[0], DOWN, buff=1).shift(RIGHT*0.5)
        sine_arrow_1 = Arrow(sine_text_1, sine_1[0][1], color=GRAY)

        self.play(FadeIn(sine_1[0], sine_text_1, sine_arrow_1))
        self.wait(2)
        self.play(FadeIn(sine_1[1]))
        self.play(Indicate(sine_1[1][0]), Indicate(side_a_label_2))
        self.play(Indicate(sine_1[1][2]), Indicate(side_c_label_2))
        self.play(FadeOut(sine_text_1, sine_arrow_1))
        self.wait(2)



        # Cosseno
        cosine_1 = MathTex(r'\text{cos}(x) = ',r' \text{sen}(y) = ',r' {b \over c}').scale(0.9).next_to(sine_1, DOWN, buff=1, aligned_edge=LEFT)
        cosine_2 = MathTex(r'\text{cos}(x) = ',r' {b \over c}').scale(0.9).move_to(cosine_1, aligned_edge=LEFT)
        
        g_aux_1 = VGroup(cosine_1[2][0], cosine_2[1][0]).set_color(COLOR_ANGLE_2)
        g_aux_2 = VGroup(cosine_1[2][2], cosine_2[1][2]).set_color(COLOR_ANGLE_3)

        cosine_text_1 = Tex('Cosseno', color=GRAY).scale(0.8).next_to(cosine_1[0], DOWN, buff=1).shift(RIGHT*0.7)
        cosine_text_2 = Tex('Co-seno', color=GRAY).scale(0.8).move_to(cosine_text_1, aligned_edge=DL)
        cosine_text_3 = Tex('(seno do complementar)', color=GRAY).scale(0.8).next_to(cosine_text_2, DOWN).shift(RIGHT*0.5)
        cosine_arrow_1 = Arrow(cosine_text_1, cosine_1[0][1], color=GRAY)

        ref_1 = Dot(side_b_label_2.get_center()).shift(UP*0.5)
        ref_2 = Dot(side_b_label_2.get_center()).shift(LEFT*0.2)
        ref_3 = Dot(angle_B_label.get_center()).shift(DOWN*0.2+LEFT*0.1)
        ref_4 = Dot(angle_A.get_center()).shift(DOWN*0.2)

        arrow_aux_1 = Arrow(ref_1.get_center(), ref_3.get_center(), color=GRAY, max_tip_length_to_length_ratio=0.5)
        arrow_aux_2 = CurvedArrow(ref_2.get_center(), ref_4.get_center(), color=GRAY, stroke_width=6, radius=-2).scale(0.9)

        self.play(FadeIn(cosine_1[0], cosine_text_1, cosine_arrow_1))
        self.wait(2)
        self.play(FadeTransform(cosine_text_1, cosine_text_2, stretch=False))
        self.wait(2)
        self.play(FadeIn(cosine_text_3))
        self.wait(2)
        self.play(FadeIn(angle_B, angle_B_label))
        self.wait(2)
        self.play(FadeIn(cosine_1[1]))
        self.wait(2)
        self.play(FadeIn(cosine_1[2]))
        self.play(Indicate(cosine_1[2][0]), Indicate(side_b_label_2))
        self.play(Indicate(cosine_1[2][2]), Indicate(side_c_label_2))
        self.wait(2)
        self.play(FadeIn(arrow_aux_1))
        self.wait(2)
        self.play(FadeIn(arrow_aux_2))
        self.wait(2)
        self.play(LaggedStart(FadeOut(cosine_1[1], arrow_aux_1, arrow_aux_2, angle_B, angle_B_label),
                              cosine_1[2].animate.move_to(cosine_2[1]),
                              lag_ratio=0.2))
        self.remove(cosine_1[0], cosine_1[2]).add(cosine_2)
        self.play(Indicate(cosine_2[1][0]), Indicate(side_b_label_2))
        self.play(Indicate(cosine_2[1][2]), Indicate(side_c_label_2))
        self.play(FadeOut(cosine_text_2, cosine_arrow_1, cosine_text_3))
        self.wait(2)



        # Tangente
        tg_1 = MathTex(r'\text{tg}(x) = ',r' {\text{sen}(x) \over \text{cos}(x)} = ',r' {a/c \over b/c} = ',r' {a \over b}').scale(0.9).next_to(cosine_2, DOWN, buff=1, aligned_edge=LEFT)
        tg_2 = MathTex(r'\text{tg}(x) = ',r' {a \over b}').scale(0.9).move_to(tg_1, aligned_edge=LEFT)
        tg_2[0].shift(DOWN*0.01)

        g_aux_3 = VGroup(tg_1[2][0], tg_1[3][0], tg_2[1][0]).set_color(COLOR_ANGLE_1)
        g_aux_3 = VGroup(tg_1[2][4], tg_1[3][2], tg_2[1][2]).set_color(COLOR_ANGLE_2)
        g_aux_4 = VGroup(tg_1[2][2], tg_1[2][6]).set_color(COLOR_ANGLE_3)

        tg_text_1 = Tex('Tangente', color=GRAY).scale(0.8).next_to(tg_1[0], DOWN, buff=1.1).shift(RIGHT*1)
        tg_arrow_1 = Arrow(tg_text_1, tg_1[0][1], color=GRAY)

        self.play(FadeIn(tg_1[0], tg_text_1, tg_arrow_1))
        self.wait(2)
        self.play(FadeIn(tg_1[1]))
        self.wait(2)
        self.play(FadeIn(tg_1[2]))
        self.wait(2)
        self.play(FadeIn(tg_1[3]))
        self.play(Indicate(tg_1[3][0]), Indicate(side_a_label_2))
        self.play(Indicate(tg_1[3][2]), Indicate(side_b_label_2))
        self.wait(2)
        self.play(LaggedStart(FadeOut(tg_1[1:3]),
                              tg_1[3].animate.move_to(tg_2[1]),
                              lag_ratio=0.2))
        self.remove(tg_1[0], tg_1[3]).add(tg_2)
        self.play(FadeOut(tg_text_1, tg_arrow_1))
        self.wait(2)



        # Cossecante
        cosecant_1 = MathTex(r'\text{cossec}(x) = ',r' {c \over a}').scale(0.9).next_to(sine_1, RIGHT, buff=1)
        cosecant_1[1][0].set_color(COLOR_ANGLE_3)
        cosecant_1[1][2].set_color(COLOR_ANGLE_1)

        cosecant_text_1 = Tex('Cossecante', color=GRAY).scale(0.8).next_to(cosecant_1[0], DOWN, buff=1).shift(RIGHT*1)
        cosecant_arrow_1 = Arrow(cosecant_text_1, cosecant_1[0][1], color=GRAY)

        self.play(FadeIn(cosecant_1[0], cosecant_text_1, cosecant_arrow_1))
        self.wait(2)
        self.play(ClockwiseTransform(sine_1[1].copy(), cosecant_1[1], path_arc=-np.pi/2))
        self.play(FadeOut(cosecant_text_1, cosecant_arrow_1))
        self.wait(2)



        # Secante
        secant_1 = MathTex(r'\text{sec}(x) = ',r' {c \over b}').scale(0.9).next_to(cosecant_1, DOWN, buff=1.1)
        secant_1[1][0].set_color(COLOR_ANGLE_3)
        secant_1[1][2].set_color(COLOR_ANGLE_2)

        secant_text_1 = Tex('Secante', color=GRAY).scale(0.8).next_to(secant_1[0], DOWN, buff=1).shift(RIGHT*0.8)
        secant_arrow_1 = Arrow(secant_text_1, secant_1[0][0], color=GRAY)

        self.play(FadeIn(secant_1[0], secant_text_1, secant_arrow_1))
        self.wait(2)
        self.play(ClockwiseTransform(cosine_2[1].copy(), secant_1[1], path_arc=-np.pi/2))
        self.play(FadeOut(secant_text_1, secant_arrow_1))
        self.wait(2)



        # Cotangente
        cotg_1 = MathTex(r'\text{cotg}(x) = ',r' {b \over a}').scale(0.9).next_to(secant_1, DOWN, buff=1)
        cotg_1[1][0].set_color(COLOR_ANGLE_2)
        cotg_1[1][2].set_color(COLOR_ANGLE_1)

        cotg_text_1 = Tex('Cotangente', color=GRAY).scale(0.8).next_to(cotg_1[0], DOWN, buff=1).shift(RIGHT*1)
        cotg_arrow_1 = Arrow(cotg_text_1, cotg_1[0][1], color=GRAY)

        self.play(FadeIn(cotg_1[0], cotg_text_1, cotg_arrow_1))
        self.wait(2)
        self.play(ClockwiseTransform(tg_2[1].copy(), cotg_1[1], path_arc=-np.pi/2))
        self.play(FadeOut(cotg_text_1, cotg_arrow_1))
        self.wait(2)



        # Comentário sobre as 3 últimas
        black_sq_1 = Square(color=BLACK).set_opacity(0.7).scale(5).move_to(sine_1, aligned_edge=UR).shift(UP*0.1+RIGHT*0.1).set_z_index(5)
        black_sq_2 = black_sq_1.copy().move_to(triangle_1, aligned_edge=LEFT).shift(LEFT*0.1).set_z_index(5)

        self.play(FadeIn(black_sq_1, black_sq_2))
        self.wait(2)
        self.play(FadeOut(black_sq_1))
        self.wait(2)



        # Sobre a palavra "Trigonometria"
        t7 = Tex('Tri','gono','metria').next_to(triangle_1, UP, buff=1).shift(RIGHT*6)
        t8 = Tex('(medidas no triângulo)', color=GRAY).scale(0.8).next_to(t7, DOWN, buff=0.2).shift(LEFT*6)
        self.play(FadeOut(black_sq_2))
        self.play(t7.animate.shift(LEFT*6), run_time=2)
        self.wait(2)
        self.play(t7[0].animate.shift(LEFT*0.3),
                  t7[2].animate.shift(RIGHT*0.3))
        self.play(LaggedStart(Indicate(t7[2], scale_factor=1.1),
                              Indicate(t7[0], scale_factor=1.1),
                              Indicate(t7[1], scale_factor=1.1),
                              lag_ratio=0.5))
        self.play(t7[0].animate.shift(RIGHT*0.3),
                  t7[2].animate.shift(LEFT*0.3))
        self.wait(2)
        self.play(FadeIn(t8))
        self.wait(2)
        


# Calculando as razões de 60° e 30°
class vid4(MovingCameraScene):
    def construct(self):
        
        # Criando o triângulo equilátero
        dot_A = Dot([-3/2, -13/15, 0]).scale(0)
        dot_B = Dot([0, 26/15, 0]).scale(0)
        dot_C = Dot([3/2, -13/15, 0]).scale(0)

        COLOR_ANGLE_1 = PURPLE
        COLOR_ANGLE_2 = GREEN
        COLOR_ANGLE_3 = RED

        angle_A = Angle.from_three_points(dot_B.get_center(), dot_A.get_center(), dot_C.get_center(), radius=0.15, stroke_width=30, color=COLOR_ANGLE_1, other_angle=True).set_z_index(-1)
        angle_B = Angle.from_three_points(dot_A.get_center(), dot_B.get_center(), dot_C.get_center(), radius=0.15, stroke_width=30, color=COLOR_ANGLE_2).set_z_index(-1)     
        angle_C = Angle.from_three_points(dot_A.get_center(), dot_C.get_center(), dot_B.get_center(), radius=0.15, stroke_width=30, color=COLOR_ANGLE_3, other_angle=True).set_z_index(-1)     

        angle_A_label = MathTex(r'60^{\circ}').scale(0.7).move_to(Angle.from_three_points(dot_B, dot_A, dot_C, radius=0.9, other_angle=True)).set_z_index(5)
        angle_B_label = angle_A_label.copy().move_to(Angle.from_three_points(dot_A, dot_B, dot_C, radius=0.8)).set_z_index(6)
        angle_C_label = angle_A_label.copy().move_to(Angle.from_three_points(dot_A, dot_C, dot_B, radius=0.8, other_angle=True)).set_z_index(5)

        triangle_1 =  Polygon(dot_A.get_center(), dot_B.get_center(), dot_C.get_center(), color=WHITE, fill_opacity=0).set_z_index(2)
        
        side_a = Line(dot_B, dot_C, color=WHITE).scale(1.01).set_z_index(3)
        side_b = Line(dot_A, dot_C, color=WHITE).scale(1.01).set_z_index(3)
        side_c = Line(dot_A, dot_B, color=WHITE).scale(1.01).set_z_index(3)

        side_a_label = MathTex(r'a', color=BLUE).next_to(side_a, RIGHT, buff=-0.5)
        side_b_label = side_a_label.copy().next_to(side_b, DOWN, buff=0.25)
        side_c_label = side_a_label.copy().next_to(side_c, LEFT, buff=-0.5)



        # Animação
        t1 = MathTex(r'60^{\circ}')
        self.play(FadeIn(t1))
        self.wait(2)

        self.play(LaggedStart(DrawBorderThenFill(triangle_1),
                              FadeIn(angle_A, angle_B, angle_C),
                              TransformFromCopy(t1, angle_A_label),
                              TransformFromCopy(t1, angle_B_label),
                              ReplacementTransform(t1, angle_C_label),
                              FadeIn(side_c_label), 
                              FadeIn(side_a_label),
                              FadeIn(side_b_label),
                              lag_ratio=0.3))
        self.wait(2)

        g_sides = VGroup(side_c_label, side_a_label, side_b_label)
        self.play(ApplyWave(g_sides, amplitude=0.1))
        self.wait(2)

        g_angles = VGroup(angle_A, angle_A_label, angle_B, angle_B_label, angle_C, angle_C_label)
        self.play(ApplyWave(g_angles, amplitude=0.1))
        self.wait(2)



        # Divide o triângulo ao meio
        line_1 = Line(dot_B, Dot((0,-13/15,0)).get_center())


        angle_30 = MathTex(r'30^{\circ}').scale(0.7).move_to(Angle.from_three_points(dot_A, dot_B, Dot((0,-13/15,0)), radius=0.8)).set_z_index(6).shift(LEFT*0.2+UP*0.1)
        angle_30_bg = SurroundingRectangle(angle_30, color=BLACK, stroke_width=0).set_opacity(0.8).set_z_index(5)
        
        angle_30_2 = MathTex(r'30^{\circ}').scale(0.7).move_to(Angle.from_three_points(dot_C, dot_B, Dot((0,-13/15,0)), radius=0.8, other_angle=True)).set_z_index(6).shift(RIGHT*0.2+UP*0.1)
        angle_30_2_bg = SurroundingRectangle(angle_30_2, color=BLACK, stroke_width=0).set_opacity(0.8).set_z_index(5)

        g_aux1 = VGroup(angle_30, angle_30_2)

        
        triangle_2 = Polygon(dot_A.get_center(), dot_B.get_center(), Dot((0,-13/15,0)).get_center(), color=WHITE, fill_opacity=0).set_z_index(2)
        

        side_a2_1 = MathTex(r'a/2', color=BLUE).next_to(triangle_2, DOWN, buff=0.25).shift(LEFT*0.1)
        side_a2_2 = side_a2_1.copy().shift(RIGHT*1.6)

        g_aux2 = VGroup(side_a2_1, side_a2_2)

        angle_B_2 = Angle.from_three_points(dot_A.get_center(), dot_B.get_center(), Dot((0,-13/15,0)).get_center(), radius=0.15, stroke_width=30, color=COLOR_ANGLE_2).set_z_index(-1)
        

        self.play(Create(line_1),
                  ReplacementTransform(angle_B_label, g_aux1),
                  FadeIn(angle_30_bg, angle_30_2_bg))
        self.play(ReplacementTransform(side_b_label, g_aux2))
        self.wait(2)
        self.add(triangle_2).remove(line_1)
        self.play(FadeOut(triangle_1, angle_30_2, angle_C, angle_C_label, side_a_label, side_a2_2),
                  ReplacementTransform(angle_B, angle_B_2))
        self.wait(2)
        self.play(Indicate(side_c_label))
        self.wait(2)
        self.play(Indicate(side_a2_1))
        self.wait(2)

        g_triangle = VGroup(triangle_2, side_c_label, side_a2_1, angle_A, angle_A_label, angle_B_2, angle_30, angle_30_bg)
        self.play(g_triangle.animate.shift(LEFT*2))
        self.wait(2)



        # Pitágoras para descobrir o outro cateto
        side_x_label = MathTex(r'x', color=GREEN).next_to(triangle_2, RIGHT, buff=0.2)
        
        t2 = MathTex(r'x^2 + \left({a \over 2}\right)^2 = a^2').scale(0.9).shift(UP*1.5+RIGHT*3.25)
        t3 = MathTex(r'\Rightarrow').scale(0.9).rotate(-90*DEGREES).next_to(t2, DOWN, buff=0.7)
        t4 = MathTex(r'x = {a\sqrt{3} \over 2}').scale(0.9).next_to(t3, DOWN, buff=0.5)
        
        g1 = VGroup(t2[0][10], t2[0][4], t4[0][2]).set_color(BLUE)
        g2 = VGroup(t2[0][0], t4[0][0]).set_color(GREEN)

        self.play(FadeIn(side_x_label, t2[0][0:10]))
        self.play(Indicate(t2[0][0:2]), Indicate(side_x_label))
        self.play(Indicate(t2[0][3:9]), Indicate(side_a2_1))
        self.wait(2)
        self.play(FadeIn(t2[0][10:]))
        self.wait(2)
        self.play(FadeIn(t3))
        self.play(FadeIn(t4))
        self.wait(2)

        side_x_label_2 = MathTex(r'{a\sqrt{3} \over 2}', color=BLUE).next_to(triangle_2, RIGHT, buff=0.2)
        self.play(LaggedStart(FadeOut(side_x_label),
                              TransformMatchingShapes(t4[0][2:], side_x_label_2),
                              FadeOut(t2, t3, t4[0][0:2]),
                              lag_ratio=0.2))
        self.wait(2)



        # Seno de 60°
        sine_1 = MathTex(r'\text{sen}(60^{\circ}) = ',r'\frac{\frac{a\sqrt{3}}{2}}{a}').scale(0.9).shift(RIGHT*2.5)
        sine_1[1][0:7].scale(1.3).set_stroke(width=0).shift(RIGHT*0.1)
        sine_1[1][7].shift(RIGHT*0.1)

        red_line1 = Line(UP*0.2, DOWN*0.2, color=RED, stroke_width=4).scale(1).rotate(50*DEGREES).move_to(sine_1[1][0])
        red_line2 = red_line1.copy().move_to(sine_1[1][7])
        
        sine_2 = MathTex(r'\text{sen}(60^{\circ}) = ',r'\frac{\sqrt{3}}{2}').scale(0.9).move_to(sine_1, aligned_edge=DL)

        self.play(FadeIn(sine_1[0], sine_1[1][6]))
        self.wait(2)
        self.play(FadeIn(sine_1[1][0:6]), Indicate(side_x_label_2))
        self.wait(2)
        self.play(FadeIn(sine_1[1][7:10]), Indicate(side_c_label))
        self.wait(2)
        self.play(Create(red_line1), Create(red_line2))
        self.wait(2)
        self.play(LaggedStart(FadeOut(red_line1, red_line2, sine_1[1][0:10]),
                              FadeIn(sine_2[1]),
                              lag_ratio=0.1))
        self.wait(2)
        self.remove(sine_1[0]).add(sine_2[0])
        self.play(sine_2.animate.shift(UP*2))
        self.wait(2)



        # Cosseno de 60°
        cosine_1 = MathTex(r'\text{cos}(60^{\circ}) = ',r'\frac{a/2}{a}').scale(0.9).shift(RIGHT*2.5)

        red_line3 = red_line1.copy().move_to(cosine_1[1][0])
        red_line4 = red_line1.copy().move_to(cosine_1[1][4])

        cosine_2 = MathTex(r'\text{cos}(60^{\circ}) = ',r'\frac{1}{2}').scale(0.9).move_to(cosine_1, aligned_edge=DL)
       
        self.play(FadeIn(cosine_1[0], cosine_1[1][3]))
        self.wait(2)
        self.play(FadeIn(cosine_1[1][0:3]), Indicate(side_a2_1))
        self.wait(2)
        self.play(FadeIn(cosine_1[1][4]), Indicate(side_c_label))
        self.wait(2)
        self.play(Create(red_line3), Create(red_line4))
        self.wait(2)
        self.play(LaggedStart(FadeOut(red_line3, red_line4, cosine_1[1]),
                              FadeIn(cosine_2[1]),
                              lag_ratio=0.1))
        self.wait(2)
        self.remove(cosine_1[0]).add(cosine_2[0])
        self.wait(2)



        # Tangente de 60°
        tg_1 = MathTex(r'\text{tg}(60^{\circ}) = ',r'\frac{\frac{a\sqrt{3}}{2}}{\frac{a}{2}}').scale(0.9).shift(RIGHT*2.5+DOWN*2)
        tg_1[1].scale(1.3).shift(RIGHT*0.1)

        red_line5 = red_line1.copy().move_to(tg_1[1][0])
        red_line6 = red_line1.copy().move_to(tg_1[1][7])

        red_line7 = red_line1.copy().move_to(tg_1[1][5])
        red_line8 = red_line1.copy().move_to(tg_1[1][9])

        tg_2 = MathTex(r'\text{tg}(60^{\circ}) = ',r'\sqrt{3}').scale(0.9).move_to(tg_1, aligned_edge=LEFT).shift(DOWN*0.01)

        self.play(FadeIn(tg_1[0], tg_1[1][6]))
        self.wait(2)
        self.play(FadeIn(tg_1[1][0:6]), Indicate(side_x_label_2))
        self.wait(2)
        self.play(FadeIn(tg_1[1][7:]), Indicate(side_a2_1))
        self.wait(2)
        self.play(Create(red_line5), Create(red_line6))
        self.play(Create(red_line7), Create(red_line8))
        self.wait(2)
        self.play(LaggedStart(FadeOut(red_line5, red_line6, red_line7, red_line8, tg_1[1]),
                              FadeIn(tg_2[1]),
                              lag_ratio=0.1))
        self.wait(2)
        self.remove(tg_1[0]).add(tg_2[0])
        self.wait(2)



        # Lembrando que cos(x) = sen(complementar de x)
        black_sq1 = Square(color=BLACK).set_opacity(0.9).scale(10).set_z_index(7)
        
        t5 = MathTex(r'\text{cos}(x) = \text{sen}(90^{\circ} - x)', color=WHITE).scale(0.9).to_edge(UP).set_z_index(8)
        
        brace_1 = Brace(t5[0][11:16], DOWN, color=GRAY).set_z_index(8)
        brace_1_text = Tex(r'Complementar de $x$', color=GRAY).scale(0.9).next_to(brace_1, DOWN).set_z_index(8)
        
        self.play(FadeIn(black_sq1),
                  FadeOut(side_a2_1, side_x_label_2, side_c_label))
        self.play(FadeIn(t5))
        self.play(FadeIn(brace_1, brace_1_text))
        self.wait(2)
        self.play(LaggedStart(FadeOut(t5, brace_1, brace_1_text),
                              FadeOut(black_sq1),
                              lag_ratio=0.2))
        self.wait(2)



        # O complementar de 60° é 30°
        arrow_1 = CurvedArrow(angle_A.get_edge_center(UP), angle_30.get_corner(DL), stroke_width=6, radius=-1.5, color=GRAY).scale(0.9).set_z_index(8).shift(LEFT*0.1+UP*0.1)
        self.play(FadeIn(arrow_1))
        self.wait(2)

        cos_30 = MathTex(r'= \text{cos}(30^{\circ}) ',r'= \frac{\sqrt{3}}{2}').scale(0.9).next_to(sine_2, RIGHT, buff=0.2)
        sen_30 = MathTex(r'= \text{sen}(30^{\circ}) ',r'= \frac{1}{2}').scale(0.9).next_to(cosine_2, RIGHT, buff=0.2)
        tg_30 = MathTex(r'= \frac{1}{\text{tg}(30^{\circ})}').scale(0.9).next_to(tg_2, RIGHT, buff=0.2).shift(DOWN*0.05)

        self.play(Indicate(sine_2))
        self.wait(2)
        self.play(FadeIn(cos_30[0]))
        self.wait(2)
        self.play(Indicate(cosine_2))
        self.wait(2)
        self.play(FadeIn(sen_30[0]))
        self.wait(2)

        g_aux3 = VGroup(triangle_2, arrow_1, angle_A, angle_A_label, angle_B_2, angle_30, angle_30_bg, angle_30_2_bg)
        self.play(FadeOut(g_aux3))
        self.wait(2)



        # Tangente de 30°
        tg_30_1 = MathTex(r'\text{tg}(30^{\circ}) =',r'\frac{\text{sen}(30^{\circ})}{\text{cos}(30^{\circ})}').scale(0.9).move_to(g_triangle).shift(LEFT*0.5)
        tg_30_2 = MathTex(r'\text{tg}(30^{\circ}) =',r'\frac{\frac{1}{2}}{\frac{\sqrt{3}}{2}}').scale(0.9).move_to(tg_30_1, aligned_edge=LEFT).shift(DOWN*0.04)
        tg_30_2[1].scale(1.25).shift(RIGHT*0.1)

        tg_30_3 = MathTex(r'\text{tg}(30^{\circ}) =',r'\frac{1}{\sqrt{3}}').scale(0.9).move_to(tg_30_1, aligned_edge=LEFT).shift(DOWN*0.02)
        tg_30_4 = MathTex(r'\frac{1}{\text{tg}(30^{\circ})} ',r'= \sqrt{3}').scale(0.9).move_to(tg_30_3, aligned_edge=LEFT).shift(DOWN*0.02)

        red_line9 = red_line1.copy().move_to(tg_30_2[1][2])
        red_line10 = red_line1.copy().move_to(tg_30_2[1][8])

        sr_1_ref = VGroup(cosine_2[1], sen_30[0])
        sr_2_ref = VGroup(sine_2[1], cos_30[0])
        sr_1 = SurroundingRectangle(sr_1_ref)
        sr_2 = SurroundingRectangle(sr_2_ref)

        self.play(FadeIn(tg_30_1[0]))
        self.wait(2)
        self.play(LaggedStart(FadeIn(tg_30_1[1]),
                              Create(sr_1),
                              Create(sr_2),
                              lag_ratio=0.3))
        self.play(FadeOut(sr_1, sr_2))
        self.wait(2)
        self.play(TransformMatchingShapes(tg_30_1[1][0:8], tg_30_2[1][0:3]),
                  TransformMatchingShapes(tg_30_1[1][8], tg_30_2[1][3]),
                  Indicate(cosine_2[1]))
        self.wait(2)
        self.play(TransformMatchingShapes(tg_30_1[1][9:], tg_30_2[1][4:]),
                  Indicate(sine_2[1]))
        self.wait(2)
        self.play(Create(red_line9), Create(red_line10))
        self.play(LaggedStart(FadeOut(red_line9, red_line10, tg_30_2[1]),
                              FadeIn(tg_30_3[1]),
                              lag_ratio=0.1))
        self.remove(tg_30_1[0]).add(tg_30_3[0])
        self.wait(2)
        self.play(TransformMatchingTex(tg_30_3, tg_30_4))
        self.wait(2)

        sr_3 = SurroundingRectangle(tg_30_4)
        sr_4 = SurroundingRectangle(tg_2)
        self.play(LaggedStart(Create(sr_3),
                              Create(sr_4),
                              lag_ratio=0.2))
        self.wait(2)
        self.play(LaggedStart(FadeOut(sr_3, sr_4, tg_30_4[1]),
                              FadeIn(tg_30[0][0]),
                              TransformMatchingShapes(tg_30_4[0], tg_30[0][1:])))
        self.wait(2)



        # Sabendo apenas seno e cosseno conseguimos encontrar várias razões
        self.play(self.camera.frame.animate.move_to((cosine_2[1].get_x(), 0, 0)))
        self.wait(2)

        sr_sen_60 = SurroundingRectangle(sine_2[0][0:8], color=YELLOW, stroke_width=0).set_opacity(0.2).set_z_index(-1)
        sr_cos_60 = SurroundingRectangle(cosine_2[0][0:8], color=YELLOW, stroke_width=0).set_opacity(0.2).set_z_index(-1)
        sr_tg_60 = SurroundingRectangle(tg_2[0][0:7], color=YELLOW, stroke_width=0).set_opacity(0.2).set_z_index(-1)
        
        self.play(FadeIn(sr_sen_60))
        self.play(FadeIn(sr_cos_60))
        self.play(FadeIn(sr_tg_60))
        self.wait(2)
        self.play(LaggedStart(Indicate(cos_30[0][1:]),
                              Indicate(sen_30[0][1:]),
                              Indicate(tg_30[0][3:]),
                              lag_ratio=0.3))
        self.wait(2)

        t6 = MathTex(r'\frac{\text{sen}(60^{\circ})}{\text{cos}(60^{\circ})} =', color=GRAY).scale(0.9).next_to(tg_2, LEFT, buff=0.2)
        self.play(FadeIn(t6))
        self.wait(2)
        self.play(LaggedStart(FadeOut(sr_tg_60),
                              FadeOut(t6),
                              lag_ratio=0.2))
        self.play(LaggedStart(Indicate(tg_2[0][0:7]),
                              Indicate(cos_30[0][1:]),
                              Indicate(sen_30[0][1:]),
                              Indicate(tg_30[0][3:]),
                              lag_ratio=0.3))
        self.wait(2)
        self.play(LaggedStart(Indicate(tg_2[0][0:7]),
                              Indicate(cos_30[0][1:]),
                              Indicate(sen_30[0][1:]),
                              Indicate(tg_30[0][3:]),
                              lag_ratio=0.3))
        self.wait(2)

        t7 = MathTex(r'\text{sen}^2(x) + \text{cos}^2(x) = 1', color=YELLOW).scale(0.9).next_to(sine_2[1], UP, buff=0.6).set_z_index(8)
        black_sq2 = black_sq1.copy()
        self.play(LaggedStart(FadeIn(black_sq2),
                              FadeIn(t7),
                              lag_ratio=0.1))
        self.wait(2)
        self.play(LaggedStart(FadeOut(t7),
                              FadeOut(black_sq2),
                              lag_ratio=0.1))
        self.wait(2)
        self.play(FadeOut(sr_cos_60))
        self.wait(2)
        self.play(LaggedStart(Indicate(cosine_2[0][0:8]),
                              Indicate(tg_2[0][0:7]),
                              Indicate(cos_30[0][1:]),
                              Indicate(sen_30[0][1:]),
                              Indicate(tg_30[0][3:]),
                              lag_ratio=0.3))
        self.wait(2)

        arrow_2 = Arrow(UP, DOWN, stroke_width=7, max_tip_length_to_length_ratio=0.2, color=GRAY).scale(0.7).next_to(sine_2[0], DOWN, buff=0.2).shift(LEFT*0.2)
        
        arrow_3a = arrow_2.copy().next_to(cosine_2[0], DOWN, buff=0.2).shift(LEFT*0.2)
        arrow_3b = CurvedArrow(sine_2.get_edge_center(LEFT), tg_2.get_edge_center(LEFT), stroke_width=5, color=GRAY).scale(0.9).shift(LEFT*0.1)

        arrow_4a = CurvedArrow(sine_2[0].get_edge_center(UP), cos_30[0].get_edge_center(UP), stroke_width=5, radius=-4, color=GRAY).scale(0.9).shift(UP*0.1)
        arrow_4b = CurvedArrow(cosine_2[0].get_edge_center(UP), sen_30[0].get_edge_center(UP), stroke_width=5, radius=-4, color=GRAY).scale(0.9).shift(UP*0.1)
        arrow_4c = CurvedArrow(tg_2[0].get_edge_center(DOWN), tg_30[0].get_edge_center(DOWN), stroke_width=5, radius=4, color=GRAY).scale(0.9).shift(DOWN*0.1)

        self.play(FadeIn(arrow_2))
        self.wait(2)
        self.play(FadeIn(arrow_3a, arrow_3b))
        self.wait(2)
        self.play(FadeIn(arrow_4a, arrow_4b, arrow_4c))
        self.wait(2)


        


# Mostrando a identidade sen^2(x) + cos^2(x) = 1
class vid5(MovingCameraScene):
    def construct(self):

        dot_1 = Dot((0,0,0))
        dot_2 = Dot((4*0.866,0,0))
        dot_3 = Dot((4*0.866,4*1/2,0))

        triangle_1 = Polygon(dot_1.get_center(), dot_2.get_center(), dot_3.get_center() , color=WHITE).move_to(ORIGIN)
        
        angle_1a = Angle.from_three_points(dot_2.get_center(), dot_1.get_center(), dot_3.get_center(), radius=0.07, stroke_width=140, color=PURPLE).set_z_index(-2).move_to(triangle_1, aligned_edge=DL)
        angle_1b = Square(color=BLACK).set_opacity(1).next_to(angle_1a, LEFT, buff=0).set_z_index(-1)
        angle_1 = VGroup(angle_1a, angle_1b)
        
        angle_1_label = MathTex('x').scale(0.9).next_to(angle_1, RIGHT, buff=0).shift(RIGHT*0.8+UP*0.2)
        
        side_r_label = MathTex('a', color=BLUE).scale(0.9).next_to(triangle_1, RIGHT, buff=0.2)
        side_d_label = MathTex('b', color=GREEN).scale(0.9).next_to(triangle_1, DOWN, buff=0.2)
        side_l_label = MathTex('c', color=RED).scale(0.9).next_to(triangle_1, LEFT, buff=-1.7).shift(UP*0.3)

        sin_1 = MathTex(r'\text{sen}(x) =',r' \frac{a}{c}').scale(0.9).shift(RIGHT*5.7+UP)     
        cos_1 = MathTex(r'\text{cos}(x) =',r' \frac{b}{c}').scale(0.9).shift(RIGHT*5.7+DOWN)

        sin_1[1][0].set_color(BLUE)
        sin_1[1][2].set_color(RED)
        cos_1[1][0].set_color(GREEN)
        cos_1[1][2].set_color(RED)

        self.camera.frame.shift(RIGHT*3)
        
        self.add(angle_1b)
        self.play(FadeIn(triangle_1, angle_1a, angle_1_label, 
                         side_r_label, side_d_label, side_l_label))
        self.play(FadeIn(sin_1))
        self.wait(2)
        self.play(Indicate(sin_1[1][0]), Indicate(side_r_label))
        self.wait(2)
        self.play(Indicate(sin_1[1][2]), Indicate(side_l_label))
        self.wait(2)
        self.play(FadeIn(cos_1))
        self.wait(2)
        self.play(Indicate(cos_1[1][0]), Indicate(side_d_label))
        self.wait(2)
        self.play(Indicate(cos_1[1][2]), Indicate(side_l_label))
        self.wait(2)



        # Escolhendo hipotenusa igual a 1
        side_1_label = MathTex('1', color=YELLOW).scale(0.9).move_to(side_l_label)
        
        sin_2 = MathTex(r'\text{sen}(x) =',r' \frac{a}{1}').scale(0.9).move_to(sin_1, aligned_edge=LEFT)
        cos_2 = MathTex(r'\text{cos}(x) =',r' \frac{b}{1}').scale(0.9).move_to(cos_1, aligned_edge=LEFT)

        sin_2[1][0].set_color(BLUE)
        sin_2[1][2].set_color(YELLOW)
        cos_2[1][0].set_color(GREEN)
        cos_2[1][2].set_color(YELLOW)

        self.play(side_l_label.animate.set_color(YELLOW))
        self.wait(2)
        self.play(TransformMatchingTex(side_l_label, side_1_label))
        self.wait(2)
        self.play(LaggedStart(TransformMatchingShapes(sin_1[1], sin_2[1]),
                              TransformMatchingShapes(cos_1[1], cos_2[1]),
                              lag_ratio=0.3))
        self.wait(2)

        sin_3 = MathTex(r'\text{sen}(x) =',r'a').scale(0.9).move_to(sin_1, aligned_edge=LEFT).shift(UP*0.02)
        cos_3 = MathTex(r'\text{cos}(x) =',r'b').scale(0.9).move_to(cos_1, aligned_edge=LEFT).shift(DOWN*0.04)

        sin_3[1][0].set_color(BLUE)
        cos_3[1][0].set_color(GREEN)
        
        self.play(ReplacementTransform(sin_2[1], sin_3[1]),
                  ReplacementTransform(cos_2[1], cos_3[1]),
                  side_1_label.animate.set_color(WHITE))
        self.wait(2)

        sr_1 = SurroundingRectangle(sin_3)
        sr_2 = SurroundingRectangle(cos_3)
        self.play(Create(sr_1))
        self.play(FadeOut(sr_1))
        self.wait(2)
        self.play(Create(sr_2))
        self.play(FadeOut(sr_2))
        self.wait(2)
        self.play(FadeOut(sin_1[0][6], cos_1[0][6], sin_3[1], cos_3[1], side_r_label, side_d_label),
                  self.camera.frame.animate.shift(LEFT*3),
                  sin_1[0][0:6].animate.next_to(triangle_1, RIGHT, buff=0.2).set_color(BLUE),
                  cos_1[0][0:6].animate.next_to(triangle_1, DOWN, buff=0.2).set_color(GREEN))
        self.wait(2)



        # Aplicando o Teorema de Pitágoras
        t1 = MathTex(r'(\text{sen}(x))^2 ',r' + ',r' (\text{cos}(x))^2 ',r' = 1^2', color=YELLOW).scale(0.9).shift(UP*3)
        t1_aux1 = MathTex(r'\text{sen}^2(x)', color=YELLOW).move_to(t1[0]).scale(0.9)
        t1_aux2 = MathTex(r'\text{cos}^2(x)', color=YELLOW).move_to(t1[2]).scale(0.9)

        self.play(FadeIn(t1[1]))
        self.play(FadeIn(t1[0]))
        self.play(FadeIn(t1[2]))
        self.wait(2)
        self.play(FadeIn(t1[3]))
        self.wait(2)
        self.play(FadeOut(t1[3][2]))
        self.wait(2)
        self.play(FadeOut(t1[0][0], t1[0][7]),                          # Transformando em sen^2(x)
                  CounterclockwiseTransform(t1[0][8], t1_aux1[0][3]),
                  TransformMatchingShapes(t1[0][1:4], t1_aux1[0][0:3]),
                  TransformMatchingShapes(t1[0][4:7], t1_aux1[0][4:7]),
                  
                  FadeOut(t1[2][0], t1[2][7]),                          # Transformando em cos^2(x)
                  CounterclockwiseTransform(t1[2][8], t1_aux2[0][3]),
                  TransformMatchingShapes(t1[2][1:4], t1_aux2[0][0:3]),
                  TransformMatchingShapes(t1[2][4:7], t1_aux2[0][4:7]))
        self.remove(t1[0][8], t1[2][8]).add(t1_aux1[0][3], t1_aux2[0][3])
        self.wait(2)

        t2 = MathTex(r'\text{sen}^2(x) ',r' + ',r' \text{cos}^2(x) ',r' = 1', color=YELLOW).scale(0.9)
        self.play(FadeOut(triangle_1, angle_1a, angle_1_label, 
                          side_1_label, sin_1[0][0:6], cos_1[0][0:6]))
        self.play(t1_aux1.animate.move_to(t2[0]),
                  t1_aux2.animate.move_to(t2[2]),
                  t1[1].animate.move_to(t2[1]),
                  t1[3][0:2].animate.move_to(t2[3]))
        self.wait(2)



        # Comentário sobre essa equação
        arrow_1 = Arrow(DOWN, UP, max_tip_length_to_length_ratio=0.18).scale(0.65).rotate(-30*DEGREES)
        arrow_1.next_to(t2[0], DOWN).shift(LEFT*0.6)
        
        self.play(FadeIn(arrow_1))
        self.wait(2)
        self.play(arrow_1.animate.shift(RIGHT*2))
        self.wait(2)
        self.play(arrow_1.animate.shift(LEFT*2))
        self.wait(2)



# Construindo o círculo trigonométrico
class vid6(MovingCameraScene):

    def angle_between(self, v1, v2):    # Calcula o ângulo entre dois vetores em graus
        cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.degrees(np.arccos(cos_theta))
    
    def construct(self):
            
        # Até aqui só demos conta de ângulos entre 0° e 90°

                # Criando pontos e linhas iniciais do triângulo     
        dot_A = Dot([0, 0, 0]).scale(0)
        dot_B = Dot([3*0.866, 3*0.5, 0]).scale(0)
        dot_C = always_redraw(lambda: Dot((dot_B.get_x(), 0, 0)).scale(0))

        line_AB = Line(dot_A, dot_B, color=WHITE)
        line_BC = Line(dot_B, dot_C, color=WHITE)
        line_CA = Line(dot_C, dot_A, color=WHITE)

                # Funções de atualização para os ângulos e linhas
        def update_triangle(mob):
                # Calculando os vetores atualizados
            AB = dot_B.get_center() - dot_A.get_center()
            BC = dot_C.get_center() - dot_B.get_center()
            CA = dot_A.get_center() - dot_C.get_center()

                # Calculando os ângulos internos
            angle_A = self.angle_between(AB, -CA)
            angle_B = self.angle_between(BC, -AB)
            angle_C = self.angle_between(CA, -BC)

                # Atualizando textos dos ângulos
            angle_A_text.become(MathTex(f"{angle_A:.0f}^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, dot_A, dot_C, radius=0.9, other_angle=True)))
            angle_B_text.become(MathTex(f"{angle_B:.0f}^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_A, dot_B, dot_C, radius=0.8)))
            angle_C_text.become(MathTex(f"{angle_C:.0f}^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, dot_C, dot_A, radius=0.9)))

                # Atualizando as linhas do triângulo
            line_AB.put_start_and_end_on(dot_A.get_center(), dot_B.get_center())
            line_BC.put_start_and_end_on(dot_B.get_center(), dot_C.get_center())
            line_CA.put_start_and_end_on(dot_C.get_center(), dot_A.get_center())

                # Atualizando as labels de seno e cosseno
            sin_label.become(MathTex(r'\text{sen}(',f'{angle_A:.0f}^\\circ',')', color=BLUE).scale(0.8).next_to(triangle_1, RIGHT, buff=0.1).next_to(sin_brace, RIGHT, buff=0.1))
            cos_label.become(MathTex(r'\text{cos}(',f'{angle_A:.0f}^\\circ',')', color=GREEN).scale(0.8).next_to(triangle_1, DOWN, buff=0.1).next_to(cos_brace, DOWN, buff=0.1))


        COLOR_ANGLE_1 = PURPLE
        COLOR_ANGLE_2 = GREEN
        COLOR_ANGLE_3 = RED

        angle_a = always_redraw(lambda: Angle.from_three_points(dot_B.get_center(), dot_A.get_center(), dot_C.get_center(), radius=0.2, stroke_width=40, color=COLOR_ANGLE_1, other_angle=True).set_z_index(-2))        
        angle_b = always_redraw(lambda: Angle.from_three_points(dot_A.get_center(), dot_B.get_center(), dot_C.get_center(), radius=0.2, stroke_width=40, color=COLOR_ANGLE_2).set_z_index(-1))       
        angle_c = always_redraw(lambda: Angle.from_three_points(dot_B.get_center(), dot_C.get_center(), dot_A.get_center(), radius=0.2, stroke_width=40, color=COLOR_ANGLE_3).set_z_index(-1))
        
        angle_A_text = MathTex("0^\\circ")
        angle_B_text = MathTex("0^\\circ")
        angle_C_text = MathTex("0^\\circ")

        for mob in [line_AB, line_BC, line_CA, angle_A_text, angle_B_text, angle_C_text]:
            mob.add_updater(update_triangle)

        triangle_1 = always_redraw(lambda: Polygon(dot_A.get_center(), dot_B.get_center(), dot_C.get_center(), color=WHITE, fill_opacity=0).set_z_index(2))

        black_sq1 = always_redraw(lambda: Square(color=BLACK).scale(10).set_opacity(1).next_to(dot_B, RIGHT, buff=0).set_z_index(-1))



        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-4, 4, 1],
                    x_length = 8,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)

        p1_x_tick = Line(DOWN*0.1, UP*0.1, color=GRAY).scale(1.4).move_to(axes.coords_to_point(3,0,0))
        n1_x_tick = p1_x_tick.copy().move_to(axes.coords_to_point(-3,0,0))
        p1_y_tick = p1_x_tick.copy().rotate(90*DEGREES).move_to(axes.coords_to_point(0,3,0))
        n1_y_tick = p1_x_tick.copy().rotate(90*DEGREES).move_to(axes.coords_to_point(0,-3,0))

        p1_x_label = MathTex('1').scale(0.9).set_opacity(0.6).next_to(p1_x_tick, DR, buff = 0.1)
        n1_x_label = MathTex('-1').scale(0.9).set_opacity(0.6).next_to(n1_x_tick, DL, buff = 0.1)
        p1_y_label = p1_x_label.copy().next_to(p1_y_tick, UL, buff = 0.1)
        n1_y_label = n1_x_label.copy().next_to(n1_y_tick, DL, buff = 0.1)

        g_axes = VGroup(axes, 
                        p1_x_tick, n1_x_tick, p1_y_tick, n1_y_tick,
                        p1_x_label, p1_y_label, n1_x_label, n1_y_label)



        path1_for_dot_B = axes.plot(lambda x: (9 - x**2)**0.5,
                            x_range=[3*0.866, 2.93], stroke_width = 0).set_color(BLUE).set_z_index(2)
        path2_for_dot_B = axes.plot(lambda x: (9 - x**2)**0.5,
                            x_range=[0.1, 2.93], stroke_width = 0).set_color(BLUE).set_z_index(2).reverse_points()
        path3_for_dot_B = axes.plot(lambda x: (9 - x**2)**0.5,
                            x_range=[0.1, 3*0.866], stroke_width = 0).set_color(BLUE).set_z_index(2)
        
        self.camera.frame.move_to(triangle_1)

        t1 = MathTex(r'0^{\circ} < x < 90^{\circ}').scale(0.9).next_to(triangle_1, UP, buff=2)
        
        labeled_line = always_redraw(lambda: LabeledLine(start=dot_A, end=dot_B, label='1', font_size=40, label_frame=False).set_z_index(2))
        
        sin_brace = always_redraw(lambda: Brace(triangle_1, RIGHT, buff=0.1, color=GRAY).set_z_index(3))
        cos_brace = always_redraw(lambda: Brace(triangle_1, DOWN, buff=0.1, color=GRAY))

        sin_label = MathTex(r'\text{sen}(30^{\circ})', color=BLUE).scale(0.8).next_to(sin_brace, RIGHT, buff=0.1)
        cos_label = MathTex(r'\text{cos}(30^{\circ})', color=GREEN).scale(0.8).next_to(cos_brace, DOWN, buff=0.1)

        # Mudando o ângulo de 0° para 90°
        self.add(dot_A, dot_B, dot_C, path2_for_dot_B)
        self.play(DrawBorderThenFill(triangle_1))
        self.add(black_sq1)
        self.wait(2)
        self.play(FadeIn(angle_a, angle_A_text))
        self.wait(2)
        self.play(FadeIn(t1))
        self.play(MoveAlongPath(dot_B, path1_for_dot_B), run_time=1.5)  
        self.play(MoveAlongPath(dot_B, path2_for_dot_B), run_time=3)  
        self.play(MoveAlongPath(dot_B, path3_for_dot_B), run_time=2.5)  
        self.wait(2)
        self.play(FadeOut(t1))
        self.wait(2)



        # Hipotenusa vale 1, então os catetos valem sen(x) e cos(x)
        self.play(FadeIn(labeled_line))
        self.wait(2)
        self.play(FadeIn(sin_label, sin_brace))
        self.wait(2)
        self.play(FadeIn(cos_label, cos_brace))
        self.wait(2)

        sin_label.add_updater(update_triangle)
        cos_label.add_updater(update_triangle)



        # Seno de 0°
        path4_for_dot_B = axes.plot(lambda x: (9 - x**2)**0.5,
                            x_range=[3*0.866, 2.98], stroke_width = 0).set_color(BLUE).set_z_index(2)
        
        self.play(MoveAlongPath(dot_B, path4_for_dot_B), run_time=2)  
        self.wait(2)
        self.play(FadeOut(angle_A_text), dot_B.animate.move_to((3,0.01,0)), run_time=2)
        self.wait(2)

        t2 = MathTex('= 0', color=GRAY).scale(0.9).next_to(sin_label, RIGHT, buff=0.2)
        self.play(FadeIn(t2))
        self.wait(2)
       


        # Cosseno de 0°
        t3 = MathTex('= 1', color=GRAY).scale(0.9).next_to(cos_label, RIGHT, buff=0.2)
        self.play(FadeIn(t3))
        self.wait(2)
        self.play(FadeOut(t2, t3))
        self.wait(2)



        #sin_of_0 = MathTex(r'\text{sen}(0^{\circ}) = 0').scale(0.8).to_edge(RIGHT).shift(UP*3.5+RIGHT*0.5)
        #cos_of_0 = MathTex(r'\text{cos}(0^{\circ}) = 1').scale(0.8).next_to(sin_of_0, DOWN, buff=0.5, aligned_edge=LEFT)

        


        # Seno e cosseno de 90°
        path5_for_dot_B = axes.plot(lambda x: (9 - x**2)**0.5,
                            x_range=[0.15, 2.99999], stroke_width = 0).set_color(BLUE).set_z_index(2).reverse_points()
        self.add(cos_label, angle_A_text)
        self.play(MoveAlongPath(dot_B, path5_for_dot_B), run_time=7)  
        self.wait(2)

        path6_for_dot_B = axes.plot(lambda x: (9 - x**2)**0.5,
                            x_range=[0.01, 0.15], stroke_width = 0).set_color(BLUE).set_z_index(2).reverse_points()
        self.play(MoveAlongPath(dot_B, path6_for_dot_B), run_time=2)  
        
        self.remove(angle_a, angle_A_text)
        t2.next_to(cos_label, RIGHT, buff=0.2)
        t3.next_to(sin_label, RIGHT, buff=0.2)

        self.wait(2)
        self.play(FadeIn(t3))
        self.wait(2)
        self.play(FadeIn(t2))
        self.wait(2)
        self.play(FadeOut(t2, t3))
        self.wait(2)



        # O vértice mais alto percorre um pedaço de circunferência de raio 1        
        path7_for_dot_B = axes.plot(lambda x: (9 - x**2)**0.5,
                            x_range=[0.01, 2.9], stroke_width = 0).set_color(BLUE).set_z_index(2)
        self.add(angle_a, angle_A_text)
        self.play(MoveAlongPath(dot_B, path7_for_dot_B), run_time=3)
        
        path8_for_dot_B = axes.plot(lambda x: (9 - x**2)**0.5,
                            x_range=[0.5, 2.9], stroke_width = 0).set_color(BLUE).set_z_index(2).reverse_points()
        self.play(MoveAlongPath(dot_B, path8_for_dot_B), run_time=3)


        
        dot_1 = always_redraw(lambda: Dot(dot_B.get_center(), color=YELLOW).scale(1.25).set_z_index(4))

        path = VMobject(color=YELLOW).set_z_index(5)
        path.set_points_as_corners([dot_1.get_center(), dot_1.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot_1.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        self.add(path)
        self.play(GrowFromCenter(dot_1), Flash(dot_1, num_lines=8))
        self.wait(2)

        #path9_for_dot_B = axes.plot(lambda x: (9 - x**2)**0.5,
        #                    x_range=[0.5, 2.99], stroke_width = 0).set_color(BLUE).set_z_index(2)
        path9_for_dot_B = ArcBetweenPoints(axes.coords_to_point(3*0.1736,3*0.9848,0), axes.coords_to_point(3*0.996,3*0.087,0), radius=-3, color=YELLOW)
        self.play(MoveAlongPath(dot_B, path9_for_dot_B), run_time=3)

        #path10_for_dot_B = axes.plot(lambda x: (9 - x**2)**0.5,
        #                    x_range=[3*0.866, 2.99], stroke_width = 0).set_color(BLUE).set_z_index(2).reverse_points()
        path10_for_dot_B = ArcBetweenPoints(axes.coords_to_point(3*0.996,3*0.087,0), axes.coords_to_point(3*0.866,3*1/2,0), radius=3, color=YELLOW)
        self.play(MoveAlongPath(dot_B, path10_for_dot_B), run_time=3)
        self.wait(2)


        circ_0 = ArcBetweenPoints(axes.coords_to_point(3,0,0), axes.coords_to_point(0,3,0), radius=3, color=YELLOW)
        circ_1 = DashedVMobject(Circle(radius=3, color=YELLOW, fill_opacity=0).move_to(axes.coords_to_point(0,0,0)), num_dashes=50)
        self.play(FadeIn(circ_1, circ_0),
                  self.camera.frame.animate.move_to(axes.coords_to_point(0,0,0)), 
                  run_time=2)
        self.play(FadeOut(circ_1))
        self.wait(2)



        # Adicionando o plano cartesiano: sen(x) e cos(x) são as coordenadas do ponto
        self.play(FadeIn(axes),
                  self.camera.frame.animate.scale(1.3),
                  run_time=2)
        self.wait(2)


        dot_coords = MathTex(r'(\text{cos}(30^{\circ}) ',r',',r' \text{sen}(30^{\circ}))').scale(0.8).next_to(dot_B, UR, buff=0.2)
        dot_coords[0][1:].set_color(GREEN)
        dot_coords[2][0:8].set_color(BLUE)

        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)

        cos_dot = always_redraw(lambda: Dot((dot_1.get_x(),0,0), color=GREEN).set_z_index(3).scale(1))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot_B.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))

        cos_label_copy = cos_label.copy()
        sin_label_copy = sin_label.copy()

        self.remove(cos_label).add(cos_label_copy)
        self.play(LaggedStart(Create(cos_dashed_line), Create(cos_line), GrowFromCenter(cos_dot), lag_ratio=0.2),
                  LaggedStart(FadeOut(cos_brace),
                              ReplacementTransform(cos_label_copy, dot_coords[0]),
                              FadeIn(cos_axis_label),
                              lag_ratio=0.2))
        self.wait(2)

        sin_dot = always_redraw(lambda: Dot((0,dot_1.get_y(),0), color=BLUE).set_z_index(3).scale(1))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot_B.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))

        self.remove(sin_label).add(sin_label_copy)
        self.play(LaggedStart(Create(sin_dashed_line), Create(sin_line), GrowFromCenter(sin_dot), lag_ratio=0.2),
                  LaggedStart(FadeOut(sin_brace, triangle_1),
                              FadeIn(dot_coords[1]),
                              ReplacementTransform(sin_label_copy, dot_coords[2]),
                              FadeIn(sin_axis_label),
                              lag_ratio=0.2))
        self.wait(2)
       


        # Podemos incluir ângulos fora da faixa de 0° a 90°
        circ_2 = Circle(radius=3, color=YELLOW, fill_opacity=0).rotate(30*DEGREES).move_to(axes.coords_to_point(0,0,0))
        self.play(Create(circ_2), run_time=3)
        self.remove(circ_0)
        self.play(circ_2.animate.set_color(WHITE).set_stroke_opacity(0.7),
                  path.animate.set_color(WHITE),
                  dot_1.animate.set_color(WHITE))
        dot_2 = dot_1.copy().set_color(WHITE)
        self.remove(dot_1).add(dot_2)
        self.wait(2)



# Construindo o círculo trigonométrico
class vid7(MovingCameraScene):

    def angle_between(self, v1, v2):    # Calcula o ângulo entre dois vetores em graus
        cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.degrees(np.arccos(cos_theta))
    
    def construct(self):

        # Retomando elementos
        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-4, 4, 1],
                    x_length = 8,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)

        p1_x_tick = Line(DOWN*0.1, UP*0.1, color=GRAY).scale(1.4).move_to(axes.coords_to_point(3,0,0))
        n1_x_tick = p1_x_tick.copy().move_to(axes.coords_to_point(-3,0,0))
        p1_y_tick = p1_x_tick.copy().rotate(90*DEGREES).move_to(axes.coords_to_point(0,3,0))
        n1_y_tick = p1_x_tick.copy().rotate(90*DEGREES).move_to(axes.coords_to_point(0,-3,0))

        p1_x_label = MathTex('1').scale(0.9).set_opacity(0.6).next_to(p1_x_tick, DR, buff = 0.1)
        n1_x_label = MathTex('-1').scale(0.9).set_opacity(0.6).next_to(n1_x_tick, DL, buff = 0.1)
        p1_y_label = p1_x_label.copy().next_to(p1_y_tick, UL, buff = 0.1)
        n1_y_label = n1_x_label.copy().next_to(n1_y_tick, DL, buff = 0.1)

        g_axes = VGroup(axes, 
                        p1_x_tick, n1_x_tick, p1_y_tick, n1_y_tick,
                        p1_x_label, p1_y_label, n1_x_label, n1_y_label)
        


        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.7, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        dot_B = Dot((3*0.866, 3*0.5, 0), color=WHITE).scale(1.25).set_z_index(4)
        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot_B.get_center(), label='1', font_size=40, label_frame=False).set_z_index(2))


        
        # Ângulo
        def update_triangle_2(mob):
                # Calculando os vetores atualizados
            AB = dot_B.get_center() - axes.coords_to_point(0,0,0)
            BC = axes.coords_to_point(3,0,0) - dot_B.get_center()
            CA = axes.coords_to_point(0,0,0) - axes.coords_to_point(3,0,0)

                # Calculando os ângulos internos
            angle_A = self.angle_between(AB, -CA)
            angle_A2 = 360 - angle_A
            angle_A3 = 360 + angle_A

                # Atualizando textos dos ângulos
            angle_A_text.become(MathTex(f"{angle_A:.0f}^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.9, other_angle=True).point_from_proportion(0.5)).set_z_index(10))
            angle_A2_text.become(MathTex(f"{angle_A2:.0f}^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.9, other_angle=True).point_from_proportion(0.5)).set_z_index(10))
            angle_A3_text.become(MathTex(f"{angle_A3:.0f}^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.9, other_angle=False).point_from_proportion(0.5)).set_z_index(10))
            angle_A4_text.become(MathTex(f"-{angle_A:.0f}^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.9, other_angle=False).point_from_proportion(0.5)).set_z_index(10))

            
        angle_A_text = (MathTex(f"30^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)))
        angle_A_text.add_updater(update_triangle_2)
        angle_A2_text = (MathTex(f"180^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)))
        angle_A2_text.add_updater(update_triangle_2)
        angle_A3_text = (MathTex(f"360^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)))
        angle_A3_text.add_updater(update_triangle_2)
        angle_A4_text = (MathTex(f"0^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)))
        angle_A4_text.add_updater(update_triangle_2)
        
        angle_a = always_redraw(lambda: Angle.from_three_points(dot_B.get_center(), axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2, stroke_width=40, color=PURPLE, other_angle=True).set_z_index(-2))        
        angle_a2 = always_redraw(lambda: Angle.from_three_points(dot_B.get_center(), axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2, stroke_width=40, color=PURPLE, other_angle=False).set_z_index(-2))        
        


        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)

        cos_dot = always_redraw(lambda: Dot((dot_B.get_x(),0,0), color=GREEN).set_z_index(3).scale(1))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot_B.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))

        sin_dot = always_redraw(lambda: Dot((0,dot_B.get_y(),0), color=BLUE).set_z_index(3).scale(1))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot_B.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))




        self.camera.frame.scale(1.3).move_to(axes.coords_to_point(0,0,0))
        self.add(axes, sin_axis_label, cos_axis_label, 
                 circ, dot_B, labeled_line, angle_a, angle_A_text,
                 cos_dot, cos_dashed_line, cos_line,
                 sin_dot, sin_dashed_line, sin_line)


    
        arrow_pos = CurvedArrow(axes.coords_to_point(3*0.996, 3*0.087, 0), axes.coords_to_point(3*0.707, 3*0.707, 0), radius=3, stroke_width=7, color=WHITE).shift(RIGHT*0.5+UP*0.5).rotate(5*DEGREES)
        arrow_pos_label = MathTex('+').scale(1.3).next_to(arrow_pos, RIGHT).shift(UP*0.5+LEFT*0.5)
        
        arrow_neg = CurvedArrow(axes.coords_to_point(3*0.996, -3*0.087, 0), axes.coords_to_point(3*0.707, -3*0.707, 0), radius=-3, stroke_width=7, color=WHITE).shift(RIGHT*0.5+DOWN*0.5).rotate(-5*DEGREES)
        arrow_neg_label = MathTex('-').scale(1.3).next_to(arrow_neg, RIGHT).shift(DOWN*0.5+LEFT*0.5)
        
        

        # Animação
        path1 = ArcBetweenPoints(axes.coords_to_point(3*0.866, 3*1/2, 0), axes.coords_to_point(-3*0.707, 3*0.707, 0), radius=3)
        self.play(MoveAlongPath(dot_B, path1), run_time=4)  



        # A faixa inclui todos os números
        t4 = MathTex(r'-\infty ^{\circ} < x < +\infty ^{\circ}').scale(1.17).to_edge(UR, buff=0.5).shift(RIGHT*1.5+UP*1)
        self.play(FadeIn(t4))
        self.wait(2)



        # Convenção de ângulos positivos e negativos
        arrow_pos = CurvedArrow(axes.coords_to_point(3*0.996, 3*0.087, 0), axes.coords_to_point(3*0.707, 3*0.707, 0), radius=3, stroke_width=7, color=WHITE).shift(RIGHT*0.5+UP*0.5).rotate(5*DEGREES)
        arrow_pos_label = MathTex('+').scale(1.3).next_to(arrow_pos, RIGHT).shift(UP*0.5+LEFT*0.5)
        
        arrow_neg = CurvedArrow(axes.coords_to_point(3*0.996, -3*0.087, 0), axes.coords_to_point(3*0.707, -3*0.707, 0), radius=-3, stroke_width=7, color=WHITE).shift(RIGHT*0.5+DOWN*0.5).rotate(-5*DEGREES)
        arrow_neg_label = MathTex('-').scale(1.3).next_to(arrow_neg, RIGHT).shift(DOWN*0.5+LEFT*0.5)

        self.play(LaggedStart(Create(arrow_pos), FadeIn(arrow_pos_label), lag_ratio=0.3))        
        path12 = Arc(angle=45*DEGREES, radius=3).rotate(135*DEGREES, about_point=axes.coords_to_point(0,0,0))
        self.play(MoveAlongPath(dot_B, path12), rate_func=rush_into, run_time=1.5)

        self.remove(angle_A_text).add(angle_A2_text)
        path13 = Arc(angle=179*DEGREES, radius=3).rotate(180*DEGREES, about_point=axes.coords_to_point(0,0,0))
        self.play(MoveAlongPath(dot_B, path13), rate_func=linear, run_time=2)

        angle_a_copy = angle_a.copy()
        self.remove(angle_A2_text, angle_a).add(angle_A3_text, angle_a_copy)
        path14 = Arc(angle=141*DEGREES, radius=3).rotate(-1*DEGREES, about_point=axes.coords_to_point(0,0,0))
        self.play(MoveAlongPath(dot_B, path14), rate_func=rush_from, run_time=3)
        self.wait(2)




        self.play(FadeOut(arrow_pos, arrow_pos_label,
                          dot_B, labeled_line, angle_a_copy, angle_A3_text,
                          sin_line, sin_dashed_line, sin_dot,
                          cos_line, cos_dashed_line, cos_dot))
        self.play(LaggedStart(Create(arrow_neg), FadeIn(arrow_neg_label), lag_ratio=0.3)) 
        self.wait(2)

        dot_B.move_to(axes.coords_to_point(3,-3*0.0001,0))
        self.play(FadeIn(dot_B, labeled_line, angle_a2, angle_A4_text,
                          sin_line, sin_dashed_line, sin_dot,
                          cos_line, cos_dashed_line, cos_dot))
        self.wait(2)
         
        self.play(dot_B.animate.shift(DOWN*0.0001))
        self.wait(2)
        path15 = Arc(angle=170*DEGREES, radius=3).rotate(-170*DEGREES, about_point=axes.coords_to_point(0,0,0)).reverse_points()
        self.play(MoveAlongPath(dot_B, path15), run_time=4)
        self.wait(2)

        self.play(FadeOut(arrow_neg, arrow_neg_label, t4,
                          dot_B, labeled_line, angle_a2, angle_A4_text,
                          sin_line, sin_dashed_line, sin_dot,
                          cos_line, cos_dashed_line, cos_dot))
        self.wait(2)



# Encontrando senos e cossenos pela simetria do círculo trigonométrico
class vid8(MovingCameraScene):

    def angle_between(self, v1, v2):    # Calcula o ângulo entre dois vetores em graus
        cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.degrees(np.arccos(cos_theta))
    
    def construct(self):

        # Retomando elementos
        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-4, 4, 1],
                    x_length = 8,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)

        p1_x_tick = Line(DOWN*0.1, UP*0.1, color=GRAY).scale(1.4).move_to(axes.coords_to_point(3,0,0))
        n1_x_tick = p1_x_tick.copy().move_to(axes.coords_to_point(-3,0,0))
        p1_y_tick = p1_x_tick.copy().rotate(90*DEGREES).move_to(axes.coords_to_point(0,3,0))
        n1_y_tick = p1_x_tick.copy().rotate(90*DEGREES).move_to(axes.coords_to_point(0,-3,0))

        p1_x_label = MathTex('1').scale(0.9).set_opacity(0.6).next_to(p1_x_tick, DR, buff = 0.1)
        n1_x_label = MathTex('-1').scale(0.9).set_opacity(0.6).next_to(n1_x_tick, DL, buff = 0.1)
        p1_y_label = p1_x_label.copy().next_to(p1_y_tick, UL, buff = 0.1)
        n1_y_label = n1_x_label.copy().next_to(n1_y_tick, DL, buff = 0.1)

        g_axes = VGroup(axes, 
                        p1_x_tick, n1_x_tick, p1_y_tick, n1_y_tick,
                        p1_x_label, p1_y_label, n1_x_label, n1_y_label)
        


        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.7, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot_B = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)
        dot_B2 = dot_B.copy().move_to(axes.coords_to_point(3*1, 3*0.001, 0))
        dot_B3 = dot_B.copy().move_to(axes.coords_to_point(3*1, 3*0.001, 0))
        dot_B4 = dot_B.copy().move_to(axes.coords_to_point(3*1, -3*0.001, 0))

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot_B.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))


        
        # Ângulo
        def update_triangle_2(mob):
                # Calculando os vetores atualizados
            AB = dot_B.get_center() - axes.coords_to_point(0,0,0)
            BC = axes.coords_to_point(3,0,0) - dot_B.get_center()
            CA = axes.coords_to_point(0,0,0) - axes.coords_to_point(3,0,0)

            AB2 = dot_B2.get_center() - axes.coords_to_point(0,0,0)
            AB3 = dot_B3.get_center() - axes.coords_to_point(0,0,0)
            AB4 = dot_B4.get_center() - axes.coords_to_point(0,0,0)

                # Calculando os ângulos internos
            angle_A = self.angle_between(AB, -CA)
            angle_A2 = 360 - angle_A
            angle_A3 = 360 + angle_A

            angle_B = self.angle_between(AB2, -CA)
            angle_C = self.angle_between(AB3, -CA)
            angle_C2 = 360 - self.angle_between(AB3, -CA)
            angle_D = self.angle_between(AB4, -CA)

                # Atualizando textos dos ângulos
            angle_A_text.become(MathTex(f"{angle_A:.0f}^\\circ", color=PURPLE_C).scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.9, other_angle=True).point_from_proportion(0.2)).set_z_index(10))
            angle_B_text.become(MathTex(f"{angle_B:.0f}^\\circ", color=PURPLE_B).scale(0.6).move_to(Angle.from_three_points(dot_B2, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=1, other_angle=True).point_from_proportion(0.5)).set_z_index(10))
            angle_C_text.become(MathTex(f"{angle_C:.0f}^\\circ", color=PURPLE_D).scale(0.6).move_to(Angle.from_three_points(dot_B3, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.8, other_angle=True).point_from_proportion(0.07)).set_z_index(10))
            angle_C_text_aux.become(MathTex(f"{angle_C2:.0f}^\\circ", color=PURPLE_D).scale(0.6).move_to(Angle.from_three_points(dot_B3, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.8, other_angle=True).point_from_proportion(0.07)).set_z_index(10))
            angle_D_text.become(MathTex(f"-{angle_D:.0f}^\\circ", color=PURPLE_A).scale(0.6).move_to(Angle.from_three_points(dot_B4, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=1, other_angle=False).point_from_proportion(0.5)).set_z_index(10))

            
        angle_A_text = (MathTex(f"30^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)).set_z_index(10))
        angle_A_text.add_updater(update_triangle_2)
        angle_B_text = (MathTex(f"30^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)).set_z_index(10))
        angle_B_text.add_updater(update_triangle_2)
        angle_C_text = (MathTex(f"30^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)).set_z_index(10))
        angle_C_text.add_updater(update_triangle_2)
        angle_C_text_aux = (MathTex(f"30^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)).set_z_index(10))
        angle_C_text_aux.add_updater(update_triangle_2)
        angle_D_text = (MathTex(f"30^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)).set_z_index(10))
        angle_D_text.add_updater(update_triangle_2)
        
        
        
        angle_a = always_redraw(lambda: Angle.from_three_points(dot_B.get_center(), axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.3, stroke_width=50, color=PURPLE_C, other_angle=True).set_z_index(-3))        
        angle_b = always_redraw(lambda: Angle.from_three_points(dot_B2.get_center(), axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.5, stroke_width=40, color=PURPLE_B, other_angle=True).set_z_index(-4))        
        angle_c = always_redraw(lambda: Angle.from_three_points(dot_B3.get_center(), axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2, stroke_width=40, color=PURPLE_D, other_angle=True).set_z_index(-2))        
        angle_d = always_redraw(lambda: Angle.from_three_points(dot_B4.get_center(), axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.4, stroke_width=57, color=PURPLE_A, other_angle=False).set_z_index(-2))        



        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)

        cos_dot = always_redraw(lambda: Dot((dot_B.get_x(),0,0), color=GREEN).set_z_index(3).scale(1))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot_B.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))

        sin_dot = always_redraw(lambda: Dot((0,dot_B.get_y(),0), color=BLUE).set_z_index(3).scale(1))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot_B.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))




        self.camera.frame.scale(1.3).move_to(axes.coords_to_point(0,0,0))
        self.add(axes, sin_axis_label, cos_axis_label) 
        self.play(FadeIn(circ, dot_B, labeled_line, angle_a, angle_A_text,
                         cos_dot, cos_dashed_line, cos_line,
                         sin_dot, sin_dashed_line, sin_line))
        self.wait(2)
        


        # Indo até os 150°
        path1 = Arc(angle=179.9*DEGREES, radius=3).rotate(0.001*DEGREES, about_point=axes.coords_to_point(0,0,0))
        self.play(MoveAlongPath(dot_B, path1), run_time=3)
        self.wait(2)

        path2 = Arc(angle=29.9*DEGREES, radius=3).rotate(150*DEGREES, about_point=axes.coords_to_point(0,0,0)).reverse_points()
        self.play(MoveAlongPath(dot_B, path2), run_time=3)
        self.wait(2)

        self.play(Indicate(angle_A_text))
        self.wait(2)



        # Adicionando os 30°
        cos_dot2 = always_redraw(lambda: Dot((dot_B2.get_x(),0,0), color=GREEN).set_z_index(3).scale(1.25))
        cos_dashed_line2 = always_redraw(lambda: DashedLine(dot_B2.get_center(), cos_dot2.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        cos_line2 = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot2.get_center(), stroke_width=8, color=GREEN).set_z_index(3))

        sin_dot2 = always_redraw(lambda: Dot((0,dot_B2.get_y(),0), color=BLUE).set_z_index(3).scale(1.25))
        sin_dashed_line2 = always_redraw(lambda: DashedLine(dot_B2.get_center(), sin_dot2.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        sin_line2 = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot2.get_center(), stroke_width=8, color=BLUE).set_z_index(3))

        line_b = always_redraw(lambda: Line(dot_B2.get_center(), axes.coords_to_point(0,0,0)).set_z_index(4))
        self.play(FadeIn(dot_B2, angle_b, angle_B_text, line_b,
                         cos_dot2, cos_dashed_line2, cos_line2,
                         sin_dot2, sin_dashed_line2, sin_line2))
        self.wait(2)

        path3 = Arc(angle=30*DEGREES, radius=3).rotate(0.001*DEGREES, about_point=axes.coords_to_point(0,0,0))
        self.play(MoveAlongPath(dot_B2, path3), run_time=2)
        self.wait(2)

        sin_30 = MathTex(r'\text{sen}(30^{\circ}) =',r' \frac{1}{2}').scale(0.9).to_edge(UR, buff=-0.8).shift(RIGHT*0.8)
        cos_30 = MathTex(r'\text{cos}(30^{\circ}) =',r' \frac{\sqrt{3}}{2}').scale(0.9).next_to(sin_30, DOWN, buff=0.5, aligned_edge=RIGHT)
        g1 = VGroup(sin_30[0][4:7], cos_30[0][4:7]).set_color(PURPLE_B)
        self.play(LaggedStart(FadeIn(sin_30), FadeIn(cos_30), lag_ratio=0.3))
        self.wait(2)



        # Os tamanhos de seno e cosseno de 150° são iguais aos de 30°
        sin_150 = MathTex(r'\text{sen}(150^{\circ}) =',r' \frac{1}{2}').scale(0.9).to_edge(UL, buff=-0.8).shift(LEFT*0.8)
        cos_150 = MathTex(r'\text{cos}(150^{\circ}) =',r' -\frac{\sqrt{3}}{2}').scale(0.9).next_to(sin_150, DOWN, buff=0.5, aligned_edge=LEFT)
        g2 = VGroup(sin_150[0][4:8], cos_150[0][4:8]).set_color(PURPLE_C)

            # Seno
        sin_dot2_copy = sin_dot2.copy().set_color(YELLOW)
        sin_line2_copy = sin_line2.copy().set_color(YELLOW)
        self.play(LaggedStart(Create(sin_line2_copy), GrowFromCenter(sin_dot2_copy), lag_ratio=0.3))
        self.play(FadeOut(sin_line2_copy, sin_dot2_copy))
        self.wait(2)
        self.play(FadeIn(sin_150[0]))
        self.play(TransformFromCopy(sin_30[1], sin_150[1]))
        self.wait(2)

            # Cosseno
        cos_dot2_copy = cos_dot2.copy().set_color(YELLOW)
        cos_line2_copy = cos_line2.copy().set_color(YELLOW)
        cos_dot_copy = cos_dot.copy().set_color(YELLOW)
        cos_line_copy = cos_line.copy().set_color(YELLOW)
        self.play(Create(cos_line_copy), Create(cos_line2_copy))
        self.play(GrowFromCenter(cos_dot_copy), GrowFromCenter(cos_dot2_copy))
        self.play(FadeOut(cos_dot_copy, cos_line_copy, cos_dot2_copy, cos_line2_copy))
        self.wait(2)
        self.play(FadeIn(cos_150[0]))
        self.play(TransformFromCopy(cos_30[1], cos_150[1][1:]))
        self.wait(2)
        self.play(GrowFromCenter(cos_150[1][0]), Flash(cos_150[1][0], num_lines=6))
        self.wait(2)



        # Senos e cossenos de 210° e -30° também têm esses mesmos tamanhos
            # 210°
        cos_dot3 = always_redraw(lambda: Dot((dot_B3.get_x(),0,0), color=GREEN).set_z_index(3).scale(1.25))
        cos_dashed_line3 = always_redraw(lambda: DashedLine(dot_B3.get_center(), cos_dot3.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        cos_line3 = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot3.get_center(), stroke_width=8, color=GREEN).set_z_index(3))

        sin_dot3 = always_redraw(lambda: Dot((0,dot_B3.get_y(),0), color=BLUE).set_z_index(3).scale(1.25))
        sin_dashed_line3 = always_redraw(lambda: DashedLine(dot_B3.get_center(), sin_dot3.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        sin_line3 = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot3.get_center(), stroke_width=8, color=BLUE).set_z_index(3))

        line_c = always_redraw(lambda: Line(dot_B3.get_center(), axes.coords_to_point(0,0,0)).set_z_index(4))

        self.play(FadeIn(dot_B3, line_c, angle_c, angle_C_text,
                         cos_dot3, cos_dashed_line3, cos_line3,
                         sin_dot3, sin_dashed_line3, sin_line3))
        self.wait(2)

        path4 = Arc(angle=30*DEGREES, radius=3).rotate(0.001*DEGREES, about_point=axes.coords_to_point(0,0,0))
        path5 = Arc(angle=150*DEGREES, radius=3).rotate(30*DEGREES, about_point=axes.coords_to_point(0,0,0))
        path6 = Arc(angle=30*DEGREES, radius=3).rotate(180*DEGREES, about_point=axes.coords_to_point(0,0,0))
        self.play(MoveAlongPath(dot_B3, path4), rate_func=rush_into)
        self.play(MoveAlongPath(dot_B3, path5), rate_func=linear, run_time=2)
        
        self.remove(angle_C_text).add(angle_C_text_aux)

        self.play(MoveAlongPath(dot_B3, path6), rate_func=rush_from)
        
        cos_210 = MathTex(r'\text{cos}(210^{\circ}) =',r' -\frac{\sqrt{3}}{2}').scale(0.9).to_edge(DL, buff=-0.8).shift(LEFT*0.8)
        sin_210 = MathTex(r'\text{sen}(210^{\circ}) =',r' -\frac{1}{2}').scale(0.9).next_to(cos_210, UP, buff=0.5, aligned_edge=LEFT)
        g3 = VGroup(sin_210[0][4:8], cos_210[0][4:8]).set_color(PURPLE_D)
        self.play(FadeIn(sin_210), FadeIn(cos_210))
        self.wait(2)



            # -30°
        cos_dot4 = always_redraw(lambda: Dot((dot_B4.get_x(),0,0), color=GREEN).set_z_index(3).scale(1.25))
        cos_dashed_line4 = always_redraw(lambda: DashedLine(dot_B4.get_center(), cos_dot4.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        cos_line4 = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot4.get_center(), stroke_width=8, color=GREEN).set_z_index(3))

        sin_dot4 = always_redraw(lambda: Dot((0,dot_B4.get_y(),0), color=BLUE).set_z_index(3).scale(1.25))
        sin_dashed_line4 = always_redraw(lambda: DashedLine(dot_B4.get_center(), sin_dot4.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        sin_line4 = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot4.get_center(), stroke_width=8, color=BLUE).set_z_index(3))

        line_d = always_redraw(lambda: Line(dot_B4.get_center(), axes.coords_to_point(0,0,0)).set_z_index(4))

        self.play(FadeIn(dot_B4, line_d, angle_d, angle_D_text,
                         cos_dot4, cos_dashed_line4, cos_line4,
                         sin_dot4, sin_dashed_line4, sin_line4))
        self.wait(2)

        path6 = Arc(angle=30*DEGREES, radius=3).rotate(-30.001*DEGREES, about_point=axes.coords_to_point(0,0,0)).reverse_points()
        self.play(MoveAlongPath(dot_B4, path6), run_time=2.5)
        
        cos_n30 = MathTex(r'\text{cos}(-30^{\circ}) =',r' \frac{\sqrt{3}}{2}').scale(0.9).to_edge(DR, buff=-0.8).shift(RIGHT*0.8)
        sin_n30 = MathTex(r'\text{sen}(-30^{\circ}) =',r' -\frac{1}{2}').scale(0.9).next_to(cos_n30, UP, buff=0.5, aligned_edge=RIGHT)
        g4 = VGroup(sin_n30[0][4:8], cos_n30[0][4:8]).set_color(PURPLE_A)
        self.play(FadeIn(sin_n30), FadeIn(cos_n30))
        self.wait(2)



# Mudando a unidade de graus para radiano
class vid9(MovingCameraScene):
    def angle_between(self, v1, v2):    # Calcula o ângulo entre dois vetores em graus
        cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.degrees(np.arccos(cos_theta))
    
    def construct(self):

        # Retomando elementos
        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-4, 4, 1],
                    x_length = 8,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)

        p1_x_tick = Line(DOWN*0.1, UP*0.1, color=GRAY).scale(1.4).move_to(axes.coords_to_point(3,0,0))
        n1_x_tick = p1_x_tick.copy().move_to(axes.coords_to_point(-3,0,0))
        p1_y_tick = p1_x_tick.copy().rotate(90*DEGREES).move_to(axes.coords_to_point(0,3,0))
        n1_y_tick = p1_x_tick.copy().rotate(90*DEGREES).move_to(axes.coords_to_point(0,-3,0))

        p1_x_label = MathTex('1').scale(0.9).set_opacity(0.6).next_to(p1_x_tick, DR, buff = 0.1)
        n1_x_label = MathTex('-1').scale(0.9).set_opacity(0.6).next_to(n1_x_tick, DL, buff = 0.1)
        p1_y_label = p1_x_label.copy().next_to(p1_y_tick, UL, buff = 0.1)
        n1_y_label = n1_x_label.copy().next_to(n1_y_tick, DL, buff = 0.1)

        g_axes = VGroup(axes, 
                        p1_x_tick, n1_x_tick, p1_y_tick, n1_y_tick,
                        p1_x_label, p1_y_label, n1_x_label, n1_y_label)
        


        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.7, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot_B = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)
        dot_B2 = dot_B.copy().move_to(axes.coords_to_point(3*1, 3*0.001, 0))
        dot_B3 = dot_B.copy().move_to(axes.coords_to_point(3*1, 3*0.001, 0))
        dot_B4 = dot_B.copy().move_to(axes.coords_to_point(3*1, -3*0.001, 0))

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot_B.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))


        
        # Ângulo
        def update_triangle_2(mob):
                # Calculando os vetores atualizados
            AB = dot_B.get_center() - axes.coords_to_point(0,0,0)
            BC = axes.coords_to_point(3,0,0) - dot_B.get_center()
            CA = axes.coords_to_point(0,0,0) - axes.coords_to_point(3,0,0)

            AB2 = dot_B2.get_center() - axes.coords_to_point(0,0,0)
            AB3 = dot_B3.get_center() - axes.coords_to_point(0,0,0)
            AB4 = dot_B4.get_center() - axes.coords_to_point(0,0,0)

                # Calculando os ângulos internos
            angle_A = self.angle_between(AB, -CA)
            angle_A2 = 360 - angle_A
            angle_A3 = 360 + angle_A

            angle_B = self.angle_between(AB2, -CA)
            angle_C = self.angle_between(AB3, -CA)
            angle_C2 = 360 - self.angle_between(AB3, -CA)
            angle_D = self.angle_between(AB4, -CA)

                # Atualizando textos dos ângulos
            angle_A_text.become(MathTex(f"{angle_A:.0f}^\\circ", color=PURPLE_C).scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.9, other_angle=True).point_from_proportion(0.2)).set_z_index(10))
            angle_B_text.become(MathTex(f"{angle_B:.0f}^\\circ", color=PURPLE_B).scale(0.6).move_to(Angle.from_three_points(dot_B2, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=1, other_angle=True).point_from_proportion(0.5)).set_z_index(10))
            angle_C_text.become(MathTex(f"{angle_C:.0f}^\\circ", color=PURPLE_D).scale(0.6).move_to(Angle.from_three_points(dot_B3, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.8, other_angle=True).point_from_proportion(0.07)).set_z_index(10))
            angle_C_text_aux.become(MathTex(f"{angle_C2:.0f}^\\circ", color=PURPLE_D).scale(0.6).move_to(Angle.from_three_points(dot_B3, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.8, other_angle=True).point_from_proportion(0.07)).set_z_index(10))
            angle_D_text.become(MathTex(f"-{angle_D:.0f}^\\circ", color=PURPLE_A).scale(0.6).move_to(Angle.from_three_points(dot_B4, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=1, other_angle=False).point_from_proportion(0.5)).set_z_index(10))



            
        angle_A_text = (MathTex(f"30^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)).set_z_index(10))
        angle_A_text.add_updater(update_triangle_2)
        angle_B_text = (MathTex(f"30^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)).set_z_index(10))
        angle_B_text.add_updater(update_triangle_2)
        angle_C_text = (MathTex(f"30^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)).set_z_index(10))
        angle_C_text.add_updater(update_triangle_2)
        angle_C_text_aux = (MathTex(f"30^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)).set_z_index(10))
        angle_C_text_aux.add_updater(update_triangle_2)
        angle_D_text = (MathTex(f"30^\\circ").scale(0.6).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2 + 3 * SMALL_BUFF, other_angle=True)).set_z_index(10))
        angle_D_text.add_updater(update_triangle_2)
        
        
        
        angle_a = always_redraw(lambda: Angle.from_three_points(dot_B.get_center(), axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.3, stroke_width=50, color=PURPLE_C, other_angle=True).set_z_index(-3))        
        angle_b = always_redraw(lambda: Angle.from_three_points(dot_B2.get_center(), axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.5, stroke_width=40, color=PURPLE_B, other_angle=True).set_z_index(-4))        
        angle_c = always_redraw(lambda: Angle.from_three_points(dot_B3.get_center(), axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.2, stroke_width=40, color=PURPLE_D, other_angle=True).set_z_index(-2))        
        angle_d = always_redraw(lambda: Angle.from_three_points(dot_B4.get_center(), axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.4, stroke_width=57, color=PURPLE_A, other_angle=False).set_z_index(-2))        

        line1 = Line(axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0))


        self.camera.frame.scale(1.3).move_to(axes.coords_to_point(0,1,0))



        self.play(FadeIn(circ, dot_B, labeled_line, line1, angle_a))

        path1 = Arc(angle=45*DEGREES, radius=3).rotate(0.001*DEGREES, about_point=axes.coords_to_point(0,0,0)) 
        self.play(MoveAlongPath(dot_B, path1), run_time=2) 

        t1 = MathTex(f"?", color=WHITE).scale(0.9).move_to(Angle.from_three_points(dot_B, axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), radius=0.9, other_angle=True).point_from_proportion(0.5)).set_z_index(10).add_updater(update_triangle_2)
        self.play(FadeIn(t1)) 
        self.wait(2) 

        t2 = Tex('Graus').next_to(circ, UP, buff=2)
        self.play(FadeIn(t2))
        self.wait(2) 



        # Explicação dos graus
        degree_ticks = VGroup(*[Line(LEFT*0.1+RIGHT*0.1, color=WHITE).scale(0.3).move_to(axes.coords_to_point(3,0,0)).rotate(i*DEGREES, about_point=axes.coords_to_point(0,0,0)) for i in range(360)])
        self.play(Write(degree_ticks), run_time=3)
        self.wait(2)



        t3_arc = VGroup(*[Line(LEFT*0.1+RIGHT*0.1, color=PURPLE).scale(0.3).move_to(axes.coords_to_point(3,0,0)).rotate(i*DEGREES, about_point=axes.coords_to_point(0,0,0)) for i in range(1)])
        t3_arc_copy = t3_arc.copy()

        t3_tracker = ValueTracker(1)
        t3 = always_redraw(lambda: MathTex(f"{t3_tracker.get_value():.0f}^\\circ", color=PURPLE_A).next_to(t3_arc, RIGHT, buff=0.5))

        self.play(self.camera.frame.animate.scale(0.4).move_to(axes.coords_to_point(0.9,1,0)))
        self.play(FadeIn(t3), FadeIn(t3_arc))
        self.add(t3_arc_copy)
        t3_arc.set_opacity(0)
        self.wait(2)
        

        degree_ticks_45 = VGroup(*[Line(LEFT*0.1+RIGHT*0.1, color=PURPLE).scale(0.3).move_to(axes.coords_to_point(3,0,0)).rotate(i*DEGREES, about_point=axes.coords_to_point(0,0,0)) for i in range(45)])
        self.play(MoveAlongPath(t3_arc, Arc(angle=45*DEGREES, radius=3)),
                  Write(degree_ticks_45),
                  t3_tracker.animate.set_value(45), 
                  run_time=2)
        self.wait(2)

        self.play(self.camera.frame.animate.scale(2.5).move_to(axes.coords_to_point(0,1,0)), run_time=3)
        self.wait(2)



        # Explicação do radiano
        t4 = Tex('Radiano').move_to(t2).shift(UP*2)
        self.play(LaggedStart(FadeOut(degree_ticks, degree_ticks_45, t3, t3_arc_copy, 
                                      angle_a, t1, labeled_line, dot_B, line1),
                              t2.animate.shift(UP*2),
                              t4.animate.shift(DOWN*2),
                              lag_ratio=0.3))
        self.wait(2)

        t4_aux = Tex('\it Raio', color=GRAY).next_to(t4, DOWN, buff=0.2)
        self.play(FadeIn(t4_aux))
        self.wait(2)
        self.play(FadeOut(t4_aux))
        self.wait(2)

        # Desenha o raio
        line3 = Line(axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), stroke_width=8, color=YELLOW)
        radius_label_1 = MathTex('R', color=YELLOW).next_to(line3, DOWN)
        self.play(LaggedStart(Create(line3), FadeIn(radius_label_1), lag_ratio=0.5))
        self.wait(2)



        # O raio vai para o lado do círculo
        line4 = line3.copy()
        self.add(line4)

        line3.become(Line(axes.coords_to_point(0,0,0), axes.coords_to_point(3,0,0), color=WHITE))
        self.play(Rotate(line4, -90*DEGREES, about_point=axes.coords_to_point(3.2,-0.2,0)),
                  radius_label_1.animate.set_color(WHITE))
        self.wait(2)
        


        # O raio se deita sobre o círculo
        line5 = Arc(angle=1.02, radius=3, color=YELLOW, stroke_width=8).rotate(-0.01, about_point=axes.c2p(0,0,0)).reverse_points()
        self.play(ReplacementTransform(line4, line5))
        self.wait(2)

        dot_center = Dot(axes.c2p(0,0,0)).set_z_index(3)
        line6 = line3.copy().scale(1.01).rotate(1, about_point=axes.coords_to_point(0,0,0)).set_z_index(2)
        angle_1 = always_redraw(lambda: Angle(line3, line6, radius=0.2, stroke_width=40, color=PURPLE, other_angle=False).set_z_index(-1))

        self.play(GrowFromCenter(dot_center), Create(line6), FadeIn(angle_1))
        self.wait(2)



        # 1 radiano
        angle_1_label_1 = Tex('1 rad', color=PURPLE).scale(0.9).move_to(Angle(line3, line6, radius=1, other_angle=False).point_from_proportion(0.35))
        self.play(FadeIn(angle_1_label_1))
        self.wait(2)

        radius_label_2 = radius_label_1.copy().set_color(YELLOW).move_to(line5).shift(RIGHT*0.8+UP*0.5)
        self.play(FadeIn(radius_label_2))
        self.wait(2)



        # 2 radianos
        line5_copy = line5.copy()
        radius_label_2_copy = radius_label_2.copy()
        path1 = Arc(angle=1, radius=3.55).rotate(0.52, about_point=axes.c2p(0,0,0))
        angle_1_label_2 = Tex('2 rad', color=PURPLE).scale(0.9).move_to(Angle(line3, Line(axes.c2p(0,0,0), axes.c2p(-3*0.416,3*0.909,0)), radius=1, other_angle=False).point_from_proportion(0.4))
        
        line6_copy = line6.copy().set_opacity(0.25)
        self.add(line6_copy)

        self.play(line5_copy.animate.shift(UP*0.2*0.479+RIGHT*0.2*0.877))
        self.play(Rotate(line5_copy, 1, about_point=axes.c2p(0,0,0)),
                  Rotate(line6, 1, about_point=axes.c2p(0,0,0)),
                  ReplacementTransform(angle_1_label_1, angle_1_label_2),
                  MoveAlongPath(radius_label_2_copy, path1))
        self.play(line5_copy.animate.shift(DOWN*0.2*0.997+LEFT*0.2*0.0707))
        self.wait(2)
        


        # 3,14 radianos
        line_180 = DashedLine(axes.c2p(-3,0,0), axes.c2p(3,0,0), color=GRAY).set_z_index(-2)
        self.play(FadeIn(line_180))
        self.wait(2)

        line5_copy2 = line5_copy.copy()
        radius_label_2_copy2 = radius_label_2_copy.copy()
        path2 = Arc(angle=1, radius=3.55).rotate(1 + 0.52, about_point=axes.c2p(0,0,0))
        angle_1_label_3 = Tex('3 rad', color=PURPLE).scale(0.9).move_to(Angle(line3, Line(axes.c2p(0,0,0), axes.c2p(-3*0.9899,3*0.1411,0)), radius=1, other_angle=False).point_from_proportion(0.4))
        
        line6_copy2 = line6.copy().set_opacity(0.25)
        self.add(line6_copy2)

        self.play(line5_copy2.animate.shift(UP*0.2*0.997+RIGHT*0.2*0.0707))
        self.play(Rotate(line5_copy2, 1, about_point=axes.c2p(0,0,0)),
                  Rotate(line6, 1.001, about_point=axes.c2p(0,0,0)),
                  ReplacementTransform(angle_1_label_2, angle_1_label_3),
                  MoveAlongPath(radius_label_2_copy2, path2))
        self.play(line5_copy2.animate.shift(DOWN*0.2*0.5984+RIGHT*0.2*0.8011))
        self.wait(2)

        line6_copy3 = line6.copy().set_opacity(0.25)
        self.add(line6_copy3)
        angle_1_label_4 = Tex('3,14 rad', color=PURPLE).scale(0.9).move_to(Angle(line3, Line(axes.c2p(0,0,0), axes.c2p(-3,3*0.0001,0)), radius=1, other_angle=False).point_from_proportion(0.4))


        self.play(self.camera.frame.animate.scale(0.5).move_to(axes.c2p(-2.5,0,0)))
        self.wait(2)

        line_014 = Arc(angle=0.14, radius=3, stroke_width=8).rotate(3.01, about_point=axes.c2p(0,0,0))
        brace_014 = ArcBrace(line_014, LEFT, color=GRAY).shift(LEFT*5.9+DOWN*0.03).rotate(-8*DEGREES)
        brace_014_label = MathTex(r'\approx 0,14R', color=GRAY).scale(0.7).next_to(brace_014, LEFT, buff=0.1)
        brace_014_label_copy = brace_014_label.copy().next_to(brace_014, LEFT, buff=0.1)

        self.play(FadeIn(brace_014))
        self.wait(2)
        self.play(Create(line_014),
                  Rotate(line6, 0.14151, about_point=axes.c2p(0,0,0)),
                  TransformMatchingShapes(angle_1_label_3, angle_1_label_4),
                  FadeIn(brace_014_label))
        self.wait(2)



        # Então meia-volta = pi R
        self.remove(t4)
        self.play(self.camera.frame.animate.scale(2).move_to(axes.c2p(0,1,0)))
        self.wait(2)



        t7 = Tex(r'Meia-volta',r'\: $=$ \:',r'$\pi R$').next_to(circ, UP, buff=2)
        t7[2][1].set_color(YELLOW)

        t5 = Tex('Meia-volta',r'\: $\approx$ \:',r'$R + R + R + 0,14R$').move_to(t7, aligned_edge=LEFT)
        g_t5 = VGroup(t5[2][0], t5[2][2], t5[2][4], t5[2][10]).set_color(YELLOW)
        
        t6 = Tex(r'Meia-volta',r'\: $\approx$ \:',r'$3,14 R$').move_to(t7, aligned_edge=LEFT)
        t6[2][4].set_color(YELLOW)
        
        self.play(FadeIn(t5[0:2]))
        self.wait(2)
        self.play(LaggedStart(ReplacementTransform(radius_label_2_copy2, t5[2][0]),
                              FadeOut(line5_copy2),
                              FadeIn(t5[2][1]),
                              ReplacementTransform(radius_label_2_copy, t5[2][2]),
                              FadeOut(line5_copy, line6_copy2),
                              FadeIn(t5[2][3]),
                              ReplacementTransform(radius_label_2, t5[2][4]),
                              FadeOut(line5, line6_copy),
                              FadeIn(t5[2][5]),
                              ReplacementTransform(brace_014_label[0][1:], t5[2][6:]),
                              FadeOut(brace_014_label[0][0], brace_014, line_014, line6_copy3, line_180),
                              lag_ratio=0.2))
        self.wait(2)

        self.play(FadeTransform(t5[2], t6[2], stretch=False))
        self.wait(2)

        self.play(FadeTransform(t5[1], t7[1], stretch=False),
                  FadeTransform(t6[2], t7[2], stretch=False))
        self.wait(2)



        # Então 180° = pi rad
        angle_1_label_5 = Tex(r'$\pi$ rad', color=PURPLE).scale(0.9).move_to(Angle(line3, Line(axes.c2p(0,0,0), axes.c2p(-3,3*0.0001,0)), radius=1, other_angle=False).point_from_proportion(0.4))

        t8 = MathTex(r'180^{\circ} = ',r' \pi \text{ rad}').shift(RIGHT*6+UP*2)
        self.play(FadeIn(t8[0]))
        self.wait(2)
        self.play(FadeIn(t8[1]), 
                  TransformMatchingShapes(angle_1_label_4, angle_1_label_5))
        self.play(FadeOut(t7[1:], t5[0]))
        self.wait(2)
        self.play(self.camera.frame.animate.move_to(axes.c2p(0,0,0)))
        self.wait(2)



        # Descobrindo outros ângulos em rad
            # 90° = pi/2
        angle_1_label_6 = Tex(r'$\pi/2$ rad', color=PURPLE).scale(0.9).move_to(Angle(line3, Line(axes.c2p(0,0,0), axes.c2p(0,3,0)), radius=1.1, other_angle=False).point_from_proportion(0.4))

        t9 = MathTex(r'90^{\circ} = ',r' \frac{\pi}{2} \text{ rad}').next_to(t8, DOWN, buff=0.8, aligned_edge=RIGHT)
        self.play(Rotate(line6, -90*DEGREES, about_point=axes.c2p(0,0,0)),
                  FadeIn(t9[0]),
                  FadeOut(angle_1_label_5))
        self.wait(2)
        self.play(FadeIn(t9[1], angle_1_label_6))
        self.wait(2)



            # 360° = 2pi
        angle_1_label_7 = Tex(r'$2 \pi$ rad', color=PURPLE).scale(0.9).move_to(Angle(line3, Line(axes.c2p(0,0,0), axes.c2p(3,-3*0.0001,0)), radius=1.1, other_angle=False).point_from_proportion(0.4))

        t10 = MathTex(r'360^{\circ} = ',r' 2 \pi \text{ rad}').next_to(t9, DOWN, buff=0.8, aligned_edge=RIGHT)
        self.play(Rotate(line6, 90*DEGREES, about_point=axes.c2p(0,0,0)),
                  FadeOut(angle_1_label_6),
                  rate_func=linear, run_time=2)

        angle_2 = always_redraw(lambda: Angle(line3, line6, radius=0.2, stroke_width=40, color=PURPLE, other_angle=False).set_z_index(-1))
        self.remove(angle_1).add(angle_2)

        self.play(Rotate(line6, 179.5*DEGREES, about_point=axes.c2p(0,0,0)),
                  FadeIn(t10[0]),
                  rate_func=linear, run_time=4)
        self.wait(2)
        self.play(FadeIn(t10[1], angle_1_label_7))
        self.wait(2)

        g1 = VGroup(t8, t9, t10)
        self.play(g1.animate.shift(RIGHT*5),
                  FadeOut(angle_2, angle_1_label_7, radius_label_1, dot_center))
        self.wait(2)



        sin_axis_label = MathTex(r'\text{sen}(x)', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}(x)', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)

        cos_dot = always_redraw(lambda: Dot((dot_B.get_x(),0,0), color=GREEN).set_z_index(3).scale(1.25))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot_B.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=8, color=GREEN).set_z_index(3))

        sin_dot = always_redraw(lambda: Dot((0,dot_B.get_y(),0), color=BLUE).set_z_index(3).scale(1.25))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot_B.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=8, color=BLUE).set_z_index(3))

        self.play(FadeIn(axes, 
                         sin_axis_label, sin_dashed_line, sin_line, sin_dot,
                         cos_axis_label, cos_dashed_line, cos_line, cos_dot))
        self.wait(2)



# Gráfico do seno
class vid10(MovingCameraScene):
    def construct(self):

        # Retomando elementos
        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-4, 4, 1],
                    x_length = 8,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)

        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.5, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))

        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)

        cos_dot = always_redraw(lambda: Dot((dot.get_x(),0,0), color=GREEN).set_z_index(3).scale(1))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))

        sin_dot = always_redraw(lambda: Dot((0,dot.get_y(),0), color=BLUE).set_z_index(3).scale(1))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))

        '''path = VMobject(color=WHITE)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)'''

        path = TracedPath(dot.get_center, stroke_width=6, stroke_color=WHITE, stroke_opacity=1).set_z_index(3)

        self.camera.frame.scale(1.3).move_to(axes.coords_to_point(0,0,0))

        self.add(axes, circ, labeled_line, dot, path,
                 sin_axis_label, sin_dashed_line, sin_line, sin_dot,
                 cos_axis_label, cos_dashed_line, cos_line, cos_dot)



        label_0 = MathTex(r'0').scale(0.9).next_to(axes.c2p(3,0,0), UR, buff=0.2)
        
        label_90 = MathTex(r'\pi/2').scale(0.9).next_to(axes.c2p(0,3,0), UR, buff=0.1)
        label_90[0][0].scale(1.1)

        label_180 = MathTex(r'\pi').scale(0.9).scale(1.1).next_to(axes.c2p(-3,0,0), UL, buff=0.2)
        
        label_270 = MathTex(r'3 \pi /2').scale(0.9).next_to(axes.c2p(0,-3,0), DR, buff=0.2)
        label_270[0][1].scale(1.1)

        label_360 = MathTex(r'2 \pi').scale(0.9).next_to(axes.c2p(3,0,0), DR, buff=0.2)
        label_360[0][1].scale(1.1)
        
        self.add(label_0, label_90, label_180, label_270, label_360) ############################3

        '''self.play(FadeIn(label_0, label_90, label_180, label_270, label_360))
        self.wait(2)

        self.play(Rotate(dot, 360*DEGREES, about_point=axes.c2p(0,0,0)), run_time=6)
        self.wait(2)
        self.wait(2)
        self.wait(2)
        self.wait(2)

        self.wait(3)'''



        # Adicionando um novo plano cartesiano
        axes_2 = Axes(x_range = [0, 3*8, 1],
                    y_range = [-4, 4, 1],
                    x_length = 3*4.5,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        axes_2.next_to(axes, RIGHT, buff=2)

        x_axes_2_label = MathTex('x', color=WHITE).next_to(axes_2.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)
        y_axes_2_label = MathTex(r'\text{sen}(x)', color=BLUE).scale(0.9).next_to(axes_2.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)

        sin_graph_0 = axes_2.plot(lambda x: 3*np.sin(x/3),
                         x_range=[0, 3*6.28], stroke_width = 7).set_color(BLUE).set_z_index(4)
        sin_graph_1 = axes_2.plot(lambda x: 3*np.sin(x/3),
                         x_range=[0, 3*PI/2], stroke_width = 7).set_color(YELLOW)
        sin_graph_2 = axes_2.plot(lambda x: 3*np.sin(x/3),
                         x_range=[3*PI/2, 3*PI], stroke_width = 7).set_color(YELLOW)
        sin_graph_3 = axes_2.plot(lambda x: 3*np.sin(x/3),
                         x_range=[3*PI, 9*PI/2], stroke_width = 7).set_color(YELLOW)
        sin_graph_4 = axes_2.plot(lambda x: 3*np.sin(x/3),
                         x_range=[9*PI/2, 6*PI], stroke_width = 7).set_color(YELLOW)
        
        dot_sin_graph = Dot(color=BLUE).move_to(axes_2.c2p(0,0,0)).scale(1.25).set_z_index(5)
        dot_sin_graph_projection = always_redraw(lambda: Line(dot_sin_graph.get_center(), (dot_sin_graph.get_x(),0,0), stroke_width=8, color=BLUE).set_z_index(-5))
        white_path = always_redraw(lambda: Line(axes_2.c2p(0,0,0), (dot_sin_graph.get_x(),0,0)).set_z_index(5))



        '''dot_sin_graph_path = VMobject(stroke_width=7, color=YELLOW)
        dot_sin_graph_path.set_points_as_corners([dot_sin_graph.get_center(), dot_sin_graph.get_center()])        
        def update_path2(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot_sin_graph.get_center()])
            path.become(previous_path)
        dot_sin_graph_path.add_updater(update_path2)'''

        dot_sin_graph_path = TracedPath(dot_sin_graph.get_center, stroke_width=7, stroke_color=YELLOW, stroke_opacity=1).set_z_index(3)


        '''dot_sin_graph_path3 = VMobject(stroke_width=7, color=WHITE)
        dot_sin_graph_path3.set_points_as_corners([dot_sin_graph.get_center(), dot_sin_graph.get_center()])        
        def update_path3(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot_sin_graph.get_x(),0,0])
            path.become(previous_path)
        dot_sin_graph_path3.add_updater(update_path3)'''




        tick_p1 = Line(LEFT*0.1, RIGHT*0.1, color=GRAY).scale(1.4).move_to(axes_2.coords_to_point(0,3,0))
        tick_p1_label = MathTex('1').scale(0.9).set_opacity(0.7).next_to(tick_p1, LEFT, buff = 0.1)
        
        tick_n1 = tick_p1.copy().move_to(axes_2.coords_to_point(0,-3,0))
        tick_n1_label = tick_p1_label.copy().next_to(tick_n1, LEFT, buff = 0.1)

        tick_x1 = tick_p1.copy().rotate(90*DEGREES).move_to(axes_2.coords_to_point(3*PI/2,0,0))
        tick_x2 = tick_x1.copy().move_to(axes_2.coords_to_point(3*PI,0,0))
        tick_x3 = tick_x1.copy().move_to(axes_2.coords_to_point(9*PI/2,0,0))
        tick_x4 = tick_x1.copy().move_to(axes_2.coords_to_point(6*PI,0,0))

        tick_x0_label = MathTex(r'0').scale(0.9).set_opacity(0.7).next_to(axes_2.c2p(0,0,0), LEFT, buff = 0.2)
        tick_x1_label = MathTex(r'\frac{\pi}{2}').scale(0.9).set_opacity(0.7).next_to(tick_x1, DOWN, buff = 0.2)
        tick_x2_label = MathTex(r'\pi').scale(0.9).set_opacity(0.7).next_to(tick_x2, DOWN, buff = 0.2)
        tick_x3_label = MathTex(r'\frac{3\pi}{2}').scale(0.9).set_opacity(0.7).next_to(tick_x3, DOWN, buff = 0.2)
        tick_x4_label = MathTex(r'2 \pi').scale(0.9).set_opacity(0.7).next_to(tick_x4, DOWN, buff = 0.2)
        
        tick_x1_label[0][0].scale(1.1)
        tick_x2_label[0][0].scale(1.1)
        tick_x3_label[0][1].scale(1.1)
        tick_x4_label[0][1].scale(1.1)

        g_axes_2 = VGroup(axes_2, x_axes_2_label, y_axes_2_label, tick_x0_label,
                          tick_p1, tick_p1_label, tick_n1, tick_n1_label,
                          tick_x1, tick_x2, tick_x3, tick_x4,
                          tick_x1_label, tick_x2_label, tick_x3_label, tick_x4_label)



        self.play(FadeIn(g_axes_2),
                  FadeOut(cos_axis_label, cos_dashed_line, cos_line, cos_dot),
                  self.camera.frame.animate.scale(1.4).move_to(axes.coords_to_point(8,0,0)))
        self.wait(2)
        self.play(Indicate(x_axes_2_label))
        self.wait(2)
        self.play(Indicate(y_axes_2_label))
        self.wait(2)



        self.play(GrowFromCenter(dot_sin_graph), Flash(dot_sin_graph, num_lines=8))
        self.add(dot_sin_graph_projection, dot_sin_graph_path, white_path)
        self.wait(2)
        self.play(Rotate(dot, 90*DEGREES, about_point=axes.c2p(0,0,0)),
                  MoveAlongPath(dot_sin_graph, sin_graph_1),
                  run_time=5)
        self.wait(2)
        self.play(Rotate(dot, 90*DEGREES, about_point=axes.c2p(0,0,0)),
                  MoveAlongPath(dot_sin_graph, sin_graph_2),
                  run_time=5)
        self.wait(2)
        self.play(Rotate(dot, 90*DEGREES, about_point=axes.c2p(0,0,0)),
                  MoveAlongPath(dot_sin_graph, sin_graph_3),
                  run_time=5)
        self.wait(2)
        self.play(Rotate(dot, 90*DEGREES, about_point=axes.c2p(0,0,0)),
                  MoveAlongPath(dot_sin_graph, sin_graph_4),
                  run_time=5)
        self.wait(2)



        # Aumentando mais ainda o ângulo: o ciclo se repete
        axes_2b = Axes(x_range = [0, 12*PI + 1, 1],
                    y_range = [-4, 4, 1],
                    x_length = 21.7575,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        axes_2b.move_to(axes_2, aligned_edge=LEFT)
        
        extra_tick_p1 = tick_x1.copy().move_to(axes_2b.coords_to_point(3*2.5*PI,0,0))
        extra_tick_p2 = tick_x1.copy().move_to(axes_2b.coords_to_point(3*3*PI,0,0))
        extra_tick_p3 = tick_x1.copy().move_to(axes_2b.coords_to_point(3*3.5*PI,0,0))
        extra_tick_p4 = tick_x1.copy().move_to(axes_2b.coords_to_point(3*4*PI,0,0))
        
        extra_tick_p1_label = MathTex(r'\frac{5\pi}{2}').scale(0.9).set_opacity(0.7).next_to(extra_tick_p1, DOWN, buff = 0.2)
        extra_tick_p2_label = MathTex(r'3\pi').scale(0.9).set_opacity(0.7).next_to(extra_tick_p2, DOWN, buff = 0.2)
        extra_tick_p3_label = MathTex(r'\frac{7\pi}{2}').scale(0.9).set_opacity(0.7).next_to(extra_tick_p3, DOWN, buff = 0.2)
        extra_tick_p4_label = MathTex(r'4\pi').scale(0.9).set_opacity(0.7).next_to(extra_tick_p4, DOWN, buff = 0.2)

        

        self.play(FadeIn(sin_graph_0))
        sin_graph_5 = axes_2.plot(lambda x: 3*np.sin(x/3),
                         x_range=[6*PI, 12*PI], stroke_width = 7).set_color(BLUE)
        
        self.play(Rotate(dot, 360*DEGREES, about_point=axes.c2p(0,0,0)),
                  MoveAlongPath(dot_sin_graph, sin_graph_5),
                  self.camera.frame.animate.scale(1.3).shift(RIGHT*4),

                  LaggedStart(ReplacementTransform(axes_2.get_x_axis(), axes_2b.get_x_axis()),
                              x_axes_2_label.animate.next_to(axes_2b.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4),
                              y_axes_2_label.animate.next_to(axes_2b.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1),
                              FadeIn(extra_tick_p1, extra_tick_p1_label),
                              FadeIn(extra_tick_p2, extra_tick_p2_label),
                              FadeIn(extra_tick_p3, extra_tick_p3_label),
                              FadeIn(extra_tick_p4, extra_tick_p4_label),
                              lag_ratio=0.5),

                  run_time=10)
        self.wait(2)
        
        

        # Indo para os ângulos negativos: o ciclo se repete
        self.play(FadeOut(dot_sin_graph, dot_sin_graph_path, dot_sin_graph_projection),
                  FadeIn(sin_graph_5))

        g1 = VGroup(axes_2.get_y_axis(), axes_2b.get_x_axis(), x_axes_2_label, y_axes_2_label, tick_x0_label,
                    tick_p1, tick_p1_label, tick_n1, tick_n1_label,
                    tick_x1, tick_x2, tick_x3, tick_x4,
                    tick_x1_label, tick_x2_label, tick_x3_label, tick_x4_label, 
                    extra_tick_p1, extra_tick_p2, extra_tick_p3, extra_tick_p4,
                    extra_tick_p1_label, extra_tick_p2_label, extra_tick_p3_label, extra_tick_p4_label,
                    sin_graph_0, sin_graph_5)
        
        white_path_copy = white_path.copy()
        self.remove(white_path).add(white_path_copy)
        self.play(g1.animate.shift(RIGHT*10),
                  FadeOut(path), run_time=4)
        self.add(path)
        dot_sin_graph.move_to(axes_2.c2p(0,0,0))
        self.play(GrowFromCenter(dot_sin_graph))

        dot_sin_graph_path2 = VMobject(stroke_width=7, color=YELLOW)
        dot_sin_graph_path2.set_points_as_corners([dot_sin_graph.get_center(), dot_sin_graph.get_center()])        
        def update_path2(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot_sin_graph.get_center()])
            path.become(previous_path)
        dot_sin_graph_path2.add_updater(update_path2)
        self.add(dot_sin_graph_path2, dot_sin_graph_projection)

        sin_graph_6 = sin_graph_0.copy().move_to(axes_2.c2p(0,0,0), aligned_edge=RIGHT).reverse_points()
        #axes_2.plot(lambda x: 3*np.sin(x/3),
        #                 x_range=[-6*PI, 0], stroke_width = 7).set_color(YELLOW).reverse_points()
        self.play(Rotate(dot, -360*DEGREES, about_point=axes.c2p(0,0,0)),
                  MoveAlongPath(dot_sin_graph, sin_graph_6),
                  run_time=10)
        self.play(FadeOut(dot_sin_graph, dot_sin_graph_path2, dot_sin_graph_projection))
        self.wait(2)

        self.play(g1.animate.shift(LEFT*10), run_time=3)
        self.wait(2)



# Gráfico do cosseno
class vid11(MovingCameraScene):
    def construct(self):

        # Retomando elementos
        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-4, 4, 1],
                    x_length = 8,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)

        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.5, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))

        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)

        cos_dot = always_redraw(lambda: Dot((dot.get_x(),0,0), color=GREEN).set_z_index(3).scale(1))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))

        sin_dot = always_redraw(lambda: Dot((0,dot.get_y(),0), color=BLUE).set_z_index(3).scale(1))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))

        path = VMobject(color=WHITE)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        self.camera.frame.scale(1.3).move_to(axes.coords_to_point(0,0,0))

        self.add(axes, circ, labeled_line, dot, path,
                 sin_axis_label, sin_dashed_line, sin_line, sin_dot,
                 cos_axis_label, cos_dashed_line, cos_line, cos_dot)



        label_0 = MathTex(r'0').scale(0.9).next_to(axes.c2p(3,0,0), UR, buff=0.2)
        
        label_90 = MathTex(r'\pi/2').scale(0.9).next_to(axes.c2p(0,3,0), UR, buff=0.1)
        label_90[0][0].scale(1.1)

        label_180 = MathTex(r'\pi').scale(0.9).scale(1.1).next_to(axes.c2p(-3,0,0), UL, buff=0.2)
        
        label_270 = MathTex(r'3 \pi /2').scale(0.9).next_to(axes.c2p(0,-3,0), DR, buff=0.2)
        label_270[0][1].scale(1.1)

        label_360 = MathTex(r'2 \pi').scale(0.9).next_to(axes.c2p(3,0,0), DR, buff=0.2)
        label_360[0][1].scale(1.1)
        
        self.add(label_0, label_90, label_180, label_270, label_360) ############################3



        # Adicionando um novo plano cartesiano
        axes_2 = Axes(x_range = [0, 12*PI + 1, 1],
                    y_range = [-4, 4, 1],
                    x_length = 21.7575,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        axes_2.next_to(axes, RIGHT, buff=2)

        x_axes_2_label = MathTex('x', color=WHITE).next_to(axes_2.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)
        y_axes_2_label = MathTex(r'\text{cos}(x)', color=GREEN).scale(0.9).next_to(axes_2.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)

        sin_graph_0 = axes_2.plot(lambda x: 3*np.cos(x/3),
                         x_range=[0, 3*6.28], stroke_width = 7).set_color(BLUE).set_z_index(4)
        sin_graph_1 = axes_2.plot(lambda x: 3*np.cos(x/3),
                         x_range=[0, 3*PI/2], stroke_width = 7).set_color(YELLOW)
        sin_graph_2 = axes_2.plot(lambda x: 3*np.cos(x/3),
                         x_range=[3*PI/2, 3*PI], stroke_width = 7).set_color(YELLOW)
        sin_graph_3 = axes_2.plot(lambda x: 3*np.cos(x/3),
                         x_range=[3*PI, 9*PI/2], stroke_width = 7).set_color(YELLOW)
        sin_graph_4 = axes_2.plot(lambda x: 3*np.cos(x/3),
                         x_range=[9*PI/2, 6*PI], stroke_width = 7).set_color(YELLOW)
        
        dot_sin_graph = Dot(color=GREEN).move_to(axes_2.c2p(0,3,0)).scale(1.25).set_z_index(5)
        dot_sin_graph_projection = always_redraw(lambda: Line((dot_sin_graph.get_x(),0,0), dot_sin_graph.get_center(), stroke_width=8, color=GREEN).set_z_index(-5))
        white_path = always_redraw(lambda: Line(axes_2.c2p(0,0,0), (dot_sin_graph.get_x(),0,0)).set_z_index(5))



        dot_sin_graph_path = VMobject(stroke_width=7, color=YELLOW)
        dot_sin_graph_path.set_points_as_corners([dot_sin_graph.get_center(), dot_sin_graph.get_center()])        
        def update_path2(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot_sin_graph.get_center()])
            path.become(previous_path)
        dot_sin_graph_path.add_updater(update_path2)


        '''dot_sin_graph_path3 = VMobject(stroke_width=7, color=WHITE)
        dot_sin_graph_path3.set_points_as_corners([dot_sin_graph.get_center(), dot_sin_graph.get_center()])        
        def update_path3(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot_sin_graph.get_x(),0,0])
            path.become(previous_path)
        dot_sin_graph_path3.add_updater(update_path3)'''




        tick_p1 = Line(LEFT*0.1, RIGHT*0.1, color=GRAY).scale(1.4).move_to(axes_2.coords_to_point(0,3,0))
        tick_p1_label = MathTex('1').scale(0.9).set_opacity(0.7).next_to(tick_p1, LEFT, buff = 0.1)
        
        tick_n1 = tick_p1.copy().move_to(axes_2.coords_to_point(0,-3,0))
        tick_n1_label = tick_p1_label.copy().next_to(tick_n1, LEFT, buff = 0.1)

        tick_x1 = tick_p1.copy().rotate(90*DEGREES).move_to(axes_2.coords_to_point(3*PI/2,0,0))
        tick_x2 = tick_x1.copy().move_to(axes_2.coords_to_point(3*PI,0,0))
        tick_x3 = tick_x1.copy().move_to(axes_2.coords_to_point(9*PI/2,0,0))
        tick_x4 = tick_x1.copy().move_to(axes_2.coords_to_point(6*PI,0,0))

        tick_x0_label = MathTex(r'0').scale(0.9).set_opacity(0.7).next_to(axes_2.c2p(0,0,0), LEFT, buff = 0.2)
        tick_x1_label = MathTex(r'\frac{\pi}{2}').scale(0.9).set_opacity(0.7).next_to(tick_x1, DOWN, buff = 0.2)
        tick_x2_label = MathTex(r'\pi').scale(0.9).set_opacity(0.7).next_to(tick_x2, DOWN, buff = 0.2)
        tick_x3_label = MathTex(r'\frac{3\pi}{2}').scale(0.9).set_opacity(0.7).next_to(tick_x3, DOWN, buff = 0.2)
        tick_x4_label = MathTex(r'2 \pi').scale(0.9).set_opacity(0.7).next_to(tick_x4, DOWN, buff = 0.2)
        
        tick_x1_label[0][0].scale(1.1)
        tick_x2_label[0][0].scale(1.1)
        tick_x3_label[0][1].scale(1.1)
        tick_x4_label[0][1].scale(1.1)

        g_axes_2 = VGroup(axes_2, x_axes_2_label, y_axes_2_label, tick_x0_label,
                          tick_p1, tick_p1_label, tick_n1, tick_n1_label,
                          tick_x1, tick_x2, tick_x3, tick_x4,
                          tick_x1_label, tick_x2_label, tick_x3_label, tick_x4_label)

        extra_tick_p1 = tick_x1.copy().move_to(axes_2.coords_to_point(3*2.5*PI,0,0))
        extra_tick_p2 = tick_x1.copy().move_to(axes_2.coords_to_point(3*3*PI,0,0))
        extra_tick_p3 = tick_x1.copy().move_to(axes_2.coords_to_point(3*3.5*PI,0,0))
        extra_tick_p4 = tick_x1.copy().move_to(axes_2.coords_to_point(3*4*PI,0,0))
        
        extra_tick_p1_label = MathTex(r'\frac{5\pi}{2}').scale(0.9).set_opacity(0.7).next_to(extra_tick_p1, DOWN, buff = 0.2)
        extra_tick_p2_label = MathTex(r'3\pi').scale(0.9).set_opacity(0.7).next_to(extra_tick_p2, DOWN, buff = 0.2)
        extra_tick_p3_label = MathTex(r'\frac{7\pi}{2}').scale(0.9).set_opacity(0.7).next_to(extra_tick_p3, DOWN, buff = 0.2)
        extra_tick_p4_label = MathTex(r'4\pi').scale(0.9).set_opacity(0.7).next_to(extra_tick_p4, DOWN, buff = 0.2)



        self.add(g_axes_2, x_axes_2_label, y_axes_2_label,
                 extra_tick_p1, extra_tick_p1_label,
                 extra_tick_p2, extra_tick_p2_label,
                 extra_tick_p3, extra_tick_p3_label,
                 extra_tick_p4, extra_tick_p4_label).remove(sin_axis_label, sin_dashed_line, sin_line, sin_dot)
        self.camera.frame.scale(1.4).move_to(axes.coords_to_point(8,0,0))
        
        dot_sin_graph_projection_copy = dot_sin_graph_projection.copy()
        self.play(LaggedStart(Create(dot_sin_graph_projection_copy), GrowFromCenter(dot_sin_graph), lag_ratio=0.5))
        self.remove(dot_sin_graph_projection_copy).add(dot_sin_graph_projection)
        self.wait(2)

        self.add(dot_sin_graph_path, white_path)
        self.wait(2)
        self.play(Rotate(dot, 359.9*DEGREES, about_point=axes.c2p(0,0,0)),
                  MoveAlongPath(dot_sin_graph, sin_graph_0), 
                  rate_func=linear, run_time=15)
        self.wait(2)

        self.remove(dot_sin_graph_path).add(sin_graph_0)
        self.wait(2)

        sin_graph_5 = axes_2.plot(lambda x: 3*np.cos(x/3),
                         x_range=[6*PI - 1, 12*PI], stroke_width = 7).set_color(YELLOW)
        sin_graph_6 = sin_graph_0.copy().set_color(YELLOW).set_stroke(opacity=0.3).move_to(axes_2.c2p(0,0,0), aligned_edge=RIGHT)
        self.play(FadeIn(sin_graph_5, sin_graph_6))
        self.wait(2)





# Comparando os gráficos de seno e cosseno
class vid12(MovingCameraScene):
    def construct(self):

        axes_2 = Axes(x_range = [0, 3*8, 1],
                    y_range = [-4, 4, 1],
                    x_length = 3*4.5,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)

        x_axes_2_label = MathTex('x', color=WHITE).next_to(axes_2.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)
        y_axes_2_label = MathTex(r'\text{sen}(x)', color=WHITE).scale(0.9).next_to(axes_2.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)

        sin_graph_0 = axes_2.plot(lambda x: 3*np.sin(x/3),
                         x_range=[0, 3*6.28], stroke_width = 7).set_color(BLUE).set_z_index(4)
   
        x_axes_2_label = MathTex('x', color=WHITE).next_to(axes_2.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)
        y_axes_2_label = MathTex(r'\text{sen}(x) \:/\: \text{cos}(x)', color=WHITE).scale(0.9).next_to(axes_2.get_y_axis(), UP, buff=0.2)

        y_axes_2_label[0][0:6].set_color(BLUE)
        y_axes_2_label[0][7:].set_color(GREEN)

        sin_graph_0 = axes_2.plot(lambda x: 2*np.sin(x/2),
                         x_range=[0, 3*8], stroke_width = 7).set_color(BLUE).set_z_index(4)
        cos_graph_0 = axes_2.plot(lambda x: 2*np.cos(x/2),
                         x_range=[0, 3*8], stroke_width = 7).set_color(GREEN).set_z_index(4)



        tick_x1 = Line(LEFT*0.1, RIGHT*0.1, color=GRAY).scale(1.4).rotate(90*DEGREES).move_to(axes_2.coords_to_point(2*PI/2,0,0))
        tick_x2 = tick_x1.copy().move_to(axes_2.coords_to_point(2*PI,0,0))
        tick_x3 = tick_x1.copy().move_to(axes_2.coords_to_point(2*3*PI/2,0,0))
        tick_x4 = tick_x1.copy().move_to(axes_2.coords_to_point(4*PI,0,0))

        tick_x0_label = MathTex(r'0').scale(0.9).set_opacity(0.7).next_to(axes_2.c2p(0,0,0), LEFT, buff = 0.2)
        tick_x1_label = MathTex(r'\frac{\pi}{2}').scale(0.9).set_opacity(0.7).next_to(tick_x1, DOWN, buff = 0.2)
        tick_x2_label = MathTex(r'\pi').scale(0.9).set_opacity(0.7).next_to(tick_x2, DOWN, buff = 0.2)
        tick_x3_label = MathTex(r'\frac{3\pi}{2}').scale(0.9).set_opacity(0.7).next_to(tick_x3, DOWN, buff = 0.2)
        tick_x4_label = MathTex(r'2 \pi').scale(0.9).set_opacity(0.7).next_to(tick_x4, DOWN, buff = 0.2)
        
        tick_x1_label[0][0].scale(1.1)
        tick_x2_label[0][0].scale(1.1)
        tick_x3_label[0][1].scale(1.1)
        tick_x4_label[0][1].scale(1.1)

        

        extra_tick_p1 = tick_x1.copy().move_to(axes_2.coords_to_point(2*2.5*PI,0,0))
        extra_tick_p2 = tick_x1.copy().move_to(axes_2.coords_to_point(2*3*PI,0,0))
        extra_tick_p3 = tick_x1.copy().move_to(axes_2.coords_to_point(2*3.5*PI,0,0))
        
        extra_tick_p1_label = MathTex(r'\frac{5\pi}{2}').scale(0.9).set_opacity(0.7).next_to(extra_tick_p1, DOWN, buff = 0.2)
        extra_tick_p2_label = MathTex(r'3\pi').scale(0.9).set_opacity(0.7).next_to(extra_tick_p2, DOWN, buff = 0.2)
        extra_tick_p3_label = MathTex(r'\frac{7\pi}{2}').scale(0.9).set_opacity(0.7).next_to(extra_tick_p3, DOWN, buff = 0.2)



        self.camera.frame.scale(1.4).move_to(axes_2.coords_to_point(11,0,0))

        '''self.add(axes_2, x_axes_2_label, y_axes_2_label, sin_graph_0, cos_graph_0,
                 tick_x1, tick_x1_label,
                 tick_x2, tick_x2_label,
                 tick_x3, tick_x3_label,
                 tick_x4, tick_x4_label,
                 extra_tick_p1, extra_tick_p1_label,
                 extra_tick_p2, extra_tick_p2_label,
                 extra_tick_p3, extra_tick_p3_label)'''
        

        self.play(FadeIn(axes_2, x_axes_2_label, y_axes_2_label,
                 tick_x1, tick_x1_label,
                 tick_x2, tick_x2_label,
                 tick_x3, tick_x3_label,
                 tick_x4, tick_x4_label,
                 extra_tick_p1, extra_tick_p1_label,
                 extra_tick_p2, extra_tick_p2_label,
                 extra_tick_p3, extra_tick_p3_label))
        self.wait(2)
        self.play(LaggedStart(Create(sin_graph_0), Create(cos_graph_0), lag_ratio=1))
        self.wait(2)



        # Os gráficos não estão alinhados horizontalmente
        self.play(cos_graph_0.animate.shift(RIGHT*1.75))
        self.play(cos_graph_0.animate.shift(LEFT*1.75))
        self.wait(2)



# Comentário sobre os gráficos de seno e cosseno terem o mesmo formato
class vid13(MovingCameraScene):
    def construct(self):

        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-4, 4, 1],
                    x_length = 8,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)

        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.5, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))

        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)

        cos_dot = always_redraw(lambda: Dot((dot.get_x(),0,0), color=GREEN).set_z_index(3).scale(1))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))

        sin_dot = always_redraw(lambda: Dot((0,dot.get_y(),0), color=BLUE).set_z_index(3).scale(1))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))

        path = VMobject(color=WHITE)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        self.camera.frame.scale(1.3).move_to(axes.coords_to_point(0,0,0))

        self.add(axes, circ, dot, labeled_line, sin_axis_label, cos_axis_label, path,
                 cos_dot, cos_dashed_line, cos_line,
                 sin_dot, sin_dashed_line, sin_line)
        
        self.play(Rotate(dot, 3*360*DEGREES, about_point=axes.c2p(0,0,0)), rate_func=linear, run_time=20)
        self.wait(2)

        self.play(Rotate(dot, 90*DEGREES, about_point=axes.c2p(0,0,0)), run_time=3)
        self.wait(2)
        self.play(Rotate(dot, 90*DEGREES, about_point=axes.c2p(0,0,0)), run_time=3)
        self.wait(2)
        self.play(Rotate(dot, 90*DEGREES, about_point=axes.c2p(0,0,0)), run_time=3)
        self.wait(2)
        self.play(Rotate(dot, 90*DEGREES, about_point=axes.c2p(0,0,0)), run_time=3)
        self.wait(2)



# O seno está atrasado em relação ao cosseno
class vid14(MovingCameraScene):
    def construct(self):

        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-4, 4, 1],
                    x_length = 8,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)

        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.5, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))

        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)

        cos_dot = always_redraw(lambda: Dot((dot.get_x(),0,0), color=GREEN).set_z_index(3).scale(1))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))

        sin_dot = always_redraw(lambda: Dot((0,dot.get_y(),0), color=BLUE).set_z_index(3).scale(1))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))

        path = VMobject(color=WHITE)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        self.camera.frame.scale(1.3).move_to(axes.coords_to_point(0,0,0))

        self.add(axes, circ, dot, labeled_line, sin_axis_label, cos_axis_label, path,
                 cos_dot, cos_dashed_line, cos_line,
                 sin_dot, sin_dashed_line, sin_line)
        
        #self.play(FadeIn())

        self.play(Rotate(dot, 3*360*DEGREES, about_point=axes.c2p(0,0,0)), rate_func=linear, run_time=20)
        self.wait(2)



# No círculo trigonométrico o arco é igual ao ângulo
class vid15(MovingCameraScene):

    def angle_between(self, v1, v2):    # Calcula o ângulo entre dois vetores em graus
        cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.degrees(np.arccos(cos_theta))
    
    def construct(self):
        
        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-4, 4, 1],
                    x_length = 8,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)

        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.5, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)
        dot.rotate(30*DEGREES, about_point=axes.c2p(0,0,0))

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))
        radius_1 = MathTex('1').scale(0.9).move_to(labeled_line).set_z_index(15)
        radius_1_copy = radius_1.copy()

        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)

        cos_dot = always_redraw(lambda: Dot((dot.get_x(),0,0), color=GREEN).set_z_index(3).scale(1))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))

        sin_dot = always_redraw(lambda: Dot((0,dot.get_y(),0), color=BLUE).set_z_index(3).scale(1))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))

        path = VMobject(color=WHITE)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        self.camera.frame.scale(1.3).move_to(axes.coords_to_point(0,0,0))

        self.add(axes, circ, dot, labeled_line, radius_1)
        #         cos_axis_label, cos_dot, cos_dashed_line, cos_line,
        #         sin_axis_label, sin_dot, sin_dashed_line, sin_line)
        


        #angle_1 = Angle(cos_line, labeled_line, color=PURPLE, radius=0.35, stroke_width=50).set_z_index(-2)
        angle_1 = always_redraw(lambda: Angle.from_three_points(dot.get_center(), axes.c2p(0,0,0), axes.c2p(3,0,0), radius=0.3, stroke_width=50, color=PURPLE, other_angle=True).set_z_index(-2))        
        angle_1_label = MathTex('x', color=PURPLE).scale(0.9).next_to(angle_1, RIGHT, buff=0).shift(RIGHT*0.3+UP*0.1)

        self.play(FadeIn(angle_1, angle_1_label))
        self.wait(2)



        arc = Arc(angle=30*DEGREES, radius=3, stroke_width=7, color=PURPLE)
        arc_brace = ArcBrace(arc, RIGHT, buff=0.1, color=GRAY)
        arc_label = MathTex('x \cdot R').next_to(arc_brace, RIGHT).shift(UP*0.2+LEFT*0.1)
        arc_label[0][0].set_color(PURPLE)

        self.play(LaggedStart(Create(arc), FadeIn(arc_brace), lag_ratio=0.3))
        self.wait(2)
        self.play(FadeIn(arc_label))
        self.wait(2)



        arc_label2 = MathTex('x \cdot 1').move_to(arc_label, aligned_edge=LEFT)
        arc_label2[0][0].set_color(PURPLE)

        self.play(FadeOut(arc_label[0][2]),
                  ClockwiseTransform(radius_1_copy, arc_label2[0][2]))
        self.wait(2)
        self.play(FadeOut(arc_label[0][1], radius_1_copy))
        self.wait(2)



        # Tanto faz medir o ângulo como a abertura ou como o arco
        self.remove(radius_1)

        arrow_1 = Arrow(DOWN, UP, color=YELLOW).rotate(45*DEGREES).shift(DOWN*0.8+RIGHT*1.1).scale(0.9)
        arrow_2 = arrow_1.copy().shift(UP*0.9+RIGHT*2.6)


        self.play(FadeOut(arc, arc_brace, arc_label[0][0]))
        arc.set_color(YELLOW)

        angle_1_label.save_state()
        self.play(Rotate(dot, -29.9*DEGREES, about_point=axes.c2p(0,0,0)),
                  angle_1_label.animate.scale(0),
                  run_time=3)
        self.wait(2)
        self.play(Rotate(dot, 29.9*DEGREES, about_point=axes.c2p(0,0,0)),
                  FadeIn(arrow_1),
                  Restore(angle_1_label),
                  run_time=3)
        
        #angle_a_copy = angle_a.copy()
        #self.remove(angle_a).add(angle_a_copy)
        #self.play(angle_a_copy.animate.set_color(PURPLE))
        self.wait(2)
        self.play(LaggedStart(Create(arc), FadeIn(arc_label[0][0]),
                              lag_ratio=0.3),
                  ReplacementTransform(arrow_1, arrow_2),
                  run_time=2)
        self.play(arc.animate.set_color(PURPLE))
        self.wait(2)


# A tangente no círculo trigonométrico
class vid16(MovingCameraScene):
    def construct(self):

        # Retomando o círculo
        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-4, 4, 1],
                    x_length = 8,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)

        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.5, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)
        dot.rotate(40*DEGREES, about_point=axes.c2p(0,0,0))
        arc_40 = Arc(angle=40*DEGREES, radius=3, color=WHITE)
        arc_40_label = MathTex('x').scale(0.9).next_to(arc_40, LEFT, buff=0).shift(RIGHT*0.35+DOWN*0.1)

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))
        radius_1 = MathTex('1').scale(0.9).move_to(labeled_line).set_z_index(15)

        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)

        cos_dot = always_redraw(lambda: Dot((dot.get_x(),0,0), color=GREEN).set_z_index(3).scale(1))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))

        sin_dot = always_redraw(lambda: Dot((0,dot.get_y(),0), color=BLUE).set_z_index(3).scale(1))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))

        path = VMobject(color=WHITE)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        self.camera.frame.scale(1.3).move_to(axes.coords_to_point(0,0,0))

        self.add(axes, circ, dot, labeled_line, radius_1, arc_40, arc_40_label,
                 cos_axis_label, cos_dot, cos_dashed_line, cos_line,
                 sin_axis_label, sin_dot, sin_dashed_line, sin_line)
        


        # Traçando o eixo das tangentes
        tg_axis = axes.get_y_axis().copy().move_to(axes.c2p(3,0,0))
        tg_axis_label = MathTex(r'\text{tg}', color=RED).scale(0.9).next_to(tg_axis, LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)

        self.play(FadeIn(tg_axis, tg_axis_label, shift=LEFT), run_time=2)
        self.wait(2)



        # Prolongando o raio do círculo
        tg_dot = always_redraw(lambda: Dot(tg_axis.number_to_point(3*0.839), color=RED).set_z_index(3).scale(1))
        tg_line = always_redraw(lambda: Line(axes.coords_to_point(3,0,0), tg_dot.get_center(), stroke_width=6, color=RED).set_z_index(3))
        tg_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), tg_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        tg_dot_aux = tg_dot.copy().set_color(YELLOW)
        tg_line_aux = tg_line.copy().set_color(YELLOW)
        tg_dashed_line_aux = tg_dashed_line.copy().set_color(YELLOW)
        
        self.play(Create(tg_dashed_line_aux))
        self.play(tg_dashed_line_aux.animate.set_color(GRAY))
        self.remove(tg_dashed_line_aux).add(tg_dashed_line)
        self.wait(2)
        self.play(LaggedStart(Create(tg_line_aux),
                              GrowFromCenter(tg_dot_aux),
                              lag_ratio=0.3))
        self.play(tg_line_aux.animate.set_color(RED),
                  tg_dot_aux.animate.set_color(RED),
                  run_time=2)
        self.remove(tg_line_aux, tg_dot_aux).add(tg_line, tg_dot)
        self.wait(2)



        tg_brace = Brace(tg_line_aux, RIGHT, color=GRAY)
        tg_brace_label = MathTex(r'\text{tg}(x)', color=RED).next_to(tg_brace, RIGHT)

        self.play(FadeIn(tg_brace, tg_brace_label))
        self.wait(2)
        self.play(FadeOut(tg_brace, tg_brace_label))
        self.wait(2)



        # Mostrando porque aquele tamanho é a tangente de 'x'
        black_sq1 = Square(color=BLACK).set_opacity(0.8).scale(10).set_z_index(15)

        angle_x = Angle.from_three_points(axes.c2p(3,3*0.839,0), axes.c2p(0,0,0), axes.c2p(3,0,0), radius=0.3, stroke_width=50, color=WHITE, other_angle=True).set_z_index(16)
        angle_x_label = MathTex('x').scale(0.9).next_to(angle_x, RIGHT, buff=0).shift(RIGHT*0.3+UP*0.15).set_z_index(16)

        triangle_1 = Polygon(axes.c2p(0,0,0), axes.c2p(3,3*0.839,0), axes.c2p(3,0,0), color=YELLOW).set_z_index(17)
        
        self.play(LaggedStart(FadeIn(black_sq1),
                              DrawBorderThenFill(triangle_1),
                              FadeIn(angle_x, angle_x_label), 
                              lag_ratio=0.3),
                  run_time=3)
        self.wait(2)



        brace_1 = tg_brace.copy().set_z_index(16)
        brace_1_label = MathTex(r'?', color=RED).next_to(brace_1, RIGHT).set_z_index(16)
        brace_1_label_2 = MathTex(r'\text{tg}(x)', color=RED).move_to(brace_1_label, aligned_edge=LEFT).set_z_index(16)

        brace_2 = Brace(Line(axes.c2p(0,0,0), axes.c2p(3,0,0)), DOWN, color=GRAY).set_z_index(16)
        brace_2_label = MathTex(r'R = 1').scale(0.9).next_to(brace_2, DOWN).set_z_index(16)

        t1 = MathTex(r'\text{tg}(x) = ',r' \frac{?}{1}').to_edge(RIGHT).shift(UP*3+RIGHT*0.5).set_z_index(16)
        t2 = MathTex(r'\text{tg}(x) = ',r' \: ?').move_to(t1, aligned_edge=LEFT).set_z_index(16)

        t1[1][2].set_color(RED)
        t2[1].set_color(RED)

        self.play(FadeIn(t1[0]))
        self.wait(2)
        self.play(FadeIn(t1[1][0:2], brace_1, brace_1_label))
        self.play(FadeIn(t1[1][2], brace_2, brace_2_label))
        self.wait(2)
        self.play(Circumscribe(brace_2_label), run_time=1.5)
        self.wait(2)
        self.play(ReplacementTransform(t1[1], t2[1]), ReplacementTransform(brace_1_label, brace_1_label_2))
        self.wait(2)
        self.play(LaggedStart(FadeOut(triangle_1, t1[0], t2[1], angle_x, angle_x_label,
                                      brace_1, brace_1_label_2, 
                                      brace_2, brace_2_label),
                              FadeOut(black_sq1),
                              lag_ratio=0.3))
        self.wait(2)



# Variando a tangente no círculo e adicionando os eixos do gráfico da tangente
class vid17(MovingCameraScene):
    def construct(self):

        # Retomando o círculo
        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-4, 4, 1],
                    x_length = 8,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        tg_axis = axes.get_y_axis().copy().move_to(axes.c2p(3,0,0))

        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.5, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)
        dot.rotate(40*DEGREES, about_point=axes.c2p(0,0,0))
        arc_40 = Arc(angle=40*DEGREES, radius=3, color=WHITE)

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))

        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)
        tg_axis_label = MathTex(r'\text{tg}', color=RED).scale(0.9).next_to(tg_axis, LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)

        cos_dot = always_redraw(lambda: Dot((dot.get_x(),0,0), color=GREEN).set_z_index(3).scale(1))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        sin_dot = always_redraw(lambda: Dot((0,dot.get_y(),0), color=BLUE).set_z_index(3).scale(1))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        tg_dot = always_redraw(lambda: Dot(tg_axis.number_to_point(3 * dot.get_y() / dot.get_x() if not np.isclose(dot.get_x(), 0) else 0), color=RED).set_z_index(3).scale(1))
        tg_line = always_redraw(lambda: Line(axes.coords_to_point(3,0,0), tg_dot.get_center(), stroke_width=6, color=RED).set_z_index(3))
        tg_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), tg_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        path = VMobject(color=WHITE)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        self.camera.frame.scale(1.3).move_to(axes.coords_to_point(0,0,0))

        self.add(axes, circ, dot, labeled_line, arc_40, path,
                 cos_axis_label, cos_dot, cos_dashed_line, cos_line,
                 sin_axis_label, sin_dot, sin_dashed_line, sin_line,
                 tg_axis, tg_axis_label, tg_dot, tg_dashed_line, tg_line)
              


        # Variando a tangente no círculo
        self.play(Rotate(dot, 360*DEGREES, about_point=axes.c2p(0,0,0)), func_rate=linear, run_time=10)
        self.play(FadeOut(path, arc_40))
        self.wait(2)



            # Adicionando um novo plano cartesiano
        axes_2 = Axes(x_range = [0, 3*8, 1],
                    y_range = [-4, 4, 1],
                    x_length = 3*4.5,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        axes_2.next_to(axes, RIGHT, buff=2)

        x_axes_2_label = MathTex('x', color=WHITE).next_to(axes_2.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)
        y_axes_2_label = MathTex(r'\text{tg}(x)', color=RED).scale(0.9).next_to(axes_2.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)

        tg_graph_1 = axes_2.plot(lambda x: 3*np.tan(x/3),
                         x_range=[0, 3*1.5], stroke_width = 7).set_color(YELLOW).set_z_index(-3)
        tg_graph_2 = axes_2.plot(lambda x: 3*np.tan(x/3),
                         x_range=[3*1.6, 3*3*1.05], stroke_width = 7).set_color(YELLOW).set_z_index(-3)
        tg_graph_3 = axes_2.plot(lambda x: 3*np.tan(x/3),
                         x_range=[3*3*1.05, 3*4.6], stroke_width = 7).set_color(YELLOW).set_z_index(-3)
        tg_graph_4 = axes_2.plot(lambda x: 3*np.tan(x/3),
                         x_range=[3*4.6, 3*3*2.5], stroke_width = 7).set_color(YELLOW).set_z_index(-3)
        extra_tg_graph_1 = tg_graph_4.copy().set_stroke(opacity=0.3).shift(LEFT*10.62).reverse_points()
        extra_tg_graph_2 = extra_tg_graph_1.copy().shift(LEFT*5.31)



        dot_tg_graph = Dot(color=RED).move_to(axes_2.c2p(0,0,0)).scale(1.25).set_z_index(5)
        dot_tg_graph_projection = always_redraw(lambda: Line(dot_tg_graph.get_center(), (dot_tg_graph.get_x(),0,0), stroke_width=6, color=RED).set_z_index(4))
        white_path = always_redraw(lambda: Line(axes_2.c2p(0,0,0), (dot_tg_graph.get_x(),0,0)).set_z_index(5))



        dot_tg_graph_path = VMobject(stroke_width=7, color=YELLOW).set_z_index(-2)
        dot_tg_graph_path.set_points_as_corners([dot_tg_graph.get_center(), dot_tg_graph.get_center()])        
        def update_path2(path):
            previous_path = path.copy().set_z_index(-2)
            previous_path.add_points_as_corners([dot_tg_graph.get_center()])
            path.become(previous_path)
        dot_tg_graph_path.add_updater(update_path2)



        tick_x1 = Line(LEFT*0.1, RIGHT*0.1, color=GRAY).scale(1.4).rotate(90*DEGREES).move_to(axes_2.coords_to_point(3*PI/2,0,0))
        tick_x2 = tick_x1.copy().move_to(axes_2.coords_to_point(3*PI,0,0))
        tick_x3 = tick_x1.copy().move_to(axes_2.coords_to_point(9*PI/2,0,0))
        tick_x4 = tick_x1.copy().move_to(axes_2.coords_to_point(6*PI,0,0))

        tick_x0_label = MathTex(r'0').scale(0.9).set_opacity(0.7).next_to(axes_2.c2p(0,0,0), LEFT, buff = 0.2)
        tick_x1_label = MathTex(r'\frac{\pi}{2}').scale(0.9).set_opacity(0.7).next_to(tick_x1, DOWN, buff = 0.2)
        tick_x2_label = MathTex(r'\pi').scale(0.9).set_opacity(0.7).next_to(tick_x2, DOWN, buff = 0.2)
        tick_x3_label = MathTex(r'\frac{3\pi}{2}').scale(0.9).set_opacity(0.7).next_to(tick_x3, DOWN, buff = 0.2)
        tick_x4_label = MathTex(r'2 \pi').scale(0.9).set_opacity(0.7).next_to(tick_x4, DOWN, buff = 0.2)
        
        tick_x1_label[0][0].scale(1.1)
        tick_x2_label[0][0].scale(1.1)
        tick_x3_label[0][1].scale(1.1)
        tick_x4_label[0][1].scale(1.1)

        g_axes_2 = VGroup(axes_2, x_axes_2_label, y_axes_2_label, tick_x0_label,
                          tick_x1, tick_x2, tick_x3, tick_x4,
                          tick_x1_label, tick_x2_label, tick_x3_label, tick_x4_label)



        # Adicionando marcação dos ângulos no círculo
        label_0 = MathTex(r'0').scale(0.9).next_to(axes.c2p(3,0,0), UR, buff=0.2)
        
        label_90 = MathTex(r'\pi/2').scale(0.9).next_to(axes.c2p(0,3,0), UR, buff=0.1)
        label_90[0][0].scale(1.1)

        label_180 = MathTex(r'\pi').scale(0.9).scale(1.1).next_to(axes.c2p(-3,0,0), UL, buff=0.2)
        
        label_270 = MathTex(r'3 \pi /2').scale(0.9).next_to(axes.c2p(0,-3,0), DR, buff=0.2)
        label_270[0][1].scale(1.1)

        label_360 = MathTex(r'2 \pi').scale(0.9).next_to(axes.c2p(3,0,0), DR, buff=0.2)
        label_360[0][1].scale(1.1)



        self.play(FadeIn(g_axes_2),
                  FadeIn(label_0, label_90, label_180, label_270, label_360),
                  FadeOut(sin_axis_label, sin_dashed_line, sin_line, sin_dot,
                          cos_axis_label, cos_dashed_line, cos_line, cos_dot),
                  self.camera.frame.animate.scale(1.4).move_to(axes.coords_to_point(8,0,0)),
                  run_time=2)
        self.wait(2)



# Variando a tangente no círculo / Gráfico da tangente
class vid18(MovingCameraScene):
    def construct(self):

        # Retomando o círculo
        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-4, 4, 1],
                    x_length = 8,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        tg_axis = axes.get_y_axis().copy().move_to(axes.c2p(3,0,0))

        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.5, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))

        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)
        tg_axis_label = MathTex(r'\text{tg}', color=RED).scale(0.9).next_to(tg_axis, LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)

        cos_dot = always_redraw(lambda: Dot((dot.get_x(),0,0), color=GREEN).set_z_index(3).scale(1))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        sin_dot = always_redraw(lambda: Dot((0,dot.get_y(),0), color=BLUE).set_z_index(3).scale(1))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        tg_dot = always_redraw(lambda: Dot(tg_axis.number_to_point(3 * dot.get_y() / dot.get_x() if not np.isclose(dot.get_x(), 0) else 0), color=RED).set_z_index(3).scale(1))
        tg_line = always_redraw(lambda: Line(axes.coords_to_point(3,0,0), tg_dot.get_center(), stroke_width=6, color=RED).set_z_index(3))
        tg_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), tg_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        '''path = VMobject(color=WHITE)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)'''

        path = TracedPath(dot.get_center, stroke_width=6, stroke_color=WHITE, stroke_opacity=1).set_z_index(3)

        self.camera.frame.scale(1.3).move_to(axes.coords_to_point(0,0,0))

        self.add(axes, circ, dot, labeled_line, path,
                 cos_axis_label, cos_dot, cos_dashed_line, cos_line,
                 sin_axis_label, sin_dot, sin_dashed_line, sin_line,
                 tg_axis, tg_axis_label, tg_dot, tg_dashed_line, tg_line)
              


        # Gráfico da tangente
            # Adicionando um novo plano cartesiano
        axes_2 = Axes(x_range = [0, 3*8, 1],
                    y_range = [-4, 4, 1],
                    x_length = 3*4.5,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        axes_2.next_to(axes, RIGHT, buff=2)

        x_axes_2_label = MathTex('x', color=WHITE).next_to(axes_2.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)
        y_axes_2_label = MathTex(r'\text{tg}(x)', color=RED).scale(0.9).next_to(axes_2.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)

        tg_graph_1 = axes_2.plot(lambda x: 3*np.tan(x/3),
                         x_range=[0, 3*1.5], stroke_width = 7).set_color(YELLOW).set_z_index(-3)
        tg_graph_2 = axes_2.plot(lambda x: 3*np.tan(x/3),
                         x_range=[3*1.6, 3*3*1.05], stroke_width = 7).set_color(YELLOW).set_z_index(-3)
        tg_graph_3 = axes_2.plot(lambda x: 3*np.tan(x/3),
                         x_range=[3*3*1.05, 3*4.6], stroke_width = 7).set_color(YELLOW).set_z_index(-3)
        tg_graph_4 = axes_2.plot(lambda x: 3*np.tan(x/3),
                         x_range=[3*4.6, 3*3*2.5], stroke_width = 7).set_color(YELLOW).set_z_index(-3)
        extra_tg_graph_1 = tg_graph_4.copy().set_stroke(opacity=0.3).shift(LEFT*10.62).reverse_points()
        extra_tg_graph_2 = extra_tg_graph_1.copy().shift(LEFT*5.31)



        dot_tg_graph = Dot(color=RED).move_to(axes_2.c2p(0,0,0)).scale(1.25).set_z_index(5)
        dot_tg_graph_projection = always_redraw(lambda: Line(dot_tg_graph.get_center(), (dot_tg_graph.get_x(),0,0), stroke_width=6, color=RED).set_z_index(4))
        white_path = always_redraw(lambda: Line(axes_2.c2p(0,0,0), (dot_tg_graph.get_x(),0,0)).set_z_index(5))



        '''dot_tg_graph_path = VMobject(stroke_width=7, color=YELLOW).set_z_index(-2)
        dot_tg_graph_path.set_points_as_corners([dot_tg_graph.get_center(), dot_tg_graph.get_center()])        
        def update_path2(path):
            previous_path = path.copy().set_z_index(-2)
            previous_path.add_points_as_corners([dot_tg_graph.get_center()])
            path.become(previous_path)
        dot_tg_graph_path.add_updater(update_path2)'''
        
        dot_tg_graph_path = TracedPath(dot_tg_graph.get_center, stroke_width=7, stroke_color=YELLOW, stroke_opacity=1).set_z_index(-2)



        tick_x1 = Line(LEFT*0.1, RIGHT*0.1, color=GRAY).scale(1.4).rotate(90*DEGREES).move_to(axes_2.coords_to_point(3*PI/2,0,0))
        tick_x2 = tick_x1.copy().move_to(axes_2.coords_to_point(3*PI,0,0))
        tick_x3 = tick_x1.copy().move_to(axes_2.coords_to_point(9*PI/2,0,0))
        tick_x4 = tick_x1.copy().move_to(axes_2.coords_to_point(6*PI,0,0))

        tick_x0_label = MathTex(r'0').scale(0.9).set_opacity(0.7).next_to(axes_2.c2p(0,0,0), LEFT, buff = 0.2)
        tick_x1_label = MathTex(r'\frac{\pi}{2}').scale(0.9).set_opacity(0.7).next_to(tick_x1, DOWN, buff = 0.2)
        tick_x2_label = MathTex(r'\pi').scale(0.9).set_opacity(0.7).next_to(tick_x2, DOWN, buff = 0.2)
        tick_x3_label = MathTex(r'\frac{3\pi}{2}').scale(0.9).set_opacity(0.7).next_to(tick_x3, DOWN, buff = 0.2)
        tick_x4_label = MathTex(r'2 \pi').scale(0.9).set_opacity(0.7).next_to(tick_x4, DOWN, buff = 0.2)
        
        tick_x1_label[0][0].scale(1.1)
        tick_x2_label[0][0].scale(1.1)
        tick_x3_label[0][1].scale(1.1)
        tick_x4_label[0][1].scale(1.1)

        g_axes_2 = VGroup(axes_2, x_axes_2_label, y_axes_2_label, tick_x0_label,
                          tick_x1, tick_x2, tick_x3, tick_x4,
                          tick_x1_label, tick_x2_label, tick_x3_label, tick_x4_label)



        # Adicionando marcação dos ângulos no círculo
        label_0 = MathTex(r'0').scale(0.9).next_to(axes.c2p(3,0,0), UR, buff=0.2)
        
        label_90 = MathTex(r'\pi/2').scale(0.9).next_to(axes.c2p(0,3,0), UR, buff=0.1)
        label_90[0][0].scale(1.1)

        label_180 = MathTex(r'\pi').scale(0.9).scale(1.1).next_to(axes.c2p(-3,0,0), UL, buff=0.2)
        
        label_270 = MathTex(r'3 \pi /2').scale(0.9).next_to(axes.c2p(0,-3,0), DR, buff=0.2)
        label_270[0][1].scale(1.1)

        label_360 = MathTex(r'2 \pi').scale(0.9).next_to(axes.c2p(3,0,0), DR, buff=0.2)
        label_360[0][1].scale(1.1)



        self.add(g_axes_2, label_0, label_90, label_180, label_270, label_360)
        self.remove(sin_axis_label, sin_dashed_line, sin_line, sin_dot,
                    cos_axis_label, cos_dashed_line, cos_line, cos_dot)
        self.camera.frame.scale(1.4).move_to(axes.coords_to_point(8,0,0))



        # Linhas pretas para disfarçar o erro no path da função quando o ponto vai de +\infty para -\infty
        black_l1 = Line(UP, DOWN, color=BLACK, stroke_width=30).scale(10).set_z_index(-1).move_to(axes_2.c2p(3*PI/2))
        black_l2 = black_l1.copy().move_to(axes_2.c2p(3*3*PI/2))
        black_l3 = black_l1.copy().move_to(axes_2.c2p(-3*PI/2))
        black_l4 = black_l1.copy().move_to(axes_2.c2p(-3*3*PI/2))
        self.add(black_l1, black_l2, black_l3, black_l4)


            # Desenhando o gráfico
        self.play(GrowFromCenter(dot_tg_graph), Flash(dot_tg_graph, num_lines=8))
        self.add(dot_tg_graph_projection, dot_tg_graph_path, white_path)
        self.wait(2)
        self.play(MoveAlongPath(dot_tg_graph, tg_graph_1),
                  run_time=5, rate_func=rush_into)
        self.play(dot_tg_graph.animate.move_to(axes_2.c2p(3*PI/2,20,0)), 
                  run_time=3, rate_func=rush_from)
        self.wait(2)
        self.play(MoveAlongPath(dot_tg_graph, tg_graph_2),
                  run_time=5)
        self.wait(2)
        self.play(MoveAlongPath(dot_tg_graph, tg_graph_3),
                  run_time=5)
        self.wait(2)
        self.play(MoveAlongPath(dot_tg_graph, tg_graph_4), run_time=10)
        self.play(FadeIn(extra_tg_graph_1, extra_tg_graph_2))
        self.wait(2)



            # Girando o ponto no círculo
        self.play(Rotate(dot, 89*DEGREES, about_point=axes.c2p(0,0,0)), func_rate=linear, run_time=5)
        self.play(dot.animate.move_to(axes.c2p(0.05,2.99,0)))
        self.wait(2)
        self.play(dot.animate.move_to(axes.c2p(-0.05,2.99,0)))
        self.play(Rotate(dot, 89*DEGREES, about_point=axes.c2p(0,0,0)), func_rate=linear, run_time=5)
        self.wait(2)
        self.play(Rotate(dot, 180*DEGREES, about_point=axes.c2p(0,0,0)), func_rate=linear, run_time=10)
        self.wait(2)

        self.play(Rotate(dot, 225*DEGREES, about_point=axes.c2p(0,0,0)), func_rate=linear, run_time=4)
        self.wait(2)
        self.play(Rotate(dot, 135*DEGREES, about_point=axes.c2p(0,0,0)), func_rate=linear, run_time=4)
        self.wait(2)
        




# Comentário sobre as assíntotas do gráfico da tangente
class vid19(MovingCameraScene):
    def construct(self):

        # Retomando o círculo
        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-4, 4, 1],
                    x_length = 8,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        tg_axis = axes.get_y_axis().copy().move_to(axes.c2p(3,0,0))

        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.5, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))

        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)
        tg_axis_label = MathTex(r'\text{tg}', color=RED).scale(0.9).next_to(tg_axis, LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)

        cos_dot = always_redraw(lambda: Dot((dot.get_x(),0,0), color=GREEN).set_z_index(3).scale(1))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        sin_dot = always_redraw(lambda: Dot((0,dot.get_y(),0), color=BLUE).set_z_index(3).scale(1))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        tg_dot = always_redraw(lambda: Dot(tg_axis.number_to_point(3 * dot.get_y() / dot.get_x() if not np.isclose(dot.get_x(), 0) else 0), color=RED).set_z_index(3).scale(1))
        tg_line = always_redraw(lambda: Line(axes.coords_to_point(3,0,0), tg_dot.get_center(), stroke_width=6, color=RED).set_z_index(3))
        tg_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), tg_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        path = VMobject(color=WHITE)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        self.camera.frame.scale(1.3).move_to(axes.coords_to_point(0,0,0))

        self.add(axes, circ, dot, labeled_line, path,
                 cos_axis_label, cos_dot, cos_dashed_line, cos_line,
                 sin_axis_label, sin_dot, sin_dashed_line, sin_line,
                 tg_axis, tg_axis_label, tg_dot, tg_dashed_line, tg_line)
              


        # Gráfico da tangente
            # Adicionando um novo plano cartesiano
        axes_2 = Axes(x_range = [0, 3*8, 1],
                    y_range = [-4, 4, 1],
                    x_length = 3*4.5,
                    y_length = 8,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        axes_2.next_to(axes, RIGHT, buff=2)

        x_axes_2_label = MathTex('x', color=WHITE).next_to(axes_2.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)
        y_axes_2_label = MathTex(r'\text{tg}(x)', color=RED).scale(0.9).next_to(axes_2.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)

        tg_graph_1 = axes_2.plot(lambda x: 3*np.tan(x/3),
                         x_range=[0, 3*1.5], stroke_width = 7).set_color(YELLOW).set_z_index(-3)
        tg_graph_2 = axes_2.plot(lambda x: 3*np.tan(x/3),
                         x_range=[3*1.6, 3*3*1.05], stroke_width = 7).set_color(YELLOW).set_z_index(-3)
        tg_graph_3 = axes_2.plot(lambda x: 3*np.tan(x/3),
                         x_range=[3*3*1.05, 3*4.6], stroke_width = 7).set_color(YELLOW).set_z_index(-3)
        tg_graph_4 = axes_2.plot(lambda x: 3*np.tan(x/3),
                         x_range=[3*4.8, 3*3*2.5], stroke_width = 7).set_color(YELLOW).set_z_index(-3)
        extra_tg_graph_1 = tg_graph_4.copy().set_stroke(opacity=0.3).shift(LEFT*10.62).reverse_points()
        extra_tg_graph_2 = extra_tg_graph_1.copy().shift(LEFT*5.31)



        dot_tg_graph = Dot(color=RED).move_to(axes_2.c2p(0,0,0)).scale(1.25).set_z_index(5)
        dot_tg_graph_projection = always_redraw(lambda: Line(dot_tg_graph.get_center(), (dot_tg_graph.get_x(),0,0), stroke_width=6, color=RED).set_z_index(4))
        white_path = always_redraw(lambda: Line(axes_2.c2p(0,0,0), (dot_tg_graph.get_x(),0,0)).set_z_index(5))



        dot_tg_graph_path = VMobject(stroke_width=7, color=YELLOW).set_z_index(-2)
        dot_tg_graph_path.set_points_as_corners([dot_tg_graph.get_center(), dot_tg_graph.get_center()])        
        def update_path2(path):
            previous_path = path.copy().set_z_index(-2)
            previous_path.add_points_as_corners([dot_tg_graph.get_center()])
            path.become(previous_path)
        dot_tg_graph_path.add_updater(update_path2)



        tick_x1 = Line(LEFT*0.1, RIGHT*0.1, color=GRAY).scale(1.4).rotate(90*DEGREES).move_to(axes_2.coords_to_point(3*PI/2,0,0))
        tick_x2 = tick_x1.copy().move_to(axes_2.coords_to_point(3*PI,0,0))
        tick_x3 = tick_x1.copy().move_to(axes_2.coords_to_point(9*PI/2,0,0))
        tick_x4 = tick_x1.copy().move_to(axes_2.coords_to_point(6*PI,0,0))

        tick_x0_label = MathTex(r'0').scale(0.9).set_opacity(0.7).next_to(axes_2.c2p(0,0,0), LEFT, buff = 0.2)
        tick_x1_label = MathTex(r'\frac{\pi}{2}').scale(0.9).set_opacity(0.7).next_to(tick_x1, DOWN, buff = 0.2).set_z_index(3)
        tick_x2_label = MathTex(r'\pi').scale(0.9).set_opacity(0.7).next_to(tick_x2, DOWN, buff = 0.2)
        tick_x3_label = MathTex(r'\frac{3\pi}{2}').scale(0.9).set_opacity(0.7).next_to(tick_x3, DOWN, buff = 0.2).set_z_index(3)
        tick_x4_label = MathTex(r'2 \pi').scale(0.9).set_opacity(0.7).next_to(tick_x4, DOWN, buff = 0.2)
        
        tick_x1_label[0][0].scale(1.1)
        tick_x2_label[0][0].scale(1.1)
        tick_x3_label[0][1].scale(1.1)
        tick_x4_label[0][1].scale(1.1)

        g_axes_2 = VGroup(axes_2, x_axes_2_label, y_axes_2_label, tick_x0_label,
                          tick_x1, tick_x2, tick_x3, tick_x4,
                          tick_x1_label, tick_x2_label, tick_x3_label, tick_x4_label)



        # Adicionando marcação dos ângulos no círculo
        label_0 = MathTex(r'0').scale(0.9).next_to(axes.c2p(3,0,0), UR, buff=0.2)
        
        label_90 = MathTex(r'\pi/2').scale(0.9).next_to(axes.c2p(0,3,0), UR, buff=0.1)
        label_90[0][0].scale(1.1)

        label_180 = MathTex(r'\pi').scale(0.9).scale(1.1).next_to(axes.c2p(-3,0,0), UL, buff=0.2)
        
        label_270 = MathTex(r'3 \pi /2').scale(0.9).next_to(axes.c2p(0,-3,0), DR, buff=0.2)
        label_270[0][1].scale(1.1)

        label_360 = MathTex(r'2 \pi').scale(0.9).next_to(axes.c2p(3,0,0), DR, buff=0.2)
        label_360[0][1].scale(1.1)



        self.add(g_axes_2, label_0, label_90, label_180, label_270, label_360)
        self.remove(sin_axis_label, sin_dashed_line, sin_line, sin_dot,
                    cos_axis_label, cos_dashed_line, cos_line, cos_dot)
        self.camera.frame.scale(1.4).move_to(axes.coords_to_point(8,0,0))



        g = VGroup(tg_graph_1, tg_graph_2, tg_graph_3, tg_graph_4)

        self.add(g, extra_tg_graph_1, extra_tg_graph_2)
        self.play(g.animate.set_color(RED),
                  FadeOut(extra_tg_graph_1, extra_tg_graph_2))
        self.wait(2)



        # tg = sen/cos
        t = MathTex(r'\text{tg}(x) = ',r' \frac{\text{sen}(x)}{\text{cos}(x)}').scale(1.4).shift(RIGHT*11.5+UP*3).set_z_index(1)
        t2 = MathTex(r'\text{tg}(x) = ',r' \frac{\text{sen}(x)}{0}').scale(1.4).move_to(t, aligned_edge=UL).set_z_index(1)
        t_aux = t.copy()
        t_bg = SurroundingRectangle(t_aux, color=BLACK, stroke_width=0).set_opacity(0.7).set_z_index(0)
        
        self.play(FadeIn(t[0]))
        self.wait(2)
        self.play(FadeIn(t[1]), FadeIn(t_bg))
        self.wait(2)
        self.play(ReplacementTransform(t[1][7:], t2[1][7]))

        red_line1 = Line(UP*0.2, DOWN*0.2, color=RED, stroke_width=8).scale(8).rotate(50*DEGREES).move_to(t2).shift(RIGHT*1.2)
        red_line2 = red_line1.copy().rotate(80*DEGREES).reverse_points()
        self.play(LaggedStart(Create(red_line1), Create(red_line2), lag_ratio=0.5))
        self.wait(2)



        tick_x1_label_bg = SurroundingRectangle(tick_x1_label, color=BLACK, stroke_width=0).set_opacity(0.7).set_z_index(1)
        tick_x3_label_bg = SurroundingRectangle(tick_x3_label, color=BLACK, stroke_width=0).set_opacity(0.7).set_z_index(1)
        self.add(tick_x1_label_bg, tick_x3_label_bg)



        asymptote_line1 = DashedLine(DOWN*5, UP*5, color=GRAY).scale(2.5).move_to(axes_2.c2p(3*PI/2))
        asymptote_line2 = asymptote_line1.copy().move_to(axes_2.c2p(3*3*PI/2))
        self.play(LaggedStart(FadeIn(asymptote_line1), 
                              FadeIn(asymptote_line2),
                              lag_ratio=0.3),
                  LaggedStart(Flash(tick_x1_label, num_lines=8, line_stroke_width=6, flash_radius=0.4, line_length=0.6), 
                              Flash(tick_x3_label, num_lines=8, line_stroke_width=6, flash_radius=0.4, line_length=0.6), 
                              lag_ratio=0.3))
        self.wait(2)




# Cossecante, secante e cotangente no círculo trigonométrico
class vid20(MovingCameraScene):
    def construct(self):

        # Retomando o círculo
        axes = Axes(x_range = [-5, 5, 1],
                    y_range = [-5, 5, 1],
                    x_length = 10,
                    y_length = 10,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        tg_axis = axes.get_y_axis().copy().move_to(axes.c2p(3,0,0))

        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.5, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)
        dot.rotate(40*DEGREES, about_point=axes.c2p(0,0,0))
        arc_40 = Arc(angle=40*DEGREES, radius=3, color=WHITE)
        arc_40_label = MathTex('x').scale(0.9).next_to(arc_40, LEFT, buff=0).shift(RIGHT*0.35+DOWN*0.1)

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))

        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)
        tg_axis_label = MathTex(r'\text{tg}', color=RED).scale(0.9).next_to(tg_axis, LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)

        cos_dot = always_redraw(lambda: Dot((dot.get_x(),0,0), color=GREEN).set_z_index(3).scale(1))
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        sin_dot = always_redraw(lambda: Dot((0,dot.get_y(),0), color=BLUE).set_z_index(3).scale(1))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        tg_dot = always_redraw(lambda: Dot(tg_axis.number_to_point(3 * dot.get_y() / dot.get_x() if not np.isclose(dot.get_x(), 0) else 0), color=RED).set_z_index(3).scale(1))
        tg_line = always_redraw(lambda: Line(axes.coords_to_point(3,0,0), tg_dot.get_center(), stroke_width=6, color=RED).set_z_index(3))
        tg_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), tg_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        path = VMobject(color=WHITE)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        #self.camera.frame.scale(1.5).move_to(axes.coords_to_point(0,0,0))



        t_cossec = MathTex(r'\text{cossec}(x)', color=WHITE)
        t_sec = MathTex(r'\text{sec}(x)', color=WHITE)
        t_cotg = MathTex(r'\text{cotg}(x)', color=WHITE)
        g1 = VGroup(t_cossec, t_sec, t_cotg).arrange(DOWN, buff=1).move_to(axes.coords_to_point(0,0,0))

        self.play(FadeIn(t_cossec))
        self.play(FadeIn(t_sec))
        self.play(FadeIn(t_cotg))
        self.wait(2)
        self.play(FadeOut(t_cossec, t_sec, t_cotg))
        self.wait(2)



        self.play(FadeIn(axes, circ, dot, labeled_line, arc_40, path, arc_40_label,
                 cos_axis_label, cos_dot, cos_dashed_line, cos_line,
                 sin_axis_label, sin_dot, sin_dashed_line, sin_line,
                 tg_axis, tg_axis_label, tg_dot, tg_dashed_line, tg_line))
        self.wait(2)



        # Cotangente
            # Adicionando o eixo
        cotg_axis = axes.get_x_axis().copy().move_to(axes.c2p(0,3,0))
        cotg_axis_label = MathTex(r'\text{cotg}', color=MAROON).scale(0.9).next_to(cotg_axis, RIGHT, buff=-0.1).shift(DOWN*0.4)
        g_cotg_axis = VGroup(cotg_axis, cotg_axis_label)
        '''self.play(FadeIn(g_cotg_axis, shift=DOWN))
        self.wait(2)'''


        
        cotg_dot = always_redraw(lambda: Dot(cotg_axis.number_to_point(3 * dot.get_x() / dot.get_y() if not np.isclose(dot.get_y(), 0) else 0), color=MAROON).set_z_index(3).scale(1))
        cotg_line = always_redraw(lambda: Line(axes.coords_to_point(0,3,0), cotg_dot.get_center(), stroke_width=6, color=MAROON).set_z_index(3))
        cotg_dashed_line = always_redraw(lambda: DashedLine(tg_dot.get_center(), cotg_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))



            # Prolongando o raio
        cotg_brace = Brace(Line(axes.c2p(0,3,0), cotg_dot), UP, color=GRAY)
        cotg_brace_label = MathTex(r'\text{cotg}(x)').next_to(cotg_brace, UP, buff=0.1)

        self.play(Create(cotg_dashed_line))
        self.play(LaggedStart(Create(cotg_line), GrowFromCenter(cotg_dot), lag_ratio=0.3))
        self.play(FadeIn(cotg_brace, cotg_brace_label))
        self.wait(2)
        self.play(FadeOut(cotg_brace, cotg_brace_label))
        self.wait(2)


        self.add(axes, circ, dot, labeled_line, arc_40, path, arc_40_label,
                 cos_axis_label, cos_dot, cos_dashed_line, cos_line,
                 sin_axis_label, sin_dot, sin_dashed_line, sin_line,
                 tg_axis, tg_axis_label, tg_dot, tg_dashed_line, tg_line,
                 cotg_axis, cotg_axis_label, cotg_line, cotg_dashed_line, cotg_dot)
        self.wait(2)

        black_sq1 = Square(color=BLACK).set_opacity(0.6).scale(10).set_z_index(10)
        self.play(FadeIn(black_sq1))
    
        # Secante
        sec_line = Line(axes.coords_to_point(0,0,0), tg_dot.get_center(), stroke_width=6, color=YELLOW).set_z_index(5).set_z_index(11)
        
        sec_brace = Brace(sec_line, UL, buff=0.1, color=GRAY).rotate(-5*DEGREES).set_z_index(11)
        sec_brace_label = MathTex(r'\text{sec}(x)').move_to(sec_brace).rotate(40*DEGREES).shift(UP*0.5+LEFT*0.5).set_z_index(11)

        self.play(Create(sec_line), run_time=3)
        self.play(FadeIn(sec_brace, sec_brace_label))
        self.wait(2)
        self.play(FadeOut(sec_line, sec_brace, sec_brace_label))
        self.wait(2)



        # Cossecante
        cossec_line = Line(axes.coords_to_point(0,0,0), cotg_dot.get_center(), stroke_width=6, color=YELLOW).set_z_index(11)
        
        cossec_brace = Brace(cossec_line, DR, buff=0.1, color=GRAY).rotate(-5*DEGREES).set_z_index(11)
        cossec_brace_label = MathTex(r'\text{cossec}(x)').move_to(cossec_brace).rotate(40*DEGREES).shift(DOWN*0.5+RIGHT*0.5).set_z_index(11)

        self.play(Create(cossec_line), run_time=3)
        self.play(FadeIn(cossec_brace, cossec_brace_label))
        self.wait(2)
        self.play(FadeOut(cossec_line, cossec_brace, cossec_brace_label, black_sq1))
        self.wait(2)


        
        
# Transformando em outra configuração do círculo trigonométrico
class vid21(MovingCameraScene):
    def construct(self):

        # Configuração atual
        axes = Axes(x_range = [-5, 5, 1],
                    y_range = [-5, 5, 1],
                    x_length = 10,
                    y_length = 10,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)
        tg_axis = axes.get_y_axis().copy().move_to(axes.c2p(3,0,0))
        cotg_axis = axes.get_x_axis().copy().move_to(axes.c2p(0,3,0))
        
        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.5, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)
        dot.rotate(40*DEGREES, about_point=axes.c2p(0,0,0))
        arc_40 = Arc(angle=40*DEGREES, radius=3, color=WHITE)
        arc_40_label = MathTex('x').scale(0.9).next_to(arc_40, LEFT, buff=0).shift(RIGHT*0.35+DOWN*0.1)

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))

        sin_axis_label = MathTex(r'\text{sen}', color=BLUE).scale(0.9).next_to(axes.get_y_axis(), LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cos_axis_label = MathTex(r'\text{cos}', color=GREEN).scale(0.9).next_to(axes.get_x_axis(), RIGHT, buff=-0.1).shift(DOWN*0.4)
        tg_axis_label = MathTex(r'\text{tg}', color=RED).scale(0.9).next_to(tg_axis, LEFT, buff=0.2, aligned_edge=UP).shift(UP*0.2+RIGHT*0.1)
        cotg_axis_label = MathTex(r'\text{cotg}', color=MAROON).scale(0.9).next_to(cotg_axis, RIGHT, buff=-0.1).shift(DOWN*0.4)

        cos_dot = Dot((dot.get_x(),0,0), color=GREEN).set_z_index(3).scale(1)
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,cos_dot.get_y(),0), cos_dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))
        cos_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), cos_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        sin_dot = Dot((0,dot.get_y(),0), color=BLUE).set_z_index(3).scale(1)
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(sin_dot.get_x(),0,0), sin_dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))
        sin_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), sin_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        tg_dot = Dot(tg_axis.number_to_point(3 * dot.get_y() / dot.get_x() if not np.isclose(dot.get_x(), 0) else 0), color=RED).set_z_index(3).scale(1)
        tg_dot_aux = Dot(axes.coords_to_point(3,0,0)).scale(0)
        tg_line = Line(tg_dot_aux.get_center(), tg_dot.get_center(), stroke_width=6, color=RED).set_z_index(3)
        tg_line2 = Line(axes.get_x_axis().number_to_point(9/(dot.get_x())), dot.get_center(), stroke_width=6, color=RED).set_z_index(3)
        tg_dashed_line = always_redraw(lambda: DashedLine(dot.get_center(), tg_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))

        cotg_dot = Dot(cotg_axis.number_to_point(3 * dot.get_x() / dot.get_y() if not np.isclose(dot.get_y(), 0) else 0), color=MAROON).set_z_index(3).scale(1)
        cotg_dot_aux = Dot(axes.coords_to_point(0,3,0)).scale(0)
        cotg_line = Line(cotg_dot_aux.get_center(), cotg_dot.get_center(), stroke_width=6, color=MAROON).set_z_index(3)
        cotg_line2 = Line(axes.get_y_axis().number_to_point(9/(dot.get_y())), dot.get_center(), stroke_width=6, color=MAROON).set_z_index(3)
        cotg_dashed_line = always_redraw(lambda: DashedLine(tg_dot.get_center(), cotg_dot.get_center(), color=GRAY).set_opacity(0.5).set_z_index(3))



        self.camera.frame.scale(1.4).move_to(axes.coords_to_point(0,0,0))

        self.add(axes, circ, dot, labeled_line, arc_40, arc_40_label,
                 cos_axis_label, cos_dot, cos_dashed_line, cos_line,
                 sin_axis_label, sin_dot, sin_dashed_line, sin_line,
                 tg_axis, tg_axis_label, tg_dot, tg_dashed_line, tg_line,
                 cotg_axis, cotg_axis_label, cotg_dot, cotg_dashed_line, cotg_line)

        # Transformando na nova configuração
            # Seno e cosseno
        sin_label = MathTex(r'\text{sen}(x)', color=BLUE).rotate(90*DEGREES).scale(0.9*abs(dot.get_y()) / 3).next_to(sin_line, LEFT, buff=0.1).shift(RIGHT*dot.get_x())
        cos_label = MathTex(r'\text{cos}(x)', color=GREEN).scale(0.9*abs(dot.get_x()) / 3).next_to(cos_line, DOWN, buff=0.1).shift(UP*dot.get_y())
        self.play(LaggedStart(sin_dot.animate.move_to(dot), FadeIn(sin_label), 
                              cos_dot.animate.move_to(dot), FadeIn(cos_label),
                              lag_ratio=0.5))

            # Tangente e cotangente
        tg_line3 = always_redraw(lambda: LabeledLine(start=axes.get_x_axis().number_to_point(9/(dot.get_x())), end=dot.get_center(), label=r'\text{tg}(x)', frame_fill_opacity=0.8, font_size=30, label_position=0.3, label_color=RED, label_frame=False, stroke_width=6, color=RED).set_z_index(3))
        cotg_line3 = always_redraw(lambda: LabeledLine(start=axes.get_y_axis().number_to_point(9/(dot.get_y())), end=dot.get_center(), label=r'\text{cotg}(x)', frame_fill_opacity=0.8, font_size=30, label_position=0.3, label_color=MAROON, label_frame=False, stroke_width=6, color=MAROON).set_z_index(3))
        self.play(tg_dot.animate.move_to(dot),
                  ReplacementTransform(tg_line, tg_line2))
        self.play(FadeIn(tg_line3), FadeOut(tg_axis, tg_axis_label))
        self.remove(tg_dot, tg_line2)
        self.play(cotg_dot.animate.move_to(dot),
                  ReplacementTransform(cotg_line, cotg_line2))
        self.play(FadeIn(cotg_line3), FadeOut(cotg_axis, cotg_axis_label))
        self.remove(cotg_dot, cotg_line2)

            # Secante e cossecante
        sec_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), axes.get_x_axis().number_to_point(9/(dot.get_x())), stroke_width=6, color=PINK).set_z_index(3))
        cossec_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), axes.get_y_axis().number_to_point(9/(dot.get_y())), stroke_width=6, color=PURPLE).set_z_index(3))
        sec_label = always_redraw(lambda: MathTex(r'\text{sec}(x)', color=PINK).scale(0.7).next_to(sec_line, DOWN, buff=0.1))
        cossec_label = always_redraw(lambda: MathTex(r'\text{cossec}(x)', color=PURPLE).rotate(90*DEGREES).scale(0.7).next_to(cossec_line, LEFT, buff=0.1))

        self.play(LaggedStart(Create(sec_line), FadeIn(sec_label), lag_ratio=0.3))
        self.play(LaggedStart(Create(cossec_line), FadeIn(cossec_label), lag_ratio=0.3))
        self.wait(2)



# Variando a outra configuração do círculo trigonométrico
class vid22(MovingCameraScene):
    def construct(self):

        axes = Axes(x_range = [-5, 5, 1],
                    y_range = [-5, 5, 1],
                    x_length = 10,
                    y_length = 10,
                    axis_config = {"include_ticks" : False}).set_opacity(0.6)

        circ = Circle(radius=3, fill_opacity=0, stroke_opacity=0.5, color=WHITE).move_to(axes.coords_to_point(0,0,0))
        
        dot = Dot((3*1, 3*0.001, 0), color=WHITE).scale(1.25).set_z_index(4)
        dot.rotate(40*DEGREES, about_point=axes.c2p(0,0,0))
        arc_40 = Arc(angle=40*DEGREES, radius=3, color=WHITE)

        labeled_line = always_redraw(lambda: LabeledLine(start=axes.coords_to_point(0,0,0), end=dot.get_center(), label='1', font_size=40, label_frame=False).set_z_index(4))
        arc_label = always_redraw(lambda: MathTex('x').scale(0.9).move_to(labeled_line.copy().scale(1.25).get_end()))
                                  
        cos_line = always_redraw(lambda: Line(axes.coords_to_point(0,dot.get_y(),0), dot.get_center(), stroke_width=6, color=GREEN).set_z_index(3))
        sin_line = always_redraw(lambda: Line(axes.coords_to_point(dot.get_x(),0,0), dot.get_center(), stroke_width=6, color=BLUE).set_z_index(3))
        sec_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), axes.get_x_axis().number_to_point(9/(dot.get_x())), stroke_width=6, color=PINK).set_z_index(3))
        cossec_line = always_redraw(lambda: Line(axes.coords_to_point(0,0,0), axes.get_y_axis().number_to_point(9/(dot.get_y())), stroke_width=6, color=PURPLE).set_z_index(3))
        tg_line = always_redraw(lambda: LabeledLine(start=axes.get_x_axis().number_to_point(9/(dot.get_x())), end=dot.get_center(), label=r'\text{tg}(x)', frame_fill_opacity=0.8, font_size=30, label_position=0.3, label_color=RED, label_frame=False, stroke_width=6, color=RED).set_z_index(3))
        cotg_line = always_redraw(lambda: LabeledLine(start=axes.get_y_axis().number_to_point(9/(dot.get_y())), end=dot.get_center(), label=r'\text{cotg}(x)', frame_fill_opacity=0.8, font_size=30, label_position=0.3, label_color=MAROON, label_frame=False, stroke_width=6, color=MAROON).set_z_index(3))

        sin_label = always_redraw(lambda: MathTex(r'\text{sen}(x)', color=BLUE).rotate(90*DEGREES).scale(0.9*abs(dot.get_y()) / 3).next_to(sin_line, LEFT, buff=0.1))
        cos_label = always_redraw(lambda: MathTex(r'\text{cos}(x)', color=GREEN).scale(0.9*abs(dot.get_x()) / 3).next_to(cos_line, DOWN, buff=0.1))
        sec_label = always_redraw(lambda: MathTex(r'\text{sec}(x)', color=PINK).scale(0.7).next_to(sec_line, DOWN, buff=0.1))
        cossec_label = always_redraw(lambda: MathTex(r'\text{cossec}(x)', color=PURPLE).rotate(90*DEGREES).scale(0.7).next_to(cossec_line, LEFT, buff=0.1))

        path = VMobject(color=WHITE)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        self.camera.frame.scale(1.4).move_to(axes.coords_to_point(0,0,0))



        self.add(axes, circ, dot, labeled_line, arc_40, path, arc_label,
                 cos_line, cos_label,
                 sin_line, sin_label,
                 tg_line, cotg_line,
                 sec_line, sec_label,
                 cossec_line, cossec_label)
        self.wait(2)
        path.save_state()
        

        self.play(Rotate(dot, 359.5*DEGREES, about_point=(axes.c2p(0,0,0))), run_time=10)
        self.play(FadeOut(path))
        self.wait(2)



        # Olhando as funções uma por uma
            # Seno e cosseno
        self.play(FadeOut(tg_line, cotg_line, sec_line, sec_label, cossec_line, cossec_label))
        self.wait(2)
        self.play(Rotate(dot, 359.5*DEGREES, about_point=(axes.c2p(0,0,0))), run_time=10)
        self.play(FadeOut(path))
        self.wait(2)

            # Tangente e cotangente
        self.remove(tg_line, cotg_line, sec_line, sec_label, cossec_line, cossec_label)
        self.wait(2)
        self.play(FadeOut(cos_line, cos_label, sin_line, sin_label),
                  FadeIn(tg_line, cotg_line))
        self.wait(2)

        tg_cotg_line = DashedLine(sec_line.get_end(), cossec_line.get_end(), stroke_width=6, color=YELLOW).scale(1.3).set_z_index(4)
        self.play(FadeIn(tg_cotg_line))
        self.wait(2)
        self.play(Flash(dot, num_lines=8, line_stroke_width=4, flash_radius=0.2, line_length=0.4))
        self.wait(2)
        self.play(FadeOut(tg_cotg_line))
        self.wait(2)
        self.play(Rotate(dot, 360*DEGREES, about_point=(axes.c2p(0,0,0))), run_time=10, rate_func=linear)
        self.play(FadeOut(path))



            # Secante e cossecante
        self.add(axes, circ, dot, labeled_line, arc_40, path, arc_label,
                 tg_line, cotg_line)
        path.save_state()
        self.wait(2)

        tg_cotg_dashedline = always_redraw(lambda: DashedLine(sec_line.get_end(), axes.get_y_axis().number_to_point(9/(dot.get_y())), stroke_width=6, color=GRAY).set_z_index(-5))
        
        self.play(FadeOut(tg_line, cotg_line),
                  FadeIn(tg_cotg_dashedline, sec_label, sec_line, cos_line, cos_label))
        self.wait(2)
        self.play(Rotate(dot, 359.5*DEGREES, about_point=(axes.c2p(0,0,0))), run_time=10, rate_func=linear)
        self.play(FadeOut(path))
        self.wait(2)

        path.restore()
        self.add(path)
        self.play(FadeOut(sec_label, sec_line, cos_line, cos_label),
                  FadeIn(cossec_label, cossec_line, sin_line, sin_label))
        self.wait(2)
        self.play(Rotate(dot, 359.5*DEGREES, about_point=(axes.c2p(0,0,0))), run_time=10)
        self.play(FadeOut(path))
        self.wait(2)






# Comentários sobre as funções que são inversas de outras, então quando uma cresce a outra diminui
class vid23(MovingCameraScene):
    def construct(self):

        # EXPORTAR COM FUNDO TRANSPARENTE : manim -pqh -t Trigonometria.py vid23

        t1 = MathTex(r'\text{cotg}(x) = \frac{1}{\text{tg}(x)}').scale(0.8).to_edge(UL, buff=1)
        t1_bg = SurroundingRectangle(t1, color=BLACK).set_opacity(0.7).set_z_index(-1)
        self.play(FadeIn(t1, t1_bg))
        self.wait(2)

        arrow_1 = Arrow(UP, DOWN, max_tip_length_to_length_ratio=0.15, max_stroke_width_to_length_ratio=8, color=GRAY).scale(0.5).next_to(t1, LEFT, buff=0.1)
        arrow_2 = arrow_1.copy().rotate(180*DEGREES).next_to(t1, RIGHT, buff=0.1).shift(DOWN*0.4)
        self.play(FadeIn(arrow_2, shift=UP))
        self.play(FadeIn(arrow_1, shift=DOWN))
        self.wait(2)
        self.play(Rotate(arrow_1, -180*DEGREES),
                  Rotate(arrow_2, -180*DEGREES))
        self.wait(2)
        self.play(FadeOut(t1, t1_bg, arrow_1, arrow_2))
        self.wait(2)



        t2 = MathTex(r'\text{sec}(x) = \frac{1}{\text{cos}(x)}').scale(0.8).to_edge(UL, buff=1)
        t2_bg = SurroundingRectangle(t1, color=BLACK).set_opacity(0.7).set_z_index(-1)
        self.play(FadeIn(t2, t2_bg))
        self.wait(2)
        
        arrow_3 = Arrow(UP, DOWN, max_tip_length_to_length_ratio=0.15, max_stroke_width_to_length_ratio=8, color=GRAY).scale(0.5).next_to(t2, LEFT, buff=0.1)
        arrow_4 = arrow_3.copy().rotate(180*DEGREES).next_to(t2, RIGHT, buff=0.1).shift(DOWN*0.4)
        self.play(FadeIn(arrow_4, shift=UP), FadeIn(arrow_3, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(t2, t2_bg, arrow_3, arrow_4))
        self.wait(2)



        t3 = MathTex(r'\text{cossec}(x) = \frac{1}{\text{sen}(x)}').scale(0.8).to_edge(UL, buff=1)
        t3_bg = SurroundingRectangle(t1, color=BLACK).set_opacity(0.7).set_z_index(-1)
        self.play(FadeIn(t3, t3_bg))
        self.wait(2)
        
        arrow_5 = Arrow(UP, DOWN, max_tip_length_to_length_ratio=0.15, max_stroke_width_to_length_ratio=8, color=GRAY).scale(0.5).next_to(t3, LEFT, buff=0.1)
        arrow_6 = arrow_5.copy().rotate(180*DEGREES).next_to(t3, RIGHT, buff=0.1).shift(DOWN*0.4)
        self.play(FadeIn(arrow_6, shift=UP), FadeIn(arrow_5, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(t3, t3_bg, arrow_5, arrow_6))
        self.wait(2)

        
        
        self.wait(2)
  



# Acréscimo ao vid1
class vid1aux(ThreeDScene):
    def construct(self):

        dot_A = Dot([-1.99, 0.2, 0]).scale(0)
        dot_B = Dot([1.34, 1.31, 0]).scale(0)  
        dot_C = Dot([0.63, -2.12, 0]).scale(0) 
        g_dots = VGroup(dot_A, dot_B, dot_C).rotate(41.6*DEGREES)  

        triangle_1 = Polygon(dot_A.get_center(), dot_B.get_center(), dot_C.get_center(), color=BLUE, fill_opacity=0).set_z_index(2)#.rotate(37*DEGREES)
        
        COLOR_ANGLE_1 = PURPLE
        COLOR_ANGLE_2 = GREEN
        COLOR_ANGLE_3 = RED

        angle_A = Angle.from_three_points(dot_B.get_center(), dot_A.get_center(), dot_C.get_center(), radius=0.2, stroke_width=40, color=COLOR_ANGLE_1, other_angle=True).set_z_index(-1)        
        angle_B = Angle.from_three_points(dot_A.get_center(), dot_B.get_center(), dot_C.get_center(), radius=0.2, stroke_width=40, color=COLOR_ANGLE_2).set_z_index(-1)
        angle_C = Angle.from_three_points(dot_B.get_center(), dot_C.get_center(), dot_A.get_center(), radius=0.2, stroke_width=40, color=COLOR_ANGLE_3).set_z_index(-1)
        g_angles = VGroup(angle_A, angle_B, angle_C)#.rotate(37*DEGREES)
        

        angle_A_copy = AnnularSector(inner_radius=0, outer_radius=0.4, angle=60*DEGREES, color=COLOR_ANGLE_1).move_to(triangle_1, aligned_edge=DL).set_z_index(-1)   
        angle_B_copy = AnnularSector(inner_radius=0, outer_radius=0.4, angle=60*DEGREES, color=COLOR_ANGLE_2).rotate(-120*DEGREES).move_to(triangle_1, aligned_edge=UP).set_z_index(-1)   
        angle_C_copy = AnnularSector(inner_radius=0, outer_radius=0.4, angle=60*DEGREES, color=COLOR_ANGLE_3).rotate(120*DEGREES).move_to(triangle_1, aligned_edge=DR).set_z_index(-1)   
        g_angles_copies = VGroup(angle_A_copy, angle_B_copy, angle_C_copy).set_opacity(0.5)


        self.add(triangle_1, g_angles, g_angles_copies)


        line_AB = Line(dot_A, dot_B, color=GRAY).set_z_index(1)
        line_AC = Line(dot_A, dot_C, color=GRAY).set_z_index(1)
        line_BC = Line(dot_B, dot_C, color=GRAY).set_z_index(1)

        line_up_1 = line_AB.copy().scale(0.5).move_to(line_AB, aligned_edge=UR)
        line_up_2 = line_BC.copy().scale(0.5).move_to(line_BC, aligned_edge=UL)
        g_up = VGroup(line_up_1, line_up_2, angle_B_copy)

        line_left_1 = line_AB.copy().scale(0.5).move_to(line_AB, aligned_edge=DL)
        line_left_2 = line_AC.copy().scale(0.25).move_to(line_AC, aligned_edge=DL)
        g_left = VGroup(line_left_1, line_left_2, angle_A_copy)

        line_right_1 = line_BC.copy().scale(0.5).move_to(line_BC, aligned_edge=DR)
        line_right_2 = line_AC.copy().scale(0.25).move_to(line_AC, aligned_edge=DR)
        g_right = VGroup(line_right_1, line_right_2, angle_C_copy)

        angle_180 = Arc(radius=0.38, angle=180*DEGREES, color=WHITE).move_to(triangle_1, aligned_edge=DOWN).set_z_index(0).reverse_points()   


        self.add(g_up, g_left, g_right)
        #self.add(Line(LEFT, RIGHT).next_to(triangle_1, DOWN, buff=0.1))

        self.wait()
        self.play(LaggedStart(Rotate(g_left, 180*DEGREES, axis=Y_AXIS, about_point=line_left_2.get_end()),
                              Rotate(g_up, 180*DEGREES, axis=X_AXIS, about_point=(dot_B.get_x(), line_AB.get_y(), 0)),
                              Rotate(g_right, -180*DEGREES, axis=Y_AXIS, about_point=line_right_2.get_start()),
                              lag_ratio=0.3), run_time=3) 
        self.wait()
        self.play(Create(angle_180))
        self.wait()
        self.play(FadeOut(g_up, g_left, g_right, angle_180))
        self.wait()
