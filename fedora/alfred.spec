Name: alfred
Version: 1.3
Release: 3%{?dist}
Summary: Personal assistant for the console

License: GPL
URL: https://github.com/maximofn/alfred
Source0: %{name}-%{version}.tar.gz

# Paquetes requeridos
Requires: python3, python3-pip, python3-setuptools

%description
A personal assistant for the console that uses chat gpt. You need an API KEY of openai for use Alfred

%prep
%autosetup

%build
cp %{SOURCE0} alfred.py
%define debug_package %{nil}

%install
mkdir -p %{buildroot}/usr/bin
install -p -m 755 alfred.py %{buildroot}/usr/bin/alfred.py

%files
/usr/bin/alfred.py

%clean
rm -rf %{buildroot}

%post
echo "Installing Ubuntu dependencies..."
# apt-get update && apt-get install -y python3 python3-pip python3-setuptools python3-wheel python3-venv python3-dev python3-pip python3-setuptools python3-wheel python3-venv python3-dev git
# Instalar dependencias de Python
echo "Installing Python dependencies..."
/usr/bin/python3 -m pip install halo
/usr/bin/python3 -m pip install --upgrade openai
echo "The alfred package is going to be installed."
if [ -d "/usr/src/alfred" ]; then
    rm -r /usr/src/alfred
    echo "Removing /usr/share/alfred..."
fi
cd /usr/src
git clone -b branch_v1.3 https://github.com/maximofn/alfred.git
cd /usr/src/alfred
find . -depth -not -name '*.py' -delete
echo "Creating symbolic link to /usr/bin/alfred..."
echo 'alias alfred="/usr/src/alfred/alfred.py"' >> ~/.bashrc
echo "The alfred package has been successfully installed."

%preun
echo "The alfred package is going to be uninstalled."

%postun
echo "The alfred package has been successfully uninstalled.."
