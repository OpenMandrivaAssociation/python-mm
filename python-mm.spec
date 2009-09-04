%define pkgname mmpython

Summary: Python Media Meta Data retrieval framework
Name: python-mm
Version: 0.4.10
Release: %mkrel 5
Source0: http://mesh.dl.sourceforge.net/sourceforge/mmpython/%{pkgname}-%{version}.tar.bz2
License: LGPL
URL: http://sourceforge.net/projects/mmpython/
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: python-devel
BuildRequires: libdvdread-devel

%description
MMPython is a Media Meta Data retrieval framework. 
It retrieves metadata from mp3, ogg, avi, jpg, tiff and 
other file formats. Among others it thereby parses ID3v2, 
ID3v1, EXIF, IPTC and Vorbis data into an object oriented 
struture.

%prep
%setup -q -n %{pkgname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)


