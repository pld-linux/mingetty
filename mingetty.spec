# TODO:
# -fix patches 1, 2 and 3
Summary:	A compact, console-only getty
Summary(de):	Ein kompaktes, auf Konsolen beschränktes GETTY
Summary(es):	Un getty compacto, que sólo funciona en la consola
Summary(fr):	getty compact, uniquement pour la console
Summary(pl):	Ma³y getty - tylko na konsolê (minimal getty)
Summary(pt_BR):	Um getty compacto, que só funciona na console
Summary(tr):	Ufak bir getty
Name:		mingetty
Version:	1.07
License:	GPL
Release:	0.1
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	72e4bce381908556ede9c3f959d1ca7a
Patch0:		%{name}-utf8.patch
Patch1:		%{name}-defaultlogin.patch
Patch2:		%{name}-mono-console.patch
Patch3:		%{name}-remote.patch
URL:		http://sourceforge.net/projects/mingetty
Requires:	login
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_sbindir	/sbin

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

%build
%{__make} \
	OPT="%{rpmcflags}" \
	CC="%{__cc}"

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
