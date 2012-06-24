Summary:	Graphical song management program for Apple's iPod
Summary(pl):	Graficzny menad�er utworow muzycznych dla urz�dze� Apple iPod
Name:		gtkpod
Version:	0.85.0
Release:	0.1
Epoch:		0
License:	GPL/LGPL
Group:		Applications/Communications
Source0:	http://osdn.dl.sourceforge.net/gtkpod/%{name}-%{version}.tar.gz
# Source0-md5:	ca870acf255dd240a02d387485940c3c
URL:		http://gtkpod.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel >= 0.11.0
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	pkgconfig
BuildRequires:	flex
BuildRequires:	libid3tag-devel
BuildRequires:	bind-libs
BuildRequires:	mpeg4ip-devel
Requires:	mpeg4ip-libs
Requires:	libid3tag
Requires:	mount
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Platform independent graphical song management program for Apple's
iPod. It allows you to upload songs and playlists to your iPod.

%description -l pl
Niezale�ne od platformy graficzny menad�er utwor�w muzycznych dla
urz�dze� Apple iPod. Pozwala wgrywa� pliki i listy utwor�w do iPod'a.

%prep
%setup -q

%build
#%%{__gettextize}
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

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODOandBUGS.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}
