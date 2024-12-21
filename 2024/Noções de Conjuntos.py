# Noçõoes de Conjuntos

from manim import*

class vid1(Scene):
    def construct(self):

    #DEFINIÇÃO DE CONJUNTO
        t1 = Text("con.jun.to", weight=BOLD).shift(UP*2+LEFT*2.2).scale(1.5)
        t2 = Tex("s.m.").shift(UP*1.1+LEFT*4.2).scale(1.2)
        t3 = Tex("coleção de objetos;").shift(LEFT*1.7+DOWN*0.5).scale(1.5)
        t4 = Tex("grupo, agrupamento.").next_to(t3, DOWN, buff=0.5).shift(RIGHT*0.35).scale(1.5)

        g = VGroup(t1, t2, t3, t4)

        self.play(Write(g), run_time=3)
        self.wait()



class vid2(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=70*DEGREES, theta=-40*DEGREES, zoom=2, frame_center=np.array([0,1,0]), focal_distance=10)
        
        self.begin_3dillusion_camera_rotation(rate=0.5)

    #DEF CAIXA
        #faces da caixa
        b1 = Polygon((0,0,0), (0,1,0), (1,1,0), (1,0,0))
        b2 = Polygon((0,0,0), (0,0,1), (0,1,1), (0,1,0))
        b3 = Polygon((0,0,0), (0,0,1), (1,0,1), (1,0,0))
        b4 = Polygon((1,1,0), (1,1,1), (0,1,1), (0,1,0))
        b5 = Polygon((1,1,0), (1,1,1), (1,0,1), (1,0,0))

        a1 = Polygon((0,0,1), (0,1,1), (0.5,1,1), (0.5,0,1))
        a2 = Polygon((0.5,0,1), (0.5,1,1), (1,1,1), (1,0,1))
        a3 = Polygon((0,0,1), (0,0.5,1), (1,0.5,1), (1,0,1))
        a4 = Polygon((0,1,1), (0,0.5,1), (1,0.5,1), (1,1,1))

        gb = VGroup(b1, b2, b3, b4, b5, a1, a2, a3, a4)
        gb.set_opacity(0.5)
        gb.set_stroke(width=5)
        
        #self.add(gb)
        self.play(Write(gb))
        self.wait()
        self.play(LaggedStart(
                    Rotate(a1, -135*DEGREES, axis=Y_AXIS, about_point=(0,0,1)),
                    Rotate(a2, 135*DEGREES, axis=Y_AXIS, about_point=(1,0,1)),
                    Rotate(a3, 135*DEGREES, axis=X_AXIS, about_point=(0,0,1)),
                    Rotate(a4, -135*DEGREES, axis=X_AXIS, about_point=(0,1,1)),
                    lag_ratio=0.3))

    #DEF OBJETOS
        #pontos
        p1 = Dot3D((0.2,0.3,0.8))
        p2 = Dot3D((0.5,0.5,0.3))
        p3 = Dot3D((0.8,0.8,0.8))

        go0 = VGroup(p1, p2, p3)

        self.play(FadeIn(go0))
        self.wait(7)

        #letras do alfabeto
        o1 = Tex("x").move_to((0.2,0.3,0.8)).scale(0.7)
        o1.rotate(70*DEGREES, X_AXIS)
        o1.rotate(60*DEGREES, Z_AXIS)

        o2 = Tex("y").move_to((0.5,0.5,0.3)).scale(0.7)
        o2.rotate(70*DEGREES, X_AXIS)
        o2.rotate(60*DEGREES, Z_AXIS)
        
        o3 = Tex("z").move_to((0.8,0.8,0.8)).scale(0.7)
        o3.rotate(70*DEGREES, X_AXIS)
        o3.rotate(60*DEGREES, Z_AXIS)
        
        go1 = VGroup(o1, o2, o3)
        
        self.play(FadeOut(go0), FadeIn(go1))
        self.wait()

        #nomes de famosos
        o4 = Tex("Will Smith").move_to((0.2,0.3,0.8)).scale(0.5)
        o4.rotate(80*DEGREES, Y_AXIS)
        o4.rotate(-10*DEGREES, Z_AXIS)
        o4.rotate(10*DEGREES, X_AXIS)

        o5 = Tex("Taylor Swift").move_to((0.5,0.5,0.7)).scale(0.5)
        o5.rotate(80*DEGREES, Y_AXIS)
        o5.rotate(-10*DEGREES, Z_AXIS)
        
        o6 = Tex("Bill Gates").move_to((0.8,0.8,0.8)).scale(0.5)
        o6.rotate(100*DEGREES, Y_AXIS)
        o6.rotate(50*DEGREES, Z_AXIS)
        o6.rotate(180*DEGREES, X_AXIS)
        
        go2 = VGroup(o4, o5, o6)
        
        self.play(FadeOut(go1), FadeIn(go2))
        self.wait(0.7)

        #figuras geométricas
        o7 = Square(side_length=0.3).move_to((0.2,0.3,0.8))
        o7.rotate(80*DEGREES, Y_AXIS)
        o7.rotate(-30*DEGREES, Z_AXIS)

        o8 = Triangle().move_to((0.5,0.5,0.4)).scale(0.2)
        o8.rotate(70*DEGREES, X_AXIS)
        o8.rotate(70*DEGREES, Z_AXIS)

        o9 = Circle(radius=0.2).move_to((0.8,0.8,0.8))
        o9.rotate(80*DEGREES, Y_AXIS)
        o9.rotate(-30*DEGREES, Z_AXIS)

        go3 = VGroup(o7, o8, o9)
        go3.set_color(WHITE)
        
        self.play(FadeOut(go2), FadeIn(go3))
        self.wait(0.5)

        #números
        o10 = MathTex("2").move_to((0.2,0.3,0.8)).scale(0.7)
        o10.rotate(80*DEGREES, X_AXIS)
        o10.rotate(40*DEGREES, Z_AXIS)

        o11 = MathTex("-4").move_to((0.5,0.5,0.4)).scale(0.7)
        o11.rotate(80*DEGREES, X_AXIS)
        o11.rotate(40*DEGREES, Z_AXIS)
        
        o12 = MathTex("7").move_to((0.8,0.8,0.8)).scale(0.7)
        o12.rotate(80*DEGREES, X_AXIS)
        o12.rotate(40*DEGREES, Z_AXIS)
        
        go4 = VGroup(o10, o11, o12)
        
        self.play(FadeOut(go3), FadeIn(go4))

        #outro conjunto
        b1_2 = Polygon((0,0,0), (0,1,0), (1,1,0), (1,0,0))
        b2_2 = Polygon((0,0,0), (0,0,1), (0,1,1), (0,1,0))
        b3_2 = Polygon((0,0,0), (0,0,1), (1,0,1), (1,0,0))
        b4_2 = Polygon((1,1,0), (1,1,1), (0,1,1), (0,1,0))
        b5_2 = Polygon((1,1,0), (1,1,1), (1,0,1), (1,0,0))

        a1_2 = Polygon((0,0,1), (0,-0.3,1.3), (1,-0.3,1.3), (1,0,1))
        a2_2 = Polygon((0,1,1), (0,1.3,1.3), (1,1.3,1.3), (1,1,1))
        a3_2 = Polygon((0,0,1), (-0.3,0,1.3), (-0.3,1,1.3), (0,1,1))
        a4_2 = Polygon((1,0,1), (1.3,0,1.3), (1.3,1,1.3), (1,1,1))

        gb_2 = VGroup(b1_2, b2_2, b3_2, b4_2, b5_2, a1_2, a2_2, a3_2, a4_2)
        gb_2.set_color(WHITE)
        gb_2.set_opacity(0.5)
        gb_2.set_stroke(width=5)
        gb_2.scale(0.5)

        self.play(FadeOut(go4), FadeIn(gb_2))
        self.wait()

        #vazia
        self.play(FadeOut(gb_2))
        self.wait(5) 


