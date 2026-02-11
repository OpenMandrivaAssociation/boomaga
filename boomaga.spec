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
Patch1:		https://github.com/Boomaga/boomaga/pull/124.patch

BuildSystem:	cmake
BuildOption:	-Wno-dev
BuildOption:	-DCUPS_SERVERBIN_DIR=%{_libdir}/cups
BuildOption:	-DCUPS_BACKEND_DIR=%{_libdir}/cups/backend
BuildOption:	-DCUPS_FILTER_DIR=%{_libdir}/cups/filter
BuildOption:	-DCUPS_PPD_DIR=%{_datadir}/ppd/boomaga
BuildRequires:	qmake5
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(poppler-cpp)

Requires:       poppler

%description
%{summary}.

Boomaga (BOOklet MAnager GA) is a virtual printer daemon for viewing a document before printing it out using the physical printer.

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
