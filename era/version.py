# Copyright (c) 2023 BMO Soluciones
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Definición unica de la version de la aplicación."""

# ---------------------------------------------------------------------------------------
# Libreria estandar
# ---------------------------------------------------------------------------------------
from datetime import datetime

# ---------------------------------------------------------------------------------------
# Librerias de terceros
# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
# Recursos locales
# ---------------------------------------------------------------------------------------


# <--------------------------------------------------------------------------> #
# Basic info:
APPNAME = "ERA - Event Registration App"
APPAUTHOR = "BMO Soluciones, S.A."

# <--------------------------------------------------------------------------> #
# SemVer (https://semver.org)
MAYOR = "0"
MENOR = "0"
PATCH = "1"

# <--------------------------------------------------------------------------> #
# Pre release data.
PRERELEASE = "a1"
REVISION = datetime.today().strftime("%Y%m%d")

# <--------------------------------------------------------------------------> #
# Release string
# Refences:
#  - https://peps.python.org/pep-0440/
# 0.0.1a1.dev20231001
if PRERELEASE:
    VERSION = MAYOR + "." + MENOR + "." + PATCH + PRERELEASE + ".dev" + REVISION
else:
    VERSION = MAYOR + "." + MENOR + "." + PATCH
