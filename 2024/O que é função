# O que é função

from manim import *

# Início do vídeo
class vid0(Scene):
    def construct(self):

        t_1 = Tex('\it Funções').scale(1.5).shift(UP*2)
        self.play(FadeIn(t_1, shift = DOWN), run_time = 2)
        self.wait(2)

        # Lâmpada
        lamp_icon_1 = Polygon([-0.4,-0.7,0], [-0.5,0,0],
                        [-1,1,0], [0,2,0], [1,1,0],
                        [0.5,0,0], [0.4,-0.7,0],
                        color = WHITE).round_corners(radius = 0.8).scale(0.7).set_z_index(0)
        lamp_correction = Line(lamp_icon_1.get_left(), lamp_icon_1.get_right(), stroke_width = 50, color = BLACK).shift(DOWN*0.75).set_z_index(1)
        lamp_icon_2 = Line((-0.5,0,0), (0.5,0,0)).scale(0.5).next_to(lamp_correction, UP, buff = 0.25).set_z_index(2)
        lamp_icon_3 = Line((-0.5,0,0), (0.5,0,0), stroke_width = 6).scale(0.5).next_to(lamp_correction, UP, buff = 0.1).set_z_index(2)
        
        ref = Dot((0,0.7,0), color = BLACK)
        lamp_icon_flashes = VGroup(*[Line(DOWN*0.4, UP*0.1).next_to(lamp_icon_1, UP, buff = 0.4).rotate(80*DEGREES, about_point = ref.get_center()).rotate((-40 * n)*DEGREES, about_point = ref.get_center()) for n in range(5)])

        lamp = VGroup(ref, lamp_icon_1, lamp_icon_2, lamp_icon_3, lamp_correction, lamp_icon_flashes).shift(DOWN*1.2)
        self.add(lamp_icon_1, lamp_icon_2, lamp_icon_3, lamp_correction)
        self.wait(2)
        self.play(Create(lamp_icon_flashes))
        self.wait(2)
        self.play(FadeOut(lamp))

        # Velocímetro
        speedometer_1 = Circle(color = RED).set_z_index(0)
        speedometer_2 = Circle(color = BLACK, fill_opacity = 1).move_to(speedometer_1.get_bottom()).shift(DOWN*0.11).set_z_index(1)
        speedometer_ticks = VGroup(*[Line(UP, DOWN*0.5, stroke_width = 2).scale(0.1).next_to(speedometer_1, UP, buff = -0.2).rotate(120*DEGREES, about_point = ORIGIN).rotate((-30 * n)*DEGREES, about_point = ORIGIN) for n in range (9)]).set_z_index(2)
        speedometer_pointer = Line((0,0,0), (0,0.7,0)).rotate(120*DEGREES, about_point = ORIGIN).set_z_index(3)
    
        speedometer = VGroup(speedometer_1, speedometer_2, speedometer_ticks, speedometer_pointer).shift(DOWN*1.2)
        
        self.add(speedometer)
        self.wait(2)
        self.play(Succession(
            Rotate(speedometer_pointer, -100*DEGREES, about_point = speedometer_1.get_center()),
            Rotate(speedometer_pointer, 10*DEGREES, about_point = speedometer_1.get_center()),
            run_time = 3))
        self.wait(2)
        self.play(FadeOut(speedometer))

        # Projeção do crescimento de uma epidemia
        axes = Axes(x_range = [0, 5, 1],
                    y_range = [0, 4.5, 1],
                    x_length = 5,
                    y_length = 5,
                    axis_config = {"include_ticks" : False,
                                   "include_tip" : False})
        graph = axes.plot(lambda x: 2 ** (x - 3), color = RED)
        g = VGroup(axes, graph).scale(0.7).shift(DOWN*1.2)
        self.play(FadeIn(axes))
        self.wait()
        self.play(Create(graph), run_time = 2)
        self.wait(2)
        self.play(FadeOut(g))

        # Órbitas dos planetas
        sun = Dot(color = YELLOW).scale(1.5).shift(DOWN*1.2+RIGHT*0.2)
        planet_1 = Dot().next_to(sun, RIGHT, buff = 0.35).set_z_index(4)
        planet_2 = Dot().next_to(sun, RIGHT, buff = 0.85).set_z_index(4)
        planet_3 = Dot().next_to(sun, RIGHT, buff = 1.3).set_z_index(4)

        planet_1_trace = TracedPath(planet_1.get_center, stroke_opacity = [1,0]).set_z_index(3)
        planet_2_trace = TracedPath(planet_2.get_center, stroke_opacity = [1,0]).set_z_index(3)
        planet_3_trace = TracedPath(planet_3.get_center, stroke_opacity = [1,0]).set_z_index(3)

        planet_1_path = Ellipse(width = 1.5, height = 1.5).move_to(sun.get_center()).shift(LEFT*0.2)
        planet_2_path = Ellipse(width = 1.6, height = 1.5).scale(1.7).move_to(sun.get_center()).shift(LEFT*0.3)
        planet_3_path = Ellipse(width = 1.7, height = 1.5).scale(1.5).scale(1.5).move_to(sun.get_center()).shift(LEFT*0.4)

        self.play(LaggedStart(
            FadeIn(sun),
            FadeIn(planet_1),
            FadeIn(planet_2),
            FadeIn(planet_3),
            lag_ratio = 0.1))
        
        self.add(planet_1_trace, planet_2_trace, planet_3_trace)

        self.play(LaggedStart(MoveAlongPath(planet_1, planet_1_path),
                              MoveAlongPath(planet_2, planet_2_path),
                              MoveAlongPath(planet_3, planet_3_path),
            lag_ratio = 0.2), run_time = 4)
        self.wait(5)
        
    

# Função como uma máquina
class vid1(Scene):
    def construct(self):

        # Máquina

        machine_color = BLUE    # Cor da máquina
        function = 'f'    # Nome da função
        x = '2'     # Nome da variável independente
        y = '4'     # Nome da variável dependente

            # Corpo
        body = RoundedRectangle(width = 4, height = 3, stroke_color = machine_color, fill_color = BLACK, fill_opacity = 1)

            # Input e Output
        input = Polygon((-2, 0.5, 0),
                        (-3, 1, 0),
                        (-3, -1, 0),
                        (-2, -0.5, 0), color = machine_color, fill_color = BLACK, fill_opacity = 1).scale(0.8).next_to(body, LEFT, buff = 0)
        output = Polygon((2, 0.5, 0),
                        (3, 1, 0),
                        (3, -1, 0),
                        (2, -0.5, 0), color = machine_color, fill_color = BLACK, fill_opacity = 1).scale(0.8).next_to(body, RIGHT, buff = 0)
        
            # Apagar a divisão entre o corpo e o input/output
        correction_left = Polygon((-2, 0.5, 0),
                        (-2.1, 0.55, 0),
                        (-2.1, -0.55, 0),
                        (-2, -0.5, 0), color = BLACK, fill_opacity = 1).scale(0.66).next_to(body, LEFT, buff = -0.03).set_z_index(2)
        correction_right = Polygon((2, 0.5, 0),
                        (2.1, 0.55, 0),
                        (2.1, -0.55, 0),
                        (2, -0.5, 0), color = BLACK, fill_opacity = 1).scale(0.66).next_to(body, RIGHT, buff = -0.03).set_z_index(2)
          
            # Engrenagem 1
                # Círculo central
        g1_1 = Circle(stroke_color = machine_color)
        g1_2 = Circle(color = BLACK, fill_opacity = 1).scale(0.7).set_z_index(2)
                # Dentes
        g2 = Square(side_length = 0.3).next_to(g1_1, UP, buff = -0.1)
        g3 = Square(side_length = 0.3).next_to(g1_1, UP, buff = -0.1).rotate(45*DEGREES, about_point = ORIGIN)
        g4 = Square(side_length = 0.3).next_to(g1_1, UP, buff = -0.1).rotate(90*DEGREES, about_point = ORIGIN)
        g5 = Square(side_length = 0.3).next_to(g1_1, UP, buff = -0.1).rotate(135*DEGREES, about_point = ORIGIN)
        g6 = Square(side_length = 0.3).next_to(g1_1, UP, buff = -0.1).rotate(180*DEGREES, about_point = ORIGIN)
        g7 = Square(side_length = 0.3).next_to(g1_1, UP, buff = -0.1).rotate(225*DEGREES, about_point = ORIGIN)
        g8 = Square(side_length = 0.3).next_to(g1_1, UP, buff = -0.1).rotate(270*DEGREES, about_point = ORIGIN)
        g9 = Square(side_length = 0.3).next_to(g1_1, UP, buff = -0.1).rotate(315*DEGREES, about_point = ORIGIN)
        g = VGroup(g1_1, g2, g3, g4, g5, g6, g7, g8, g9).set_fill(color = machine_color, opacity = 1).set_stroke(color = machine_color)
        
        gear_1 = VGroup(g1_1, g1_2, g2, g3, g4, g5, g6, g7, g8, g9)

        # (Alterativa para criar os dentes da engrenagem)
        gear_1_teeth = VGroup(*[Square(side_length = 0.3).next_to(g1_1, UP, buff = -0.1).rotate((45 * n)*DEGREES, about_point = ORIGIN) for n in range (8)])
        gear_1_teeth.set_fill(color = machine_color, opacity = 1).set_stroke(color = machine_color)

            # Engrenagem 2
                # Círculo central
        g1_1_2 = Circle(stroke_color = machine_color)
        g1_2_2 = Circle(color = BLACK, fill_opacity = 1).scale(0.7).set_z_index(2)
                # Dentes
        g2_2 = Square(side_length = 0.3).next_to(g1_1_2, UP, buff = -0.1)
        g3_2 = Square(side_length = 0.3).next_to(g1_1_2, UP, buff = -0.1).rotate(45*DEGREES, about_point = ORIGIN)
        g4_2 = Square(side_length = 0.3).next_to(g1_1_2, UP, buff = -0.1).rotate(90*DEGREES, about_point = ORIGIN)
        g5_2 = Square(side_length = 0.3).next_to(g1_1_2, UP, buff = -0.1).rotate(135*DEGREES, about_point = ORIGIN)
        g6_2 = Square(side_length = 0.3).next_to(g1_1_2, UP, buff = -0.1).rotate(180*DEGREES, about_point = ORIGIN)
        g7_2 = Square(side_length = 0.3).next_to(g1_1_2, UP, buff = -0.1).rotate(225*DEGREES, about_point = ORIGIN)
        g8_2 = Square(side_length = 0.3).next_to(g1_1_2, UP, buff = -0.1).rotate(270*DEGREES, about_point = ORIGIN)
        g9_2 = Square(side_length = 0.3).next_to(g1_1_2, UP, buff = -0.1).rotate(315*DEGREES, about_point = ORIGIN)
        g_2 = VGroup(g1_1_2, g2_2, g3_2, g4_2, g5_2, g6_2, g7_2, g8_2, g9_2).set_fill(color = machine_color, opacity = 1).set_stroke(color = machine_color)
        
        gear_2 = VGroup(g1_1_2, g1_2_2, g2_2, g3_2, g4_2, g5_2, g6_2, g7_2, g8_2, g9_2).scale(0.85).shift(RIGHT*1.92+UP).rotate(-10*DEGREES)


        gears = VGroup(gear_1, gear_2).move_to(ORIGIN).scale(0.5)


        machine = VGroup(body, input, output, correction_left, correction_right, gears).scale(0.8)
        
        machine_label = MathTex(function, color = machine_color).scale(1.5).next_to(machine, UP)

        machine_label_2 = MathTex('f(','x',') = 2','x', color = machine_color).scale(1.2).next_to(machine, UP)
        machine_label_2[1].set_color(WHITE)
        machine_label_2[3].set_color(WHITE)

        machine_label_3 = MathTex('f(','2',')','= 2 \cdot','2', color = machine_color).scale(1.2).next_to(machine, UP).shift(RIGHT*0.185)
        machine_label_3[1].set_color(WHITE)
        machine_label_3[4].set_color(WHITE)

        machine_label_4 = MathTex('f(','2',')','= 4', color = machine_color).scale(1.2).next_to(machine, UP).shift(LEFT*0.185)
        machine_label_4[1].set_color(WHITE)

        # Animação da máquina

        self.add(machine, machine_label)
        self.wait(3)
        self.play(ReplacementTransform(machine_label, machine_label_2))
        self.wait(2)

            # Variável x entra no input
        input_arrow = MathTex(r'\rightarrow').scale(1.5).next_to(machine, LEFT, buff = 0.5).set_z_index(-1)
        x_variable = MathTex(x).scale(1.2).next_to(input_arrow, LEFT, buff = 0.5).set_z_index(-1)
    
        self.play(FadeIn(x_variable), FadeIn(input_arrow))
        self.play(x_variable.animate.shift(RIGHT*3),
                  input_arrow.animate.shift(RIGHT*3),
                  run_time = 2)
        self.remove(x_variable, input_arrow)

            # Engrenagens giram
        self.play(Rotate(gear_1, -360*DEGREES),
                  Rotate(gear_2, 360*DEGREES),
                  run_time = 3)
        self.play(ReplacementTransform(machine_label_2, machine_label_3))
        self.wait(2)
        self.play(ReplacementTransform(machine_label_3[3:5], machine_label_4[3]))
        self.wait(2)

            # Variável y sai do output
        output_arrow = MathTex(r'\rightarrow').scale(1.5).next_to(machine, RIGHT, buff = 0.5).set_z_index(-1).shift(LEFT*3)
        y_variable = MathTex(y).scale(1.5).next_to(output_arrow, RIGHT, buff = 0.5).set_z_index(-1)

        self.add(y_variable, output_arrow)
        self.play(y_variable.animate.shift(RIGHT*3),
                  output_arrow.animate.shift(RIGHT*3),
                  run_time = 2)
        self.play(FadeOut(output_arrow))
        self.wait(3)