class vid3(Scene):
    def construct(self):

    #DIAGRAMA DE VENN

        t0 = Tex("Diagrama de Venn", color=GREEN).to_edge(UL).scale(1)
        u = Underline(t0).set_color(GREEN)

        self.play(LaggedStart(Write(t0), Write(u), lag_ratio=0.5))

        #conjunto
        c = Circle(radius=2, color=BLUE, fill_opacity=0.1)
        A = MathTex("A", color=BLUE).next_to(c, UL, buff=-0.6).scale(1.5).set_z_index(2)
        Ab = MathTex("A", color=BLACK, stroke_width=10).move_to(A).scale(1.5).set_z_index(1)
        
        #elementos
        x = MathTex("x").move_to((-0.8,0.5,0)).scale(1.3)
        y = MathTex("y").move_to((-0.1,-1,0)).scale(1.3)    
        z = MathTex("z").move_to((1,0,0)).scale(1.5)
        w = MathTex("w").move_to((-1,-2.7,0)).scale(1.3)

        cA = VGroup(c, A, Ab, x, y, z, w)
        self.play(DrawBorderThenFill(c))
        self.wait()
        self.play(FadeIn(A, Ab))
        self.wait()
        self.play(LaggedStart(FadeIn(x), FadeIn(y), FadeIn(z), FadeIn(w), lag_ratio=0.3))
        self.wait()
        self.play(FadeOut(t0, u))

        #pertinência
        self.play(cA.animate.shift(LEFT*3))
        self.wait()

        t1 = MathTex(r"x,\:y,\:z \:\in\: ","A").scale(1.5).shift(RIGHT*3)
        t1[1].set_color(BLUE)

        t2 = MathTex(r"w \:\notin\: ","A").scale(1.5).shift(RIGHT*3+DOWN)
        t2[1].set_color(BLUE)

        self.play(Write(t1))
        self.wait()
        self.play(LaggedStart(t1.animate.shift(UP), Write(t2), lag_ratio=0.5))
        self.wait()

        #cardinalidade
        tc = Tex(r"Cardinalidade:",r" número de \\ elementos do conjunto").shift(RIGHT*3)
        tc[0].set_color(YELLOW)

        tc2 = MathTex(r"\vert","A",r"\vert").shift(RIGHT*3+DOWN)
        tc2[0].set_color(YELLOW)
        tc2[1].set_color(BLUE)
        tc2[2].set_color(YELLOW)

        tc3 = MathTex(r"\vert","A",r"\vert").shift(RIGHT*3+DOWN)
        tc3[1].set_color(BLUE)

        tc4 = MathTex(r"\vert","A",r"\vert","=3").shift(RIGHT*3+DOWN)
        tc3[1].set_color(BLUE)

        self.play(LaggedStart(FadeOut(t1, t2), Write(tc), lag_ratio=0.6))
        self.wait()
        self.play(LaggedStart(tc.animate.shift(UP), Write(tc2), lag_ratio=0.6))
        self.wait()
        self.play(TransformMatchingShapes(tc2, tc3))
        self.wait()
        self.play(TransformMatchingShapes(tc3, tc4))
        self.wait()



class vid4(Scene):
    def construct(self):

    #ENUMERAÇÃO
        
        t0 = Tex("Enumeração", color=GREEN).to_corner(UL).scale(1)
        u = Underline(t0).set_color(GREEN)

        self.play(LaggedStart(Write(t0), Write(u), lag_ratio=0.5))
        
        t1 = MathTex(r"A",r"= \left\{ x,\:y,\:z \right\}").scale(1.5)
        t1[0].set_color(BLUE)

        t1_2 = MathTex(r"A",r"=",r"\left\{",r"x,\:y,\:z",r"\right\}").scale(1.5)
        t1_2[0].set_color(BLUE)
        t1_2[2].set_color(YELLOW)
        t1_2[4].set_color(YELLOW)

        self.play(Write(t1))
        self.wait()
        self.play(TransformMatchingShapes(t1, t1_2))
        self.play(TransformMatchingShapes(t1_2, t1))
        self.wait()
        self.play(FadeOut(t0, u))
        self.wait()

        #não importa a ordem dos elementos
        t2 = MathTex(r"B",r"= \left\{ z,\:x,\:y \right\}").scale(1.5).shift(DOWN)
        t2[0].set_color(RED)

        t3 = MathTex(r"\Rightarrow").shift(RIGHT*0.7).scale(1.5)
        t4 = MathTex(r"A","=","B").shift(RIGHT*3).scale(1.5)
        t4[0].set_color(BLUE)
        t4[2].set_color(RED)

        self.play(LaggedStart(t1.animate.shift(UP), Write(t2), lag_ratio=0.8))
        self.wait()

        g = VGroup(t1, t2)
        self.play(LaggedStart(g.animate.shift(LEFT*3), FadeIn(t3), Write(t4), lag_ratio=0.6))
        self.wait()
        
        #elementos repetidos
        self.play(FadeOut(t2, t3, t4), t1.animate.shift(RIGHT*3+DOWN))
        self.wait()

        t5 = MathTex(r"\vert","A",r"\vert","=3").scale(1.5).shift(UP*2)
        t5[1].set_color(BLUE)

        t6 = MathTex(r"A",r"= \left\{ x,\:x,\:y,\:y,\:z,\:z \right\}").scale(1.5)
        t6[0].set_color(BLUE)

        self.play(Write(t5))
        self.wait()
        self.play(TransformMatchingShapes(t1, t6))
        self.wait()



class vid5(Scene):
    def construct(self):

    #DESCRIÇÃO
        
        t0 = Tex("Descrição por uma propriedade", color=GREEN).to_corner(UL).scale(1)
        u = Underline(t0).set_color(GREEN)

        self.play(LaggedStart(Write(t0), Write(u), lag_ratio=0.5), run_time=2)
        self.wait()

        #conjunto A
        A0 = MathTex(r"A",r"= \left\{ x,\:y,\:z \right\}").scale(1.5)
        A0[0].set_color(BLUE)
        
        A_1 = Tex("3 últimas letras do alfabeto").shift(RIGHT*0.5)
        A_2 = MathTex("A",r"=\left\{").next_to(A_1, LEFT, buff=0.05)
        A_2[0].set_color(BLUE)
        A_3 = MathTex(r"\right\}").next_to(A_1, RIGHT, buff=0.05)
        A = VGroup(A_2, A_1, A_3).scale(1.5)

        self.play(Write(A0))
        self.wait()
        self.play(TransformMatchingShapes(A0, A))
        self.wait()
        self.play(FadeOut(t0, u))

        #conjunto-exemplo B
        B_1 = Tex("números maiores que 2").shift(RIGHT*0.5)
        B_2 = MathTex("B",r"=\left\{").next_to(B_1, LEFT, buff=0.05)
        B_2[0].set_color(RED)
        B_3 = MathTex(r"\right\}").next_to(B_1, RIGHT, buff=0.05)
        B = VGroup(B_2, B_1, B_3).scale(1.5)

        self.play(LaggedStart(FadeOut(A), Write(B), lag_ratio=0.8))

        t1 = MathTex(r"12 \:\in\:","B").shift(UP*2+LEFT*2).scale(1.3)
        t1[1].set_color(RED)

        t2 = MathTex(r"-4 \:\notin\:","B").shift(UP*2+RIGHT*2).scale(1.3)
        t2[1].set_color(RED)

        self.play(FadeIn(t1))
        self.wait()
        self.play(FadeIn(t2))
        self.wait()



class vid6(Scene):
    def construct(self):

    #CONJUNTOS UNITÁRIO E VAZIO
        
        #conjunto unitário
        n1 = Tex("Conjunto unitário", color=YELLOW).shift(UP*2).scale(1.3)

        t1 = MathTex(r"A",r"= \left\{ x \right\}").scale(1.5)
        t1[0].set_color(BLUE)
        
        self.play(Write(t1))
        self.wait()
        self.play(FadeIn(n1))
        self.wait()
        self.play(FadeOut(n1))
        self.wait()

        #conjunto vazio
        n2 = Tex("Conjunto vazio", color=YELLOW).shift(UP*2).scale(1.3)
        
        t2 = MathTex(r"A",r"= \left\{ \: \right\}").scale(1.5)
        t2[0].set_color(BLUE)

        t3 = MathTex(r"A",r"=",r"\left\{ \: \right\}").scale(1.5)
        t3[0].set_color(BLUE)
        t3[2].set_color(YELLOW)

        t4 = MathTex(r"A",r"=",r"\left\{ \: \right\}").scale(1.5)
        t4[0].set_color(BLUE)

        t5 = MathTex(r"A",r"=",r"\left\{ \: \right\} =",r"\text{\o}").scale(1.5)
        t5[0].set_color(BLUE)
        t5[3].set_color(YELLOW)

        t6 = MathTex(r"A",r"=",r"\left\{ \: \right\} =",r"\text{\o}").scale(1.5)
        t6[0].set_color(BLUE)

        self.play(TransformMatchingShapes(t1, t2))
        self.wait()
        self.play(FadeIn(n2))
        self.wait()
        self.play(TransformMatchingShapes(t2, t3))
        self.wait()
        self.play(TransformMatchingShapes(t3, t4))
        self.wait()
        self.play(TransformMatchingShapes(t4, t5))
        self.wait()
        self.play(TransformMatchingShapes(t5, t6))
        self.wait()
        self.play(FadeOut(n2))
        self.wait()

        t7 = MathTex(r"\left\{ \: \right\}").scale(1.5).shift(LEFT*2)
        t8 = MathTex("=").scale(1.5)
        g = VGroup(t7, t8)

        self.play(TransformMatchingShapes(t6, g))
        self.wait()



