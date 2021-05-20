#!/usr/bin/env bash
pandoc -f gfm -t latex -o _coursework_pandoc.tex <(cat intro.md tech.md math.md real.md end.md l_list.md)
lualatex coursework.tex
