Summary:	GNOME Icon Editor
Name:		gnome-iconedit
Version:	1.0.6
Release:	4
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://www.abdn.ac.uk/~u07ih/gnome-iconedit/%{name}-%{version}.tar.gz
Patch0:		%{name}-gdk_pixbuf.patch
URL:		http://www.abdn.ac.uk/~u07ih/gnome-iconedit/
Buildrequires:	gdk-pixbuf-devel >= 0.7.0
BuildRequires:	libpng >= 1.0.8
Buildrequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
GNOME Icon Editor.

GNOME-Iconedit is a simple icon editor for the GNOME desktop
environment. It is not as powerful as the wonderful GIMP, but has
enough features to create simple icons or cursors.

%prep
%setup -q
%patch -p1

%build
automake
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Graphics

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
%{_pixmapsdir}/gnome-iconedit
