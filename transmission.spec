Summary:	Lightweight BitTorrent client
Name:		transmission
Version:	2.82
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://download.m0k.org/transmission/files/%{name}-%{version}.tar.xz
# Source0-md5:	a5ef870c0410b12d10449c2d36fa4661
BuildRequires:	gtk+3-devel
BuildRequires:	libevent-devel
BuildRequires:	openssl-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight BitTorrent client with GTK+ interface.

%package common
Summary:	Common files
Group:		Applications

%description common
Common files.

%package cli
Summary:	Transmission CLI client
Group:		Applications
Requires:	%{name}-common = %{version}-%{release}

%description cli
Transmission CLI client.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--with-gtk
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ceb,ckb,eu,mr,pa,ta_LK,tl,ur}

%find_lang %{name}-gtk

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}-gtk.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transmission-gtk
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.*
%{_pixmapsdir}/*.png
%{_mandir}/man1/transmission-gtk.1*

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transmission-cli
%{_mandir}/man1/transmission-cli.1*

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transmission-create
%attr(755,root,root) %{_bindir}/transmission-daemon
%attr(755,root,root) %{_bindir}/transmission-edit
%attr(755,root,root) %{_bindir}/transmission-remote
%attr(755,root,root) %{_bindir}/transmission-show
%{_mandir}/man1/transmission-create.1*
%{_mandir}/man1/transmission-daemon.1*
%{_mandir}/man1/transmission-edit.1*
%{_mandir}/man1/transmission-remote.1*
%{_mandir}/man1/transmission-show.1*