# Função área do retângulo A = 2x
class vid2(Scene):
    def construct(self):

        rectangle = Rectangle(width = 3, height = 2, color = BLUE, fill_opacity = 0.2)

        base = Brace(rectangle, DOWN, color = RED)
        
        height = Brace(rectangle, LEFT, color = BLUE)
        height_label = MathTex('2', color = BLUE).next_to(height, LEFT)

        base_label_1 = MathTex('x', color = base.get_color()).next_to(base, DOWN, buff = 0.3)
        base_label_2 = MathTex('x = 1', color = base.get_color()).next_to(base, DOWN)
        base_label_3 = MathTex('x = 2', color = base.get_color()).next_to(base, DOWN)
        base_label_4 = MathTex('x = 5', color = base.get_color()).next_to(base, DOWN)


        area_label_0 = MathTex('y', color = BLUE).move_to(rectangle.get_center())
        
        area_label_3 = MathTex(r'y = 2 \cdot','1',' = 2', color = BLUE).next_to(rectangle, UP, buff = 1)
        area_label_3[1].set_color(base.get_color())
        
        area_label_1 = MathTex(r'y','= 2','x', color = BLUE).move_to(area_label_3)
        area_label_1[2].set_color(base.get_color())
        
        area_label_2 = MathTex(r'y = 2 \cdot','1','',' = 2', color = BLUE).move_to(area_label_3)
        area_label_2[1].set_color(base.get_color())
        
        area_label_4 = MathTex(r'y = 2 \cdot','2',' = 4', color = BLUE).move_to(area_label_3)
        area_label_4[1].set_color(base.get_color())
        
        area_label_5 = MathTex(r'y = 2 \cdot','5',' = 10', color = BLUE).move_to(area_label_3)
        area_label_5[1].set_color(base.get_color())


        # Criando o retângulo e a fórmula da área
        self.play(DrawBorderThenFill(rectangle))
        self.wait(2)

        self.play(FadeIn(height))
        height.add_updater(lambda m: m.become(Brace(rectangle, LEFT, color = BLUE)))
        self.play(Write(height_label))
        height_label.add_updater(lambda m: m.become(MathTex('2', color = BLUE).next_to(height, LEFT)))
        
        self.play(FadeIn(base))
        base.add_updater(lambda m: m.become(Brace(rectangle, DOWN, color = base.get_color())))
        self.play(Write(base_label_1))
        self.wait(3)

        self.play(Write(area_label_0))
        self.wait(2)
        self.play(ReplacementTransform(area_label_0, area_label_1[0]))
        self.play(Write(area_label_1[1:3]))
        self.wait(2)

        # Variando o tamanho da base
        self.play(rectangle.animate.stretch_to_fit_width(1),
                  TransformMatchingShapes(base_label_1, base_label_2),
                  TransformMatchingShapes(area_label_1, area_label_3[0:2]))
        self.wait(2)
        self.play(Write(area_label_3[2]))
        self.wait(2)
        self.play(rectangle.animate.stretch_to_fit_width(2),
                  ReplacementTransform(base_label_2, base_label_3),
                  ReplacementTransform(area_label_3, area_label_4))
        self.wait(2)
        self.play(rectangle.animate.stretch_to_fit_width(5),
                  ReplacementTransform(base_label_3, base_label_4),
                  ReplacementTransform(area_label_4, area_label_5))
        self.wait(2)

        area_label_6 = MathTex(r'y = f(',r'x',r') = 2',r'x', color = BLUE).move_to(area_label_3)
        area_label_6[1].set_color(base.get_color())
        area_label_6[3].set_color(base.get_color())
        self.play(ReplacementTransform(area_label_5, area_label_1),
                  ReplacementTransform(base_label_4, base_label_1))
        self.wait(2)
        self.play(ReplacementTransform(area_label_1, area_label_6))
        self.wait(2)

        # Função vai para o centro 
        t = MathTex(r'y','=',' f(',r'x',r') = 2',r'x').scale(1.2)
        self.play(LaggedStart(FadeOut(rectangle, height, height_label, base, base_label_1),
                  TransformMatchingShapes(area_label_6, t),
                  lag_ratio = 0.8))
        self.wait(2)
        self.play(t[0].animate.set_color(BLUE),
                  t[3].animate.set_color(RED),
                  t[5].animate.set_color(RED))
        self.wait(2)
        self.play(t.animate.set_color(WHITE))
        self.wait(2)
        self.play(t[2:6].animate.set_color(YELLOW))
        self.wait(2)
        self.play(t.animate.set_color(WHITE))
        self.wait(2)



# Variáveis independente e dependente
class vid3(Scene):
    def construct(self):

        
        t = MathTex(r'y','=',' f(',r'x',r') = 2',r'x').scale(1.2)
        self.add(t)

        var_dep_1 = Tex(r'\it Variável').next_to(t, DL, buff = 1)
        var_dep_2 = Tex(r'\it dependente').next_to(var_dep_1, DOWN)
        var_dep_arrow = Arrow(var_dep_1.get_corner(UR), t.get_corner(DL))
        var_dep = VGroup(var_dep_1, var_dep_2, var_dep_arrow).set_color(BLUE)

        var_indep_1 = Tex(r'\it Variável').next_to(t, DR, buff = 1)
        var_indep_2 = Tex(r'\it independente').next_to(var_indep_1, DOWN)
        var_indep_arrow = Arrow(var_indep_1.get_corner(UL), t.get_corner(DR))
        var_indep = VGroup(var_indep_1, var_indep_2, var_indep_arrow).set_color(RED)

        self.play(t[0].animate.set_color(BLUE),
                  t[3].animate.set_color(RED),
                  t[5].animate.set_color(RED))
        self.play(FadeIn(var_dep_1, var_indep_1, var_dep_arrow, var_indep_arrow))
        self.wait(2)
        self.play(FadeIn(var_indep_2))

        t1 = MathTex(r'y','=',' f(',r'1',r') = 2 \cdot',r'1').scale(1.2).align_to(t, LEFT)
        t1[0].set_color(BLUE)
        t1[3].set_color(RED)
        t1[5].set_color(RED)
        self.play(TransformMatchingShapes(t, t1),
                  Rotate(var_indep_arrow, -15*DEGREES, about_point = var_indep_arrow.get_corner(DR)))

        t2 = MathTex(r'y','=',' f(',r'2',r') = 2 \cdot',r'2').scale(1.2).align_to(t, LEFT)
        t2[0].set_color(BLUE)
        t2[3].set_color(RED)
        t2[5].set_color(RED)
        self.play(ReplacementTransform(t1, t2))

        t3 = MathTex(r'y','=',' f(',r'3',r') = 2 \cdot',r'3').scale(1.2).align_to(t, LEFT)
        t3[0].set_color(BLUE)
        t3[3].set_color(RED)
        t3[5].set_color(RED)
        self.play(ReplacementTransform(t2, t3))

        t4 = MathTex(r'y','=',' f(',r'4',r') = 2 \cdot',r'4').scale(1.2).align_to(t, LEFT)
        t4[0].set_color(BLUE)
        t4[3].set_color(RED)
        t4[5].set_color(RED)
        self.play(ReplacementTransform(t3, t4))

        t5 = MathTex(r'y','=',' f(',r'5',r') = 2 \cdot',r'5').scale(1.2).align_to(t, LEFT)
        t5[0].set_color(BLUE)
        t5[3].set_color(RED)
        t5[5].set_color(RED)
        self.play(ReplacementTransform(t4, t5))
        
        t6 = MathTex(r'y','=',' f(',r'x',r') = 2 \cdot',r'x').scale(1.2).align_to(t, LEFT)
        t6[0].set_color(BLUE)
        t6[3].set_color(RED)
        t6[5].set_color(RED)
        self.play(ReplacementTransform(t5, t6))

        self.play(FadeIn(var_dep_2))
        
        t7 = MathTex(r'2','=',' f(',r'1',r') = 2 \cdot',r'1').scale(1.2).align_to(t, LEFT)
        t7[0].set_color(BLUE)
        t7[3].set_color(RED)
        t7[5].set_color(RED)
        self.play(ReplacementTransform(t6, t7))

        t8 = MathTex(r'4','=',' f(',r'2',r') = 2 \cdot',r'2').scale(1.2).align_to(t, LEFT)
        t8[0].set_color(BLUE)
        t8[3].set_color(RED)
        t8[5].set_color(RED)
        self.play(ReplacementTransform(t7, t8))

        t9 = MathTex(r'6','=',' f(',r'3',r') = 2 \cdot',r'3').scale(1.2).align_to(t, LEFT)
        t9[0].set_color(BLUE)
        t9[3].set_color(RED)
        t9[5].set_color(RED)
        self.play(ReplacementTransform(t8, t9))

        t10 = MathTex(r'8','=',' f(',r'4',r') = 2 \cdot',r'4').scale(1.2).align_to(t, LEFT)
        t10[0].set_color(BLUE)
        t10[3].set_color(RED)
        t10[5].set_color(RED)
        self.play(ReplacementTransform(t9, t10))

        t11 = MathTex(r'10','=',' f(',r'5',r') = 2 \cdot',r'5').scale(1.2)
        t11[0].set_color(BLUE)
        t11[3].set_color(RED)
        t11[5].set_color(RED)
        self.play(ReplacementTransform(t10, t11))

        t12 = MathTex(r'y','=',' f(',r'x',r') = 2',r'x').scale(1.2)
        t12[0].set_color(BLUE)
        t12[3].set_color(RED)
        t12[5].set_color(RED)
        self.play(ReplacementTransform(t11, t12),
                  Rotate(var_indep_arrow, 15*DEGREES, about_point = var_indep_arrow.get_corner(DR)))
        self.play(FadeOut(var_dep, var_indep))
        self.wait(3)

        t13 = MathTex(r's','=',' f(',r'v',r') = 2',r'v').scale(1.2)
        t13[0].set_color(BLUE)
        t13[3].set_color(RED)
        t13[5].set_color(RED)
        self.play(ReplacementTransform(t12, t13))
        self.wait(2)

        t14 = MathTex(r'c','=',' f(',r't',r') = 2',r't').scale(1.2)
        t14[0].set_color(BLUE)
        t14[3].set_color(RED)
        t14[5].set_color(RED)
        self.play(ReplacementTransform(t13, t14))
        self.wait(2)
       
        self.play(ReplacementTransform(t14, t11))
        self.wait(3)

        func_arrow = Arrow(UP*0.5, DOWN).next_to(t12[2], UP)
        self.play(FadeIn(func_arrow))
        self.wait(3)

        t15 = MathTex(r'y','=',' g(',r'x',r') = 2',r'x').scale(1.2)
        t15[0].set_color(BLUE)
        t15[3].set_color(RED)
        t15[5].set_color(RED)
        self.play(ReplacementTransform(t11, t15))
        self.wait(2)

        t16 = MathTex(r'y','=',' h(',r'x',r') = 2',r'x').scale(1.2)
        t16[0].set_color(BLUE)
        t16[3].set_color(RED)
        t16[5].set_color(RED)
        self.play(ReplacementTransform(t15, t16))
        self.wait(2)

        t17 = MathTex(r'y','=',' f(',r'x',r') = 2',r'x').scale(1.2)
        t17[0].set_color(BLUE)
        t17[3].set_color(RED)
        t17[5].set_color(RED)
        self.play(ReplacementTransform(t16, t17),
                  FadeOut(func_arrow))
        self.wait(2)



# Tabela
class vid4(Scene):
    def construct(self):

        t = MathTex(r'y','=',' f(',r'x',r') = 2',r'x').scale(1.2)
        t[0].set_color(BLUE)
        t[3].set_color(RED)
        t[5].set_color(RED)
        self.add(t)
        self.wait(2)
        self.play(t.animate.shift(UP*3))

        v_line = Line(UP, DOWN, stroke_width = 2).scale(2).shift(DOWN*0.3)
        h_line_1 = Line(LEFT, RIGHT, stroke_width = 2).scale(2)
        h_line_2 = Line(LEFT, RIGHT, stroke_width = 2).scale(2)
        h_line_3 = Line(LEFT, RIGHT, stroke_width = 2).scale(2)
        h_line_4 = Line(LEFT, RIGHT, stroke_width = 2).scale(2)
        h_lines = VGroup(h_line_1, h_line_2, h_line_3, h_line_4).arrange(DOWN, buff = 1).shift(DOWN*0.8)
        
        x_table = MathTex('x', color = RED).scale(1.3).next_to(v_line, LEFT, buff = 0.9).shift(UP*1.5)
        y_table = MathTex('y', color = BLUE).scale(1.2).next_to(v_line, RIGHT, buff = 0.9).shift(UP*1.5)

        # Criando tabela
        self.play(LaggedStart(
            Create(v_line),
            Create(h_lines),
            lag_ratio = 0.5))
        self.play(FadeIn(x_table))
        self.wait(2)
        self.play(FadeIn(y_table))
        self.wait(2)

        # Destaque na lei da função
        arrow1 = Arrow(DOWN*0.5, UP).rotate(-45*DEGREES).shift(LEFT*2.4+UP*1.8)
        g = VGroup(v_line, h_lines, x_table, y_table)
        self.play(g.animate.set_opacity(0.3),
                  FadeIn(arrow1))
        self.wait(2)
        self.play(arrow1.animate.shift(RIGHT*3.3))
        self.wait(2)
        self.play(FadeOut(arrow1),
                  g.animate.set_opacity(1))

        x_value_1 = MathTex('1').scale(1.2).next_to(v_line, LEFT, buff = 0.9).shift(UP*0.5)
        x_value_2 = MathTex('2').scale(1.2).next_to(v_line, LEFT, buff = 0.9).shift(DOWN*0.5)
        x_value_3 = MathTex(r'\pi').scale(1.2).next_to(v_line, LEFT, buff = 0.9).shift(DOWN*1.5)
        x_values = VGroup(x_value_1, x_value_2, x_value_3)

        y_value_1 = MathTex('2').scale(1.2).next_to(v_line, RIGHT, buff = 0.9).shift(UP*0.5)
        y_value_2 = MathTex('4').scale(1.2).next_to(v_line, RIGHT, buff = 0.9).shift(DOWN*0.5)
        y_value_3 = MathTex(r'2\pi').scale(1.2).next_to(v_line, RIGHT, buff = 0.75).shift(DOWN*1.5)
        y_values = VGroup(y_value_1, y_value_2, y_value_3)

        etc1 = MathTex('...').scale(1.2).next_to(v_line, LEFT, buff = 0.9).shift(DOWN*2.5).rotate(-90*DEGREES)
        etc2 = MathTex('...').scale(1.2).next_to(v_line, RIGHT, buff = 0.9).shift(DOWN*2.5).rotate(-90*DEGREES)

        table = VGroup(v_line, h_lines, x_table, y_table, x_values, y_values, etc1, etc2)

        # Colocando valores
        self.play(FadeIn(x_value_1))
        self.wait(2)
        self.play(FadeIn(y_value_1))
        self.wait(2)

        self.play(FadeIn(x_value_2))
        self.wait(2)
        self.play(FadeIn(y_value_2))
        self.wait(2)

        self.play(FadeIn(x_value_3))
        self.wait(2)
        self.play(FadeIn(y_value_3))
        self.wait(2)

        self.play(LaggedStart(Write(etc1), Write(etc2), lag_ratio = 0.5))
        self.wait(2)
        
        # FadeOut geral
        self.play(FadeOut(t, table))



