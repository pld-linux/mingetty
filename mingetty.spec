Summary:	A compact, console-only getty
Summary(de.UTF-8):	Ein kompaktes, auf Konsolen beschränktes GETTY
Summary(es.UTF-8):	Un getty compacto, que sólo funciona en la consola
Summary(fr.UTF-8):	getty compact, uniquement pour la console
Summary(pl.UTF-8):	Mały getty - tylko na konsolę (minimal getty)
Summary(pt_BR.UTF-8):	Um getty compacto, que só funciona na console
Summary(tr.UTF-8):	Ufak bir getty
Name:		mingetty
Version:	1.07
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/mingetty/%{name}-%{version}.tar.gz
# Source0-md5:	72e4bce381908556ede9c3f959d1ca7a
Patch0:		%{name}-utf8.patch
Patch1:		%{name}-mono-console.patch
Patch2:		%{name}-defaultlogin.patch
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

%description -l de.UTF-8
mingetty von Florian La Roche ist ein kleiner, minimalistischer getty
für die Verwendung an virtuellen Konsolen. Er ist nicht für serielle
Leitungen geeignet (der Autor empfiehlt für diesen Zweck`mgetty').

%description -l es.UTF-8
mingetty, de Florian La Roche, es un ligero y pequeño getty para usar
solamente en pantallas virtuales. Mingetty no es apropiado para líneas
seriales (el autor recomienda el uso de "mgetty" para este propósito.

%description -l fr.UTF-8
mingetty, de Florian La Roche, est un getty réduit et allégé pour
console virtuelle uniquement. mingetty n'est pas adapté pour les
lignes série (l'auteur recommande d'utiliser `mgetty' pour cet usage).

%description -l pl.UTF-8
Mingetty - Floriana La Roche, jest minimalnym getty do użytku na
wirtualnej konsoli. Mingetty nie obsługuje portów szeregowych.

%description -l pt_BR.UTF-8
mingetty, de Florian La Roche, é um leve e pequeno getty para usar
somente em consoles virtuais. Mingetty não é apropriado para linhas
seriais (o autor recomenda o uso de "mgetty" para este propósito.

%description -l tr.UTF-8
Bu pakette seri bağlantı üzerinden sisteme girişe olanak veren, akıllı
bir getty sürümü bulunur. Otomatik arama ve faks desteği içerir
(sağladığı fax desteğinin tam olarak kullanılabilmesi için
mgetty-sendfax paketi gerekir).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -W -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man8,%{_sbindir}}

install mingetty $RPM_BUILD_ROOT%{_sbindir}

install *.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/mingetty
%{_mandir}/man8/*
