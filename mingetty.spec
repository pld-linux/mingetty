Summary:     a compact, console-only getty
Summary(de): ein kompaktes, auf Konsolen beschränktes GETTY 
Summary(fr): getty compact, uniquement pour la console
Summary(pl): Ma³y getty - tylko na konsolê (minimal getty)
Summary(tr): Ufak bir getty
Name:        mingetty
Version:     0.9.4
Copyright:   GPL
Release:     9
Group:       Utilities/System
Source:      ftp://jurix.jura.uni-sb.de/pub/linux/source/system/daemons/%{name}-%{version}.tar.gz
Patch0:      %{name}-%{version}-make.patch
Patch1:      %{name}-%{version}-glibc.patch
Patch2:      %{name}-%{version}-isprint.patch
Patch3:      %{name}-%{version}-wtmplock.patch
Buildroot:   /tmp/%{name}-%{version}-root

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
%patch0 -p0 -b .make
%patch1 -p1 -b .glibc
%patch2 -p1 -b .isprint
%patch3 -p1 -b .wtmplock

%build
make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/man/man8,sbin}
install -s mingetty $RPM_BUILD_ROOT/sbin
install *.8 $RPM_BUILD_ROOT/usr/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc ANNOUNCE 
%attr(755, root, root) /sbin/mingetty
%attr(644, root, man) /usr/man/man8/mingetty.8

%changelog
* Tue Oct 06 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
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
