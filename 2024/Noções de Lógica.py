# Noções de Lógica

from manim import *

#THUMBNAIL
class tn(Scene):
    def construct(self):

        t = Tex("Lógica").shift(UP).scale(3).set_color_by_gradient([WHITE, GRAY_C])
        ex = MathTex(r"\forall x,y \in \mathbb{R} \: ( x < y \: \Rightarrow \: \exists m \in \mathbb{R}, \: x < m < y)", stroke_width=1.5).scale(1.3).set_color_by_gradient([GOLD_B, GOLD_E]).shift(DOWN)

        self.add(ex, t)


#PROPOSIÇÃO
class vid1(Scene):
    def construct(self):

        ex = MathTex(r"\forall x,y \in \mathbb{R} \: ( x < y \: \Rightarrow \: \exists m \in \mathbb{R}, \: x < m < y)")

        t1 = Tex("Proposição", color=YELLOW).shift(UP)
        t2 = Tex("Afirmação de uma relação entre duas coisas").next_to(t1, DOWN)
        g1 = VGroup(t1, t2)
        sr1 = SurroundingRectangle(g1, buff=0.2, stroke_color=YELLOW, fill_color=[YELLOW_E, YELLOW_C], stroke_width=1, fill_opacity=0.1)
        g2 = VGroup(g1, sr1)
        t3 = Tex("`Um coelho é um animal'")
        t3a = Tex("`Um ","coelho"," é um animal'")
        t3a[1].set_color(YELLOW)
        t3b = Tex("`Um ","coelho"," é um "," animal","'")
        t3b[1].set_color(YELLOW)
        t3b[3].set_color(YELLOW)
        t4 = Tex("`8 é um número par'")
        t5 = MathTex("5 - 1 = 4")
        t6 = MathTex("2 > 3")
        t7 = Tex("`8 é ímpar?'", color=RED)
        t8 = MathTex(r"\sqrt2 + 4 \sqrt5", color=RED).shift(DOWN*0.5)

        self.play(Write(ex))
        self.wait()
        self.play(FadeOut(ex))
        self.wait()

        
        self.play(Write(t1))
        self.wait()
        self.play(LaggedStart(FadeIn(t2), Create(sr1), lag_ratio=1))
        self.wait()
        self.play(g2.animate.shift(UP*2))
        self.wait()
        self.play(FadeIn(t3))
        self.wait()
        self.play(TransformMatchingTex(t3, t3a))
        self.wait()
        self.play(TransformMatchingTex(t3a, t3b))
        self.wait()
        self.play(t3b.animate.shift(DOWN*5))
        self.wait()
        self.play(FadeIn(t4))
        self.wait()
        self.play(t4.animate.shift(DOWN*5))
        self.wait()
        self.play(FadeIn(t5))
        self.wait(3)
        self.play(t5.animate.shift(DOWN*5))
        self.wait()
        self.play(FadeIn(t6))
        self.wait(3)
        self.play(t6.animate.shift(DOWN*5))
        self.wait()
        self.play(FadeIn(t7))
        self.wait(3)
        self.play(t7.animate.shift(UP))
        self.wait()
        self.play(FadeIn(t8))
        self.wait(3)
        self.play(t8.animate.shift(DOWN*5), t7.animate.shift(DOWN*6))
        self.wait()
        self.play(FadeOut(g2))

#VALOR LÓGICO / PRINCÍPIOS DA LÓGICA
class vid2(Scene):
    def construct(self):        

        t1 = Tex("Princípio do Terceiro Excluído", color=YELLOW).shift(UP*2)
        t2 = Tex("Toda proposição é ou verdadeira ou falsa").next_to(t1, DOWN)
        g1 = VGroup(t1, t2)
        sr1 = SurroundingRectangle(g1, buff=0.2, stroke_color=YELLOW, fill_color=[YELLOW_E, YELLOW_C], stroke_width=1, fill_opacity=0.1)
        g2 = VGroup(g1, sr1)

        t3 = Tex("Princípio da Não-Contradição", color=YELLOW).shift(DOWN*0.5)
        t4 = Tex("Uma proposição não pode ser").next_to(t3, DOWN)
        t5 = Tex("verdadeira e falsa ao mesmo tempo").next_to(t4, DOWN, buff=0.1)
        g3 = VGroup(t3, t4, t5)
        sr2 = SurroundingRectangle(g3, buff=0.2, stroke_color=YELLOW, fill_color=[YELLOW_E, YELLOW_C], stroke_width=1, fill_opacity=0.1)
        g4 = VGroup(g3, sr2)

        t6 = MathTex("5 - 1 = 4").shift(UP)
        v = Tex("(V)").shift(UP+LEFT*2)
        v[0].set_color(GREEN)
        t7 = MathTex("2 > 3").shift(DOWN*0.2)
        f = Tex("(F)").shift(DOWN*0.2+LEFT*2)
        f[0].set_color(RED)

        self.play(Write(t2))
        self.wait()
        self.play(FadeIn(t1), Create(sr1))
        self.wait()

        self.play(LaggedStart(Write(t4), Write(t5), lag_ratio=1), run_time=3)
        self.wait()
        self.play(FadeIn(t3), Create(sr2))
        self.wait()
        self.play(FadeOut(g2, g4))
        self.wait()

        self.play(FadeIn(t6, v))
        self.wait()
        self.play(FadeIn(t7, f))
        self.wait()
        self.play(FadeOut(t6, t7, v, f))
        self.wait()

