Summary:	Graphical song management program for Apple's iPod
Summary(pl):	Graficzny menad¿er utworów muzycznych dla urz±dzeñ Apple iPod
Name:		gtkpod
Version:	0.99.2
Release:	1
Epoch:		0
License:	GPL/LGPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/gtkpod/%{name}-%{version}.tar.gz
# Source0-md5:	73c2767100a64ac9a2ba488909bc8b3b
Source1:	%{name}.desktop
URL:		http://gtkpod.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	flex
BuildRequires:	gettext-devel >= 0.11.0
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	libglade2-devel
BuildRequires:	libid3tag-devel >= 0.15
BuildRequires:	mpeg4ip-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	mount
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Platform independent graphical song management program for Apple's
iPod. It allows you to upload songs and playlists to your iPod.

%description -l pl
Niezale¿ne od platformy graficzny menad¿er utworów muzycznych dla
urz±dzeñ Apple iPod. Pozwala wgrywaæ pliki i listy utworów do iPoda.

%prep
%setup -q
sed -ie 's!/usr/bin/awk!/bin/awk!g' scripts/ldif2vcf.sh

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/gtkpod.desktop

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
cp pixmaps/gtkpod-icon-32x32.png $RPM_BUILD_ROOT%{_pixmapsdir}/gtkpod.png

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