class vid7(ThreeDScene):
    def construct(self):

    #ANIMAÇÃO CAIXA VAZIA (CONJUNTO VAZIO)

        self.set_camera_orientation(phi=70*DEGREES, theta=-40*DEGREES, zoom=2, frame_center=np.array([0,1,0]), focal_distance=10)

        self.begin_ambient_camera_rotation(rate=0.5)

        b1_2 = Polygon((0,0,0), (0,1,0), (1,1,0), (1,0,0))
        b2_2 = Polygon((0,0,0), (0,0,1), (0,1,1), (0,1,0))
        b3_2 = Polygon((0,0,0), (0,0,1), (1,0,1), (1,0,0))
        b4_2 = Polygon((1,1,0), (1,1,1), (0,1,1), (0,1,0))
        b5_2 = Polygon((1,1,0), (1,1,1), (1,0,1), (1,0,0))

        a1_2 = Polygon((0,0,1), (0,-0.3,1.3), (1,-0.3,1.3), (1,0,1))
        a2_2 = Polygon((0,1,1), (0,1.3,1.3), (1,1.3,1.3), (1,1,1))
        a3_2 = Polygon((0,0,1), (-0.3,0,1.3), (-0.3,1,1.3), (0,1,1))
        a4_2 = Polygon((1,0,1), (1.3,0,1.3), (1.3,1,1.3), (1,1,1))

        gb_2 = VGroup(b1_2, b2_2, b3_2, b4_2, b5_2, a1_2, a2_2, a3_2, a4_2)
        gb_2.set_color(WHITE)
        gb_2.set_opacity(0.5)
        gb_2.set_stroke(width=5)
        gb_2.move_to((0,1,0.5))

        self.wait()
        self.play(FadeIn(gb_2))
        self.wait(15)
        


class vid8(ThreeDScene):
    def construct(self):

    #Conjunto unitário contendo conjunto vazio
        
        P1 = MathTex(r"P= \left\{ \: \text{\o} \: \right\}").scale(1.5)
        P2 = MathTex(r"P= \left\{ \left\{ \: \right\} \right\}").scale(1.5)
        P3 = MathTex(r"P=",r"\left\{",r"\left\{ \: \right\}",r"\right\}").scale(1.5).shift(UP*2.5)
        P3[1].set_color(BLUE)
        P3[3].set_color(BLUE)
        P4 = MathTex(r"P=",r"\left\{",r"\left\{ \: \right\}",r"\right\}").scale(1.5).shift(UP*2.5)
        P4[1].set_color(BLUE)
        P4[2].set_color(YELLOW)
        P4[3].set_color(BLUE)

        t = Tex("Unitário ou vazio?", color=YELLOW).scale(1.3).shift(UP*2)

        self.play(Write(P1))
        self.wait()
        self.play(FadeIn(t))
        self.wait()
        self.play(TransformMatchingTex(P1, P2))
        self.wait()
        self.play(LaggedStart(FadeOut(t), P2.animate.shift(UP*2.5), lag_ratio=0.7))
        self.wait()
        self.play(TransformMatchingShapes(P2, P3))
        self.wait()
        self.play(TransformMatchingShapes(P3, P4))
        self.wait()



class vid9(ThreeDScene):
    def construct(self):

    #ANIMAÇÃO CAIXA CONTENDO CAIXA VAZIA

        self.set_camera_orientation(phi=70*DEGREES, theta=-40*DEGREES, zoom=2, frame_center=np.array([0,1,0]), focal_distance=10)

        self.begin_ambient_camera_rotation(rate=0.5)

        #caixa de fora
        b1_2 = Polygon((0,0,0), (0,1,0), (1,1,0), (1,0,0))
        b2_2 = Polygon((0,0,0), (0,0,1), (0,1,1), (0,1,0))
        b3_2 = Polygon((0,0,0), (0,0,1), (1,0,1), (1,0,0))
        b4_2 = Polygon((1,1,0), (1,1,1), (0,1,1), (0,1,0))
        b5_2 = Polygon((1,1,0), (1,1,1), (1,0,1), (1,0,0))

        a1_2 = Polygon((0,0,1), (0,-0.3,1.3), (1,-0.3,1.3), (1,0,1))
        a2_2 = Polygon((0,1,1), (0,1.3,1.3), (1,1.3,1.3), (1,1,1))
        a3_2 = Polygon((0,0,1), (-0.3,0,1.3), (-0.3,1,1.3), (0,1,1))
        a4_2 = Polygon((1,0,1), (1.3,0,1.3), (1.3,1,1.3), (1,1,1))

        gb_2 = VGroup(b1_2, b2_2, b3_2, b4_2, b5_2, a1_2, a2_2, a3_2, a4_2)
        gb_2.set_color(BLUE)
        gb_2.set_opacity(0.5)
        gb_2.set_stroke(width=5)
        gb_2.move_to((0,1,0.5))

        #caixa de dentro
        b1_1 = Polygon((0,0,0), (0,1,0), (1,1,0), (1,0,0))
        b2_1 = Polygon((0,0,0), (0,0,1), (0,1,1), (0,1,0))
        b3_1 = Polygon((0,0,0), (0,0,1), (1,0,1), (1,0,0))
        b4_1 = Polygon((1,1,0), (1,1,1), (0,1,1), (0,1,0))
        b5_1 = Polygon((1,1,0), (1,1,1), (1,0,1), (1,0,0))

        a1_1 = Polygon((0,0,1), (0,-0.3,1.3), (1,-0.3,1.3), (1,0,1))
        a2_1 = Polygon((0,1,1), (0,1.3,1.3), (1,1.3,1.3), (1,1,1))
        a3_1 = Polygon((0,0,1), (-0.3,0,1.3), (-0.3,1,1.3), (0,1,1))
        a4_1 = Polygon((1,0,1), (1.3,0,1.3), (1.3,1,1.3), (1,1,1))

        gb_1 = VGroup(b1_1, b2_1, b3_1, b4_1, b5_1, a1_1, a2_1, a3_1, a4_1)
        gb_1.set_color(YELLOW)
        gb_1.set_opacity(0.5)
        gb_1.set_stroke(width=5)
        gb_1.scale(0.5)
        gb_1.move_to((0,1,0.5))

        self.wait()
        self.play(FadeIn(gb_2))
        self.wait(2)
        self.play(FadeIn(gb_1))
        self.wait(15)

#IMAGES PARA TEXTO 
    
class img_caixa(ThreeDScene):
    def construct(self): 

        self.set_camera_orientation(phi=70*DEGREES, theta=-40*DEGREES, zoom=2, frame_center=np.array([0,1,0]), focal_distance=10)

        self.camera.background_color = WHITE

        #faces da caixa
        b1 = Polygon((0,0,0), (0,1,0), (1,1,0), (1,0,0))
        b2 = Polygon((0,0,0), (0,0,1), (0,1,1), (0,1,0))
        b3 = Polygon((0,0,0), (0,0,1), (1,0,1), (1,0,0))
        b4 = Polygon((1,1,0), (1,1,1), (0,1,1), (0,1,0))
        b5 = Polygon((1,1,0), (1,1,1), (1,0,1), (1,0,0))

        a1 = Polygon((0,0,1), (0,1,1), (0.5,1,1), (0.5,0,1)).rotate(-135*DEGREES, axis=Y_AXIS, about_point=(0,0,1))
        a2 = Polygon((0.5,0,1), (0.5,1,1), (1,1,1), (1,0,1)).rotate(135*DEGREES, axis=Y_AXIS, about_point=(1,0,1))
        a3 = Polygon((0,0,1), (0,0.5,1), (1,0.5,1), (1,0,1)).rotate(135*DEGREES, axis=X_AXIS, about_point=(0,0,1))
        a4 = Polygon((0,1,1), (0,0.5,1), (1,0.5,1), (1,1,1)).rotate(-135*DEGREES, axis=X_AXIS, about_point=(0,1,1))

        gb = VGroup(b1, b2, b3, b4, b5, a1, a2, a3, a4).set_color(BLUE_D)
        gb.set_opacity(0.5)
        gb.set_stroke(width=5)
        
        self.add(gb)

        #letras do alfabeto
        o1 = MathTex("x", color=BLACK, fill_opacity=0.7).move_to((0.2,0.3,0.8)).scale(0.7)
        o1.rotate(70*DEGREES, X_AXIS)
        o1.rotate(60*DEGREES, Z_AXIS)

        o2 = MathTex("y", color=BLACK, fill_opacity=0.7).move_to((0.5,0.5,0.3)).scale(0.7)
        o2.rotate(70*DEGREES, X_AXIS)
        o2.rotate(60*DEGREES, Z_AXIS)
        
        o3 = MathTex("z", color=BLACK, fill_opacity=0.7).move_to((0.8,0.8,0.8)).scale(0.7)
        o3.rotate(70*DEGREES, X_AXIS)
        o3.rotate(60*DEGREES, Z_AXIS)
        
        go1 = VGroup(o1, o2, o3)
        
        self.add(go1)

