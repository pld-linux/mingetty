Summary:	a compact, console-only getty
Summary(de):	ein kompaktes, auf Konsolen beschr�nktes GETTY 
Summary(fr):	getty compact, uniquement pour la console
Summary(pl):	Ma�y getty - tylko na konsol� (minimal getty)
Summary(tr):	Ufak bir getty
Name:		mingetty
Version:	0.9.4
Release:	12
License:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source0:	ftp://jurix.jura.uni-sb.de/pub/linux/source/system/daemons/%{name}-%{version}.tar.gz
Patch0:		mingetty-misc.patch
Patch1:		mingetty-current-time.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
mingetty, by Florian La Roche, is a lightweight, minimalist getty for
use on virtual consoles only. mingetty is not suitable for serial
lines (the author recommends using `mgetty' for that purpose).

%description -l de
mingetty von Florian La Roche ist ein kleiner, minimalistischer getty
f�r die Verwendung an virtuellen Konsolen. Er ist nicht f�r serielle
Leitungen geeignet (der Autor empfiehlt f�r diesen Zweck`mgetty').

%description -l fr
mingetty, de Florian La Roche, est un getty r�duit et all�g� pour
console virtuelle uniquement. mingetty n'est pas adapt� pour les
lignes s�rie (l'auteur recommande d'utiliser `mgetty' pour cet usage).

%description -l pl 
Mingetty - Floriana La Roche, jest minimalnym getty do u�ytku na
wirtualnej konsoli. Mingetty nie obs�uguje port�w szeregowych.

%description -l tr
Bu pakette seri ba�lant� �zerinden sisteme giri�e olanak veren, ak�ll�
bir getty s�r�m� bulunur. Otomatik arama ve faks deste�i i�erir
(sa�lad��� fax deste�inin tam olarak kullan�labilmesi i�in
mgetty-sendfax paketi gerekir).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man8,%{_sbindir}}
install -s mingetty $RPM_BUILD_ROOT%{_sbindir}

install *.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE.gz

%attr(755,root,root) %{_sbindir}/mingetty

%{_mandir}/man8/*
