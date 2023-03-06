#!/usr/bin/env python3

PACKAGE = "alfred"
VERSION = 1
RELEASE = 3
ARCHITECTURE = "all"
SUMARY = "Personal assistant for the console"
DESCRIPTION = "A personal assistant for the console that uses chat gpt. You need an API KEY of openai for use Alfred"
MAINTAINER = "MaximoFN"
EMAIL = "maximofn@gmail.com"
DEPENDENCIES = "python3, python3-pip, python3-setuptools"
LICENSE = "GPL"
URL = f"https://github.com/maximofn/{PACKAGE}"

# DEBIAN

## alfred.install
text = "usr/bin/{PACKAGE}}/*\n"
with open("debian/alfred.install", "w") as f:
    f.write(text)

## control
text = f"Package: {PACKAGE}\n\
Version: {VERSION}.{RELEASE}\n\
Architecture: {ARCHITECTURE}\n\
Maintainer: {MAINTAINER} <{EMAIL}>\n\
Description: {SUMARY}\n\
 {DESCRIPTION}\n\
Depends: {DEPENDENCIES}\n"
with open("debian/control", "w") as f:
    f.write(text)

## postinst
text = f"{'#'}!/bin/sh\n\
\n\
set -e\n\
\n\
# Instalar dependencias de Ubuntu\n\
echo \"Installing Ubuntu dependencies...\"\n\
# apt-get update {'&&'} apt-get install -y python3 python3-pip python3-setuptools python3-wheel python3-venv python3-dev python3-pip python3-setuptools python3-wheel python3-venv python3-dev git\n\
\n\
# Instalar dependencias de Python\n\
echo \"Installing Python dependencies...\"\n\
/usr/bin/python3 -m pip install halo\n\
/usr/bin/python3 -m pip install --upgrade openai\n\
\n\
# Copiar archivos fuentes a /usr/share/{PACKAGE}\n\
echo \"Copying source files to /usr/share/{PACKAGE}...\"\n\
if [ -d \"/usr/src/{PACKAGE}\" ]; then\n\
    echo \"Removing /usr/share/{PACKAGE}...\"\n\
    rm -r /usr/src/{PACKAGE}\n\
fi\n\
cd /usr/src\n\
git clone -b branch_v{VERSION}.{RELEASE} {URL}.git\n\
cd /usr/src/{PACKAGE}\n\
find . -depth -not -name '*.py' -delete\n\
\n\
# Crear enlace simbólico para que los usuarios puedan ejecutar el programa escribiendo '{PACKAGE}'\n\
echo \"Creating symbolic link to /usr/bin/{PACKAGE}...\"\n\
USER=$SUDO_USER\n\
echo 'alias {PACKAGE}=\"/usr/src/{PACKAGE}/{PACKAGE}.py\"' >> /home/$USER/.bashrc"
with open("debian/postinst", "w") as f:
    f.write(text)

# FEDORA

## alfred.spec
text = f"Name: {PACKAGE}\n\
Version: {VERSION}.{RELEASE}\n\
Release: {RELEASE}%{'{'}?dist{'}'}\n\
Summary: {SUMARY}\n\
\n\
License: {LICENSE}\n\
URL: {URL}\n\
Source0: %{'{'}name{'}'}-%{'{'}version{'}'}.tar.gz\n\
\n\
# Paquetes requeridos\n\
Requires: {DEPENDENCIES}\n\
\n\
%description\n\
{DESCRIPTION}\n\
\n\
%prep\n\
%autosetup\n\
\n\
%build\n\
cp %{'{'}SOURCE0{'}'} {PACKAGE}.py\n\
%define debug_package %{'{'}nil{'}'}\n\
\n\
%install\n\
mkdir -p %{'{'}buildroot{'}'}/usr/bin\n\
install -p -m 755 {PACKAGE}.py %{'{'}buildroot{'}'}/usr/bin/{PACKAGE}.py\n\
\n\
%files\n\
/usr/bin/{PACKAGE}.py\n\
\n\
%clean\n\
rm -rf %{'{'}buildroot{'}'}\n\
\n\
%post\n\
echo \"Installing Ubuntu dependencies...\"\n\
# apt-get update && apt-get install -y python3 python3-pip python3-setuptools python3-wheel python3-venv python3-dev python3-pip python3-setuptools python3-wheel python3-venv python3-dev git\n\
# Instalar dependencias de Python\n\
echo \"Installing Python dependencies...\"\n\
/usr/bin/python3 -m pip install halo\n\
/usr/bin/python3 -m pip install --upgrade openai\n\
echo \"The {PACKAGE} package is going to be installed.\"\n\
if [ -d \"/usr/src/{PACKAGE}\" ]; then\n\
    rm -r /usr/src/{PACKAGE}\n\
    echo \"Removing /usr/share/alfred...\"\n\
fi\n\
cd /usr/src\n\
git clone -b branch_v{VERSION}.{RELEASE} {URL}.git\n\
cd /usr/src/alfred\n\
find . -depth -not -name '*.py' -delete\n\
echo \"Creating symbolic link to /usr/bin/{PACKAGE}...\"\n\
echo 'alias alfred=\"/usr/src/{PACKAGE}/{PACKAGE}.py\"' >> ~/.bashrc\n\
echo \"The alfred package has been successfully installed.\"\n\
\n\
%preun\n\
echo \"The {PACKAGE} package is going to be uninstalled.\"\n\
\n\
%postun\n\
echo \"The {PACKAGE} package has been successfully uninstalled..\"\n\
"
with open("fedora/alfred.spec", "w") as f:
    f.write(text)

