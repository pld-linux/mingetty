Summary:	A compact, console-only getty
Summary(de):	Ein kompaktes, auf Konsolen beschränktes GETTY
Summary(es):	Un getty compacto, que sólo funciona en la consola
Summary(fr):	getty compact, uniquement pour la console
Summary(pl):	Ma³y getty - tylko na konsolê (minimal getty)
Summary(pt_BR):	Um getty compacto, que só funciona na console
Summary(tr):	Ufak bir getty
Name:		mingetty
Version:	0.9.4
License:	GPL
Release:	20
Group:		Applications/System
Source0:	ftp://jurix.jura.uni-sb.de/pub/linux/source/system/daemons/%{name}-%{version}.tar.gz
# Source0-md5: 2366883ee2253c7116b2ee0d9aafbb06
Patch0:		%{name}-misc.patch
Patch1:		%{name}-current-time.patch
Patch2:		%{name}-mono-console.patch
Patch3:		%{name}-remote.patch
Patch4:		%{name}-fgetc.patch
Patch5:		%{name}-autologin.patch
Patch6:		%{name}-autologin-remove-restrictions.patch
Patch7:		%{name}-syslog.patch
Patch8:		%{name}-manpage.patch
Patch9:		%{name}-s390.patch
Requires:	login
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
mingetty, by Florian La Roche, is a lightweight, minimalist getty for
use on virtual consoles only. mingetty is not suitable for serial
lines (the author recommends using `mgetty' for that purpose).

%description -l de
mingetty von Florian La Roche ist ein kleiner, minimalistischer getty
für die Verwendung an virtuellen Konsolen. Er ist nicht für serielle
Leitungen geeignet (der Autor empfiehlt für diesen Zweck`mgetty').

%description -l es
mingetty, de Florian La Roche, es un ligero y pequeño getty para usar
solamente en pantallas virtuales. Mingetty no es apropiado para líneas
seriales (el autor recomienda el uso de "mgetty" para este propósito.

%description -l fr
mingetty, de Florian La Roche, est un getty réduit et allégé pour
console virtuelle uniquement. mingetty n'est pas adapté pour les
lignes série (l'auteur recommande d'utiliser `mgetty' pour cet usage).

%description -l pl
Mingetty - Floriana La Roche, jest minimalnym getty do u¿ytku na
wirtualnej konsoli. Mingetty nie obs³uguje portów szeregowych.

%description -l pt_BR
mingetty, de Florian La Roche, é um leve e pequeno getty para usar
somente em consoles virtuais. Mingetty não é apropriado para linhas
seriais (o autor recomenda o uso de "mgetty" para este propósito.

%description -l tr
Bu pakette seri baðlantý üzerinden sisteme giriþe olanak veren, akýllý
bir getty sürümü bulunur. Otomatik arama ve faks desteði içerir
(saðladýðý fax desteðinin tam olarak kullanýlabilmesi için
mgetty-sendfax paketi gerekir).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
%{__make} OPT="%{rpmcflags}" CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man8,%{_sbindir}}

install mingetty $RPM_BUILD_ROOT%{_sbindir}

install *.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE
%attr(755,root,root) %{_sbindir}/mingetty
%{_mandir}/man8/*
