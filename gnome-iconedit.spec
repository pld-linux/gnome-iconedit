Summary:	GNOME Icon Editor
Summary(pl):	Edytor ikon dla GNOME
Name:		gnome-iconedit
Version:	1.0.6
Release:	7
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.abdn.ac.uk/~u07ih/gnome-iconedit/%{name}-%{version}.tar.gz
# Source0-md5:	98c84ce38d93e9f6036074db47ab444b
Patch0:		%{name}-gdk_pixbuf.patch
Patch1:		%{name}-cleanfiles.patch
Patch2:		%{name}-macros.patch
Patch3:		%{name}-acfix.patch
Patch4:		%{name}-c.patch
URL:		http://www.abdn.ac.uk/~u07ih/gnome-iconedit/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel >= 0.7.0
BuildRequires:	gettext-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
GNOME-Iconedit is a simple icon editor for the GNOME desktop
environment. It is not as powerful as the wonderful GIMP, but has
enough features to create simple icons or cursors.

%description -l pl
GNOME-Iconedit to prosty edytor ikon dla ¶rodowiska GNOME. Nie jest
tak potê¿ny jak wspania³y GIMP, ale mo¿e wystarczaj±co du¿o by tworzyæ
proste ikony lub kursory.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Graphics

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_datadir}/idl/*.idl
%{_pixmapsdir}/gnome-iconedit
%{_applnkdir}/Graphics/*
