# TODO
# - Check for MP4 Headers: mp4v2/mp4v2.h: mp4v2-devel
Summary:	Graphical song management program for Apple's iPod
Summary(pl.UTF-8):	Graficzny menadżer utworów muzycznych dla urządzeń Apple iPod
Name:		gtkpod
Version:	2.1.0
Release:	2
License:	GPL/LGPL
Group:		X11/Applications/Multimedia
Source0:	http://downloads.sourceforge.net/gtkpod/%{name}-%{version}.tar.gz
# Source0-md5:	8e01f7cf2db1a421140eab561aee26d7
Patch1:		desktop.patch
URL:		http://www.gtkpod.org/
BuildRequires:	flex
BuildRequires:	gdl-devel >= 3.0.0
BuildRequires:	gettext-devel >= 0.11.0
BuildRequires:	glib2-devel >= 1:2.28.5
BuildRequires:	gtk+3-devel >= 3.0.11
BuildRequires:	intltool
BuildRequires:	libanjuta-devel >= 1:3.0
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomecanvas-devel
BuildRequires:	libgpod-devel >= 0.4.0
BuildRequires:	libid3tag-devel >= 0.15
BuildRequires:	libxml2-devel >= 2.7.7
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	sed >= 4.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	/sbin/ldconfig
# M4A -> MP3 conversion support
Requires:	mount
Suggests:	faad2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Platform independent graphical song management program for Apple's
iPod. It allows you to upload songs and playlists to your iPod.

%description -l pl.UTF-8
Niezależne od platformy graficzny menadżer utworów muzycznych dla
urządzeń Apple iPod. Pozwala wgrywać pliki i listy utworów do iPoda.

%prep
%setup -q
%patch1 -p1
%{__sed} -i -e 's!/usr/bin/awk!/bin/awk!g' scripts/ldif2vcf.sh

%build
%configure \
	FAAD=yes \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/gtkpod.svg

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtkpod/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/gtkpod/doc

# no -devel
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}
%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgtkpod.so

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor
%glib_compile_schemas

%postun
/sbin/ldconfig
%update_icon_cache hicolor
if [ "$1" = "0" ]; then
	%glib_compile_schemas
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODOandBUGS.txt
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/libgtkpod.so.*.*.*
%ghost %{_libdir}/libgtkpod.so.1
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/%{name}
%{_datadir}/gtkpod/data
%{_datadir}/gtkpod/icons
%dir %{_datadir}/gtkpod/scripts/convert-2m4a.sh
%attr(755,root,root) %{_datadir}/gtkpod/scripts/*
%{_datadir}/glib-2.0/schemas/org.gtkpod.gschema.xml
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%dir %{_libdir}/gtkpod
%attr(755,root,root) %{_libdir}/gtkpod/lib*.so
%{_libdir}/gtkpod/*.plugin
