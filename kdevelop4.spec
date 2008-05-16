%define compile_apidox 1
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

Name: 		kdevelop4
Summary: 	Integrated Development Environment for C++/C
Version:        4.0.74
Release:        %mkrel 1
Epoch:          3
URL:            http://www.kde.org 
Source:         ftp://ftp.kde.org/pub/kde/stable/%version/src/kdevelop-%version.tar.bz2
Source1:        c_cpp_reference-2.0.2.tar.bz2
Group: 		Development/C++
BuildRoot:	%_tmppath/%name-%version-%release-root
License:        GPL
BuildRequires:  kdelibs4-devel >= %version
BuildRequires:  kdevplatform4-devel >= %version
BuildRequires:  jpeg-devel
BuildRequires:  png-devel 
BuildRequires:  X11-devel
BuildRequires:  libart_lgpl-devel
BuildRequires:  flex
BuildRequires:  graphviz
BuildRequires:  db-devel
BuildRequires:  subversion-devel
BuildRequires:  apr-devel
BuildRequires:  apr-util-devel
%if %compile_apidox
BuildRequires:  doxygen
%endif
%py_requires -d

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
Requires:      libz-devel
Requires:      ctags
Requires:      png-devel libart_lgpl-devel libtool
Requires:      cmake
Requires:      awk
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Conflicts:     mandrake-mime <= 0.4-5mdk

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

%post
%{update_desktop_database}
%update_icon_cache crystalsvg


%postun
%{clean_desktop_database}
%clean_icon_cache crystalsvg

