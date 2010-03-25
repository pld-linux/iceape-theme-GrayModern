%define		_realname	graymodern
%define		_snap		2007-06-18_sea1.1
Summary:	Theme like Modern, only gray
Summary(pl.UTF-8):	Motyw identyczny jak Modern, tylko że szary
Name:		iceape-theme-GrayModern
Version:	2007.06.18
Release:	2
License:	GPL
Group:		X11/Applications/Networking
#Source0:	http://mozilla-themes.schellen.net/%{_realname}_%{_snap}.jar
# version with non-free logos replaced
Source0:	%{_realname}_%{_snap}.jar
# Source0-md5:	d464a95d4923aab870312d4409b88fb5
Source1:	gen-installed-chrome.sh
URL:		http://mozilla-themes.schellen.net/
BuildRequires:	perl-base
BuildRequires:	unzip
Requires(post,postun):	iceape >= 1.1
Requires(post,postun):	textutils
Requires:	iceape >= 1.1
Obsoletes:	seamonkey-theme-GrayModern
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/iceape/chrome

%description
Theme for Iceape, like Modern only gray.

%description -l pl.UTF-8
Motyw dla Iceape, identyczny jak Modern, tylko że szary.

%prep
%setup -q -c -T
install %{SOURCE0} %{_realname}.jar
install %{SOURCE1} .
./gen-installed-chrome.sh skin %{_realname}.jar > %{_realname}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}
install %{_realname}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
	%{_sbindir}/iceape-chrome+xpcom-generate
fi

%postun
[ ! -x %{_sbindir}/iceape-chrome+xpcom-generate ] || %{_sbindir}/iceape-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
