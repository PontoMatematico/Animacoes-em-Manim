# Conjuntos Numéricos

from manim import*   

# THUMBNAIL (OK)
class tn(Scene):
    def construct(self):

        cN = Ellipse(width=2, height=2, color=LIGHT_PINK, fill_opacity=0.2).set_z_index(6)
        tN = MathTex(r"\mathbb{N}", color=LIGHT_PINK).move_to(cN).set_z_index(7).scale(1.8)
        tNb = MathTex(r"\mathbb{N}", color=BLACK, stroke_width=7).move_to(tN).set_z_index(6).scale(1.8)
        n1 = MathTex("1").move_to(cN).shift(UP*0.5)
        n2 = MathTex("0").move_to(cN).shift(LEFT*0.5+DOWN*0.2)
        n3 = MathTex("2").move_to(cN).shift(RIGHT*0.4+DOWN*0.3)
        nN = VGroup(n1, n2, n3).set_z_index(7)
        N = VGroup(cN, tN, tNb).shift(LEFT*2.5)

        cZ = Ellipse(width=4.5, height=3, color=BLUE, fill_opacity=0.2).set_z_index(5)
        tZ = MathTex(r"\mathbb{Z}", color=BLUE).next_to(cN, RIGHT, buff=2.5).set_z_index(6).scale(2)
        tZb = MathTex(r"\mathbb{Z}", color=BLACK, stroke_width=7).move_to(tZ).set_z_index(5).scale(2)
        n4 = MathTex("-1").move_to(cZ).shift(RIGHT*0.7+UP*0.7)
        n5 = MathTex("-2").move_to(cZ).shift(RIGHT*1.5)
        n6 = MathTex("-3").move_to(cZ).shift(RIGHT*0.9+DOWN*0.7)
        nZ = VGroup(n4, n5, n6).set_z_index(6)      
        Z = VGroup(cZ, tZ, tZb).shift(LEFT*1.8)

        cQ = Ellipse(width=7, height=4, color=GREEN, fill_opacity=0.2).set_z_index(4)
        tQ = MathTex(r"\mathbb{Q}", color=GREEN).next_to(cZ, RIGHT, buff=1.7).set_z_index(5).scale(2.2)
        tQb = MathTex(r"\mathbb{Q}", color=BLACK, stroke_width=7).move_to(tQ).set_z_index(4).scale(2.2)
        n7 = MathTex(r"1 \over 2").move_to(cQ).shift(RIGHT*1.9+UP*0.8)
        n8 = MathTex(r"7 \over 3").move_to(cQ).shift(RIGHT*2.7)
        n9 = MathTex(r"0,111...").move_to(cQ).shift(RIGHT*2+DOWN).scale(0.9)
        nQ = VGroup(n7, n8, n9).set_z_index(5)
        Q = VGroup(cQ, tQ, tQb).shift(LEFT)

        cR = Ellipse(width=9.5, height=5, color=ORANGE, fill_opacity=0.2).set_z_index(3).shift(RIGHT*0.3)
        tR = MathTex(r"\mathbb{R}", color=ORANGE).next_to(cQ, RIGHT, buff=1.3).set_z_index(4).scale(2.4)
        tRb = MathTex(r"\mathbb{R}", color=BLACK, stroke_width=7).move_to(tR).set_z_index(3).scale(2.4)
        n10 = MathTex(r"\pi").move_to(cR).shift(RIGHT*3.25+UP).scale(1.3)
        n11 = MathTex(r"\sqrt{2}").move_to(cR).shift(RIGHT*3.8)
        n12 = MathTex(r"e").move_to(cR).shift(RIGHT*3.3+DOWN).scale(1.2)
        nR = VGroup(n10, n11, n12).set_z_index(4)
        R = VGroup(cR, tR, tRb).shift(LEFT*0.5)

        cC = Ellipse(width=12, height=6, color=RED, fill_opacity=0.2).set_z_index(2).shift(RIGHT*0.3)
        tC = MathTex(r"\mathbb{C}", color=RED).next_to(cR, RIGHT, buff=0.5).set_z_index(3).scale(2.6)
        tCb = MathTex(r"\mathbb{C}", color=BLACK, stroke_width=7).move_to(tC).set_z_index(2).scale(2.6)
        n13 = MathTex(r"\sqrt{-1}").move_to(cC).shift(RIGHT*4.3+UP)
        n14 = MathTex(r"3+2i").move_to(cC).shift(RIGHT*4.6+DOWN*0.5)
        nC = VGroup(n13, n14).set_z_index(3)
        C = VGroup(cC, tC, tCb).shift(RIGHT*0.3)

        cN2 = Ellipse(width=2, height=2, color=LIGHT_PINK, fill_opacity=0, stroke_opacity=0.4).set_z_index(6).shift(LEFT*2.5)
        cZ2 = Ellipse(width=4.5, height=3, color=BLUE, fill_opacity=0, stroke_opacity=0.4).set_z_index(5).shift(LEFT*1.8)
        cQ2 = Ellipse(width=7, height=4, color=GREEN, fill_opacity=0, stroke_opacity=0.45).set_z_index(4).shift(LEFT)
        cR2 = Ellipse(width=9.5, height=5, color=ORANGE, fill_opacity=0, stroke_opacity=0.5).set_z_index(3).shift(RIGHT*0.3).shift(LEFT*0.5)
        cC2 = Ellipse(width=12, height=6, color=RED, fill_opacity=0, stroke_opacity=0.5).set_z_index(2).shift(RIGHT*0.3).shift(RIGHT*0.3)
        
        g3 = VGroup(cN2, cZ2, cQ2, cR2, cC2).scale(0.8).move_to((0,0,0)).shift(DOWN)

        self.add(g3)

        g = VGroup(N, Z, Q, R, C).scale(0.8).move_to((0,0,0)).shift(DOWN)
        g1 = VGroup(cN, cZ, cQ, cR, cC).set_opacity(0.2)

        t = Tex("Conjuntos Numéricos").shift(UP*2.5).scale(2).set_color(color=[WHITE, GRAY_C])

        self.add(g, t)

# INTRODUÇÃO (OK)
class vid0(Scene):
    def construct(self):

        cN = Ellipse(width=2, height=2, color=LIGHT_PINK, fill_opacity=0.2).set_z_index(6)
        tN = MathTex(r"\mathbb{N}", color=LIGHT_PINK).move_to(cN).set_z_index(7).scale(1.5)
        tNb = MathTex(r"\mathbb{N}", color=BLACK, stroke_width=6).move_to(tN).set_z_index(6).scale(1.5)
        n1 = MathTex("1").move_to(cN).shift(UP*0.5)
        n2 = MathTex("0").move_to(cN).shift(LEFT*0.5+DOWN*0.2)
        n3 = MathTex("2").move_to(cN).shift(RIGHT*0.4+DOWN*0.3)
        nN = VGroup(n1, n2, n3).set_z_index(7)
        N = VGroup(cN, tN, tNb).shift(LEFT*2.5)

        cZ = Ellipse(width=4.5, height=3, color=BLUE, fill_opacity=0.2).set_z_index(5)
        tZ = MathTex(r"\mathbb{Z}", color=BLUE).next_to(cN, RIGHT, buff=2.5).set_z_index(6).scale(1.5)
        tZb = MathTex(r"\mathbb{Z}", color=BLACK, stroke_width=6).move_to(tZ).set_z_index(5).scale(1.5)
        n4 = MathTex("-1").move_to(cZ).shift(RIGHT*0.7+UP*0.7)
        n5 = MathTex("-2").move_to(cZ).shift(RIGHT*1.5)
        n6 = MathTex("-3").move_to(cZ).shift(RIGHT*0.9+DOWN*0.7)
        nZ = VGroup(n4, n5, n6).set_z_index(6)      
        Z = VGroup(cZ, tZ, tZb).shift(LEFT*1.8)

        cQ = Ellipse(width=7, height=4, color=GREEN, fill_opacity=0.2).set_z_index(4)
        tQ = MathTex(r"\mathbb{Q}", color=GREEN).next_to(cZ, RIGHT, buff=1.7).set_z_index(5).scale(1.5)
        tQb = MathTex(r"\mathbb{Q}", color=BLACK, stroke_width=6).move_to(tQ).set_z_index(4).scale(1.5)
        n7 = MathTex(r"1 \over 2").move_to(cQ).shift(RIGHT*1.9+UP*0.8)
        n8 = MathTex(r"7 \over 3").move_to(cQ).shift(RIGHT*2.7)
        n9 = MathTex(r"0,111...").move_to(cQ).shift(RIGHT*2+DOWN).scale(0.9)
        nQ = VGroup(n7, n8, n9).set_z_index(5)
        Q = VGroup(cQ, tQ, tQb).shift(LEFT)

        cR = Ellipse(width=9.5, height=5, color=ORANGE, fill_opacity=0.2).set_z_index(3).shift(RIGHT*0.3)
        tR = MathTex(r"\mathbb{R}", color=ORANGE).next_to(cQ, RIGHT, buff=1.3).set_z_index(4).scale(1.5)
        tRb = MathTex(r"\mathbb{R}", color=BLACK, stroke_width=6).move_to(tR).set_z_index(3).scale(1.5)
        n10 = MathTex(r"\pi").move_to(cR).shift(RIGHT*3.25+UP).scale(1.3)
        n11 = MathTex(r"\sqrt{2}").move_to(cR).shift(RIGHT*3.8)
        n12 = MathTex(r"e").move_to(cR).shift(RIGHT*3.3+DOWN).scale(1.2)
        nR = VGroup(n10, n11, n12).set_z_index(4)
        R = VGroup(cR, tR, tRb).shift(LEFT*0.5)

        cC = Ellipse(width=12, height=6, color=RED, fill_opacity=0.2).set_z_index(2).shift(RIGHT*0.3)
        tC = MathTex(r"\mathbb{C}", color=RED).next_to(cR, RIGHT, buff=0.5).set_z_index(3).scale(1.5)
        tCb = MathTex(r"\mathbb{C}", color=BLACK, stroke_width=6).move_to(tC).set_z_index(2).scale(1.5)
        n13 = MathTex(r"\sqrt{-1}").move_to(cC).shift(RIGHT*4.3+UP)
        n14 = MathTex(r"3+2i").move_to(cC).shift(RIGHT*4.6+DOWN*0.5)
        nC = VGroup(n13, n14).set_z_index(3)
        C = VGroup(cC, tC, tCb).shift(RIGHT*0.3)

        g = VGroup(cN, cZ, cQ, cR, cC).move_to(ORIGIN)

        t1 = MathTex("5").move_to(tN).scale(1.5)
        t2 = MathTex("-2").move_to(tZ).scale(1.5)
        t3 = MathTex(r"{9 \over 4}").move_to(tQ).scale(1.5)
        t4 = MathTex(r"\sqrt{3}").move_to(tR).scale(1.5).shift(LEFT*0.1)
        t5 = MathTex(r"\sqrt{-3}").move_to(tC).scale(1.5)

        g2 = VGroup(t1, t2, t3, t4, t5).move_to(ORIGIN)

        gt = VGroup(tN, tZ, tQ, tR, tC, tNb, tZb, tQb, tRb, tCb).shift(LEFT*0.6)

        self.play(LaggedStart(FadeIn(t1),
                              FadeIn(t2),
                              FadeIn(t3),
                              FadeIn(t4),
                              FadeIn(t5),
                              lag_ratio=0.5))
        self.wait(3)

        self.play(g2.animate.shift(RIGHT*1.2))
        
        self.play(LaggedStart(DrawBorderThenFill(cN),
                              DrawBorderThenFill(cZ),
                              DrawBorderThenFill(cQ),
                              DrawBorderThenFill(cR),
                              DrawBorderThenFill(cC),
                              lag_ratio=0.2))
        self.wait(3)

        self.play(LaggedStart(FadeOut(t1), FadeIn(tN, tNb),
                              FadeOut(t2), FadeIn(tZ, tZb),
                              FadeOut(t3), FadeIn(tQ, tQb),
                              FadeOut(t4), FadeIn(tR, tRb),
                              FadeOut(t5), FadeIn(tC, tCb),
                              lag_ratio=0.3))
        self.wait(3)