#NEGAÇÃO
class vid3(Scene):
    def construct(self):        

        t1 = Tex("P: `O céu é azul'").shift(UP)
        t2 = Tex(r"P: `O céu não é azul'").shift(DOWN*0.5)
        t3 = MathTex(r"\sim").next_to(t2, LEFT, buff=0.1)
        
        v = Tex("(V)").shift(UP+RIGHT*3.5)
        v[0].set_color(GREEN)

        f = Tex("(F)").shift(DOWN*0.5+RIGHT*3.5)
        f[0].set_color(RED)

        self.play(FadeIn(t1))
        self.wait()
        self.play(FadeIn(t2, t3))
        self.wait()
        self.play(FadeIn(v))
        self.wait()
        self.play(FadeIn(f))
        self.wait()

#CONECTIVOS

#CONJUNÇÃO
class vid4(Scene):
    def construct(self):        

        #EXPLICAÇÃO
        t1 = Tex("P").shift(LEFT).scale(1.5)
        t2 = Tex("Q").shift(RIGHT).scale(1.5)
        g1 = VGroup(t1, t2)
        
        t3 = Tex("Conjunção", color=GREEN).to_corner(UP)
        ut3 = Underline(t3, color=GREEN)
        
        t4 = Tex("P e Q")
        
        t5a = MathTex(r"\wedge")
        t5b = Tex("P").next_to(t5a, LEFT)
        t5c = Tex("Q").next_to(t5a, RIGHT)
        t5 = VGroup(t5a, t5b, t5c)

        v1 = Tex("(V)").next_to(t5, UP)
        v1[0].set_color(GREEN)
        
        v2 = Tex("(V)").shift(DOWN*0.5+LEFT).scale(0.7)
        v2[0].set_color(GREEN)

        v3 = Tex("(V)").shift(DOWN*0.5+RIGHT).scale(0.7)
        v3[0].set_color(GREEN)

        f1 = Tex("(F)").next_to(t5, UP)
        f1[0].set_color(RED)

        f2 = Tex("(F)").shift(DOWN*0.5+LEFT).scale(0.7)
        f2[0].set_color(RED)

        self.play(LaggedStart(Write(t1), Write(t2), lag_ratio=0.5))
        self.wait()
        self.play(Write(t3), Create(ut3))
        self.wait()
        self.play(TransformMatchingShapes(g1, t4))
        self.wait()
        self.play(TransformMatchingShapes(t4, t5))
        self.wait()
        self.play(FadeIn(v1))
        self.wait()
        self.play(FadeIn(v2, v3))
        self.wait()
        self.play(FadeOut(v1, v2), FadeIn(f2))
        self.wait()
        self.play(FadeIn(f1))
        self.wait()
        self.play(LaggedStart(FadeOut(f1, f2, v3), t5.animate.shift(UP*2), lag_ratio=0.5))


        #EXEMPLO (v)

        t6 = Tex("P: `O céu é azul'").shift(LEFT*2)
        t7 = Tex("Q: `8 é par'").shift(RIGHT*2)
        g2 = VGroup(t6, t7)
        t8 = Tex("`O céu é azul e 8 é par'")

        v4 = Tex("(V)").shift(DOWN*0.5+LEFT*0.9).scale(0.7)
        v4[0].set_color(GREEN)

        v5 = Tex("(V)").shift(DOWN*0.5+RIGHT*1.5).scale(0.7)
        v5[0].set_color(GREEN)

        v6 = Tex("(V)").next_to(t8, LEFT, buff=0.5)
        v6[0].set_color(GREEN)
    
        self.play(FadeIn(t6))
        self.wait()
        self.play(FadeIn(t7))
        self.wait()
        self.play(LaggedStart(FadeOut(g2), FadeIn(t8), lag_ratio=0.5))
        self.wait()
        self.play(FadeIn(v6))
        self.wait()
        self.play(FadeIn(v4, v5))
        self.wait()
        self.play(FadeOut(v4, v5, v6, t8))

        #EXEMPLO (F)

        t9b = MathTex("1 > 2").shift(LEFT*1.5)
        t9a = Tex("P:").next_to(t9b, LEFT, buff=0.3)
        t9 = VGroup(t9a, t9b)

        t10a = Tex("Q:").shift(RIGHT*1.5)
        t10b = MathTex("4 > 3").next_to(t10a, RIGHT, buff=0.3)
        t10 = VGroup(t10a, t10b)

        g3 = VGroup(t9, t10)

        t11c = Tex("e")
        t11a = MathTex("1 > 2").next_to(t11c, LEFT, buff=0.3)
        t11b = MathTex("4 > 3").next_to(t11c, RIGHT, buff=0.3)
        t11 = VGroup(t11a, t11b, t11c)

        f3 = Tex("(F)").shift(DOWN*0.5+LEFT).scale(0.7)
        f3[0].set_color(RED)

        v7 = Tex("(V)").shift(DOWN*0.5+RIGHT).scale(0.7)
        v7[0].set_color(GREEN)

        f4 = Tex("(F)").next_to(t11, LEFT, buff=0.5)
        f4[0].set_color(RED)

        self.play(FadeIn(t9))
        self.wait()
        self.play(FadeIn(t10))
        self.wait()
        self.play(LaggedStart(FadeOut(g3), FadeIn(t11), lag_ratio=0.5))
        self.wait()
        self.play(FadeIn(f4))
        self.wait()
        self.play(FadeIn(f3, v7))
        self.wait()
        self.play(FadeOut(v7, f3, f4, t11, t5, t3, ut3))