# Domínio e Contradomínio
class vid5(Scene):
    def construct(self):

        # Função associa x ---> f(x)
        t1 = MathTex('f', color = BLUE).scale(1.5).shift(UP)
        t2 = MathTex('x',r'\longmapsto','f(x)').scale(1.5).shift(RIGHT*0.5)
        self.play(FadeIn(t1))
        self.play(Write(t2[0]))
        self.play(GrowFromEdge(t2[1], LEFT))
        self.play(FadeIn(t2[2]))
        self.wait(2)

        t3 = MathTex('x',r'\longmapsto','y').scale(1.5).shift(DOWN*0.05)
        t3[0].set_color(RED)
        t3[2].set_color(BLUE)
        t4 = MathTex('x',r'\longmapsto','y').scale(1.5).shift(DOWN*0.05)
        
        self.play(ReplacementTransform(t2[0], t3[0]))
        self.play(ReplacementTransform(t3[0], t4[0]))
        self.wait(2)
        self.play(ReplacementTransform(t2[2], t3[2]))
        self.play(ReplacementTransform(t3[2], t4[2]))
        self.wait(2)

        # Domínio e Contradomínio
        domain = Ellipse(width = 3, height = 4, fill_opacity = 0.2).shift(LEFT*2.5)
        domain_label_1 = MathTex('?', color = RED).scale(1.5).next_to(domain, UP, buff = 0.3).set_z_index(1)
        domain_label_2 = Tex(r'\it Domínio', color = RED).scale(1.1).next_to(domain, UP, buff = 0.3).set_z_index(1)
        domain_label_3 = MathTex(r'D_{f}', color = RED).scale(1.2).next_to(domain, UP, buff = 0.3).set_z_index(1)
        domain_label_4 = MathTex(r'\mathbb{R}_{+}', color = RED).scale(1.2).next_to(domain, UP, buff = 0.3).set_z_index(1)        

        codomain = Ellipse(width = 3, height = 4, color = BLUE, fill_opacity = 0.2).shift(RIGHT*2.5)
        codomain_label_1 = MathTex('?', color = BLUE).scale(1.5).next_to(codomain, UP, buff = 0.3).set_z_index(1)
        codomain_label_2 = Tex(r'\it Contradomínio', color = BLUE).scale(1.1).next_to(codomain, UP, buff = 0.3).set_z_index(1)
        codomain_label_3 = MathTex(r'CD_{f}', color = BLUE).scale(1.2).next_to(codomain, UP, buff = 0.3).set_z_index(1)
        codomain_label_4= MathTex(r'\mathbb{R}_{+}', color = BLUE).scale(1.2).next_to(codomain, UP, buff = 0.3).set_z_index(1)

        x_1 = MathTex('x').scale(1.5).move_to(domain)
        y_1 = MathTex('y').scale(1.5).move_to(codomain)
        g = VGroup(x_1, y_1)
        
        self.play(FadeOut(t1, t2[1]), TransformMatchingShapes(t4, g))
        self.play(DrawBorderThenFill(domain))
        self.wait(2)
        self.play(DrawBorderThenFill(codomain))
        self.wait(2)
        self.play(FadeIn(domain_label_1, codomain_label_1))
        self.wait(2)
        self.play(LaggedStart(
            TransformMatchingShapes(domain_label_1, domain_label_2),
            TransformMatchingShapes(codomain_label_1, codomain_label_2),
            lag_ratio = 0.8))
        self.wait(2)

        # Destaque no domínio
        g1 = VGroup(codomain_label_2, y_1)
        self.play(g1.animate.set_opacity(0.3), codomain.animate.set_stroke(opacity = 0.4))
        self.play(TransformMatchingShapes(domain_label_2, domain_label_3))
        self.wait(2)

        # Destaque no contradomínio
        g2 = VGroup(domain_label_3, x_1)
        self.play(g1.animate.set_opacity(1), codomain.animate.set_stroke(opacity = 1),
                  g2.animate.set_opacity(0.3), domain.animate.set_stroke(opacity = 0.4))
        self.play(TransformMatchingShapes(codomain_label_2, codomain_label_3))
        self.wait(2)
        self.play(g2.animate.set_opacity(1), domain.animate.set_stroke(opacity = 1))
        self.wait(2)

        # Seta da função ligando x ---> y
        t = MathTex('f').scale(1.2).shift(UP*1.5)
        self.play(FadeIn(t))

        arrow = CurvedArrow((-2.1,0.1,0), (2.1,0.1,0), radius = -4, stroke_width = 2)
        self.play(Create(arrow), run_time = 1.5)
        self.wait(2)

        # Df e CDf = R+
        self.play(TransformMatchingShapes(domain_label_3, domain_label_4),
                  TransformMatchingShapes(codomain_label_3, codomain_label_4))
        self.wait(2)

        # Definindo a função exemplo
            # Diagarma vai para baixo
        g_diagram = VGroup(domain, codomain,
                           domain_label_4, codomain_label_4,
                           x_1, y_1,
                           t, arrow)
        self.play(g_diagram.animate.scale(0.9).shift(DOWN*1.2))
            # Diminuir opacidade do diagrama
        g3 = VGroup(domain_label_4, codomain_label_4)
        black_rectangle = Rectangle(width = 10, height = 8, color = BLACK, fill_opacity = 0.5).shift(DOWN*3.2).set_z_index(2)
        self.play(g3.animate.set_opacity(0.3), FadeIn(black_rectangle))
        self.wait(2)

        tt = MathTex(r'f:',r'\mathbb{R}_{+}',r'\to',r'\mathbb{R}_{+}',r'\:\:,\:\:',r'f(x) = 2x').shift(UP*3)
        self.play(Write(tt[0:4]))
        self.wait(2)
        self.play(Write(tt[4:6]))
        self.wait(2)

        # Destaque na definição da função com uma seta      
        arrow2 = Arrow(DOWN, UP*0.5, color = YELLOW).rotate(45*DEGREES).shift(UP*2.5+LEFT*1.5)
        self.play(FadeIn(arrow2))
        self.wait(2)
        self.play(arrow2.animate.shift(RIGHT*1.5))
        self.wait(2)
        self.play(arrow2.animate.shift(RIGHT*1.5))
        self.wait(2)
        self.play(arrow2.animate.shift(RIGHT*1.4))
        self.wait(2)
        self.play(FadeOut(arrow2))
        self.wait(2)

        # Pode substituir f(x) = 2x por x ---> 2x
        tt2 = MathTex(r'f:',r'\mathbb{R}_{+}',r'\to',r'\mathbb{R}_{+}',r'\:\:,\:\:',r'x \longmapsto 2x').shift(UP*3+LEFT*0.15)
        tt2[5].set_color(YELLOW)

        self.play(tt[5].animate.set_color(YELLOW))
        self.wait(2)
        self.play(TransformMatchingShapes(tt[5], tt2[5]))
        self.wait(2)
        self.play(tt2[5].animate.set_color(WHITE))
        arrow2.shift(LEFT*1.6)
        self.play(FadeIn(arrow2))
        self.wait(2)
        self.play(arrow2.animate.shift(RIGHT*1.4))
        self.wait(2)
        self.play(FadeOut(arrow2))
        self.wait(2)

            # Volta a opacidade do diagrama ao normal
        self.play(g3.animate.set_opacity(1), FadeOut(black_rectangle))
        self.wait(2)

        # Colocando alguns pontos no diagrama
        x_value_1 = MathTex('1', color = YELLOW).move_to(x_1)
        y_value_1 = MathTex('2', color = YELLOW).move_to(y_1)
        
        self.play(TransformMatchingShapes(x_1, x_value_1))
        self.play(x_value_1.animate.set_color(WHITE))
        self.play(arrow.animate.set_color(YELLOW))
        self.play(arrow.animate.set_color(WHITE))
        self.play(TransformMatchingShapes(y_1, y_value_1))
        self.play(y_value_1.animate.set_color(WHITE))
        self.wait(2)


        g4 = VGroup(x_value_1, y_value_1, arrow, t)
        x_value_2 = MathTex('2', color = YELLOW).move_to(x_1)
        y_value_2 = MathTex('4', color = YELLOW).move_to(y_1)
        arrow3 = CurvedArrow((-2.1,-1.2,0), (2.1,-1.2,0), radius = -4, stroke_width = 2, color = YELLOW).scale(0.9).shift(UP*0.1)
        
        self.play(g4.animate.shift(UP),
                  FadeIn(x_value_2, arrow3, y_value_2))
        self.play(x_value_2.animate.set_color(WHITE),
                  arrow3.animate.set_color(WHITE),
                  y_value_2.animate.set_color(WHITE))
        self.wait(2)


        x_value_3 = MathTex('3', color = YELLOW).move_to(x_1).shift(DOWN)
        y_value_3 = MathTex('6', color = YELLOW).move_to(y_1).shift(DOWN)
        arrow4 = CurvedArrow((-2.1,-2.2,0), (2.1,-2.2,0), radius = -4, stroke_width = 2, color = YELLOW).scale(0.9).shift(UP*0.1)
        
        self.play(FadeIn(x_value_3, arrow4, y_value_3))
        self.play(x_value_3.animate.set_color(WHITE),
                  arrow4.animate.set_color(WHITE),
                  y_value_3.animate.set_color(WHITE))
        self.wait(2)
    


# Definição geral de função
class vid6(Scene):
    def construct(self):

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

        # Função e setas
                                         # 0            1         2         3         4                  5                         6             7      8       9             10                11        12     13      
        function_definition = Tex(r'\it Uma função ',r'$f:\:$',r'$A$',r'$\:\to\:$',r'$B$',r' é uma relação que associa ',r'\\ cada elemento ',r'$x$',r' de ',r'$A$',r' a um único elemento ',r'$f(x)$',r' de ',r'$B$').scale(0.95).shift(UP*2.7)
        function_definition[2].set_color(RED)
        function_definition[4].set_color(BLUE)
        function_definition[7].set_color(RED)
        function_definition[9].set_color(RED)
        function_definition[11].set_color(BLUE)
        function_definition[13].set_color(BLUE)

        function = MathTex(r'f').scale(1.2).shift(UP*2.3)

        arrow_1 = CurvedArrow((-2.2, 1.2, 0), (2.2, 1.2, 0), radius = -5, stroke_width = 2.5)
        arrow_2 = CurvedArrow((-2.2, 0.4, 0), (2.2, 0.4, 0), radius = -5, stroke_width = 2.5)
        arrow_3 = CurvedArrow((-2.2, -0.4, 0), (2.2, -0.4, 0), radius = -5, stroke_width = 2.5)
        arrow_4 = CurvedArrow((-2.2, -1.1, 0), (2.2, -0.4, 0), radius = -5, stroke_width = 2.5)

        arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4)

        g_diagram = VGroup(domain, domain_label_1, domain_elements,
                           codomain, codomain_label_1, codomain_elements,
                           function, arrows).scale(0.9).shift(DOWN*1.2)

        # Criar domínio e contradomínio
        self.play(FadeIn(
            domain, domain_label_1,
            domain_element_1,
            domain_element_2,
            domain_element_3,
            domain_element_4))
        self.play(FadeIn(
            codomain, codomain_label_1,
            codomain_element_1,
            codomain_element_2,
            codomain_element_3,
            codomain_element_4))
        self.wait()

        # Escrevendo a definição de função
        self.play(Write(function_definition[0]))
        self.wait(2)
        self.play(Write(function_definition[1:5]))
        self.wait(2)
        self.play(Write(function_definition[5:7]), run_time = 2)
        self.wait(2)
        self.play(Write(function_definition[7:10]))
        self.wait(2)
        self.play(Write(function_definition[10]))
        self.wait(2)
        self.play(Write(function_definition[11:14]))
        self.wait(2)

        # Criando as setas
        self.play(LaggedStart(
            Create(arrow_1),
            Create(arrow_2),
            Create(arrow_3),
            Create(arrow_4),
            lag_ratio = 0.3),
            FadeIn(function))
        
        # Destaque no domínio (A) e contradomínio (B) na definição
            # Diminui a opacidade de tudo
        g = VGroup(function_definition[0], function_definition[5:14])
        black_rectangle = Rectangle(width = 10, height = 8, color = BLACK, fill_opacity = 0.5).shift(DOWN*2.2).set_z_index(2)
        self.play(g.animate.set_opacity(0.3), FadeIn(black_rectangle))

            # Seta indicando A e B
        indicative_arrow = Arrow(DOWN, UP*0.5).rotate(45*DEGREES).shift(UP*2.5+LEFT*1.3)
        self.play(FadeIn(indicative_arrow))
        self.wait(2)
        self.play(indicative_arrow.animate.shift(RIGHT*1.1))
        self.wait(2)
        self.play(FadeOut(indicative_arrow))

            # Volta a opacidade de tudo ao normal
        self.play(g.animate.set_opacity(1), FadeOut(black_rectangle))
        self.wait(2)



# Mostrando as condições para ser função e exemplos de relações que não são funções
class vid7(Scene):
    def construct(self):

        # Retomando a definição e o diagrama
            # Definição
                                         # 0            1         2         3         4                  5                         6             7      8       9             10                11        12     13      
        function_definition = Tex(r'\it Uma função ',r'$f:\:$',r'$A$',r'$\:\to\:$',r'$B$',r' é uma relação que associa ',r'\\ cada elemento ',r'$x$',r' de ',r'$A$',r' a um único elemento ',r'$f(x)$',r' de ',r'$B$').scale(0.95).shift(UP*2.7)
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
        arrow_4 = CurvedArrow((-2.2, -1.1, 0), (2.2, -0.4, 0), radius = -5, stroke_width = 2.5)
        arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4)

        g_diagram = VGroup(domain, domain_label_1, domain_elements,
                           codomain, codomain_label_1, codomain_elements,
                           function, arrows).scale(0.9).shift(DOWN*1.2)

        self.add(function_definition, g_diagram)
        self.wait(2)

        # Indicando as implicações da definição
            # 1 Não pode sobrar elemento no domínio
        underline_1 = Underline(function_definition[6:10], color = YELLOW)
        self.play(FadeIn(underline_1))
        self.wait(2)

        indicative_arrow_1 = Arrow(DOWN, UP*0.5, color = YELLOW).rotate(-60*DEGREES).shift(DOWN*0.2+LEFT*3)
        self.play(FadeIn(indicative_arrow_1))
        self.play(indicative_arrow_1.animate.shift(DOWN*2.1))
        self.play(FadeOut(indicative_arrow_1))
        self.play(FadeOut(underline_1))
        self.wait(2)

            # 2 Cada elemento de A associado a apenas um elemento de B
        underline_2 = Underline(function_definition[10:14], color = YELLOW)
        self.play(FadeIn(underline_2))
        self.wait(2)

        indicative_arrow_2 = Arrow(DOWN, UP*0.5, color = YELLOW).rotate(60*DEGREES).shift(DOWN*0.2+RIGHT*3)
        self.play(FadeIn(indicative_arrow_2))
        self.play(indicative_arrow_2.animate.shift(DOWN*1.5))
        self.play(FadeOut(indicative_arrow_2))
        self.play(FadeOut(underline_2))
        self.wait(2)

            # Conclusão: de cada elemento em A deve sair uma seta
        self.play(LaggedStart(
            Flash(domain_element_1, num_lines = 8),
            Flash(domain_element_2, num_lines = 8),
            Flash(domain_element_3, num_lines = 8),
            Flash(domain_element_4, num_lines = 8),
            lag_ratio = 0.3))
        self.wait(2)
                
        self.wait(2)
        self.play(LaggedStart(
            Indicate(arrow_1, scale_factor = 1.05),
            Indicate(arrow_2, scale_factor = 1.05),
            Indicate(arrow_3, scale_factor = 1.05),
            Indicate(arrow_4, scale_factor = 1.05),
            lag_ratio = 0.4))
        self.wait(2)

        # Exemplos de relações que não são funções
        self.play(FadeOut(arrows, function))
        self.wait(2)
        
        t_1 = Tex('Não é função', color = RED_D).scale(0.9).shift(UP)

            # Relação 1
        r1_arrow_1 = CurvedArrow((-2.2, 1.2, 0), (2.2, 0.8, 0), radius = -5, stroke_width = 2.5)
        r1_arrow_2 = CurvedArrow((-2.2, 0.4, 0), (2.2, 0, 0), radius = -5, stroke_width = 2.5)
        r1_arrow_3 = CurvedArrow((-2.2, -0.4, 0), (2.2, -0.8, 0), radius = -5, stroke_width = 2.5)
        r1_arrows = VGroup(r1_arrow_1, r1_arrow_2, r1_arrow_3).scale(0.9).shift(DOWN*1.2)
        self.play(codomain_elements.animate.shift(DOWN*0.4),
                  FadeOut(codomain_element_4))
        self.play(Create(r1_arrows))
        self.wait(2)
        self.play(FadeIn(t_1))
        self.wait(2)
        
        indicative_arrow_3 = Arrow(DOWN, UP*0.5, color = YELLOW).rotate(-60*DEGREES).shift(DOWN*2.4+LEFT*3)
        self.play(FadeIn(indicative_arrow_3))
        self.wait(2)
        self.play(FadeOut(indicative_arrow_3))
        self.wait(2)
        self.play(FadeOut(r1_arrows, t_1))
        self.wait(2)

            # Relação 2
        r2_arrow_1 = CurvedArrow((-2.2, 0.8, 0), (2.2, 1.2, 0), radius = -5, stroke_width = 2.5)
        r2_arrow_2 = CurvedArrow((-2.2, 0, 0), (2.2, 0.4, 0), radius = -5, stroke_width = 2.5)
        r2_arrow_3 = CurvedArrow((-2.2, -0.8, 0), (2.2, -0.4, 0), radius = -5, stroke_width = 2.5)
        r2_arrow_4 = CurvedArrow((-2.2, -0.8, 0), (2.2, -1.2, 0), radius = -5, stroke_width = 2.5)
        r2_arrows = VGroup(r2_arrow_1, r2_arrow_2, r2_arrow_3, r2_arrow_4).scale(0.9).shift(DOWN*1.2)
        self.play(domain_elements.animate.shift(DOWN*0.4),
                  FadeOut(domain_element_4),
                  codomain_elements.animate.shift(UP*0.4),
                  FadeIn(codomain_element_4))
        self.play(Create(r2_arrows))
        self.wait(2)
        self.play(FadeIn(t_1))
        self.wait(2)
        self.play(Flash(domain_element_3))
        self.wait(2)
        self.play(LaggedStart(
            Indicate(r2_arrow_3, scale_factor = 1.05),
            Indicate(r2_arrow_4, scale_factor = 1.05),
            lag_ratio = 0.4))
        self.wait(2)
        self.play(LaggedStart(
            Flash(codomain_element_3),
            Flash(codomain_element_4),
            lag_ratio = 0.4))
        self.wait(2)
        self.play(FadeOut(r2_arrows, t_1))
        self.wait(2)

            # Relação 3 (a incial)
        t_2 = Tex('É função', color = GREEN).scale(0.9).shift(UP)
        self.play(domain_elements.animate.shift(UP*0.4),
                  FadeIn(domain_element_4))
        self.play(Create(arrows))
        self.wait(2)
        self.play(FadeIn(t_2))
        self.wait(2)
        
        indicative_arrow_1.shift(UP*2.1)
        self.play(FadeIn(indicative_arrow_1))
        self.play(indicative_arrow_1.animate.shift(DOWN*2.1))
        self.play(FadeOut(indicative_arrow_1))
        self.wait(2)
        self.play(LaggedStart(
            Flash(domain_element_1, num_lines = 8),
            Flash(domain_element_2, num_lines = 8),
            Flash(domain_element_3, num_lines = 8),
            Flash(domain_element_4, num_lines = 8),
            lag_ratio = 0.3))
        self.wait(2)
                
        self.wait(2)
        self.play(LaggedStart(
            Indicate(arrow_1, scale_factor = 1.05),
            Indicate(arrow_2, scale_factor = 1.05),
            Indicate(arrow_3, scale_factor = 1.05),
            Indicate(arrow_4, scale_factor = 1.05),
            lag_ratio = 0.4))
        self.wait(2)
        self.play(TransformMatchingShapes(t_2, function))
        self.wait(2)



