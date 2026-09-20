Name:		boomaga
Version:	3.7.0
Release:	1
Summary:	Virtual printer for viewing a document before printing it out using the physical printer
License:	GPL-2.0-only AND LGPL-2.1-only
Group:		Publishing
URL:		https://www.boomaga.org/
Source0:	https://github.com/Boomaga/boomaga/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	cmake
BuildOption:	-Wno-dev
BuildOption:	-DCUPS_SERVERBIN_DIR=%{_libdir}/cups
BuildOption:	-DCUPS_BACKEND_DIR=%{_libdir}/cups/backend
BuildOption:	-DCUPS_FILTER_DIR=%{_libdir}/cups/filter
BuildOption:	-DCUPS_PPD_DIR=%{_datadir}/ppd/boomaga
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(cups)
BuildRequires:	pkgconfig(poppler-cpp)

Requires:	poppler

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