%files
%defattr(-,root,root) 
%{_kde_bindir}/kdev_includepathresolver
%{_kde_bindir}/kdevelop
%{_kde_bindir}/qmake-parser
%{_kde_datadir}/kde4/services/*.desktop
%dir %{_kde_appsdir}/kdevappwizard
%{_kde_appsdir}/kdevappwizard/kdevappwizard.rc
%dir %{_kde_appsdir}/kdevappwizard/templates
%{_kde_appsdir}/kdevappwizard/templates/qmake_qt4guiapp.tar.bz2
%dir %{_kde_appsdir}/kdevcmakebuilder
%{_kde_appsdir}/kdevcmakebuilder/data.kdev4
%dir %{_kde_appsdir}/kdevcmakemanager
%{_kde_appsdir}/kdevcmakemanager/data.kdev4
%dir %{_kde_appsdir}/kdevcustommakemanager
%{_kde_appsdir}/kdevcustommakemanager/kdevcustommakemanager.rc
%dir %{_kde_appsdir}/kdevdocumentview
%{_kde_appsdir}/kdevdocumentview/kdevdocumentview.rc
%dir %{_kde_appsdir}/kdevelop
%{_kde_appsdir}/kdevelop/kdevelop.notifyrc
%{_kde_appsdir}/kdevelop/kdevelopui.rc
%dir %{_kde_appsdir}/kdevelop/pics
%{_kde_appsdir}/kdevelop/pics/*.png
%dir %{_kde_appsdir}/kdevgrepview
%{_kde_appsdir}/kdevgrepview/kdevgrepview.rc
%dir %{_kde_appsdir}/kdevcppdebugger
%{_kde_appsdir}/kdevcppdebugger/kdevcppdebuggerui.rc
%dir %{_kde_appsdir}/kdevcppsupport
%{_kde_appsdir}/kdevcppsupport/kdevcppsupport.rc
%dir %{_kde_appsdir}/kdevqtdesigner
%{_kde_appsdir}/kdevqtdesigner/kdevqtdesigner.rc
%dir %{_kde_appsdir}/kdevvalgrind
%{_kde_appsdir}/kdevvalgrind/kdevvalgrind.rc      
%dir %{_kde_appsdir}/kdevplatform
%dir %{_kde_appsdir}/kdevplatform/profiles
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/AdaIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/AdaIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/CandCppIDE
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/CandCppIDE/CIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/CandCppIDE/CIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/CandCppIDE/CppIDE
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/CandCppIDE/CppIDE/KDECppIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/CandCppIDE/CppIDE/KDECppIDE/profile.config
%{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/CandCppIDE/CppIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/CandCppIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/CandCppIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/FortranIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/FortranIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/HaskellIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/HaskellIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/JavaIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/JavaIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/PascalIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/PascalIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/CompiledLanguageIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/DatabaseIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/DatabaseIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/ScriptingLanguageIDE/PHPIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/ScriptingLanguageIDE/PHPIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/ScriptingLanguageIDE/PerlIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/ScriptingLanguageIDE/PerlIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/ScriptingLanguageIDE/PythonIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/ScriptingLanguageIDE/PythonIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/ScriptingLanguageIDE/RubyIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/ScriptingLanguageIDE/RubyIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/ScriptingLanguageIDE/ShellIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/ScriptingLanguageIDE/ShellIDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/IDE/ScriptingLanguageIDE
%{_kde_appsdir}/kdevplatform/profiles/IDE/ScriptingLanguageIDE/profile.config
%{_kde_appsdir}/kdevplatform/profiles/IDE/profile.config
%dir %{_kde_appsdir}/kdevplatform/profiles/KDevAssistant
%{_kde_appsdir}/kdevplatform/profiles/KDevAssistant/profile.config
%{_kde_appsdir}/kdevplatform/profiles/profile.config
%dir %{_kde_appsdir}/kdevqmakebuilder
%{_kde_appsdir}/kdevqmakebuilder/data.kdev4
%dir %{_kde_datadir}/config
%{_kde_datadir}/config/kdeveloprc
%{_kde_iconsdir}/hicolor/*/*/*.png
%{_kde_libdir}/kde4/kcm_kdev_makebuilder.so
%{_kde_libdir}/kde4/kcm_kdev_qmakebuilder.so
%{_kde_libdir}/kde4/kcm_kdevcmake_settings.so
%{_kde_libdir}/kde4/kdevappwizard.so
%{_kde_libdir}/kde4/kdevcmakebuilder.so
%{_kde_libdir}/kde4/kdevcmakemanager.so
%{_kde_libdir}/kde4/kdevcpplanguagesupport.so
%{_kde_libdir}/kde4/kdevcustommakemanager.so
%{_kde_libdir}/kde4/kdevdocumentview.so
%{_kde_libdir}/kde4/kdevgrepview.so
%{_kde_libdir}/kde4/kdevmakebuilder.so
%{_kde_libdir}/kde4/kdevqmakebuilder.so
%{_kde_libdir}/kde4/kdevqmakemanager.so
%{_kde_libdir}/kde4/kcm_kdev_cppdebugger.so
%{_kde_libdir}/kde4/kdevcppdebugger.so
%{_kde_libdir}/libkdev4cmakecommon.so
%{_kde_libdir}/libkdev4cppduchain.so
%{_kde_libdir}/libkdev4cppparser.so
%{_kde_libdir}/libkdev4cpprpp.so
%{_kde_libdir}/libkdev4qmakeparser.so
%{_kde_libdir}/kde4/kcm_kdev_valgrindsettings.so
%{_kde_libdir}/kde4/kdevqtdesigner.so
%{_kde_libdir}/kde4/kdevvalgrind.so
%{_kde_libdir}/libkdev4qmakeduchain.so

#------------------------------------------------

%package devel
Summary: Development files for kdevelop
Group: Development/KDE and Qt

Obsoletes: %lib_name-devel < 3.96.1

%description devel
Development files for kdevelop.

%files devel
%defattr(-,root,root)
%{_kde_appsdir}/cmake/modules/FindKDevelop.cmake
%{_kde_appsdir}/cmake/modules/KDevelopMacros.cmake
%{_kde_includedir}/kdevelop/cmake/icmakebuilder.h
%{_kde_includedir}/kdevelop/make/imakebuilder.h
%{_kde_includedir}/kdevelop/qmake/iqmakebuilder.h

#------------------------------------------------

%package doc
Summary: Development files for kdevelop
Group: Development/KDE and Qt

%description doc
Documentation kdevelop.

%files doc
%defattr(-,root,root)

#------------------------------------------------

%prep
%setup -q -n kdevelop-%version

%build

%cmake_kde4

%make


%if %compile_apidox
#make apidox
%endif

%install
rm -fr %buildroot

cd $RPM_BUILD_DIR/kdevelop-%version
cd build

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot



