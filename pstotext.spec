Summary:	PostScript to text converter
Summary(pl):	Konwerter PostScriptu do czystego tekstu
Name:		pstotext
Version:	1.8g
Release:	1
License:	Digital's paranoid but open-source license
Group:		Applications/Text
Source0:	http://www.research.digital.com/SRC/virtualpaper/binaries/%{name}.tar.Z
URL:		http://www.research.digital.com/SRC/virtualpaper/pstotext.html
Requires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility reads in postscript files and outputs an ASCII rendering.
While the rendering is not always accurate, it is often sufficient.

%description -l pl
To narzędzie czyta pliki PostScript i produkuje odpowiednik ASCII.
Efekt nie zawsze jest idealny, ale zazwyczaj wystarczający.

%prep
%setup -q -n %{name}

%build
%{__make} CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install pstotext $RPM_BUILD_ROOT%{_bindir}/pstotext
install pstotext.1 $RPM_BUILD_ROOT%{_mandir}/man1/pstotext.1

gzip -9nf pstotext.txt

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/pstotext
%{_mandir}/man1/pstotext.1*

%clean
rm -rf $RPM_BUILD_ROOT