# NATURAIS (OK)
class vid1(Scene):
    def construct(self):

        # Definição

        t1 = MathTex("1, \: 2, \: 3, \: ...").scale(1.2).shift(RIGHT*0.5)
        t2 = MathTex("0").shift(UP).scale(1.2)
        g1 = VGroup(t1, t2)
        t3 = MathTex(r"\{ 0, \: 1, \: 2, \: 3, \: ... \}").shift(DOWN*0.5)
        t4 = MathTex(r"\mathbb{N}"," = \{ 0, \: 1, \: 2, \: 3, \: ... \}").shift(DOWN*0.5)
        t4[0].set_color(LIGHT_PINK)

        self.wait()
        self.play(Write(t1), run_time=2)
        self.wait(3)
        self.play(t1.animate.shift(DOWN))
        self.play(Write(t2))
        self.wait(3)
        self.play(TransformMatchingTex(g1, t3))
        self.wait(4)

        Nc = MathTex(r"\mathbb{N}", color=LIGHT_PINK).scale(1.5).to_corner(UL)
        tN = Tex("Números Naturais").scale(1.2).shift(UP*2)
        tNsr = SurroundingRectangle(tN, buff=0.2, color=LIGHT_PINK, fill_opacity=0.2)
        
        self.play(FadeIn(tN))
        self.play(Create(tNsr))
        self.wait(3)

        tNe_1 = MathTex("Natural", color=GRAY).next_to(t4, DOWN, buff=0.2).shift(LEFT*2)
        tNe_2 = Tex("`", color=GRAY).next_to(tNe_1, LEFT, buff=0.1).shift(UP*0.1)
        tNe_3 = Tex("'", color=GRAY).next_to(tNe_1, RIGHT, buff=0.1).shift(UP*0.1)
        tNe = VGroup(tNe_1, tNe_2, tNe_3)

        self.play(TransformMatchingShapes(t3, t4))
        self.wait()
        self.play(FadeIn(tNe))
        self.play(FadeOut(tNe))
        self.wait(3)

        all_1 = VGroup(tN, tNsr, t4)
        self.play(FadeOut(all_1), t4[0].animate.move_to(Nc).scale(1.5))
        self.add(Nc)
        self.wait(3)
        
        # Soma de naturais
        
        t5_1 = MathTex("2 + 1").shift(UP*2)
        t5_2 = MathTex("= 3").next_to(t5_1, RIGHT, buff=0.2)

        t6_1 = MathTex("5 + 5")
        t6_2 = MathTex("= 10").next_to(t6_1, RIGHT, buff=0.2)

        t7_1 = MathTex("2 + 5").shift(DOWN*2)
        t7_2 = MathTex("= 7").next_to(t7_1, RIGHT, buff=0.2)

        soma = VGroup(t5_1, t6_1, t7_1, t5_2, t6_2, t7_2).shift(LEFT)
        
        self.play(LaggedStart(FadeIn(t5_1), FadeIn(t6_1), FadeIn(t7_1), lag_ratio=0.5))
        self.wait(3)
        self.play(LaggedStart(FadeIn(t5_2), FadeIn(t6_2), FadeIn(t7_2), lag_ratio=0.5))
        self.wait(3)

        all_2 = VGroup(t5_1, t6_1, t7_1, t5_2, t6_2, t7_2)
        self.play(FadeOut(all_2))


        # Subtração de naturais (Problema)

        # a - b, a >= b

        ts_1 = MathTex("a-b", color=YELLOW).scale(1.2)
        ts_2 = MathTex(r"\:\:\: , \:\:\: a \ge b", color=YELLOW).scale(1.2).next_to(ts_1, RIGHT, buff=0.5)
        g = VGroup(ts_1, ts_2).move_to((0,2,0))

        t8 = MathTex("2 - 1 = 1")

        t9 = MathTex("5 - 5 = 0").shift(DOWN*2)

        t10 = MathTex("2 - 5 = \: ?").shift(DOWN*0.8)
        
        self.play(FadeIn(ts_1))
        self.play(FadeIn(ts_2))
        self.wait(3)
        self.play(FadeIn(t8))
        self.play(FadeIn(t9))
        self.wait(3)

        # a - b, a < b

        ts_3 = MathTex(r"\:\:\: , \:\:\: a < b", color=YELLOW).scale(1.2).next_to(ts_1, RIGHT, buff=0.5)

        self.play(FadeOut(t8, t9))
        self.play(TransformMatchingShapes(ts_2, ts_3))
        self.wait(3)
        self.play(FadeIn(t10))
        self.wait(3)

        all_3 = VGroup(ts_1, ts_3, t10, Nc)
        self.play(FadeOut(all_3))

# INTEIROS (OK)
class vid2(Scene):
    def construct(self):

        # Definição
        
        Zc = MathTex(r"\mathbb{Z}", color=BLUE).scale(1.5).to_corner(UL)
        tZ = Tex("Números Inteiros").scale(1.2).shift(UP*2)
        tZsr = SurroundingRectangle(tZ, buff=0.2, color=BLUE, fill_opacity=0.2)

        t1 = MathTex("-1, \: -2, \: -3, \: ...").shift(RIGHT*0.5).scale(1.2)
        t2 = MathTex(r"-1, \: -2, \: -3, \: ... \: \cup \: ",r"\mathbb{N}").scale(1.2)
        t2[1].set_color(LIGHT_PINK)
        t3 = MathTex(r"\{ ... \: , \: -3, \: -2, \: -1, \:\: 0, \:\: 1, \:\: 2, \:\: 3, \: ... \}").shift(DOWN*0.5)
        t4 = MathTex(r"\mathbb{Z}",r"= \{ ... \: , \: -3, \: -2, \: -1, \:\: 0, \:\: 1, \:\: 2, \:\: 3, \: ... \}").shift(DOWN*0.5)
        t4[0].set_color(BLUE)

        tZe_1 = MathTex("Zahlen", color=GRAY).next_to(t4, DOWN, buff=0.2).shift(LEFT*4)
        tZe_2 = Tex("`", color=GRAY).next_to(tZe_1, LEFT, buff=0.1).shift(UP*0.1)
        tZe_3 = Tex("'", color=GRAY).next_to(tZe_1, RIGHT, buff=0.1).shift(UP*0.1)
        tZe = VGroup(tZe_1, tZe_2, tZe_3)

        a1 = Arrow((0, 0, 0), (3, 0, 0), tip_length=0.3, stroke_width=3).shift(DOWN*1.5+RIGHT*1.3)
        a2 = Arrow((0, 0, 0), (-3, 0, 0), tip_length=0.3, stroke_width=3).shift(DOWN*1.5+RIGHT*0.8)
        
        self.play(Write(t1), run_time = 2)
        self.wait(3)
        self.play(ReplacementTransform(t1, t2))
        self.wait(3)
        self.play(TransformMatchingTex(t2, t3))
        self.wait(3)
        self.play(FadeIn(tZ))
        self.play(Create(tZsr))
        self.wait(3)
        self.play(TransformMatchingTex(t3, t4))
        self.wait()
        self.play(FadeIn(tZe))
        self.play(FadeOut(tZe))
        self.wait(3)
        self.play(GrowArrow(a1))
        self.play(FadeOut(a1))
        self.wait(3)
        self.play(GrowArrow(a2))
        self.play(FadeOut(a2))
        self.wait()

        all_1 = VGroup(tZ, tZsr, t4)
        self.play(FadeOut(all_1), t4[0].animate.move_to(Zc).scale(1.5))
        self.add(Zc)

        # Operações com inteiros

        # Soma, Subtração, Multiplicação
        
        t5_1 = MathTex("-2 + 4").shift(UP*2)
        t5_2 = MathTex("= 2").next_to(t5_1, RIGHT, buff=0.2)

        t6_1 = MathTex(r"3 - 5")
        t6_2 = MathTex("= -2").next_to(t6_1, RIGHT, buff=0.2)

        t7_1 = MathTex("-3 \cdot 2").shift(DOWN*2)
        t7_2 = MathTex("= -6").next_to(t7_1, RIGHT, buff=0.2)

        operacoes = VGroup(t5_1, t5_2, t6_1, t6_2, t7_1, t7_2).shift(LEFT*1)
        
        self.play(LaggedStart(FadeIn(t5_1), FadeIn(t6_1), FadeIn(t7_1), lag_ratio=0.5))
        self.wait(3)
        self.play(LaggedStart(FadeIn(t5_2), FadeIn(t6_2), FadeIn(t7_2), lag_ratio=0.5))
        self.wait(3)

        all_2 = VGroup(t5_1, t5_2, t6_1, t6_2, t7_1, t7_2)
        self.play(FadeOut(all_2))

        # Divisão (problema)

        ts_1 = MathTex(r"a \div b", color=YELLOW).scale(1.2)
        ts_2 = MathTex(r"\:\:\: , \:\:\: a = k \cdot b", color=YELLOW).scale(1.2).next_to(ts_1, RIGHT, buff=0.6)
        g = VGroup(ts_1, ts_2).move_to((0,2,0))
        ts_2_2 = MathTex(r"(b \neq 0)", color=YELLOW, opacity=0.5).scale(1.2).next_to(ts_2, DOWN).shift(RIGHT*0.9).scale(0.8)
        ts_3 = MathTex(r"\:\:\: , \:\:\: a \neq k \cdot b", color=YELLOW).scale(1.2).move_to(ts_2)

        t8 = MathTex(r"{3 \over 1} = 3").shift(LEFT*2+DOWN*0.8)

        t9 = MathTex(r"{8 \over 4} = 2").shift(RIGHT*2+DOWN*0.8)

        t10 = MathTex(r"{3 \over 4} = \: ?").shift(LEFT*2+DOWN*0.8)

        t11 = MathTex(r"{2 \over 9} = \: ?").shift(RIGHT*2+DOWN*0.8)

        self.play(FadeIn(ts_1))
        self.wait(3)
        self.play(FadeIn(ts_2))
        self.wait(3)
        self.play(FadeIn(ts_2_2))
        self.wait(3)
        self.play(FadeOut(ts_2_2))
        self.wait(3)
        self.play(FadeIn(t8))
        self.play(FadeIn(t9))
        self.wait(3)
        self.play(FadeOut(t8, t9))
        self.play(TransformMatchingTex(ts_2, ts_3))
        self.wait(3)
        self.play(FadeIn(t10))
        self.wait(3)
        self.play(FadeIn(t11))
        self.wait(3)

        all_3 = VGroup(ts_1, ts_3, t10, t11, Zc)
        self.play(FadeOut(all_3))

# RACIONAIS
class vid3(Scene):
    def construct(self):

        # Definição

        Qc = MathTex(r"\mathbb{Q}", color=GREEN).scale(1.5).to_corner(UL)
        tQ = Tex("Números Racionais").scale(1.2).shift(UP*2)
        tQsr = SurroundingRectangle(tQ, buff=0.2, color=GREEN, fill_opacity=0.2)

        self.play(FadeIn(tQ))
        self.play(Create(tQsr))
        self.wait(3)

        t3_1 = MathTex(r"\biggl\{",r"{a \over b}",r"\:\: \biggr\rvert \:\: a,b \in \mathbb{Z} \:\:,\:\: b \neq 0 \biggr\}").shift(DOWN*0.8)
        t3_1[1].set_color(YELLOW)

        t3_2 = MathTex(r"\biggl\{ {a \over b} \:\: \biggr\rvert \:\: ",r"a,b \in \mathbb{Z}",r" \:\:,\:\: b \neq 0 \biggr\}").shift(DOWN*0.8)
        t3_2[1].set_color(YELLOW)

        t3_3 = MathTex(r"\biggl\{ {a \over b} \:\: \biggr\rvert \:\: a,b \in \mathbb{Z} \:\:,\:\: ",r"b \neq 0 ",r"\biggr\}").shift(DOWN*0.8)
        t3_3[1].set_color(YELLOW)

        t3_4 = MathTex(r"\biggl\{ {a \over b} \:\: \biggr\rvert \:\: a,b \in \mathbb{Z} \:\:,\:\: ",r"b \neq 0 ",r"\biggr\}").shift(DOWN*0.8)

        t4 = MathTex(r"\mathbb{Q}",r"= \biggl\{ {a \over b} \:\: \biggr\rvert \:\: a,b \in \mathbb{Z} \:\:,\:\: b \neq 0 \biggr\}").shift(DOWN*0.8)
        t4[0].set_color(GREEN)
        
        self.play(Write(t3_1))
        self.wait(3)
        self.play(TransformMatchingShapes(t3_1, t3_2))
        self.wait(3)
        self.play(TransformMatchingShapes(t3_2, t3_3))
        self.wait(3)
        self.play(TransformMatchingShapes(t3_3, t3_4))
        self.wait(3)
        self.play(TransformMatchingTex(t3_4, t4))
        self.wait(3)

        tQe_1 = MathTex("Quociente", color=GRAY).next_to(t4, DOWN, buff=0.1).shift(LEFT*2.9)
        tQe_2 = Tex("`", color=GRAY).next_to(tQe_1, LEFT, buff=0.1).shift(UP*0.1)
        tQe_3 = Tex("'", color=GRAY).next_to(tQe_1, RIGHT, buff=0.1).shift(UP*0.1)
        tQe = VGroup(tQe_1, tQe_2, tQe_3)

        self.play(FadeIn(tQe))
        self.wait(3)

        all_1 = VGroup(tQ, tQsr, t4, tQe)
        self.play(FadeOut(all_1), t4[0].animate.move_to(Qc).scale(1.5))
        self.add(Qc)
        self.wait(3)

        # números fracionários e decimais

        t5 = MathTex(r"3 \over 4").shift(LEFT*1.5)
        t5_2 = MathTex(r"{3 \over 4}","=","0,75").shift(LEFT*1.5)
        t5sr = SurroundingRectangle(t5_2[0], buff=0.1, fill_opacity=0.2, color=YELLOW)
        t5sr_2 = SurroundingRectangle(t5_2[2], buff=0.1, fill_opacity=0.2, color=YELLOW)

        t6 = MathTex(r"2 \over 9").shift(RIGHT*1.5)
        t6_2 = MathTex(r"{2 \over 9}","=","0,222...").shift(RIGHT*1.5)
        t6sr = SurroundingRectangle(t6_2[0], buff=0.1, fill_opacity=0.2, color=YELLOW)
        t6sr_2 = SurroundingRectangle(t6_2[2], buff=0.1, fill_opacity=0.2, color=YELLOW)
        
        self.play(LaggedStart(FadeIn(t5), FadeIn(t6), lag_ratio=0.5))
        self.wait(3)
        self.play(LaggedStart(TransformMatchingShapes(t5, t5_2), TransformMatchingShapes(t6, t6_2), lag_ratio=0.5))
        self.wait(3)
        self.play(FadeIn(t5sr, t6sr))
        self.wait(3)
        self.play(FadeOut(t5sr, t6sr), FadeIn(t5sr_2, t6sr_2))
        self.wait(3)
        self.play(FadeOut(t5sr_2, t6sr_2))
        self.wait(3)

        all_2 = VGroup(t5_2, t6_2)
        self.play(FadeOut(all_2))
        self.wait()

        t7 = MathTex(r"2 = {2 \over 1}").shift(LEFT*1.5)
        t8 = MathTex(r"5 = {5 \over 1}").shift(RIGHT*1.5)
        t9 = MathTex(r"5 = {5 \over 1} = {10 \over 2}").shift(RIGHT*1.5)

        self.play(FadeIn(t7))
        self.wait(3)
        self.play(FadeIn(t8))
        self.wait(3)
        self.play(t7.animate.shift(LEFT*0.5), TransformMatchingTex(t8, t9))
        self.wait(3)

        all_3 = VGroup(t7, t9, Qc)
        self.play(FadeOut(all_3))

