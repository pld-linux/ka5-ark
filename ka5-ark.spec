%define		kdeappsver	18.04.0
%define		qtver		5.3.2
%define		kaname		ark
Summary:	Ark
Name:		ka5-%{kaname}
Version:	18.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	08c0d389041ac428dce7700a5c3b41fe
Patch0:		unique_ptr.patch
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	libarchive-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ark is a graphical file compression/decompression utility with support
for multiple formats, including tar, gzip, bzip2, rar and zip, as well
as CD-ROM images. Ark can be used to browse, extract, create, and
modify archives.

%prep
%setup -q -n %{kaname}-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/ark.categories
%attr(755,root,root) %{_bindir}/ark
%ghost %{_libdir}/libkerfuffle.so.18
%{_libdir}/libkerfuffle.so.18.*.*
%{_libdir}/qt5/plugins/arkpart.so
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
%dir %{_datadir}/kxmlgui5/ark
%{_datadir}/kxmlgui5/ark/ark_viewer.rc
%{_datadir}/metainfo/org.kde.ark.appdata.xml
