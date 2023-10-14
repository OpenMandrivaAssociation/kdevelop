%define compile_apidox 0
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

# We cannot do it when debug is set to nil like in 2012.1
%if %unstable
#define dont_strip 1
%endif

%define libname_orig libkdevplatform4
%define major   5
%define libname %mklibname kdevplatform %{major}
%define old_major 2
%define old_libname %mklibname kdevplatform4 %{old_major}
%define dev_clang_major 512
%define __requires_exclude /bin/zsh

Summary:	Integrated Development Environment for C++/C
Name:		kdevelop
Version:	23.08.2
Release:	1
Epoch:		4
Group:		Development/C++
License:	GPLv2
Url:		http://www.kdevelop.org/
Source0:	https://download.kde.org/%([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)/release-service/%{version}/src/kdevelop-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
Patch1:		kdevplatform-5.0.3-bsdtar.patch
Patch2:		kdevelop-23.03.90-clang16.patch
BuildRequires:	qt5-assistant
BuildRequires:	boost-devel
BuildRequires:	bash-completion
BuildRequires:	pkgconfig(bash-completion)
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
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Runner)
BuildRequires:	cmake(OktetaKastenControllers)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	cmake(KDevelop-PG-Qt)
BuildRequires:	cmake(KF5SysGuard)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(Grantlee5)
BuildRequires:	libkomparediff2-kf5-devel
BuildRequires:	cmake(KDEExperimentalPurpose)
BuildRequires:	llvm-devel
BuildRequires:	llvm-static-devel
BuildRequires:	spirv-llvm-translator
BuildRequires:	llvm-bolt
BuildRequires:	libclc-amdgcn
BuildRequires:	libclc-nvptx
BuildRequires:	clang-devel
BuildRequires:	shared-mime-info
BuildRequires:	subversion-devel
BuildRequires:	astyle-devel
BuildRequires:	meson
BuildRequires:	clazy
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	pkgconfig(libxml-2.0)
%if %{compile_apidox}
BuildRequires:	doxygen
%endif
Requires:	cmake
Requires:	git
Requires:	gdb
Requires:	kdevplatform >= %{EVRD}
Recommends:	meson
Recommends:	clazy
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
%{_bindir}/%{name}*
%{_bindir}/kdev_includepathsconverter
%{_datadir}/applications/*.desktop
%{_datadir}/qlogging-categories5/kdevelop.categories
%{_datadir}/mime/packages/kdev*.xml
%{_libdir}/libKDevCMakeCommon.so.%{dev_clang_major}
%{_libdir}/libKDevClangPrivate.so.%{dev_clang_major}
%{_libdir}/libKDevCompileAnalyzerCommon.so.%{dev_clang_major}
%{_libdir}/qt5/plugins/kdevplatform
%{_kde5_iconsdir}/hicolor/*/apps/%{name}.png
%{_kde5_iconsdir}/hicolor/*/apps/kdevgh.png
%{_kde5_iconsdir}/hicolor/*/apps/cmake.png
%{_kde5_iconsdir}/hicolor/*/apps/cppcheck.png
%{_kde5_iconsdir}/hicolor/*/apps/github-*.png
%{_kde5_iconsdir}/hicolor/*/apps/clazy.png
%{_kde5_iconsdir}/hicolor/*/apps/qtlogo.svg
%{_kde5_iconsdir}/hicolor/scalable/apps/kdevelop.svg
%{_datadir}/kdevqmljssupport
%{_datadir}/kdevelop
%{_datadir}/kdevfiletemplates
%{_datadir}/kdevcodegen
%{_datadir}/kdevgdb
%{_datadir}/kdevlldb
%{_datadir}/kdevappwizard
%{_datadir}/kdevmanpage
%{_datadir}/kdevclangsupport
%{_datadir}/knotifications5/kdevelop.notifyrc
%{_datadir}/metainfo/org.kde.kdevelop.appdata.xml
%{_datadir}/knsrcfiles/kdevappwizard.knsrc
%{_datadir}/knsrcfiles/kdevelop-qthelp.knsrc
%{_datadir}/knsrcfiles/kdevfiletemplates.knsrc
%{_libdir}/libKDevelopSessionsWatch.so
%{_libdir}/qt5/plugins/kf5/krunner/krunner_kdevelopsessions.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kdevelopsessions/libkdevelopsessionsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kdevelopsessions/qmldir
%{_datadir}/bash-completion/completions/kdevelop
# Exclude kdevplatform folders
%exclude %{_kde5_datadir}/kdevplatform/
%exclude %{_kde5_datadir}/kdevcodegen/
%exclude %{_kde5_datadir}/kdevcodeutils/