# REAIS (OK)
class vid4(Scene):
    def construct(self):
        
        # Quadrado de lado 1

        sq = Polygon((-1,1,0), (-1,-1,0), (1, -1, 0), (1,1,0), color=WHITE).shift(DOWN*0.5)
        l1 = MathTex("1").next_to(sq, DOWN)
        l2 = MathTex("1").next_to(sq, RIGHT)
        d = Line((-1,-1,0), (1,1,0), color=RED, stroke_width=5).shift(DOWN*0.5)
        dl = MathTex(r"\sqrt{2}", color=RED).shift(UP*0.3+LEFT*0.3).rotate(45*DEGREES).shift(DOWN*0.5)

        self.play(LaggedStart(Create(sq), Write(l1), Write(l2), Create(d), Write(dl), lag_ratio=0.4))
        self.wait(3)

        dl2 = MathTex(r"\sqrt{2}").shift(UP*2).scale(1.2)
        dl3 = MathTex(r"\sqrt{2} = 1,41421356237309...").shift(UP*2)

        self.play(ReplacementTransform(dl, dl2))
        self.wait(3)
        self.play(TransformMatchingShapes(dl2, dl3))
        self.wait(3)
        self.play(FadeOut(sq, l1, l2, d))
        self.wait(3)

        # Aproximação para raiz de 2

        t1 = MathTex(r"\sqrt{2} \approx 1,414")
        l = Line((-1.7,-0.2,0), (1.7,0.2,0), color=RED)

        self.play(FadeIn(t1))
        self.wait(3)
        self.play(Create(l))
        self.wait(3)
        self.play(FadeOut(l, t1))
        self.wait(3)
        self.play(ReplacementTransform(dl3, dl2))
        self.wait(3)
        self.play(FadeIn(sq, l1, l2, d, dl))
        self.wait(3)

        # Número irracionais

        self.play(FadeOut(sq, l1, l2, d, dl))
        self.play(dl2.animate.shift(DOWN*2))
        self.wait(3)
        
        t2_1 = Tex("Irracional", color=MAROON).scale(1.5).to_edge(UP, buff=2)
        t2_2 = MathTex(r"\left( \mathbb{I} \right)", color=MAROON).scale(1.5).next_to(t2_1, RIGHT, buff=0.2).shift(DOWN*0.1)
        t2 = VGroup(t2_1, t2_2).move_to((0,2,0))
        
        self.play(FadeIn(t2))
        self.wait(3)

        # Exemplos de irracionais

        t3 = MathTex(r"\sqrt{3}").scale(1.2).shift(LEFT*2)
        t4 = MathTex(r"\pi").scale(1.6).shift(RIGHT*0.1)
        t5 = MathTex(r"e").scale(1.5).shift(RIGHT*2)

        self.play(FadeOut(dl2))
        self.play(FadeIn(t3))
        self.wait(3)
        self.play(FadeIn(t4))
        self.wait(3)
        self.play(FadeIn(t5))
        self.wait(3)

        self.play(FadeOut(t2, t3, t4, t5,))
        self.wait(3)

        # "Definição" dos Reais
        
        t5 = MathTex(r"\mathbb{Q}",r"\: \cup \:",r"\mathbb{I}").scale(1.2)
        t5[0].set_color(GREEN)
        t5[2].set_color(MAROON)

        t6 = MathTex(r"\mathbb{R}","=",r"\mathbb{Q}",r"\: \cup \:",r"\mathbb{I}").scale(1.2)
        t6[0].set_color(ORANGE)
        t6[2].set_color(GREEN)
        t6[4].set_color(MAROON)

        tRe_1 = MathTex("Real", color=GRAY).next_to(t6, DOWN, buff=0.2).shift(LEFT*1.3)
        tRe_2 = Tex("`", color=GRAY).next_to(tRe_1, LEFT, buff=0.1).shift(UP*0.1)
        tRe_3 = Tex("'", color=GRAY).next_to(tRe_1, RIGHT, buff=0.1).shift(UP*0.1)
        tRe = VGroup(tRe_1, tRe_2, tRe_3)

        Rc = MathTex(r"\mathbb{R}", color=ORANGE).scale(1.5).to_corner(UL)
        tR = Tex("Números Reais").scale(1.2).shift(UP*2)
        tRsr = SurroundingRectangle(tR, buff=0.2, color=ORANGE, fill_opacity=0.2)

        self.play(Write(t5))
        self.wait(3)
        self.play(LaggedStart(TransformMatchingShapes(t5, t6), FadeIn(tR), Create(tRsr), lag_ratio=0.5))
        self.play(FadeIn(tRe))
        self.play(FadeOut(tRe))
        self.wait(3)

        g = VGroup(t6, tR, tRsr)

        self.play(FadeOut(g), t6[0].animate.move_to(Rc).scale(1.25))
        self.add(Rc)
        self.wait(3)

# REAIS RETA NUMÉRICA (OK)
class vid5(Scene):
    def construct(self):

        Rc = MathTex(r"\mathbb{R}", color=ORANGE).scale(1.5).to_corner(UL)
        self.add(Rc)
        self.wait()

        # Reta numérica
        number_line = NumberLine(x_range=[-3.999,4,1], include_numbers=True, include_tip=True)
        number_line_label = MathTex(r"\mathbb{R}").next_to(number_line, DR, buff=0.1).shift(UP*0.3)
        
        value = ValueTracker(0)

        # Ponto sobre a reta
        dot = Dot().add_updater(lambda m: m.move_to(number_line.number_to_point(value.get_value())))

        # Valor do ponto
        dot_label = MathTex("0").next_to(dot, UP, buff=0.3)
        dot_label.add_updater(lambda m: m.become(MathTex(f"{value.get_value():.1f}").next_to(dot, UP, buff=0.3)))
        dot_label.next_to(dot, UP, buff=0.3)

        # Módulo do ponto (reta da origem até o ponto)
        origin = number_line.number_to_point(0)
        dot_module = Line(start=origin, end=(dot), color=YELLOW)
        dot_module.add_updater(lambda m: m.become(Line(start=origin, end=(dot), color=YELLOW)))

        dot_label_positive_2 = MathTex("2").move_to((2,0.5,0))
        dot_label_negative_2 = MathTex("-2").move_to((-2,0.5,0))

        self.add(number_line, number_line_label, dot, dot_label, dot_module)
        self.wait(3)
        self.play(value.animate.set_value(2.5), rate_func=smooth)
        self.play(value.animate.set_value(-1.5), rate_func=smooth)
        self.play(value.animate.set_value(2), rate_func=smooth)
        self.remove(dot_label)
        self.add(dot_label_positive_2)
        self.wait(3)

        # Medida da distância entre o ponto e a origem
        m_1 = Line((0,-1,0), (2,-1,0))
        m_2 = Line((0,0.1,0), (0,-0.1,0)).next_to(m_1, LEFT, buff=0)
        m_3 = Line((0,0.1,0), (0,-0.1,0)).next_to(m_1, RIGHT, buff=0)
        m_number = MathTex("2").next_to(m_1, DOWN, buff=0.2)
        m = VGroup(m_1, m_2, m_3, m_number).set_color(YELLOW)

        self.play(GrowFromCenter(m_2), run_time=0.4)
        self.play(Create(m_1), run_time=0.8)
        self.play(GrowFromCenter(m_3), run_time=0.3)
        self.play(FadeIn(m_number))
        self.wait(3)

        # Número positivo ou negativo
        self.remove(dot_label_positive_2)
        self.add(dot_label)
        self.play(value.animate.set_value(-2), m.animate.shift(LEFT*2), rate_func=smooth)
        self.remove(dot_label)
        self.add(dot_label_negative_2)
        self.wait(3)
        self.remove(m, dot, dot_module, dot_label)
        self.wait(3)

# REAIS NÚMEROS SIMÉTRICOS (OK)
class vid6(Scene):
    def construct(self):

        ###### Recuperar algumas variáveis

            # Reta numérica
        number_line = NumberLine(x_range=[-3.999,4,1], include_numbers=True, include_tip=True)
        number_line_label = MathTex(r"\mathbb{R}").next_to(number_line, DR, buff=0.1).shift(UP*0.3)
        
        value = ValueTracker(0)

            # Ponto sobre a reta
        dot = Dot().add_updater(lambda m: m.move_to(number_line.number_to_point(value.get_value())))

            # Módulo do ponto (reta da origem até o ponto)
        origin = number_line.number_to_point(0)
        dot_module = Line(start=origin, end=(dot), color=YELLOW)
        dot_module.add_updater(lambda m: m.become(Line(start=origin, end=(dot), color=YELLOW)))

        Rc = MathTex(r"\mathbb{R}", color=ORANGE).scale(1.5).to_corner(UL)

        self.add(number_line, number_line_label, Rc)
        self.wait(3)

        #####

        # Definir o ponto simétrico
        value_symmetrical = ValueTracker(0)

        # Ponto '-x'
        dot_symmetrical = Dot().add_updater(lambda m: m.move_to(number_line.number_to_point(value_symmetrical.get_value())))

        dot_symmetrical_label = MathTex("-x").next_to(dot_symmetrical, UP, buff=0.3)
        dot_symmetrical_label.add_updater(lambda m: m.become(MathTex("-x").next_to(dot_symmetrical, UP, buff=0.3)))
        dot_symmetrical_module = Line(start=ORIGIN, end=(dot_symmetrical), color=YELLOW)
        dot_symmetrical_module.add_updater(lambda m: m.become(Line(start=ORIGIN, end=(dot_symmetrical), color=YELLOW)))

        # Label do ponto 'x'
        dot_symmetrical_label_positive_x = MathTex("x").next_to(dot, UP, buff=0.3)
        dot_symmetrical_label_positive_x.add_updater(lambda m: m.become(MathTex("x").next_to(dot, UP, buff=0.3)))
          
        self.play(GrowFromCenter(dot), GrowFromCenter(dot_symmetrical))
        self.wait(3)
        self.play(FadeIn(dot_symmetrical_label_positive_x))
        self.wait(3)
        self.add(dot_module, dot_symmetrical_module)
        self.play(GrowFromCenter(dot_symmetrical_label),
                  value.animate.set_value(2.5),
                  value_symmetrical.animate.set_value(-2.5), rate_func=smooth)
        self.wait(3)

        # Exemplo '2' e '-2'
        dot_label_positive_2 = MathTex("2").move_to((2,0.5,0))
        dot_label_negative_2 = MathTex("-2").move_to((-2,0.5,0))
        
        self.play(value.animate.set_value(2),
                  value_symmetrical.animate.set_value(-2), rate_func=smooth)
        self.play(LaggedStart(FadeOut(dot_symmetrical_label, dot_symmetrical_label_positive_x),
                  FadeIn(dot_label_positive_2, dot_label_negative_2), lag_ratio=0.3), run_time=0.5)
        self.wait(3)

        # Exemplo 'pi' e '-pi'
        dot_label_positive_pi = MathTex(r"\pi").move_to((3.14,0.5,0))
        dot_label_negative_pi = MathTex(r"-\pi").move_to((-3.14,0.5,0))
        
        self.play(FadeOut(dot_label_positive_2, dot_label_negative_2))
        self.play(value.animate.set_value(3.14),
                  value_symmetrical.animate.set_value(-3.14), rate_func=smooth)
        self.play(FadeIn(dot_label_positive_pi, dot_label_negative_pi), run_time=0.5)
        self.wait(3)

        # Multiplicar por -1
        
        # Desaparece o 'pi' e o ponto volta a ser 'x'
        self.play(LaggedStart(FadeOut(dot_symmetrical, dot_label_negative_pi, dot_label_positive_pi, dot_symmetrical_module),
                              value.animate.set_value(1.5),
                              lag_ratio=0.7))
        self.play(FadeIn(dot_symmetrical_label_positive_x))
        self.wait(3)