# Elementos sobrando no Contradomínio e conjunto Imagem
class vid8(Scene):
    def construct(self):

        # Retomando a definição e o diagrama
            # Definição
                                         # 0            1         2         3         4                  5                         6             7      8       9             10                11        12     13      
        function_definition = Tex(r'\it Uma função ',r'$f:\:$',r'$A$',r'$\:\to\:$',r'$B$',r' é uma relação que associa ',r'\\ cada elemento ',r'$x$',r' de ',r'$A$',r' a um único elemento ',r'$f(x)$',r' de ',r'$B$').scale(0.95).shift(UP*2.7)
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
        codomain_elements = VGroup(codomain_element_1, codomain_element_2, codomain_element_3, codomain_element_4).set_z_index(2)
                # Setas
        function = MathTex(r'f').scale(1.2).shift(UP*2.3)

        arrow_1 = CurvedArrow((-2.2, 1.2, 0), (2.2, 1.2, 0), radius = -5, stroke_width = 2.5)
        arrow_2 = CurvedArrow((-2.2, 0.4, 0), (2.2, 0.4, 0), radius = -5, stroke_width = 2.5)
        arrow_3 = CurvedArrow((-2.2, -0.4, 0), (2.2, -0.4, 0), radius = -5, stroke_width = 2.5)
        arrow_4 = CurvedArrow((-2.2, -1.1, 0), (2.2, -0.4, 0), radius = -5, stroke_width = 2.5)
        arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4).set_z_index(2)

        g_diagram = VGroup(domain, domain_label_1, domain_elements,
                           codomain, codomain_label_1, codomain_elements,
                           function, arrows).scale(0.9).shift(DOWN*1.2)

        self.add(function_definition, g_diagram)
        self.wait(2)

        # Indicar elemento sobrando no Contradomínio
        indicative_arrow_1 = Arrow(DOWN, UP*0.5, color = YELLOW).rotate(60*DEGREES).shift(DOWN*2.3+RIGHT*3)
        self.play(FadeIn(indicative_arrow_1))
        self.wait(2)
        self.play(FadeOut(indicative_arrow_1))
        self.wait(2)

        # Conjunto Imagem
        indicative_brace_1_ref = Line((2.4, 0.1, 0), (2.4, -1.8, 0))
        indicative_brace_1 = Brace(indicative_brace_1_ref, RIGHT, color = YELLOW)
        self.play(FadeIn(indicative_brace_1))
        self.wait(2)
        self.play(FadeOut(indicative_brace_1))

        range = Ellipse(width = 2, height = 2.4, color = GREEN_D, fill_opacity = 0.3).move_to(codomain).shift(UP*0.4)
        self.play(DrawBorderThenFill(range), run_time = 2)
        self.wait(2)

        range_label_1_line_1 = Line((3, -0.8, 0), (3.8, 0, 0), color = range.get_color()).set_z_index(4)
        range_label_1_line_2 = Line((3, -0.8, 0), (3.8, 0, 0), color = BLACK, stroke_width = 8).move_to(range_label_1_line_1).scale(1.05).set_z_index(2)
        range_label_1_line = VGroup(range_label_1_line_1, range_label_1_line_2)

        range_label_1 = MathTex(r'Imagem', color = range.get_color()).shift(RIGHT*4.5+UP*0.3).set_z_index(4)
        self.play(FadeIn(range_label_1_line), Write(range_label_1))
        self.wait(2)

        range_label_2 = MathTex(r'Im',r'\subset','B').move_to(range_label_1, aligned_edge = LEFT).set_z_index(4)
        range_label_2[0].set_color(range.get_color())
        range_label_2[2].set_color(BLUE)
        self.play(ReplacementTransform(range_label_1, range_label_2[0]))
        self.wait(2)
        self.play(Write(range_label_2[1:3]))
        self.wait(2)

        # FadeOut geral
        black_rectangle = Rectangle(width = 10, height = 8, color = BLACK, fill_opacity = 1).scale(10).set_z_index(5)
        self.play(FadeIn(black_rectangle))
        self.wait(2)



