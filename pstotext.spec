# TODO
# - security http://security.gentoo.org/glsa/glsa-200507-29.xml
Summary:	PostScript to text converter
Summary(pl):	Konwerter PostScriptu do czystego tekstu
Name:		pstotext
Version:	1.8g
Release:	2
License:	Digital's paranoid but open-source license
Group:		Applications/Text
Source0:	http://www.research.compaq.com/SRC/virtualpaper/binaries/%{name}.tar.Z
# Source0-md5:	1be0be028ccc85be1bf55d7e90976b18
URL:		http://www.research.compaq.com/SRC/virtualpaper/pstotext.html
Requires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility reads in postscript files and outputs an ASCII rendering.
While the rendering is not always accurate, it is often sufficient.

%description -l pl
To narzêdzie czyta pliki PostScript i produkuje odpowiednik ASCII.
Efekt nie zawsze jest idealny, ale zazwyczaj wystarczaj±cy.

%prep
%setup -q -n %{name}

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
