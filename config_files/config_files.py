PACKAGE = "alfred"
VERSION = 1.0
RELEASE = 1
ARCHITECTURE = "all"
SUMARY = "Personal assistant for the console"
DESCRIPTION = "Alfred is a personal assistant for the console that uses chat gpt. You need an API KEY of openai for use Alfred"
DESCRIPTION = "A personal assistant for the console that uses chat gpt. You need an API KEY of openai for use Alfred"
MAINTAINER = "MaximoFN"
EMAIL = "maximofn@gmail.com"
DEPENDENCIES = "python3, python3-pip, python3-setuptools"
LICENSE = "GPL"
URL = "maximofn.com/alfred"


# Create the file debian/control
with open("../debian/control", "w") as f:
    f.write(
f"Package: {PACKAGE}\n\
Version: {VERSION}\n\
Architecture: {ARCHITECTURE}\n\
Maintainer: {MAINTAINER} <{EMAIL}>\n\
Description: {SUMARY}\n\
 {DESCRIPTION}\n\
Depends: {DEPENDENCIES}\n")

# Create the file fedora/alfred.spec
# with open("../fedora/alfred.spec", "w") as f:
#     f.write(
# f"Name: {PACKAGE}\n\
# Version: {VERSION}\n\
# Release: {RELEASE}\n\
# Summary: {SUMARY}\n\
# License: {LICENSE}\n\
# URL: {URL}\n\
# Source0: %'{'name'}'-%'{'version'}¡.tar.gz\n\
# BuildArch: {ARCHITECTURE}\n\
# BuildRequires: {DEPENDENCIES}\n\
# \n\
# %description\n\
# {DESCRIPTION}\n\
# \n\
# %prep\n\
# %setup -q\n\
# \n\
# %build\n\
# \n\
# %install\n\
# rm -rf %'{'buildroot'}'\n\
# mkdir -p %{buildroot}/usr/bin\n\
# mkdir -p %{buildroot}/usr/share/alfred\n\
# mkdir -p %{buildroot}/usr/share/applications\n\
# mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps\n\
# \n\
# cp -r ../alfred %{buildroot}/usr/share/alfred\n\
# cp -r ../alfred.desktop %{buildroot}/usr/share/applications\n\
# cp -r ../alfred.png %{buildroot}/usr/share/icons/hicolor/256x256/apps\n\
# \n\
# %files\n\
# %defattr(-,root,root,-)\n\
# /usr/share/alfred\n\
# /usr/share/applications/alfred.desktop\n\
# /usr/share/icons/hicolor/256x256/apps/alfred.png\n\
# \n\
# %changelog\n\
# * {VERSION} {RELEASE} {MAINTAINER} <{EMAIL}> - {VERSION}-{RELEASE}\n\
# - Initial version")
