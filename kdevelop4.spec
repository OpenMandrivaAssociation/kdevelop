%define compile_apidox 0
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%if %unstable
%define dont_strip 1
%endif

%define lib_name_orig libkdevelop4
%define lib_major 3
%define lib_name %mklibname kdevelop4 %lib_major
%define old_lib_major 2
%define old_lib_name %mklibname kdevelop4 %old_lib_major

Name: 		    kdevelop4
Summary: 	    Integrated Development Environment for C++/C
Version:        4.4.0
Release:        1
Epoch:          4
URL:            http://www.kdevelop.org/
Source:		http://fr2.rpmfind.net/linux/KDE/stable/kdevelop/%{version}/src/kdevelop-%{version}.tar.bz2
Group: 		    Development/C++
BuildRoot:	    %_tmppath/%name-%version-%release-root
License:        GPL
BuildRequires:  kdelibs4-devel >= 2:4.5.0
BuildRequires:  kdevplatform4-devel >= 4:1.4.0
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	kdesdk4-devel >= 1:4.5.71
%if %compile_apidox
BuildRequires:  doxygen
%endif
Requires:      enscript 
Requires:      gcc-c++ 
Requires:      gcc-cpp 
Requires:      openssl-devel
Requires:      libx11-devel
Requires:      jpeg-devel 
Requires:      qt4-devel >= 4.2
Requires:      make 
Requires:      perl 
Requires:      sgml-tools 
Requires:      gettext 
Requires:      zlib-devel
Requires:      ctags
Requires:      png-devel libart_lgpl-devel libtool
Requires:      cmake
Requires:      awk
Requires:      git
Requires:      kdevplatform4 >= 4:1.1.80
Conflicts:     mandrake-mime <= 0.4-5mdk
Obsoletes:     kdevelop <= 4:3.5.3-2
Obsoletes:     %{_lib}kdevelop3 <= 4:3.5.3-2

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

%files -f %name.lang
%defattr(-,root,root) 
%{_kde_bindir}/kdevelop
%{_kde_bindir}/kdevelop!
%{_kde_services}/*.desktop
%{_kde_appsdir}/kdevcmakebuilder
%{_kde_appsdir}/kdevgdb
%{_kde_appsdir}/kdevcmakemanager
%{_kde_appsdir}/kdevappwizard
%{_kde_appsdir}/kdevcustommakemanager
%{_kde_appsdir}/kdevcppsupport
%{_kde_appsdir}/kdevelop
%{_kde_appsdir}/kdevokteta
%{_kde_appsdir}/plasma/plasmoids/kdevelopsessions
%{_kde_appsdir}/plasma/services/org.kde.plasma.dataengine.kdevelopsessions.operations
%{_kde_datadir}/applications/kde4/kdevelop.desktop
%{_kde_datadir}/applications/kde4/kdevelop_ps.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_datadir}/config/kdeveloprc
%{_kde_datadir}/config/kdevelop-qthelp.knsrc
%{_kde_datadir}/mime/packages/kdevelop.xml
%{_kde_libdir}/kde4/kcm_kdev_makebuilder.so
%{_kde_libdir}/kde4/kcm_kdevcmake_settings.so
%{_kde_libdir}/kde4/kdevastyle.so
%{_kde_libdir}/kde4/kdevcmakebuilder.so
%{_kde_libdir}/kde4/kdevcmakedocumentation.so
%{_kde_libdir}/kde4/kdevcmakemanager.so
%{_kde_libdir}/kde4/kdevcpplanguagesupport.so
%{_kde_libdir}/kde4/kdevcustommakemanager.so
%{_kde_libdir}/kde4/kdevcustomscript.so
%{_kde_libdir}/kde4/krunner_kdevelopsessions.so
%{_kde_libdir}/kde4/kdevgdb.so
%{_kde_libdir}/kde4/kdevkdeprovider.so
%{_kde_libdir}/kde4/kdevmakebuilder.so
%{_kde_libdir}/kde4/kdevmanpage.so
%{_kde_libdir}/kde4/kdevokteta.so
%{_kde_libdir}/kde4/kdevqthelp.so
%{_kde_libdir}/kde4/kdevqthelp_config.so
%{_kde_libdir}/kde4/plasma_engine_kdevelopsessions.so
%{_kde_libdir}/libkdev4cmakecommon.so
%{_kde_libdir}/libkdev4cpprpp.so
%{_kde_libdir}/libkdev4cppduchain.so
%{_kde_libdir}/libkdev4cppparser.so

#------------------------------------------------

%package devel
Summary: Development files for kdevelop
Group: Development/KDE and Qt

Obsoletes: %lib_name-devel < 3.96.1
Obsoletes: %{_lib}kdevelop-devel <= 4:3.5.3-2

%description devel
Development files for kdevelop.

%files devel
%defattr(-,root,root)
%{_kde_appsdir}/cmake/modules/FindKDevelop.cmake
%{_kde_includedir}/kdevelop

#------------------------------------------------

%package doc
Summary: Development files for kdevelop
Group: Development/KDE and Qt
Obsoletes: kdevelop-doc <= 4:3.5.3-2

%description doc
Documentation kdevelop.

%files doc
%defattr(-,root,root)

#------------------------------------------------

%prep
%setup -q -n kdevelop-%{version}

%build
%cmake_kde4
%make

%if %compile_apidox
make apidox
%endif

%install
rm -fr %buildroot
%makeinstall_std -C build

%find_lang %name --all-name --with-kde 


%clean
rm -fr %buildroot