#------------------------------------------------
%package -n plasma-dataengine-kdevelopsessions
Summary:	Show KDevelop sessions
Group:		Graphical desktop/KDE
Requires:	%{name} >= %{EVRD}

%description -n plasma-dataengine-kdevelopsessions
Show KDevelop sessions.

%files -n plasma-dataengine-kdevelopsessions
#{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_kdevelopsessions.so

#------------------------------------------------
%package -n plasma-applet-kdevelopsessions
Summary:	Show KDevelop sessions
Group:		Graphical desktop/KDE
Requires:	plasma-dataengine-kdevelopsessions >= %{EVRD}

%description -n plasma-applet-kdevelopsessions
Show KDevelop sessions.

%files -n plasma-applet-kdevelopsessions
#{_libdir}/qt5/plugins/krunner_kdevelopsessions.so
%{_datadir}/kservices5/*kdevelopsessions.desktop
%{_datadir}/plasma/plasmoids/kdevelopsessions
#{_datadir}/plasma/services/*.operations

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
%package -n kdevplatform
Summary:	Files for kdevplatform
Group:		Development/KDE and Qt
Obsoletes:      kdevplatform4

%description -n kdevplatform
Kdevelop platform tools.

%files -n kdevplatform 
%{_bindir}/kdev_dbus_socket_transformer
%{_bindir}/kdev_format_source
%{_bindir}/kdevplatform_shell_environment.sh
%{_datadir}/kdevcodegen
%{_datadir}/kdevcodeutils
%{_datadir}/kdevplatform
%{_datadir}/qlogging-categories5/kdevplatform.categories
%{_iconsdir}/hicolor/*/apps/subversion.*
%{_iconsdir}/hicolor/*/apps/bazaar.png
%{_iconsdir}/hicolor/*/apps/git.*
%{_iconsdir}/hicolor/*/actions/breakpoint.*
%{_libdir}/qt5/plugins/grantlee/*/kdev_filters.so
%{_libdir}/qt5/qml/org/kde/kdevplatform/libkdevelopdashboarddeclarativeplugin.so
%{_libdir}/qt5/qml/org/kde/kdevplatform/qmldir
%{_datadir}/kservicetypes5/kdevelopplugin.desktop
%dir %{_qt5_plugindir}/kdevplatform

#-----------------------------------------------------------------------------

%define kdevplatforminterfaces_major 58
%define libkdevplatforminterfaces %mklibname KDevPlatformInterfaces %{kdevplatforminterfaces_major}

%package -n %{libkdevplatforminterfaces}
Summary:        KF5 library
Group:          System/Libraries

%description -n %{libkdevplatforminterfaces}
KF5 library.

%files -n %{libkdevplatforminterfaces}
%{_libdir}/libKDevPlatformInterfaces.so.*

#-----------------------------------------------------------------------------

%define kdevplatformlanguage_major 58
%define libkdevplatformlanguage %mklibname KDevPlatformLanguage %{kdevplatformlanguage_major}

%package -n %{libkdevplatformlanguage}
Summary:        KF5 library
Group:          System/Libraries

%description -n %{libkdevplatformlanguage}
KF5 library.

%files -n %{libkdevplatformlanguage}
%{_libdir}/libKDevPlatformLanguage.so.*

#-----------------------------------------------------------------------------

%define kdevplatformoutputview_major 58
%define libkdevplatformoutputview %mklibname KDevPlatformOutputView %{kdevplatformoutputview_major}

%package -n %{libkdevplatformoutputview}
Summary:        KF5 library
Group:          System/Libraries

%description -n %{libkdevplatformoutputview}
KF5 library.

%files -n %{libkdevplatformoutputview}
%{_libdir}/libKDevPlatformOutputView.so.*

#-----------------------------------------------------------------------------

%define kdevplatformproject_major 58
%define libkdevplatformproject %mklibname KDevPlatformProject %{kdevplatformproject_major}

%package -n %{libkdevplatformproject}
Summary:        KF5 library
Group:          System/Libraries

%description -n %{libkdevplatformproject}
KF5 library.

%files -n %{libkdevplatformproject}
%{_libdir}/libKDevPlatformProject.so.*

#-----------------------------------------------------------------------------

%define kdevplatformshell_major 58
%define libkdevplatformshell %mklibname KDevPlatformShell %{kdevplatformshell_major}

%package -n %{libkdevplatformshell}
Summary:        KF5 library
Group:          System/Libraries

%description -n %{libkdevplatformshell}
KF5 library.

%files -n %{libkdevplatformshell}
%{_libdir}/libKDevPlatformShell.so.*

#-----------------------------------------------------------------------------

