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
Name:		kdevelop4
Version:	4.7.1
Release:	1
Epoch:		4
Group:		Development/C++
License:	GPLv2
Url:		http://www.kdevelop.org/
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/kdevelop/%{version}/src/kdevelop-%{version}.tar.xz
Source1:	%{name}.rpmlintrc

BuildRequires:	kdelibs4-devel
BuildRequires:	kdevplatform4-devel >= %{kdevplatform_version}
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	okteta-devel
%if %{compile_apidox}
BuildRequires:	doxygen
%endif
Requires:	cmake
Requires:	git
Requires:	gdb
Requires:	kdevplatform4 >= %{kdevplatform_version}
Suggests:	plasma-applet-kdevelopsessions

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
%{_kde_bindir}/*
%{_kde_services}/kcm_kdev*.desktop
%{_kde_services}/kdev*.desktop
%{_kde_appsdir}/kdevgdb
%{_kde_appsdir}/kdevappwizard
%{_kde_appsdir}/kdevcustommakemanager
%{_kde_appsdir}/kdevcppsupport
%{_kde_appsdir}/kdevelop
%{_kde_appsdir}/kdevokteta
%{_kde_appsdir}/kdevfiletemplates
%{_kde_appsdir}/kdevcodegen
%{_kde_applicationsdir}/*.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_datadir}/config/kdeveloprc
%{_kde_datadir}/config/kdevelop-qthelp.knsrc
%{_kde_datadir}/mime/packages/kdevelop.xml
%{_kde_libdir}/kde4/kcm_kdev_makebuilder.so
%{_kde_libdir}/kde4/kcm_kdev_ninjabuilder.so
%{_kde_libdir}/kde4/kcm_kdevcmake_settings.so
%{_kde_libdir}/kde4/kcm_kdev_cmakebuilder.so
%{_kde_libdir}/kde4/kcm_kdevcustombuildsystem.so
%{_kde_libdir}/kde4/kdevastyle.so
%{_kde_libdir}/kde4/kdevcmakebuilder.so
%{_kde_libdir}/kde4/kdevcmakedocumentation.so
%{_kde_libdir}/kde4/kdevcmakemanager.so
%{_kde_libdir}/kde4/kdevcpplanguagesupport.so
%{_kde_libdir}/kde4/kdevcustombuildsystem.so
%{_kde_libdir}/kde4/kdevcustommakemanager.so
%{_kde_libdir}/kde4/kdevexecuteplasmoid.so
%{_kde_libdir}/kde4/kdevgdb.so
%{_kde_libdir}/kde4/kdevghprovider.so
%{_kde_libdir}/kde4/kdevkdeprovider.so
%{_kde_libdir}/kde4/kdevmakebuilder.so
%{_kde_libdir}/kde4/kdevmanpage.so
%{_kde_libdir}/kde4/kdevninja.so
%{_kde_libdir}/kde4/kdevokteta.so
%{_kde_libdir}/kde4/kdevqthelp.so
%{_kde_libdir}/kde4/kdevqthelp_config.so
%{_kde_libdir}/kde4/kdevcustomscript.so
%{_kde_libdir}/kde4/krunner_kdevelopsessions.so
%{_kde_libdir}/libkdev4cmakecommon.so
%{_kde_libdir}/libkdev4cpprpp.so
%{_kde_libdir}/libkdev4cppduchain.so
%{_kde_libdir}/libkdev4cppparser.so
%{_kde_libdir}/kde4/kcm_kdevcustomdefinesandincludes.so
%{_kde_libdir}/kde4/kdevdefinesandincludesmanager.so
%{_kde_libdir}/libkdevcompilerprovider.so
%{_datadir}/apps/kdevmanpage/manpagedocumentation.css

#------------------------------------------------
%package -n plasma-dataengine-kdevelopsessions
Summary:	Show KDevelop sessions
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Requires:	%{name} >= %{EVRD}

%description -n plasma-dataengine-kdevelopsessions
Show KDevelop sessions.

%files -n plasma-dataengine-kdevelopsessions
%{_kde_libdir}/kde4/plasma_engine_kdevelopsessions.so
%{_kde_services}/plasma-dataengine-kdevelopsessions.desktop
%{_kde_appsdir}/plasma/services/org.kde.plasma.dataengine.kdevelopsessions.operations

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
%{_kde_services}/plasma-applet-kdevelopsessions.desktop
%{_kde_appsdir}/plasma/plasmoids/kdevelopsessions

#------------------------------------------------
%package devel
Summary:	Development files for kdevelop
Group:		Development/KDE and Qt

%description devel
Development files for kdevelop.

%files devel
%{_kde_appsdir}/cmake/modules/FindKDevelop.cmake
%{_kde_includedir}/kdevelop

#------------------------------------------------

%prep
%setup -qn kdevelop-%{version}

%build
%cmake_kde4
%make

%if %{compile_apidox}
make apidox
%endif

%install
%makeinstall_std -C build

%find_lang %{name} --all-name --with-html