# DOCKERFILES

# Dockerfile.ubuntu_build
text = f"FROM ubuntu:20.04\n\
\n\
WORKDIR /home\n\
\n\
COPY {PACKAGE}/{PACKAGE}.py .\n\
COPY {PACKAGE}_build/debian/control .\n\
COPY {PACKAGE}_build/debian/postinst .\n\
COPY {PACKAGE}_build/debian/{PACKAGE}.install .\n\
\n\
RUN mkdir /usr/bin/{PACKAGE}\n\
RUN mkdir /usr/bin/{PACKAGE}/DEBIAN\n\
RUN mv {PACKAGE}.py /usr/bin/{PACKAGE}/{PACKAGE}.py\n\
RUN mv control /usr/bin/{PACKAGE}/DEBIAN/\n\
RUN mv postinst /usr/bin/{PACKAGE}/DEBIAN/\n\
RUN mv {PACKAGE}.install /usr/bin/{PACKAGE}/DEBIAN/\n\
RUN chmod +x /usr/bin/{PACKAGE}/{PACKAGE}.py /usr/bin/{PACKAGE}/DEBIAN/control /usr/bin/{PACKAGE}/DEBIAN/postinst /usr/bin/{PACKAGE}/DEBIAN/{PACKAGE}.install\n\
\n\
RUN cd /usr/bin/{PACKAGE} && dpkg-deb --build . /home/{PACKAGE}v{VERSION}_{RELEASE}.deb && chmod +x /home/{PACKAGE}v{VERSION}_{RELEASE}.deb"
with open("docker/Dockerfile.ubuntu_build", "w") as f:
    f.write(text)

# Dockerfile.ubuntu_test1
text = f"FROM ubuntu:20.04\n\
\n\
WORKDIR /home\n\
\n\
RUN apt-get update && apt-get install -y python3 python3-pip git && rm -rf /var/lib/apt/lists/*\n\
\n\
COPY {PACKAGE}_build/debian/{PACKAGE}v{VERSION}_{RELEASE}.deb .\n\
\n\
RUN chmod +x {PACKAGE}v{VERSION}_{RELEASE}.deb\n\
RUN dpkg -i {PACKAGE}v{VERSION}_{RELEASE}.deb\n\
RUN rm {PACKAGE}v{VERSION}_{RELEASE}.deb"
with open("docker/Dockerfile.ubuntu_test1", "w") as f:
    f.write(text)

# Dockerfile.ubuntu_test2
text = f"FROM ubuntu:20.04\n\
\n\
WORKDIR /home\n\
\n\
RUN apt-get update && apt-get install -y python3 python3-pip git && rm -rf /var/lib/apt/lists/*\n\
\n\
COPY {PACKAGE}_build/debian/{PACKAGE}v{VERSION}_{RELEASE}.deb .\n\
\n\
RUN /usr/bin/python3 -m pip install halo\n\
RUN /usr/bin/python3 -m pip install --upgrade openai\n\
\n\
RUN chmod +x {PACKAGE}v{VERSION}_{RELEASE}.deb\n\
RUN dpkg -i {PACKAGE}v{VERSION}_{RELEASE}.deb\n\
RUN rm {PACKAGE}v{VERSION}_{RELEASE}.deb"
with open("docker/Dockerfile.ubuntu_test2", "w") as f:
    f.write(text)

# Dockerfile.ubuntu_test3
text = f"FROM ubuntu:20.04\n\
\n\
WORKDIR /home\n\
\n\
RUN apt-get update && apt-get install -y python3 python3-pip git && rm -rf /var/lib/apt/lists/*\n\
\n\
COPY {PACKAGE}_build/debian/{PACKAGE}v{VERSION}_{RELEASE}.deb .\n\
\n\
RUN cd /usr/src\n\
RUN git clone {URL}.git /usr/src\n\
\n\
RUN chmod +x {PACKAGE}v{VERSION}_{RELEASE}.deb\n\
RUN dpkg -i {PACKAGE}v{VERSION}_{RELEASE}.deb\n\
RUN rm {PACKAGE}v{VERSION}_{RELEASE}.deb"
with open("docker/Dockerfile.ubuntu_test3", "w") as f:
    f.write(text)