# REAIS ROTAÇÃO DE 180° x(-1) (OK)
class vid7(Scene):
    def construct(self):

        ###### Recuperar algumas variáveis

            # Reta numérica
        number_line = NumberLine(x_range=[-3.999,4,1], include_numbers=True, include_tip=True)
        number_line_label = MathTex(r"\mathbb{R}").next_to(number_line, DR, buff=0.1).shift(UP*0.3)

        Rc = MathTex(r"\mathbb{R}", color=ORANGE).scale(1.5).to_corner(UL)
        
        self.add(number_line, number_line_label, Rc)
        self.wait(3)

        #####

        # Rotação de 180°
        product_neg_1 = MathTex(r"x \cdot (-1)").shift(DOWN*2)

        # Ponto 'x'
        dot_x_rotate = Dot((1.5,0,0))
        
        dot_x_rotate_module = Line(start=ORIGIN, end=(dot_x_rotate), color=YELLOW)
        dot_x_rotate_module.add_updater(lambda m: m.become(Line(start=ORIGIN, end=(dot_x_rotate), color=YELLOW)))
        
        dot_x_rotate_label = MathTex("x").next_to(dot_x_rotate, UP, buff=0.3)
        dot_x_rotate_label.add_updater(lambda m: m.become(MathTex("x").next_to(dot_x_rotate, UP, buff=0.3)))

        dot_x_rotate_label_negative = MathTex("-x").next_to((-1.5,0,0), UP, buff=0.4)

        # Ângulo de rotação
        angle = Angle(number_line, dot_x_rotate_module)
        angle.add_updater(lambda m: m.become(Angle(number_line, dot_x_rotate_module)))
        angle_180_label = MathTex(r"180^{\circ}").shift(UP*0.7).scale(0.7)

        self.add(dot_x_rotate, dot_x_rotate_module, dot_x_rotate_label, angle)
        self.wait(3)

        self.play(FadeIn(product_neg_1))
        self.play(Rotate(dot_x_rotate, angle=PI, about_point=ORIGIN), rate_func=smooth, run_time=1.5)
        self.play(TransformMatchingShapes(dot_x_rotate_label, dot_x_rotate_label_negative), FadeIn(angle_180_label), run_time=0.5)
        self.wait(3)

        self.remove(dot_x_rotate, dot_x_rotate_label_negative, dot_x_rotate_module, angle_180_label, product_neg_1)
        self.wait(3)

# REAIS EXEMPLO ROTAÇÃO DE 180° 2(-1) (OK)
class vid8(Scene):
    def construct(self):

        ###### Recuperar algumas variáveis

            # Reta numérica
        number_line = NumberLine(x_range=[-3.999,4,1], include_numbers=True, include_tip=True)
        number_line_label = MathTex(r"\mathbb{R}").next_to(number_line, DR, buff=0.1).shift(UP*0.3)

        Rc = MathTex(r"\mathbb{R}", color=ORANGE).scale(1.5).to_corner(UL)
        
        self.add(number_line, number_line_label, Rc)
        self.wait(3)

        #####

        # Rotação de 180°
        product_neg_1 = MathTex(r"2 \cdot (-1)").shift(DOWN*2)

        # Ponto 'x'
        dot_x_rotate = Dot((2,0,0))
        
        dot_x_rotate_module = Line(start=ORIGIN, end=(dot_x_rotate), color=YELLOW)
        dot_x_rotate_module.add_updater(lambda m: m.become(Line(start=ORIGIN, end=(dot_x_rotate), color=YELLOW)))
        
        dot_x_rotate_label = MathTex("2").next_to(dot_x_rotate, UP, buff=0.3)
        dot_x_rotate_label.add_updater(lambda m: m.become(MathTex("2").next_to(dot_x_rotate, UP, buff=0.3)))

        dot_x_rotate_label_negative = MathTex("-2").next_to((-2,0,0), UP, buff=0.4)

        # Ângulo de rotação
        angle = Angle(number_line, dot_x_rotate_module)
        angle.add_updater(lambda m: m.become(Angle(number_line, dot_x_rotate_module)))

        self.add(dot_x_rotate, dot_x_rotate_module, dot_x_rotate_label, angle)
        self.wait(3)

        self.play(FadeIn(product_neg_1))
        self.play(Rotate(dot_x_rotate, angle=PI, about_point=ORIGIN), rate_func=smooth, run_time=1.5)
        self.play(TransformMatchingShapes(dot_x_rotate_label, dot_x_rotate_label_negative), run_time=0.8)
        self.wait(3)

        self.remove(dot_x_rotate, dot_x_rotate_label_negative, dot_x_rotate_module, product_neg_1, angle)
        self.wait(3)

# REAIS ELEVADO AO QUADRADO (PROBLEMA) (OK)
class vid9(Scene):
    def construct(self):
        
        Rc = MathTex(r"\mathbb{R}", color=ORANGE).scale(1.5).to_corner(UL)
        self.add(Rc)
        self.wait(3)
        
        t1 = MathTex(r"\mathbb{R}", color=ORANGE).scale(2)
        self.play(TransformMatchingShapes(Rc, t1))
        self.wait(3)
        self.play(TransformMatchingShapes(t1, Rc))
        self.wait(3)

        # Todo real elevado ao quadrado é positivo
        t2 = MathTex("2^2 = 4").shift(UP*2)
        t3 = MathTex(r"(-3)^2 = 9")
        t4 = MathTex("(-1)^2 = 1").shift(DOWN*2)
        
        self.play(LaggedStart(FadeIn(t2), FadeIn(t3), FadeIn(t4), lag_ratio=0.5))
        self.wait(3)
        self.play(FadeOut(t2, t3, t4))
        self.wait()

        # Só pode tirar raiz de número positivo
        t5 = MathTex(r"\sqrt{y} \:\:\:\: , \:\:\: y \geq 0", color=YELLOW).shift(UP*2)
        t6 = MathTex(r"\sqrt{y} \:\:\:\: , \:\:\: y < 0", color=YELLOW).shift(UP*2)
        t7 = MathTex(r"\sqrt{y} \: \notin \: \mathbb{R} \:\:\:\: , \:\:\: y < 0", color=YELLOW).shift(UP*2)

        self.play(FadeIn(t5))
        self.wait(3)

        t8 = MathTex(r"\sqrt{4} = 2")
        t9 = MathTex(r"\sqrt{9} = 3").shift(DOWN*2)
        
        self.play(LaggedStart(FadeIn(t8), FadeIn(t9), lag_ratio=0.5))
        self.wait(3)

        # Tirar raiz de número negativo é impossível
        self.play(LaggedStart(FadeOut(t8, t9), TransformMatchingShapes(t5, t6), lag_ratio=0.5))
        self.wait()

        t10 = MathTex(r"\sqrt{-4} = \: ?")
        t11 = MathTex(r"\sqrt{-9} = \: ?").shift(DOWN*2)
        
        self.play(LaggedStart(FadeIn(t10), FadeIn(t11), TransformMatchingShapes(t6, t7), lag_ratio=0.5))
        self.wait(3)

        all_1 = VGroup(t10, t11, t7)
        self.play(FadeOut(all_1))
        self.wait()

        # Exemplo de equação quadrática sem solução real 
        eq_example1 = MathTex(r"{1 \over 3}x^2 + 3 = 0")
        self.play(Write(eq_example1))
        self.wait(3)

        eq_example2 = MathTex(r"{1 \over 3}x^2 = -3")
        self.play(TransformMatchingShapes(eq_example1, eq_example2))
        self.wait(3)

        eq_example3 = MathTex(r"x^2 = -3 \cdot 3")
        self.play(TransformMatchingShapes(eq_example2, eq_example3))
        self.wait(3)

        eq_example4 = MathTex(r"x^2 = -9")
        self.play(TransformMatchingShapes(eq_example3, eq_example4))
        self.wait(3)

        eq_example5 = MathTex(r"x = \pm \sqrt{-9}")
        self.play(TransformMatchingShapes(eq_example4, eq_example5))
        self.wait(3)

        self.play(FadeOut(Rc, eq_example5))
        self.wait(3)

# COMPLEXOS (OK)
class vid10(Scene):
    def construct(self):
        
        # Título
        Cc = MathTex(r"\mathbb{C}", color=RED).scale(1.5).to_corner(UL)
        tC = Tex("Números Complexos").scale(1.2).shift(UP*2)
        tCsr = SurroundingRectangle(tC, buff=0.2, color=RED, fill_opacity=0.2)
        
        self.play(FadeIn(tC), Create(tCsr), lag_ratio=0.5)
        self.wait(3)

        # Unidade imaginária
        t1 = MathTex("i").scale(1.5).shift(DOWN*0.5)
        self.play(Write(t1))
        self.wait(3)

        t2 = MathTex(r"i = \sqrt{-1}").shift(DOWN*0.5)
        self.play(TransformMatchingShapes(t1, t2))
        self.wait(3)

        t3 = MathTex(r"i = \sqrt{-1} \:\:\: \Rightarrow \:\:\: i \cdot i").shift(DOWN*0.5)
        self.play(TransformMatchingShapes(t2, t3))
        self.wait(3)

        t4 = MathTex(r"i = \sqrt{-1} \:\:\: \Rightarrow \:\:\: i^2").shift(DOWN*0.5)
        self.play(TransformMatchingTex(t3, t4))
        self.wait(3)

        t5 = MathTex(r"i = \sqrt{-1} \:\:\: \Rightarrow \:\:\: i^2 = -1").shift(DOWN*0.5)
        self.play(TransformMatchingShapes(t4, t5))
        self.wait(3)

        self.play(FadeOut(t5))
        self.wait()

        # Solução da equação-exemplo
        t6 = MathTex(r"x = \pm \sqrt{-9}").shift(DOWN*0.5)
        self.play(FadeIn(t6))
        self.wait(3)

        t7 = MathTex(r"x = \pm \sqrt{9 \cdot (-1)}").shift(DOWN*0.5)
        self.play(TransformMatchingShapes(t6, t7))
        self.wait(3)

        t8 = MathTex(r"x = \pm \sqrt{9} \cdot \sqrt{-1}").shift(DOWN*0.5)
        self.play(TransformMatchingShapes(t7, t8))
        self.wait(3)

        t9 = MathTex(r"x = \pm 3 \cdot i").shift(DOWN*0.5)
        self.play(TransformMatchingShapes(t8, t9))
        self.wait(3)
        
        t10 = MathTex(r"x = \pm 3i").shift(DOWN*0.5)
        self.play(TransformMatchingShapes(t9, t10))
        self.wait(3)

        self.play(FadeOut(t10))
        self.wait(3)

        # Definição de número complexo
        t11 = MathTex(r"z", color=YELLOW).shift(DOWN*0.5)
        self.play(Write(t11))
        self.wait(3)

        t12 = MathTex(r"z \: \vert \: ","z = a + bi").shift(DOWN*0.5)
        t12[1].set_color(YELLOW)
        self.play(TransformMatchingShapes(t11, t12))
        self.wait(3)

        t13 = MathTex(r"z \: \vert \: z = a + bi \:\: , \:\: ",r"a,b \in \mathbb{R}").shift(DOWN*0.5)
        t13[1].set_color(YELLOW)
        self.play(TransformMatchingShapes(t12, t13))
        self.wait(3)

        t14 = MathTex(r"z \: \vert \: z = a + bi \:\: , \:\: a,b \in \mathbb{R} \:\: , \:\: ",r"i = \sqrt{-1}").shift(DOWN*0.5)
        t14[1].set_color(YELLOW)
        self.play(TransformMatchingShapes(t13, t14))
        self.wait(3)

        t15 = MathTex(r"\left\{ z \: \vert \: z = a + bi \:\: , \:\: a,b \in \mathbb{R} \:\: , \:\: i = \sqrt{-1} \right\}").shift(DOWN*0.5)
        self.play(TransformMatchingTex(t14, t15))
        self.wait(3)

        t16 = MathTex(r"\mathbb{C}",r"= \left\{ z \: \vert \: z = a + bi \:\: , \:\: a,b \in \mathbb{R} \:\: , \:\: i = \sqrt{-1} \right\}").shift(DOWN*0.5)
        t16[0].set_color(RED)
        self.play(TransformMatchingShapes(t15, t16))
        self.wait(3)
   
        tCe_1 = MathTex("Complexo", color=GRAY).next_to(t16, DOWN, buff=0.2).shift(LEFT*4.5)
        tCe_2 = Tex("`", color=GRAY).next_to(tCe_1, LEFT, buff=0.1).shift(UP*0.1)
        tCe_3 = Tex("'", color=GRAY).next_to(tCe_1, RIGHT, buff=0.1).shift(UP*0.1)
        tCe = VGroup(tCe_1, tCe_2, tCe_3)
        self.play(FadeIn(tCe))
        self.play(FadeOut(tCe))
        self.wait(3)
        
        # Símbolo 'C' no canto
        Qc = MathTex(r"\mathbb{C}", color=RED).scale(1.5).to_corner(UL)
        all_1 = VGroup(tC, tCsr, t16)
        self.play(FadeOut(all_1), t16[0].animate.move_to(Qc).scale(1.5))
        self.add(Qc)
        self.wait(3)