#DISJUNÇÃO
class vid5(Scene):
    def construct(self):        

        #EXPLICAÇÃO
        t1 = Tex("P").shift(LEFT).scale(1.5)
        t2 = Tex("Q").shift(RIGHT).scale(1.5)
        g1 = VGroup(t1, t2)
        
        t3 = Tex("Disjunção", color=GREEN).to_corner(UP)
        ut3 = Underline(t3, color=GREEN)
        
        t4 = Tex("P ou Q")

        self.play(LaggedStart(Write(t1), Write(t2), lag_ratio=0.5))
        self.wait()
        self.play(Write(t3), Create(ut3))
        self.wait()
        self.play(TransformMatchingShapes(g1, t4))
        self.wait()
        self.play(t4.animate.shift(UP*2))
        self.wait()

        #DIFERENÇA DISJ. INCLUSIVA / EXCLUSIVA

        t6 = Tex("`Choveu em São Paulo ou no Rio'")
        t7 = Tex("`Maria é paulista ou carioca'")
        t8 = Tex("Inclusiva", color=GREEN).shift(UP*2+LEFT*3)
        t9 = Tex("Exclusiva", color=GREEN).shift(UP*2+RIGHT*3)

        t10a = MathTex(r"\vee")
        t10b = Tex("P").next_to(t10a, LEFT)
        t10c = Tex("Q").next_to(t10a, RIGHT)
        t10 = VGroup(t10a, t10b, t10c).next_to(t8, DOWN)

        ginc = VGroup(t8, t10)

        t11a = MathTex(r"\underline \vee")
        t11b = Tex("P").next_to(t11a, LEFT)
        t11c = Tex("Q").next_to(t11a, RIGHT)
        t11 = VGroup(t11a, t11b, t11c).next_to(t9, DOWN)

        gexc = VGroup(t9, t11)

        t12 = Tex("`P ou Q'", color=GRAY).next_to(t10, DOWN, buff=0.5)
        t13 = Tex("`ou P ou Q'", color=GRAY).next_to(t11, DOWN, buff=0.5)

        self.play(FadeIn(t6))
        self.wait()
        self.play(FadeOut(t6))
        self.wait()
        self.play(FadeIn(t7))
        self.wait()
        self.play(FadeOut(t7))
        self.wait()
        self.play(FadeOut(t4))
        self.wait()
        self.play(LaggedStart(FadeIn(t8), FadeIn(t9), lag_ratio=1))
        self.wait()
        self.play(LaggedStart(Write(t10), Write(t11), lag_ratio=1))
        self.wait()
        self.play(FadeIn(t12))
        self.wait()
        self.play(FadeIn(t13))
        self.wait()
        self.play(FadeOut(t12, t13))
        self.play(ginc.animate.shift(RIGHT*3), gexc.animate.shift(RIGHT*6))
        self.wait()

        #EXEMPLO (V) INCLUSIVA

        t14b = MathTex("1 + 1 = 2").shift(LEFT*1.5)
        t14a = Tex("P:").next_to(t14b, LEFT, buff=0.3)
        t14 = VGroup(t14a, t14b)

        t15a = Tex("Q:").shift(RIGHT*1.5)
        t15b = MathTex("2 + 2 = 3").next_to(t15a, RIGHT, buff=0.3)
        t15 = VGroup(t15a, t15b)

        ginc2 = VGroup(t14, t15).shift(DOWN*0.5)

        t16a = Tex("ou")
        t16b = MathTex("1 + 1 = 2").next_to(t16a, LEFT, buff=0.3)
        t16c = MathTex("2 + 2 = 3").next_to(t16a, RIGHT, buff=0.3)
        t16 = VGroup(t16a, t16b, t16c).shift(DOWN*0.5)

        v1 = Tex("(V)").next_to(t16, LEFT, buff=0.5)
        v1[0].set_color(GREEN)
        
        v2 = Tex("(V)").shift(DOWN+LEFT*1.5).scale(0.7)
        v2[0].set_color(GREEN)

        f1 = Tex("(F)").shift(DOWN+RIGHT*1.5).scale(0.7)
        f1[0].set_color(RED)

        t17a = Tex("ou")
        t17b = MathTex("1 + 1 = 0").next_to(t17a, LEFT, buff=0.3)
        t17c = MathTex("2 + 2 = 3").next_to(t17a, RIGHT, buff=0.3)
        t17 = VGroup(t17a, t17b, t17c).shift(DOWN*0.5)

        self.play(FadeIn(t14))
        self.wait()
        self.play(FadeIn(t15))
        self.wait()
        self.play(LaggedStart(FadeOut(ginc2), FadeIn(t16), lag_ratio=0.5))
        self.wait()
        self.play(FadeIn(v1))
        self.wait()
        self.play(FadeIn(v2, f1))
        self.wait()
        
        #EXEMPLO (F) INCLUSIVA
        
        f2 = Tex("(F)").next_to(t17, LEFT, buff=0.5)
        f2[0].set_color(RED)
        
        f3 = Tex("(F)").shift(DOWN+LEFT*1.5).scale(0.7)
        f3[0].set_color(RED)
        
        self.play(FadeOut(v1, v2))
        self.wait()
        self.play(TransformMatchingTex(t16, t17))
        self.wait()
        self.play(FadeIn(f2, f3))
        self.wait()

        #EXEMPLO (V) EXCLUSIVA

        t18a = Tex("ou")
        t18b = MathTex("1 + 1 = 2").next_to(t18a, LEFT, buff=0.3)
        t18c = MathTex("2 + 2 = 3").next_to(t18a, RIGHT, buff=0.3)
        t18d = Tex("ou").next_to(t18b, LEFT, buff=0.3)
        t18 = VGroup(t18a, t18b, t18c, t18d).shift(DOWN*0.5+RIGHT*0.5)

        v3 = Tex("(V)").next_to(t18, LEFT, buff=0.5)
        v3[0].set_color(GREEN)

        v4 = Tex("(V)").shift(DOWN+LEFT).scale(0.7)
        v4[0].set_color(GREEN)

        f4 = Tex("(F)").shift(DOWN+RIGHT*2).scale(0.7)
        f4[0].set_color(RED)
        
        self.play(FadeOut(f1, f2, f3, t17))
        self.play(gexc.animate.shift(LEFT*9), ginc.animate.shift(LEFT*9))
        self.wait()
        self.play(FadeIn(t18))
        self.wait()
        self.play(FadeIn(v3))
        self.wait()
        self.play(FadeIn(v4, f4))
        self.wait()

        #EXEMPLO (F) EXCLUSIVA

        t19a = Tex("ou")
        t19b = MathTex("1 + 1 = 2").next_to(t19a, LEFT, buff=0.3)
        t19c = MathTex("2 + 2 = 4").next_to(t19a, RIGHT, buff=0.3)
        t19d = Tex("ou").next_to(t19b, LEFT, buff=0.3)
        t19 = VGroup(t19a, t19b, t19c, t19d).shift(DOWN*0.5+RIGHT*0.5)
        
        f5 = Tex("(F)").next_to(t19, LEFT, buff=0.5)
        f5[0].set_color(RED)

        v5 = Tex("(V)").shift(DOWN+RIGHT*2).scale(0.7)
        v5[0].set_color(GREEN)
        
        self.play(FadeOut(v3, f4), TransformMatchingTex(t18, t19))
        self.wait()
        self.play(FadeIn(f5, v5))
        self.wait()
        self.play(FadeOut(t3, ut3, gexc, t19, v4, f5, v5))

