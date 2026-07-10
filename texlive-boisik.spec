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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Boisik is a serif font set (inspired by the Baskerville typeface),
written in Metafont. The set comprises roman and italic text fonts and
maths fonts. LaTeX support is offered for use with OT1, IL2 and OM*
encodings.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/boisik
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/tex/latex/boisik
%dir %{_datadir}/texmf-dist/doc/fonts/boisik/example
%dir %{_datadir}/texmf-dist/fonts/source/public/boisik
%dir %{_datadir}/texmf-dist/fonts/tfm/public/boisik
%doc %{_datadir}/texmf-dist/doc/fonts/boisik/README
%doc %{_datadir}/texmf-dist/doc/fonts/boisik/example/boisik-idiot.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/boisik/example/boisik-idiot.tex
%doc %{_datadir}/texmf-dist/doc/fonts/boisik/example/boisik.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/boisik/example/boisik.tex
%doc %{_datadir}/texmf-dist/doc/fonts/boisik/example/bskrlogo10.mf
%doc %{_datadir}/texmf-dist/doc/fonts/boisik/example/table.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/boisik/example/table.tex
%doc %{_datadir}/texmf-dist/doc/fonts/boisik/example/testfont.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/boisik/example/testfont.tex
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskarr10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskarrows.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskbase.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskex10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskext.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskhc10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bski10-TS1.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bski10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskib10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskiol10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskital.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskiu10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskiub10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskletters-i.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskletters-o.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskletters-r.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskligtab-i.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskligtab-sc.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskligtab.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsklist-T1.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsklist-TS1.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsklist-ar.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsklist-bb.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsklist-ex.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsklist-lc.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsklist-ma.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsklist-mi-up.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsklist-mi.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsklist-ms.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsklist-sc.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsklist-sy.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsklist-uc.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskma10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskmab10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskmath.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskmathma.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskmathms.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskmathsy.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskmi10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskmib10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskms10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskmsb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskmsbsl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskmssl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskr10-T1.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskr10-TS1.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskr10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskrb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskrc10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskrcb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskrf10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskrl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskrol10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskroman.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskrsb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskrsl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bskrw10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsksc.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsksc10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsksy10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsksyb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsksybsl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsksymbols.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsksyol10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/boisik/bsksysl10.mf
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskarr10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskex10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskhc10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bski10-TS1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bski10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskib10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskiol10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskiu10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskiub10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskma10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskmab10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskmi10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskmib10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskms10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskmsb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskmsbsl10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskmssl10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskr10-T1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskr10-TS1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskr10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskrb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskrc10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskrcb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskrf10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskrl10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskrol10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskrsb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskrsl10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bskrw10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bsksc10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bsksy10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bsksyol10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boisik/bsksysl10.tfm
%{_datadir}/texmf-dist/tex/latex/boisik/boisik.sty
%{_datadir}/texmf-dist/tex/latex/boisik/il2bsk.fd
%{_datadir}/texmf-dist/tex/latex/boisik/il2bskf.fd
%{_datadir}/texmf-dist/tex/latex/boisik/lblbskm.fd
%{_datadir}/texmf-dist/tex/latex/boisik/lblcmr.fd
%{_datadir}/texmf-dist/tex/latex/boisik/lblenc.def
%{_datadir}/texmf-dist/tex/latex/boisik/lbmbsk.fd
%{_datadir}/texmf-dist/tex/latex/boisik/lbmbskms.fd
%{_datadir}/texmf-dist/tex/latex/boisik/lbmcmr.fd
%{_datadir}/texmf-dist/tex/latex/boisik/lbmenc.def
%{_datadir}/texmf-dist/tex/latex/boisik/lbsbsk.fd
%{_datadir}/texmf-dist/tex/latex/boisik/lbsbsksy.fd
%{_datadir}/texmf-dist/tex/latex/boisik/lbscmr.fd
%{_datadir}/texmf-dist/tex/latex/boisik/lbsenc.def
%{_datadir}/texmf-dist/tex/latex/boisik/ot1bsk.fd
%{_datadir}/texmf-dist/tex/latex/boisik/ot1bskf.fd
%{_datadir}/texmf-dist/tex/latex/boisik/ts1bsk.fd
%{_datadir}/texmf-dist/tex/latex/boisik/ubskex.fd
