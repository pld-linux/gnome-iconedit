Summary:	GNOME Icon Editor
Name:		gnome-iconedit
Version:	1.0.6
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source:		http://www.abdn.ac.uk/~u07ih/gnome-iconedit/%{name}-%{version}.tar.gz
Patch:		gnome-iconedit-applnk.patch
URL:		http://www.abdn.ac.uk/~u07ih/gnome-iconedit/
Buildrequires:	gdk-pixbuf-devel
Buildrequires:	libpng-devel
Buildrequires:	gettext-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_applnkdir	%{_datadir}/applnk
%define		_sysconfdir	/etc/X11/GNOME

%description
GNOME Icon Editor.

GNOME-Iconedit is a simple icon editor for the GNOME desktop environment. It
is not as powerful as the wonderful GIMP, but has enough features to create
simple icons or cursors.

%prep
%setup -q
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
automake
gettextize --copy --force
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_datadir}/gnome/help/gnome-iconedit
%{_applnkdir}/Graphics/*
%{_datadir}/pixmaps/gnome-iconedit
