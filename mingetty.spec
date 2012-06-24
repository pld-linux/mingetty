Summary:	a compact, console-only getty
Summary(de):	ein kompaktes, auf Konsolen beschr�nktes GETTY 
Summary(fr):	getty compact, uniquement pour la console
Summary(pl):	Ma�y getty - tylko na konsol� (minimal getty)
Summary(tr):	Ufak bir getty
Name:		mingetty
Version:	0.9.4
Copyright:	GPL
Release:	9
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source:		ftp://jurix.jura.uni-sb.de/pub/linux/source/system/daemons/%{name}-%{version}.tar.gz
Patch0:		mingetty-make.patch
Patch1:		mingetty-glibc.patch
Patch2:		mingetty-isprint.patch
Patch3:		mingetty-wtmplock.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
mingetty, by Florian La Roche, is a lightweight, minimalist getty for
use on virtual consoles only.  mingetty is not suitable for serial
lines (the author recommends using `mgetty' for that purpose).

%description -l de
mingetty von Florian La Roche ist ein kleiner, minimalistischer getty
f�r die Verwendung an virtuellen Konsolen. Er ist nicht f�r serielle
Leitungen geeignet (der Autor empfiehlt f�r diesen Zweck`mgetty').

%description -l fr
mingetty, de Florian La Roche, est un getty r�duit et all�g� pour
console virtuelle uniquement. mingetty n'est pas adapt� pour les lignes
s�rie (l'auteur recommande d'utiliser `mgetty' pour cet usage). 

%description -l pl 
Mingetty - Floriana La Roche, jest minimalnym getty do u�ytku na wirtualnej
konsoli. Mingetty nie obs�uguje port�w szeregowych.

%description -l tr
Bu pakette seri ba�lant� �zerinden sisteme giri�e olanak veren, ak�ll� bir
getty s�r�m� bulunur. Otomatik arama ve faks deste�i i�erir (sa�lad��� fax
deste�inin tam olarak kullan�labilmesi i�in mgetty-sendfax paketi gerekir).

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .glibc
%patch2 -p1 -b .isprint
%patch3 -p1 -b .wtmplock

%build
make RPM_OPTS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/man/man8,sbin}
install -s mingetty $RPM_BUILD_ROOT/sbin
install *.8 $RPM_BUILD_ROOT/usr/man/man8

gzip -9nf $RPM_BUILD_ROOT/usr/man/man8/* \
	ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE.gz
%attr(755,root,root) /sbin/mingetty
/usr/man/man8/*

%changelog
* Fri Apr  9 1999 Piotr Czerwi�ski <pius@pld.org.pl>
- added Group(pl),
- fixed passing $RPM_OPT_FLAGS during compile,
- gzipping documentation and man pages,
- removed man group from man pages,
- cosmetic changes for common l&f.

* Tue Oct 06 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [0.9.4-8]
- added pl translation,
- minor modifications of the spec file.

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- fixed build problems on intel and alpha for manhattan

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