class img_diagrama(ThreeDScene):
        def construct(self): 

            self.camera.background_color = WHITE

            #conjunto
            c = Circle(radius=2, color=BLUE_D, fill_opacity=0.3)
            A = MathTex("A", color=BLUE_E).next_to(c, UL, buff=-0.6).scale(1.5).set_z_index(2)
            Ab = MathTex("A", color=WHITE, stroke_width=10).move_to(A).scale(1.5).set_z_index(1)
            
            #elementos
            x = MathTex("x", color=BLACK).move_to((-0.8,0.5,0)).scale(1.3)
            y = MathTex("y", color=BLACK).move_to((-0.1,-1,0)).scale(1.3)    
            z = MathTex("z", color=BLACK).move_to((1,0,0)).scale(1.5)
            w = MathTex("w", color=BLACK).move_to((2.5,-1.3,0)).scale(1.3)

            cA = VGroup(c, A, Ab, x, y, z, w)

            self.add(cA)

class img_caixa_conjunto_vazio(ThreeDScene):
    def construct(self): 

        self.set_camera_orientation(phi=70*DEGREES, theta=-40*DEGREES, zoom=2, frame_center=np.array([0,1,0]), focal_distance=10)

        self.camera.background_color = WHITE

        #faces da caixa
        b1 = Polygon((0,0,0), (0,1,0), (1,1,0), (1,0,0))
        b2 = Polygon((0,0,0), (0,0,1), (0,1,1), (0,1,0))
        b3 = Polygon((0,0,0), (0,0,1), (1,0,1), (1,0,0))
        b4 = Polygon((1,1,0), (1,1,1), (0,1,1), (0,1,0))
        b5 = Polygon((1,1,0), (1,1,1), (1,0,1), (1,0,0))

        a1 = Polygon((0,0,1), (0,1,1), (0.5,1,1), (0.5,0,1)).rotate(-135*DEGREES, axis=Y_AXIS, about_point=(0,0,1))
        a2 = Polygon((0.5,0,1), (0.5,1,1), (1,1,1), (1,0,1)).rotate(135*DEGREES, axis=Y_AXIS, about_point=(1,0,1))
        a3 = Polygon((0,0,1), (0,0.5,1), (1,0.5,1), (1,0,1)).rotate(135*DEGREES, axis=X_AXIS, about_point=(0,0,1))
        a4 = Polygon((0,1,1), (0,0.5,1), (1,0.5,1), (1,1,1)).rotate(-135*DEGREES, axis=X_AXIS, about_point=(0,1,1))

        gb = VGroup(b1, b2, b3, b4, b5, a1, a2, a3, a4).set_color(BLUE_D)
        gb.set_opacity(0.5)
        
        t = MathTex(r"\{ \: \} \:\: =", color=BLACK).rotate(90*DEGREES).rotate(90*DEGREES, axis=Y_AXIS).rotate(-40*DEGREES, axis=Z_AXIS)
        t.shift(LEFT*2)

        self.add(gb, t)

class img_conjunto_p_unitario(ThreeDScene):
    def construct(self): 

        #self.set_camera_orientation(phi=70*DEGREES, theta=-40*DEGREES, zoom=2, frame_center=np.array([0,1,0]), focal_distance=10)

        self.camera.background_color = WHITE

        #caixa de fora
        b1_2 = Polygon((0,0,0), (0,1,0), (1,1,0), (1,0,0))
        b2_2 = Polygon((0,0,0), (0,0,1), (0,1,1), (0,1,0))
        b3_2 = Polygon((0,0,0), (0,0,1), (1,0,1), (1,0,0))
        b4_2 = Polygon((1,1,0), (1,1,1), (0,1,1), (0,1,0))
        b5_2 = Polygon((1,1,0), (1,1,1), (1,0,1), (1,0,0))

        a1_2 = Polygon((0,0,1), (0,-0.3,1.3), (1,-0.3,1.3), (1,0,1))
        a2_2 = Polygon((0,1,1), (0,1.3,1.3), (1,1.3,1.3), (1,1,1))
        a3_2 = Polygon((0,0,1), (-0.3,0,1.3), (-0.3,1,1.3), (0,1,1))
        a4_2 = Polygon((1,0,1), (1.3,0,1.3), (1.3,1,1.3), (1,1,1))

        gb_2 = VGroup(b1_2, b2_2, b3_2, b4_2, b5_2, a1_2, a2_2, a3_2, a4_2)
        gb_2.set_color(BLUE)
        gb_2.set_opacity(0.3)
        gb_2.set_stroke(width=5)
        gb_2.move_to((0,1,0.5))

        #caixa de dentro
        b1_1 = Polygon((0,0,0), (0,1,0), (1,1,0), (1,0,0))
        b2_1 = Polygon((0,0,0), (0,0,1), (0,1,1), (0,1,0))
        b3_1 = Polygon((0,0,0), (0,0,1), (1,0,1), (1,0,0))
        b4_1 = Polygon((1,1,0), (1,1,1), (0,1,1), (0,1,0))
        b5_1 = Polygon((1,1,0), (1,1,1), (1,0,1), (1,0,0))

        a1_1 = Polygon((0,0,1), (0,-0.3,1.3), (1,-0.3,1.3), (1,0,1))
        a2_1 = Polygon((0,1,1), (0,1.3,1.3), (1,1.3,1.3), (1,1,1))
        a3_1 = Polygon((0,0,1), (-0.3,0,1.3), (-0.3,1,1.3), (0,1,1))
        a4_1 = Polygon((1,0,1), (1.3,0,1.3), (1.3,1,1.3), (1,1,1))

        gb_1 = VGroup(b1_1, b2_1, b3_1, b4_1, b5_1, a1_1, a2_1, a3_1, a4_1)
        gb_1.set_color(RED_E)
        gb_1.set_opacity(0.6)
        gb_1.scale(0.5)
        gb_1.move_to((0,1,0.3))
        
        t = MathTex(r"P = ",r"\{ ",r" \{ \: \} ",r" \} ",r" =", color=BLACK)
        t[1].set_color(BLUE_E)
        t[2].set_color(RED_E)
        t[3].set_color(BLUE_E)


        self.add(t)





