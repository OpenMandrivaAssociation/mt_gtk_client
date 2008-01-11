%define name mt_gtk_client
%define version 0.1.98
%define release %mkrel 5

Summary: A Maitretarot GTK+ client
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Games/Cards
Source: http://www.nongnu.org/download/maitretarot/%{name}.pkg/%{version}/%{name}-%{version}.tar.bz2
Source10: %name-16.png
Source11: %name-32.png
Source12: %name-48.png
URL: http://www.nongnu.org/maitretarot/
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: cardpics
BuildRequires: glib2-devel gtk+2-devel libmaitretarot-devel libmt_client-devel
BuildRequires: libxml2-devel
Provides: maitretarot-client

%description
mt_gtk_client is a GTK+ client for the Maitretarot server. Maitretarot and its
various clients make a Tarot game

%description -l fr
mt_gtk_client est un client GTK+ pour le serveur Maitretarot. Maitretarot et
ses differents clients constituent un jeu de tarot.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang %name

# mv %buildroot/usr/bin/%{_target_cpu}-mandrake-linux-gnu-%name %buildroot/usr/bin/%name

cp %SOURCE10 $RPM_BUILD_ROOT%_miconsdir/%name.png
cp %SOURCE11 $RPM_BUILD_ROOT%_iconsdir/%name.png
cp %SOURCE12 $RPM_BUILD_ROOT%_liconsdir/%name.png


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Maitretarot
Comment=Maitretarot Client
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;X-MandrivaLinux-MoreApplications-Games-Cards;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%name.png
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%dir %{_datadir}/%name
%dir %{_datadir}/%name/data
%{_datadir}/%name/data/maitretarot.png


