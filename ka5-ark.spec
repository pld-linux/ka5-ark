%define		kdeappsver	21.12.0
%define		qtver		5.9.0
%define		kaname		ark
Summary:	Ark
Name:		ka5-%{kaname}
Version:	21.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	e7b7ba1c865777c440bd7a5375ca3a16
Patch0:		no-programs.patch
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-karchive-devel >= 5.38.0
BuildRequires:	kf5-kconfig-devel >= 5.38.0
BuildRequires:	kf5-kcrash-devel >= 5.38.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.38.0
BuildRequires:	kf5-kdoctools-devel >= 5.38.0
BuildRequires:	kf5-ki18n-devel >= 5.38.0
BuildRequires:	kf5-kiconthemes-devel >= 5.38.0
BuildRequires:	kf5-kio-devel >= 5.38.0
BuildRequires:	kf5-kitemmodels-devel >= 5.38.0
BuildRequires:	kf5-kparts-devel >= 5.38.0
BuildRequires:	kf5-kpty-devel >= 5.38.0
BuildRequires:	kf5-kservice-devel >= 5.38.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.38.0
BuildRequires:	libarchive-devel >= 3.2.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
Suggests:	lrzip
Suggests:	lzop
Suggests:	rar
Suggests:	unrar
Suggests:	zstd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ark is a graphical file compression/decompression utility with support
for multiple formats, including tar, gzip, bzip2, rar and zip, as well
as CD-ROM images. Ark can be used to browse, extract, create, and
modify archives.

%description -l pl.UTF-8
Ark jest graficznym programem użytkowym do kompresji/dekompresji
plików w wielu formatach, np. tar, gzip, bzip2, rar i zip, jak i
obrazów CD-ROMów. Ark może być wykorzystywany do przeglądania,
rozpakowywania, tworzenia i modyfikowania archiwów.

%prep
%setup -q -n %{kaname}-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ark
%ghost %{_libdir}/libkerfuffle.so.21
%attr(755,root,root) %{_libdir}/libkerfuffle.so.*.*.*
%dir %{_libdir}/qt5/plugins/kerfuffle
%{_libdir}/qt5/plugins/kerfuffle/kerfuffle_cli7z.so
%{_libdir}/qt5/plugins/kerfuffle/kerfuffle_clirar.so
%{_libdir}/qt5/plugins/kerfuffle/kerfuffle_cliunarchiver.so
%{_libdir}/qt5/plugins/kerfuffle/kerfuffle_clizip.so
%{_libdir}/qt5/plugins/kerfuffle/kerfuffle_libarchive.so
%{_libdir}/qt5/plugins/kerfuffle/kerfuffle_libarchive_readonly.so
%{_libdir}/qt5/plugins/kerfuffle/kerfuffle_libbz2.so
%{_libdir}/qt5/plugins/kerfuffle/kerfuffle_libgz.so
%{_libdir}/qt5/plugins/kerfuffle/kerfuffle_libxz.so
%{_libdir}/qt5/plugins/kerfuffle/kerfuffle_libzip.so
%{_libdir}/qt5/plugins/kf5/kfileitemaction/compressfileitemaction.so
%{_libdir}/qt5/plugins/kf5/kfileitemaction/extractfileitemaction.so
%{_libdir}/qt5/plugins/kf5/kio_dnd/extracthere.so
%{_desktopdir}/org.kde.ark.desktop
%{_datadir}/config.kcfg/ark.kcfg
%{_iconsdir}/hicolor/128x128/apps/ark.png
%{_iconsdir}/hicolor/48x48/apps/ark.png
%{_iconsdir}/hicolor/64x64/apps/ark.png
%{_iconsdir}/hicolor/scalable/apps/ark.svgz
%{_datadir}/kservices5/ark_part.desktop
%{_datadir}/kservicetypes5/kerfufflePlugin.desktop
%{_datadir}/metainfo/org.kde.ark.appdata.xml
%lang(ca) %{_mandir}/ca/man1/ark.1*
%lang(de) %{_mandir}/de/man1/ark.1*
%lang(es) %{_mandir}/es/man1/ark.1*
%lang(fr) %{_mandir}/fr/man1/ark.1*
%lang(gl) %{_mandir}/gl/man1/ark.1*
%lang(it) %{_mandir}/it/man1/ark.1*
%lang(C) %{_mandir}/man1/ark.1*
%lang(nl) %{_mandir}/nl/man1/ark.1*
%lang(pt) %{_mandir}/pt/man1/ark.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/ark.1*
%lang(sr) %{_mandir}/sr/man1/ark.1*
%lang(sv) %{_mandir}/sv/man1/ark.1*
%lang(uk) %{_mandir}/uk/man1/ark.1*
%{_datadir}/qlogging-categories5/ark.categories
%{_libdir}/qt5/plugins/kerfuffle/kerfuffle_libzstd.so
%{_libdir}/qt5/plugins/kf5/parts/arkpart.so
