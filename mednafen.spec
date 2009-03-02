Summary:	Multi-game-system emulator using OpenGL
Summary(pl.UTF-8):	Wieloplatformowy emulator gier używający OpenGL
Name:		mednafen
Version:	0.8.B
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/mednafen/%{name}-%{version}.tar.bz2
# Source0-md5:	d1aab33cbb5d4e585724c19177f0f02f
URL:		http://mednafen.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libcdio-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mednafen is a portable, utilizing OpenGL and SDL,
argument(command-line)-driven multi-system emulator with many advanced
features. The Atari Lynx, GameBoy (Color), GameBoy Advance, NES, PC
Engine(TurboGrafx 16), SuperGrafx, Neo Geo Pocket (Color), PC-FX, and
WonderSwan (Color) are emulated.

%description -l pl.UTF-8
Mednafen jest wieloplatformowym emulatorem przenośnym, używającym
OpenGL i SDL, działającym z linii poleceń i posiadającym wiele
zaawansowanych cech. Emulowane platformy to: Atari Lynx, GameBoy
(Color), GameBoy Advance, NES, PC Engine(TurboGrafx 16), SuperGrafx,
Neo Geo Pocket (Color), PC-FX, oraz WonderSwan (Color).

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/mednafen