# Dockerfile.fedora_build
text = f"FROM fedora:36\n\
\n\
RUN dnf update -y && dnf install -y rpm-build git && dnf clean all\n\
\n\
RUN mkdir -p /root/rpmbuild/{'{'}BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS{'}'}\n\
COPY {PACKAGE}/{PACKAGE}.py /root/rpmbuild/SOURCES/\n\
RUN mkdir /tmp/{PACKAGE}\n\
RUN mkdir /tmp/{PACKAGE}/{PACKAGE}-{VERSION}.{RELEASE}\n\
COPY {PACKAGE}/{PACKAGE}.py /tmp/{PACKAGE}/{PACKAGE}-{VERSION}.{RELEASE}\n\
RUN cd /tmp/{PACKAGE} && tar -czvf /root/rpmbuild/SOURCES/{PACKAGE}-{VERSION}.{RELEASE}.tar.gz {PACKAGE}-{VERSION}.{RELEASE}\n\
RUN chmod 777 /root/rpmbuild/SOURCES/{PACKAGE}-{VERSION}.{RELEASE}.tar.gz\n\
COPY {PACKAGE}_build/fedora/{PACKAGE}.spec /root/rpmbuild/SPECS/\n\
\n\
RUN rpmbuild -ba /root/rpmbuild/SPECS/{PACKAGE}.spec && chmod +x /root/rpmbuild/RPMS/x86_64/{PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm"
with open("docker/Dockerfile.fedora_build", "w") as f:
    f.write(text)

# Dockerfile.fedora_test1
text = f"FROM fedora:36\n\
\n\
WORKDIR /home\n\
\n\
RUN dnf update -y && dnf install -y python3 python3-pip git && dnf clean all\n\
\n\
COPY {PACKAGE}_build/fedora/{PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm .\n\
\n\
RUN chmod +x {PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm \n\
RUN rpm -i {PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm\n\
RUN rm {PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm"
with open("docker/Dockerfile.fedora_test1", "w") as f:
    f.write(text)

# Dockerfile.fedora_test2
text = f"FROM fedora:36\n\
\n\
WORKDIR /home\n\
\n\
RUN dnf update -y && dnf install -y python3 python3-pip git && dnf clean all\n\
\n\
COPY {PACKAGE}_build/fedora/{PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm .\n\
\n\
RUN /usr/bin/python3 -m pip install halo\n\
RUN /usr/bin/python3 -m pip install --upgrade openai\n\
\n\
RUN chmod +x {PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm \n\
RUN rpm -i {PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm\n\
RUN rm {PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm"
with open("docker/Dockerfile.fedora_test2", "w") as f:
    f.write(text)

# Dockerfile.fedora_test3
text = f"FROM fedora:36\n\
\n\
WORKDIR /home\n\
\n\
RUN dnf update -y && dnf install -y python3 python3-pip git && dnf clean all\n\
\n\
COPY {PACKAGE}_build/fedora/{PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm .\n\
\n\
RUN cd /usr/src && git clone {URL}.git\n\
\n\
RUN chmod +x {PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm \n\
RUN rpm -i {PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm\n\
RUN rm {PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm"
with open("docker/Dockerfile.fedora_test3", "w") as f:
    f.write(text)

# SCRIPTS

## BUILD
text = f"{'#'}!/bin/bash\n\
\n\
# Build ubuntu 20.04 docker image\n\
rm debian/{PACKAGE}v{VERSION}_{RELEASE}.deb\n\
docker build -f docker/Dockerfile.ubuntu_build -t maximofn/ubuntu_20_04_build:0.0.1 ../\n\
docker run -it --rm -v ./debian/:/mnt maximofn/ubuntu_20_04_build:0.0.1 cp /home/{PACKAGE}v{VERSION}_{RELEASE}.deb /mnt\n\
docker image rm maximofn/ubuntu_20_04_build:0.0.1\n\
\n\
# Build fedora 36 docker image\n\
rm fedora/{PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm\n\
docker build -f docker/Dockerfile.fedora_build -t maximofn/fedora36_build:0.0.1 ../\n\
docker run -it --rm -v ./fedora/:/mnt maximofn/fedora36_build:0.0.1 cp /root/rpmbuild/RPMS/x86_64/{PACKAGE}-{VERSION}.{RELEASE}-{RELEASE}.fc36.x86_64.rpm /mnt\n\
docker image rm maximofn/fedora36_build:0.0.1"
with open("build_dockers.sh", "w") as f:
    f.write(text)