# COMPLEXOS PLANO COMPLEXO (OK)
class vid11(Scene):
    def construct(self):

        # Símbolo 'C' no canto
        Qc = MathTex(r"\mathbb{C}", color=RED).scale(1.5).to_corner(UL)
        self.add(Qc)
        self.wait()
        
        # Reta real
        re_axis = NumberLine(x_range=[-3.999,4,1], include_tip=True).shift(DOWN)
        re_axis_label = MathTex(r"Re").next_to(re_axis, DR, buff=0.1)

        n3n = MathTex("-3").scale(0.75).move_to((-3.15,-1.4,0))
        n2n = MathTex("-2").scale(0.75).move_to((-2.15,-1.4,0))
        n1n = MathTex("-1").scale(0.75).move_to((-1.15,-1.4,0))
        n0 = MathTex("0").scale(0.75).move_to((0,-1.4,0))
        n1 = MathTex("1").scale(0.75).move_to((1,-1.4,0))
        n2 = MathTex("2").scale(0.75).move_to((2,-1.4,0))
        n3 = MathTex("3").scale(0.75).move_to((3,-1.4,0))
        re_axis_numbers = VGroup(n3n, n2n, n1n, n0, n1, n2, n3)
        
        self.play(Create(re_axis), Create(re_axis_numbers), FadeIn(re_axis_label))
        self.wait(3)

        # Eixo imaginário
        im_axis = NumberLine(x_range=[-2.999,2.999], include_numbers=False, include_tip=True, rotation=90*DEGREES)
        im_axis_label = MathTex(r"Im").next_to(im_axis, UL, buff=0.1)

        i0 = MathTex(r"0").scale(0.75).move_to((-0.2,-1.4,0))
        i1 = MathTex(r"-i").scale(0.75).move_to((-0.4,-1.97,0))
        i2 = MathTex(r"i").scale(0.75).move_to((-0.25,0.05,0))
        i3 = MathTex(r"2i").scale(0.75).move_to((-0.3,1.05,0))
        i4 = MathTex(r"3i").scale(0.75).move_to((-0.3,2.05,0))
        i_numbers = VGroup(i1, i0, i2, i3, i4)

        # Plano
        number_plane = NumberPlane(
            x_range=(-3.5, 3.5, 1),
            y_range=(-1.5, 3.5, 1),
            x_length=7,
            y_length=5,
        ).move_to(DOWN*0).set_z_index(-1).set_opacity(0.5)
        
        self.play(Create(im_axis), FadeOut(n0), run_time = 2)
        self.wait(3)
        self.play(Create(number_plane), run_time = 2)
        self.wait(3)
        self.play(Create(i_numbers))
        self.wait(3)
        self.play(FadeIn(im_axis_label))
        self.wait(3)
        
        # Número complexo como par ordenado
        complex_number = MathTex("z = a + bi", color=RED).shift(UP*3.2+RIGHT*2)
        self.play(FadeIn(complex_number))
        self.wait(3)

            # Par ordenado
        x = ValueTracker(2.5)
        y = ValueTracker(0.5)

        pair_dot_1 = Dot((2.5, 0.5, 0), color=RED)
        pair_dot = Dot((x.get_value(), y.get_value(), 0), color=RED)
        pair_dot.add_updater(lambda m: m.become(Dot((x.get_value(), y.get_value(), 0), color=RED)))

        pair_label_1 = MathTex("(a,b)").scale(0.8).next_to(pair_dot, UP)
        pair_label = MathTex("(a,b)").scale(0.8).next_to(pair_dot, UP)
        pair_label.add_updater(lambda m: m.become(MathTex("(a,b)").scale(0.8).next_to(pair_dot, UP)))

            # Projeções do par ordenado
        a_proj = DashedLine(pair_dot, (x.get_value(), -1, 0), color=RED)
        a_proj.add_updater(lambda m: m.become(DashedLine(pair_dot, (x.get_value(), -1, 0), color=RED)))
        a_module = Line((0,-1,0), a_proj, color=YELLOW)
        a_module.add_updater(lambda m: m.become(Line((0,-1,0), a_proj, color=YELLOW)))
        a_value = MathTex("a", color=RED).next_to(a_proj, DOWN, buff=0.2)

        b_proj = DashedLine(pair_dot, (0, y.get_value(), 0), color=RED)
        b_proj.add_updater(lambda m: m.become(DashedLine(pair_dot, (0, y.get_value(), 0), color=RED)))
        b_module = Line((0,-1,0), b_proj, color=ORANGE)
        b_module.add_updater(lambda m: m.become(Line((0,-1,0), b_proj, color=ORANGE)))
        b_value = MathTex("b", color=RED).next_to(b_proj, LEFT, buff=0.15)
        
        self.play(GrowFromCenter(pair_dot_1), GrowFromCenter(pair_label_1))
        self.add(pair_dot, pair_label)
        self.remove(pair_dot_1, pair_label_1)
        self.wait(3)
        self.play(Create(a_proj))
        self.play(GrowFromCenter(a_value), Create(a_module))
        self.wait(3)
        self.play(Create(b_proj))
        self.play(GrowFromCenter(b_value), Create(b_module))
        self.wait(3)
        
        # Ponto percorrendo o plano
        self.play(FadeOut(a_value, b_value), x.animate.set_value(0.5), y.animate.set_value(1.5), rate_func=linear, run_time=0.7)
        self.play(x.animate.set_value(-1.5), y.animate.set_value(1), rate_func=linear, run_time=0.7)
        self.play(x.animate.set_value(-2), y.animate.set_value(-2), rate_func=linear, run_time=1)
        self.play(x.animate.set_value(1.5), y.animate.set_value(-2.5), rate_func=linear, run_time=0.8)
        self.play(x.animate.set_value(1), y.animate.set_value(0), rate_func=linear, run_time=0.7)
        self.wait(3)
        
        # Ponto-exemplo (3 + 2i)
        complex_number_example = MathTex("z = 3 + 2i", color=RED).shift(UP*3.2+RIGHT*2)
        pair_label_example = MathTex("(3,2)").scale(0.8).next_to((3, 1, 0), UP)
        self.play(TransformMatchingShapes(complex_number, complex_number_example))
        self.play(x.animate.set_value(3), y.animate.set_value(1), rate_func=smooth)
        self.play(TransformMatchingShapes(pair_label, pair_label_example), run_time = 0.7)
        self.wait(3)  
        self.play(FadeOut(complex_number_example,
                          pair_dot,
                          pair_label_example,
                          a_proj,
                          a_module,
                          b_proj,
                          b_module))
        self.wait(3)

        # Rotação de 90° (x i)
        pair_dot_2 = Dot((2, -1, 0), color=RED)

        n2_module = Line(start=(0,-1,0), end=pair_dot_2, color=YELLOW)
        n2_module.add_updater(lambda m: m.become(Line((0,-1,0), pair_dot_2, color=YELLOW)))

        l = Line((0,-1,0), (1,-0.99,0))
        angle = Angle(l, n2_module)
        angle.add_updater(lambda m: m.become(Angle(l, n2_module)))
        angle_90_label = MathTex("90^{\circ}").scale(0.7).move_to((0.6,-0.4,0))

        product_i = MathTex(r"\cdot i").shift(RIGHT*2.5+UP*0.5).scale(1.5)

        self.play(GrowFromCenter(pair_dot_2), Create(n2_module))
        self.play(FadeIn(product_i))
        self.wait(3)
        self.play(FadeIn(angle), Rotate(pair_dot_2, angle=PI/2, about_point=(0,-1,0)), rate_func=smooth, run_time=1.5)
        self.play(FadeIn(angle_90_label))
        self.wait(3)
        self.remove(pair_dot_2, n2_module, product_i, angle, angle_90_label)
        self.wait(3)

        # Rotação de 180° (x i^2)
            # Primeira rotação de 90°
        pair_dot_2 = Dot((2, -1, 0), color=RED)
        self.play(GrowFromCenter(pair_dot_2), Create(n2_module))
        self.play(FadeIn(product_i))
        self.play(FadeIn(angle), Rotate(pair_dot_2, angle=PI/2, about_point=(0,-1,0)), rate_func=smooth, run_time=1.5)
        self.play(FadeIn(angle_90_label))
        self.wait(3)

            # Segunda rotação de 90°
        product_i_2 = MathTex(r"\cdot i").shift(LEFT*2.5+UP*0.5).scale(1.5)
        angle_90_label_2 = MathTex("90^{\circ}").scale(0.7).move_to((-0.6,-0.4,0))

        self.play(FadeIn(product_i_2))
        self.play(Rotate(pair_dot_2, angle=PI/2, about_point=(0,-1,0)), rate_func=smooth, run_time=1.5)
        self.play(FadeIn(angle_90_label_2))
        self.wait(3)

        g_angle = VGroup(angle_90_label, angle_90_label_2)
        angle_180_label = MathTex("180^{\circ}").scale(0.7).move_to((0.8,-0.4,0))
        self.play(Transform(g_angle, angle_180_label))
        self.wait(3)
        
        g_product = VGroup(product_i, product_i_2)
        product_i_3 = MathTex(r"\cdot (-1)").shift(RIGHT*2.5+UP*0.5)       
        self.play(TransformMatchingShapes(g_product, product_i_3))
        self.wait(3)