#CONDICIONAL
class vid6(Scene):
    def construct(self):        

        #EXPLICAÇÃO
        t1 = Tex("P").shift(LEFT).scale(1.5)
        t2 = Tex("Q").shift(RIGHT).scale(1.5)
        g1 = VGroup(t1, t2)
        
        t3 = Tex("Condicional", color=GREEN).to_corner(UP)
        ut3 = Underline(t3, color=GREEN)
        
        t4 = Tex("se P, então Q")
        t5 = Tex("ou `P implica Q'", color=GRAY).next_to(t4, DOWN)

        t6a = MathTex(r"\rightarrow")
        t6b = Tex("P").next_to(t6a, LEFT, buff=0.3)
        t6c = Tex("Q").next_to(t6a, RIGHT, buff=0.3)
        t6 = VGroup(t6a, t6b ,t6c)

        t8a = MathTex(r"\rightarrow", color=YELLOW)
        t8b = Tex("P").next_to(t8a, LEFT, buff=0.3)
        t8c = Tex("Q").next_to(t8a, RIGHT, buff=0.3)
        t8 = VGroup(t8a, t8b ,t8c)

        t9a = MathTex(r"\Rightarrow", color=YELLOW)
        t9b = Tex("P").next_to(t9a, LEFT, buff=0.3)
        t9c = Tex("Q").next_to(t9a, RIGHT, buff=0.3)
        t9 = VGroup(t9a, t9b ,t9c)

        self.play(LaggedStart(Write(t1), Write(t2), lag_ratio=0.5))
        self.wait()
        self.play(Write(t3), Create(ut3))
        self.wait()
        self.play(TransformMatchingShapes(g1, t4))
        self.wait()
        self.play(FadeIn(t5))
        self.wait()
        self.play(FadeOut(t5))
        self.wait()
        self.play(TransformMatchingShapes(t4, t6))
        self.wait()
        self.play(TransformMatchingShapes(t6, t8))
        self.wait()
        self.play(TransformMatchingShapes(t8, t9))
        self.wait()
        self.play(TransformMatchingShapes(t9, t6))
        self.wait()
        self.play(t6.animate.shift(UP*2))

        t9 = Tex("`Se Mickey é um rato, então Mickey é um animal'")

        self.play(FadeIn(t9))
        self.wait()
        self.play(LaggedStart(FadeOut(t9), t6.animate.shift(DOWN*2), lag_ratio=0.5))
        self.wait()

        f1 = Tex("(F)").next_to(t6, UP)
        f1[0].set_color(RED)

        v1 = Tex("(V)").shift(DOWN*0.5+LEFT).scale(0.7)
        v1[0].set_color(GREEN)

        f2 = Tex("(F)").shift(DOWN*0.5+RIGHT).scale(0.7)
        f2[0].set_color(RED)

        self.play(FadeIn(f1))
        self.wait()
        self.play(LaggedStart(FadeIn(v1), FadeIn(f2), lag_ratio=0.5))
        self.wait()
        self.play(FadeOut(f1, v1, f2))
        self.wait()

        #RECÍPROCA

        t10a = MathTex(r"\not\Rightarrow")
        t10b = Tex("Q").next_to(t10a, LEFT, buff=0.5)
        t10c = MathTex(r"\rightarrow").next_to(t10b, LEFT, buff=0.3)
        t10d = Tex("P").next_to(t10c, LEFT, buff=0.3)

        t10e = Tex("Q").next_to(t10a, RIGHT, buff=0.5)
        t10f = MathTex(r"\rightarrow").next_to(t10e, RIGHT, buff=0.3)
        t10g = Tex("P").next_to(t10f, RIGHT, buff=0.3)

        t10 = VGroup(t10a, t10b, t10c, t10d, t10e, t10f, t10g)

        t10_2 = Tex("(recíproca)", color=YELLOW).next_to(t10, DOWN).shift(RIGHT*1.53)

        t11a = MathTex(r"\rightarrow")
        t11b = Tex("Mickey é um rato").next_to(t11a, LEFT, buff=0.3)
        t11c = Tex("Mickey é um animal").next_to(t11a, RIGHT, buff=0.3)
        t11 = VGroup(t11a, t11b, t11c).move_to((0,0.5,0))

        t12a = MathTex(r"\rightarrow")
        t12b = Tex("Mickey é um animal").next_to(t12a, LEFT, buff=0.3)
        t12c = Tex("Mickey é um rato").next_to(t12a, RIGHT, buff=0.3)
        t12 = VGroup(t12a, t12b, t12c).set_color(RED).move_to((0,-0.5,0))

        t13a = MathTex(r"\rightarrow")
        t13b = Tex("P").next_to(t13a, LEFT, buff=0.3)
        t13c = Tex("Q").next_to(t13a, RIGHT, buff=0.3)
        t13 = VGroup(t13a, t13b ,t13c).shift(UP*0.5)

        t14a = MathTex(r"\rightarrow")
        t14b = Tex("Q").next_to(t14a, LEFT, buff=0.3)
        t14c = Tex("P").next_to(t14a, RIGHT, buff=0.3)
        t14 = VGroup(t14a, t14b ,t14c).next_to(t13, DOWN, buff=0.5)

        g2 = VGroup(t13, t14)

        self.play(TransformMatchingTex(t6, t10))
        self.wait()
        self.play(FadeIn(t10_2), run_time=0.5)
        self.play(FadeOut(t10_2))
        self.wait()
        self.play(t10.animate.shift(UP*2))
        self.wait()
        self.play(FadeIn(t11))
        self.wait()
        self.play(FadeIn(t12))
        self.wait()
        self.play(LaggedStart(FadeOut(t11, t12), TransformMatchingShapes(t10, g2), lag_ratio=0.5))
        self.wait()

