# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/

%define branch_date 20070418

%define use_enable_final 1
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

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
Version: 	3.80.3
Release: 	%mkrel 0.%branch_date.3
Epoch: 3
URL: http://www.kde.org 
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdevelop-%version-%branch_date.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdevelop-%version.tar.bz2
%endif
Source1: c_cpp_reference-2.0.2.tar.bz2
Source2: kdevelop-3.0-Makefile.PL
Patch0: kdevelop-3.2.1-stdcppfix.patch
Group: 		Development/C++
BuildRoot:	%_tmppath/%name-%version-%release-root
License: GPL
%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release
BuildRequires: libjpeg-devel
BuildRequires: png-devel 
BuildRequires:	X11-devel
BuildRequires: libart_lgpl-devel
BuildRequires: flex
BuildRequires: graphviz
BuildRequires: db-devel
BuildRequires: subversion-devel
BuildRequires: apr-devel
BuildRequires: apr-util-devel
%if %compile_apidox
#BuildRequires: doxygen
%endif
%py_requires -d

Requires: enscript 
Requires: gcc-c++ 
Requires: gcc-cpp 
Requires: openssl-devel
#why kdeutils is required ?
#Requires: kdegraphics4 kdelibs4-devel kdesdk4  kdeutils4
Requires: libx11-devel
Requires: jpeg-devel 
Requires: qt4-devel >= 4.2
Requires: make 
Requires: perl 
Requires: sgml-tools 
Requires: gettext 
Requires: libz-devel
#Requires: kdbg  
Requires: ctags
Requires: png-devel libart_lgpl-devel libtool
Requires: cmake
Requires: awk
Requires: %lib_name = %epoch:%version-%release
#Requires: graphviz
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Conflicts: mandrake-mime <= 0.4-5mdk

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
   * The inclusion of any other program you need for development by adding it to
     the "Tools" menu according to your individual needs.

%post
%{update_desktop_database}
%update_icon_cache crystalsvg


%postun
%{clean_desktop_database}
%clean_icon_cache crystalsvg

%files
%defattr(-,root,root) 
%_bindir/*
%_libdir/kde4/*
%_datadir/apps/*
%_datadir/icons/*/*/*/*
%_datadir/config/kdeveloprc
%_datadir/kde4/services/*
%_datadir/kde4/servicetypes/*
#%_datadir/config/kdevassistantrc
%exclude %_datadir/apps/cmake/modules/KDevelopMacros.cmake

#------------------------------------------------

%package -n %lib_name-devel
Summary: Development files for kdevelop
Group: Development/KDE and Qt

Provides: kdevelop4-devel = %epoch:%version-%release
Requires: %lib_name = %epoch:%version-%release

%description -n %lib_name-devel
Development files for kdevelop.

%files -n %lib_name-devel
%defattr(-,root,root)
%_libdir/*.so
%dir %_includedir/kdevelop
%_includedir/*/*
%_datadir/apps/cmake/modules/KDevelopMacros.cmake


#------------------------------------------------

%package -n %lib_name
Summary: Libraries files for kdevelop
Group: Development/KDE and Qt
Obsoletes: %old_lib_name
Provides: %lib_name_orig = %epoch:%version-%release

%description -n %lib_name
Libraries files for kdevelop.

%post -n %lib_name-devel -p /sbin/ldconfig
%postun -n %lib_name-devel -p /sbin/ldconfig

%post -n %lib_name -p /sbin/ldconfig
%postun -n %lib_name -p /sbin/ldconfig

%files -n %lib_name
%defattr(-,root,root)
%_libdir/*.so.*


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
%setup -q -nkdevelop-%version-%branch_date

%build

cd $RPM_BUILD_DIR/kdevelop-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make


%if %compile_apidox
#make apidox
%endif

%install
rm -fr %buildroot

cd $RPM_BUILD_DIR/kdevelop-%version-%branch_date
cd build

make DESTDIR=%buildroot install



# Create LMDK menus
install -d %buildroot/%_datadir/applications/kde/

#Create LMDK menu entries
for kdev in kdevelop kdevdesigner kdevassistant kdevelop_c_cpp kdevelop_kde_cpp kdevelop_ruby kdevelop_scripting; do
	mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde/${kdev}.desktop  "More Applications/Development/Development Environments" 
done

(
cd $RPM_BUILD_DIR/%name-%version/
rm -rf perl-kdevelop
mkdir perl-kdevelop/
cd perl-kdevelop/
install -m 0755 %SOURCE2 Makefile.PL
ln ../parts/appwizard/common/kdevelop.pm kdevelop.pm
perl Makefile.PL INSTALLDIRS=vendor
make install DESTDIR=%buildroot
)

%clean
rm -fr %buildroot