# Gráfico
class vid9(MovingCameraScene):
    def construct(self):

        t_1 = Tex('\it Gráfico').scale(1.2).to_edge(UP, buff = 1)

        axes = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3)
        axes_labels = VGroup(x_label, y_label).set_color(YELLOW)
        axes_zero = MathTex('0').scale(0.8).next_to(axes, DL, buff = -0.7)

        plane = NumberPlane(x_range = [0, 5, 1],
                    y_range = [0, 4, 1],
                    x_length = 4,
                    y_length = 3).shift(UP*0.3+RIGHT*0.34).set_opacity(0.4)
        
        graph_1 = axes.plot(lambda x: x * 1/3 + np.sin(x + 4) + 1.3,
                            x_range=[0.5, 4], stroke_width = 7).set_color(BLUE).set_z_index(2)
        graph_1_label = MathTex('f', color = graph_1.get_color()).next_to(graph_1, UR, buff = 0.1).shift(DOWN*0.3)
        
        g_graph = VGroup(axes, axes_zero, axes_labels, plane, graph_1, graph_1_label)#.scale(1.1).shift(DOWN)

        # Construindo o plano cartesiano
        r_1 = NumberLine(x_range = [-1, 5, 1], length = 5, include_ticks = False, include_tip = True).shift(DOWN*5+RIGHT*2)
        r_2 = NumberLine(x_range = [-1, 4, 1], length = 4, include_ticks = False, include_tip = True).rotate(90*DEGREES).shift(LEFT*8+UP*2)
        g_r = VGroup(r_1, r_2)

        r_1_label = MathTex(r'\mathbb{R}').next_to(r_1, DR, buff = 0)
        r_2_label = MathTex(r'\mathbb{R}').next_to(r_2, UL, buff = 0)
        g_r_labels = VGroup(r_1_label, r_2_label)
       
        self.play(ReplacementTransform(g_r, axes),
                  r_1_label.animate.move_to(x_label.get_center()),
                  r_2_label.animate.move_to(y_label.get_center()),
                  run_time = 2)
        self.wait(2)

        # Interseção: origem
        origin_dot = Dot(axes.coords_to_point(0,0,0), color = YELLOW)
        origin_label = Tex('\it Origem', color = GRAY).next_to(axes, DL, buff = -3.5).shift(DOWN)
        origin_arrow = Arrow(origin_label, origin_dot, color = GRAY).set_opacity(0.7).scale(0.9).rotate(-5*DEGREES, about_point = axes.coords_to_point(0,0,0))
        self.play(GrowFromCenter(origin_dot))
        self.wait(2)
        self.play(origin_dot.animate.set_color(WHITE))
        self.play(FadeIn(origin_label, origin_arrow))
        self.wait(2)
        self.play(Write(axes_zero))
        self.wait(2)
        self.play(FadeOut(origin_label, origin_arrow))
        self.wait(2)
        
        # Sentido de crescimento dos eixos
        y_tip_ref = Dot(axes.coords_to_point(0,4.2,0), color = YELLOW)
        x_tip_ref = Dot(axes.coords_to_point(4.7,0,0), color = YELLOW)
        self.play(LaggedStart(
            Flash(x_tip_ref, num_lines = 8, flash_radius = 0.3),
            Flash(y_tip_ref, num_lines = 8, flash_radius = 0.3),
            lag_ratio = 0.5))
        self.wait(2)

            # Números do eixo x
        x_n0_label = MathTex('-1').scale(0.8).next_to(axes.coords_to_point(-1,0,0), DOWN, buff = 0.2)
        x_n0_tick = Line(DOWN*0.1, UP*0.1, stroke_width = 2).move_to(axes.coords_to_point(-1,0,0))
        x_n0 = VGroup(x_n0_label, x_n0_tick)

        x_n1_label = MathTex('1').scale(0.8).next_to(axes.coords_to_point(1,0,0), DOWN, buff = 0.2)
        x_n1_tick = Line(DOWN*0.1, UP*0.1, stroke_width = 2).move_to(axes.coords_to_point(1,0,0))
        x_n1 = VGroup(x_n1_label, x_n1_tick)

        x_n2_label = MathTex('2').scale(0.8).next_to(axes.coords_to_point(2,0,0), DOWN, buff = 0.2)
        x_n2_tick = Line(DOWN*0.1, UP*0.1, stroke_width = 2).move_to(axes.coords_to_point(2,0,0))
        x_n2 = VGroup(x_n2_label, x_n2_tick)

        x_n3_label = MathTex('3').scale(0.8).next_to(axes.coords_to_point(3,0,0), DOWN, buff = 0.2)
        x_n3_tick = Line(DOWN*0.1, UP*0.1, stroke_width = 2).move_to(axes.coords_to_point(3,0,0))
        x_n3 = VGroup(x_n3_label, x_n3_tick)

        x_n4_label = MathTex('4').scale(0.8).next_to(axes.coords_to_point(4,0,0), DOWN, buff = 0.2)
        x_n4_tick = Line(DOWN*0.1, UP*0.1, stroke_width = 2).move_to(axes.coords_to_point(4,0,0))
        x_n4 = VGroup(x_n4_label, x_n4_tick)

        x_numbers = VGroup(x_n0, x_n1, x_n2, x_n3, x_n4).set_z_index(3)
        self.play(Write(x_numbers), run_time = 1.5)
        self.wait(2)

            # Números do eixo y
        y_n0_label = MathTex('-1').scale(0.8).next_to(axes.coords_to_point(0,-1,0), LEFT, buff = 0.2)
        y_n0_tick = Line(LEFT*0.1, RIGHT*0.1, stroke_width = 2).move_to(axes.coords_to_point(0,-1,0))
        y_n0 = VGroup(y_n0_label, y_n0_tick)

        y_n1_label = MathTex('1').scale(0.8).next_to(axes.coords_to_point(0,1,0), LEFT, buff = 0.2)
        y_n1_tick = Line(LEFT*0.1, RIGHT*0.1, stroke_width = 2).move_to(axes.coords_to_point(0,1,0))
        y_n1 = VGroup(y_n1_label, y_n1_tick)

        y_n2_label = MathTex('2').scale(0.8).next_to(axes.coords_to_point(0,2,0), LEFT, buff = 0.2)
        y_n2_tick = Line(LEFT*0.1, RIGHT*0.1, stroke_width = 2).move_to(axes.coords_to_point(0,2,0))
        y_n2 = VGroup(y_n2_label, y_n2_tick)

        y_n3_label = MathTex('3').scale(0.8).next_to(axes.coords_to_point(0,3,0), LEFT, buff = 0.2)
        y_n3_tick = Line(LEFT*0.1, RIGHT*0.1, stroke_width = 2).move_to(axes.coords_to_point(0,3,0))
        y_n3 = VGroup(y_n3_label, y_n3_tick)

        y_n4_label = MathTex('4').scale(0.8).next_to(axes.coords_to_point(0,4,0), LEFT, buff = 0.2)
        y_n4_tick = Line(LEFT*0.1, RIGHT*0.1, stroke_width = 2).move_to(axes.coords_to_point(0,4,0))
        y_n4 = VGroup(y_n4_label, y_n4_tick)

        y_numbers = VGroup(y_n0, y_n1, y_n2, y_n3, y_n4).set_z_index(3)
        self.play(Write(y_numbers), run_time = 1.5)
        self.wait(2)

        # Nomes dos eixos x e y
        self.play(ReplacementTransform(r_1_label, x_label))
        self.play(x_label.animate.set_color(WHITE))
        self.wait(2)
        self.play(ReplacementTransform(r_2_label, y_label))
        self.play(y_label.animate.set_color(WHITE))
        self.wait(2)

        # Plano composto de infinitos pontos
        dots = VGroup(*[Dot().scale(0.5) for i in range(120)])
        dots.arrange_in_grid(cols = 12).move_to(axes.coords_to_point(2.5,2.2,0)).shift(RIGHT*0.1)
        self.play(Create(dots))
        self.wait(2)

        # Ponto = (x,y)
        dot_1 = Dot(axes.coords_to_point(2.5,2.2,0))
        dot_1_label = MathTex('(','x',',','y',')').scale(0.9).next_to(dot_1, UR, buff = 0.05)
        self.play(FadeOut(dots))
        self.play(GrowFromCenter(dot_1))
        self.wait(2)
        self.play(Write(dot_1_label))
        self.wait(2)

            # Coordenada x
        x_coord_dashed_line = DashedLine(dot_1, axes.coords_to_point(2.5,0,0), color = YELLOW).set_z_index(-1)
        self.play(dot_1_label[1].animate.set_color(YELLOW))
        self.wait(2)
        self.play(Create(x_coord_dashed_line))
        
        x_coord_axis_label = MathTex('x', color = YELLOW).scale(0.9).next_to(x_coord_dashed_line, DOWN, buff = 0.13)
        self.play(GrowFromCenter(x_coord_axis_label),
                  x_numbers.animate.set_opacity(0.3))
        self.wait(2)
        self.play(dot_1_label[1].animate.set_color(WHITE),
                  x_coord_dashed_line.animate.set_color(WHITE),
                  x_coord_axis_label.animate.set_color(WHITE))
        self.wait(2)

            # Coordenada y
        y_coord_dashed_line = DashedLine(dot_1, axes.coords_to_point(0,2.2,0), color = YELLOW).set_z_index(-1)
        self.play(dot_1_label[3].animate.set_color(YELLOW))
        self.wait(2)
        self.play(Create(y_coord_dashed_line))
        
        y_coord_axis_label = MathTex('y', color = YELLOW).scale(0.9).next_to(y_coord_dashed_line, LEFT, buff = 0.13)
        self.play(GrowFromCenter(y_coord_axis_label),
                  y_numbers.animate.set_opacity(0.3),
                  axes_zero.animate.set_opacity(0.3))
        self.wait(2)
        self.play(dot_1_label[3].animate.set_color(WHITE),
                  y_coord_dashed_line.animate.set_color(WHITE),
                  y_coord_axis_label.animate.set_color(WHITE))
        self.wait(2)
        self.play(FadeOut(dot_1, dot_1_label,
                          x_coord_dashed_line, x_coord_axis_label,
                          y_coord_dashed_line, y_coord_axis_label),
                          x_numbers.animate.set_opacity(1),
                          y_numbers.animate.set_opacity(1),
                          axes_zero.animate.set_opacity(1))
        self.wait(2)

        # Exemplo: ponto (3,2)
        dot_2 = Dot(axes.coords_to_point(4,2,0), color = YELLOW)
        dot_2_label = MathTex('(','4',',','2',')').scale(0.8)
        self.play(FadeIn(dot_2_label))
        self.wait(2)
        self.play(dot_2_label.animate.shift(RIGHT*2.3+UP*0.5),
                  GrowFromCenter(dot_2))
        self.play(dot_2.animate.set_color(WHITE))
        self.wait(2)

        x2_coord_dashed_line = DashedLine(dot_2, axes.coords_to_point(4,0,0), color = YELLOW).set_z_index(-1)
        self.play(Create(x2_coord_dashed_line))
        self.wait(2)
        self.play(x_n4.animate.set_color(YELLOW))
        self.play(x2_coord_dashed_line.animate.set_color(WHITE),
                  x_n4.animate.set_color(WHITE))
        self.wait(2)

        y2_coord_dashed_line = DashedLine(dot_2, axes.coords_to_point(0,2,0), color = YELLOW).set_z_index(-1)
        self.play(Create(y2_coord_dashed_line))
        self.wait(2)
        self.play(y_n2.animate.set_color(YELLOW))
        self.play(y2_coord_dashed_line.animate.set_color(WHITE),
                  y_n2.animate.set_color(WHITE))
        self.wait(2)

        # Ponto associa dois números: x ---> y
        self.play(FadeOut(x2_coord_dashed_line, y2_coord_dashed_line))
        self.wait(2)

        arrow_4_to_2_1 = Line(axes.coords_to_point(4,0,0), dot_2, buff = 0, stroke_width = 5)
        arrow_4_to_2_2 = Arrow(dot_2, axes.coords_to_point(0.1,2,0), buff = 0, stroke_width = 5, tip_length = 0.2)
        arrow_4_to_2 = VGroup(arrow_4_to_2_1, arrow_4_to_2_2).set_color(GRAY).set_opacity(0.5).set_z_index(-1)
        self.play(Create(arrow_4_to_2), run_time = 2)
        self.wait(2)

        dot_2_label_2 = MathTex('(','x',',','y',')', color = YELLOW).scale(0.8).move_to(dot_2_label)
        
        x_n4_2_label = MathTex('x', color = YELLOW).scale(0.8).next_to(axes.coords_to_point(4,0,0), DOWN, buff = 0.2)
        x_n4_2_tick = Line(DOWN*0.1, UP*0.1, stroke_width = 2).move_to(axes.coords_to_point(4,0,0))
        x_n4_2 = VGroup(x_n4_2_label, x_n4_2_tick)

        y_n2_2_label = MathTex('y', color = YELLOW).scale(0.8).next_to(axes.coords_to_point(0,2,0), LEFT, buff = 0.2)
        y_n2_2_tick = Line(LEFT*0.1, RIGHT*0.1, stroke_width = 2).move_to(axes.coords_to_point(0,2,0))
        y_n2_2 = VGroup(y_n2_2_label, y_n2_2_tick)

        self.play(ReplacementTransform(dot_2_label[1], dot_2_label_2[1]),
                  ReplacementTransform(x_n4, x_n4_2),
                  FadeOut(x_n0, x_n1, x_n2, x_n3))
        self.wait(2)
        self.play(dot_2_label_2[1].animate.set_color(WHITE),
                  x_n4_2.animate.set_color(WHITE))
        self.wait(2)

        self.play(ReplacementTransform(dot_2_label[3], dot_2_label_2[3]),
                  ReplacementTransform(y_n2, y_n2_2),
                  FadeOut(y_n0, y_n1, y_n3, y_n4))
        self.wait(2)
        self.play(dot_2_label_2[3].animate.set_color(WHITE),
                  y_n2_2.animate.set_color(WHITE))
        self.wait(2)

        # Tudo vai para baixo
        self.play(self.camera.frame.animate.shift(UP))

        # Função também associa dois números: x ---> f(x)
        function_f = MathTex('f', color = BLUE).shift(UP*0.7)
        function_x_to_fx = MathTex('x',r'\longmapsto','f(x)').shift(RIGHT*0.35)
        g_f = VGroup(function_f, function_x_to_fx).shift(UP*3.5)
        self.play(FadeIn(function_f))
        self.wait(2)
        self.play(Write(function_x_to_fx[0]))
        self.wait(2)
        self.play(GrowFromEdge(function_x_to_fx[1], LEFT))
        self.play(FadeIn(function_x_to_fx[2]))
        self.wait(2)
        
        self.play(FadeOut(dot_2,
                          dot_2_label[0], dot_2_label[2], dot_2_label[4],
                          dot_2_label_2[1], dot_2_label_2[3],
                          x_n4_2, y_n2_2,
                          arrow_4_to_2))
        
        # Representar função como pontos
            # Pontos em cima do graph_1
        function_dot_1 = Dot(graph_1.get_point_from_function(t = 0.5)).scale(0.8)
        function_dot_2 = Dot(graph_1.get_point_from_function(t = 1.1)).scale(0.8)
        function_dot_3 = Dot(graph_1.get_point_from_function(t = 1.6)).scale(0.8)
        function_dot_4 = Dot(graph_1.get_point_from_function(t = 2.05)).scale(0.8)
        function_dot_5 = Dot(graph_1.get_point_from_function(t = 2.5)).scale(0.8)
        function_dot_6 = Dot(graph_1.get_point_from_function(t = 2.9)).scale(0.8)
        function_dot_7 = Dot(graph_1.get_point_from_function(t = 3.4)).scale(0.8)
        function_dot_8 = Dot(graph_1.get_point_from_function(t = 4)).scale(0.8)
        function_dots = VGroup(function_dot_1, function_dot_2,
                               function_dot_3, function_dot_4,
                               function_dot_5, function_dot_6,
                               function_dot_7, function_dot_8).set_color(BLUE).set_z_index(2)
        self.play(LaggedStart(
            FadeIn(function_dot_1), FadeIn(function_dot_2),
            FadeIn(function_dot_3), FadeIn(function_dot_4),
            FadeIn(function_dot_5), FadeIn(function_dot_6),
            FadeIn(function_dot_7), FadeIn(function_dot_8),
            lag_ratio = 0.1))
        self.wait(2)

            # Reta numérica simulando o eixo x
        number_line_x = NumberLine(x_range = [-1, 5, 1], length = 5, include_ticks =  False, color = YELLOW, stroke_width = 1).next_to(axes, DOWN,  buff = -0.82).set_z_index(-1)
        self.add(number_line_x)

            # Reta numérica simulando o eixo y
        number_line_y = NumberLine(x_range = [-1, 4, 1], length = 4, include_ticks =  False, color = YELLOW, stroke_width = 1).rotate(90*DEGREES).next_to(axes, LEFT,  buff = -0.83).set_z_index(-1)
        self.add(number_line_x)

            # Seta ligando x ---> f(x)
        dot_ref = Dot(axes.coords_to_point(2.5, 2.3485, 0), color = BLACK).scale(0.0001).set_z_index(-2)

        arrow_x_to_fx_1 = Line((dot_ref.get_x(), number_line_x.get_y(), 0), dot_ref,
                               buff = 0, stroke_width = 5, color = GRAY).set_opacity(0.5)
        arrow_x_to_fx_1.add_updater(lambda m: m.become(Line((dot_ref.get_x(), number_line_x.get_y(), 0), dot_ref,
                               buff = 0, stroke_width = 5, color = GRAY).set_opacity(0.5)))
        
        arrow_x_to_fx_2 = Arrow(dot_ref, (number_line_y.get_x() + 0.1, dot_ref.get_y(), 0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)
        arrow_x_to_fx_2.add_updater(lambda m: m.become(Arrow(dot_ref, (number_line_y.get_x() + 0.1, dot_ref.get_y(), 0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)))

        arrow_x_to_fx = VGroup(arrow_x_to_fx_1, arrow_x_to_fx_2).set_z_index(1)

            # Par ordenado (x,f(x))
        function_dot_pair = MathTex('(x,f(x))').scale(0.8).next_to(arrow_x_to_fx_1, UR).shift(DOWN*0.5)

            # x e f(x) nos eixos
        function_dot_x_coord_label = MathTex('x').scale(0.9).next_to(arrow_x_to_fx_1, DOWN, buff = 0.2)
        function_dot_x_coord_tick = Line(DOWN*0.1, UP*0.1, stroke_width = 2).next_to(arrow_x_to_fx_1, DOWN, buff = -0.1)
        function_dot_x_coord = VGroup(function_dot_x_coord_label, function_dot_x_coord_tick)

        function_dot_fx_coord_tick = Line(LEFT*0.1, RIGHT*0.1, stroke_width = 2).next_to(arrow_x_to_fx_2, LEFT, buff = 0)
        function_dot_fx_coord_label = MathTex('f(x)').scale(0.8).next_to(function_dot_fx_coord_tick, LEFT, buff = 0.1)
        function_dot_fx_coord = VGroup(function_dot_fx_coord_label, function_dot_fx_coord_tick)

        self.play(FadeIn(function_dot_x_coord))
        function_dot_x_coord_label.add_updater(lambda m: m.become(MathTex('x').scale(0.9).next_to(arrow_x_to_fx_1, DOWN, buff = 0.2)))
        function_dot_x_coord_tick.add_updater(lambda m: m.become(Line(DOWN*0.1, UP*0.1, stroke_width = 2).next_to(arrow_x_to_fx_1, DOWN, buff = -0.1)))
        self.wait(2)
        self.play(Create(arrow_x_to_fx), run_time = 1.5)
        self.wait(2)
        self.play(FadeIn(function_dot_fx_coord))
        function_dot_fx_coord_label.add_updater(lambda m: m.become(MathTex('f(x)').scale(0.8).next_to(function_dot_fx_coord_tick, LEFT, buff = 0.1)))
        function_dot_fx_coord_tick.add_updater(lambda m: m.become(Line(LEFT*0.1, RIGHT*0.1, stroke_width = 2).next_to(arrow_x_to_fx_2, LEFT, buff = 0)))
        self.wait(2)
        self.play(FadeIn(function_dot_pair))
        function_dot_pair.add_updater(lambda m: m.become(MathTex('(x,f(x))').scale(0.8).next_to(arrow_x_to_fx_1, UR).shift(DOWN*0.5)))
        self.wait(2)        

            # Ponto anda para trás no gráfico até o início
        graph_1_aux_1 = axes.plot(lambda x: x * 1/3 + np.sin(x + 4) + 1.3,
                            x_range=[0.5, 2.5]).set_color(BLUE).set_z_index(2)
        graph_1_aux_1.reverse_points()
        self.play(MoveAlongPath(dot_ref, graph_1_aux_1), run_time = 2.1)

            # Ponto percorre todo o gráfico
        self.play(MoveAlongPath(dot_ref, graph_1), run_time = 2)

            # Ponto anda para trás no gráfico até o meio
        graph_1_aux_2 = axes.plot(lambda x: x * 1/3 + np.sin(x + 4) + 1.3,
                            x_range=[2.5, 4]).set_color(BLUE).set_z_index(2)
        graph_1_aux_2.reverse_points()
        self.play(MoveAlongPath(dot_ref, graph_1_aux_2), run_time = 1.5)
        self.wait(2)
        
        # Adicionando mais pontos até virar uma curva
            # Definindo mais pontos do gráfico
        function_dot_9 = Dot(graph_1.get_point_from_function(t = 0.9)).scale(0.8)
        function_dot_10 = Dot(graph_1.get_point_from_function(t = 1.3)).scale(0.8)
        function_dot_11 = Dot(graph_1.get_point_from_function(t = 1.8)).scale(0.8)
        function_dot_12 = Dot(graph_1.get_point_from_function(t = 2.3)).scale(0.8)
        function_dot_13 = Dot(graph_1.get_point_from_function(t = 2.7)).scale(0.8)
        function_dot_14 = Dot(graph_1.get_point_from_function(t = 3.05)).scale(0.8)
        function_dot_15 = Dot(graph_1.get_point_from_function(t = 3.8)).scale(0.8)
        function_dots_2 = VGroup(function_dot_9,
                                 function_dot_10, function_dot_11,
                                 function_dot_12, function_dot_13,
                                 function_dot_14, function_dot_15).set_color(BLUE_D).set_z_index(3)
        self.play(Create(function_dots_2), run_time = 1.2)
        self.wait(2)

        function_dot_16 = Dot(graph_1.get_point_from_function(t = 0.7)).scale(0.8)
        function_dot_17 = Dot(graph_1.get_point_from_function(t = 1.4)).scale(0.8)
        function_dot_18 = Dot(graph_1.get_point_from_function(t = 1.9)).scale(0.8)
        function_dot_19 = Dot(graph_1.get_point_from_function(t = 2.2)).scale(0.8)
        function_dot_20 = Dot(graph_1.get_point_from_function(t = 2.7)).scale(0.8)
        function_dot_21 = Dot(graph_1.get_point_from_function(t = 3.2)).scale(0.8)
        function_dot_22 = Dot(graph_1.get_point_from_function(t = 3.6)).scale(0.8)
        function_dots_3 = VGroup(function_dot_16, function_dot_17,
                                 function_dot_18, function_dot_19,
                                 function_dot_20, function_dot_21,
                                 function_dot_22).set_color(BLUE_E).set_z_index(2)
        self.play(Create(function_dots_3))
        self.wait(2)

            # Todos os pontos viram a curva do gráfico
        g_all_dots = VGroup(function_dots, function_dots_2, function_dots_3)
        self.play(FadeTransform(g_all_dots, graph_1), run_time = 1.5)
        self.wait(2)

        graphic_text_1 = Tex('\it Gráfico de f', color = BLUE).scale(0.9).next_to(function_dot_8, RIGHT, buff = 0.2)
        graphic_text_2 = Tex(r'\it $G_{f}$', color = BLUE).scale(0.9).move_to(graphic_text_1, aligned_edge = LEFT)
        self.play(FadeIn(graphic_text_1))
        self.wait(2)
        self.play(ReplacementTransform(graphic_text_1, graphic_text_2))
        self.wait(2)
        
        arrow_x_to_fx_2_2 = Arrow(dot_ref, (number_line_y.get_x(), dot_ref.get_y(), 0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)

        self.play(FadeOut(function_dot_pair, function_dot_x_coord, function_dot_fx_coord),
                  ReplacementTransform(arrow_x_to_fx_2, arrow_x_to_fx_2_2))
        self.wait(2)

        # Encontrar domínio e imagem graficamente
            # Mais setas associando x ---> f(x) 
       
        arrow_1_1 = Line((function_dot_2.get_x(), number_line_x.get_y(), 0), function_dot_2.get_center(),
                               buff = 0, stroke_width = 5, color = GRAY).set_opacity(0.5)
        arrow_1_2 = Arrow(function_dot_2.get_center(), (number_line_y.get_x(), function_dot_2.get_y(), 0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)
        arrow_1 = VGroup(arrow_1_1, arrow_1_2).set_z_index(1)


        arrow_2_1 = Line((function_dot_3.get_x(), number_line_x.get_y(), 0), function_dot_3.get_center(),
                               buff = 0, stroke_width = 5, color = GRAY).set_opacity(0.5)
        arrow_2_2 = Arrow(function_dot_3.get_center(), (number_line_y.get_x(), function_dot_3.get_y(), 0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)
        arrow_2 = VGroup(arrow_2_1, arrow_2_2).set_z_index(1)


        arrow_3_1 = Line((function_dot_4.get_x(), number_line_x.get_y(), 0), function_dot_4.get_center(),
                               buff = 0, stroke_width = 5, color = GRAY).set_opacity(0.5)
        arrow_3_2 = Arrow(function_dot_4.get_center(), (number_line_y.get_x(), function_dot_4.get_y(), 0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)
        arrow_3 = VGroup(arrow_3_1, arrow_3_2).set_z_index(1)


        arrow_4_1 = Line((function_dot_6.get_x(), number_line_x.get_y(), 0), function_dot_6.get_center(),
                               buff = 0, stroke_width = 5, color = GRAY).set_opacity(0.5)
        arrow_4_2 = Arrow(function_dot_6.get_center(), (number_line_y.get_x(), function_dot_6.get_y(), 0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)
        arrow_4 = VGroup(arrow_4_1, arrow_4_2).set_z_index(1)


        arrow_5_1 = Line((function_dot_7.get_x(), number_line_x.get_y(), 0), function_dot_7.get_center(),
                               buff = 0, stroke_width = 5, color = GRAY).set_opacity(0.5)
        arrow_5_2 = Arrow(function_dot_7.get_center(), (number_line_y.get_x(), function_dot_7.get_y(), 0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)
        arrow_5 = VGroup(arrow_5_1, arrow_5_2).set_z_index(1)


        more_arrows_1 = VGroup(arrow_1_1, arrow_2_1, arrow_3_1, arrow_4_1, arrow_5_1)
        more_arrows_2 = VGroup(arrow_1_2, arrow_2_2, arrow_3_2, arrow_4_2, arrow_5_2)

        self.play(Create(more_arrows_1), run_time = 2)
        self.wait(2)
        self.play(Create(more_arrows_2), run_time = 2)
        self.wait(2)

            # Encontrar domínio
        domain_brace_ref = Line(function_dot_1, function_dot_8)
        domain_brace = Brace(domain_brace_ref, DOWN, buff = 0.8, color = RED)
        domain_brace_label = MathTex(r'D_{f}', color = domain_brace.get_color()).scale(0.8).next_to(domain_brace, DOWN)
        self.play(FadeIn(domain_brace, domain_brace_label))
        self.wait(2)

            # Projetar gráfico sobre o eixo x
        x_graph_proj = axes.get_area(graph = graph_1, color = RED, stroke_width = 0, fill_opacity = 0.05).set_z_index(-5)
        x_graph_proj_black = axes.get_area(graph = graph_1, color = BLACK).set_opacity(1).scale(1.05).set_z_index(-3)
        self.play(FadeOut(more_arrows_1, arrow_x_to_fx_1))
        self.wait(2)
        self.add(x_graph_proj_black, x_graph_proj)
        self.play(x_graph_proj_black.animate.shift(DOWN*5), run_time = 3)
        self.wait(2)

            # Intervalo do domínio
        domain_interval_dot_1 = Dot(number_line_x.number_to_point(0.5))
        domain_interval_dot_2 = Dot(number_line_x.number_to_point(4))
        domain_interval_line = Line(number_line_x.number_to_point(0.5), number_line_x.number_to_point(4), stroke_width = 10, stroke_opacity = 0.7)
        domain_interval = VGroup(domain_interval_dot_1,
                                 domain_interval_dot_2,
                                 domain_interval_line).set_color(domain_brace.get_color()).set_z_index(3)
        self.play(LaggedStart(
            GrowFromCenter(domain_interval_dot_1),
            Create(domain_interval_line),
            GrowFromCenter(domain_interval_dot_2),
            lag_ratio = 0.2))
        self.play(FadeOut(domain_brace))
        self.play(domain_brace_label.animate.shift(UP*0.6))
        self.wait(2)

            # Encontrar imagem 
        range_brace_ref = Line(number_line_y.number_to_point(0.27), number_line_y.number_to_point(3.6227))
        range_brace = Brace(range_brace_ref, LEFT, buff = 0.3, color = GREEN)
        range_brace_label = MathTex(r'Im_{f}', color = GREEN).scale(0.8).next_to(range_brace, LEFT)
        self.play(FadeIn(range_brace, range_brace_label))
        self.wait(2)

            # Projetar gráfico sobre o eixo y
        y_graph_proj_ref = Rectangle(width = 3.2, height = 2.57).move_to(graph_1, aligned_edge = UP).shift(LEFT*0.25)
        y_graph_proj = Difference(y_graph_proj_ref, x_graph_proj, stroke_opacity = 0, color = GREEN, fill_opacity = 0.3).set_z_index(-4)
        y_graph_proj_black = Difference(y_graph_proj, x_graph_proj, color = BLACK, fill_opacity = 1).scale(1.1).set_z_index(-3).shift(UP*0.05)

        y_graph_proj_black_rectangle = Rectangle(width = 3.5, height = 3.5, color = BLACK, fill_opacity = 1).move_to(x_graph_proj).set_z_index(-3)
        self.play(FadeOut(more_arrows_2, arrow_x_to_fx_2_2))
        self.wait(2)
        self.add(y_graph_proj_black, y_graph_proj)
        self.play(y_graph_proj_black.animate.shift(LEFT*4), run_time = 2)
        self.wait(2)

            # Intervalo da imagem
        range_interval_dot_1 = Dot(number_line_y.number_to_point(0.2))
        range_interval_dot_2 = Dot(number_line_y.number_to_point(3.44))
        range_interval_line = Line(number_line_y.number_to_point(0.2), number_line_y.number_to_point(3.44), stroke_width = 10, stroke_opacity = 0.7)
        range_interval = VGroup(range_interval_dot_1,
                                 range_interval_dot_2,
                                 range_interval_line).set_color(range_brace.get_color()).set_z_index(3)
        self.play(LaggedStart(
            GrowFromCenter(range_interval_dot_1),
            Create(range_interval_line),
            GrowFromCenter(range_interval_dot_2),
            lag_ratio = 0.2))
        self.play(FadeOut(range_brace))
        self.play(range_brace_label.animate.shift(RIGHT*0.6))
        self.wait(2)

            # Contradomínio: não pode ser encontrado graficamente, mas tem pelo menos o mesmo tamanho da imagem
        codomain_label_1 = MathTex(r'CD_{f}','?', color = ORANGE).scale(0.9).next_to(range_brace_label, UL, buff = 0.6)
        codomain_label_2 = MathTex(r'CD_{f}','\supset',r'Im_{f}').scale(0.8).move_to(range_brace_label, aligned_edge = RIGHT)
        codomain_label_2[0].set_color(codomain_label_1.get_color())
        codomain_label_2[2].set_color(range_brace_label.get_color())
        self.play(FadeIn(codomain_label_1[0]))
        self.wait(2)
        self.play(FadeIn(codomain_label_1[1]))
        self.wait(2)
        self.play(Indicate(range_interval, scale_factor = 1.1))
        self.wait(2)
        self.play(ReplacementTransform(codomain_label_1[0], codomain_label_2[0]),
                  FadeIn(codomain_label_2[1]),
                  FadeOut(codomain_label_1[1]))
        self.wait(2)



        # Imagem gráfico
        '''t_1.set_color(BLUE)
        axes_labels.set_color(WHITE)
        g = VGroup(axes, axes_labels, graph_1).shift(DOWN)
        self.add(g, t_1)'''


        
# Condição para que uma curva seja gráfico de função (Teste da Reta Vertical)
class vid10(MovingCameraScene):
    def construct(self):

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
                            x_range=[0.5, 4], stroke_width = 7).set_color(BLUE).set_z_index(2)
        function_dot_8 = Dot(graph_1.get_point_from_function(t = 4)).scale(0.8)
        graphic_text_1 = Tex('\it Gráfico de f', color = BLUE).scale(0.9).next_to(function_dot_8, RIGHT, buff = 0.2)
        graphic_text_2 = Tex(r'\it $G_{f}$', color = BLUE).scale(0.9).move_to(graphic_text_1, aligned_edge = LEFT)

        function_f = MathTex('f', color = BLUE).shift(UP*0.7)
        function_x_to_fx = MathTex('x',r'\longmapsto','f(x)').shift(RIGHT*0.35)
        g_f = VGroup(function_f, function_x_to_fx).shift(UP*3.5)

        self.add(axes, axes_labels, axes_zero, graph_1, graphic_text_2, g_f)
        self.wait(2)

        # Relembrando a definição de função
                                         # 0            1         2         3         4                  5                         6             7      8       9             10                11        12     13      
        function_definition = Tex(r'\it Uma função ',r'$f:\:$',r'$A$',r'$\:\to\:$',r'$B$',r' é uma relação que associa ',r'\\ cada elemento ',r'$x$',r' de ',r'$A$',r' a um único elemento ',r'$f(x)$',r' de ',r'$B$').scale(0.95).shift(UP*3.7)
        function_definition[2].set_color(RED)
        function_definition[4].set_color(BLUE)
        function_definition[7].set_color(RED)
        function_definition[9].set_color(RED)
        function_definition[11].set_color(BLUE)
        function_definition[13].set_color(BLUE)
        underline_func_def = Underline(function_definition[6:14], color = YELLOW)
        self.play(FadeOut(g_f))
        self.play(FadeIn(function_definition))
        self.wait(2)
        self.play(FadeIn(underline_func_def))
        self.wait(2)

        # Teste da reta vertical
        vert_line_test_text = Tex('\it Teste da Reta Vertical', color = YELLOW).move_to(function_definition)
        
        dot_intersection = Dot(graph_1.get_point_from_function(t = 2.5), color = YELLOW).set_z_index(4)
        vertical_line_1 = Line(UP, DOWN, color = dot_intersection.get_color(), stroke_opacity = 0.7).scale(2).move_to((dot_intersection.get_x(), 0, 0)).set_z_index(3)
        vertical_line_1.add_updater(lambda m: m.become(Line(UP, DOWN, color = dot_intersection.get_color(), stroke_opacity = 0.7).scale(2).move_to((dot_intersection.get_x(), 0, 0)).set_z_index(3)))
        self.play(Create(vertical_line_1))
        self.wait(2)
        self.play(GrowFromCenter(dot_intersection))
        self.wait(2)
        
        arrow_x_to_fx = Arrow(dot_intersection.get_center(), axes.coords_to_point(0.1, dot_intersection.get_y()+1.86, 0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)

        x_dot = Dot(axes.coords_to_point(2.5,0,0)).set_z_index(4)
        y_dot = Dot(axes.coords_to_point(0,2.3485,0)).set_z_index(4)
        indicative_arrow = Arrow(DOWN, UP*0.5, color = YELLOW).rotate(135*DEGREES).shift(DOWN*0.6+RIGHT*1)

        self.play(GrowFromCenter(x_dot), Flash(x_dot, num_lines = 8))
        self.wait(2)
        self.play(Create(arrow_x_to_fx))
        self.wait(2)
        self.play(GrowFromCenter(y_dot), Flash(y_dot, num_lines = 8))
        self.wait(2)
        self.play(FadeOut(x_dot, y_dot, arrow_x_to_fx))
        self.wait(2)
        self.play(FadeOut(function_definition, underline_func_def))
        self.play(FadeIn(vert_line_test_text))
        
        graph_1_aux_1 = axes.plot(lambda x: x * 1/3 + np.sin(x + 4) + 1.3,
                            x_range=[0.5, 2.5], stroke_width = 7).set_color(BLUE).set_z_index(2)
        graph_1_aux_1.reverse_points()
        self.play(MoveAlongPath(dot_intersection, graph_1_aux_1), run_time = 1.5)
        self.play(MoveAlongPath(dot_intersection, graph_1), run_time = 4)
        self.wait(2)

        # Mostrando curvas que são gráficos de funções e uma curva que não é
        its_graph_text = Tex('É gráfico de função', color = GREEN).scale(0.8).shift(UP*2.7)
        not_graph_text = Tex('Não gráfico de função', color = RED).scale(0.8).shift(UP*2.7)
        
            # É gráfico de função
        self.play(FadeIn(its_graph_text))
        self.wait(2)
        self.remove(its_graph_text, graph_1, graphic_text_2, vertical_line_1, dot_intersection)
        self.wait(2)
        
            # Também é gráfico de função
        graph_2 = axes.plot(lambda x: np.sin(x * 3) + 2,
                            x_range=[-0.5, 4.7], stroke_width = 7).set_color(BLUE).set_z_index(2)
        self.play(Create(graph_2))
        self.wait(2)

        dot_intersection_2 = Dot(graph_2.get_point_from_function(t = -0.5), color = YELLOW).set_z_index(4)
        vertical_line_2 = Line(UP, DOWN, color = dot_intersection_2.get_color(), stroke_opacity = 0.7).scale(2).move_to((dot_intersection_2.get_x(), 0, 0)).set_z_index(3)
        vertical_line_2.add_updater(lambda m: m.become(Line(UP, DOWN, color = dot_intersection_2.get_color(), stroke_opacity = 0.7).scale(2).move_to((dot_intersection_2.get_x(), 0, 0)).set_z_index(3)))
        
        self.play(Create(vertical_line_2),GrowFromCenter(dot_intersection_2))
        self.play(LaggedStart(
            MoveAlongPath(dot_intersection_2, graph_2),
            FadeIn(its_graph_text),
            lag_ratio = 0.3), run_time = 4.5)
        self.wait(2)
        self.remove(its_graph_text, graph_2, vertical_line_2, dot_intersection_2)
        self.wait(2)

            # Não é gráfico de função
        graph_3_1 = axes.plot(lambda x: np.sin(x - 1.3) + 2,
                            x_range=[-1, 2.96], stroke_width = 7).set_color(BLUE).set_z_index(2)
        graph_3_2 = ArcBetweenPoints((1,1.5,0), (1,0,0),
                                angle = -180*DEGREES, stroke_width = 7, color = BLUE).set_z_index(3).shift(DOWN*0.48+LEFT*0.2)
        graph_3 = VGroup(graph_3_1, graph_3_2)
        self.play(Create(graph_3_1), rate_func = rush_into)
        self.play(Create(graph_3_2), rate_func = rush_from)
        self.wait(2)

        dot_intersection_3 = Dot(graph_3_1.get_point_from_function(t = -1), color = YELLOW).set_z_index(4)
        vertical_line_3 = Line(UP, DOWN, color = dot_intersection_3.get_color(), stroke_opacity = 0.7).scale(2).move_to((dot_intersection_3.get_x(), 0, 0)).set_z_index(3)
        vertical_line_3.add_updater(lambda m: m.become(Line(UP, DOWN, color = dot_intersection_3.get_color(), stroke_opacity = 0.7).scale(2).move_to((dot_intersection_3.get_x(), 0, 0)).set_z_index(3)))

        dot_intersection_4_ref = ArcBetweenPoints((1,1.5,0), (1,0,0),
                                angle = -180*DEGREES, stroke_width = 7, color = BLUE).set_z_index(3).shift(DOWN*0.48+LEFT*0.2)
        dot_intersection_4_ref.reverse_points()        
        dot_intersection_4 = Dot(color = YELLOW).set_z_index(4)

        self.play(Create(vertical_line_3),GrowFromCenter(dot_intersection_3))
        self.play(MoveAlongPath(dot_intersection_3, graph_3_1), run_time = 2, rate_func = rush_into)
        self.play(MoveAlongPath(dot_intersection_3, graph_3_2),
                  MoveAlongPath(dot_intersection_4, dot_intersection_4_ref),
                  run_time = 2, rate_func = rush_from)
        self.play(FadeIn(not_graph_text))
        self.wait(2)

            # Setas indicando que um x está associado a dois y
        x_dot_2 = Dot(axes.coords_to_point(2.96,0,0))
        y_dot_2_1 = Dot(axes.coords_to_point(0,2.996,0))
        y_dot_2_2 = Dot((y_dot_2_1.get_x(), dot_intersection_3.get_y(), 0))

        arrow_x_to_fx_2 = Arrow(dot_intersection_4.get_center(), y_dot_2_1,
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)
        arrow_x_to_fx_3 = Arrow(dot_intersection_3.get_center(), y_dot_2_2,
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)

        indicative_arrow_2 = Arrow(DOWN, UP*0.5, color = YELLOW).rotate(-135*DEGREES).shift(DOWN*0.6+RIGHT*0.2)
        self.play(GrowFromCenter(x_dot_2), 
                  Flash(x_dot_2, num_lines = 8))
        self.play(Create(arrow_x_to_fx_2),
                  Create(arrow_x_to_fx_3))
        self.play(GrowFromCenter(y_dot_2_1),
                  GrowFromCenter(y_dot_2_2),
                  Flash(y_dot_2_2, num_lines = 8),
                  Flash(y_dot_2_1, num_lines = 8))
        self.wait(2)
        self.remove(not_graph_text, graph_3)
        self.wait(2)



# Gráfico da função-exemplo da área do retângulo
class vid11(MovingCameraScene):
    def construct(self):

        self.camera.frame.shift(UP*2)

        rectangle = Rectangle(width = 3, height = 2, color = BLUE, fill_opacity = 0.2)
        base = Brace(rectangle, DOWN, color = RED)
        base_label_1 = MathTex('x', color = base.get_color()).next_to(base, DOWN, buff = 0.3)
        height = Brace(rectangle, LEFT, color = WHITE)
        height_label = MathTex('2').next_to(height, LEFT)
        g_rectangle = VGroup(rectangle, base, height, height_label, base_label_1).shift(UP)

        t_1 = MathTex(r'f:',r'\mathbb{R}_{+}',r'\to',r'\mathbb{R}_{+}',r'\:\:,\:\:',r'f(',r'x',r') =',r'2x').shift(UP*3)
        t_1_copy = MathTex(r'f:',r'\mathbb{R}_{+}',r'\to',r'\mathbb{R}_{+}',r'\:\:,\:\:',r'f(',r'x',r') =',r'2x').shift(UP*3)
        self.play(FadeIn(t_1, g_rectangle))
        self.wait(2)
        self.play(self.camera.frame.animate.shift(DOWN*2),
                  FadeOut(g_rectangle), run_time = 1.5)
        self.wait(2)

        # Gráfico
            # Eixos
        axes = Axes(x_range = [-3, 4, 1],
                    y_range = [-3, 7, 1],
                    x_length = 7,
                    y_length = 8,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes.coords_to_point(4,0,0), DR, buff = 0.2)
        y_label = MathTex("y").next_to(axes.coords_to_point(0,7,0), UL, buff = 0.2).shift(DOWN*0.2)
        axes_labels = VGroup(x_label, y_label)
        axes_zero = MathTex('0', color = YELLOW).scale(0.8).next_to(axes.coords_to_point(0,0,0), DL, buff = 0.2)
        g_axes = VGroup(axes, axes_labels, axes_zero).scale(0.9).shift(DOWN*1.7+LEFT)

        black_rectangle_1 = Rectangle(width = 5, height = 0.25).to_edge(DOWN, buff = 0)
        black_rectangle_2 = Rectangle(width = 3, height = 2).to_edge(DOWN, buff = 0).shift(LEFT*4)
        black_rectangles = VGroup(black_rectangle_1, black_rectangle_2).set_color(BLACK).set_fill(opacity = 1).set_z_index(5)
        self.add(black_rectangles)

        self.play(FadeIn(axes, axes_labels))
        self.wait(2)

        #self.add(t_1, g_axes)

            # Encontrando pontos do gráfico
                # Labels das coordenadas nos eixos
        axes_x1_label = MathTex('1', color = YELLOW).scale(0.8).next_to(axes.coords_to_point(1,0,0), DOWN, buff = 0.2)
        axes_x1_tick = Line(DOWN*0.1, UP*0.1, stroke_width = 2).move_to(axes.coords_to_point(1,0,0))
        axes_x1 = VGroup(axes_x1_label, axes_x1_tick)
        
        axes_x2_label = MathTex('2', color = YELLOW).scale(0.8).next_to(axes.coords_to_point(2,0,0), DOWN, buff = 0.2)
        axes_x2_tick = Line(DOWN*0.1, UP*0.1, stroke_width = 2).move_to(axes.coords_to_point(2,0,0))
        axes_x2 = VGroup(axes_x2_label, axes_x2_tick)

        axes_x3_label = MathTex('3', color = YELLOW).scale(0.8).next_to(axes.coords_to_point(3,0,0), DOWN, buff = 0.2)
        axes_x3_tick = Line(DOWN*0.1, UP*0.1, stroke_width = 2).move_to(axes.coords_to_point(3,0,0))
        axes_x3 = VGroup(axes_x3_label, axes_x3_tick)

        axes_y1_label = MathTex('2', color = YELLOW).scale(0.8).next_to(axes.coords_to_point(0,2,0), LEFT, buff = 0.2)
        axes_y1_tick = Line(LEFT*0.1, RIGHT*0.1, stroke_width = 2).move_to(axes.coords_to_point(0,2,0))
        axes_y1 = VGroup(axes_y1_label, axes_y1_tick)

        axes_y2_label = MathTex('4', color = YELLOW).scale(0.8).next_to(axes.coords_to_point(0,4,0), LEFT, buff = 0.2)
        axes_y2_tick = Line(LEFT*0.1, RIGHT*0.1, stroke_width = 2).move_to(axes.coords_to_point(0,4,0))
        axes_y2 = VGroup(axes_y2_label, axes_y2_tick)

        axes_y3_label = MathTex('6', color = YELLOW).scale(0.8).next_to(axes.coords_to_point(0,6,0), LEFT, buff = 0.2)
        axes_y3_tick = Line(LEFT*0.1, RIGHT*0.1, stroke_width = 2).move_to(axes.coords_to_point(0,6,0))
        axes_y3 = VGroup(axes_y3_label, axes_y3_tick)

        axes_numbers = VGroup(axes_x1, axes_x2, axes_x3,
                              axes_y1, axes_y2, axes_y3).set_color(YELLOW).set_z_index(2)

                # x = 0
        dot_x0 = Dot(axes.coords_to_point(0,0,0), color = YELLOW)
        
        t_1_x0 = MathTex(r'f:',r'\mathbb{R}_{+}',r'\to',r'\mathbb{R}_{+}',r'\:\:,\:\:',r'f(',r'0',r') =',r'2 \cdot 0').move_to(t_1, aligned_edge = LEFT)
        t_1_x0[6].set_color(YELLOW)
        t_1_x0[8].set_color(YELLOW)
        self.play(ReplacementTransform(t_1[6], t_1_x0[6]),
                  ReplacementTransform(t_1[8], t_1_x0[8]),
                  FadeIn(axes_zero))
        self.wait(2)

        t_1_x0_2 = MathTex(r'f:',r'\mathbb{R}_{+}',r'\to',r'\mathbb{R}_{+}',r'\:\:,\:\:',r'f(',r'0',r') =',r'0').move_to(t_1, aligned_edge = LEFT)
        t_1_x0_2[6].set_color(YELLOW)
        t_1_x0_2[8].set_color(YELLOW)
        self.play(ReplacementTransform(t_1_x0[8], t_1_x0_2[8]))
        self.wait(2)
        
        self.play(GrowFromCenter(dot_x0))
        self.play(t_1_x0[6].animate.set_color(WHITE),
                  t_1_x0_2[8].animate.set_color(WHITE),
                  dot_x0.animate.set_color(BLUE),
                  axes_zero.animate.set_color(WHITE))
        self.wait(2)


                # x = 1
        t_1_x1 = MathTex(r'f:',r'\mathbb{R}_{+}',r'\to',r'\mathbb{R}_{+}',r'\:\:,\:\:',r'f(',r'1',r') =',r'2 \cdot 1').move_to(t_1, aligned_edge = LEFT)
        t_1_x1[6].set_color(YELLOW)
        t_1_x1[8].set_color(YELLOW)

        dot_x1 = Dot(axes.coords_to_point(1,2,0), color = YELLOW)
        line_x1 = DashedLine(axes.coords_to_point(1,0,0), axes.coords_to_point(1,2,0), color = GRAY)
        line_y1 = DashedLine(axes.coords_to_point(0,2,0), axes.coords_to_point(1,2,0), color = line_x1.get_color())

        self.play(ReplacementTransform(t_1_x0[6], t_1_x1[6]),
                  ReplacementTransform(t_1_x0_2[8], t_1_x1[8]),
                  FadeIn(axes_x1))
        self.wait(2)

        t_1_x1_2 = MathTex(r'f:',r'\mathbb{R}_{+}',r'\to',r'\mathbb{R}_{+}',r'\:\:,\:\:',r'f(',r'1',r') =',r'2').move_to(t_1, aligned_edge = LEFT)
        t_1_x1_2[6].set_color(YELLOW)
        t_1_x1_2[8].set_color(YELLOW)
        self.play(ReplacementTransform(t_1_x1[8], t_1_x1_2[8]),
                  FadeIn(axes_y1))
        self.play(FadeIn(line_x1), FadeIn(line_y1), GrowFromCenter(dot_x1))
        self.play(t_1_x1[6].animate.set_color(WHITE),
                  t_1_x1_2[8].animate.set_color(WHITE),
                  dot_x1.animate.set_color(BLUE),
                  axes_x1.animate.set_color(WHITE),
                  axes_y1.animate.set_color(WHITE))
        self.wait(2)


                # x = 2
        t_1_x2 = MathTex(r'f:',r'\mathbb{R}_{+}',r'\to',r'\mathbb{R}_{+}',r'\:\:,\:\:',r'f(',r'2',r') =',r'4').move_to(t_1, aligned_edge = LEFT)
        t_1_x2[6].set_color(YELLOW)
        t_1_x2[8].set_color(YELLOW)

        dot_x2 = Dot(axes.coords_to_point(2,4,0), color = YELLOW)
        line_x2 = DashedLine(axes.coords_to_point(2,0,0), axes.coords_to_point(2,4,0), color = line_x1.get_color())
        line_y2 = DashedLine(axes.coords_to_point(0,4,0), axes.coords_to_point(2,4,0), color = line_x1.get_color())

        self.play(ReplacementTransform(t_1_x1[6], t_1_x2[6]),
                  ReplacementTransform(t_1_x1_2[8], t_1_x2[8]),
                  FadeIn(axes_x2), FadeIn(axes_y2))
        self.play(FadeIn(line_x2), FadeIn(line_y2), GrowFromCenter(dot_x2))
        self.play(t_1_x2[6].animate.set_color(WHITE),
                  t_1_x2[8].animate.set_color(WHITE),
                  dot_x2.animate.set_color(BLUE),
                  axes_x2.animate.set_color(WHITE),
                  axes_y2.animate.set_color(WHITE))
        self.wait(2)


                # x = 3
        t_1_x3 = MathTex(r'f:',r'\mathbb{R}_{+}',r'\to',r'\mathbb{R}_{+}',r'\:\:,\:\:',r'f(',r'3',r') =',r'6').move_to(t_1, aligned_edge = LEFT)
        t_1_x3[6].set_color(YELLOW)
        t_1_x3[8].set_color(YELLOW)

        dot_x3 = Dot(axes.coords_to_point(3,6,0), color = YELLOW)
        line_x3 = DashedLine(axes.coords_to_point(3,0,0), axes.coords_to_point(3,6,0), color = line_x1.get_color())
        line_y3 = DashedLine(axes.coords_to_point(0,6,0), axes.coords_to_point(3,6,0), color = line_x1.get_color())

        self.play(ReplacementTransform(t_1_x2[6], t_1_x3[6]),
                  ReplacementTransform(t_1_x2[8], t_1_x3[8]),
                  FadeIn(axes_x3), FadeIn(axes_y3))
        self.play(FadeIn(line_x3), FadeIn(line_y3), GrowFromCenter(dot_x3))
        self.play(t_1_x3[6].animate.set_color(WHITE),
                  t_1_x3[8].animate.set_color(WHITE),
                  dot_x3.animate.set_color(BLUE),
                  axes_x3.animate.set_color(WHITE),
                  axes_y3.animate.set_color(WHITE))
        self.wait(2)
        self.play(ReplacementTransform(t_1_x3[6], t_1_copy[6]),
                  ReplacementTransform(t_1_x3[8], t_1_copy[8]))
        self.wait(2)


        # Adicionando mais pontos
        dot_1 = Dot(axes.coords_to_point(0.5,1,0), color = BLUE_D)
        dot_2 = Dot(axes.coords_to_point(1.5,3,0), color = dot_1.get_color())
        dot_3 = Dot(axes.coords_to_point(2.5,5,0), color = dot_1.get_color())
        more_dots_1 = VGroup(dot_1, dot_2, dot_3)
        self.play(Create(more_dots_1))
        self.wait(2)

        # Adicionando ainda mais pontos
        dot_4 = Dot(axes.coords_to_point(0.25,0.5,0), color = BLUE_E)
        dot_5 = Dot(axes.coords_to_point(0.75,1.5,0), color = dot_4.get_color())
        dot_6 = Dot(axes.coords_to_point(1.25,2.5,0), color = dot_4.get_color())
        dot_7 = Dot(axes.coords_to_point(1.75,3.5,0), color = dot_4.get_color())
        dot_8 = Dot(axes.coords_to_point(2.25,4.5,0), color = dot_4.get_color())
        dot_9 = Dot(axes.coords_to_point(2.75,5.5,0), color = dot_4.get_color())
        more_dots_2 = VGroup(dot_4, dot_5, dot_6, dot_7, dot_8, dot_9)
        self.play(Create(more_dots_2))
        self.wait(2)

        # Os pontos se tornam uma reta
        graph = axes.plot(lambda x: 2 * x, stroke_width = 7, color = dot_x0.get_color(), x_range = [0, 3])
        g_dots = VGroup(dot_x0, dot_x1, dot_x2, dot_x3,
                        more_dots_1, more_dots_2)
        self.play(TransformMatchingShapes(g_dots, graph))
        self.wait(2)

        # Mostrar que o domínio e contradomínio restringem o gráfico à parte positiva     
        g = VGroup(axes, axes_labels, axes_numbers, axes_zero, graph,
                   line_x1, line_x2, line_x3, line_y1, line_y2, line_y3)
        self.play(g.animate.scale(0.8).shift(UP),
                  black_rectangle_1.animate.shift(DOWN*2),
                  black_rectangle_2.animate.shift(LEFT*5))
        self.wait(2)

        x_axis_negative_part = Line(axes.coords_to_point(0,0,0), axes.coords_to_point(-3,0,0), color = RED, stroke_width = 20, stroke_opacity = 0.5).set_z_index(4)
        y_axis_negative_part = Line(axes.coords_to_point(0,0,0), axes.coords_to_point(0,-3,0), color = RED, stroke_width = 20, stroke_opacity = 0.5).set_z_index(4)
        self.play(FadeIn(x_axis_negative_part, y_axis_negative_part))
        self.wait(2)

        # Destaque no domínio e contradomínio
        black_rectangle_3 = Rectangle(width = 10, height = 7, color = BLACK, fill_opacity = 0.8).shift(DOWN).set_z_index(5)
        self.play(FadeIn(black_rectangle_3))
        self.wait(2)

        indicative_arrow_1 = Arrow(DOWN, UP*0.5, color = YELLOW).rotate(45*DEGREES).shift(UP*2.5+LEFT*1.4).set_z_index(6)
        indicative_arrow_2 = Arrow(DOWN, UP*0.5, color = YELLOW).rotate(45*DEGREES).shift(UP*2.5+RIGHT*0.1).set_z_index(6)
        self.play(FadeIn(indicative_arrow_1, indicative_arrow_2))
        self.wait(2)

        t_2 = MathTex(r'f:',r'\mathbb{R}',r'\:\:\to\:\:',r'\mathbb{R}',r'\:\:,\:\:',r'f(',r'x',r') =',r'2x', color = YELLOW).shift(UP*3)
        self.play(ReplacementTransform(t_1[1], t_2[1]),
                  ReplacementTransform(t_1[3], t_2[3]))
        self.play(t_2[1].animate.set_color(WHITE),
                  t_2[3].animate.set_color(WHITE))
        self.wait(2)
        self.play(FadeOut(black_rectangle_3, indicative_arrow_1, indicative_arrow_2))
        self.wait(2)

        graph_negative_part = axes.plot(lambda x: 2 * x, stroke_width = 7, color = dot_x0.get_color(), x_range = [-1.5, 0]).set_z_index(-4)
        graph_negative_part.reverse_points()
        self.play(Create(graph_negative_part), FadeOut(x_axis_negative_part, y_axis_negative_part))
        self.wait(2)


        '''self.add(t_1, g_axes, graph,
                 dot_x0, dot_x1, dot_x2, dot_x3,
                 more_dots_1, more_dots_2,
                 line_x1, line_x2, line_x3, line_y1, line_y2, line_y3,
                 black_rectangles, x_axis_negative_part, y_axis_negative_part,
                 indicative_arrow_1, indicative_arrow_2,
                 black_rectangle_3)'''



# Função definida por partes e seu gráfico
class vid12(MovingCameraScene):
    def construct(self):

        # Função-exemplo
        g = MathTex(r'g : \mathbb{R} \to \mathbb{R} \:\:,\:\: g(x) = \begin{cases} 2x^2 \: , \:\:\: se \:\:\:\: x < 1 \\ x + 1 \: , \:\:\: se \:\:\:\: x \geq 1 \end{cases}').scale(0.9)
        self.play(Write(g[0][0:5]))
        self.wait(2)
        self.play(Write(g[0][5:12]))
        self.wait(2)
        self.play(Write(g[0][12:15]))
        self.wait(2)
        self.play(Write(g[0][15:21]))
        self.wait(2)
        self.play(Write(g[0][21:24]))
        self.wait(2)
        self.play(Write(g[0][24:30]))
        self.wait(2)
        self.play(g.animate.to_edge(UP))
        self.wait(2)

        # Eixos
        axes = Axes(x_range = [-1, 5, 1],
                    y_range = [-1, 4.5, 1],
                    x_length = 5,
                    y_length = 4.5,
                    axis_config = {"include_ticks" : False})
        x_label = MathTex("x").next_to(axes, DR, buff = -0.5).shift(RIGHT*0.5)
        y_label = MathTex("y").next_to(axes, UL, buff = -0.5).shift(UP*0.3)
        axes_labels = VGroup(x_label, y_label)
        axes_zero = MathTex('0').scale(0.8).next_to(axes.coords_to_point(0,0,0), DL, buff = 0.2)
        
        x_axis_n1_label = MathTex('1').scale(0.8).next_to(axes.coords_to_point(1,0,0), DOWN, buff = 0.2)
        x_axis_n1_tick = Line(DOWN*0.1, UP*0.1, stroke_width = 2).move_to(axes.coords_to_point(1,0,0))
        x_axis_n1 = VGroup(x_axis_n1_label, x_axis_n1_tick)

        x_axis_n2_label = MathTex('2').scale(0.8).next_to(axes.coords_to_point(2,0,0), DOWN, buff = 0.2)
        x_axis_n2_tick = Line(DOWN*0.1, UP*0.1, stroke_width = 2).move_to(axes.coords_to_point(2,0,0))
        x_axis_n2 = VGroup(x_axis_n2_label, x_axis_n2_tick)

        y_axis_n1_label = MathTex('1').scale(0.8).next_to(axes.coords_to_point(0,1,0), LEFT, buff = 0.2)
        y_axis_n1_tick = Line(LEFT*0.1, RIGHT*0.1, stroke_width = 2).move_to(axes.coords_to_point(0,1,0))
        y_axis_n1 = VGroup(y_axis_n1_label, y_axis_n1_tick)

        y_axis_n3_label = MathTex('3').scale(0.8).next_to(axes.coords_to_point(0,2.5,0), LEFT, buff = 0.2)
        y_axis_n3_tick = Line(LEFT*0.1, RIGHT*0.1, stroke_width = 2).move_to(axes.coords_to_point(0,2.5,0))
        y_axis_n3 = VGroup(y_axis_n3_label, y_axis_n3_tick)

        g_axes = VGroup(axes, axes_labels, axes_zero, x_axis_n1, x_axis_n2, y_axis_n1, y_axis_n3).shift(DOWN*1)
        self.play(FadeIn(axes, axes_labels, axes_zero, x_axis_n1))
        self.wait(2)

        # Domínio dividido em dois intervalos
            # x < 1
        brace_1_ref = Line(axes.coords_to_point(1,0,0), axes.coords_to_point(-1,0,0), color = ORANGE, stroke_width = 15, stroke_opacity = 0.7)
        brace_1 = Brace(brace_1_ref, UP, color = YELLOW)
        brace_1_label = MathTex('x < 1', color = YELLOW).next_to(brace_1, UP)
        self.play(FadeIn(brace_1, brace_1_label))
        self.wait(2)

            # x >= 1
        brace_2_ref = Line(axes.coords_to_point(1,0,0), axes.coords_to_point(4.57,0,0), color = RED, stroke_width = 15, stroke_opacity = 0.7)
        brace_2 = Brace(brace_2_ref, UP, color = YELLOW)
        brace_2_label = MathTex(r'x \geq 1', color = YELLOW).next_to(brace_2, UP)
        self.play(FadeIn(brace_2, brace_2_label))
        self.wait(2)

        # Gráfico 1
        graph_1_part_1 = axes.plot(lambda x: 2*x**2,
                            x_range=[-1.5, 1], stroke_width = 7).set_color(BLUE).set_z_index(2)
        graph_1_part_2 = axes.plot(lambda x: x + 1,
                            x_range=[0.99, 4], stroke_width = 7).set_color(BLUE).set_z_index(2)
        self.play(Succession(FadeOut(brace_1, brace_1_label), Create(graph_1_part_1)),
                  g[0][12:15].animate.set_color(YELLOW))
        self.play(g[0][12:15].animate.set_color(WHITE))
        self.wait(2)
        self.play(Succession(FadeOut(brace_2, brace_2_label), Create(graph_1_part_2)),
                  g[0][21:24].animate.set_color(YELLOW))
        self.play(g[0][21:24].animate.set_color(WHITE))
        self.wait(2)

        # Seta inicando a quebra no gráfico
        indicative_arrow_1 = Arrow(DOWN, UP*0.5, color = YELLOW).rotate(55*DEGREES).shift(DOWN*1+LEFT*0.2)
        self.play(FadeIn(indicative_arrow_1))
        self.wait(2)

        self.play(FadeOut(g, x_axis_n1, graph_1_part_1, graph_1_part_2, indicative_arrow_1))

        # Outra função-exemplo
        h = MathTex(r'h : \mathbb{R} \to \mathbb{R} \:\:,\:\: h(x) = \begin{cases} x - 1 \: , \:\:\: se \:\:\:\: x < 2 \\ x + 1 \: , \:\:\: se \:\:\:\: x \geq 2 \end{cases}').scale(0.9).to_edge(UP)

        # Gráfico 2
        graph_2_part_1 = axes.plot(lambda x: x - 1,
                            x_range=[-0.1, 2], stroke_width = 7).set_color(BLUE).set_z_index(2)
        graph_2_part_2 = axes.plot(lambda x: x + 0.5,
                            x_range=[2, 4.5], stroke_width = 7).set_color(BLUE).set_z_index(2)
        dashed_line = DashedLine(graph_2_part_1.get_point_from_function(t = 2), graph_2_part_2.get_point_from_function(t = 2), color = YELLOW)
        self.play(FadeIn(graph_2_part_1, graph_2_part_2, x_axis_n2))
        self.wait(2)
        self.play(FadeIn(dashed_line))
        self.play(FadeOut(dashed_line))
        self.wait(2)

        self.play(FadeIn(h))
        self.wait(2)
        self.play(h[0][12:21].animate.set_color(YELLOW),
                  graph_2_part_1.animate.set_color(YELLOW))
        self.wait(2)
        self.play(h[0][12:21].animate.set_color(WHITE),
                  graph_2_part_1.animate.set_color(BLUE))
        self.play(h[0][21:30].animate.set_color(YELLOW),
                  graph_2_part_2.animate.set_color(YELLOW))
        self.wait(2)
        self.play(h[0][21:30].animate.set_color(WHITE),
                  graph_2_part_2.animate.set_color(BLUE))
        self.wait(2)

        # Lembrar que um x não pode se associar a dois y
        arrow_x_to_fx_1 = Line(axes.coords_to_point(2,0,0), axes.coords_to_point(2,2.5,0),
                               buff = 0, stroke_width = 5, color = GRAY).set_opacity(0.5)
        arrow_x_to_fx_2 = Arrow(axes.coords_to_point(2,1,0), axes.coords_to_point(0.1,1,0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)
        arrow_x_to_fx_3 = Arrow(axes.coords_to_point(2,2.5,0), axes.coords_to_point(0.1,2.5,0),
                                buff = 0, stroke_width = 5, tip_length = 0.2, color = GRAY).set_opacity(0.5)
        arrow_x_to_fx = VGroup(arrow_x_to_fx_1, arrow_x_to_fx_2, arrow_x_to_fx_3).set_z_index(-2)
        self.play(Create(arrow_x_to_fx_1))
        self.play(Create(arrow_x_to_fx_2), Create(arrow_x_to_fx_3), FadeIn(y_axis_n1, y_axis_n3))
        self.wait(2)

        indicative_arrow_2 = Arrow(DOWN, UP*0.5, color = YELLOW).rotate(-135*DEGREES).shift(DOWN*1+LEFT*2.5)
        self.play(FadeIn(indicative_arrow_2))
        self.wait(2)
        self.play(indicative_arrow_2.animate.shift(UP*1.4))
        self.wait(2)
        self.play(FadeOut(indicative_arrow_2))
        self.wait(2)

        dot_1 = Dot(axes.coords_to_point(2,2.5,0), color = YELLOW).scale(1.2)
        dot_2_1 = Dot(axes.coords_to_point(2,1,0), color = YELLOW).scale(1.2)
        dot_2_2 = Dot(axes.coords_to_point(2,1,0), color = BLACK).scale(0.8).set_z_index(3)
        indicative_arrow_3 = Arrow(DOWN, UP*0.5, color = YELLOW).rotate(90*DEGREES).shift(DOWN*1.35+RIGHT*0.7)
        self.play(h[0][21:30].animate.set_color(YELLOW))
        self.wait(2)
        self.play(FadeOut(arrow_x_to_fx))
        self.play(GrowFromCenter(dot_1))
        self.play(h[0][21:30].animate.set_color(WHITE),
                  dot_1.animate.set_color(BLUE))
        self.wait(2)
        self.play(FadeIn(indicative_arrow_3))
        self.wait(2)
        self.play(GrowFromCenter(dot_2_1), GrowFromCenter(dot_2_2), FadeOut(indicative_arrow_3))
        self.play(dot_2_1.animate.set_color(BLUE))
        self.wait(2)

        arrow_x_to_fx.set_z_index(4)
        self.play(Succession(Create(arrow_x_to_fx_1), Create(arrow_x_to_fx_3)), run_time = 2)
        self.wait(2)
        self.play(FadeOut(arrow_x_to_fx_1, arrow_x_to_fx_3))
        self.wait(2)

        self.play(LaggedStart(
            Flash(dot_2_1, num_lines = 8),
            Flash(dot_1, num_lines = 8),
            lag_ratio = 0.3))
        self.wait(2)
        
        indicative_arrow_4 = Arrow(DOWN, UP*0.5, color = YELLOW).rotate(45*DEGREES).shift(DOWN*0.8+RIGHT*0.5)
        self.play(FadeIn(indicative_arrow_3))
        self.wait(2)
        self.play(FadeOut(indicative_arrow_3))
        self.wait(2)
        self.play(FadeIn(indicative_arrow_4))
        self.wait(2)
        self.play(FadeOut(indicative_arrow_4))
        self.wait(3)
        