class vid10(Scene):
    def construct(self):

    #SUBCONJUNTOS
    #conjunto A
        cA = Circle(radius=2, color=BLUE, fill_opacity=0.1)
        tA = MathTex("A", color=BLUE).next_to(cA, UL, buff=-0.6).scale(1.5).set_z_index(2)
        tAb = MathTex("A", color=BLACK, stroke_width=10).move_to(tA).scale(1.5).set_z_index(1)
        
        A = VGroup(cA, tA, tAb)

        #elementos de A
        x = MathTex("x").move_to((-0.8,0.5,0)).scale(1.3)
        y = MathTex("y").move_to((-0.1,-1,0)).scale(1.3)    
        z = MathTex("z").move_to((1,0,0)).scale(1.5)

    #conjunto B (subconjunto de A)
        cB = Ellipse(width=2, height=3).rotate(20*DEGREES).move_to((-0.5, -0.2, 0))
        tB = MathTex("B", color=RED).next_to(cB, UR, buff=-0.6).scale(1.5).set_z_index(2)
        tBb = MathTex("B", color=BLACK, stroke_width=10).move_to(tB).scale(1.5).set_z_index(1)

        B = VGroup(cB, tB, tBb)

        self.play(LaggedStart(DrawBorderThenFill(cA), FadeIn(tA, tAb), FadeIn(x, y, z), lag_ratio=0.6))
        self.wait()
        self.play(LaggedStart(DrawBorderThenFill(cB), FadeIn(tB, tBb), lag_ratio=0.6))
        self.wait()

        all = VGroup(A, B, x, y, z)

        self.play(all.animate.shift(LEFT*2.5))
        self.wait()

        #texto B subconjunto de A
        t1 = Tex("B"," é ","subconjunto"," de ","A").shift(RIGHT*3+UP*2).scale(1.1)
        t1[0].set_color(RED)
        t1[2].set_color(YELLOW)
        t1[4].set_color(BLUE)

        d2_1 = Dot((0.8, 1, 0)) 
        d2_2 = Dot((0.8, 0.3, 0)) 
        d3_1 = Dot((0.8, -0.7, 0)) 
        d3_2 = Dot((0.8, -1.4, 0)) 

        t2_1 = Tex("B"," pode ser gerado").next_to(d2_1, RIGHT)
        t2_1[0].set_color(RED)

        t2_2 = Tex("a partir de ","A").next_to(d2_2, RIGHT)
        t2_2[1].set_color(BLUE)

        t2 = VGroup(t2_1, t2_2)

        t3_1 = Tex("Todo elemento de ","B").next_to(d3_1, RIGHT)
        t3_1[1].set_color(RED)
        t3_2 = Tex("é também elemento de ","A").next_to(d3_2, RIGHT)
        t3_2[1].set_color(BLUE)

        t3 = VGroup(t3_1, t3_2)

        self.play(Write(t1))
        self.wait()
        self.play(FadeIn(d2_1, t2))
        self.wait()
        self.play(FadeIn(d3_1, t3))
        self.wait()

        self.play(FadeOut(d2_1, d3_1, t2, t3))

        #B contido em A / A contém B
        t4 = MathTex("B",r"\subset","A").scale(1.3).shift(RIGHT*3+UP*0.5)
        t4[0].set_color(RED)
        t4[2].set_color(BLUE)

        t5 = MathTex("A",r"\supset","B").scale(1.3).shift(RIGHT*3+DOWN)
        t5[0].set_color(BLUE)
        t5[2].set_color(RED)

        self.play(FadeIn(t4))
        self.wait()
        self.play(FadeIn(t5))
        self.wait()

        self.play(FadeOut(B, t1, t4, t5))

    #conjunto C (outro subconjunto de A)
        cC = Circle(radius=1.9, color=GREEN, fill_opacity=0.1).shift(LEFT*2.5)
        tC = MathTex("C", color=GREEN).next_to(cC, UR, buff=-0.6).scale(1.5).set_z_index(2)
        tCb = MathTex("C", color=BLACK, stroke_width=10).move_to(tC).scale(1.5).set_z_index(1)
        
        C = VGroup(cC, tC, tCb)
        
        self.play(LaggedStart(DrawBorderThenFill(cC), FadeIn(tC, tCb), lag_ratio=0.6))
        self.wait()

        #texto B subconjunto de A
        t6 = MathTex("C",r"\subset","A").shift(RIGHT*3+UP*1.5).scale(1.3)
        t6[0].set_color(GREEN)
        t6[2].set_color(BLUE)

        t7 = MathTex("C",r"=","A").shift(RIGHT*3).scale(1.3)
        t7[0].set_color(GREEN)
        t7[2].set_color(BLUE)

        t8 = MathTex("A",r"\subset","A").shift(RIGHT*3+DOWN*1.5).scale(1.3)
        t8[0].set_color(BLUE)
        t8[2].set_color(BLUE)

        self.play(FadeIn(t6))
        self.wait()
        self.play(FadeIn(t7))
        self.wait()
        self.play(FadeIn(t8))
        self.wait()

        self.play(FadeOut(C, t6, t7, t8))

    #conjunto vazio (subconjunto de A)
        cV = Circle(radius=0.7, color=PURPLE, fill_opacity=0.1).shift(LEFT*2.2+UP*1)
        tV = MathTex(r"\text{\o}", color=PURPLE).next_to(cV, UR, buff=-0.3).scale(1.5).set_z_index(2)
        tVb = MathTex(r"\text{\o}", color=BLACK, stroke_width=10).move_to(tV).scale(1.5).set_z_index(1)
        
        V = VGroup(cV, tV, tVb)
        
        t9 = MathTex(r"\text{\o}",r"\subset","A").shift(RIGHT*3).scale(1.3)
        t9[0].set_color(PURPLE)
        t9[2].set_color(BLUE)

        self.play(LaggedStart(DrawBorderThenFill(cV), FadeIn(tV, tVb), lag_ratio=0.6))
        self.wait()
        self.play(FadeIn(t9))
        self.wait()



class vid11(Scene):
    def construct(self):

    #PROPRIEDADES DA INCLUSÃO 
        tp = Tex("Propriedades da Inclusão", color=GREEN).scale(1.2).to_edge(UP)
        u3 = Underline(tp, color=GREEN)

        d1 = Dot((-3,1,0))
        d2 = Dot((-3,0,0))
        d3 = Dot((-3,-1,0))
        d4 = Dot((-3,-2,0))

        p1 = MathTex(r"\text{\o} \subset A").scale(1.2).next_to(d1, RIGHT)
        p2 = MathTex(r"A \subset A").scale(1.2).next_to(d2, RIGHT)
        p3 = MathTex(r"A \subset B \:e\: B \subset A \: \rightarrow \: A = B").scale(1.2).next_to(d3, RIGHT)
        p4 = MathTex(r"A \subset B \:e\: B \subset C \: \rightarrow \: A \subset C").scale(1.2).next_to(d4, RIGHT)

        self.play(LaggedStart(Write(tp), Write(u3), lag_ratio=0.6), run_time=1)
        self.wait()
        self.play(FadeIn(d1, p1))
        self.wait()
        self.play(FadeIn(d2, p2))
        self.wait()
        self.play(FadeIn(d3, p3))
        self.wait()
        self.play(FadeIn(d4, p4))
        self.wait()
        self.play(FadeOut(tp, u3, d1, p1, d2, p2, d3, p3, d4, p4))



class vid12(Scene):
    def construct(self):
             
    #CONJUNTO DAS PARTES
        t1 = Tex("Conjunto das partes (P(A)):"," conjunto de").to_edge(UP)
        t1[0].set_color(YELLOW)
        t2 = Tex("todos os subconjuntos de A").next_to(t1, DOWN)

        A = MathTex(r"A = \left\{ x, y \right\}").scale(1.3).shift(UP*0.5)
        s1 = MathTex(r"\text{\o}").scale(1.3).shift(LEFT*3+DOWN)
        s2 = MathTex(r"\left\{ x, y \right\}").scale(1.3).shift(LEFT*1.1+DOWN)
        s3 = MathTex(r"\left\{ x \right\}").scale(1.3).shift(RIGHT*1.1+DOWN)
        s4 = MathTex(r"\left\{ y \right\}").scale(1.3).shift(RIGHT*3+DOWN)
        
        p = MathTex(r"P(A) = \left\{ \text{\o} , \left\{ x, y \right\} , \left\{ x \right\} , \left\{ y \right\} \right\}").scale(1.3).shift(DOWN)

        self.play(LaggedStart(Write(t1), Write(t2), lag_ratio=0.5))
        self.wait()
        self.play(FadeIn(A))
        self.wait()
        self.play(FadeIn(s1))
        self.wait()
        self.play(FadeIn(s2))
        self.wait()
        self.play(FadeIn(s3))
        self.wait()
        self.play(FadeIn(s4))
        self.wait()

        gs = VGroup(s1, s2, s3, s4)

        self.play(TransformMatchingShapes(gs, p))
        self.wait()

        self.play(FadeOut(t1, t2, A, p))



