#!/usr/bin/env bash
pandoc -f gfm+tex_math_dollars -t latex -o _coursework_pandoc.tex <(cat intro.md tech.md math.md real.md end.md l_list.md)
lualatex coursework.tex