#BICONDICIONAL
class vid7(Scene):
    def construct(self):
        
        t3 = Tex("Condicional", color=GREEN).to_corner(UP)
        ut3 = Underline(t3, color=GREEN)
        gt1 = VGroup(t3, ut3)

        t = Tex("Bicondicional", color=GREEN).to_corner(UP).shift(UP*2)
        ut = Underline(t, color=GREEN)
        gt2 = VGroup(t, ut)

        t13a = MathTex(r"\rightarrow")
        t13b = Tex("P").next_to(t13a, LEFT, buff=0.3)
        t13c = Tex("Q").next_to(t13a, RIGHT, buff=0.3)
        t13 = VGroup(t13a, t13b ,t13c).shift(UP*0.5)

        t14a = MathTex(r"\rightarrow")
        t14b = Tex("Q").next_to(t14a, LEFT, buff=0.3)
        t14c = Tex("P").next_to(t14a, RIGHT, buff=0.3)
        t14 = VGroup(t14a, t14b ,t14c).next_to(t13, DOWN, buff=0.5)

        g2 = VGroup(t13, t14)
        
        self.add(t3, ut3, g2)
        self.wait()

        v1 = Tex("(V)").next_to(t13, LEFT, buff=0.5)
        v1[0].set_color(GREEN)

        v2 = Tex("(V)").next_to(t14, LEFT, buff=0.5)
        v2[0].set_color(GREEN)

        gv = VGroup(v1, v2)

        g1 = VGroup(g2, gv)

        t1a = MathTex(r"\leftrightarrow")
        t1b = Tex("P").next_to(t1a, LEFT, buff=0.3)
        t1c = Tex("Q").next_to(t1a, RIGHT, buff=0.3)
        t1 = VGroup(t1a, t1b ,t1c)
        
        v4 = Tex("(V)").shift(DOWN*0.5+LEFT).scale(0.7)
        v4[0].set_color(GREEN)

        v5 = Tex("(V)").shift(DOWN*0.5+RIGHT).scale(0.7)
        v5[0].set_color(GREEN)

        f3 = Tex("(F)").shift(DOWN*0.5+LEFT).scale(0.7)
        f3[0].set_color(RED)

        f4 = Tex("(F)").shift(DOWN*0.5+RIGHT).scale(0.7)
        f4[0].set_color(RED)

        self.play(FadeIn(gv))
        self.wait()
        self.play(LaggedStart(FadeOut(g1), FadeIn(t1), lag_ratio=0.7))
        self.play(LaggedStart(gt1.animate.shift(UP*2), gt2.animate.shift(DOWN*2), lag_ratio=0.7))
        self.wait()
        self.play(FadeIn(v4, v5))
        self.wait()
        self.play(LaggedStart(FadeOut(v4, v5), FadeIn(f3, f4), lag_ratio=0.5))
        self.wait()
        self.play(LaggedStart(FadeOut(f3, f4), t1.animate.shift(UP*2), lag_ratio=0.5))
        self.wait()

        #EXEMPLO BICONDICIONAL

        t2a = MathTex(r"\leftrightarrow")
        t2b = Tex("é par").next_to(t2a, LEFT, buff=0.3)
        t2c = MathTex("x").next_to(t2b, LEFT, buff=0.3)
        t2d = MathTex("x").next_to(t2a, RIGHT, buff=0.3)
        t2e = Tex("é divisível por 2").next_to(t2d, RIGHT, buff=0.3)
        t2 = VGroup(t2a, t2b, t2c, t2d, t2e).move_to((0,0,0))

        a1 = Arrow((-1.5, 0, 0), (1.5, 0, 0), tip_length=0.3, stroke_width=3).shift(UP*0.5+LEFT).scale(0.9)
        a2 = Arrow((1.5, 0, 0), (-1.5, 0, 0), tip_length=0.3, stroke_width=3).shift(DOWN*0.5+LEFT).scale(0.9)

        v3 = Tex("(V)").next_to(t2, LEFT)
        v3[0].set_color(GREEN)

        self.play(FadeIn(t2))
        self.wait()
        self.play(GrowArrow(a1))
        self.wait()
        self.play(FadeOut(a1))
        self.wait()
        self.play(GrowArrow(a2))
        self.wait()
        self.play(FadeOut(a2))
        self.wait()
        self.play(FadeIn(v3))
        self.wait()
        self.play(FadeOut(gt2, t1, t2, v3))

