%define		_snap	20060804
Summary:	Graphical song management program for Apple's iPod
Summary(pl.UTF-8):	Graficzny menadżer utworów muzycznych dla urządzeń Apple iPod
Name:		gtkpod
Version:	0.99.14
Release:	0
Epoch:		0
License:	GPL/LGPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/gtkpod/%{name}-%{version}.tar.gz
# Source0-md5:	f7948eceb955b302f4c47da4c0e1ec12
Source1:	%{name}.desktop
Patch0:		%{name}-unk208.patch
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
BuildRequires:	sed >= 4.0
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
sed -ie 's!/usr/bin/awk!/bin/awk!g' scripts/ldif2vcf.sh

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/gtkpod.desktop

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
cp data/icons/32x32/gtkpod.png $RPM_BUILD_ROOT%{_pixmapsdir}/gtkpod.png

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODOandBUGS.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/gtkpod.desktop
%{_pixmapsdir}/gtkpod.png
