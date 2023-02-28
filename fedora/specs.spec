Name: alfred
Version: 1.0
Release: 1%{?dist}
Summary: Descripción del paquete

License: GPL
URL: URL del proyecto
Source0: %{name}-%{version}.tar.gz

# Paquetes requeridos
Requires: python

%description
Descripción detallada del paquete.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/bin
install -p -m 755 %{SOURCE0} %{buildroot}/usr/bin/alfred.py

%files
/usr/bin/alfred.py

%clean
rm -rf %{buildroot}

%post
echo "El paquete alfred se ha instalado correctamente."

%preun
echo "El paquete alfred se va a desinstalar."

%postun
echo "El paquete alfred se ha desinstalado correctamente."
