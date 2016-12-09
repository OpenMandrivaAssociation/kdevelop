%define compile_apidox 0
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

# We cannot do it when debug is set to nil like in 2012.1
%if %unstable
#define dont_strip 1
%endif

%define kdevplatform_version 4:1.%(echo %{version} | cut -d. -f2,3)

Summary:	Integrated Development Environment for C++/C
Name:		kdevelop
Version:	5.0.3
Release:	1
Epoch:		4
Group:		Development/C++
License:	GPLv2
Url:		http://www.kdevelop.org/
Source0:	http://download.kde.org/stable/kdevelop/%{version}/src/kdevelop-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
BuildRequires:	qt5-assistant
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Crash)
BuildRequires:  cmake(KF5Runner)

BuildRequires:	cmake(OktetaKastenControllers)

BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Help)

BuildRequires:  cmake(KDevelop-PG-Qt)
BuildRequires:  cmake(KF5SysGuard)
BuildRequires:	cmake(KF5Plasma)

BuildRequires:	clang-devel
BuildRequires:  kdevplatform-devel
BuildRequires:	shared-mime-info

%if %{compile_apidox}
BuildRequires:	doxygen
%endif
Requires:	cmake
Requires:	git
Requires:	gdb
Requires:	kdevplatform >= %{kdevplatform_version}
%rename	kdevelop4

%description
The KDevelop Integrated Development Environment provides many features that
developers need as well as providing a unified interface to programs like gdb,
the C/C++ compiler, and make.

KDevelop manages or provides:
   * All development tools needed for C++ programming like Compiler, Linker,
     automake and autoconf
   * KAppWizard, which generates complete, ready-to-go sample applications
   * Classgenerator, for creating new classes and integrating them into the
     current project
   * File management for sources, headers, documentation etc. to be included in
     the project
   * The creation of User-Handbooks written with SGML and the automatic
     generation of HTML-output with the KDE look and feel
   * Automatic HTML-based API-documentation for your project's classes with
     cross-references to the used libraries; Internationalization support for
     your application, allowing translators to easily add their target language
     to a project
   * WYSIWYG (What you see is what you get) creation of user interfaces with a
     built-in dialog editor
   * Debugging your application by integrating KDbg
   * Editing of project-specific pixmaps with KIconEdit
   * The inclusion of any other program you need for development by adding it
     to the "Tools" menu according to your individual needs.

%files -f %{name}.lang
%{_bindir}/*
%{_iconsdir}/*/*/*/*
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/kdevelop.xml
%{_libdir}/libkdevcmakecommon.so
%{_libdir}/libKDevClangPrivate.so.25
%{_libdir}/qt5/plugins/kdevplatform
%{_datadir}/kdevqmljssupport
%{_datadir}/kdevelop
%{_datadir}/kdevfiletemplates
%{_datadir}/kdevcodegen
%{_datadir}/kdevgdb
%{_datadir}/kdevappwizard
%{_datadir}/kdevmanpage
%{_datadir}/kdevclangsupport
%{_datadir}/kdevqmakebuilder
%{_datadir}/knotifications5/kdevelop.notifyrc
%{_datadir}/metainfo/org.kde.kdevelop.appdata.xml
%{_datadir}/mime/packages/kdevelopinternal.xml

#------------------------------------------------
%package -n plasma-dataengine-kdevelopsessions
Summary:	Show KDevelop sessions
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Requires:	%{name} >= %{EVRD}

%description -n plasma-dataengine-kdevelopsessions
Show KDevelop sessions.

%files -n plasma-dataengine-kdevelopsessions
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_kdevelopsessions.so

#------------------------------------------------
%package -n plasma-applet-kdevelopsessions
Summary:	Show KDevelop sessions
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Requires:	plasma-dataengine-kdevelopsessions >= %{EVRD}
BuildArch:	noarch

%description -n plasma-applet-kdevelopsessions
Show KDevelop sessions.

%files -n plasma-applet-kdevelopsessions
%{_libdir}/qt5/plugins/krunner_kdevelopsessions.so
%{_datadir}/kservices5/*kdevelopsessions.desktop
%{_datadir}/plasma/plasmoids/kdevelopsessions
%{_datadir}/plasma/services/*.operations

#------------------------------------------------
%package devel
Summary:	Development files for kdevelop
Group:		Development/KDE and Qt

%description devel
Development files for kdevelop.

%files devel
%{_libdir}/cmake/KDevelop
%{_includedir}/kdevelop

#------------------------------------------------

%prep
%setup -qn kdevelop-%{version}

%build
%cmake_kde5 -DBSDTAR=1
%ninja

%if %{compile_apidox}
make apidox
%endif

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-html