class vid13(Scene):
    def construct(self):
             
    #DIFERENÇA PERTINÊNCIA E INCLUSÃO
        t1 = MathTex(r"\times", color=GREEN).scale(1)
        t2 = Tex(r"Pertinência", color=GREEN).next_to(t1, LEFT*1.6).scale(1.2)
        t3 = Tex(r"Inclusão", color=GREEN).next_to(t1, RIGHT*1.6).scale(1.2)

        t = VGroup(t1, t2, t3).shift(RIGHT*0.2).to_edge(UP)
        un = Underline(t, color=GREEN)

        tt = VGroup(t1, t2, t3, un)

        self.play(LaggedStart(Write(t2), Write(t1), Write(t3), Write(un), lag_ratio=0.5))
        self.wait()

        t4 = Tex("Pertinência", color=GREEN).shift(UP*2+LEFT*3).scale(1.2)
        t5 = Tex("Inclusão", color=GREEN).shift(UP*2+RIGHT*3).scale(1.2)

        ttt = VGroup(t4, t5)

        self.play(TransformMatchingShapes(tt, ttt))
        self.wait()

        t6 = Tex("elemento - conjunto").shift(UP*1+LEFT*3)
        t7 = MathTex(r"\in").scale(1.5).next_to(t6, DOWN*2)
        t8 = MathTex(r"\notin").scale(1.5).next_to(t7, DOWN*2)

        t9 = Tex("conjunto - conjunto").shift(UP*1+RIGHT*3)
        t10 = MathTex(r"\subset").scale(1.5).next_to(t9, DOWN*2)
        t11 = MathTex(r"\not\subset").scale(1.5).next_to(t10, DOWN*2)

        tg1 = VGroup(t10, t11).shift(LEFT)

        t12 = MathTex(r"\supset").scale(1.5).next_to(t9, DOWN*2)
        t13 = MathTex(r"\not\supset").scale(1.5).next_to(t12, DOWN*2)

        tg2 = VGroup(t12, t13).shift(RIGHT)

        self.play(FadeIn(t6))
        self.wait()
        self.play(FadeIn(t7))
        self.wait()
        self.play(FadeIn(t8))
        self.wait()
        self.play(FadeIn(t9))
        self.wait()
        self.play(FadeIn(t10))
        self.wait()
        self.play(FadeIn(t11))
        self.wait()
        self.play(FadeIn(t12))
        self.wait()
        self.play(FadeIn(t13))
        self.wait()

        self.play(FadeOut(ttt, t6, t7, t8, t9, t10, t11, t12, t13))
        self.wait()

        #conjunto-exemplo X
        X = MathTex(r"X = \left\{ a, b, c \right\}").scale(1.5)

        self.play(Write(X))
        self.wait()
        self.play(X.animate.shift(UP*2.5))
        self.wait()

        t14 = MathTex(r"a, b, c \: \in \: X").scale(1.3).shift(LEFT*2.5)
        t15 = MathTex(r"a, b, c \: \subset \: X").scale(1.3).shift(RIGHT*2.5)
        t15l = Line((-1.3,0.1,0), (1.3,-0.1,0), color=RED).scale(1.3).shift(RIGHT*2.5)
        
        self.play(FadeIn(t14))
        self.wait()
        self.play(LaggedStart(FadeIn(t15), Write(t15l), lag_ratio=1))
        self.wait()
        self.play(FadeOut(t14, t15, t15l))
        self.wait()

        t16 = MathTex(r"a").scale(1.3)
        t17 = MathTex(r"\left\{ a \right\}").scale(1.3)
        t18 = MathTex(r"\left\{ a \right\} \: \subset \: X").scale(1.3)
        t19 = MathTex(r"X \: \supset \: \left\{ a \right\}").scale(1.3).shift(RIGHT*2.5)

        self.play(Write(t16))
        self.wait()
        self.play(TransformMatchingShapes(t16, t17))
        self.wait()
        self.play(TransformMatchingShapes(t17, t18))
        self.wait()
        self.play(t18.animate.shift(LEFT*2.5), FadeIn(t19))
        self.wait()
        self.play(FadeOut(t18, t19))
        self.wait()

        t20 = MathTex(r"\text{\o} \: \subset \: X").scale(1.3).shift(LEFT*2.5)
        t21 = MathTex(r"\text{\o} \: \in \: X").scale(1.3).shift(RIGHT*2.5)
        t21l = Line((-0.9,0.1,0), (0.9,-0.1,0), color=RED).scale(1.3).shift(RIGHT*2.5)
        X2 = MathTex(r"X = \left\{ a, b, c, \text{\o} \right\}").scale(1.5).shift(UP*2.5)

        self.play(FadeIn(t20))
        self.wait()
        self.play(LaggedStart(FadeIn(t21), Write(t21l), lag_ratio=1))
        self.wait()
        self.play(TransformMatchingShapes(X, X2), FadeOut(t21l))
        self.wait()



