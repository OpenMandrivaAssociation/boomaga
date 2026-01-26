Name:           boomaga
Version:        3.0.0
Release:        3
Summary:        Virtual printer for viewing a document before printing it out using the physical printer
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Publishing
URL:            https://www.boomaga.org/
Source0:        https://github.com/Boomaga/boomaga/archive/v%{version}/%{name}-%{version}.tar.gz
# Patch backported from upstream PR#108 for compatibility with newer ghostscript
Patch0:         boomaga-ghostscript-9.54.patch

BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconfig(poppler)
BuildRequires:  lib64cups-devel
BuildRequires:  qt5-linguist-tools
BuildRequires:  pkgconfig(poppler-cpp)

#Requires:       qt5-qtbase
Requires:       poppler

%description
%{summary}.

Boomaga (BOOklet MAnager GA) is a virtual printer daemon for viewing a document before printing it out using the physical printer.

%prep
%autosetup -p1 -n boomaga-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -Wno-dev \
    -DCUPS_SERVERBIN_DIR=%{_libdir}/cups \
    -DCUPS_BACKEND_DIR=%{_libdir}/cups/backend \
    -DCUPS_FILTER_DIR=%{_libdir}/cups/filter \
    -DCUPS_PPD_DIR=%{_datadir}/ppd/boomaga \
    -DLIB_SUFFIX=64 \   # if CMake supports it (common in projects with ${LIB_SUFFIX})

%make_build

%install
%make_install -C build

%files
%license COPYING GPL LGPL
%doc README*
%{_bindir}/boomaga
%{_libdir}/cups/backend/boomaga
%{_datadir}/applications/boomaga.desktop
%{_datadir}/boomaga/
%{_datadir}/dbus-1/services/org.boomaga.service
%{_datadir}/icons/hicolor/*/apps/boomaga.*
%{_datadir}/mime/packages/boomaga.xml
%{_datadir}/ppd/boomaga/
%{_mandir}/man1/boomaga.1*

%changelog