#QUANTIFICADORES
class vid8(Scene):
    def construct(self):
        
        t1 = MathTex(r"x \in \mathbb{Z} , \:\: x ^ 2 = 4").shift(UP)

        t1y = MathTex(r"x \in \mathbb{Z} , \:\: x ^ 2 = 4", color=YELLOW).shift(UP)

        t1q1 = MathTex(r"\exists x \in \mathbb{Z} , \:\: x ^ 2 = 4").move_to(t1.get_right(),aligned_edge = RIGHT)
        t1qy = MathTex(r"\exists",r"x \in \mathbb{Z} , \:\: x ^ 2 = 4").move_to(t1.get_right(),aligned_edge = RIGHT)
        t1qy[0].set_color(YELLOW)

        t2a = MathTex(r"x \in \mathbb{Z} , \:\: x")
        t2b = Tex("é par").next_to(t2a, RIGHT, buff=0.3)
        t2c = MathTex(r"\vee \:\: x").next_to(t2b, RIGHT, buff=0.3)
        t2d = Tex("é ímpar").next_to(t2c, RIGHT, buff=0.3)
        t2 = VGroup(t2a, t2b ,t2c, t2d).move_to((0,-0.5,0))

        t2ya = MathTex(r"x \in \mathbb{Z} , \:\: x")
        t2yb = Tex("é par").next_to(t2ya, RIGHT, buff=0.3)
        t2yc = MathTex(r"\vee \:\: x").next_to(t2yb, RIGHT, buff=0.3)
        t2yd = Tex("é ímpar").next_to(t2yc, RIGHT, buff=0.3)
        t2y = VGroup(t2ya, t2yb ,t2yc, t2yd).move_to((0,-0.5,0)).set_color(YELLOW)

        t2qa = MathTex(r"\forall x \in \mathbb{Z} , \:\: x")
        t2qb = Tex("é par").next_to(t2qa, RIGHT, buff=0.3)
        t2qc = MathTex(r"\vee \:\: x").next_to(t2qb, RIGHT, buff=0.3)
        t2qd = Tex("é ímpar").next_to(t2qc, RIGHT, buff=0.3)
        t2q1 = VGroup(t2qa, t2qb ,t2qc, t2qd).move_to(t2.get_right(),aligned_edge = RIGHT)

        t2qya = MathTex(r"\forall",r"x \in \mathbb{Z} , \:\: x")
        t2qya[0].set_color(YELLOW)
        t2qyb = Tex("é par").next_to(t2qya, RIGHT, buff=0.3)
        t2qyc = MathTex(r"\vee \:\: x").next_to(t2qyb, RIGHT, buff=0.3)
        t2qyd = Tex("é ímpar").next_to(t2qyc, RIGHT, buff=0.3)
        t2qy = VGroup(t2qya, t2qyb ,t2qyc, t2qyd).move_to(t2.get_right(),aligned_edge = RIGHT)

        self.play(FadeIn(t1))
        self.wait()
        self.play(FadeIn(t2))
        self.wait()
        self.play(FadeIn(t1y))
        self.wait()
        self.play(FadeOut(t1y))
        self.wait()
        self.play(FadeIn(t2y))
        self.wait()
        self.play(FadeOut(t2y))
        self.wait()

        #ADD QUANTIFICADORES

        self.play(TransformMatchingShapes(t1, t1qy))
        self.wait()
        self.play(TransformMatchingShapes(t1qy, t1q1))
        self.wait()
        self.play(TransformMatchingTex(t2, t2qy))
        self.wait()
        self.play(TransformMatchingShapes(t2qy, t2q1))
        self.wait()
        
        #TELA QUANTIFICADORES

        t = Tex("Quantificadores", color=GREEN).to_corner(UP)
        ut = Underline(t, color=GREEN)
        gt = VGroup(t, ut)

        a = MathTex(r"\forall", color=WHITE).shift(LEFT*2).scale(1.5)
        at = Tex("`para todo'", color=GRAY).next_to(a, DOWN)

        e = MathTex(r"\exists", color=WHITE).shift(RIGHT*2).scale(1.5)
        et1 = Tex("`existe'", color=GRAY).next_to(e, DOWN)
        ge1 = VGroup(e, et1)

        e2 = MathTex(r"\exists !", color=WHITE).next_to(et1, DOWN, buff=0).scale(1.5)
        et2 = Tex("`existe um único'", color=GRAY).next_to(e2, DOWN)
        ge2 = VGroup(e2, et2)

        ge1_2 = VGroup(ge1, ge2)

        e3 = MathTex(r"\nexists", color=WHITE).next_to(et2, DOWN, buff=0).scale(1.5)
        et3 = Tex("`não existe'", color=GRAY).next_to(e3, DOWN)
        ge3 = VGroup(e3, et3)

        g1 = VGroup(t1q1, t2q1)
        g2 = VGroup(a, e)


        self.play(LaggedStart(FadeOut(g1), FadeIn(g2), lag_ratio=0.5))
        self.wait()
        self.play(Write(t), Create(ut))
        self.wait()
        self.play(FadeIn(at))
        self.wait()
        self.play(FadeIn(et1))
        self.wait()
        self.play(LaggedStart(ge1.animate.shift(UP), FadeIn(ge2), lag_ratio=0.5))
        self.wait()
        self.play(LaggedStart(ge1_2.animate.shift(UP), FadeIn(ge3), lag_ratio=0.5))
        self.wait()
        
        gall = VGroup(a, at, ge1, ge2, ge3)

        #COMBINAR QUANTIFICADORES

        t3 = MathTex(r"\nexists x \in \mathbb{R} , \: \forall y \in \mathbb{R} , \: x > y")
        t4a = Tex("`não existe um número real maior", color=GRAY).next_to(t3, DOWN, buff=0.5)
        t4b = Tex("que todos os outros'", color=GRAY).next_to(t4a, DOWN)
        t4 = VGroup(t4a, t4b)

        self.play(LaggedStart(FadeOut(gall), FadeIn(t3), lag_ratio=0.5))
        self.wait()
        self.play(FadeIn(t4))
        self.wait()
        self.play(FadeOut(t3, t4, gt))