class vid14(Scene):
    def construct(self):

    #OPERAÇÕES COM CONJUNTOS
        
    #conjuntos separados

        #conjunto A
        cA = Circle(radius=2, color=BLUE, fill_opacity=0.1)
        tA = MathTex("A", color=BLUE).next_to(cA, UL, buff=-0.6).scale(1.5).set_z_index(2)
        tAb = MathTex("A", color=BLACK, stroke_width=10).move_to(tA).scale(1.5).set_z_index(1)
        
        A = VGroup(cA, tA, tAb).shift(LEFT*2.5).scale(0.85)
        
        #conjunto B
        cB = Circle(radius=2, color=RED, fill_opacity=0.1)
        tB = MathTex("B", color=RED).next_to(cB, UR, buff=-0.6).scale(1.5).set_z_index(2)
        tBb = MathTex("B", color=BLACK, stroke_width=10).move_to(tB).scale(1.5).set_z_index(1)
        
        B = VGroup(cB, tB, tBb).shift(RIGHT*2.5).scale(0.85)
        
        #elementos
        a = MathTex("a").move_to((-3.5,0.5,0)).scale(1.3).scale(0.85)
        b = MathTex("b").move_to((-3,-1,0)).scale(1.3).scale(0.85)
        e = MathTex("e").move_to((3.5,0.5,0)).scale(1.5).scale(0.85)
        f = MathTex("f").move_to((3,-1,0)).scale(1.3).scale(0.85)

        #elementos comuns
        c1 = MathTex("c").move_to((-2,1,0)).scale(1.5).scale(0.85)
        d1 = MathTex("d").move_to((-1.5,-0.5,0)).scale(1.3).scale(0.85)
        c2 = MathTex("c").move_to((2,1,0)).scale(1.5).scale(0.85)
        d2 = MathTex("d").move_to((1.5,-0.5,0)).scale(1.3).scale(0.85)

        c1y = MathTex("c").move_to((-2,1,0)).scale(1.5).set_color(YELLOW).scale(0.85)
        d1y = MathTex("d").move_to((-1.5,-0.5,0)).scale(1.3).set_color(YELLOW).scale(0.85)
        c2y = MathTex("c").move_to((2,1,0)).scale(1.5).set_color(YELLOW).scale(0.85)
        d2y = MathTex("d").move_to((1.5,-0.5,0)).scale(1.3).set_color(YELLOW).scale(0.85)

        el = VGroup(a, b, e, f)
        cd = VGroup(c1, d1, c2, d2)
        cdy = VGroup(c1y, d1y, c2y, d2y)

        self.play(LaggedStart(Write(A), Write(B), FadeIn(el, cd), lag_ratio=0.5))
        self.wait()
        self.play(TransformMatchingShapes(cd, cdy))
        self.wait()

    #conjuntos A e B sobrepostos
        #conjunto A
        cA2 = Circle(radius=2, color=BLUE, fill_opacity=0.1)
        tA2 = MathTex("A", color=BLUE).next_to(cA2, UL, buff=-0.6).scale(1.5).set_z_index(2)
        tAb2 = MathTex("A", color=BLACK, stroke_width=10).move_to(tA2).scale(1.5).set_z_index(1)
        
        A2 = VGroup(cA2, tA2, tAb2).shift(LEFT).scale(0.85)
        
        #conjunto B
        cB2 = Circle(radius=2, color=RED, fill_opacity=0.1)
        tB2 = MathTex("B", color=RED).next_to(cB2, UR, buff=-0.6).scale(1.5).set_z_index(2)
        tBb2 = MathTex("B", color=BLACK, stroke_width=10).move_to(tB2).scale(1.5).set_z_index(1)
        
        B2 = VGroup(cB2, tB2, tBb2).shift(RIGHT).scale(0.85)

        #elementos
        a = MathTex("a").move_to((-3.5,0.5,0)).scale(1.3).shift(RIGHT*1.5).scale(0.85)
        b = MathTex("b").move_to((-3,-1,0)).scale(1.3).shift(RIGHT*1.5).scale(0.85)
        e = MathTex("e").move_to((3.5,0.5,0)).scale(1.5).shift(LEFT*1.5).scale(0.85)
        f = MathTex("f").move_to((3,-1,0)).scale(1.3).shift(LEFT*1.5).scale(0.85)

        #elementos comuns
        cy = MathTex("c").move_to((0,0.7,0)).scale(1.5).set_color(YELLOW).scale(0.85)
        dy = MathTex("d").move_to((0,-0.7,0)).scale(1.3).set_color(YELLOW).scale(0.85)
        c = MathTex("c").move_to((0,0.7,0)).scale(1.5).scale(0.85)
        d = MathTex("d").move_to((0,-0.7,0)).scale(1.3).scale(0.85)

        el2 = VGroup(a, b, e, f)
        cd2y = VGroup(cy, dy)  
        cd2 = VGroup(c, d)  

        self.play(TransformMatchingShapes(A, A2),
                  TransformMatchingShapes(B, B2),
                  TransformMatchingShapes(el, el2),
                  TransformMatchingShapes(cdy, cd2y))
        self.wait()
        self.play(TransformMatchingShapes(cd2y, cd2))
        self.wait()

        all = VGroup(A2, B2, el2, cd2)
        
    #união
        tun1 = Tex("União", color=GREEN).scale(1.2).to_edge(UP)
        u1 = Underline(tun1, color=GREEN)
        tun2 = MathTex(r"A \cup B").scale(1.2).to_edge(DOWN, buff=1)

        un = Union(cA2, cB2, color=YELLOW, fill_opacity=0.2)
        self.play(LaggedStart(FadeIn(un, tun1, u1), FadeIn(tun2), lag_ratio=0.7))
        self.wait()
        self.play(FadeOut(un, tun1, u1, tun2))
        self.wait()

    #interseção
        tint1 = Tex("Interseção", color=GREEN).scale(1.2).to_edge(UP)
        u2 = Underline(tint1, color=GREEN)
        tint2 = MathTex(r"A \cap B").scale(1.2).to_edge(DOWN, buff=1)

        int = Intersection(cA2, cB2, color=YELLOW, fill_opacity=0.2)
        self.play(LaggedStart(FadeIn(int, tint1, u2), FadeIn(tint2), lag_ratio=0.7))
        self.wait()
        self.play(FadeOut(int, tint1, u2, tint2))
        self.wait()

        self.play(FadeOut(all))
        self.wait()

    #propriedades da união
        tpun = Tex("Propriedades da União", color=GREEN).scale(1.2).to_edge(UP)
        u3 = Underline(tpun, color=GREEN)

        d1 = Dot((-3,1,0))
        d2 = Dot((-3,0,0))
        d3 = Dot((-3,-1,0))
        d4 = Dot((-3,-2,0))

        pun1 = MathTex(r"A \cup \text{\o} = A").scale(1.2).next_to(d1, RIGHT)
        pun2 = MathTex(r"A \cup A = A").scale(1.2).next_to(d2, RIGHT)
        pun3 = MathTex(r"A \cup B = B \cup A").scale(1.2).next_to(d3, RIGHT)
        pun4 = MathTex(r"A \subset B \rightarrow A \cup B = B").scale(1.2).next_to(d4, RIGHT)

        self.play(LaggedStart(Write(tpun), Write(u3), lag_ratio=0.6), run_time=1)
        self.wait()
        self.play(FadeIn(d1, pun1))
        self.wait()
        self.play(FadeIn(d2, pun2))
        self.wait()
        self.play(FadeIn(d3, pun3))
        self.wait()
        self.play(FadeIn(d4, pun4))
        self.wait()
        self.play(FadeOut(tpun, u3, d1, pun1, d2, pun2, d3, pun3, d4, pun4))
        self.wait()

    #propriedades da interseção
        tpint = Tex("Propriedades da Interseção", color=GREEN).scale(1.2).to_edge(UP)
        u4 = Underline(tpint, color=GREEN)

        d1_2 = Dot((-5,1,0))
        d2_2 = Dot((-5,0,0))
        d3_2 = Dot((-5,-1,0))
        d4_2 = Dot((-5,-2,0))

        pint1 = Tex(r"A e B não possuem elemento em comum").scale(1.2).next_to(d1_2, RIGHT)
        pint1_2 = MathTex(r"\rightarrow A \cap B = \text{\o}").scale(1.2).next_to(d2_2, RIGHT)
        pint2 = MathTex(r"A \cap \text{\o} = \text{\o}").scale(1.2).next_to(d3_2, RIGHT)
        pint3 = MathTex(r"A \cap A = A").scale(1.2).next_to(d4_2, RIGHT)
        pint4 = MathTex(r"A \cap B = B \cap A").scale(1.2).next_to(d1_2, RIGHT)
        pint5 = MathTex(r"A \subset B \rightarrow A \cap B = A").scale(1.2).next_to(d2_2, RIGHT)

        self.play(LaggedStart(Write(tpint), Write(u4), lag_ratio=0.6), run_time=1)
        self.wait()
        self.play(FadeIn(d1_2, pint1, pint1_2))
        self.wait()
        self.play(FadeIn(d3_2, pint2))
        self.wait()
        self.play(FadeIn(d4_2, pint3))
        self.wait()
        self.play(FadeOut(d1_2, d3_2, d4_2, pint1, pint1_2, pint2, pint3))
        self.wait()
        self.play(FadeIn(d1_2, pint4))
        self.wait()
        self.play(FadeIn(d2_2, pint5))
        self.wait()
        self.play(FadeOut(tpint, u4, d1_2, d2_2, pint4, pint5))
        self.wait()

    #diferença
        tdif1 = Tex("Diferença", color=GREEN).scale(1.2).to_edge(UP)
        u5 = Underline(tdif1, color=GREEN)
        tdif2 = MathTex(r"A - B").scale(1.2).to_edge(DOWN, buff=1)
        tdif3 = MathTex(r"A \: \backslash \: B").scale(1.2).to_edge(DOWN, buff=0.85)

        dif = Difference(cA2, cB2, color=YELLOW, fill_opacity=0.2)
        self.play(LaggedStart(FadeIn(all), FadeIn(tdif1, u5), FadeIn(tdif2), lag_ratio=0.7))
        self.wait()
        self.play(FadeIn(dif))
        self.wait()
        self.play(TransformMatchingShapes(tdif2, tdif3))
        self.wait()
        self.play(FadeOut(dif, tdif1, u5, tdif3))
        self.wait()

        #diferença simétrica
        tds1 = Tex("Diferença simétrica", color=YELLOW).scale(1.2).to_edge(UP)
        tds2 = MathTex(r"(A \cup B) \: \backslash \: (A \cap B)").scale(1.2).to_edge(DOWN, buff=1)
        tds3 = MathTex(r"(A - B) \cup (B - A)").scale(1.2).to_edge(DOWN, buff=1)

        difsim_1 = Difference(cA2, cB2, color=YELLOW, fill_opacity=0.2)
        difsim_2 = Difference(cB2, cA2, color=YELLOW, fill_opacity=0.2)
        difsim = VGroup(difsim_1, difsim_2)

        self.play(FadeIn(tds1, difsim))
        self.wait()
        self.play(FadeIn(tds2))
        self.wait()
        self.play(TransformMatchingTex(tds2, tds3))
        self.wait()
        self.play(FadeOut(all, tds1, tds3, difsim))
        self.wait()

    #propriedades da diferença
        tpd = Tex("Propriedades da Diferença", color=GREEN).scale(1.2).to_edge(UP)
        u6 = Underline(tpd, color=GREEN)

        d1 = Dot((-3,1,0))
        d2 = Dot((-3,0,0))
        d3 = Dot((-3,-1,0))
        d4 = Dot((-3,-2,0))

        pd1 = MathTex(r"A \: \backslash \: \text{\o} = A").scale(1.2).next_to(d1, RIGHT)
        pd2 = MathTex(r"A \: \backslash \: A = \text{\o}").scale(1.2).next_to(d2, RIGHT)
        pd3 = MathTex(r"A \: \backslash \: B \neq B \: \backslash \: A").scale(1.2).next_to(d3, RIGHT)
        pd4 = MathTex(r"A \subset B \rightarrow A \: \backslash \: B = \text{\o}").scale(1.2).next_to(d4, RIGHT)

        self.play(LaggedStart(Write(tpd), Write(u6), lag_ratio=0.6), run_time=1)
        self.wait()
        self.play(FadeIn(d1, pd1))
        self.wait()
        self.play(FadeIn(d2, pd2))
        self.wait()
        self.play(FadeIn(d3, pd3))
        self.wait()
        self.play(FadeIn(d4, pd4))
        self.wait()
        self.play(FadeOut(tpd, u6, d1, pd1, d2, pd2, d3, pd3, d4, pd4))
        self.wait()
    


