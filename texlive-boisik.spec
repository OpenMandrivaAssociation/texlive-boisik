# revision 15878
# category Package
# catalog-ctan /fonts/boisik
# catalog-date 2009-08-23 18:29:20 +0200
# catalog-license gpl2
# catalog-version 0.5
Name:		texlive-boisik
Version:	0.5
Release:	2
Summary:	A font inspired by Baskerville design
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/boisik
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boisik.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boisik.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Boisik is a serif font (inspired by the Baskerville typeface),
written in MetaFont. It comprises roman and italic text fonts
and maths fonts. LaTeX support is offered for use with OT1, IL2
and OM* encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/boisik/bskarr10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskarrows.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskbase.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskex10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskext.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskhc10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bski10-TS1.mf
%{_texmfdistdir}/fonts/source/public/boisik/bski10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskib10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskiol10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskital.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskiu10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskiub10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskletters-i.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskletters-o.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskletters-r.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskligtab-i.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskligtab-sc.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskligtab.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsklist-T1.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsklist-TS1.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsklist-ar.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsklist-bb.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsklist-ex.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsklist-lc.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsklist-ma.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsklist-mi-up.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsklist-mi.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsklist-ms.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsklist-sc.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsklist-sy.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsklist-uc.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskma10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskmab10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskmath.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskmathma.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskmathms.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskmathsy.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskmi10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskmib10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskms10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskmsb10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskmsbsl10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskmssl10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskr10-T1.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskr10-TS1.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskr10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskrb10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskrc10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskrcb10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskrf10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskrl10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskrol10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskroman.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskrsb10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskrsl10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bskrw10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsksc.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsksc10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsksy10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsksyb10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsksybsl10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsksymbols.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsksyol10.mf
%{_texmfdistdir}/fonts/source/public/boisik/bsksysl10.mf
%{_texmfdistdir}/fonts/tfm/public/boisik/bskarr10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskex10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskhc10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bski10-TS1.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bski10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskib10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskiol10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskiu10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskiub10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskma10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskmab10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskmib10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskms10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskmsb10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskmsbsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskmssl10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskr10-T1.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskr10-TS1.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskr10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskrb10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskrc10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskrcb10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskrf10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskrl10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskrol10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskrsb10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskrsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bskrw10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bsksc10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bsksy10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bsksyol10.tfm
%{_texmfdistdir}/fonts/tfm/public/boisik/bsksysl10.tfm
%{_texmfdistdir}/tex/latex/boisik/boisik.sty
%{_texmfdistdir}/tex/latex/boisik/il2bsk.fd
%{_texmfdistdir}/tex/latex/boisik/il2bskf.fd
%{_texmfdistdir}/tex/latex/boisik/lblbskm.fd
%{_texmfdistdir}/tex/latex/boisik/lblcmr.fd
%{_texmfdistdir}/tex/latex/boisik/lblenc.def
%{_texmfdistdir}/tex/latex/boisik/lbmbsk.fd
%{_texmfdistdir}/tex/latex/boisik/lbmbskms.fd
%{_texmfdistdir}/tex/latex/boisik/lbmcmr.fd
%{_texmfdistdir}/tex/latex/boisik/lbmenc.def
%{_texmfdistdir}/tex/latex/boisik/lbsbsk.fd
%{_texmfdistdir}/tex/latex/boisik/lbsbsksy.fd
%{_texmfdistdir}/tex/latex/boisik/lbscmr.fd
%{_texmfdistdir}/tex/latex/boisik/lbsenc.def
%{_texmfdistdir}/tex/latex/boisik/ot1bsk.fd
%{_texmfdistdir}/tex/latex/boisik/ot1bskf.fd
%{_texmfdistdir}/tex/latex/boisik/ts1bsk.fd
%{_texmfdistdir}/tex/latex/boisik/ubskex.fd
%doc %{_texmfdistdir}/doc/fonts/boisik/README
%doc %{_texmfdistdir}/doc/fonts/boisik/example/boisik-idiot.pdf
%doc %{_texmfdistdir}/doc/fonts/boisik/example/boisik-idiot.tex
%doc %{_texmfdistdir}/doc/fonts/boisik/example/boisik.pdf
%doc %{_texmfdistdir}/doc/fonts/boisik/example/boisik.tex
%doc %{_texmfdistdir}/doc/fonts/boisik/example/bskrlogo10.mf
%doc %{_texmfdistdir}/doc/fonts/boisik/example/table.pdf
%doc %{_texmfdistdir}/doc/fonts/boisik/example/table.tex
%doc %{_texmfdistdir}/doc/fonts/boisik/example/testfont.pdf
%doc %{_texmfdistdir}/doc/fonts/boisik/example/testfont.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
