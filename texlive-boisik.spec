%global tl_name boisik
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	A font inspired by Baskerville design
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/boisik
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boisik.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boisik.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Boisik is a serif font set (inspired by the Baskerville typeface),
written in Metafont. The set comprises roman and italic text fonts and
maths fonts. LaTeX support is offered for use with OT1, IL2 and OM*
encodings.