# LISTA DOS CONJUNTOS
class vid12(Scene):
    def construct(self):

        N = MathTex(r"\mathbb{N}"," = \{ 0, \: 1, \: 2, \: 3, \: ... \}").shift(UP*2)
        N[0].set_color(LIGHT_PINK)

        Z = MathTex(r"\mathbb{Z}",r"= \{ ... \: , \: -2, \: -1, \:\: 0, \:\: 1, \:\: 2, \: ... \}").shift(UP*1)
        Z[0].set_color(BLUE)

        Q = MathTex(r"\mathbb{Q}",r"= \biggl\{ {a \over b} \:\: \biggr\rvert \:\: a,b \in \mathbb{Z} \:\:,\:\: b \neq 0 \biggr\}")
        Q[0].set_color(GREEN)

        R = MathTex(r"\mathbb{R}","=",r"\mathbb{Q}",r"\: \cup \:",r"\mathbb{I}").shift(DOWN*1)
        R[0].set_color(ORANGE)

        C = MathTex(r"\mathbb{C}",r"= \left\{ z \: \vert \: z = a + bi \:\: , \:\: a,b \in \mathbb{R} \:\: , \:\: i = \sqrt{-1} \right\}").shift(DOWN*2)
        C[0].set_color(RED)

        g = VGroup(N, Z, Q, R, C).arrange(direction=DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(FadeIn(N))
        self.wait(3)

        self.play(FadeIn(Z))
        self.wait(3)

        self.play(FadeIn(Q))
        self.wait(3)

        self.play(FadeIn(R))
        self.wait(3)

        self.play(FadeIn(C))
        self.wait(3)

        self.play(FadeOut(g))

# CONSTRUÇÃO DO DIAGRAMA DE VENN (OK)
class vid13(Scene):
    def construct(self):

        # Um conjunto está contido no próximo
        t = MathTex(r"\mathbb{N}",r"\:\: \subset \:\:",r"\mathbb{Z}",r"\:\: \subset \:\:",r"\mathbb{Q}",r"\:\: \subset \:\:",r"\mathbb{R}",r"\:\: \subset \:\:",r"\mathbb{C}")
        t[0].set_color(LIGHT_PINK)
        t[2].set_color(BLUE)
        t[4].set_color(GREEN)
        t[6].set_color(ORANGE)
        t[8].set_color(RED)
        self.play(Write(t), run_time = 3)
        self.wait(3)
        self.play(FadeOut(t))
        self.wait(3)

        # Naturais
        cN = Ellipse(width=2, height=2, color=LIGHT_PINK, fill_opacity=0.2).set_z_index(6)
        tN = MathTex(r"\mathbb{N}", color=LIGHT_PINK).next_to(cN, UP, buff=-0.1).shift(RIGHT*0.1).set_z_index(7).scale(1.2)
        tNb = MathTex(r"\mathbb{N}", color=BLACK, stroke_width=6).move_to(tN).set_z_index(6).scale(1.2)
        n1 = MathTex("1").move_to(cN).shift(UP*0.5)
        n2 = MathTex("0").move_to(cN).shift(LEFT*0.5+DOWN*0.2)
        n3 = MathTex("2").move_to(cN).shift(RIGHT*0.4+DOWN*0.3)
        nN = VGroup(n1, n2, n3).set_z_index(7)
        N = VGroup(cN, tN, tNb, nN)

        self.play(LaggedStart(FadeIn(n2), FadeIn(n1), FadeIn(n3), lag_ratio=0.7))
        self.wait(3)
        self.play(LaggedStart(DrawBorderThenFill(cN), FadeIn(tN, tNb), lag_ratio=0.7))
        self.wait(3)
        self.play(N.animate.shift(LEFT*0.8))
        self.wait(3)

        # Inteiros
        cZ = Ellipse(width=4.5, height=3, color=BLUE, fill_opacity=0.2).set_z_index(5)
        tZ = MathTex(r"\mathbb{Z}", color=BLUE).next_to(cZ, UP, buff=-0.08).set_z_index(6).scale(1.2)
        tZb = MathTex(r"\mathbb{Z}", color=BLACK, stroke_width=6).move_to(tZ).set_z_index(5).scale(1.2)
        n4 = MathTex("-1").move_to(cZ).shift(RIGHT*0.7+UP*0.7)
        n5 = MathTex("-2").move_to(cZ).shift(RIGHT*1.5)
        n6 = MathTex("-3").move_to(cZ).shift(RIGHT*0.9+DOWN*0.7)
        nZ = VGroup(n4, n5, n6).set_z_index(6)      
        NZ = VGroup(N, cZ, tZ, tZb, nZ)

        self.play(LaggedStart(FadeIn(n4), FadeIn(n5), FadeIn(n6), lag_ratio=0.7))
        self.wait(3)
        self.play(LaggedStart(DrawBorderThenFill(cZ), FadeIn(tZ, tZb), lag_ratio=0.7))
        self.wait(3)
        self.play(NZ.animate.shift(LEFT))
        self.wait(3)

        # Racionais
        cQ = Ellipse(width=7, height=4, color=GREEN, fill_opacity=0.2).set_z_index(4)
        tQ = MathTex(r"\mathbb{Q}", color=GREEN).next_to(cQ, UP, buff=-0.1).shift(LEFT*0.15).set_z_index(5).scale(1.2)
        tQb = MathTex(r"\mathbb{Q}", color=BLACK, stroke_width=6).move_to(tQ).set_z_index(4).scale(1.2)
        n7 = MathTex(r"1 \over 2").move_to(cQ).shift(RIGHT*1.9+UP*0.8)
        n8 = MathTex(r"7 \over 3").move_to(cQ).shift(RIGHT*2.7)
        n9 = MathTex(r"0,111...").move_to(cQ).shift(RIGHT*2+DOWN).scale(0.9)
        nQ = VGroup(n7, n8, n9).set_z_index(5)
        NZQ = VGroup(NZ, cQ, tQ, tQb, nQ)

        self.play(LaggedStart(FadeIn(n7), FadeIn(n8), FadeIn(n9), lag_ratio=0.7))
        self.wait(3)
        self.play(LaggedStart(DrawBorderThenFill(cQ), FadeIn(tQ, tQb), lag_ratio=0.7))
        self.wait(3)
        self.play(NZQ.animate.shift(LEFT*0.7))
        self.wait(3)

        # Reais
        cR = Ellipse(width=9, height=5, color=ORANGE, fill_opacity=0.2).set_z_index(3)
        tR = MathTex(r"\mathbb{R}", color=ORANGE).next_to(cR, UP, buff=-0.08).set_z_index(4).scale(1.2)
        tRb = MathTex(r"\mathbb{R}", color=BLACK, stroke_width=6).move_to(tR).set_z_index(3).scale(1.2)
        n10 = MathTex(r"\pi").move_to(cR).shift(RIGHT*3.25+UP).scale(1.3)
        n11 = MathTex(r"\sqrt{2}").move_to(cR).shift(RIGHT*3.8)
        n12 = MathTex(r"e").move_to(cR).shift(RIGHT*3.3+DOWN).scale(1.2)
        nR = VGroup(n10, n11, n12).set_z_index(4).shift(LEFT*0.2)
        NZQR = VGroup(NZQ, cR, tR, tRb, nR)
        self.play(LaggedStart(FadeIn(n10), FadeIn(n11), FadeIn(n12), lag_ratio=0.7))
        self.wait(3)
        self.play(LaggedStart(DrawBorderThenFill(cR), FadeIn(tR, tRb), lag_ratio=0.7))
        self.wait(3)
        self.play(NZQR.animate.shift(LEFT*0.9))
        self.wait(3)
        
        # Complexos
        cC = Ellipse(width=11.5, height=6, color=RED, fill_opacity=0.2).set_z_index(2)
        tC = MathTex(r"\mathbb{C}", color=RED).next_to(cC, UP, buff=-0.1).shift(LEFT*0.2).set_z_index(3).scale(1.2)
        tCb = MathTex(r"\mathbb{C}", color=BLACK, stroke_width=6).move_to(tC).set_z_index(2).scale(1.2)
        n13 = MathTex(r"\sqrt{-1}").move_to(cC).shift(RIGHT*4.3+UP)
        n14 = MathTex(r"3+2i").move_to(cC).shift(RIGHT*4.6+DOWN*0.2)
        n15 = MathTex(r"-3i").move_to(cC).shift(RIGHT*4.1+DOWN*1.2)
        nC = VGroup(n13, n14, n15).set_z_index(3)
        C = VGroup(cC, tC, tCb, nC)

        self.play(LaggedStart(FadeIn(n13), FadeIn(n14), FadeIn(n15), lag_ratio=0.7))
        self.wait(3)
        self.play(LaggedStart(DrawBorderThenFill(cC), FadeIn(tC, tCb), lag_ratio=0.7))
        self.wait(3)

# MODIFICADORES (OK)
class vid14(Scene):
    def construct(self):

        # Explicação
        t1 = Tex("Modificadores", color=YELLOW).scale(1.2).shift(UP*2)
        self.play(Write(t1))
        
        t_asterisk = MathTex(r"*").shift(UP*0.5)
        t_plus = MathTex(r"+").shift(DOWN*0.5)
        t_minus = MathTex(r"-").shift(DOWN*1.5)
        self.play(LaggedStart(FadeIn(t_asterisk), FadeIn(t_plus), FadeIn(t_minus), lag_ratio=0.5))
        self.wait(3)
        
        t_asterisk_1 = Tex(": Remove o número zero").next_to((-2.8, 0.5, 0), RIGHT, buff=0.3).shift(UP*0.05)
        self.play(t_asterisk.animate.shift(LEFT*2.8))
        self.play(FadeIn(t_asterisk_1))
        self.wait(3)

        t_plus_1 = Tex(": Remove os números negativos").next_to((-2.8, -0.5, 0), RIGHT, buff=0.3)
        self.play(t_plus.animate.shift(LEFT*2.8))
        self.play(FadeIn(t_plus_1))
        self.wait(3)

        t_minus_1 = Tex(": Remove os números positivos").next_to((-2.8, -1.5, 0), RIGHT, buff=0.3)
        self.play(t_minus.animate.shift(LEFT*2.8))
        self.play(FadeIn(t_minus_1))
        self.wait(3)

        self.play(FadeOut(t1, t_asterisk, t_plus, t_minus,
                          t_asterisk_1, t_plus_1, t_minus_1))
        self.wait(3)

        # Exemplo com o conjunto Z     
        Z = MathTex(r"\mathbb{Z}",r" = \left\{ ... \:, \: -3, \: -2, \: -1, \:\: 0, \:\: 1, \:\: 2, \:\: 3, \: ... \right\}").scale(1.1).shift(UP*2)
        Z[0].set_color(BLUE)
        self.play(FadeIn(Z))
        self.wait(3)

        Z_asterisk = MathTex(r"\mathbb{Z}^{*}",r" = \left\{ ... \:, \: -3, \: -2, \: -1, \:\: 1, \:\: 2, \:\: 3, \: ... \right\}")
        Z_asterisk[0].set_color(BLUE)

        Z_plus = MathTex(r"\mathbb{Z}_{+}",r" = \left\{ 0, \:\: 1, \:\: 2, \:\: 3, \: ... \right\}")
        Z_plus[0].set_color(BLUE)

        Z_minus = MathTex(r"\mathbb{Z}_{-}",r" = \left\{ ... \:, \: -3, \: -2, \: -1, \:\: 0 \right\}")
        Z_minus[0].set_color(BLUE)

        g1 = VGroup(Z_asterisk, Z_plus, Z_minus).arrange(direction=DOWN, buff=0.5, aligned_edge=LEFT).shift(DOWN)
        
        self.play(FadeIn(Z_asterisk))
        self.wait(3)
        self.play(FadeIn(Z_plus))
        self.wait(3)
        self.play(FadeIn(Z_minus))
        self.wait(3)

        self.play(FadeOut(g1))
        self.wait(3)

        Z_plus_asterisk = MathTex(r"\mathbb{Z}_{+}^{*}",r" = \left\{ \:\: 1, \:\: 2, \:\: 3, \: ... \right\}")
        Z_plus_asterisk[0].set_color(BLUE)

        Z_minus_asterisk = MathTex(r"\mathbb{Z}_{-}^{*}",r" = \left\{ ... \:, \: -3, \: -2, \: -1 \right\}")
        Z_minus_asterisk[0].set_color(BLUE)

        g2 = VGroup(Z_plus_asterisk, Z_minus_asterisk).arrange(direction=DOWN, buff=0.5, aligned_edge=LEFT).shift(DOWN)

        Z_plus_asterisk_label = MathTex(r"Inteiros \:\: positivos", color=GRAY).next_to(Z_plus_asterisk, UP).shift(RIGHT*0.5)
        Z_minus_asterisk_label = MathTex(r"Inteiros \:\: negativos", color=GRAY).next_to(Z_plus_asterisk, DOWN, buff=1.3).shift(RIGHT*0.5)

        g3 = VGroup(Z_plus_asterisk_label, Z_minus_asterisk_label)

        self.play(FadeIn(Z_plus_asterisk))
        self.wait(3)
        self.play(FadeIn(Z_plus_asterisk_label))
        self.wait(3)

        self.play(FadeIn(Z_minus_asterisk))
        self.wait(3)
        self.play(FadeIn(Z_minus_asterisk_label))
        self.wait(3)

        self.play(FadeOut(Z, g2, g3))

# APÊNDICE: RAIZ DE 2 NA RETA NUMÉRICA
class vid15(Scene):
    def construct(self):

        Rc = MathTex(r"\mathbb{R}", color=ORANGE).scale(1.5).to_corner(UL)

        # Reta numérica
        number_line = NumberLine(x_range=[-3.999,4,1], include_numbers=True, include_tip=True)
        number_line_label = MathTex(r"\mathbb{R}").next_to(number_line, DR, buff=0.1).shift(UP*0.3)
        
        value = ValueTracker(0)

        # Ponto sobre a reta
        dot = Dot().add_updater(lambda m: m.move_to(number_line.number_to_point(value.get_value())))

        # Valor do ponto
        dot_label = MathTex("0").next_to(dot, UP, buff=0.3)
        dot_label.add_updater(lambda m: m.become(MathTex(f"{value.get_value():.1f}").next_to(dot, UP, buff=0.3)))
        dot_label.next_to(dot, UP, buff=0.3)

        # Módulo do ponto (reta da origem até o ponto)
        origin = number_line.number_to_point(0)
        dot_module = Line(start=origin, end=(dot), color=YELLOW)
        dot_module.add_updater(lambda m: m.become(Line(start=origin, end=(dot), color=YELLOW)))

        self.add(Rc, number_line)

        # Quadrado de lado 1

        sq = Polygon((0,0.5,0), (1,0.5,0), (1, 1.5, 0), (0,1.5,0), color=WHITE).shift(DOWN*0.5)
        d = Line((0,0.5,0), (1, 1.5, 0), color=RED, stroke_width=5).shift(DOWN*0.5)
        dl = MathTex(r"\sqrt{2}", color=RED).rotate(45*DEGREES).next_to(sq, UL, buff=-0.65).scale(0.6)

        g = VGroup (sq, d, dl)

        dot = Dot((1.414, 0, 0))
        dot_label = MathTex(r"\sqrt{2}", color=RED).next_to(dot, UP, buff=0.2).scale(0.8).shift(LEFT*0.1)

        self.wait(3)
        self.play(LaggedStart(Create(sq), Create(d), FadeIn(dl), lag_ratio=0.7))
        self.play(Rotate(g, -45*DEGREES, about_point=ORIGIN))
        self.play(GrowFromCenter(dot), FadeOut(sq), ReplacementTransform(dl, dot_label))
        self.wait(3)
        self.play(FadeOut(d, dot_label, dot))
        self.wait()

# IMAGENS PARA O TEXTO

class N(ThreeDScene):
    def construct(self):

        self.camera.background_color = WHITE

        t = MathTex(r"\mathbb{N}",r"= \left\{0, 1, 2, 3, ...\right\}", color=BLACK).set_z_index(1)
        sr = SurroundingRectangle(t, color=GRAY_A, buff=0.3, corner_radius=0.1, fill_opacity=0.5)

        self.add(t, sr)

class Z(ThreeDScene):
    def construct(self):

        self.camera.background_color = WHITE

        t = MathTex(r"\mathbb{Z} =  \left\{ ... , -3, -2, -1, \:\: 0, \:\: 1, \:\: 2, \:\: 3, ... \right\}", color=BLACK).set_z_index(1)
        sr = SurroundingRectangle(t, color=GRAY_A, buff=0.3, corner_radius=0.1, fill_opacity=0.5)

        self.add(t, sr)

class Q(ThreeDScene):
    def construct(self):

        self.camera.background_color = WHITE

        t = MathTex(r"\mathbb{Q} = \left\{ {a \over b} \: \Big\vert \: a,b \in \mathbb{Z} \:\:\:,\:\:\: b \neq 0 \right\}", color=BLACK).set_z_index(1)
        sr = SurroundingRectangle(t, color=GRAY_A, buff=0.3, corner_radius=0.1, fill_opacity=0.5)

        self.add(t, sr)

class square(ThreeDScene):
    def construct(self):

        self.camera.background_color = WHITE

        sq = Polygon((-1,1,0), (-1,-1,0), (1, -1, 0), (1,1,0), color=BLACK, stroke_width=5).shift(DOWN*0.5)
        l1 = MathTex("1", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).next_to(sq, DOWN)
        l2 = MathTex("1", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).next_to(sq, RIGHT)
        d = Line((-1,-1,0), (1,1,0), color=RED, stroke_width=7).shift(DOWN*0.5).set_z_index(-1)
        dl = MathTex(r"\sqrt{2}", color=RED, stroke_width=1.5, tex_template=TexFontTemplates.times_fourier_it).shift(UP*0.3+LEFT*0.3).rotate(45*DEGREES).shift(DOWN*0.5)

        self.add(sq, l1, l2, d, dl)

class R(ThreeDScene):
    def construct(self):

        self.camera.background_color = WHITE

        t = MathTex(r"\mathbb{R} = \mathbb{Q} \:\cup\: \mathbb{I}", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).set_z_index(1)
        sr = SurroundingRectangle(t, color=GRAY_A, buff=0.3, corner_radius=0.1, fill_opacity=0.5)

class number_line(ThreeDScene):
    def construct(self):

        self.camera.background_color = WHITE

        # Reta numérica
        number_line = NumberLine(x_range=[-3.999,4,1], include_tip=True, tip_shape=StealthTip, color=BLACK, stroke_width=2.5)
        n3n = MathTex("-3", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-3.15,-1.4,0))
        n2n = MathTex("-2", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-2.15,-1.4,0))
        n1n = MathTex("-1", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-1.15,-1.4,0))
        n0 = MathTex("0", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((0,-1.4,0))
        n1 = MathTex("1", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((1,-1.4,0))
        n2 = MathTex("2", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((2,-1.4,0))
        n3 = MathTex("3", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((3,-1.4,0))
        re_axis_numbers = VGroup(n3n, n2n, n1n, n0, n1, n2, n3).set_color(BLACK).shift(UP)
        number_line_label = MathTex(r"\mathbb{R}", color=BLACK).next_to(number_line, DR, buff=0.1).shift(UP*0.3)
        
        # Ponto sobre a reta
        dot = Dot((2,0,0), color=RED)

        # Módulo do ponto (reta da origem até o ponto)
        origin = number_line.number_to_point(0)
        dot_module = Line(start=origin, end=(dot), color=RED, stroke_width=5)

        #dot_label = MathTex(", color=RED, stroke_width=1.5).move_to((2,0.5,0))

        # Medida da distância entre o ponto e a origem
        m_1 = Line((0,0.5,0), (2,0.5,0), stroke_width=5)
        m_2 = Line((0,0.1,0), (0,-0.1,0)).next_to(m_1, LEFT, buff=0)
        m_3 = Line((0,0.1,0), (0,-0.1,0)).next_to(m_1, RIGHT, buff=0)
        m_number = MathTex("2", tex_template=TexFontTemplates.times_fourier_it).next_to(m_1, UP, buff=0.2)
        m = VGroup(m_1, m_2, m_3, m_number).set_color(RED)

        self.add(number_line, number_line_label, dot, dot_module, m, re_axis_numbers)

class number_line_square(ThreeDScene):
    def construct(self):

        self.camera.background_color = WHITE

        # Reta numérica
        number_line = NumberLine(x_range=[-3.999,4,1], include_tip=True, tip_shape=StealthTip, color=BLACK, stroke_width=2.5)
        n3n = MathTex("-3", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-3.15,-1.4,0))
        n2n = MathTex("-2", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-2.15,-1.4,0))
        n1n = MathTex("-1", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-1.15,-1.4,0))
        n0 = MathTex("0", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((0,-1.4,0))
        n1 = MathTex("1", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((1,-1.4,0))
        n2 = MathTex("2", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((2,-1.4,0))
        n3 = MathTex("3", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((3,-1.4,0))
        re_axis_numbers = VGroup(n3n, n2n, n1n, n0, n1, n2, n3).set_color(BLACK).shift(UP)
        number_line_label = MathTex(r"\mathbb{R}", color=BLACK).next_to(number_line, DR, buff=0.1).shift(UP*0.3)
        
        # Ponto sobre a reta
        dot = Dot((1.414,0,0), color=RED)

        # Módulo do ponto (reta da origem até o ponto)
        origin = number_line.number_to_point(0)
        dot_module = Line(start=origin, end=(dot), color=RED, stroke_width=5)

        dot_label = MathTex(r"\sqrt{2}", color=RED, tex_template=TexFontTemplates.times_fourier_it).move_to((1.414,0.5,0)).scale(0.8)

        sq = Polygon((0,0,0), (1,0,0), (1, 1, 0), (0,1,0), color=BLACK, stroke_width=5, stroke_opacity=0.4).rotate(-45*DEGREES, about_point=(0,0,0))

        self.add(sq, number_line, number_line_label, dot, dot_module, dot_label, re_axis_numbers)

class number_line_symmetrical(ThreeDScene):
    def construct(self):

        self.camera.background_color = WHITE

        # Reta numérica
        number_line = NumberLine(x_range=[-3.999,4,1], include_tip=True, tip_shape=StealthTip, color=BLACK, stroke_width=2.5)
        n3n = MathTex("-3", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-3.15,-1.4,0))
        n2n = MathTex("-2", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-2.15,-1.4,0))
        n1n = MathTex("-1", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-1.15,-1.4,0))
        n0 = MathTex("0", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((0,-1.4,0))
        n1 = MathTex("1", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((1,-1.4,0))
        n2 = MathTex("2", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((2,-1.4,0))
        n3 = MathTex("3", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((3,-1.4,0))
        re_axis_numbers = VGroup(n3n, n2n, n1n, n0, n1, n2, n3).set_color(BLACK).shift(UP)
        number_line_label = MathTex(r"\mathbb{R}", color=BLACK).next_to(number_line, DR, buff=0.1).shift(UP*0.3)
        
        # Ponto sobre a reta
        dot = Dot((2,0,0), color=BLACK)
        dot_2 = Dot((-2,0,0), color=RED)

        # Módulo do ponto (reta da origem até o ponto)
        origin = number_line.number_to_point(0)
        dot_module = Line(start=origin, end=(dot), color=BLACK, stroke_width=5)
        dot_module_2 = Line(start=origin, end=(dot_2), color=RED, stroke_width=5)

        # Seta do giro de 180°
        arrow = CurvedArrow(start_point=(4,0,0), end_point=(-4,0.2,0), radius=4.01, tip_shape=StealthTip, color=DARK_GRAY).scale(0.5).shift(DOWN*1+RIGHT*0.04)
        angle_label = MathTex(r"180^{\circ}", color=DARK_GRAY, tex_template=TexFontTemplates.times_fourier_it).move_to((0,1,0)).scale(0.8)
        product_label_1 = MathTex(r"\times", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).scale(0.7).move_to((0,2.3,0)).shift(LEFT*0.4)
        product_label_2 = MathTex(r"(-1)", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).scale(0.8).next_to(product_label_1, RIGHT, buff=0.1)

        self.add(arrow, product_label_1, product_label_2, angle_label, number_line, number_line_label, dot, dot_2, dot_module, dot_module_2, re_axis_numbers)

class C(ThreeDScene):
    def construct(self):

        self.camera.background_color = WHITE

        t = MathTex(r"\mathbb{C} = \left\{ z \: \vert \: z=a+bi \:\:,\:\: a,b \in \mathbb{R} \:\:,\:\: i = \sqrt{-1} \right\}", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).set_z_index(1)
        sr = SurroundingRectangle(t, color=GRAY_A, buff=0.3, corner_radius=0.1, fill_opacity=0.5)

        self.add(t, sr)

class complex_plane(ThreeDScene):
    def construct(self):

        self.camera.background_color = WHITE

        # Reta real
        re_axis = NumberLine(x_range=[-3.999,4,1], include_tip=True, tip_shape=StealthTip, color=BLACK).shift(DOWN)
        re_axis_label = MathTex(r"Re", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).next_to(re_axis, DR, buff=0.1)

        n3n = MathTex("-3", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-3.15,-1.4,0))
        n2n = MathTex("-2", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-2.15,-1.4,0))
        n1n = MathTex("-1", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-1.15,-1.4,0))
        n1 = MathTex("1", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((1,-1.4,0))
        n2 = MathTex("2", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((2,-1.4,0))
        n3 = MathTex("3", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((3,-1.4,0))
        re_axis_numbers = VGroup(n3n, n2n, n1n, n1, n2, n3).set_color(BLACK)
        
        self.add(re_axis, re_axis_numbers, re_axis_label)

        # Eixo imaginário
        im_axis = NumberLine(x_range=[-2.999,2.999], include_numbers=False, include_tip=True, tip_shape=StealthTip, rotation=90*DEGREES, color=BLACK)
        im_axis_label = MathTex(r"Im", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).next_to(im_axis, UL, buff=0.1)

        i0 = MathTex(r"0", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-0.2,-1.4,0))
        i1 = MathTex(r"-i", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-0.4,-1.97,0))
        i2 = MathTex(r"i", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-0.25,0.05,0))
        i3 = MathTex(r"2i", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-0.3,1.05,0))
        i4 = MathTex(r"3i", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-0.3,2.05,0))
        i_numbers = VGroup(i1, i0, i2, i3, i4).set_color(BLACK)

        # Plano
        number_plane = NumberPlane(
            x_range=(-3.5, 3.5, 1),
            y_range=(-1.5, 3.5, 1),
            x_length=7,
            y_length=5
        ).move_to(DOWN*0).set_z_index(-1).set_opacity(0.3).set_color(GRAY)
        
        # Número complexo como par ordenado

            # Par ordenado
        x = ValueTracker(2.5)
        y = ValueTracker(0.5)

        pair_dot = Dot((x.get_value(), y.get_value(), 0), color=RED)
        pair_label = MathTex("(a,b)", color=RED, tex_template=TexFontTemplates.times_fourier_it).scale(0.8).next_to(pair_dot, UP).shift(DOWN*0.15)
        complex_number = MathTex("=\: a + bi", color=RED, tex_template=TexFontTemplates.times_fourier_it).scale(0.8).next_to(pair_label, RIGHT)


            # Projeções do par ordenado
        a_proj = DashedLine(pair_dot, (x.get_value(), -1, 0), color=RED).set_z_index(-1)
        a_value = MathTex("a", color=RED, tex_template=TexFontTemplates.times_fourier_it).next_to(a_proj, DOWN, buff=0.27).scale(0.9)

        b_proj = DashedLine(pair_dot, (0, y.get_value(), 0), color=RED).set_z_index(-1)
        b_value = MathTex("b", color=RED, tex_template=TexFontTemplates.times_fourier_it).next_to(b_proj, LEFT, buff=0.15).scale(0.9)     

        self.add(im_axis, number_plane, i_numbers, im_axis_label, complex_number,
                 pair_dot, pair_label, a_proj, a_value, b_proj, b_value)

        # Ponto-exemplo (3 + 2i)
        pair_dot_example = Dot((-3,1,0), color=BLACK)
        pair_label_example = MathTex("(-3,2)", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).scale(0.8).next_to((-3.1, 1, 0), UP).shift(DOWN*0.1)
        pair_label_example_2 = MathTex("-3 + 2i \: =", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).scale(0.8).next_to(pair_label_example, LEFT)

        self.add(pair_dot_example, pair_label_example, pair_label_example_2)

class complex_plane_90_rotation(ThreeDScene):
    def construct(self):

        self.camera.background_color = WHITE

        # Reta real
        re_axis = NumberLine(x_range=[-3.999,4,1], include_tip=True, tip_shape=StealthTip, color=BLACK).shift(DOWN)
        re_axis_label = MathTex(r"Re", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).next_to(re_axis, DR, buff=0.1)

        n3n = MathTex("-3", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-3.15,-1.4,0))
        n2n = MathTex("-2", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-2.15,-1.4,0))
        n1n = MathTex("-1", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-1.15,-1.4,0))
        n1 = MathTex("1", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((1,-1.4,0))
        n2 = MathTex("2", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((2,-1.4,0))
        n3 = MathTex("3", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((3,-1.4,0))
        re_axis_numbers = VGroup(n3n, n2n, n1n, n1, n2, n3).set_color(BLACK)
        
        self.add(re_axis, re_axis_numbers, re_axis_label)

        # Eixo imaginário
        im_axis = NumberLine(x_range=[-2.999,2.999], include_numbers=False, include_tip=True, tip_shape=StealthTip, rotation=90*DEGREES, color=BLACK)
        im_axis_label = MathTex(r"Im", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).next_to(im_axis, UL, buff=0.1)

        i0 = MathTex(r"0", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-0.2,-1.4,0))
        i1 = MathTex(r"-i", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-0.4,-1.97,0))
        i2 = MathTex(r"i", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-0.25,0.05,0))
        i3 = MathTex(r"2i", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-0.3,1.05,0))
        i4 = MathTex(r"3i", tex_template=TexFontTemplates.times_fourier_it).scale(0.75).move_to((-0.3,2.05,0))
        i_numbers = VGroup(i1, i0, i2, i3, i4).set_color(BLACK)

        # Plano
        number_plane = NumberPlane(
            x_range=(-3.5, 3.5, 1),
            y_range=(-1.5, 3.5, 1),
            x_length=7,
            y_length=5
        ).move_to(DOWN*0).set_z_index(-1).set_opacity(0.3).set_color(GRAY)

        self.add(im_axis, number_plane, i_numbers, im_axis_label)

        # Multiplicar por i
        arrow_1 = CurvedArrow(start_point=(4,-2,0), end_point=(0,2,0), radius=4, tip_shape=StealthTip, color=DARK_GRAY, stroke_width=3).scale(0.5).shift(LEFT*1+DOWN*0.05)
        arrow_2 = CurvedArrow(start_point=(-1,2,0), end_point=(-4,-2,0), radius=3.9, tip_shape=StealthTip, color=DARK_GRAY, stroke_width=3).scale(0.5).shift(RIGHT*1.3)

        angle_label_1 = MathTex(r"90^{\circ}", color=DARK_GRAY, tex_template=TexFontTemplates.times_fourier_it).scale(0.8).next_to((0,-1,0), UR, buff=0.5).shift(RIGHT*0.4)
        product_label_1_1 = MathTex(r"\times", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).scale(0.6).next_to((0,-1,0), UR, buff=1.5)
        product_label_1_2 = MathTex(r"i", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).scale(0.9).next_to(product_label_1_1, RIGHT, buff=0.1).shift(UP*0.05)

        angle_label_2 = MathTex(r"90^{\circ}", color=DARK_GRAY, tex_template=TexFontTemplates.times_fourier_it).scale(0.8).next_to((0,-1,0), UL, buff=0.5).shift(LEFT*0.4)
        product_label_2_1 = MathTex(r"\times", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).scale(0.6).next_to((0,-1,0), UL, buff=1.5).shift(LEFT*0.3)
        product_label_2_2 = MathTex(r"i", color=BLACK, tex_template=TexFontTemplates.times_fourier_it).scale(0.9).next_to(product_label_2_1, RIGHT, buff=0.1).shift(UP*0.05)

        self.add(arrow_1, angle_label_1, product_label_1_1, product_label_1_2,
                 arrow_2, angle_label_2, product_label_2_1, product_label_2_2)

