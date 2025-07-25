Summary:	PostScript to text converter
Summary(pl.UTF-8):	Konwerter PostScriptu do czystego tekstu
Name:		pstotext
Version:	1.9
Release:	2
License:	Digital's paranoid but open-source license
Group:		Applications/Text
Source0:	ftp://mirror.cs.wisc.edu/pub/mirrors/ghost/contrib/%{name}-%{version}.tar.gz
# Source0-md5:	64576e8a10ff5514e285d98b3898ae78
#Source0:	http://www.research.compaq.com/SRC/virtualpaper/binaries/%{name}.tar.Z
Patch0:		pstotext-dsafer.patch
URL:		http://www.research.compaq.com/SRC/virtualpaper/pstotext.html
Requires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility reads in postscript files and outputs an ASCII rendering.
While the rendering is not always accurate, it is often sufficient.

%description -l pl.UTF-8
To narzędzie czyta pliki PostScript i produkuje odpowiednik ASCII.
Efekt nie zawsze jest idealny, ale zazwyczaj wystarczający.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install pstotext $RPM_BUILD_ROOT%{_bindir}/pstotext
install pstotext.1 $RPM_BUILD_ROOT%{_mandir}/man1/pstotext.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc pstotext.txt
%attr(755,root,root) %{_bindir}/pstotext
%{_mandir}/man1/pstotext.1*
