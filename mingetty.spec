Summary:	a compact, console-only getty
Summary(de):	ein kompaktes, auf Konsolen beschränktes GETTY 
Summary(fr):	getty compact, uniquement pour la console
Summary(pl):	Ma³y getty - tylko na konsolê (minimal getty)
Summary(tr):	Ufak bir getty
Name:		mingetty
Version:	0.9.4
License:	GPL
Release:	18
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://jurix.jura.uni-sb.de/pub/linux/source/system/daemons/%{name}-%{version}.tar.gz
Patch0:		%{name}-misc.patch
Patch1:		%{name}-current-time.patch
Patch2:		%{name}-mono-console.patch
Patch3:		%{name}-remote.patch
Patch4:		%{name}-fgetc.patch
Patch5:		%{name}-autologin.patch
Patch6:		%{name}-autologin-remove-restrictions.patch
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

%description -l fr
mingetty, de Florian La Roche, est un getty réduit et allégé pour
console virtuelle uniquement. mingetty n'est pas adapté pour les
lignes série (l'auteur recommande d'utiliser `mgetty' pour cet usage).

%description -l pl 
Mingetty - Floriana La Roche, jest minimalnym getty do u¿ytku na
wirtualnej konsoli. Mingetty nie obs³uguje portów szeregowych.

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

%build
%{__make} OPT="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man8,%{_sbindir}}

install mingetty $RPM_BUILD_ROOT%{_sbindir}

install *.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE.gz

%attr(755,root,root) %{_sbindir}/mingetty

%{_mandir}/man8/*