class Diagram(Scene):
    def construct(self):

        self.camera.background_color = WHITE

        # Um conjunto está contido no próximo
        t = MathTex(r"\mathbb{N}",r"\:\: \subset \:\:",r"\mathbb{Z}",r"\:\: \subset \:\:",r"\mathbb{Q}",r"\:\: \subset \:\:",r"\mathbb{R}",r"\:\: \subset \:\:",r"\mathbb{C}", tex_template=TexFontTemplates.times_fourier_it)

        self.add(t)

        # Naturais
        cN = Ellipse(width=2, height=2, color=LIGHT_PINK, fill_opacity=0.2).set_z_index(6)
        tN = MathTex(r"\mathbb{N}", color=PURPLE_E, tex_template=TexFontTemplates.times_fourier_it).next_to(cN, UP, buff=-0.1).shift(RIGHT*0.1).set_z_index(7).scale(1.2)
        tNb = MathTex(r"\mathbb{N}", color=WHITE, stroke_width=6, stroke_opacity=0.5, tex_template=TexFontTemplates.times_fourier_it).move_to(tN).set_z_index(6).scale(1.2)
        n1 = MathTex("1", tex_template=TexFontTemplates.times_fourier_it).move_to(cN).shift(UP*0.5)
        n2 = MathTex("0", tex_template=TexFontTemplates.times_fourier_it).move_to(cN).shift(LEFT*0.5+DOWN*0.2)
        n3 = MathTex("2", tex_template=TexFontTemplates.times_fourier_it).move_to(cN).shift(RIGHT*0.4+DOWN*0.3)
        nN = VGroup(n1, n2, n3).set_z_index(7).set_color(BLACK)
        N = VGroup(cN, tN, tNb, nN).shift(LEFT*0.8)

        # Inteiros
        cZ = Ellipse(width=4.5, height=3, color=BLUE, fill_opacity=0.2).set_z_index(5)
        tZ = MathTex(r"\mathbb{Z}", color=BLUE_E, tex_template=TexFontTemplates.times_fourier_it).next_to(cZ, UP, buff=-0.08).set_z_index(6).scale(1.2).shift(RIGHT*0.1)
        tZb = MathTex(r"\mathbb{Z}", color=WHITE, stroke_width=6, stroke_opacity=0.5, tex_template=TexFontTemplates.times_fourier_it).move_to(tZ).set_z_index(5).scale(1.2)
        n4 = MathTex("-1", tex_template=TexFontTemplates.times_fourier_it).move_to(cZ).shift(RIGHT*0.7+UP*0.7)
        n5 = MathTex("-2", tex_template=TexFontTemplates.times_fourier_it).move_to(cZ).shift(RIGHT*1.5)
        n6 = MathTex("-3", tex_template=TexFontTemplates.times_fourier_it).move_to(cZ).shift(RIGHT*0.9+DOWN*0.7)
        nZ = VGroup(n4, n5, n6).set_z_index(6).set_color(BLACK)    
        NZ = VGroup(N, cZ, tZ, tZb, nZ).shift(LEFT)

        # Racionais
        cQ = Ellipse(width=7, height=4, color=GREEN, fill_opacity=0.2).set_z_index(4)
        tQ = MathTex(r"\mathbb{Q}", color=GREEN_E, tex_template=TexFontTemplates.times_fourier_it).next_to(cQ, UP, buff=-0.1).shift(LEFT*0.15).set_z_index(5).scale(1.2)
        tQb = MathTex(r"\mathbb{Q}", color=WHITE, stroke_width=6, stroke_opacity=0.5, tex_template=TexFontTemplates.times_fourier_it).move_to(tQ).set_z_index(4).scale(1.2)
        n7 = MathTex(r"1 \over 2", tex_template=TexFontTemplates.times_fourier_it).move_to(cQ).shift(RIGHT*1.9+UP*0.8)
        n8 = MathTex(r"7 \over 3", tex_template=TexFontTemplates.times_fourier_it).move_to(cQ).shift(RIGHT*2.7)
        n9 = MathTex(r"0,111...", tex_template=TexFontTemplates.times_fourier_it).move_to(cQ).shift(RIGHT*2+DOWN).scale(0.9)
        nQ = VGroup(n7, n8, n9).set_z_index(5).set_color(BLACK)
        NZQ = VGroup(NZ, cQ, tQ, tQb, nQ).shift(LEFT*0.7)

        # Reais
        cR = Ellipse(width=9, height=5, color=ORANGE, fill_opacity=0.2).set_z_index(3)
        tR = MathTex(r"\mathbb{R}", color=DARK_BROWN, tex_template=TexFontTemplates.times_fourier_it).next_to(cR, UP, buff=-0.08).set_z_index(4).scale(1.2)
        tRb = MathTex(r"\mathbb{R}", color=WHITE, stroke_width=6, stroke_opacity=0.5, tex_template=TexFontTemplates.times_fourier_it).move_to(tR).set_z_index(3).scale(1.2)
        n10 = MathTex(r"\pi", tex_template=TexFontTemplates.times_fourier_it).move_to(cR).shift(RIGHT*3.25+UP).scale(1.3)
        n11 = MathTex(r"\sqrt{2}", tex_template=TexFontTemplates.times_fourier_it).move_to(cR).shift(RIGHT*3.8)
        n12 = MathTex(r"e", tex_template=TexFontTemplates.times_fourier_it).move_to(cR).shift(RIGHT*3.3+DOWN).scale(1.2)
        nR = VGroup(n10, n11, n12).set_z_index(4).shift(LEFT*0.2).set_color(BLACK)
        NZQR = VGroup(NZQ, cR, tR, tRb, nR).shift(LEFT*0.9)
        
        # Complexos
        cC = Ellipse(width=11.5, height=6, color=RED, fill_opacity=0.2).set_z_index(2)
        tC = MathTex(r"\mathbb{C}", color=RED_E, tex_template=TexFontTemplates.times_fourier_it).next_to(cC, UP, buff=-0.1).shift(LEFT*0.2).set_z_index(3).scale(1.2)
        tCb = MathTex(r"\mathbb{C}", color=WHITE, stroke_width=6, stroke_opacity=0.5, tex_template=TexFontTemplates.times_fourier_it).move_to(tC).set_z_index(2).scale(1.2)
        n13 = MathTex(r"\sqrt{-1}", tex_template=TexFontTemplates.times_fourier_it).move_to(cC).shift(RIGHT*4.3+UP)
        n14 = MathTex(r"3+2i", tex_template=TexFontTemplates.times_fourier_it).move_to(cC).shift(RIGHT*4.6+DOWN*0.2)
        n15 = MathTex(r"-3i", tex_template=TexFontTemplates.times_fourier_it).move_to(cC).shift(RIGHT*4.1+DOWN*1.2)
        nC = VGroup(n13, n14, n15).set_z_index(3).set_color(BLACK)
        NZQRC = VGroup(NZQR, cC, tC, tCb, nC)

        self.add(NZQRC)
