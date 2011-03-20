Summary:	GUI frontend for Cuneiform OCR
Name:		cuneiform-qt
Version:	0.1.2
Release:	1%{?dist}

License:	GPLv3+
Group:		Applications/Multimedia
URL:		http://www.altlinux.org/Cuneiform-Qt
Source0:	http://downloads.sourceforge.net/project/cuneiform-qt/cuneiform-qt/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	ImageMagick-devel
BuildRequires:	qt-devel >= 4.3.0

Requires:	cuneiform


%description
This application is GUI frontend for Cuneiform (OCR system originally 
developed and open sourced by Cognitive technologies). It allow
to open scanned image, view this one in preview pane, recornize text via
Cuneiform and save result in HTML file.


%prep
%setup -q


%build
PREFIX=%{_prefix} qmake-qt4 "QMAKE_CFLAGS+=%{optflags}" "QMAKE_CXXFLAGS+=%{optflags}" %{name}.pro
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS README TODO
%{_bindir}/%{name}
%{_datadir}/apps/%{name}/*.qm
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/cuneiform-qt.png


%changelog
* Tue May  5 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 0.1.2-1
- initial build for Fedora
