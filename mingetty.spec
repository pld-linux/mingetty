Summary:	a compact, console-only getty
Summary(de):	ein kompaktes, auf Konsolen beschränktes GETTY 
Summary(fr):	getty compact, uniquement pour la console
Summary(pl):	Ma³y getty - tylko na konsolê (minimal getty)
Summary(tr):	Ufak bir getty
Name:		mingetty
Version:	0.9.4
Copyright:	GPL
Release:	11
Group:		Utilities/System
Group(pl):	Narzêdzia/System
URL:		ftp://jurix.jura.uni-sb.de/pub/linux/source/system/daemons
Source:		%{name}-%{version}.tar.gz
Patch0:		mingetty-misc.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
mingetty, by Florian La Roche, is a lightweight, minimalist getty for
use on virtual consoles only.  mingetty is not suitable for serial
lines (the author recommends using `mgetty' for that purpose).

%description -l de
mingetty von Florian La Roche ist ein kleiner, minimalistischer getty
für die Verwendung an virtuellen Konsolen. Er ist nicht für serielle
Leitungen geeignet (der Autor empfiehlt für diesen Zweck`mgetty').

%description -l fr
mingetty, de Florian La Roche, est un getty réduit et allégé pour
console virtuelle uniquement. mingetty n'est pas adapté pour les lignes
série (l'auteur recommande d'utiliser `mgetty' pour cet usage). 

%description -l pl 
Mingetty - Floriana La Roche, jest minimalnym getty do u¿ytku na wirtualnej
konsoli. Mingetty nie obs³uguje portów szeregowych.

%description -l tr
Bu pakette seri baðlantý üzerinden sisteme giriþe olanak veren, akýllý bir
getty sürümü bulunur. Otomatik arama ve faks desteði içerir (saðladýðý fax
desteðinin tam olarak kullanýlabilmesi için mgetty-sendfax paketi gerekir).

%prep
%setup -q
%patch0 -p1

%build
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/share/man/man8,sbin}
install -s mingetty $RPM_BUILD_ROOT/sbin

install *.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE.gz

%attr(755,root,root) /sbin/mingetty

%{_mandir}/man8/*

%changelog
* Mon Jun 07 1999 Jan Rêkorajski <baggins@pld.org.pl>
  [0.9.4-10]
- spec cleanup

* Fri Apr  9 1999 Piotr Czerwiñski <pius@pld.org.pl>
- added Group(pl),
- fixed passing $RPM_OPT_FLAGS during compile,
- gzipping documentation and man pages,
- removed man group from man pages,
- cosmetic changes for common l&f.

* Tue Oct 06 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.9.4-8]
- added pl translation,
- minor modifications of the spec file.