%define kdevplatformutil_major 58
%define libkdevplatformutil %mklibname KDevPlatformUtil %{kdevplatformutil_major}

%package -n %{libkdevplatformutil}
Summary:        KF5 library
Group:          System/Libraries

%description -n %{libkdevplatformutil}
KF5 library.

%files -n %{libkdevplatformutil}
%{_libdir}/libKDevPlatformUtil.so.*

#-----------------------------------------------------------------------------

%define kdevplatformvcs_major 58
%define libkdevplatformvcs %mklibname KDevplatformVcs %{kdevplatformvcs_major}

%package -n %{libkdevplatformvcs}
Summary:        KF5 library
Group:          System/Libraries

%description -n %{libkdevplatformvcs}
KF5 library.

%files -n %{libkdevplatformvcs}
%{_libdir}/libKDevPlatformVcs.so.*

#-----------------------------------------------------------------------------

%define sublime_major 58
%define libsublime %mklibname KDevPlatformSublime %{sublime_major}

%package -n %{libsublime}
Summary:        KF5 library
Group: System/Libraries

%description -n %{libsublime}
KF5 library.

%files -n %{libsublime}
%{_libdir}/libKDevPlatformSublime.so.*

#-----------------------------------------------------------------------------

%define kdevplatformdebugger_major 58
%define libkdevplatformdebugger %mklibname KDevPlatformDebugger %{kdevplatformdebugger_major}

%package -n %{libkdevplatformdebugger}
Summary:        KF5 library
Group:          System/Libraries

%description -n %{libkdevplatformdebugger}
KF5 library.

%files -n %{libkdevplatformdebugger}
%{_libdir}/libKDevPlatformDebugger.so.*

#-----------------------------------------------------------------------------

%define kdevplatformdocumentation_major 58
%define libkdevplatformdocumentation %mklibname KDevPlatformDocumentation %{kdevplatformdocumentation_major}

%package -n %{libkdevplatformdocumentation}
Summary:        KF5 library
Group:          System/Libraries

%description -n %{libkdevplatformdocumentation}
KF5 library.

%files -n %{libkdevplatformdocumentation}
%{_libdir}/libKDevPlatformDocumentation.so.*

#-----------------------------------------------------------------------------

%define kdevplatformserialization_major 58
%define libkdevplatformserialization %mklibname KDevPlatformSerialization %kdevplatformserialization_major

%package -n %libkdevplatformserialization
Summary: KF5 library
Group: System/Libraries

%description -n %libkdevplatformserialization
KF5 library.

%files -n %libkdevplatformserialization
%_libdir/libKDevPlatformSerialization.so.*

#-----------------------------------------------------------------------------

%package -n %{libname}-devel
Summary:        Development files for kdevplatform
Group:          Development/KDE and Qt

Provides:       kdevplatform-devel = %{EVRD}

Requires:       %{libkdevplatforminterfaces} = %{EVRD}
Requires:       %{libkdevplatformlanguage} = %{EVRD}
Requires:       %{libkdevplatformoutputview} = %{EVRD}
Requires:       %{libkdevplatformproject} = %{EVRD}
Requires:       %{libkdevplatformshell} = %{EVRD}
Requires:       %{libkdevplatformutil} = %{EVRD}
Requires:       %{libkdevplatformvcs} = %{EVRD}
Requires:       %{libsublime} = %{EVRD}
Requires:       %{libkdevplatformdebugger} = %{EVRD}
Requires:       %{libkdevplatformdocumentation} = %{EVRD}
Requires:       %{libkdevplatformserialization} = %{EVRD}

%description -n %{libname}-devel
Development files for kdevplatform.

%files -n %{libname}-devel
%{_libdir}/cmake/KDevPlatform
%{_includedir}/kdevplatform
%{_libdir}/libKDevPlatformSerialization.so
%{_libdir}/libKDevPlatformInterfaces.so
%{_libdir}/libKDevPlatformLanguage.so
%{_libdir}/libKDevPlatformOutputView.so
%{_libdir}/libKDevPlatformProject.so
%{_libdir}/libKDevPlatformShell.so
%{_libdir}/libKDevPlatformUtil.so
%{_libdir}/libKDevPlatformVcs.so
%{_libdir}/libKDevPlatformSublime.so
%{_libdir}/libKDevPlatformDebugger.so
%{_libdir}/libKDevPlatformDocumentation.so

#-----------------------------------------------------------------------------


%prep
%setup -qn kdevelop-%{version}
%autopatch -p1

%build
%cmake_kde5 -DBUILD_TESTING=OFF -DBSDTAR=1
%ninja

%if %{compile_apidox}
make apidox
%endif

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-html
