Summary:	Graphical song management program for Apple's iPod
Summary(pl.UTF-8):	Graficzny menadżer utworów muzycznych dla urządzeń Apple iPod
Name:		gtkpod
Version:	1.0.0
Release:	1
License:	GPL/LGPL
Group:		X11/Applications/Multimedia
Source0:	http://downloads.sourceforge.net/gtkpod/%{name}-%{version}.tar.gz
# Source0-md5:	cadd402dcd1cfbedda0357bf24965a7c
Patch0:		%{name}-unk208.patch
Patch1:		desktop.patch
URL:		http://gtkpod.sourceforge.net/
BuildRequires:	flex
BuildRequires:	gettext-devel >= 0.11.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomecanvas-devel
BuildRequires:	libgpod-devel >= 0.4.0
BuildRequires:	libid3tag-devel >= 0.15
BuildRequires:	mpeg4ip-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	sed >= 4.0
Requires:	hicolor-icon-theme
Requires:	mount
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Platform independent graphical song management program for Apple's
iPod. It allows you to upload songs and playlists to your iPod.

%description -l pl.UTF-8
Niezależne od platformy graficzny menadżer utworów muzycznych dla
urządzeń Apple iPod. Pozwala wgrywać pliki i listy utworów do iPoda.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -ie 's!/usr/bin/awk!/bin/awk!g' scripts/ldif2vcf.sh

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/gtkpod.svg

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODOandBUGS.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