#EXEMPLO DO INÍCIO DO VÍDEO
class vid9(Scene):
    def construct(self):

        ex = MathTex(r"\forall x,y \in \mathbb{R} \: ( x < y \: \Rightarrow \: \exists m \in \mathbb{R}, \: x < m < y)")
        exy1 = MathTex(r"\forall x,y \in \mathbb{R}",r" \: ( x < y \: \Rightarrow \: \exists m \in \mathbb{R}, \: x < m < y)")
        exy1[0].set_color(YELLOW)

        exy2 = MathTex(r"\forall x,y \in \mathbb{R} \: ( ",r"x < y",r" \: \Rightarrow \: \exists m \in \mathbb{R}, \: x < m < y)")
        exy2[1].set_color(YELLOW)

        exy3 = MathTex(r"\forall x,y \in \mathbb{R} \: ( x < y \: ",r"\Rightarrow",r" \: \exists m \in \mathbb{R}, \: x < m < y)")
        exy3[1].set_color(YELLOW)

        exy4 = MathTex(r"\forall x,y \in \mathbb{R} \: ( x < y \: \Rightarrow \: ",r"\exists m \in \mathbb{R}",r", \: x < m < y)")
        exy4[1].set_color(YELLOW)

        exy5 = MathTex(r"\forall x,y \in \mathbb{R} \: ( x < y \: \Rightarrow \: \exists m \in \mathbb{R}, \: ",r"x < m < y",")")
        exy5[1].set_color(YELLOW)

        self.play(Write(ex), run_time=3)
        self.play(FadeIn(exy1))
        self.play(FadeIn(exy2))
        self.remove(exy1)
        self.play(FadeIn(exy3))
        self.remove(exy2)
        self.play(FadeIn(exy4))
        self.remove(exy3)
        self.play(FadeIn(exy5))
        self.remove(exy4)
        self.play(FadeOut(exy5))

        #PROVA DO EXEMPLO

        rl = Arrow((-1,0,0), (1,0,0), tip_length=0.3, stroke_width=4).scale(4)
        r = MathTex(r"\mathbb{R}").next_to(rl, DR, buff=0)
        
        xl = Line((0,1,0), (0,-1,0)).scale(0.2).shift(LEFT*1.5)
        x = MathTex("x").next_to(xl, DOWN)

        yl = Line((0,1,0), (0,-1,0)).scale(0.2).shift(RIGHT*1.5)
        y = MathTex("y").next_to(yl, DOWN)

        ml = Line((0,1,0), (0,-1,0), color=YELLOW).scale(0.2).shift(LEFT*0.5)
        mm = MathTex("m", color=YELLOW).next_to(ml, UP)
        m = VGroup(ml, mm)
        
        t3 = MathTex(r"m",r"= {x + y \over 2}").shift(DOWN*2.3)
        t3[0].set_color(YELLOW)

        self.play(ex.animate.shift(UP*2.5))
        self.wait()
        self.play(LaggedStart(GrowArrow(rl), FadeIn(r), lag_ratio=0.5))
        self.play(Create(xl), Create(yl), Create(ml), run_time=0.5)
        self.play(GrowFromCenter(x), GrowFromCenter(y), GrowFromCenter(mm), run_time=0.5)
        self.wait()
        self.play(m.animate.shift(LEFT*0.8))
        self.play(m.animate.shift(RIGHT*2.5))
        self.play(m.animate.shift(LEFT*1.7))
        self.wait()
        self.play(m.animate.shift(RIGHT*0.5))
        self.play(FadeIn(t3))
        self.wait()

        gall = VGroup(ex, rl, r, xl, x, yl, y, m, t3)
        d=Dot().scale(2)

        self.play(gall.animate.become(d), run_time=3)
        self.play(gall.animate.scale(51))
        self.play(FadeOut(gall))
        self.wait()
        