class vid15(Scene):
    def construct(self):

    #CONJUNTO UNIVERSO E COMPLEMENTAR
        #conjunto A
        cA = Circle(radius=2, color=BLUE, fill_opacity=0.1)
        tA = MathTex("A", color=BLUE).next_to(cA, UL, buff=-0.6).scale(1.5).set_z_index(2)
        tAb = MathTex("A", color=BLACK, stroke_width=10).move_to(tA).scale(1.5).set_z_index(1)
        
        A = VGroup(cA, tA, tAb).scale(0.85)

        #elementos de A
        x = MathTex("x").move_to((-0.8,0.5,0)).scale(1.3)
        y = MathTex("y").move_to((-0.1,-1,0)).scale(1.3)    
        z = MathTex("z").move_to((1,0,0)).scale(1.5) 

        el = VGroup(x, y, z)

        #conjunto universo
        t1 = Tex("Conjunto universo", color=YELLOW).scale(1.2).to_edge(UP)

        cU = RoundedRectangle(height=5, width=10, color=PURPLE, fill_opacity=0.1)
        tU = MathTex("U", color=PURPLE).shift(UP*2.6+LEFT*4).scale(1.5).set_z_index(2)
        tUb = MathTex("U", color=BLACK, stroke_width=10).move_to(tU).scale(1.5).set_z_index(1)
        
        U = VGroup(cU, tU, tUb).scale(0.85)

        self.play(LaggedStart(DrawBorderThenFill(cA), FadeIn(tA, tAb), FadeIn(x, y, z), lag_ratio=0.6))
        self.wait()
        self.play(FadeIn(t1))
        self.wait()
        self.play(LaggedStart(DrawBorderThenFill(cU), FadeIn(tU, tUb), lag_ratio=0.6))
        self.wait()
        self.play(FadeOut(t1))
        self.wait()

    #complementar
        tc1 = Tex("Complementar", color=GREEN).scale(1.2).to_edge(UP)
        u1 = Underline(tc1, color=GREEN)
        tc2 = MathTex(r"A","^ c").scale(1.2).to_edge(DOWN, buff=1)
        tc2[0].set_color(BLUE)
        tc3 = MathTex(r"A","^ c = ","U"," - ","A").scale(1.2).to_edge(DOWN, buff=1)
        tc3[0].set_color(BLUE)
        tc3[2].set_color(PURPLE)
        tc3[4].set_color(BLUE)

        comp = Difference(cU, cA, color=YELLOW, fill_opacity=0.2)

        self.play(LaggedStart(FadeIn(comp, tc1, u1), FadeIn(tc2), lag_ratio=0.7))
        self.wait()
        self.play(TransformMatchingShapes(tc2, tc3))
        self.wait()
        self.play(FadeOut(comp, tc3))
        self.wait()

    #complementar de A em relação a B
        #conjunto B
        cB = Circle(radius=2, color=RED, fill_opacity=0.1)
        tB = MathTex("B", color=RED).next_to(cB, UR, buff=-0.6).scale(1.5).set_z_index(2)
        tBb = MathTex("B", color=BLACK, stroke_width=10).move_to(tB).scale(1.5).set_z_index(1)
        
        B = VGroup(cB, tB, tBb).scale(0.85)

        c1 = Circle(radius=2).scale(0.85).scale(0.6)
        c2 = Circle(radius=2).scale(0.85)
        comp2 = Difference(c2, c1, color=YELLOW, fill_opacity=0.2)

        tc4 = MathTex(r"A","^ c = ","B"," - ","A").scale(1.2).to_edge(DOWN, buff=1)
        tc4[0].set_color(BLUE)
        tc4[2].set_color(RED)
        tc4[4].set_color(BLUE)
        
        self.play(A.animate.scale(0.6), el.animate.scale(0.6))
        self.wait()
        self.play(FadeIn(B))
        self.wait()
        self.play(FadeIn(comp2))
        self.wait()
        self.play(FadeIn(tc4))
        self.wait()

        self.play(FadeOut(tc1, u1, A, el, B, U, comp2, tc4))
        self.wait()

        #propriedades do complementar
        tpc = Tex("Propriedades do Complementar", color=GREEN).scale(1.2).to_edge(UP)
        u6 = Underline(tpc, color=GREEN)

        d1 = Dot((-3,1,0))
        d2 = Dot((-3,0,0))
        d3 = Dot((-3,-1,0))
        d4 = Dot((-3,-2,0))

        pc1 = MathTex(r"\text{\o} ^ c = U").scale(1.2).next_to(d1, RIGHT)
        pc2 = MathTex(r"U ^ c = \text{\o}").scale(1.2).next_to(d2, RIGHT)
        pc3 = MathTex(r"(A ^ c) ^ c = A").scale(1.2).next_to(d3, RIGHT)
        pc4 = MathTex(r"A \subset B \rightarrow B ^ c \subset A ^ c").scale(1.2).next_to(d4, RIGHT)

        self.play(LaggedStart(Write(tpc), Write(u6), lag_ratio=0.6), run_time=1)
        self.wait()
        self.play(FadeIn(d1, pc1))
        self.wait()
        self.play(FadeIn(d2, pc2))
        self.wait()
        self.play(FadeIn(d3, pc3))
        self.wait()
        self.play(FadeIn(d4, pc4))
        self.wait()
        self.play(FadeOut(tpc, u6, d1, pc1, d2, pc2, d3, pc3, d4, pc4))
        self.wait()


        
class imgs(Scene):
    def construct(self):

    #IMAGENS PARA AS PROPRIEDADES
    #props da inclusão
        #conjunto A
        cA = Circle(radius=1.2, color=BLUE, fill_opacity=0.1)
        tA = MathTex("A", color=BLUE).next_to(cA, UL, buff=-0.5).scale(1.5).set_z_index(2)
        tAb = MathTex("A", color=BLACK, stroke_width=10).move_to(tA).scale(1.5).set_z_index(1)
        
        A = VGroup(cA, tA, tAb)

        #conjunto B
        cB = Circle(radius=2, color=RED, fill_opacity=0.1)
        tB = MathTex("B", color=RED).next_to(cB, UR, buff=-0.6).scale(1.5).set_z_index(2)
        tBb = MathTex("B", color=BLACK, stroke_width=10).move_to(tB).scale(1.5).set_z_index(1)
        
        B = VGroup(cB, tB, tBb)

        #conjunto C
        cC = Circle(radius=2.5, color=GREEN, fill_opacity=0.1)
        tC = MathTex("B", color=GREEN).next_to(cC, UR, buff=-0.6).scale(1.5).set_z_index(2)
        tCb = MathTex("C", color=BLACK, stroke_width=10).move_to(tC).scale(1.5).set_z_index(1)
        
        C = VGroup(cC, tC, tCb)

        #conjunto universo
        t1 = Tex("Conjunto universo", color=YELLOW).scale(1.2).to_edge(UP)

        cU = RoundedRectangle(height=5, width=8, color=PURPLE, fill_opacity=0.1)
        tU = MathTex("U", color=PURPLE).shift(UP*2.6+LEFT*2.8).scale(1.5).set_z_index(2)
        tUb = MathTex("U", color=BLACK, stroke_width=10).move_to(tU).scale(1.5).set_z_index(1)
        
        U = VGroup(cU, tU, tUb)

        d = Difference(cU, cA, color=YELLOW, fill_opacity=0.2)


        #conjunto A
        cA2 = Circle(radius=2, color=BLUE, fill_opacity=0.1)
        tA2 = MathTex("A", color=BLUE).next_to(cA2, UL, buff=-0.6).scale(1.5).set_z_index(2)
        tAb2 = MathTex("A", color=BLACK, stroke_width=10).move_to(tA2).scale(1.5).set_z_index(1)
        
        A2 = VGroup(cA2, tA2, tAb2).shift(LEFT).scale(0.85)
        
        #conjunto B
        cB2 = Circle(radius=2, color=RED, fill_opacity=0.1)
        tB2 = MathTex("B", color=RED).next_to(cB2, UR, buff=-0.6).scale(1.5).set_z_index(2)
        tBb2 = MathTex("B", color=BLACK, stroke_width=10).move_to(tB2).scale(1.5).set_z_index(1)
        
        B2 = VGroup(cB2, tB2, tBb2).shift(RIGHT).scale(0.85)

        d = Difference(cB2, cA2, color=YELLOW, fill_opacity=0.2)

        self.add(A2, B2, d)
