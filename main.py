#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class ManimScene(Scene):
    def construct(self):
        title = TextMobject("Welcome")
        boiz = TexMobject("\\mathbb{BOIZ}")
        subtitle = TextMobject("and")
        lads = TexMobject("\\mathbb{LADS}")
        group1 = VGroup(title, boiz, subtitle, lads).arrange(DOWN)
        self.play(
            FadeInFrom(title, UP),
            FadeInFrom(boiz, LEFT),
            FadeInFrom(subtitle, DOWN),
            FadeInFrom(lads, RIGHT)
        )
        self.wait()
        title2 = TextMobject("As well as")
        lads2 = TexMobject("\\mathbb{LADS}")
        subtitle2 = TextMobject("and")
        boiz2 = TexMobject("\\mathbb{BOIZ}")
        group2 = VGroup(title2, lads2, subtitle2, boiz2).arrange(DOWN)
        self.play(
            Transform(group1, group2)
        )
        self.wait()
        self.play(
            FadeOutAndShift(group1)
        )
        self.wait()