#INTRODUÇÃO
class vid10(Scene):
    def construct(self):

        t1a = Tex("`Sócrates é mortal, pois Sócrates é um homem")
        t1b = Tex("e todo homem é mortal'").next_to(t1a, DOWN)
        t1 = VGroup(t1a, t1b)

        #self.play(FadeIn(t1))
        #self.wait()
        #self.play(FadeOut(t1))
        
        t2 = Text("ló.gi.ca", weight=BOLD).shift(UP*2+LEFT*2.2).scale(1.3)
        t3 = MathTex("s.f.").scale(1.2).move_to(t2.get_left(),aligned_edge = LEFT).shift(DOWN)
        t4 = Tex("disciplina que estuda o").scale(1.2).move_to(t2.get_left(),aligned_edge = LEFT).shift(DOWN*3)
        t5 = Tex("raciocínio humano").scale(1.2).move_to(t4.get_left(),aligned_edge = LEFT).shift(DOWN*0.6)

        self.play(LaggedStart(FadeIn(t2), FadeIn(t3), lag_ratio=0.6))
        self.play(LaggedStart(Write(t4), Write(t5), lag_ratio=0.5), run_time=2)
        self.wait()
        self.play(FadeOut(t2, t3, t4, t5))
        self.wait()
        
class vid11(Scene):
    def construct(self):        

        t1 = Tex("P").shift(LEFT).scale(1.5)
        t2 = Tex("P").shift(RIGHT).scale(1.5)
        t3 = MathTex(r"\sim").scale(1.5).next_to(t2, LEFT, buff=0.1)
        t4  = Tex("`não-P'", color=GRAY).next_to(t2, DOWN, buff= 0.3).shift(LEFT*0.1)
        g = VGroup(t2, t3, t4)

        self.play(FadeIn(t1))
        self.wait()
        self.play(FadeIn(g))
        self.wait()
